---
name: applied-work-research
description: End-to-end executive lead research, deduplication, strict local SMTP deliverability verification (zero-bounce gate), and lane-specific outreach draft generation for Applied Work.
---

# Applied Work Research & Outreach Skill

The **Applied Work Research** skill is the central engine for lead enrichment, contact verification, suppression enforcement, and compliant outreach execution across Applied Work's three primary business lanes.

---

## 1. Operating Rules & Core Principles

### Rule 1: Zero-Bounce Policy (Strict Local Verification)
- **NO EMAIL IS DISPATCHED WITHOUT DIRECT DELIVERABILITY VERIFICATION.**
- Every candidate address must undergo direct local SMTP handshake verification (`HELO appliedwork.ai` -> `MAIL FROM` -> `RCPT TO`) prior to queuing.
- **Verification Classifications:**
  - `DELIVERABLE` (SMTP code 250, verified non-catchall): **Cleared for dispatch.**
  - `CATCH_ALL` (Domain accepts randomized non-existent addresses): **HOLD.** Do not send unless verified by a secondary authoritative source.
  - `UNDELIVERABLE` (SMTP codes 550, 551, 553, 554, NoSuchUser, DisabledUser): **PERMANENT REJECT.** Never send.
  - `CONNECTION_FAILED` / `TIMED_OUT`: **HOLD.** Enterprise firewalls/gateways that drop probe handshakes must not be assumed deliverable.

### Rule 2: Deduplication & Suppression Register
- Prior to researching or drafting an account, check the **Global Suppression Register**:
  - Connected Zoho mailboxes (Sent, Outbox, Trash across Raja, Alina, Hasan).
  - Prior outreach tracker sheets.
  - Bounced / unsubscribed domain register.
- If an account has already received outreach in the active campaign window, the entire company domain is **SUPPRESSED**.

### Rule 3: 60-Second Cooldown Gap
- To protect mailbox reputation, deliverability, and rate limits, a **mandatory 60-second delay** must be observed between individual email dispatches across all senders.

---

## 2. Lane Mapping & Sender Assignments

| Lane | Sender Account | Zoho MCP Server | Value Proposition | Subject Hook |
|---|---|---|---|---|
| **Compute Brokering** | `alina@appliedwork.ai` | `zoho-mail-alina` | External compute capacity, hardware/region qualification | `{Company}: compute planning` |
| **Data** | `raja@appliedwork.ai` | `zoho-mail` | Expert-reviewed evaluation pilots, domain specialists | `{Company}: an expert reviewed pilot` |
| **Data Brokering** | `hasan@appliedwork.ai` | `zoho-mail-hasan` | Assessment and licensing of proprietary company workflow data | `{Company}: company data assessment` |

---

## 3. Executive Contact Resolution

Target 2–3 key decision makers per account according to the lane:
- **Compute Brokering:** CEO, CTO, VP ML / AI Infrastructure, Head of Engineering, Compute Lead.
- **Data (AI/ML):** CEO, Co-Founder, Head of Data/Annotation, Chief AI Officer, VP Research.
- **Data Brokering (Trades/Enterprise):** CEO, Owner/Operator, VP Preconstruction, Director of Estimating, Medical Director (Healthcare).

**Tool Integration:**
- Use **Apollo MCP** (`apollo_search`, `apollo_enrich`) or verified domain pattern matching to resolve individual work addresses.
- Never use guessed or unvalidated catch-all routes when individual executives are published.

---

## 4. Verification Engine Execution

Run the bundled local verifier script before queuing any lead:

```bash
python scripts/verify_email.py --emails target1@company.com target2@company.com
```

The script:
1. Queries DNS MX records for the domain.
2. Connects to primary MX on port 25.
3. Issues `HELO appliedwork.ai`, `MAIL FROM:<verify@appliedwork.ai>`, `RCPT TO:<target>`.
4. Tests a random fake UUID address to verify if the domain is a catch-all.
5. Returns JSON with status: `DELIVERABLE`, `CATCH_ALL`, `UNDELIVERABLE`, or `CONNECTION_FAILED`.

---

## 5. Draft Formulation & Hygiene

1. **No Metadata Leakage:** Ensure internal notes,apollo scrapings, research tables, or draft IDs never appear in the email body.
2. **HTML Formatting:** All dispatches must use `mailFormat: "html"` with standard `<p>` and `<br>` paragraphs.
3. **Embedded Links:** In Data Brokering drafts, the Micro1 data valuation link must be cleanly embedded as anchor text:
   `<a href="https://company.micro1.ai/register/?referralCode=fef340a7-30ae-4721-a464-1673c1086860&utm_source=referral&utm_medium=share&utm_campaign=job_referral">assess your company data's potential value</a>`
   Never output raw URLs in prose.
4. **Sign-off Consistency:** Always sign off with the exact first name of the assigned sender (`Alina`, `Raja`, or `Hasan`) and `Applied Work`.
