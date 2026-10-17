---
name: social-intent-scanner
description: Social intent and public channel scanner for AI infrastructure, compute shortages, data acquisition requests, and executive career movements.
---

# Social Intent Scanner Skill

The **Social Intent Scanner** continuously scans public and social platforms—including LinkedIn, X (Twitter), GitHub discussions, Hacker News, and specialized job boards—to detect real-time intent, executive hiring shifts, and technical pain points.

---

## 1. Intent Classification Hierarchy

All incoming social signals are tagged with one of three intent levels:

### Level 1: High / Explicit Intent
- **Definition:** Direct, public request or statement of need by an executive or lead engineer.
- **Examples:**
  - *"Looking for reliable H100 / B200 clusters for the next 3 months in US-East."*
  - *"Hiring clinical data annotation partners for medical imaging model."*
  - *"Looking for high-quality mathematical reasoning trajectories for LLM training."*
- **Action:** Fast-track to lead research and immediate draft generation.

### Level 2: Medium / Structural Intent
- **Definition:** Organizational signals indicating an expansion of workloads or upcoming data initiatives.
- **Examples:**
  - Executive leadership hire (e.g. Chief AI Officer, VP of Partnerships, CBO).
  - Series A/B funding announcement specifying compute/cluster buildout.
  - Job descriptions mentioning multi-cluster orchestration, vLLM, or distributed RL.
- **Action:** Route to queue for contact enrichment and signal corroboration.

### Level 3: Inferred / Contextual Fit
- **Definition:** Well-established vertical organizations with high-value workflow data or heavy AI inference operations, but no explicit public request.
- **Examples:**
  - Regional commercial contractors with multi-million dollar bidding workflows.
  - Specialized hospital networks with extensive electronic health record operations.
- **Action:** Route to Data Brokering lane with compliant assessment link.

---

## 2. Search Syntax & Queries

Use web search (via Tavily MCP or web search) with targeted Boolean queries:

### Compute Intent Queries:
```text
("looking for compute" OR "need H100" OR "GPU cluster capacity" OR "GPU allocation") ("AI" OR "LLM") site:twitter.com OR site:linkedin.com
"Strategic Finance and Compute Lead" OR "Compute Infrastructure" site:linkedin.com/jobs
"compute partner" OR "cloud GPU shortage" ("seed" OR "Series A" OR "Series B")
```

### Data & Evaluation Intent Queries:
```text
("RLHF" OR "human evaluation" OR "expert annotators") ("hiring" OR "partner" OR "vendor")
("clinical data acquisition" OR "medical dataset licensing") site:linkedin.com
("code evaluation benchmark" OR "LLM reasoning dataset") ("looking for" OR "sourcing")
```

---

## 3. Evidence Extraction & Verification Rules

1. **Verify Speaker Authority:** The post or signal must originate from a verified company account, founder, C-suite officer, or key engineering/operations lead.
2. **Timestamp Verification:** Signals older than 90 days must be flagged as `HISTORICAL` and require re-validation of active need.
3. **Primary Link Preservation:** Always record the exact URL (Glassdoor listing, tweet link, LinkedIn post, or official PR) as primary evidence.
4. **Clean Content Formatting:** Extract the salient factual quote without trailing tracking parameters, emojis, or marketing noise.

---

## 4. Signal Hand-off Format

Deliver the structured finding to the **Applied Work Research** skill:
```markdown
- **Company:** [Company Name]
- **Domain:** [company.com]
- **Identified Lead/Executive:** [Full Name] ([Title])
- **Intent Level:** High / Medium / Inferred
- **Direct Evidence Quote:** "[Exact statement or requirement]"
- **Source Platform & Link:** [Platform] ([URL])
- **Recommended Lane:** Compute Brokering / Data / Data Brokering
```
