# SMTP Verification Matrix & Deliverability Standards

Applied Work mandates direct local SMTP handshakes before any email is dispatched.

| SMTP Return Code | Response Description | Catch-All Test Result | Verdict | Queue Action |
|---|---|---|---|---|
| **250** | Mailbox OK / Recipient accepted | Fake user rejected (550) | **DELIVERABLE** | Cleared for dispatch |
| **250** | Mailbox OK / Recipient accepted | Fake user accepted (250) | **CATCH_ALL** | **HOLD.** Deliverability unproven |
| **550 / 551** | NoSuchUser / Access Denied | N/A | **UNDELIVERABLE** | **HARD BLOCK.** Saved from bounce |
| **552 / 554** | Mailbox full / Transaction failed | N/A | **UNDELIVERABLE** | **HARD BLOCK** |
| **Timeout / 0** | Connection dropped / Port 25 filtered | N/A | **CONNECTION_FAILED** | **HOLD.** Do not assume deliverable |

### Catch-All Probe Methodology:
1. Probe targeted recipient address: `RCPT TO:<target@domain.com>`.
2. Probe randomized non-existent UUID: `RCPT TO:<antigravity_test_9f2a7b1c@domain.com>`.
3. If both return 250, the receiving server is a catch-all and does not perform per-user validation at SMTP time.
