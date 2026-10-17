# Applied Work Outreach and Mailbox Rules

This document defines the strict operational and hygiene rules governing all outbound communications from Applied Work across Antigravity, Gemini CLI, and automated agents.

---

## 1. Zero-Bounce & Verification Policy

1. **Pre-Send Verification:** Every single email address must be verified locally via direct SMTP handshake (`HELO appliedwork.ai` -> `MAIL FROM` -> `RCPT TO`).
2. **Deliverability Status Enforcement:**
   - `DELIVERABLE` (Code 250, non-catchall): Cleared for dispatch.
   - `CATCH_ALL`: **HOLD.** Domain accepts arbitrary non-existent recipients; existence of individual person is unverified.
   - `UNDELIVERABLE` (Codes 550, 551, 553, 554, NoSuchUser, DisabledUser): **PERMANENT EXCLUSION.**
   - `CONNECTION_FAILED` / `TIMED_OUT`: **HOLD.** Unverified addresses cannot be sent to.
3. **No Inferred Guesses:** Never dispatch to unverified pattern-derived addresses (e.g. `first.last@domain`) without prior SMTP confirmation.

---

## 2. Global Deduplication & Suppression Register

1. **Company Domain Suppression:** Once any employee or general inbox of a target company domain receives an outreach message, the entire domain enters suppression for the active campaign cycle (30 days minimum).
2. **Multi-Mailbox Sync:** Always check Sent and Outbox folders across all three connected accounts (`raja@appliedwork.ai`, `alina@appliedwork.ai`, `hasan@appliedwork.ai`) before queuing a domain.
3. **Domain Aliases:** Verify whether a subsidiary or alternative domain belongs to an already-contacted parent entity.
4. **Unsubscribe / Bounce Register:** Immediately add any bounced or opt-out domain to the suppression register.

---

## 3. Mandatory 60-Second Cooldown Gap

- **Strict Timing:** A minimum delay of **60 seconds** must elapse between each email dispatch.
- **Purpose:** Protects sender domain reputation, prevents IP throttling by receiving providers (Google Workspace, Microsoft Exchange), and avoids rapid-fire spam scoring.
- **Implementation:** In automated loops, utilize explicit timer scheduling (`schedule(DurationSeconds=60)` in Antigravity or `sleep 60` in CLI).

---

## 4. Lane Allocation & Sender Personas

| Lane | Sender Persona | Address | Subject Hook Pattern | Value Proposition |
|---|---|---|---|---|
| **Compute Brokering** | Alina | `alina@appliedwork.ai` | `{Company}: compute planning` | Independent capacity options, GPU/cluster qualification, memory/region matching. |
| **Data (Pilots)** | Raja | `raja@appliedwork.ai` | `{Company}: an expert reviewed pilot` | Expert contributor sourcing, RLHF/reasoning evaluations, multi-modal QA. |
| **Data Brokering** | Hasan | `hasan@appliedwork.ai` | `{Company}: company data assessment` | Assessing and licensing proprietary internal workflow/estimating/clinical data for AI training. |

---

## 5. Draft Content & Formatting Standards

1. **Clean HTML Format:** Dispatches must use standard HTML paragraph (`<p>`) and break (`<br>`) tags.
2. **Embedded Anchor Links:** Referral or evaluation links (such as Micro1 data valuation) must be cleanly embedded as clickable HTML anchor tags:
   `<a href="https://company.micro1.ai/register/?referralCode=fef340a7-30ae-4721-a464-1673c1086860&utm_source=referral&utm_medium=share&utm_campaign=job_referral">assess your company data's potential value</a>`
   Never output naked URLs in draft prose.
3. **Zero Research Leakage:** Internal scraping metadata, Glassdoor snippets, draft IDs, or tracker annotations must be completely stripped before sending.
4. **Accurate Sign-Off:** Senders must sign off with their own first name and `Applied Work`.
