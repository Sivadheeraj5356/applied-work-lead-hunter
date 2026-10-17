"""
Standalone Local SMTP Email Verifier with Catch-All Detection
Enforces Applied Work Zero-Bounce Deliverability Policy.
"""

import sys
import re
import socket
import smtplib
import subprocess
import json
import uuid
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

import functools

@functools.lru_cache(maxsize=2048)
def resolve_mx_records(domain):
    """Resolves DNS MX records using dnspython or fallback."""
    try:
        import dns.resolver
        answers = dns.resolver.resolve(domain, 'MX', lifetime=4)
        sorted_answers = sorted(answers, key=lambda r: r.preference)
        return [str(r.exchange).rstrip('.') for r in sorted_answers]
    except Exception:
        pass
    
    try:
        cmd = ['powershell', '-NoProfile', '-Command', 
               f"(Resolve-DnsName -Type MX {domain} -ErrorAction SilentlyContinue | Sort-Object Preference).NameExchange"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=3)
        mx_records = [line.strip().rstrip('.') for line in res.stdout.strip().splitlines() if line.strip()]
        if mx_records:
            return mx_records
    except Exception:
        pass
    
    return [domain]

def verify_single_email(email, from_addr="verify@appliedwork.ai", check_catchall=True, timeout=8):
    email = email.strip()
    match = EMAIL_REGEX.search(email)
    if not match:
        return {"email": email, "status": "INVALID_SYNTAX", "code": 0, "details": "Invalid email syntax"}
    
    clean_email = match.group(0)
    user, domain = clean_email.split('@', 1)
    
    mx_list = resolve_mx_records(domain)
    if not mx_list:
        return {"email": clean_email, "status": "NO_MX_RECORDS", "code": 0, "details": f"Domain {domain} has no active MX records"}

    for mx in mx_list[:2]:
        try:
            server = smtplib.SMTP(mx, 25, timeout=timeout)
            server.helo('appliedwork.ai')
            server.mail(from_addr)
            code, msg = server.rcpt(clean_email)
            msg_str = msg.decode('utf-8', errors='ignore') if isinstance(msg, bytes) else str(msg)
            
            if code == 250:
                is_catchall = False
                if check_catchall:
                    try:
                        fake_user = f"antigravity_test_{uuid.uuid4().hex[:8]}"
                        c_code, _ = server.rcpt(f"{fake_user}@{domain}")
                        if c_code == 250:
                            is_catchall = True
                    except Exception:
                        pass
                try:
                    server.quit()
                except Exception:
                    pass
                
                if is_catchall:
                    return {
                        "email": clean_email,
                        "status": "CATCH_ALL",
                        "code": code,
                        "mx": mx,
                        "details": "Mailbox accepted, but domain accepts all addresses (catch-all)"
                    }
                else:
                    return {
                        "email": clean_email,
                        "status": "DELIVERABLE",
                        "code": code,
                        "mx": mx,
                        "details": "Mailbox confirmed deliverable and available (250 OK)"
                    }
            elif code in [550, 551, 552, 553, 554]:
                try:
                    server.quit()
                except Exception:
                    pass
                return {
                    "email": clean_email,
                    "status": "UNDELIVERABLE",
                    "code": code,
                    "mx": mx,
                    "details": f"Mailbox rejected by server: {msg_str.strip()}"
                }
            else:
                try:
                    server.quit()
                except Exception:
                    pass
                return {
                    "email": clean_email,
                    "status": "RISKY",
                    "code": code,
                    "mx": mx,
                    "details": f"Server returned code {code}: {msg_str.strip()}"
                }
        except (smtplib.SMTPConnectError, smtplib.SMTPServerDisconnected, socket.timeout, ConnectionRefusedError, OSError) as e:
            continue
            
    return {
        "email": clean_email,
        "status": "CONNECTION_FAILED",
        "code": 0,
        "details": "Could not complete SMTP handshake with MX servers (timed out or port 25 restricted)"
    }

def main():
    parser = argparse.ArgumentParser(description="Applied Work SMTP Email Verifier")
    parser.add_argument("--emails", nargs="+", help="List of emails to verify")
    parser.add_argument("--file", help="JSON file containing email list or objects with 'email' key")
    parser.add_argument("--output", help="Optional output JSON file")
    parser.add_argument("--threads", type=int, default=8, help="Number of concurrent threads")
    args = parser.parse_args()

    email_list = []
    if args.emails:
        email_list.extend(args.emails)
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, str):
                        email_list.append(item)
                    elif isinstance(item, dict) and "email" in item:
                        email_list.append(item["email"])

    if not email_list:
        print("Error: No emails provided to verify. Use --emails or --file.")
        sys.exit(1)

    print(f"Starting verification of {len(email_list)} email addresses across {args.threads} threads...\n")
    results = []

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_map = {executor.submit(verify_single_email, em): em for em in email_list}
        for future in as_completed(future_map):
            res = future.result()
            results.append(res)
            print(f"[{res['status']}] {res['email']} -> {res.get('details')}")

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults successfully written to {args.output}")

if __name__ == "__main__":
    main()
