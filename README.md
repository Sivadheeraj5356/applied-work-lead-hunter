# Applied Work — Autonomous Lead Hunter & Signal Pipeline

An autonomous, end-to-end research, scraping, and lead generation engine engineered for **Applied Work**. It continuously monitors intent signals across **X (Twitter)**, **LinkedIn**, **Reddit**, RSS, SEC filings, and public news feeds, matches them against live suppression blacklists, executes zero-bounce direct port 25 SMTP verification, and syncs qualified leads and signals directly into Google Sheets.

---

## 1. Architecture Overview

```
                      ┌───────────────────────────────────────────────┐
                      │            Signal & Scraping Sources          │
                      │  • X (Twitter) Intent Scanner                 │
                      │  • Reddit Discussions (r/LocalLLaMA, r/sysadmin)│
                      │  • Tech News & RSS Ingestion                  │
                      │  • SEC / Chapter 7 & 11 Distress Filings     │
                      └───────────────────────┬───────────────────────┘
                                              │
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │              Deduplication Core               │
                      │  • Live 1,492+ Company Suppression Blacklist  │
                      │  • Exact & Normalized Substring Matching      │
                      │  • Domain Normalization                       │
                      └───────────────────────┬───────────────────────┘
                                              │
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │         Zero-Bounce Deliverability Gate       │
                      │  • Parallel Direct Port 25 SMTP Handshakes    │
                      │  • DNS MX Record Resolution with LRU Cache    │
                      │  • Anti-Catch-All Detection (Randomized Box)  │
                      │  • Strict 250 OK Qualification Only           │
                      └───────────────────────┬───────────────────────┘
                                              │
                                              ▼
                      ┌───────────────────────────────────────────────┐
                      │          Google Sheets Rest API Client        │
                      │  • Service Account JWT Authentication         │
                      │  • Chunked Batch Appends & Dimension Control  │
                      │  • Multi-Tab Sync (Compute, Data, Brokering)  │
                      │  • Real-Time Summary Tab Metric Verification   │
                      └───────────────────────────────────────────────┘
```

---

## 2. Directory Structure

```text
applied-work/
├── .agents/
│   └── skills/
│       ├── applied-work-research/     # SMTP verification & deep research protocols
│       ├── signal-hunter/             # Structured query templates & intent rubrics
│       └── social-intent-scanner/     # Social media signal extraction
├── config/
│   ├── antigravity_mcp_config.json    # MCP registration for Antigravity
│   ├── gemini_cli_setup.bat           # Setup for Windows Gemini CLI
│   ├── gemini_cli_setup.sh            # Setup for macOS/Linux Gemini CLI
│   └── google_service_account.json    # (Ignored in Git) Google Cloud Service Account
├── exports/
│   └── batch_300_20261017/            # Full local snapshot of 300 novel leads
│       ├── batch_300_summary.json
│       ├── Compute_Brokering_100.csv
│       ├── Daily_Research_Log_300.csv
│       ├── Daily_Signals_300.csv
│       ├── Data_100.csv
│       ├── Data_Brokering_100.csv
│       └── linkeldn_contacts_300.csv
├── rules/
│   └── outreach-and-mailbox-rules.md  # Suppression, cooldowns, zero-bounce policy
├── scripts/
│   ├── data_pool_compute_100.py       # 100 novel compute brokering leads
│   ├── data_pool_data_100.py          # 100 novel data evaluation leads
│   ├── data_pool_databrokering_100.py # 100 novel data brokering leads (50 distressed)
│   ├── run_pipeline_300.py            # Master pipeline runner
│   ├── reconcile_data_tab.py          # Data tab row alignment & summary sync
│   ├── verify_email.py                # Standalone multi-threaded SMTP verifier
│   └── verify_live_summaries.py       # Live summary metric audit script
├── src/
│   ├── cloudflare/
│   │   ├── worker.js                  # 4-hour cron autonomous worker
│   │   └── wrangler.toml              # Cloudflare Worker configuration
│   ├── core/
│   │   ├── deduplicator.py            # Blacklist suppression filter
│   │   ├── sheets_client.py           # Authenticated Google Sheets client
│   │   └── verifier.py                # Parallel SMTP deliverability verifier
│   └── scrapers/
│       ├── news_scraper.py            # TechCrunch / VentureBeat / HackerNews RSS
│       ├── reddit_scraper.py          # Reddit intent scraper
│       └── x_scraper.py               # X/Twitter search query generator
├── tracker_data/
│   └── live_blacklist_set.txt         # 1,492 blacklisted companies
├── .gitignore                         # Protects service accounts & secrets
└── README.md
```

