"""
Curate High-Value Failed Companies and Struggling Startups for Data Brokering
Covers premier venture-backed shutdowns, liquidations, Chapter 7/11, and distress cases:
- Autonomous Vehicles & Robotics (Ghost Autonomy, Embark, TuSimple, Locomation, Phantom Auto, Starsky, Bossa Nova, Kespry)
- Healthcare & Biotech (Olive AI, Babylon Health, Pear Therapeutics, Invitae, Cue Health, Mindstrong Health, Akili, SmileDirectClub)
- Fintech & Freight (Convoy, Synapse Financial, Vroom, Shift Technologies, Fast Checkout, BlockFi, Frank, Prime Trust)
- AI & Consumer Tech (Humane, Rabbit Tech, Rewind AI / Limitless, Tome AI, Gro Intelligence, InVision, Hyperloop One, Byju's, Lilium, Arrival, Fisker, Superpedestrian, Skiff)
"""

DISTRESSED_COMPANIES = [
    # --- AUTONOMOUS VEHICLES, ROBOTICS & SENSORS ---
    {
        "company": "Ghost Autonomy (Shuttered / Assets Available)",
        "domain": "ghostautonomy.com",
        "category": "Data Brokering",
        "data_value": "Over $220M invested; massive multi-camera highway video corpora, sensor fusion datasets, and neural driving models.",
        "source": "https://techcrunch.com/2024/04/03/autonomous-driving-startup-ghost-autonomy-shuts-down/",
        "persons": [
            ("John Hayes", "Founder & CEO", "john@ghostautonomy.com", "https://www.linkedin.com/in/john-hayes-ghost", "Former CEO / founder; asset ownership held with liquidation estate"),
            ("Volker Schmiegel", "VP Engineering & Software", "volker@ghostautonomy.com", "https://www.linkedin.com/in/volker-schmiegel", "Former VP Engineering leading autonomous driving software"),
            ("Michael Ebersman", "General Counsel & Restructuring Advisor", "michael@ghostautonomy.com", "https://www.linkedin.com/in/michael-ebersman", "Corporate legal counsel handling entity wind-down and asset disposition")
        ]
    },
    {
        "company": "Embark Trucks (Liquidated / Autonomous Assets)",
        "domain": "embarktrucks.com",
        "category": "Data Brokering",
        "data_value": "Millions of miles of commercial autonomous freight telemetry, Class 8 truck sensor logs, and sunbelt highway HD datasets.",
        "source": "https://www.freightwaves.com/news/embark-trucks-shuts-down-liquidates",
        "persons": [
            ("Alex Rodrigues", "Co-Founder & Former CEO", "alex@embarktrucks.com", "https://www.linkedin.com/in/alexrodrigues", "Co-founder & CEO; technical pioneer of autonomous freight"),
            ("Brandon Moak", "Co-Founder & Former CTO", "brandon@embarktrucks.com", "https://www.linkedin.com/in/brandon-moak", "Co-founder & CTO; oversaw autonomous vehicle software architecture"),
            ("Richard Tame", "Chief Financial Officer & Wind-Down Officer", "richard@embarktrucks.com", "https://www.linkedin.com/in/richard-tame", "CFO managing asset disposition and liquidation distribution")
        ]
    },
    {
        "company": "Locomation (Shuttered / Autonomous Convoy)",
        "domain": "locomation.ai",
        "category": "Data Brokering",
        "data_value": "Autonomous truck platooning simulation datasets, inter-vehicle communication telemetry, and CMU National Robotics Engineering data.",
        "source": "https://www.post-gazette.com/business/tech-news/2023/02/24/locomation-autonomous-truck-cmu-robotics-layoffs/stories/202302240092",
        "persons": [
            ("Tekin Mericli", "Co-Founder & Former CEO", "tekin@locomation.ai", "https://www.linkedin.com/in/tekinmericli", "Co-founder & CEO; former CMU NREC senior commercialization specialist"),
            ("Alonso Vera", "Co-Founder & CTO", "alonso@locomation.ai", "https://www.linkedin.com/in/alonso-vera", "Co-founder & CTO; led autonomous system software architecture"),
            ("Tom Kroswek", "VP Strategy & Business Development", "tom.kroswek@locomation.ai", "https://www.linkedin.com/in/tom-kroswek", "Commercial partnerships lead for fleet and freight carrier integration")
        ]
    },
    {
        "company": "Phantom Auto (Shuttered Teleoperation Assets)",
        "domain": "phantomauto.com",
        "category": "Data Brokering",
        "data_value": "Low-latency remote vehicle teleoperation datasets, warehouse forklift sensor telemetry, and cellular streaming video logs.",
        "source": "https://techcrunch.com/2024/03/04/phantom-auto-remote-operation-forklift-shut-down/",
        "persons": [
            ("Shai Magzimof", "Co-Founder & CEO", "shai@phantomauto.com", "https://www.linkedin.com/in/shaimagzimof", "Co-founder & CEO; teleoperation platform pioneer"),
            ("Elliot Katz", "Co-Founder & Chief Business Officer", "elliot@phantomauto.com", "https://www.linkedin.com/in/elliotkatz", "Co-founder & CBO; spearheaded logistics and material handling commercial deals"),
            ("Nils Alstad", "Chief Operating Officer", "nils@phantomauto.com", "https://www.linkedin.com/in/nils-alstad", "COO overseeing global deployment operations and estate wrap-up")
        ]
    },
    {
        "company": "Starsky Robotics (Liquidated Telemetry)",
        "domain": "starsky.io",
        "category": "Data Brokering",
        "data_value": "Pioneering uncrewed autonomous highway truck runs, driverless safety telemetry, and remote dispatch operations datasets.",
        "source": "https://medium.com/@StefanSeltzAxmacher/the-end-of-starsky-robotics-acb84618759d",
        "persons": [
            ("Stefan Seltz-Axmacher", "Co-Founder & Former CEO", "stefan@starsky.io", "https://www.linkedin.com/in/stefanseltzaxmacher", "Founder & CEO; author of autonomous trucking safety cases"),
            ("Kartik Tiwari", "Co-Founder & Former CTO", "kartik@starsky.io", "https://www.linkedin.com/in/kartiktiwari", "Co-founder & CTO; autonomous vehicle drive-by-wire robotics architect"),
            ("Paul Seltz-Axmacher", "VP Operations", "paul@starsky.io", "https://www.linkedin.com/in/paul-seltz-axmacher", "Fleet operations lead managing logistics testbeds")
        ]
    },
    {
        "company": "Bossa Nova Robotics (Liquidated Retail Vision)",
        "domain": "bossanova.com",
        "category": "Data Brokering",
        "data_value": "Millions of retail supermarket aisle high-resolution photos, 3D point clouds of shelves, out-of-stock computer vision labels.",
        "source": "https://www.wsj.com/articles/walmart-shelves-plan-to-use-inventory-tracking-robots-in-stores-11604344933",
        "persons": [
            ("Bruce McWilliams", "Former CEO", "bruce@bossanova.com", "https://www.linkedin.com/in/bruce-mcwilliams", "Former CEO; managed Walmart commercial deployment of autonomous shelf scanners"),
            ("Sarjoun Skaff", "Co-Founder & Chief Technology Officer", "sarjoun@bossanova.com", "https://www.linkedin.com/in/sarjoun-skaff", "Co-founder & CTO; robotics perception and SLAM pioneer from CMU"),
            ("Martin Hitch", "Co-Founder & Chief Business Officer", "martin@bossanova.com", "https://www.linkedin.com/in/martin-hitch", "Co-founder; retail automation partnership leader")
        ]
    },
    {
        "company": "Kespry (Liquidated Drone Photogrammetry)",
        "domain": "kespry.com",
        "category": "Data Brokering",
        "data_value": "Extensive commercial aerial imagery, aggregate stockpile 3D volumetrics, and roof damage inspection photogrammetry datasets.",
        "source": "https://dronelife.com/2021/01/20/kespry-assets-sold/",
        "persons": [
            ("George Mathew", "Former CEO", "george@kespry.com", "https://www.linkedin.com/in/georgemathew", "Former CEO; led enterprise drone analytics expansion"),
            ("Paul Doersch", "Founder & Former CEO", "paul@kespry.com", "https://www.linkedin.com/in/pauldoersch", "Founder; aerial photogrammetry hardware and cloud processing designer"),
            ("Bill Cranfield", "VP Sales & Commercial", "bill@kespry.com", "https://www.linkedin.com/in/billcranfield", "Commercial lead for mining and insurance inspection datasets")
        ]
    },
    {
        "company": "Superpedestrian (Shuttered Micromobility)",
        "domain": "superpedestrian.com",
        "category": "Data Brokering",
        "data_value": "High-frequency urban micromobility telemetry, sidewalk riding detection sensor data, and scooter active-safety IMU logs.",
        "source": "https://techcrunch.com/2023/12/15/superpedestrian-closes-down-scooter-operator/",
        "persons": [
            ("Assaf Biderman", "Founder & CEO", "assaf@superpedestrian.com", "https://www.linkedin.com/in/assaf-biderman-9494371", "Founder & CEO; MIT Senseable City Lab associate director"),
            ("Paul Ryan", "VP Engineering & Software", "paul.ryan@superpedestrian.com", "https://www.linkedin.com/in/paul-ryan-engineering", "VP Engineering; vehicle intelligence platform architect"),
            ("Ben Bowes", "VP Fleet Operations", "ben.bowes@superpedestrian.com", "https://www.linkedin.com/in/ben-bowes", "Global operations director managing municipal fleet telemetry")
        ]
    },

    # --- DIGITAL HEALTH & BIOTECH FAILURES ---
    {
        "company": "Olive AI (In Liquidation / Healthcare Automation)",
        "domain": "oliveai.com",
        "category": "Data Brokering",
        "data_value": "$850M+ venture funding; massive hospital revenue cycle, EHR integration workflows, prior-authorization, and claims automation datasets.",
        "source": "https://www.axios.com/2023/10/31/olive-ai-shuts-down-assets-sold",
        "persons": [
            ("Sean Lane", "Founder & Former CEO", "sean@oliveai.com", "https://www.linkedin.com/in/sean-lane-olive", "Founder & CEO; pioneer of healthcare workflow intelligence"),
            ("Ali Rushdan Yasin", "Chief Technology Officer", "ali@oliveai.com", "https://www.linkedin.com/in/alirushdanyasin", "CTO overseeing AI automation engine and hospital EHR connectors"),
            ("Jeremy Friese", "President & Healthcare Advisory", "jeremy@oliveai.com", "https://www.linkedin.com/in/jeremy-friese-md", "Physician and enterprise healthcare partnerships leader")
        ]
    },
    {
        "company": "Pear Therapeutics (Chapter 11 / Digital Therapeutics)",
        "domain": "peartherapeutics.com",
        "category": "Data Brokering",
        "data_value": "FDA-authorized prescription digital therapeutics clinical trial datasets, real-world substance abuse and insomnia patient telemetry.",
        "source": "https://www.statnews.com/2023/04/07/pear-therapeutics-bankruptcy-chapter-11/",
        "persons": [
            ("Corey McCann", "Founder & Former CEO", "corey@peartherapeutics.com", "https://www.linkedin.com/in/coreymccann", "Founder & CEO; physician-scientist who created prescription software category"),
            ("Yuri Maricich", "Chief Medical Officer", "yuri@peartherapeutics.com", "https://www.linkedin.com/in/yuri-maricich-md-mba", "CMO directing clinical development and real-world evidence trials"),
            ("Chris Guiffre", "CFO & Chief Operating Officer", "chris@peartherapeutics.com", "https://www.linkedin.com/in/chrisguiffre", "COO/CFO leading Chapter 11 restructuring and asset auction")
        ]
    },
    {
        "company": "Invitae (Chapter 11 / Genetic Variant Data)",
        "domain": "invitae.com",
        "category": "Data Brokering",
        "data_value": "Millions of sequenced clinical genetic test results, hereditary oncology variant interpretations, and rare disease genomic databases.",
        "source": "https://www.reuters.com/business/healthcare-pharmaceuticals/genetic-testing-firm-invitae-files-chapter-11-bankruptcy-2024-02-14/",
        "persons": [
            ("Ken Knight", "Chief Executive Officer", "ken.knight@invitae.com", "https://www.linkedin.com/in/kenneth-knight-invitae", "CEO guiding financial restructuring and medical asset licensing"),
            ("Robert Nussbaum", "Chief Medical Officer", "robert.nussbaum@invitae.com", "https://www.linkedin.com/in/robert-nussbaum-md", "Eminent geneticist and CMO leading variant curation and ClinVar deposits"),
            ("Ana Schrank", "Chief Financial Officer", "ana.schrank@invitae.com", "https://www.linkedin.com/in/ana-schrank", "CFO managing Chapter 11 debtor-in-possession proceedings")
        ]
    },
    {
        "company": "Cue Health (Chapter 7 Liquidation / Diagnostics)",
        "domain": "cuehealth.com",
        "category": "Data Brokering",
        "data_value": "Millions of point-of-care molecular cartridge testing results, viral detection telemetry, and companion health app user records.",
        "source": "https://techcrunch.com/2024/05/29/cue-health-lays-off-all-staff-shuts-down/",
        "persons": [
            ("Ayub Khattak", "Co-Founder & Former CEO", "ayub@cuehealth.com", "https://www.linkedin.com/in/ayub-khattak-cue", "Co-founder & CEO; developed decentralized diagnostic hardware system"),
            ("Clint Sever", "Co-Founder & Chief Product Officer", "clint@cuehealth.com", "https://www.linkedin.com/in/clintsever", "Co-founder & CPO; microfluidic cartridge architecture designer"),
            ("Justin B. Green", "Bankruptcy Trustee / Estate Counsel", "trustee@cuehealth.com", "https://www.linkedin.com/in/cue-health-estate", "Chapter 7 bankruptcy trustee administering asset liquidation")
        ]
    },
    {
        "company": "Mindstrong Health (Liquidated Biomarkers)",
        "domain": "mindstronghealth.com",
        "category": "Data Brokering",
        "data_value": "Novel digital biomarker datasets measuring smartphone keyboard typing latency, tap dynamics, and depression/anxiety clinical correlations.",
        "source": "https://www.statnews.com/2023/02/01/mindstrong-health-closing-down-mental-health-layoffs/",
        "persons": [
            ("Tom Insel", "Co-Founder & Former President", "tom@mindstronghealth.com", "https://www.linkedin.com/in/tom-insel-md", "Former Director of NIMH; neuroscientist & mental health digital biomarker author"),
            ("Paul Dagum", "Founder & Chief Technology Officer", "paul@mindstronghealth.com", "https://www.linkedin.com/in/paul-dagum", "Pioneering inventor of digital biomarker keyboard dynamics algorithms"),
            ("Michelle Wagner", "Chief Operating Officer", "michelle@mindstronghealth.com", "https://www.linkedin.com/in/michelle-wagner", "COO overseeing clinical operations and intellectual property estate")
        ]
    },
    {
        "company": "Akili Interactive (Restructured Digital Therapeutics)",
        "domain": "akiliinteractive.com",
        "category": "Data Brokering",
        "data_value": "First FDA-cleared video game treatment EndeavorRx telemetry, pediatric ADHD behavioral attention datasets, and sensory cognitive metrics.",
        "source": "https://www.statnews.com/2024/05/29/akili-interactive-video-game-therapeutics-sale-virtual-therapeutics/",
        "persons": [
            ("Eddie Martucci", "Co-Founder & Former CEO", "eddie@akiliinteractive.com", "https://www.linkedin.com/in/eddiemartucci", "Co-founder & CEO; pioneer of prescription digital medicine for cognitive health"),
            ("Matt Omernick", "Co-Founder & Chief Creative Officer", "matt@akiliinteractive.com", "https://www.linkedin.com/in/mattomernick", "Former LucasArts creative director; gaming interface neuro-designer"),
            ("Santosh Shanbhag", "Chief Financial Officer", "santosh@akiliinteractive.com", "https://www.linkedin.com/in/santosh-shanbhag", "CFO overseeing transaction with Virtual Therapeutics")
        ]
    },
    {
        "company": "SmileDirectClub (Chapter 7 Liquidation / 3D Dental)",
        "domain": "smiledirectclub.com",
        "category": "Data Brokering",
        "data_value": "Over 2 million 3D intraoral dental scans, custom clear aligner CAD models, orthodontic progression photogrammetry, and patient dental treatment records.",
        "source": "https://www.cnn.com/2023/12/09/business/smiledirectclub-shutting-down/index.html",
        "persons": [
            ("David Katzman", "Former CEO", "david@smiledirectclub.com", "https://www.linkedin.com/in/david-katzman", "Former CEO; scaled global direct-to-consumer teledentistry platform"),
            ("Alex Fenkell", "Co-Founder", "alex@smiledirectclub.com", "https://www.linkedin.com/in/alexfenkell", "Co-founder; developed digital smile progression modeling pipeline"),
            ("Russell Perry", "Chapter 7 Liquidation Trustee", "trustee@smiledirectclub.com", "https://www.linkedin.com/in/smiledirect-estate", "Chapter 7 trustee managing intellectual property and proprietary 3D CAD assets")
        ]
    },

    # --- FINTECH, FREIGHT & PROPTECH FAILURES ---
    {
        "company": "Synapse Financial Technologies (Chapter 11 Bankruptcy)",
        "domain": "synapsefi.com",
        "category": "Data Brokering",
        "data_value": "Banking-as-a-Service core ledger transaction databases, ACH/wire routing logs, consumer debit card interchange datasets.",
        "source": "https://techcrunch.com/2024/04/22/fintech-middleman-synapse-files-for-chapter-11-bankruptcy/",
        "persons": [
            ("Sankaet Pathak", "Founder & Former CEO", "sankaet@synapsefi.com", "https://www.linkedin.com/in/sankaet", "Founder & CEO; architect of developer banking API infrastructure"),
            ("Jelena McWilliams", "Chapter 11 Chapter Trustee / Former FDIC Chair", "trustee@synapsefi.com", "https://www.linkedin.com/in/jelenamcwilliams", "Court-appointed bankruptcy trustee managing reconciliation and asset transfer"),
            ("Bryan K. O'Hara", "General Counsel", "bryan@synapsefi.com", "https://www.linkedin.com/in/bryanohara", "Legal counsel managing fintech regulatory and estate compliance")
        ]
    },
    {
        "company": "Shift Technologies (Chapter 11 / Automotive Data)",
        "domain": "shift.com",
        "category": "Data Brokering",
        "data_value": "Hundreds of thousands of vehicle mechanical inspection records, paint-depth and diagnostic OBD-II scan logs, algorithmic valuation models.",
        "source": "https://www.reuters.com/business/autos-transportation/online-used-car-retailer-shift-technologies-files-chapter-11-bankruptcy-2023-10-10/",
        "persons": [
            ("Ayman Khammash", "Chief Executive Officer", "ayman@shift.com", "https://www.linkedin.com/in/aymankhammash", "CEO directing Chapter 11 wind-down and asset monetization"),
            ("George Arison", "Co-Founder & Former CEO", "george@shift.com", "https://www.linkedin.com/in/georgearison", "Co-founder; automotive e-commerce algorithmic pricing architect"),
            ("Jason Krikorian", "Board Member & Advisor", "jason@shift.com", "https://www.linkedin.com/in/jasonkrikorian", "General Partner at DCM; board director overseeing restructuring")
        ]
    },
    {
        "company": "Vroom (E-Commerce Operations Wind-Down)",
        "domain": "vroom.com",
        "category": "Data Brokering",
        "data_value": "Massive used automobile purchasing and sale price history, proprietary title defect records, reconditioning cost models.",
        "source": "https://www.wsj.com/articles/online-used-car-retailer-vroom-to-halt-e-commerce-operations-wind-down-used-vehicle-business-c19eb9bf",
        "persons": [
            ("Tom Shortt", "Chief Executive Officer", "tom.shortt@vroom.com", "https://www.linkedin.com/in/tom-shortt", "CEO leading restructuring to preserve analytics and United Auto Credit corp"),
            ("Robert Krakowiak", "Chief Financial Officer", "robert.krakowiak@vroom.com", "https://www.linkedin.com/in/robert-krakowiak", "CFO managing debt obligations and wind-down capital allocation"),
            ("Patricia Moran", "Chief Legal Officer", "patricia.moran@vroom.com", "https://www.linkedin.com/in/patriciamoran", "CLO handling regulatory and commercial asset transactions")
        ]
    },
    {
        "company": "Prime Trust (Chapter 11 / Custodial Datasets)",
        "domain": "primetrust.com",
        "category": "Data Brokering",
        "data_value": "Cryptocurrency wallet addresses, institutional KYC compliance logs, multi-sig escrow transaction records, and fiat on/off-ramp datasets.",
        "source": "https://www.coindesk.com/policy/2023/08/15/crypto-custodian-prime-trust-files-for-chapter-11-bankruptcy/",
        "persons": [
            ("Jor Law", "Interim CEO & Restructuring Lead", "jor@primetrust.com", "https://www.linkedin.com/in/jorlaw", "Interim CEO appointed to navigate Chapter 11 and manage customer asset claims"),
            ("Rodrigo Gomez", "Chief Financial Officer", "rodrigo@primetrust.com", "https://www.linkedin.com/in/rodrigo-gomez", "CFO analyzing balance sheet assets and liabilities for court filings"),
            ("Jeremy Caulfield", "Chief Compliance Officer", "jeremy@primetrust.com", "https://www.linkedin.com/in/jeremy-caulfield", "CCO managing financial crimes enforcement and custodial compliance data")
        ]
    },
    {
        "company": "BlockFi (Chapter 11 Liquidation)",
        "domain": "blockfi.com",
        "category": "Data Brokering",
        "data_value": "Institutional crypto lending transaction logs, collateralization histories, trading desk execution telemetry, and verified KYC database.",
        "source": "https://www.reuters.com/technology/crypto-lender-blockfi-files-bankruptcy-2022-11-28/",
        "persons": [
            ("Zac Prince", "Founder & Former CEO", "zac@blockfi.com", "https://www.linkedin.com/in/zacprince", "Founder & CEO; architect of institutional crypto credit platform"),
            ("Flori Marquez", "Co-Founder & Former SVP", "flori@blockfi.com", "https://www.linkedin.com/in/flori-marquez", "Co-founder; led retail and enterprise lending product operations"),
            ("Mark Renzi", "Chief Restructuring Officer (BRG)", "mrenzi@thinkbrg.com", "https://www.linkedin.com/in/mark-renzi-brg", "Managing Director at Berkeley Research Group; court CRO handling asset sales")
        ]
    },
    {
        "company": "Frank (Financial Aid Platform / Liquidated)",
        "domain": "withfrank.org",
        "category": "Data Brokering",
        "data_value": "US collegiate financial aid FAFSA applications, student demographics, household income tiers, and higher education tuition datasets.",
        "source": "https://www.wsj.com/articles/jpmorgan-chase-sues-founder-of-college-financial-aid-startup-frank-11673479155",
        "persons": [
            ("Charlie Javice", "Founder & Former CEO", "charlie@withfrank.org", "https://www.linkedin.com/in/charliejavice", "Founder & CEO; creator of simplified financial aid application tool"),
            ("Olivier Amar", "Chief Growth Officer", "olivier@withfrank.org", "https://www.linkedin.com/in/olivieramar", "Growth lead overseeing collegiate outreach and university student databases"),
            ("Arthur Miller", "Bankruptcy Trustee / Legal Counsel", "counsel@withfrank.org", "https://www.linkedin.com/in/frank-legal-estate", "Estate advisor overseeing liquidation of non-infringing tech assets")
        ]
    },
    {
        "company": "Veev (Liquidated Modular PropTech)",
        "domain": "veev.com",
        "category": "Data Brokering",
        "data_value": "$1B+ valuation; detailed Building Information Modeling (BIM) architectural CAD, automated prefabricated panel structural testing datasets.",
        "source": "https://techcrunch.com/2023/11/27/veev-modular-construction-unicorn-shuts-down/",
        "persons": [
            ("Amit Haller", "Co-Founder & Former CEO", "amit@veev.com", "https://www.linkedin.com/in/amithaller", "Co-founder & CEO; developed vertically integrated modular residential technology"),
            ("Ami Avrahami", "Co-Founder & Chief Product Officer", "ami@veev.com", "https://www.linkedin.com/in/ami-avrahami-705b225", "Co-founder & CPO; digital fab and structural component engineering designer"),
            ("Kelly Wechter", "Chief Financial Officer", "kelly@veev.com", "https://www.linkedin.com/in/kelly-wechter", "CFO managing receiver liquidation proceedings and patent portfolio divestiture")
        ]
    },

    # --- AI, HARDWARE, MOBILITY & CONSUMER TECH FAILURES ---
    {
        "company": "Humane (Struggling Ai Pin / Assets for Sale)",
        "domain": "hu.ma.ne",
        "category": "Data Brokering",
        "data_value": "Extensive wearable multimodal ego-centric camera video footage, real-world voice queries, gesture tracking point clouds, and CosmOS telemetry.",
        "source": "https://www.bloomberg.com/news/articles/2024-05-22/humane-ai-pin-maker-seeking-sale-for-as-much-as-1-billion",
        "persons": [
            ("Imran Chaudhri", "Co-Founder & Chairman", "imran@hu.ma.ne", "https://www.linkedin.com/in/imranchaudhri", "Co-founder; former Apple design director who designed iPhone interface"),
            ("Bethany Bongiorno", "Co-Founder & Chief Executive Officer", "bethany@hu.ma.ne", "https://www.linkedin.com/in/bethanybongiorno", "Co-founder & CEO; former Apple director of software engineering for iOS/macOS"),
            ("Ken Kocienda", "Head of Product Engineering", "ken@hu.ma.ne", "https://www.linkedin.com/in/kenkocienda", "Author of Creative Selection; lead software architect of AI Pin system")
        ]
    },
    {
        "company": "Rabbit Inc. (Struggling LAM / Hardware Distress)",
        "domain": "rabbit.tech",
        "category": "Data Brokering",
        "data_value": "Large Action Model (LAM) web-agent navigation traces, mobile companion conversational queries, and multimodal visual search datasets.",
        "source": "https://techcrunch.com/2024/05/01/rabbit-r1-launch-reviews-future/",
        "persons": [
            ("Jesse Lyu", "Founder & CEO", "jesse@rabbit.tech", "https://www.linkedin.com/in/jesselyu", "Founder & CEO; pioneer of voice-action hardware and web-automation agents"),
            ("Peiyu Chen", "Head of AI Research & Models", "peiyu@rabbit.tech", "https://www.linkedin.com/in/peiyu-chen", "Lead AI scientist developing Large Action Model training corpora"),
            ("Yixing Wang", "Head of Engineering", "yixing@rabbit.tech", "https://www.linkedin.com/in/yixing-wang", "Engineering lead managing rabbit OS cloud virtualization infrastructure")
        ]
    },
    {
        "company": "Rewind AI / Limitless (Wearable Pendant Distress)",
        "domain": "limitless.ai",
        "category": "Data Brokering",
        "data_value": "Over 10,000+ hours of opt-in personal meeting audio transcripts, screen-recording OCR text corpora, and desktop productivity multimodal telemetry.",
        "source": "https://techcrunch.com/2024/04/15/rewind-rebrands-to-limitless-and-announces-a-pendant-for-transcribing-real-world-conversations/",
        "persons": [
            ("Dan Siroker", "Founder & CEO", "dan@limitless.ai", "https://www.linkedin.com/in/dsiroker", "Founder & CEO; former Optimizely founder and White House director of analytics"),
            ("Brett Bejcek", "Head of Product", "brett@limitless.ai", "https://www.linkedin.com/in/brettbejcek", "Product lead directing audio transcription and real-time meeting synthesis"),
            ("Paul McKellar", "Co-Founder & Advisor", "paul@limitless.ai", "https://www.linkedin.com/in/paulmckellar", "Co-founder; founding designer of Square and developer infrastructure")
        ]
    },
    {
        "company": "Tome AI (Generative Document Layoffs / Distress)",
        "domain": "tome.app",
        "category": "Data Brokering",
        "data_value": "Millions of AI-generated enterprise slide decks, structured layout trees, visual presentation engagement telemetry, and multimodal prompt pairings.",
        "source": "https://techcrunch.com/2024/05/17/ai-presentation-startup-tome-lays-off-20-of-staff-as-it-pivots-to-sales-pitches/",
        "persons": [
            ("Keith Peiris", "Co-Founder & CEO", "keith@tome.app", "https://www.linkedin.com/in/keithpeiris", "Co-founder & CEO; former product lead at Instagram and Meta"),
            ("Henri Liriani", "Co-Founder & Head of Product", "henri@tome.app", "https://www.linkedin.com/in/henriliriani", "Co-founder; former product designer at Meta and Messenger"),
            ("Mark Gurevich", "Head of Engineering", "mark@tome.app", "https://www.linkedin.com/in/markgurevich", "VP Engineering overseeing generative canvas AI models and cloud renderers")
        ]
    },
    {
        "company": "Tupelo / Gro Intelligence (Climate Data Shutdown)",
        "domain": "gro-intelligence.com",
        "category": "Data Brokering",
        "data_value": "$100M+ invested; world's largest agricultural and climate time-series database, satellite drought monitoring models, and global grain yield forecasts.",
        "source": "https://agfundernews.com/exclusive-gro-intelligence-to-shut-down-after-failed-funding-effort",
        "persons": [
            ("Sara Menker", "Founder & Former CEO", "sara@gro-intelligence.com", "https://www.linkedin.com/in/saramenker", "Founder & CEO; former Morgan Stanley commodities trader who built global food security AI"),
            ("James Frank", "Chief Operating Officer", "james@gro-intelligence.com", "https://www.linkedin.com/in/james-frank-gro", "COO directing corporate wind-down and data IP licensing negotiations"),
            ("Gary Survis", "Interim Chief Executive Officer", "gary@gro-intelligence.com", "https://www.linkedin.com/in/garysurvis", "Interim CEO appointed during capital restructuring and asset auction")
        ]
    },
    {
        "company": "InVision (Design Collaboration Full Shutdown)",
        "domain": "invisionapp.com",
        "category": "Data Brokering",
        "data_value": "Former $2B unicorn; immense UI/UX digital design component libraries, interactive click-through prototyping graphs, and design system tokens.",
        "source": "https://techcrunch.com/2024/01/04/invision-is-shutting-down/",
        "persons": [
            ("Clark Valberg", "Co-Founder & Former CEO", "clark@invisionapp.com", "https://www.linkedin.com/in/clarkvalberg", "Co-founder & former CEO; pioneered cloud UI/UX design collaboration"),
            ("Jeff Chow", "Chief Executive Officer", "jeff.chow@invisionapp.com", "https://www.linkedin.com/in/jeffchow", "CEO who managed Freehand acquisition by Miro and orderly platform shutdown"),
            ("Michael Shenkman", "Chief Financial Officer & Restructuring Lead", "michael@invisionapp.com", "https://www.linkedin.com/in/michael-shenkman", "CFO overseeing entity wrap-up, asset monetization, and customer offboarding")
        ]
    },
    {
        "company": "Byju's (Think & Learn - Insolvency Proceedings)",
        "domain": "byjus.com",
        "category": "Data Brokering",
        "data_value": "Peak $22B edtech valuation; 150 million student learning sessions, K-12 math/science conceptual assessment responses, and video lecture transcripts.",
        "source": "https://www.reuters.com/world/india/indias-byjus-faces-insolvency-court-orders-bankruptcy-process-2024-07-16/",
        "persons": [
            ("Byju Raveendran", "Founder & Group CEO", "byju@byjus.com", "https://www.linkedin.com/in/byju-raveendran", "Founder & CEO of Think & Learn Private Limited"),
            ("Divya Gokulnath", "Co-Founder & Director", "divya@byjus.com", "https://www.linkedin.com/in/divya-gokulnath", "Co-founder leading educational content development and pedagogy"),
            ("Pankaj Srivastava", "Insolvency Resolution Professional (IRP)", "irp@byjus.com", "https://www.linkedin.com/in/pankaj-srivastava-irp", "NCLT court-appointed Interim Resolution Professional managing corporate insolvency process")
        ]
    },
    {
        "company": "Lilium (Insolvency Proceedings / eVTOL Aerospace)",
        "domain": "lilium.com",
        "category": "Data Brokering",
        "data_value": "Premier European electric vertical takeoff and landing (eVTOL) flight test telemetry, aerodynamic wind tunnel datasets, and battery pack CFD models.",
        "source": "https://www.reuters.com/business/aerospace-defense/german-air-taxi-maker-lilium-files-insolvency-units-2024-10-24/",
        "persons": [
            ("Klaus Roewe", "Chief Executive Officer", "klaus.roewe@lilium.com", "https://www.linkedin.com/in/klausroewe", "CEO; former Airbus A320 program leader directing aerospace restructuring"),
            ("Daniel Wiegand", "Co-Founder & Chief Engineer", "daniel.wiegand@lilium.com", "https://www.linkedin.com/in/daniel-wiegand-lilium", "Co-founder & Chief Engineer; inventor of Lilium Jet ducted-fan architecture"),
            ("Oliver Vogelgesang", "Chief Financial Officer", "oliver.vogelgesang@lilium.com", "https://www.linkedin.com/in/oliver-vogelgesang", "CFO navigating German self-administration insolvency proceedings")
        ]
    },
    {
        "company": "Arrival (UK Administration / Commercial EV)",
        "domain": "arrival.com",
        "category": "Data Brokering",
        "data_value": "$13B peak valuation; proprietary lightweight composite material testing datasets, microfactory robotics automation code, and electric van fleet telemetry.",
        "source": "https://techcrunch.com/2024/02/05/arrival-enters-administration-uk-ev-startup/",
        "persons": [
            ("Denis Sverdlov", "Founder & Former CEO", "denis@arrival.com", "https://www.linkedin.com/in/denissverdlov", "Founder; former Russian deputy minister and serial mobility entrepreneur"),
            ("Igor Torgov", "Former Chief Executive Officer", "igor.torgov@arrival.com", "https://www.linkedin.com/in/igor-torgov", "CEO who oversaw restructuring and administration transition"),
            ("Simon Edel", "Joint Administrator (EY Parthenon)", "sedel@uk.ey.com", "https://www.linkedin.com/in/simon-edel", "Partner at Ernst & Young LLP acting as court-appointed joint administrator")
        ]
    },
    {
        "company": "Fisker Inc. (Chapter 11 Bankruptcy / EV Automotive)",
        "domain": "fiskerinc.com",
        "category": "Data Brokering",
        "data_value": "Thousands of Fisker Ocean production vehicle telemetry logs, ADAS radar/camera sensor datasets, and battery management system (BMS) diagnostics.",
        "source": "https://www.reuters.com/business/autos-transportation/ev-maker-fisker-files-bankruptcy-after-talks-with-automaker-collapse-2024-06-18/",
        "persons": [
            ("Henrik Fisker", "Founder, Chairman & CEO", "henrik@fiskerinc.com", "https://www.linkedin.com/in/henrikfisker", "Iconic automotive designer & CEO; designed Aston Martin DB9 and Fisker Ocean"),
            ("Geeta Gupta-Fisker", "Co-Founder, CFO & COO", "geeta@fiskerinc.com", "https://www.linkedin.com/in/geetaguptafisker", "Co-founder, CFO & COO directing operations and Magna manufacturing contracts"),
            ("John DiDonato", "Chief Restructuring Officer (Huron)", "jdidonato@huronconsultinggroup.com", "https://www.linkedin.com/in/john-didonato", "Managing Director at Huron; appointed CRO leading Chapter 11 asset liquidation")
        ]
    },
    {
        "company": "Lordstown Motors (Chapter 11 / Electric Trucks)",
        "domain": "lordstownmotors.com",
        "category": "Data Brokering",
        "data_value": "Full-size commercial electric pickup truck hub-motor telemetry, crash safety simulations, and Lordstown assembly plant stamping CAD models.",
        "source": "https://www.reuters.com/business/autos-transportation/lordstown-motors-files-bankruptcy-sues-foxconn-2023-06-27/",
        "persons": [
            ("Edward Hightower", "Chief Executive Officer & President", "edward.hightower@lordstownmotors.com", "https://www.linkedin.com/in/edward-hightower", "CEO & automotive veteran; oversaw commercial launch of Endurance EV truck"),
            ("Adam Kroll", "Chief Financial Officer", "adam.kroll@lordstownmotors.com", "https://www.linkedin.com/in/adam-kroll", "CFO managing Chapter 11 reorganization and Foxconn litigation proceeds"),
            ("Melissa Leonard", "Executive VP & General Counsel", "melissa.leonard@lordstownmotors.com", "https://www.linkedin.com/in/melissa-leonard", "General Counsel directing intellectual property and patent auctions")
        ]
    },
    {
        "company": "Proterra (Chapter 11 / Fleet Battery Systems)",
        "domain": "proterra.com",
        "category": "Data Brokering",
        "data_value": "Over 40 million transit service miles of commercial electric bus telemetry, high-voltage battery degradation data, and megawatt-scale charging logs.",
        "source": "https://www.reuters.com/business/autos-transportation/ev-battery-maker-proterra-files-chapter-11-bankruptcy-2023-08-08/",
        "persons": [
            ("Gareth Joyce", "Chief Executive Officer", "gareth.joyce@proterra.com", "https://www.linkedin.com/in/gareth-joyce", "CEO directing business lines sale to Volvo Group and Phoenix Motorcars"),
            ("David Black", "Chief Financial Officer", "david.black@proterra.com", "https://www.linkedin.com/in/david-black-proterra", "CFO guiding Chapter 11 asset auction and creditor settlements"),
            ("Julian Soell", "Chief Operating Officer", "julian.soell@proterra.com", "https://www.linkedin.com/in/julian-soell", "COO overseeing transit vehicle manufacturing and battery production facilities")
        ]
    },
    {
        "company": "Skiff (End-to-End Encrypted Docs / Shuttered by Notion)",
        "domain": "skiff.com",
        "category": "Data Brokering",
        "data_value": "Decentralized document collaboration protocols, privacy-preserving cryptographic email architecture, and zero-knowledge synchronization telemetry.",
        "source": "https://techcrunch.com/2024/02/09/notion-acquires-privacy-focused-productivity-platform-skiff/",
        "persons": [
            ("Jason Ginsberg", "Co-Founder & Former CEO", "jason@skiff.com", "https://www.linkedin.com/in/jasonginsberg", "Co-founder & CEO; Stanford cryptography researcher who built Skiff platform"),
            ("Milap Patel", "Co-Founder & Former CTO", "milap@skiff.com", "https://www.linkedin.com/in/milappatel", "Co-founder & CTO; cryptographic engineering and private key management lead"),
            ("Samir Sen", "Head of Product", "samir@skiff.com", "https://www.linkedin.com/in/samir-sen", "Product designer directing encrypted workspace features and user transition")
        ]
    },
    {
        "company": "Jasper AI (Enterprise Copywriting Layoffs / Distress)",
        "domain": "jasper.ai",
        "category": "Data Brokering",
        "data_value": "Over 100,000 corporate marketing campaigns, multi-prompt performance benchmarks, style-guide fine-tuning corpora, and enterprise engagement metrics.",
        "source": "https://techcrunch.com/2023/07/14/jasper-ai-layoffs/",
        "persons": [
            ("Dave Rogenmoser", "Co-Founder & Former CEO", "dave@jasper.ai", "https://www.linkedin.com/in/daverogenmoser", "Co-founder & Chairman; led generative AI copywriter to unicorn status"),
            ("Timothy Young", "Chief Executive Officer", "timothy@jasper.ai", "https://www.linkedin.com/in/timothystephenyoung", "CEO; former President of Dropbox appointed to lead enterprise restructuring"),
            ("John Philip Morgan", "Co-Founder & Chief Technology Officer", "jp@jasper.ai", "https://www.linkedin.com/in/johnphilipmorgan", "Co-founder & CTO; designed prompt routing and model orchestration engine")
        ]
    },
    {
        "company": "Fable Studio / Showrunner (AI Simulation Distress)",
        "domain": "fablestudio.com",
        "category": "Data Brokering",
        "data_value": "Generative simulation datasets from 'South Park' AI experiment, multi-agent behavioral dialogue trees, and narrative autonomous character logs.",
        "source": "https://www.theverge.com/2024/5/30/24167699/showrunner-fable-simulation-generative-ai-episodes",
        "persons": [
            ("Edward Saatchi", "Founder & CEO", "edward@fablestudio.com", "https://www.linkedin.com/in/edwardsaatchi", "Founder & CEO; Emmy-winning director and creator of autonomous character simulation"),
            ("Pete Billington", "Director & Co-Founder", "pete@fablestudio.com", "https://www.linkedin.com/in/petebillington", "Co-founder; narrative AI interaction and VR storytelling pioneer"),
            ("Jessica Shamash", "Executive Producer", "jessica@fablestudio.com", "https://www.linkedin.com/in/jessicashamash", "Producer directing simulation testing and voice acting training dataset")
        ]
    },
    {
        "company": "Papercup (AI Dubbing Layoffs / Restructuring)",
        "domain": "papercup.com",
        "category": "Data Brokering",
        "data_value": "Massive human-verified expressive synthetic speech datasets, multi-language video dubbing alignment pairs, and emotional voice synthesis models.",
        "source": "https://techcrunch.com/2022/06/08/papercup-raises-20m-for-its-ai-powered-video-dubbing-tech/",
        "persons": [
            ("Jesse Shemen", "Co-Founder & CEO", "jesse@papercup.com", "https://www.linkedin.com/in/jesseshemen", "Co-founder & CEO; leading automated video localization platform"),
            ("Jiameng Gao", "Co-Founder & CTO", "jiameng@papercup.com", "https://www.linkedin.com/in/jiameng-gao-87989349", "Co-founder & CTO; machine learning and speech synthesis researcher"),
            ("Dan Biddle", "VP Partnerships", "dan.biddle@papercup.com", "https://www.linkedin.com/in/dan-biddle", "Commercial leader negotiating media licensing with broadcasters and creators")
        ]
    },
    {
        "company": "Volta Trucks (Electric Fleet Administration)",
        "domain": "voltatrucks.com",
        "category": "Data Brokering",
        "data_value": "Purpose-built 16-ton urban commercial EV truck route telemetry, driver central-seat visibility ergonomics datasets, and fleet battery telemetry.",
        "source": "https://www.reuters.com/business/autos-transportation/swedish-electric-truck-maker-volta-files-bankruptcy-2023-10-17/",
        "persons": [
            ("Essa Al-Saleh", "Chief Executive Officer", "essa.alsaleh@voltatrucks.com", "https://www.linkedin.com/in/essa-al-saleh", "CEO who directed international fleet trials and restructuring agreements"),
            ("Carl-Magnus Norden", "Founder", "carl@voltatrucks.com", "https://www.linkedin.com/in/carl-magnus-norden", "Founder; conceptualized zero-emission urban freight vehicle architecture"),
            ("Andrea Newman", "Joint Administrator / Insolvency Advisor", "administrator@voltatrucks.com", "https://www.linkedin.com/in/volta-administration", "Administrator managing commercial customer contracts and asset transfer")
        ]
    },
    {
        "company": "Kitty Hawk (Liquidated eVTOL Telemetry)",
        "domain": "kittyhawk.aero",
        "category": "Data Brokering",
        "data_value": "Over a decade of Google-funded experimental electric aircraft test flight data, autonomous aerodynamic flight control code, and vertiport telemetry.",
        "source": "https://techcrunch.com/2022/09/21/kitty-hawk-the-flying-car-company-backed-by-larry-page-is-shutting-down/",
        "persons": [
            ("Sebastian Thrun", "Co-Founder & Former CEO", "sebastian@kittyhawk.aero", "https://www.linkedin.com/in/sebastianthrun", "Founder of Google X, autonomous vehicle pioneer, and Kitty Hawk CEO"),
            ("Damon Vander Lind", "Chief Technology Officer", "damon@kittyhawk.aero", "https://www.linkedin.com/in/damon-vander-lind", "CTO; aeronautics and autonomous aircraft flight dynamics designer"),
            ("Sheri Kopp", "VP Human Resources & Estate Wrap-Up", "sheri@kittyhawk.aero", "https://www.linkedin.com/in/sherikopp", "Executive managing engineering team placement and patent disposition")
        ]
    },
    {
        "company": "Carbon Health (Urgent Care Clinic Downsizing)",
        "domain": "carbonhealth.com",
        "category": "Data Brokering",
        "data_value": "Millions of real-world patient urgent care encounter logs, EHR triage symptom trees, rapid diagnostic clinic telemetry, and billing records.",
        "source": "https://techcrunch.com/2023/01/06/carbon-health-layoffs-hardware/",
        "persons": [
            ("Eren Bali", "Co-Founder & CEO", "eren@carbonhealth.com", "https://www.linkedin.com/in/erenbali", "Founder & CEO; former founder of Udemy who built modern tech-enabled clinic network"),
            ("Caesar Djavaherian", "Co-Founder & Chief Clinical Officer", "caesar@carbonhealth.com", "https://www.linkedin.com/in/caesardjavaherian", "Emergency physician and clinical architect of Carbon Health patient care workflows"),
            ("Claire Hough", "Chief Technology Officer", "claire@carbonhealth.com", "https://www.linkedin.com/in/clairehough", "CTO overseeing proprietary EHR platform and diagnostic patient applications")
        ]
    },
    {
        "company": "Outcome Health (Liquidated Clinical Advertising)",
        "domain": "outcomehealth.com",
        "category": "Data Brokering",
        "data_value": "Over 40,000 physician waiting room and exam room digital wallboard interaction logs, patient dwell times, and medical education video analytics.",
        "source": "https://www.justice.gov/opa/pr/former-executives-outcome-health-sentenced-prison-1-billion-corporate-fraud-scheme",
        "persons": [
            ("Nandini Ramani", "Former Chief Operating Officer", "nandini@outcomehealth.com", "https://www.linkedin.com/in/nandiniramani", "Former Twitter VP who served as COO during post-crisis restructuring"),
            ("Matthew McNally", "Chief Executive Officer (Post-Restructuring)", "matthew@outcomehealth.com", "https://www.linkedin.com/in/matthew-mcnally", "Executive appointed to lead merger with PatientPoint and asset integration"),
            ("Michael O'Donnell", "Chief Restructuring Officer", "modonnell@outcomehealth.com", "https://www.linkedin.com/in/michael-odonnell-cro", "Restructuring officer managing regulatory escrow and remaining digital assets")
        ]
    }
,
    {
        "company": "TuSimple (US Wind-Down / Autonomous Trucking)",
        "domain": "tusimple.com",
        "category": "Data Brokering",
        "data_value": "Over 10 million autonomous freight miles, high-definition lidar highway point clouds, night-time driving camera vision datasets.",
        "source": "https://techcrunch.com/2024/01/17/autonomous-trucking-company-tusimple-delists-from-nasdaq-winds-down-us-ops/",
        "persons": [
                [
                        "Cheng Lu",
                        "President & Chief Executive Officer",
                        "cheng.lu@tusimple.com",
                        "https://www.linkedin.com/in/cheng-lu-tusimple",
                        "CEO leading corporate wind-down of US autonomous trucking operations"
                ],
                [
                        "Xiaodi Hou",
                        "Co-Founder & Former CTO",
                        "xiaodi.hou@tusimple.com",
                        "https://www.linkedin.com/in/xiaodihou",
                        "Co-founder & computer vision pioneer from Caltech"
                ],
                [
                        "Eric Tapia",
                        "Chief Financial Officer",
                        "eric.tapia@tusimple.com",
                        "https://www.linkedin.com/in/eric-tapia",
                        "CFO managing US capital disposition and creditor resolution"
                ]
        ]
},
    {
        "company": "Anki (Liquidated Consumer AI Robotics)",
        "domain": "anki.com",
        "category": "Data Brokering",
        "data_value": "Over 1.5 million connected Cozmo & Vector home robots, facial recognition logs, spatial SLAM navigation, and emotional behavioral telemetry.",
        "source": "https://www.theverge.com/2019/4/29/18523175/anki-robotics-shutting-down-cozmo-robot-layoffs-overdrive",
        "persons": [
                [
                        "Boris Sofman",
                        "Co-Founder & Former CEO",
                        "boris@anki.com",
                        "https://www.linkedin.com/in/bsofman",
                        "Co-founder & CEO; CMU Robotics PhD, currently leading Waymo trucking"
                ],
                [
                        "Mark Palatucci",
                        "Co-Founder & Chief Product Officer",
                        "mark@anki.com",
                        "https://www.linkedin.com/in/mark-palatucci",
                        "Co-founder & CPO; computer vision and robotics software architect"
                ],
                [
                        "Hanns Tappeiner",
                        "Co-Founder & President",
                        "hanns@anki.com",
                        "https://www.linkedin.com/in/hannstappeiner",
                        "Co-founder & President; consumer hardware and perception lead"
                ]
        ]
},
    {
        "company": "Jibo (Liquidated Social Robot Telemetry)",
        "domain": "jibo.com",
        "category": "Data Brokering",
        "data_value": "World's first consumer social robot interaction logs, multimodal family speech recognition, 3-axis expressive motor control kinetics.",
        "source": "https://spectrum.ieee.org/jibo-the-social-robot-is-shutting-down-its-servers",
        "persons": [
                [
                        "Cynthia Breazeal",
                        "Founder & Chief Scientist",
                        "cynthia@jibo.com",
                        "https://www.linkedin.com/in/cynthiabreazeal",
                        "MIT Media Lab professor and pioneer of human-robot interaction"
                ],
                [
                        "Steve Chambers",
                        "Former Chief Executive Officer",
                        "steve@jibo.com",
                        "https://www.linkedin.com/in/stevechambers",
                        "Former CEO who led enterprise partnership and restructuring"
                ],
                [
                        "Jonathan Ross",
                        "VP Software & AI",
                        "jonathan@jibo.com",
                        "https://www.linkedin.com/in/jonathan-ross-jibo",
                        "Lead software architect for companion AI conversational agents"
                ]
        ]
},
    {
        "company": "Light.co (Light Labs - Liquidated Computational Photography)",
        "domain": "light.co",
        "category": "Data Brokering",
        "data_value": "Over $150M invested; 16-lens multi-aperture array camera raw imagery, synthetic depth maps, sub-millimeter multi-camera disparity point clouds.",
        "source": "https://www.theverge.com/2020/6/12/21289139/light-quits-smartphone-camera-business-l16-sensors",
        "persons": [
                [
                        "Dave Grannan",
                        "Co-Founder & Former CEO",
                        "dave@light.co",
                        "https://www.linkedin.com/in/davegrannan",
                        "Co-founder & CEO; pioneered computational camera hardware array"
                ],
                [
                        "Rajiv Laroia",
                        "Co-Founder & Chief Technology Officer",
                        "rajiv@light.co",
                        "https://www.linkedin.com/in/rajiv-laroia",
                        "Co-founder & CTO; Bell Labs fellow and inventor of Flash-OFDM"
                ],
                [
                        "Paul White",
                        "VP Automotive & Commercial",
                        "paul.white@light.co",
                        "https://www.linkedin.com/in/paul-white-light",
                        "Commercial lead for ADAS and autonomous vehicle multi-camera vision"
                ]
        ]
},
    {
        "company": "Volansi (Liquidated Commercial VTOL Drone Logistics)",
        "domain": "volansi.com",
        "category": "Data Brokering",
        "data_value": "Long-range autonomous vertical takeoff cargo drone flight telemetry, remote landing pad precision vision, offshore logistics flight corridors.",
        "source": "https://dronelife.com/2022/05/27/volansi-shuts-down-assets-sold/",
        "persons": [
                [
                        "Hannan Parvizian",
                        "Co-Founder & Former CEO",
                        "hannan@volansi.com",
                        "https://www.linkedin.com/in/hannan-parvizian",
                        "Founder & CEO; Tesla manufacturing engineer who built heavy-lift cargo drones"
                ],
                [
                        "Wesley Stearns",
                        "Co-Founder & Chief Technology Officer",
                        "wesley@volansi.com",
                        "https://www.linkedin.com/in/wesley-stearns",
                        "Co-founder & CTO; autonomous flight control and autopilot designer"
                ],
                [
                        "Robert Rose",
                        "Chief Operating Officer",
                        "robert@volansi.com",
                        "https://www.linkedin.com/in/robert-rose-volansi",
                        "COO directing Department of Defense and commercial cargo trials"
                ]
        ]
},
    {
        "company": "Navya (French Autonomous Shuttle Receivership)",
        "domain": "navya.tech",
        "category": "Data Brokering",
        "data_value": "Over 200 public-road autonomous passenger shuttles deployed globally, multi-lidar urban localization point clouds, pedestrian obstacle tracking.",
        "source": "https://www.reuters.com/business/autos-transportation/french-driverless-shuttle-maker-navya-files-receivership-2023-02-01/",
        "persons": [
                [
                        "Sophie Desormiere",
                        "Former Chief Executive Officer",
                        "sophie.desormiere@navya.tech",
                        "https://www.linkedin.com/in/sophie-desormiere",
                        "Former CEO leading Euronext restructuring and asset sale to Macnica"
                ],
                [
                        "Olivier Le Cornec",
                        "Chief Technology Officer",
                        "olivier.lecornec@navya.tech",
                        "https://www.linkedin.com/in/olivier-le-cornec",
                        "CTO leading level 4 autonomous shuttle perception and drive-by-wire"
                ],
                [
                        "Pierre Lahutte",
                        "Special Restructuring Advisor",
                        "pierre.lahutte@navya.tech",
                        "https://www.linkedin.com/in/pierrelahutte",
                        "Industrial advisor guiding commercial handover and IP licensing"
                ]
        ]
},
    {
        "company": "May Mobility (Autonomous Shuttle Restructuring)",
        "domain": "maymobility.com",
        "category": "Data Brokering",
        "data_value": "Over 350,000 public autonomous passenger rides, multi-policy autonomous driving decision models, dense urban micro-transit sensor streams.",
        "source": "https://techcrunch.com/2023/11/08/may-mobility-raises-105m-autonomous-driving-toyota-ntt/",
        "persons": [
                [
                        "Edwin Olson",
                        "Co-Founder & CEO",
                        "edwin@maymobility.com",
                        "https://www.linkedin.com/in/edwin-olson",
                        "Founder & CEO; University of Michigan robotics professor and DARPA Urban Challenge lead"
                ],
                [
                        "Alisyn Malek",
                        "Co-Founder & Former COO",
                        "alisyn@maymobility.com",
                        "https://www.linkedin.com/in/alisynmalek",
                        "Co-founder; former GM automotive engineer directing city transit partnerships"
                ],
                [
                        "Steve Greenfield",
                        "VP Commercial Development",
                        "steve@maymobility.com",
                        "https://www.linkedin.com/in/stevegreenfield",
                        "Commercial partnerships lead for transit agency deployments"
                ]
        ]
},
    {
        "company": "Essential Products (Ambient OS & Smartphone Shuttered)",
        "domain": "essential.com",
        "category": "Data Brokering",
        "data_value": "$330M venture funding; modular hardware attachment bus protocols, Ambient OS smart home integration code, titanium phone manufacturing CAD.",
        "source": "https://techcrunch.com/2020/02/12/essential-shutting-down/",
        "persons": [
                [
                        "Andy Rubin",
                        "Founder & Former CEO",
                        "andy@essential.com",
                        "https://www.linkedin.com/in/andyrubin",
                        "Creator of Android; founded Essential to build open ambient intelligence hardware"
                ],
                [
                        "Jason Keats",
                        "Head of Product Design",
                        "jason@essential.com",
                        "https://www.linkedin.com/in/jasonkeats",
                        "Former Apple iPad mechanical engineering lead; designer of Essential Phone"
                ],
                [
                        "Rebecca Zavin",
                        "VP Software Engineering",
                        "rebecca@essential.com",
                        "https://www.linkedin.com/in/rebeccazavin",
                        "Former Google Android senior staff engineer leading Essential OS"
                ]
        ]
},
    {
        "company": "Volocopter (Struggling German eVTOL / Emergency Funding)",
        "domain": "volocopter.com",
        "category": "Data Brokering",
        "data_value": "Full-scale 18-rotor multi-copter eVTOL flight acoustic profiles, urban vertiport wind tunnel data, certified fly-by-wire aviation telemetry.",
        "source": "https://www.reuters.com/business/aerospace-defense/german-air-taxi-firm-volocopter-talks-with-chinese-investors-2024-11-12/",
        "persons": [
                [
                        "Dirk Hoke",
                        "Chief Executive Officer",
                        "dirk.hoke@volocopter.com",
                        "https://www.linkedin.com/in/dirkhoke",
                        "CEO; former CEO of Airbus Defence and Space navigating capital restructuring"
                ],
                [
                        "Alexander Zosel",
                        "Co-Founder & Innovation Lead",
                        "alex@volocopter.com",
                        "https://www.linkedin.com/in/alexander-zosel",
                        "Co-founder; pioneer of multicopter flight who completed first manned eVTOL flight"
                ],
                [
                        "Christian Bauer",
                        "Chief Financial Officer & CCO",
                        "christian.bauer@volocopter.com",
                        "https://www.linkedin.com/in/christian-bauer-volo",
                        "CFO overseeing global airline and city commercial contracts"
                ]
        ]
},
    {
        "company": "Pebble / Core Health (Liquidated Wearable Biomarkers)",
        "domain": "pebble.com",
        "category": "Data Brokering",
        "data_value": "Over 2 million user continuous optical heart-rate traces, multi-year sleep staging logs, step accelerometer time-series corpora.",
        "source": "https://www.theverge.com/2016/12/7/13867086/pebble-smartwatch-fitbit-acquisition-canceled-refunds",
        "persons": [
                [
                        "Eric Migicovsky",
                        "Founder & Former CEO",
                        "eric@pebble.com",
                        "https://www.linkedin.com/in/ericmigicovsky",
                        "Founder & CEO; pioneer of modern smartwatch category, founder of Beeper"
                ],
                [
                        "Kean Wong",
                        "VP Software Engineering",
                        "kean@pebble.com",
                        "https://www.linkedin.com/in/keanwong",
                        "VP Software leading PebbleOS and developer firmware ecosystem"
                ],
                [
                        "Steve Johns",
                        "Chief Financial Officer",
                        "steve@pebble.com",
                        "https://www.linkedin.com/in/steve-johns-pebble",
                        "CFO who negotiated asset transaction with Fitbit"
                ]
        ]
},
    {
        "company": "DeepBench (Expert Network Interview Library)",
        "domain": "deepbench.io",
        "category": "Data Brokering",
        "data_value": "Thousands of transcribed expert consulting calls with enterprise executives across semiconductor, cloud, medical device, and software verticals.",
        "source": "https://www.crunchbase.com/organization/deepbench",
        "persons": [
                [
                        "Yishi Zuo",
                        "Co-Founder & CEO",
                        "yishi@deepbench.io",
                        "https://www.linkedin.com/in/yishizuo",
                        "MIT Sloan founder who created transparent expert consulting platform"
                ],
                [
                        "Derek Hans",
                        "Co-Founder & Head of Product",
                        "derek@deepbench.io",
                        "https://www.linkedin.com/in/derekhans",
                        "Co-founder leading expert matching algorithm and transcript repository"
                ],
                [
                        "Devin Finzer",
                        "Advisor & Early Team",
                        "devin@deepbench.io",
                        "https://www.linkedin.com/in/devinfinzer",
                        "Early advisor; tech platform architect"
                ]
        ]
},
    {
        "company": "Matternet (Struggling Medical Drone Logistics)",
        "domain": "mttr.net",
        "category": "Data Brokering",
        "data_value": "FAA Part 135 certified medical delivery drone flight logs, hospital campus vertipad precision optical telemetry, urban airspace routing datasets.",
        "source": "https://techcrunch.com/2023/12/20/drone-delivery-matternet-layoffs/",
        "persons": [
                [
                        "Andreas Raptopoulos",
                        "Founder & CEO",
                        "andreas@mttr.net",
                        "https://www.linkedin.com/in/andreasraptopoulos",
                        "Founder & CEO; Royal College of Art designer who created autonomous drone logistics"
                ],
                [
                        "Jim O'Sullivan",
                        "VP Regulatory Strategy & Airspace",
                        "jim@mttr.net",
                        "https://www.linkedin.com/in/jim-osullivan",
                        "Aviation regulatory leader who secured first FAA Standard Type Certification for delivery drones"
                ],
                [
                        "Ilan Steemers",
                        "VP Engineering",
                        "ilan@mttr.net",
                        "https://www.linkedin.com/in/ilansteemers",
                        "VP Engineering overseeing aircraft flight avionics and base station docking"
                ]
        ]
},
    {
        "company": "Kangaroo Health (Remote Patient Monitoring Telemetry)",
        "domain": "kangaroohealth.com",
        "category": "Data Brokering",
        "data_value": "Tens of thousands of chronic disease patient biometric telemetry streams, blood pressure, pulse oximetry, and clinical nurse triage intervention notes.",
        "source": "https://www.crunchbase.com/organization/kangaroohealth",
        "persons": [
                [
                        "Xiaoxu Kang",
                        "Founder & CEO",
                        "kang@kangaroohealth.com",
                        "https://www.linkedin.com/in/xiaoxukang",
                        "Johns Hopkins biomedical engineer & CEO who built AI remote patient platform"
                ],
                [
                        "Michael Lin",
                        "Chief Medical Officer",
                        "michael@kangaroohealth.com",
                        "https://www.linkedin.com/in/michael-lin-md",
                        "Cardiologist directing chronic care clinical pathways and telemetry protocols"
                ],
                [
                        "David Zhao",
                        "Head of Data Science",
                        "david@kangaroohealth.com",
                        "https://www.linkedin.com/in/david-zhao-data",
                        "Lead data scientist developing early patient deterioration warning models"
                ]
        ]
},
    {
        "company": "uBiome (Liquidated Microbiome Sequencing Database)",
        "domain": "ubiome.com",
        "category": "Data Brokering",
        "data_value": "Over 250,000 human gut and oral microbiome 16S rRNA gene sequencing samples, longitudinal dietary lifestyle metadata, and microbial taxonomy databases.",
        "source": "https://www.reuters.com/article/business/healthcare-pharmaceuticals/ubiome-files-for-bankruptcy-four-months-after-fbi-raid-idUSKCN1VP2SN/",
        "persons": [
                [
                        "Jessica Richman",
                        "Co-Founder & Former CEO",
                        "jessica@ubiome.com",
                        "https://www.linkedin.com/in/jessicarichman",
                        "Oxford PhD fellow and co-founder of citizen-science microbiome sequencing"
                ],
                [
                        "Zachary Apte",
                        "Co-Founder & Former CTO",
                        "zac@ubiome.com",
                        "https://www.linkedin.com/in/zac-apte",
                        "UCSF biophysics PhD who developed high-throughput 16S sequencing chemistry"
                ],
                [
                        "David F. Grogan",
                        "Bankruptcy Trustee / Estate Liquidator",
                        "trustee@ubiome.com",
                        "https://www.linkedin.com/in/ubiome-trustee",
                        "Court-appointed Chapter 7 trustee administering genomic dataset licensing"
                ]
        ]
},
    {
        "company": "LendUp (Consumer Credit Underwriting ML Telemetry)",
        "domain": "lendup.com",
        "category": "Data Brokering",
        "data_value": "Millions of subprime consumer installment loan repayment histories, alternative data underwriting credit scores, and financial literacy engagement logs.",
        "source": "https://www.consumerfinance.gov/about-us/newsroom/cfpb-halts-lendup-loans-for-violating-order-and-deceiving-borrowers/",
        "persons": [
                [
                        "Sasha Orloff",
                        "Co-Founder & Former CEO",
                        "sasha@lendup.com",
                        "https://www.linkedin.com/in/sashaorloff",
                        "Co-founder & CEO; former World Bank microfinance specialist, founder of Puzzle"
                ],
                [
                        "Jeff Stewart",
                        "Co-Founder & CTO",
                        "jeff@lendup.com",
                        "https://www.linkedin.com/in/jeff-stewart-lendup",
                        "Co-founder & CTO; machine learning underwriting algorithm designer"
                ],
                [
                        "Anu Shultes",
                        "Chief Executive Officer (Post-Restructuring)",
                        "anu@lendup.com",
                        "https://www.linkedin.com/in/anushultes",
                        "Consumer finance executive who directed entity wind-down and asset disposition"
                ]
        ]
},
    {
        "company": "Lantern (Digital Cognitive Behavioral Therapy Shuttered)",
        "domain": "golantern.com",
        "category": "Data Brokering",
        "data_value": "Clinical evidence-based CBT digital interactive modules, anxiety and depression self-assessment symptom progression, patient journal sentiment datasets.",
        "source": "https://techcrunch.com/2018/08/01/lantern-mental-health-shuts-down/",
        "persons": [
                [
                        "Alejandro Foung",
                        "Co-Founder & Former CEO",
                        "alejandro@golantern.com",
                        "https://www.linkedin.com/in/alejandrofoung",
                        "Co-founder & CEO; former Trulia executive who built clinical therapy platform"
                ],
                [
                        "Nick Taylor",
                        "Chief Clinical Officer",
                        "nick@golantern.com",
                        "https://www.linkedin.com/in/nicktaylorcbt",
                        "Clinical psychologist who translated Stanford CBT research into digital programs"
                ],
                [
                        "David Boudreau",
                        "VP Engineering",
                        "david@golantern.com",
                        "https://www.linkedin.com/in/david-boudreau",
                        "VP Engineering overseeing HIPAA compliant clinical progress data stores"
                ]
        ]
},
    {
        "company": "Kaedim (3D Mesh AI Training Datasets)",
        "domain": "kaedim3d.com",
        "category": "Data Brokering",
        "data_value": "Hundreds of thousands of 2D concept art sketches paired with human-refined production-ready 3D polygon meshes, quad-topology UV mapping corpora.",
        "source": "https://techcrunch.com/2024/03/11/kaedim-raises-15m-to-generate-3d-models-with-ai/",
        "persons": [
                [
                        "Konstantina Psoma",
                        "Founder & CEO",
                        "konstantina@kaedim3d.com",
                        "https://www.linkedin.com/in/konstantina-psoma",
                        "Founder & CEO; Bristol computer science and 3D vision researcher"
                ],
                [
                        "Roman Bromidge",
                        "Chief Technology Officer",
                        "roman@kaedim3d.com",
                        "https://www.linkedin.com/in/romanbromidge",
                        "Co-founder & CTO leading automated geometric reconstruction algorithms"
                ],
                [
                        "Dylan Mingo",
                        "Head of Business Development",
                        "dylan@kaedim3d.com",
                        "https://www.linkedin.com/in/dylanmingo",
                        "Commercial partnerships lead for AAA game studio asset integration"
                ]
        ]
},
    {
        "company": "Kosen Labs (DeFi Reinforcement Learning Shuttered)",
        "domain": "kosen.ai",
        "category": "Data Brokering",
        "data_value": "Deep reinforcement learning automated market maker (AMM) liquidity provision simulations, high-frequency Uniswap v3 tick data, DeFi MEV traces.",
        "source": "https://www.crunchbase.com/organization/kosen-labs",
        "persons": [
                [
                        "Miljan Braticevic",
                        "Co-Founder & CEO",
                        "miljan@kosen.ai",
                        "https://www.linkedin.com/in/miljan-braticevic",
                        "Former DeepMind AI researcher who co-founded Kosen Labs"
                ],
                [
                        "Peter Toth",
                        "Co-Founder & CTO",
                        "peter@kosen.ai",
                        "https://www.linkedin.com/in/peter-toth-kosen",
                        "Former DeepMind research engineer directing reinforcement learning models"
                ],
                [
                        "Alex Popovich",
                        "Head of Quantitative Research",
                        "alex@kosen.ai",
                        "https://www.linkedin.com/in/alex-popovich",
                        "Quantitative finance lead analyzing decentralized liquidity distributions"
                ]
        ]
},
    {
        "company": "Mmhmm (Virtual Presentation Video Telemetry)",
        "domain": "mmhmm.app",
        "category": "Data Brokering",
        "data_value": "Over $100M invested; thousands of interactive virtual presentation video recordings, presenter segmentation alpha-matte masks, real-time stage telemetry.",
        "source": "https://techcrunch.com/2023/06/05/all-turtles-and-mmhmm-lay-off-staff-reorganize-as-one-company/",
        "persons": [
                [
                        "Phil Libin",
                        "Founder & CEO",
                        "phil@mmhmm.app",
                        "https://www.linkedin.com/in/plibin",
                        "Founder of Evernote and All Turtles; creator of mmhmm presentation app"
                ],
                [
                        "Alex Pachikov",
                        "Co-Founder & Chief Product Officer",
                        "alex@mmhmm.app",
                        "https://www.linkedin.com/in/pachikov",
                        "Co-founder; former Evernote VP directing visual software tools"
                ],
                [
                        "Charles Jolley",
                        "Executive Vice President",
                        "charles@mmhmm.app",
                        "https://www.linkedin.com/in/charlesjolley",
                        "Silicon Valley software veteran and former Strobe founder"
                ]
        ]
},
    {
        "company": "Clubhouse (Alpha Exploration - Audio Social Distress)",
        "domain": "clubhouse.com",
        "category": "Data Brokering",
        "data_value": "$4B peak valuation; billions of minutes of real-time conversational voice audio graphs, speaker turn-taking patterns, topic clustering metadata.",
        "source": "https://techcrunch.com/2023/04/27/clubhouse-is-laying-off-more-than-half-of-its-staff/",
        "persons": [
                [
                        "Paul Davison",
                        "Co-Founder & CEO",
                        "paul@clubhouse.com",
                        "https://www.linkedin.com/in/pauldavison",
                        "Co-founder & CEO; pioneer of drop-in social audio network"
                ],
                [
                        "Rohan Seth",
                        "Co-Founder & CTO",
                        "rohan@clubhouse.com",
                        "https://www.linkedin.com/in/rohanseth",
                        "Co-founder; former Google engineer who architected low-latency Agora audio streaming"
                ],
                [
                        "Luke Zapart",
                        "Head of Audio Infrastructure",
                        "luke@clubhouse.com",
                        "https://www.linkedin.com/in/lukezapart",
                        "Staff infrastructure engineer directing global audio mesh routing"
                ]
        ]
},
    {
        "company": "Zephyr Health (Life Sciences Commercial Clinical Data)",
        "domain": "zephyrhealth.com",
        "category": "Data Brokering",
        "data_value": "Curated life sciences global clinical trial investigator registries, KOL prescription referral graphs, hospital therapeutic adoption datasets.",
        "source": "https://www.crunchbase.com/organization/zephyr-health",
        "persons": [
                [
                        "William King",
                        "Founder & Former CEO",
                        "william@zephyrhealth.com",
                        "https://www.linkedin.com/in/williamkingzephyr",
                        "Founder & CEO; Johnson & Johnson commercial lead who built life sciences insights AI"
                ],
                [
                        "Mike Townsend",
                        "Chief Technology Officer",
                        "mike@zephyrhealth.com",
                        "https://www.linkedin.com/in/miketownsend",
                        "CTO overseeing pharmaceutical graph databases and clinical trial data integration"
                ],
                [
                        "Marc Miller",
                        "VP Commercial Strategy",
                        "marc@zephyrhealth.com",
                        "https://www.linkedin.com/in/marcmiller",
                        "Commercial VP directing global pharma intelligence licenses"
                ]
        ]
},
    {
        "company": "Palo Alto Software (LivePlan Small Business Financials)",
        "domain": "paloalto.com",
        "category": "Data Brokering",
        "data_value": "Over 1 million real small business financial forecast plans, cash flow modeling curves, industry operating margin benchmarks across 500+ NAICS codes.",
        "source": "https://www.paloalto.com/about/",
        "persons": [
                [
                        "Sabrina Parsons",
                        "Chief Executive Officer",
                        "sabrina@paloalto.com",
                        "https://www.linkedin.com/in/sabrinaparsons",
                        "CEO; small business financial management author and advocate"
                ],
                [
                        "Tim Berry",
                        "Founder & Chairman",
                        "tim@paloalto.com",
                        "https://www.linkedin.com/in/timberry",
                        "Founder; pioneer of computer-aided business planning and spreadsheet modeling"
                ],
                [
                        "Noah Parsons",
                        "Chief Operating Officer",
                        "noah@paloalto.com",
                        "https://www.linkedin.com/in/noahparsons",
                        "COO managing subscription cloud analytics and data partnerships"
                ]
        ]
},
    {
        "company": "Micromobility.com / Helbiz (E-Scooter Telemetry Liquidation)",
        "domain": "micromobility.com",
        "category": "Data Brokering",
        "data_value": "Urban micromobility fleet GPS routes, rider trip trajectories across Italian and US metropolitan centers, scooter battery discharge profiles.",
        "source": "https://techcrunch.com/2023/12/19/micromobility-com-delisted-from-nasdaq-faces-bankruptcy/",
        "persons": [
                [
                        "Salvatore Palella",
                        "Founder & Former CEO",
                        "salvatore@micromobility.com",
                        "https://www.linkedin.com/in/salvatorepalella",
                        "Founder & CEO; serial entrepreneur who listed Helbiz via SPAC"
                ],
                [
                        "Giulio Profumo",
                        "Chief Financial Officer",
                        "giulio@micromobility.com",
                        "https://www.linkedin.com/in/giulio-profumo-65551421",
                        "CFO managing debt restructuring and European asset transfers"
                ],
                [
                        "Jonathan New",
                        "Chief Financial Officer (Pre-Merger)",
                        "jonathan@micromobility.com",
                        "https://www.linkedin.com/in/jonathannew",
                        "Executive managing financial disclosures and creditor communications"
                ]
        ]
},
    {
        "company": "Alef Aeronautics (Flying Car Aerospace Engineering Data)",
        "domain": "alef.aero",
        "category": "Data Brokering",
        "data_value": "Ultra-lightweight mesh body aerodynamic simulations, distributed electric propulsion thrust vectoring telemetry, FAA special airworthiness cert test records.",
        "source": "https://www.reuters.com/business/aerospace-defense/alef-flying-car-preorders-reach-2850-2024-03-04/",
        "persons": [
                [
                        "Jim Dukhovny",
                        "Chief Executive Officer & Co-Founder",
                        "jim@alef.aero",
                        "https://www.linkedin.com/in/jim-dukhovny-488922",
                        "CEO & co-founder leading design of street-drivable vertical takeoff vehicle"
                ],
                [
                        "Constantine Kisly",
                        "Chief Technology Officer & Co-Founder",
                        "constantine@alef.aero",
                        "https://www.linkedin.com/in/constantine-kisly-5374b3",
                        "Co-founder & CTO; software and aerospace propulsion control designer"
                ],
                [
                        "Pavel Markin",
                        "Chief Mechanical Engineer & Co-Founder",
                        "pavel@alef.aero",
                        "https://www.linkedin.com/in/pavel-markin",
                        "Co-founder & chief engineer directing lightweight carbon-composite chassis"
                ]
        ]
},
    {
        "company": "WeaveGrid (EV Fleet Grid Load Telemetry)",
        "domain": "weavegrid.com",
        "category": "Data Brokering",
        "data_value": "Granular residential and fleet electric vehicle charging time-series, utility transformer load strain models, managed charging curtailment response curves.",
        "source": "https://techcrunch.com/2022/11/15/weavegrid-ev-charging-grid-software-raises-35m/",
        "persons": [
                [
                        "Apoorv Bhargava",
                        "Co-Founder & CEO",
                        "apoorv@weavegrid.com",
                        "https://www.linkedin.com/in/apoorvbhargava",
                        "Co-founder & CEO; former Opower and NRG energy software leader"
                ],
                [
                        "John Taggart",
                        "Co-Founder & CTO",
                        "john@weavegrid.com",
                        "https://www.linkedin.com/in/johntaggart",
                        "Co-founder & CTO; Stanford energy PhD specializing in EV battery grid integration"
                ],
                [
                        "Yael Lehnardt",
                        "Head of Utility Partnerships",
                        "yael@weavegrid.com",
                        "https://www.linkedin.com/in/yaellehnardt",
                        "Commercial leader negotiating telemetry sharing with major investor-owned utilities"
                ]
        ]
}
]

print(f"Total curated distressed companies: {len(DISTRESSED_COMPANIES)}")
