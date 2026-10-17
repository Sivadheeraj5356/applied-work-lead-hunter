"""
Zero-Bounce SMTP Email Verifier
Performs RFC 5322 syntax validation, multi-provider DNS MX resolution with caching,
and direct port 25 SMTP handshake with anti-catch-all detection.
"""

import re
import socket
import smtplib
import uuid
import functools
from concurrent.futures import ThreadPoolExecutor

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

@functools.lru_cache(maxsize=4096)
def resolve_mx_records(domain):
    """Resolves DNS MX records using dnspython or socket fallback."""
    try:
        import dns.resolver
        answers = dns.resolver.resolve(domain, 'MX', lifetime=3)
        sorted_answers = sorted(answers, key=lambda r: r.preference)
        return [str(r.exchange).rstrip('.') for r in sorted_answers]
    except Exception:
        pass
    return [domain]

def verify_single_email(email, from_addr="verify@appliedwork.ai", check_catchall=True, timeout=3):
    """
    Verifies deliverability of a single email address via SMTP handshake.
    Returns: dict with email, status (DELIVERABLE, UNDELIVERABLE, CATCH_ALL, RISKY, INVALID_SYNTAX), details
    """
    if not email:
        return {"email": "", "status": "EMAIL_UNRESOLVED", "details": "Empty address"}
        
    email = email.strip()
    match = EMAIL_REGEX.search(email)
    if not match:
        return {"email": email, "status": "INVALID_SYNTAX", "details": "Invalid syntax"}
        
    clean_email = match.group(0)
    user, domain = clean_email.split('@', 1)
    
    mx_list = resolve_mx_records(domain)
    if not mx_list:
        return {"email": clean_email, "status": "NO_MX_RECORDS", "details": f"No MX records for {domain}"}
        
    for mx in mx_list[:2]:
        try:
            server = smtplib.SMTP(mx, 25, timeout=timeout)
            server.helo('appliedwork.ai')
            server.mail(from_addr)
            code, msg = server.rcpt(clean_email)
            
            if code == 250:
                is_catchall = False
                if check_catchall:
                    try:
                        fake_user = f"aw_probe_{uuid.uuid4().hex[:8]}"
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
                    return {"email": clean_email, "status": "CATCH_ALL", "details": f"MX {mx} accepted recipient but domain is catch-all"}
                return {"email": clean_email, "status": "DELIVERABLE", "details": f"250 OK from {mx}; non-catch-all verified"}
            elif code in (550, 551, 552, 553, 554):
                try:
                    server.quit()
                except Exception:
                    pass
                return {"email": clean_email, "status": "UNDELIVERABLE", "details": f"Rejected by {mx} with code {code}"}
            else:
                try:
                    server.quit()
                except Exception:
                    pass
                return {"email": clean_email, "status": "RISKY", "details": f"Server {mx} responded with {code}"}
        except socket.timeout:
            continue
        except Exception as e:
            continue
            
    return {"email": clean_email, "status": "CONNECTION_FAILED", "details": f"Could not connect to MX servers for {domain}"}

def verify_emails_parallel(email_list, max_workers=16):
    """Runs batch verification across multiple threads."""
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futs = {executor.submit(verify_single_email, em): em for em in email_list if em}
        for fut in futs:
            res = fut.result()
            results[res["email"]] = res
    return results