---

## 3. Operational Mechanics

### A. Strict Zero-Bounce Deliverability Gate
Every email candidate is verified live via direct socket connection to the domain's primary MX server on TCP port 25 before being tagged `DELIVERABLE`:
- **Step 1:** DNS MX lookup via `dnspython`.
- **Step 2:** Catch-all detection by probing a randomized nonexistent recipient (e.g. `nonexistent-verifier-check-94812@domain.com`). If 250 OK is returned, the domain is marked `CATCH_ALL`.
- **Step 3:** Specific candidate mailbox check (`MAIL FROM: <verify@appliedwork.ai>` $\rightarrow$ `RCPT TO: <candidate@domain.com>`).
- **Classification:**
  - `DELIVERABLE`: Confirmed 250 OK on non-catch-all server.
  - `CATCH_ALL`: Server accepts all recipients; held for secondary enrichment.
  - `UNDELIVERABLE`: 550 User Not Found / Disabled. Hard blocked.
  - `CONNECTION_FAILED`: Port 25 filtered or timeout; held.

### B. Lane Mapping & Outreach Personas
- **Compute Brokering (Alina — `alina@appliedwork.ai`):** Focuses on teams deploying or expanding large-scale GPU clusters (H100/H200/GB200) or seeking spot capacity.
- **Data (Raja — `raja@appliedwork.ai`):** Focuses on frontier labs, evaluation frameworks, and RLHF/RLVR data operations.
- **Data Brokering (Hasan — `hasan@appliedwork.ai`):** Focuses on distressed venture-backed AI/robotics assets (Chapter 7/11, acqui-hires, wound-down companies) for proprietary data acquisition, alongside commercial MEP and healthcare systems.

---

## 4. Execution & Deployment

### Option 1: Autonomous Execution via Cloudflare Workers
The engine includes a Cloudflare Worker configured with a cron trigger running every 4 hours (`0 */4 * * *`):
1. Install Wrangler CLI:
   ```bash
   npm install -g wrangler
   ```
2. Navigate to the Cloudflare module:
   ```bash
   cd src/cloudflare
   ```
3. Deploy to your Cloudflare account:
   ```bash
   npx wrangler deploy
   ```
4. Manual trigger:
   ```bash
   curl https://applied-work-lead-hunter.<your-subdomain>.workers.dev/run-cycle
   ```

### Option 2: Local / Scheduled Task Execution
Run the full 300-lead pipeline locally or via Windows Task Scheduler / systemd cron:
```bash
python scripts/run_pipeline_300.py
```
To verify live numbers across all Google Sheet summary tabs:
```bash
python scripts/verify_live_summaries.py
```

---

## 5. Google Sheets Integration
- **Spreadsheet ID:** `1yc5LGR1NvgqPlKR9iMZyS3vYHADlNU91WwoDdrt_duY`
- **Synced Tabs:**
  - `Compute Brokering` & `Compute Brokering Summary` (568 leads)
  - `Data` & `Data Summary` (637 leads)
  - `Data Brokering` & `Data Brokering Summary` (660 leads)
  - `Daily Signals` (300 signals per batch)
  - `linkeldn` (600+ verified decision-maker contacts)
  - `Daily Research Log` (Audited batch summaries)
