---
name: signal-hunter
description: Automated discovery and qualification of high-intent buying signals for AI Compute Brokering, Data Sourcing, and Proprietary Data Brokering across target enterprise accounts.
---

# Signal Hunter Skill

The **Signal Hunter** skill monitors, detects, and qualifies active business and technical triggers that indicate an enterprise has an imminent need for AI compute capacity, expert-annotated data, or proprietary domain data licensing.

---

## 1. Core Lanes & Target Triggers

Signal Hunter classifies all detected opportunities into three operational lanes:

### Lane A: Compute Brokering
- **Sender Persona:** Alina (`alina@appliedwork.ai`)
- **Core Value Proposition:** Workload qualification, provider comparison (GPUs, memory, networking, region, timeline), independent external capacity options.
- **Target Signals:**
  - Job vacancies for *Compute Lead*, *ML Infrastructure Engineer*, *Director of Strategic Finance & Compute*, or *HPC Systems Engineer*.
  - Recent announcements of foundation model training, large multi-modal architectures, or video/audio generation models.
  - Published cloud partnerships (e.g. AWS, GCP, CoreWeave, Lambda Labs) indicating scaling constraints or workload migrations.
  - Complaints or updates regarding GPU wait times, cluster limits, or inference latency bottlenecks.

### Lane B: Data (Expert Reviewed Pilots)
- **Sender Persona:** Raja (`raja@appliedwork.ai`)
- **Core Value Proposition:** Expert contributor sourcing, project organization, rigorous QA, and delivery across software engineering, legal, finance, math, and healthcare.
- **Target Signals:**
  - Model evaluation challenges (e.g. complex reasoning, RLHF, code generation benchmarks, noisy audio/speech transcription, multi-lingual translation).
  - Open positions for *Annotation Operations*, *Model Evaluation Lead*, or *RLHF Scientist*.
  - Academic or industry benchmark releases showing error rates or hallucinations in specific vertical domains.

### Lane C: Data Brokering (Enterprise Workflow Data Licensing)
- **Sender Persona:** Hasan (`hasan@appliedwork.ai`)
- **Core Value Proposition:** Assessment and preparation of company-authored procedures, estimation methods, clinical workflows, and trade records for authorized AI training.
- **Target Signals:**
  - Specialized industry leaders (e.g. commercial MEP contractors, hospital chains, legal practices, fintech claims processors).
  - Public RFPs, HMIS/ERP system rollouts, operational SOP publications, or digitized workflow appointments.
  - Strong regional presence and deep domain history with proprietary estimating, scheduling, and diagnostic workflows.

---

## 2. Signal Discovery Workflow

```
[Target Industry / Account Pool]
                │
                ▼
  [Tool Query: Tavily / Apollo / Web]
                │
                ├──> Job Postings & Career Pages
                ├──> Press Releases & Leadership Appointments
                └──> Technical Blogs & Benchmark Reports
                │
                ▼
  [Signal Qualification Matrix]
  - Is the signal fresh (< 90 days)?
  - Is there an identifiable decision maker?
  - Does the company match size/revenue threshold?
                │
                ▼
  [Lane Routing & Lead Package Output]
```

---

## 3. Tool Usage & Integration

When integrated via MCP:
- **Tavily MCP (`tavily_search`):** Search for recent press releases, job listings, and technical updates:
  ```json
  {
    "query": "\"Compute Lead\" OR \"ML Infrastructure\" hiring site:linkedin.com/jobs OR site:boards.greenhouse.io",
    "topic": "news"
  }
  ```
- **Apollo MCP (`apollo_search` / `apollo_enrich`):** Resolve company size, verified domain, and identify executive team members corresponding to the signal.

---

## 4. Signal Output Schema

For each qualified signal, produce a structured record:

```markdown
#### [Signal ID] [Company Name]
- **Lane:** Compute Brokering | Data | Data Brokering
- **Signal Summary:** [1-2 sentences on what triggered the qualification]
- **Source URL:** [Direct link to job posting, article, or press release]
- **Signal Date:** [YYYY-MM-DD or Recency]
- **Target Role Candidate:** [e.g. VP Infrastructure, Head of AI, Estimating Director]
- **Qualification Evidence:** [Key quote or job description excerpt]
- **Suggested Subject Line Hook:** [e.g. "{Company}: compute planning" or "{Company}: an expert reviewed pilot"]
```
