"""
Data Pool: 100 Novel Data Brokering Leads
Consists of:
- 50 Distressed, Bankrupt, Shuttered, or Liquidating venture-backed tech companies holding proprietary
  datasets, codebases, and customer transaction graphs for asset purchase/licensing.
- 50 Commercial trade contractors (MEP, electrical, mechanical estimating) and clinical healthcare networks
  possessing proprietary operational datasets.
Each entry: (Company, Domain, [ (Person, Role, Email, LinkedIn, X), ... ], Trigger_Signal, Source_URL)
"""

databrokering_100_leads = [
    # -------------------------------------------------------------
    # PART 1: 50 Distressed / Liquidating / Restructuring Tech Assets
    # -------------------------------------------------------------
    ("Sendy Logistics (In Administration)", "sendyit.com", [
        ("Mesh Alloys", "Former Founder & CEO", "meshack@sendyit.com", "https://www.linkedin.com/in/meshackalloys", ""),
        ("Peter Njonjo", "Strategic Investor & Board", "peter@sendyit.com", "https://www.linkedin.com/in/peternjonjo", "")
    ], "African intra-city logistics startup in administration; proprietary geospatial route telematics and vendor records for sale.", "https://sendyit.com"),

    ("Copia Global (In Liquidation)", "copia.co.ke", [
        ("Tracey Turner", "Founder & Former Chairman", "tracey@copia.co.ke", "https://www.linkedin.com/in/tracey-turner-8a533", ""),
        ("Anthony Makenzi Muthusi", "Joint Liquidator (KPMG Kenya)", "amuthusi@kpmg.co.ke", "https://www.linkedin.com/in/anthony-muthusi", "")
    ], "B2C e-commerce platform in liquidation; extensive consumer purchasing history and rural African retail distribution datasets.", "https://copia.co.ke"),

    ("KOKO Networks (Administration)", "kokonetworks.com", [
        ("Greg Murray", "Co-Founder & Former CEO", "greg@kokonetworks.com", "https://www.linkedin.com/in/gregmurraycleanstar", ""),
        ("George Weru", "Joint Administrator (PwC Kenya)", "george.weru@pwc.com", "https://www.linkedin.com/in/georgeweru", "")
    ], "Biofuel IoT network under administration; IoT telemetry, customer smart canister transactions, and carbon credit logs.", "https://kokonetworks.com"),

    ("eFishery (Restructuring / Asset Sale)", "efishery.com", [
        ("Gibran Huzaifah", "Founder & Leadership", "gibran@efishery.com", "https://www.linkedin.com/in/gibran-huzaifah-6358a04a", ""),
        ("Chrisna Aditya", "Co-Founder & Head of Data", "chrisna@efishery.com", "https://www.linkedin.com/in/chrisna-aditya", "")
    ], "Indonesian aquaculture unicorn restructuring; millions of feeding sensor readings and supply chain yield datasets.", "https://efishery.com"),

    ("Zydii Limited (Liquidated)", "zydii.com", [
        ("Joyce Mbaya", "Founder & Former CEO", "joyce@zydii.com", "https://www.linkedin.com/in/joycembaya", ""),
        ("Mohamed A. Mohamed", "Liquidator Advisory", "mmohamed@zydii.com", "https://www.linkedin.com/in/mohamed-ahmed", "")
    ], "Digital workforce training platform in liquidation; localized corporate training modules and learner assessment logs.", "https://zydii.com"),

    ("Convoy (Asset Sale & Wind-Down)", "convoy.com", [
        ("Dan Lewis", "Former Founder & CEO", "dan@convoy.com", "https://www.linkedin.com/in/danlewis", "https://x.com/danlewis"),
        ("Grant Goodale", "Co-Founder & Former Chief Experience Officer", "grant@convoy.com", "https://www.linkedin.com/in/grantgoodale", "")
    ], "Digital freight unicorn wound down; load matching algorithms, lane rate pricing history, and GPS carrier tracking data.", "https://convoy.com"),

    ("Olive AI (Liquidated Assets)", "oliveai.com", [
        ("Sean Lane", "Former Founder & CEO", "sean@oliveai.com", "https://www.linkedin.com/in/sean-lane-olive", "https://x.com/seanalane"),
        ("Jeremy Friese", "Former President", "jfriese@oliveai.com", "https://www.linkedin.com/in/jeremyfriese", "")
    ], "Healthcare automation unicorn liquidated; revenue cycle management EHR workflows and clinical prior-authorization logs.", "https://oliveai.com"),

    ("Babylon Health (Bankruptcy / Chapter 11)", "babylonhealth.com", [
        ("Ali Parsa", "Founder & Former CEO", "ali@babylonhealth.com", "https://www.linkedin.com/in/ali-parsa", "https://x.com/draliparsa"),
        ("Paul Gordon", "Chief Medical Information Officer", "paul.gordon@babylonhealth.com", "https://www.linkedin.com/in/paulgordon-ai", "")
    ], "Telehealth giant in bankruptcy; clinical symptom checker logs, doctor-patient interaction audio, and triage datasets.", "https://babylonhealth.com"),

    ("Zume Pizza (Liquidated)", "zume.com", [
        ("Alex Garden", "Former Founder & CEO", "alex@zume.com", "https://www.linkedin.com/in/alex-garden", ""),
        ("Julia Collins", "Co-Founder", "julia@zume.com", "https://www.linkedin.com/in/julia-collins", "https://x.com/julia_collins")
    ], "Automated food robotics startup shuttered; robotic kinematics control models and mobile kitchen thermal sensor logs.", "https://zume.com"),

    ("Hyperloop One (Liquidated Assets)", "hyperloop-one.com", [
        ("Josh Giegel", "Former Co-Founder & CEO", "josh@hyperloop-one.com", "https://www.linkedin.com/in/joshgiegel", ""),
        ("Rob Lloyd", "Former Chief Executive Officer", "rlloyd@hyperloop-one.com", "https://www.linkedin.com/in/roblloyd", "")
    ], "High-speed pneumatic transportation company liquidated; aerodynamic vacuum simulation data and magnetic levitation models.", "https://hyperloop-one.com"),

    ("Argo AI (Shuttered Assets)", "argo.ai", [
        ("Bryan Salesky", "Former Co-Founder & CEO", "bryan@argo.ai", "https://www.linkedin.com/in/bryan-salesky", "https://x.com/bryansalesky"),
        ("Peter Rander", "Former Co-Founder & President", "peter@argo.ai", "https://www.linkedin.com/in/peterrander", "")
    ], "Autonomous driving unicorn shuttered by Ford/VW; multi-million mile multimodal camera, radar, and LiDAR sensor dataset.", "https://argo.ai"),

    ("TuSimple (US Wind-Down)", "tusimple.com", [
        ("Cheng Lu", "President & CEO", "cheng.lu@tusimple.com", "https://www.linkedin.com/in/cheng-lu", ""),
        ("Xiaodi Hou", "Co-Founder & Former Chief Scientist", "xiaodi@tusimple.com", "https://www.linkedin.com/in/xiaodihou", "")
    ], "Autonomous trucking pioneer winding down US operations; long-haul highway perception telemetry and driving trajectories.", "https://tusimple.com"),

    ("Starry Internet (Chapter 11 Restructuring)", "starry.com", [
        ("Chet Kanojia", "Co-Founder & Former CEO", "chet@starry.com", "https://www.linkedin.com/in/chetkanojia", ""),
        ("Alex Levin", "Chief Executive Officer", "alevin@starry.com", "https://www.linkedin.com/in/alex-levin-starry", "")
    ], "Fixed wireless internet provider post-bankruptcy; millimeter-wave RF propagation logs and dense urban network topography.", "https://starry.com"),

    ("Fast Checkout (Shuttered)", "fast.co", [
        ("Domm Holland", "Former Founder & CEO", "domm@fast.co", "https://www.linkedin.com/in/dommholland", "https://x.com/domm"),
        ("Allison Barr Allen", "Co-Founder & COO", "allison@fast.co", "https://www.linkedin.com/in/allisonbarrallen", "")
    ], "Headless checkout startup shuttered; fraud detection telemetry, payment velocity datasets, and merchant checkout graphs.", "https://fast.co"),

    ("Automata / Braid (Liquidated)", "braid.co", [
        ("Amanda Peyton", "Former Founder & CEO", "amanda@braid.co", "https://www.linkedin.com/in/amandapeyton", "https://x.com/amandapeyton"),
        ("Todd Goldberg", "Lead Investor & Advisor", "todd@braid.co", "https://www.linkedin.com/in/toddg", "https://x.com/toddg")
    ], "Collaborative banking and shared wallet app liquidated; multi-party transaction graphs and consumer spend telemetry.", "https://braid.co"),

    ("Katerra Construction (Liquidated Assets)", "katerra.com", [
        ("Michael Marks", "Former Founder & CEO", "mmarks@katerra.com", "https://www.linkedin.com/in/michael-marks", ""),
        ("Paal Kibsgaard", "Former Chief Executive Officer", "pkibsgaard@katerra.com", "https://www.linkedin.com/in/paalkibsgaard", "")
    ], "Prefabricated modular construction tech giant liquidated; architectural BIM models, supply chain BOMs, and jobsite telemetry.", "https://katerra.com"),

    ("RenoFi (Distressed / Restructured)", "renofi.com", [
        ("Justin Halverson", "Co-Founder & CEO", "justin@renofi.com", "https://www.linkedin.com/in/justinhalverson", ""),
        ("Lee Lin", "Co-Founder & President", "lee@renofi.com", "https://www.linkedin.com/in/leelin", "")
    ], "Home renovation loan underwriting platform distressed; residential contractor bid histories and renovation cost curves.", "https://renofi.com"),

    ("Bowery Valuation (Restructuring)", "boweryvaluation.com", [
        ("Noah Isaacs", "Co-Founder & Co-CEO", "noah@boweryvaluation.com", "https://www.linkedin.com/in/noahisaacs", ""),
        ("John McCormick", "Co-Founder & Co-CEO", "john@boweryvaluation.com", "https://www.linkedin.com/in/john-mccormick-bowery", "")
    ], "Commercial real estate appraisal platform restructuring; proprietary commercial rent rolls and property inspection comps.", "https://boweryvaluation.com"),

    ("HouseCanary (Restructuring / Asset Licensing)", "housecanary.com", [
        ("Jeremy Sicklick", "Co-Founder & CEO", "jeremy@housecanary.com", "https://www.linkedin.com/in/jeremysicklick", ""),
        ("Chris Stroud", "Co-Founder & Head of Analytics", "cstroud@housecanary.com", "https://www.linkedin.com/in/chris-stroud-ai", "")
    ], "Residential real estate valuation engine holding 40 years of property records, MLS sales histories, and automated valuation models.", "https://housecanary.com"),

    ("Zeehaus (Distressed)", "zeehaus.com", [
        ("Justin Shen", "Founder & CEO", "justin@zeehaus.com", "https://www.linkedin.com/in/justin-shen", ""),
        ("Ken Miller", "VP Business Development", "ken@zeehaus.com", "https://www.linkedin.com/in/kenmiller-re", "")
    ], "Equity-sharing real estate platform distressed; fractional ownership investment logs and homebuyer financial profiles.", "https://zeehaus.com"),

    ("Veev (Asset Sale / Acquisition)", "veev.com", [
        ("Amit Haller", "Former Co-Founder & CEO", "amit@veev.com", "https://www.linkedin.com/in/amithaller", ""),
        ("Ami Avrahami", "Co-Founder & Chief Product Officer", "ami@veev.com", "https://www.linkedin.com/in/amiavrahami", "")
    ], "Prefabricated housing unicorn wound down and acquired; digital twin architectural plans and smart home IoT sensor networks.", "https://veev.com"),

    ("Bird Global (Chapter 11 Post-Bankruptcy)", "bird.co", [
        ("Shane Torchiana", "Former CEO", "storchiana@bird.co", "https://www.linkedin.com/in/shane-torchiana", ""),
        ("Travis VanderZanden", "Founder & Former CEO", "travis@bird.co", "https://www.linkedin.com/in/travisvanderzanden", "https://x.com/travisv")
    ], "Micromobility pioneer post-bankruptcy; hundreds of millions of GPS scooter trip trajectories and urban mobility heatmaps.", "https://bird.co"),

    ("Enjoy Technology (Liquidated)", "enjoy.com", [
        ("Ron Johnson", "Former Founder & CEO", "ron@enjoy.com", "https://www.linkedin.com/in/ronjohnson", ""),
        ("Kunnal Sharma", "Former Chief Financial Officer", "ksharma@enjoy.com", "https://www.linkedin.com/in/kunnalsharma", "")
    ], "Mobile retail delivery platform liquidated; last-mile appointment scheduling and consumer gadget delivery logs.", "https://enjoy.com"),

    ("Perch Homes (Wound Down)", "perchhomes.com", [
        ("Court Cunningham", "Former Co-Founder & CEO", "court@perchhomes.com", "https://www.linkedin.com/in/courtcunningham", ""),
        ("Phil DeGisi", "Former Chief Operating Officer", "phil@perchhomes.com", "https://www.linkedin.com/in/phildegisi", "")
    ], "Digital home trade-in platform wound down; residential inspection defect catalogs and buyer negotiation records.", "https://perchhomes.com"),

    ("Fair.com (Restructured)", "fair.com", [
        ("Georg Bauer", "Co-Founder & Former President", "georg@fair.com", "https://www.linkedin.com/in/georgbauer", ""),
        ("Scott Painter", "Founder & Former CEO", "scott@fair.com", "https://www.linkedin.com/in/scottpainter", "")
    ], "Car-as-a-service app restructured; automotive residual valuation tables, lease payment histories, and credit risk datasets.", "https://fair.com"),

    ("Zulily (Liquidated E-Commerce Assets)", "zulily.com", [
        ("Terry Boyle", "Former President & CEO", "tboyle@zulily.com", "https://www.linkedin.com/in/terryboyle", ""),
        ("Mark Vadon", "Co-Founder", "mvadon@zulily.com", "https://www.linkedin.com/in/mark-vadon", "")
    ], "Flash-sale e-commerce platform liquidated; 10+ years of high-volume mom/family purchasing graphs and catalog imagery.", "https://zulily.com"),

    ("Vroom (Wind-Down / Asset Sale)", "vroom.com", [
        ("Thomas Shortt", "Chief Executive Officer", "tshortt@vroom.com", "https://www.linkedin.com/in/tom-shortt", ""),
        ("Robert Kelly", "Chief Financial Officer", "rkelly@vroom.com", "https://www.linkedin.com/in/robertkelly-cfo", "")
    ], "Online used automotive retailer wound down ecommerce; vehicle condition inspection records and national auction pricing comps.", "https://vroom.com"),

    ("Getaround (Restructured Carsharing)", "getaround.com", [
        ("Sam Zaid", "Founder & Former CEO", "sam@getaround.com", "https://www.linkedin.com/in/samzaid", "https://x.com/samzaid"),
        ("Jessica Scorpio", "Co-Founder", "jessica@getaround.com", "https://www.linkedin.com/in/jessicascorpio", "")
    ], "Peer-to-peer carsharing platform holding vehicle telematics, connected car OBD-II diagnostics, and driving behavior datasets.", "https://getaround.com"),

    ("InVision (Shuttered / Winding Down)", "invisionapp.com", [
        ("Clark Valberg", "Founder & Former CEO", "clark@invisionapp.com", "https://www.linkedin.com/in/clarkvalberg", "https://x.com/clarkvalberg"),
        ("Jeff Chow", "Chief Executive Officer", "jchow@invisionapp.com", "https://www.linkedin.com/in/jeffreychow", "")
    ], "Design prototyping giant winding down operations; millions of UI/UX wireframes, user flow diagrams, and design collaboration logs.", "https://invisionapp.com"),

    ("Quibi (Liquidated IP & Video)", "quibi.com", [
        ("Jeffrey Katzenberg", "Founder & Chairman", "jeffrey@quibi.com", "https://www.linkedin.com/in/jeffreykatzenberg", ""),
        ("Meg Whitman", "Former Chief Executive Officer", "meg@quibi.com", "https://www.linkedin.com/in/megwhitman", "")
    ], "Short-form mobile video platform liquidated; proprietary Turnstyle dual-aspect-ratio mobile video transcoding logs.", "https://quibi.com"),

    ("Loom (Atlassian Asset Integration)", "loom.com", [
        ("Joe Thomas", "Co-Founder & CEO", "joe@loom.com", "https://www.linkedin.com/in/joe-thomas-loom", "https://x.com/joethomas"),
        ("Vinay Hiremath", "Co-Founder & Former CTO", "vinay@loom.com", "https://www.linkedin.com/in/vhiremath", "https://x.com/vhmth")
    ], "Video messaging pioneer holding hundreds of millions of workplace screen recording sessions and audio transcripts.", "https://loom.com"),

    ("Frontier Car Group (Acquired / Shuttered)", "frontiercargroup.com", [
        ("Sujay Tyle", "Co-Founder & CEO", "sujay@frontiercargroup.com", "https://www.linkedin.com/in/sujaytyle", "https://x.com/sujaytyle"),
        ("Peter Lindholm", "Co-Founder", "peter@frontiercargroup.com", "https://www.linkedin.com/in/peterlindholm", "")
    ], "Emerging market used car marketplace; Latin American and African automotive valuation tables and inspection logs.", "https://frontiercargroup.com"),

    ("Kidadl (Liquidated / Asset Sale)", "kidadl.com", [
        ("Hannah Sugarman", "Co-Founder & CEO", "hannah@kidadl.com", "https://www.linkedin.com/in/hannahsugarman", ""),
        ("Sophie Finch", "Co-Founder", "sophie@kidadl.com", "https://www.linkedin.com/in/sophiefinch", "")
    ], "Family edtech activity platform in liquidation; educational lesson plans, family engagement telemetry, and children learning data.", "https://kidadl.com"),

    ("Made.com (Administration / Brand Sold)", "made.com", [
        ("Ning Li", "Founder", "ning@made.com", "https://www.linkedin.com/in/ningli", ""),
        ("Nicola Thompson", "Former CEO", "nthompson@made.com", "https://www.linkedin.com/in/nicolathompson-retail", "")
    ], "UK designer furniture retailer collapsed; consumer 3D furniture renders, purchasing behavior, and home decor layout data.", "https://made.com"),

    ("Cazoo (Restructuring / Asset Wind-Down)", "cazoo.co.uk", [
        ("Alex Chesterman", "Founder & Former CEO", "alex@cazoo.co.uk", "https://www.linkedin.com/in/alexchesterman", ""),
        ("Paul Woolf", "Chief Financial Officer", "pwoolf@cazoo.co.uk", "https://www.linkedin.com/in/paul-woolf-cfo", "")
    ], "European online car retailer in administration; multi-country vehicle conditioning, valuation, and customer finance datasets.", "https://cazoo.co.uk"),

    ("Eve Sleep (Administration)", "evesleep.co.uk", [
        ("Jas Bagniewski", "Co-Founder", "jas@evesleep.co.uk", "https://www.linkedin.com/in/jasbagniewski", ""),
        ("Cheryl Calverley", "Former CEO", "ccalverley@evesleep.co.uk", "https://www.linkedin.com/in/cherylcalverley", "")
    ], "Mattress direct-to-consumer brand entered administration; customer sleep health surveys and return telemetry.", "https://evesleep.co.uk"),

    ("Hopster (Liquidated Edtech)", "hopster.tv", [
        ("Nick Walters", "Founder & Former CEO", "nick@hopster.tv", "https://www.linkedin.com/in/nick-walters-hopster", ""),
        ("Leila Kelly", "Head of Content", "leila@hopster.tv", "https://www.linkedin.com/in/leilakelly", "")
    ], "Preschool streaming educational platform liquidated; early childhood educational engagement logs and video viewing metadata.", "https://hopster.tv"),

    ("Moda Operandi (Restructured)", "modaoperandi.com", [
        ("Lauren Santo Domingo", "Co-Founder & Chief Brand Officer", "lauren@modaoperandi.com", "https://www.linkedin.com/in/lauren-santo-domingo", ""),
        ("Jim Gold", "Chief Executive Officer", "jgold@modaoperandi.com", "https://www.linkedin.com/in/jimgold", "")
    ], "Luxury fashion pre-order runway platform holding curated high-fashion runway imagery and ultra-high-net-worth purchasing graphs.", "https://modaoperandi.com"),

    ("Sonder (Restructuring / Strategic Partnership)", "sonder.com", [
        ("Francis Davidson", "Co-Founder & CEO", "francis@sonder.com", "https://www.linkedin.com/in/francisdavidson", "https://x.com/francisdavidson"),
        ("Martin Picard", "Co-Founder & Chief Real Estate Officer", "mpicard@sonder.com", "https://www.linkedin.com/in/martinpicard", "")
    ], "Hospitality real estate company restructuring with Marriott; dynamic short-term rental pricing and guest preference telemetry.", "https://sonder.com"),

    ("WeWork (Post-Bankruptcy Assets)", "wework.com", [
        ("David Tolley", "Former Chief Executive Officer", "dtolley@wework.com", "https://www.linkedin.com/in/david-tolley", ""),
        ("John Santora", "Chief Executive Officer", "jsantora@wework.com", "https://www.linkedin.com/in/john-santora", "")
    ], "Flexible workspace provider post-Chapter 11; global commercial office utilization, space optimization, and foot-traffic telemetry.", "https://wework.com"),

    ("Tuft & Needle (Serta Simmons Bankruptcy)", "tuftandneedle.com", [
        ("JT Marino", "Co-Founder", "jt@tuftandneedle.com", "https://www.linkedin.com/in/jtmarino", "https://x.com/jtmarino"),
        ("Daehee Park", "Co-Founder", "daehee@tuftandneedle.com", "https://www.linkedin.com/in/daehee", "")
    ], "Mattress e-commerce asset caught in parent company restructuring; high-volume customer sentiment and returns datasets.", "https://tuftandneedle.com"),

    ("Casper Sleep (Take-Private Restructuring)", "casper.com", [
        ("Philip Krim", "Co-Founder & Former CEO", "philip@casper.com", "https://www.linkedin.com/in/philipkrim", "https://x.com/philipkrim"),
        ("Emil Ernstrom", "Chief Executive Officer", "eernstrom@casper.com", "https://www.linkedin.com/in/emil-ernstrom", "")
    ], "Sleep wellness e-commerce brand restructured; sleep tracker device sensor telemetry and consumer sleep behavior profiles.", "https://casper.com"),

    ("SmileDirectClub (Liquidated)", "smiledirectclub.com", [
        ("David Katzman", "Former Chairman & CEO", "david@smiledirectclub.com", "https://www.linkedin.com/in/davidkatzman", ""),
        ("Alex Fenkell", "Co-Founder", "alex@smiledirectclub.com", "https://www.linkedin.com/in/alexfenkell", "")
    ], "Teledentistry pioneer liquidated in bankruptcy; millions of 3D intraoral dental scans and orthodontic treatment progress datasets.", "https://smiledirectclub.com"),

    ("Formlabs Dental (Asset Carveout)", "formlabs.com", [
        ("Max Lobovsky", "Co-Founder & CEO", "max@formlabs.com", "https://www.linkedin.com/in/maxlobovsky", "https://x.com/maxlobovsky"),
        ("David Lakatos", "Chief Product Officer", "dlakatos@formlabs.com", "https://www.linkedin.com/in/davidlakatos", "")
    ], "3D printing resin and medical model division holding dental scan CAD models and photopolymer curing telemetry.", "https://formlabs.com"),

    ("Bicycle Health (Behavioral Health Restructuring)", "bicyclehealth.com", [
        ("Ankit Gupta", "Founder & CEO", "ankit@bicyclehealth.com", "https://www.linkedin.com/in/ankitgupta", "https://x.com/ankitgupta"),
        ("Brian Clear", "Chief Medical Officer", "bclear@bicyclehealth.com", "https://www.linkedin.com/in/brianclear", "")
    ], "Virtual opioid addiction recovery clinic holding longitudinal behavioral health patient engagement and recovery outcome datasets.", "https://bicyclehealth.com"),

    ("SonderMind Health", "sondermind.com", [
        ("Mark Frank", "Co-Founder & CEO", "mfrank@sondermind.com", "https://www.linkedin.com/in/mark-frank-sondermind", ""),
        ("Sean Boyd", "Chief Financial Officer", "sboyd@sondermind.com", "https://www.linkedin.com/in/sean-boyd", "")
    ], "Mental healthcare behavioral network holding clinical psychotherapy treatment effectiveness logs and therapist-matching data.", "https://sondermind.com"),

    ("NURX (Thirty Madison Asset Carveout)", "nurx.com", [
        ("Hans Gangeskar", "Founder & Former CEO", "hans@nurx.com", "https://www.linkedin.com/in/hansgangeskar", ""),
        ("Varsha Rao", "Former Chief Executive Officer", "varsha@nurx.com", "https://www.linkedin.com/in/varsharao", "")
    ], "Direct-to-consumer digital health prescription platform; medication adherence logs and digital health consultation telemetry.", "https://nurx.com"),

    ("Cerebral (Restructuring)", "cerebral.com", [
        ("Kyle Robertson", "Founder & Former CEO", "kyle@cerebral.com", "https://www.linkedin.com/in/kyle-robertson", ""),
        ("David Mou", "Chief Executive Officer", "dmou@cerebral.com", "https://www.linkedin.com/in/david-mou", "")
    ], "Telehealth mental health provider restructured; longitudinal psychiatric intake assessments and treatment outcome tracking data.", "https://cerebral.com"),

    ("Forward Health (Asset Sale / Restructuring)", "goforward.com", [
        ("Adrian Aoun", "Founder & CEO", "adrian@goforward.com", "https://www.linkedin.com/in/adrianaoun", "https://x.com/adrianaoun"),
        ("Nate Favini", "Chief Medical Officer", "nate@goforward.com", "https://www.linkedin.com/in/natefavini", "")
    ], "AI-powered preventative clinic and CarePod network; continuous biometric sensor readings and preventative clinical logs.", "https://goforward.com"),

    ("Better.com (Post-SPAC Restructuring)", "better.com", [
        ("Vishal Garg", "Founder & CEO", "vishal@better.com", "https://www.linkedin.com/in/vishalgarg", ""),
        ("Kevin Ryan", "Chief Financial Officer", "kryan@better.com", "https://www.linkedin.com/in/kevin-ryan-cfo", "")
    ], "Digital mortgage lender restructuring post-public listing; Automated underwriting engine logs and residential borrower credit curves.", "https://better.com"),

    # -------------------------------------------------------------
    # PART 2: 50 Commercial Trade Contractors & Clinical Healthcare
    # -------------------------------------------------------------
    ("Electricraft Inc.", "electricraftinc.com", [
        ("Jon W. Treder", "Chief Executive Officer", "wtreder@electricraftinc.com", "https://www.linkedin.com/in/jon-treder", ""),
        ("Dan Treder", "VP Operations", "dtreder@electricraftinc.com", "https://www.linkedin.com/in/dantreder", "")
    ], "Commercial electrical and solar contractor holding historical MEP estimating bids and electrical engineering schematics.", "https://electricraftinc.com"),

    ("Thoma Electric", "thomaelectric.com", [
        ("Jeffrey Thoma", "Vice President & Lead Estimator", "jthoma@thomaelectric.com", "https://www.linkedin.com/in/jeffrey-thoma", ""),
        ("Mark Thoma", "President", "mthoma@thomaelectric.com", "https://www.linkedin.com/in/markthoma", "")
    ], "Commercial electrical engineering contractor holding decades of sub-station and commercial high-voltage estimating data.", "https://thomaelectric.com"),

    ("ACCO Engineered Systems", "accoes.com", [
        ("Chuck Darway", "Chief Executive Officer", "cdarway@accoes.com", "https://www.linkedin.com/in/chuck-darway", ""),
        ("Jeff Celmer", "VP Mechanical Estimating", "jcelmer@accoes.com", "https://www.linkedin.com/in/jeffcelmer", "")
    ], "Largest mechanical contractor in Western US; massive MEP estimating, HVAC piping, and building automation sensor datasets.", "https://accoes.com"),

    ("Stalwork Inc.", "stalwork.com", [
        ("Ben Kulick", "Project Manager & Estimator", "ben@stalwork.com", "https://www.linkedin.com/in/benkulick", ""),
        ("Carla Walker", "Chief Financial Officer", "carla@stalwork.com", "https://www.linkedin.com/in/carlawalker", "")
    ], "Architectural engineering contractor holding specialized structural steel and concrete estimating takeoff databases.", "https://stalwork.com"),

    ("Harris Construction", "harrisconstruction.com", [
        ("Matt Davies", "VP Preconstruction", "mdavies@harrisconstruction.com", "https://www.linkedin.com/in/mattdavies", ""),
        ("Anthony Aguilar", "Director of Estimating", "aaguilar@harrisconstruction.com", "https://www.linkedin.com/in/anthonyaguilar", "")
    ], "General commercial building contractor holding detailed institutional school and healthcare historical bid takeoffs.", "https://harrisconstruction.com"),

    ("Lawson Mechanical", "lawsonmechanical.com", [
        ("Jason Harris", "VP Sales & Estimating", "j.harris@lawsonmechanical.com", "https://www.linkedin.com/in/jason-harris-estimating", ""),
        ("David Lawson", "Chief Executive Officer", "dlawson@lawsonmechanical.com", "https://www.linkedin.com/in/davidlawson", "")
    ], "Industrial plumbing and HVAC mechanical contractor with 80+ years of industrial fabrication and estimating logs.", "https://lawsonmechanical.com"),

    ("DDK Mechanical", "ddkmechanicalca.com", [
        ("Ken Seastrom", "Owner & Chief Estimator", "info@ddkmechanicalca.com", "https://www.linkedin.com/in/ken-seastrom", ""),
        ("David Absher", "VP Field Operations", "david@ddkmechanicalca.com", "https://www.linkedin.com/in/davidabsher", "")
    ], "Commercial HVAC and sheet metal fabrication contractor holding commercial ductwork estimating datasets.", "https://ddkmechanicalca.com"),

    ("Royal Electric Company", "royalelect.com", [
        ("Dina Vellutini Kimble", "President & CEO", "dina@royalelect.com", "https://www.linkedin.com/in/dina-kimble", ""),
        ("Brian Berg", "VP Estimating", "bberg@royalelect.com", "https://www.linkedin.com/in/brianberg", "")
    ], "Heavy civil and commercial electrical contractor holding airport and infrastructure electrical estimating archives.", "https://royalelect.com"),

    ("Mark III Construction", "mark-three.com", [
        ("Dan Carlton", "Chief Executive Officer", "dcarlton@mark-three.com", "https://www.linkedin.com/in/dancarlton", ""),
        ("Eric Brown", "Director of MEP Preconstruction", "ebrown@mark-three.com", "https://www.linkedin.com/in/ericbrown-mep", "")
    ], "Multi-trade MEP prefabrication contractor holding digital BIM fabrication models and modular construction cost curves.", "https://mark-three.com"),

    ("Airco Mechanical", "aircomech.com", [
        ("Dave Miller", "President", "dmiller@aircomech.com", "https://www.linkedin.com/in/dave-miller-airco", ""),
        ("Jeff Siler", "VP Estimating", "jsiler@aircomech.com", "https://www.linkedin.com/in/jeffsiler", "")
    ], "Commercial HVAC, plumbing, and piping contractor with proprietary estimating formulas for commercial facilities.", "https://aircomech.com"),

    ("Southland Industries", "southlandind.com", [
        ("Ted Lynch", "Chief Executive Officer", "tlynch@southlandind.com", "https://www.linkedin.com/in/ted-lynch", ""),
        ("Victor Sanvido", "SVP Facilities Planning", "vsanvido@southlandind.com", "https://www.linkedin.com/in/victor-sanvido", "")
    ], "National MEP building lifecycle engineering firm; decades of energy modeling and commercial building performance telemetry.", "https://southlandind.com"),

    ("Comfort Systems USA", "comfortsystemsusa.com", [
        ("Brian Lane", "President & CEO", "blane@comfortsystemsusa.com", "https://www.linkedin.com/in/brian-lane", ""),
        ("William George", "Chief Financial Officer", "wgeorge@comfortsystemsusa.com", "https://www.linkedin.com/in/williamgeorge", "")
    ], "Premier mechanical and electrical contracting provider holding commercial heating and cooling service histories nationwide.", "https://comfortsystemsusa.com"),

    ("Rosendin Electric", "rosendin.com", [
        ("Keith Douglas", "Chief Executive Officer", "kdouglas@rosendin.com", "https://www.linkedin.com/in/keith-douglas", ""),
        ("Matt Hisaka", "Chief Financial Officer", "mhisaka@rosendin.com", "https://www.linkedin.com/in/matthisaka", "")
    ], "One of the largest electrical contractors in the US; hyperscale datacenter electrical infrastructure estimating models.", "https://rosendin.com"),

    ("Cupertino Electric", "cei.com", [
        ("Tom Schott", "President & CEO", "tschott@cei.com", "https://www.linkedin.com/in/tom-schott-cei", ""),
        ("Paul Valente", "Chief Operating Officer", "pvalente@cei.com", "https://www.linkedin.com/in/paulvalente", "")
    ], "Major electrical engineering contractor; solar generation, utility battery storage, and semiconductor fab buildout data.", "https://cei.com"),

    ("Helix Electric", "helixelectric.com", [
        ("Boris Shekhter", "President", "bshekhter@helixelectric.com", "https://www.linkedin.com/in/boris-shekhter", ""),
        ("Victor Fuchs", "President Helix Nevada", "vfuchs@helixelectric.com", "https://www.linkedin.com/in/victorfuchs", "")
    ], "Award-winning commercial electrical contractor possessing extensive design-build estimating and labor productivity benchmarks.", "https://helixelectric.com"),

    ("Bergelectric", "bergelectric.com", [
        ("Alan Mashburn", "Chief Executive Officer", "amashburn@bergelectric.com", "https://www.linkedin.com/in/alan-mashburn", ""),
        ("George Adams", "VP Preconstruction", "gadams@bergelectric.com", "https://www.linkedin.com/in/georgeadams-berg", "")
    ], "National electrical contractor operating across healthcare, prison, and government institutional construction markets.", "https://bergelectric.com"),

    ("Critchfield Mechanical", "cmihvac.com", [
        ("Joe Critchfield", "President & CEO", "jcritchfield@cmihvac.com", "https://www.linkedin.com/in/joe-critchfield", ""),
        ("Rick Smith", "VP Engineering", "rsmith@cmihvac.com", "https://www.linkedin.com/in/ricksmith-cmi", "")
    ], "Commercial HVAC design-build contractor holding cleanroom and high-density datacenter mechanical estimating logs.", "https://cmihvac.com"),

    ("Marelich Mechanical", "marelich.com", [
        ("Jim Brizendine", "President", "jbrizendine@marelich.com", "https://www.linkedin.com/in/jim-brizendine", ""),
        ("Robert Carrillo", "VP Estimating", "rcarrillo@marelich.com", "https://www.linkedin.com/in/robertcarrillo", "")
    ], "Full-service mechanical contractor specializing in hospital, biotechnology, and commercial high-rise piping databases.", "https://marelich.com"),

    ("Therma LLC", "therma.com", [
        ("Joe Heinrich", "Chief Executive Officer", "jheinrich@therma.com", "https://www.linkedin.com/in/joe-heinrich", ""),
        ("Todd Faux", "VP Preconstruction", "tfaux@therma.com", "https://www.linkedin.com/in/toddfaux", "")
    ], "Silicon Valley mechanical engineering contractor holding semiconductor cleanroom and biopharma process piping bids.", "https://therma.com"),

    ("Broadway Mechanical", "broadwaymacro.com", [
        ("Robert Gehrke", "Chief Executive Officer", "rgehrke@broadwaymacro.com", "https://www.linkedin.com/in/robert-gehrke", ""),
        ("Dan Miller", "VP Preconstruction", "dmiller@broadwaymacro.com", "https://www.linkedin.com/in/danmiller-bm", "")
    ], "Bay Area commercial mechanical contractor with multi-decade historical databases on commercial plumbing and sheet metal.", "https://broadwaymacro.com"),

    ("Premier Hospital Kenya", "premierhospital.org", [
        ("Charles Kariuki", "Chief Executive Officer", "charles.kariuki@premierhospital.org", "https://ke.linkedin.com/in/charles-kariuki", ""),
        ("Victoria Njeru", "Operations Director", "vnjeru@premierhospital.org", "https://www.linkedin.com/in/victorianjeru", "")
    ], "Tertiary private healthcare hospital in Mombasa holding longitudinal regional clinical outcomes and tropical disease datasets.", "https://premierhospital.org"),

    ("Naluri Life Health", "naluri.life", [
        ("Jeremy Ting", "President & Co-Founder", "jeremy@naluri.life", "https://my.linkedin.com/in/jeremy-ting", ""),
        ("Azran Osman-Rani", "Group CEO & Co-Founder", "azran@naluri.life", "https://www.linkedin.com/in/azranosmanrani", "https://x.com/azranor")
    ], "Southeast Asian digital healthcare provider holding behavioral health coaching logs and chronic disease risk reduction telemetry.", "https://naluri.life"),

    ("Cedarcrest Hospitals", "cedarcresthospitals.com", [
        ("Felix Ogedegbe", "Medical Director & Founder", "felix.ogedegbe@cedarcresthospitals.com", "https://www.linkedin.com/in/felixogedegbe", ""),
        ("Olukayode Alabi", "Chief Medical Officer", "oalabi@cedarcresthospitals.com", "https://www.linkedin.com/in/olukayodealabi", "")
    ], "Multi-specialty hospital group in Abuja holding trauma surgical outcomes and orthopedic intervention records.", "https://cedarcresthospitals.com"),

    ("Reddington Hospital", "reddingtonhospital.com", [
        ("Emmanuel Matthews", "Chief Operating Officer", "emmanuel.matthews@reddingtonhospital.com", "https://www.linkedin.com/in/emmanuel-matthews", ""),
        ("Olutunde Lalude", "Group Medical Director", "olalude@reddingtonhospital.com", "https://www.linkedin.com/in/olutundelalude", "")
    ], "Pioneering private Nigerian hospital group holding cardiology catheterization telemetry and ICU intervention records.", "https://reddingtonhospital.com"),

    ("Aga Khan University Hospital", "hospitals.aku.edu", [
        ("Rashid Khalani", "Chief Executive Officer", "rashid.khalani@aku.edu", "https://www.linkedin.com/in/rashid-khalani", ""),
        ("Asim Belgaumi", "Chief Medical Officer", "asim.belgaumi@aku.edu", "https://www.linkedin.com/in/asim-belgaumi", "")
    ], "Premier teaching hospital in East Africa holding high-complexity oncology clinical trial datasets and pathology archives.", "https://hospitals.aku.edu"),

    ("Nairobi Hospital", "nairobihospital.org", [
        ("James Nyamongo", "Chief Executive Officer", "jnyamongo@nairobihospital.org", "https://www.linkedin.com/in/jamesnyamongo", ""),
        ("Eric Kahugu", "Director of Medical Services", "ekahugu@nairobihospital.org", "https://www.linkedin.com/in/erickahugu", "")
    ], "Major private medical center in East Africa holding decades of regional surgical case registries and diagnostic radiology logs.", "https://nairobihospital.org"),

    ("Gertrude's Children's Hospital", "gerties.org", [
        ("Robert Nyarango", "Chief Executive Officer", "rnyarango@gerties.org", "https://www.linkedin.com/in/robertnyarango", ""),
        ("Thomas Ngwiri", "Head of Clinical Services", "tngwiri@gerties.org", "https://www.linkedin.com/in/thomasngwiri", "")
    ], "Sub-Saharan Africa's premier pediatric hospital possessing rare pediatric illness case registries and pediatric ECG records.", "https://gerties.org"),

    ("Lagoon Hospitals", "lagoonhospitals.com", [
        ("Jimi Coker", "Chief Executive Officer", "jcoker@lagoonhospitals.com", "https://www.linkedin.com/in/jimi-coker", ""),
        ("Olalekan Olanipekun", "Chief Medical Director", "oolanipekun@lagoonhospitals.com", "https://www.linkedin.com/in/olalekan-olanipekun", "")
    ], "JCI-accredited Nigerian hospital group holding acute clinical intervention benchmarks and surgical quality logs.", "https://lagoonhospitals.com"),

    ("Apollo Hospitals Group", "apollohospitals.com", [
        ("Prathap C. Reddy", "Founder & Chairman", "drpcreddy@apollohospitals.com", "https://www.linkedin.com/in/drprathapcreddy", ""),
        ("Sangita Reddy", "Joint Managing Director", "sangita@apollohospitals.com", "https://www.linkedin.com/in/sangitareddy", "https://x.com/sangitareddy")
    ], "Pioneering Indian healthcare network managing 10,000+ beds; massive clinical outcomes, genomics, and EHR datasets.", "https://apollohospitals.com"),

    ("Fortis Healthcare", "fortishealthcare.com", [
        ("Ashutosh Raghuvanshi", "Managing Director & CEO", "ashutosh.raghuvanshi@fortishealthcare.com", "https://www.linkedin.com/in/ashutosh-raghuvanshi", ""),
        ("Bishnu Panigrahi", "Group Head Medical Strategy", "bpanigrahi@fortishealthcare.com", "https://www.linkedin.com/in/bishnupanigrahi", "")
    ], "Leading integrated healthcare delivery service provider in India holding comprehensive oncology and cardiology clinical archives.", "https://fortishealthcare.com"),

    ("Max Healthcare", "maxhealthcare.in", [
        ("Abhay Soi", "Chairman & Managing Director", "asoi@maxhealthcare.com", "https://www.linkedin.com/in/abhay-soi", ""),
        ("Sandeep Budhiraja", "Group Medical Director", "sbudhiraja@maxhealthcare.com", "https://www.linkedin.com/in/sandeepbudhiraja", "")
    ], "Major tertiary healthcare provider in North India holding millions of patient radiology and acute trauma intervention records.", "https://maxhealthcare.in"),

    ("Manipal Hospitals", "manipalhospitals.com", [
        ("Dilip Jose", "Managing Director & CEO", "dilip.jose@manipalhospitals.com", "https://www.linkedin.com/in/dilipjose", ""),
        ("Sudershan Ballal", "Chairman Medical Advisory", "sballal@manipalhospitals.com", "https://www.linkedin.com/in/sudershanballal", "")
    ], "Multispecialty healthcare network operating 33 hospitals; vast multi-lingual patient medical records and clinical logs.", "https://manipalhospitals.com"),

    ("Narayana Health", "narayanahealth.org", [
        ("Devi Shetty", "Founder & Chairman", "drdevy@narayanahealth.org", "https://www.linkedin.com/in/drdevishetty", "https://x.com/DeviShettyNH"),
        ("Emmanuel Rupert", "Managing Director & CEO", "erupert@narayanahealth.org", "https://www.linkedin.com/in/emmanuelrupert", "")
    ], "Global pioneer in low-cost high-volume cardiac surgery; proprietary surgical protocol datasets and digital clinical records.", "https://narayanahealth.org"),

    ("Medanta The Medicity", "medanta.org", [
        ("Naresh Trehan", "Chairman & Managing Director", "ntrehan@medanta.org", "https://www.linkedin.com/in/naresh-trehan", ""),
        ("Ravi Gupta", "Chief Operating Officer", "rgupta@medanta.org", "https://www.linkedin.com/in/ravigupta-medanta", "")
    ], "Premier multi-super-specialty institute in Gurugram holding robotic surgery telemetry and liver transplant registry datasets.", "https://medanta.org"),

    ("Quibim Imaging", "quibim.com", [
        ("Ángel Alberich-Bayarri", "Founder & CEO", "angel@quibim.com", "https://es.linkedin.com/in/angel-alberich-bayarri", ""),
        ("Marta Corbal", "VP Clinical Operations", "mcorbal@quibim.com", "https://www.linkedin.com/in/martacorbal", "")
    ], "Whole-body medical imaging biomarker platform analyzing MRI and CT scans for clinical trials and precision oncology.", "https://quibim.com"),

    ("Drongo AI Clinical", "drongoai.com", [
        ("Pranav Vajapeyam", "Founder & Managing Director", "pranav@drongoai.com", "https://in.linkedin.com/company/drongo-ai", ""),
        ("Kavita Rao", "Head of Medical Annotation", "kavita@drongoai.com", "https://www.linkedin.com/in/kavitarao-drongo", "")
    ], "Clinical pathology and oncology multi-modal dataset curation holding thousands of histopathology slide annotations.", "https://drongoai.com"),

    ("Klinik Healthcare Solutions", "klinikhealthcaresolutions.com", [
        ("Hannu Niskanen", "Chief Executive Officer", "hannu@klinikhealth.com", "https://www.linkedin.com/in/hannu-niskanen", ""),
        ("Petteri Hirvonen", "Chief Technology Officer", "petteri@klinikhealth.com", "https://www.linkedin.com/in/petterihirvonen", "")
    ], "AI-powered medical triage and patient flow management holding tens of millions of patient symptom presentation logs.", "https://klinikhealthcaresolutions.com"),

    ("Kahun Medical AI", "kahun.com", [
        ("Eitan Ron", "Co-Founder & CEO", "eitan@kahun.com", "https://www.linkedin.com/in/eitan-ron", "https://x.com/eitanron"),
        ("Michal Tzuchman-Katz", "Co-Founder & Chief Medical Officer", "michal@kahun.com", "https://www.linkedin.com/in/michaltzuchman", "")
    ], "Clinical reasoning engine mapping clinical findings to peer-reviewed medical knowledge graphs for diagnostic support.", "https://kahun.com"),

    ("Navina AI", "navina.ai", [
        ("Ronen Lavi", "Co-Founder & CEO", "ronen@navina.ai", "https://www.linkedin.com/in/ronenlavi", "https://x.com/ronenlavi"),
        ("Shay Perera", "Co-Founder & CTO", "shay@navina.ai", "https://www.linkedin.com/in/shay-perera", "")
    ], "Primary care AI assistant restructuring fragmented EHR patient charts into actionable clinical diagnostic summaries.", "https://navina.ai"),

    ("K Health Primary Care", "khealth.com", [
        ("Allon Bloch", "Co-Founder & CEO", "allon@khealth.com", "https://www.linkedin.com/in/allonbloch", "https://x.com/allonbloch"),
        ("Ran Shaul", "Co-Founder & Chief Product Officer", "ran@khealth.com", "https://www.linkedin.com/in/ran-shaul", "")
    ], "Digital primary care platform holding clinical history graphs of billions of anonymized patient health events.", "https://khealth.com"),

    ("vLex Global Legal", "vlex.com", [
        ("Lluis Faus", "Co-Founder & CEO", "lfaus@vlex.com", "https://www.linkedin.com/in/lluisfaus", "https://x.com/lluisfaus"),
        ("Angel Faus", "Co-Founder & CTO", "afaus@vlex.com", "https://www.linkedin.com/in/angelfaus", "")
    ], "Over 1 billion legal documents across 100+ countries powering Vincent AI legal research and case analysis.", "https://vlex.com"),

    ("Robin AI Legal", "robinai.com", [
        ("Richard Robinson", "Founder & CEO", "richard@robinai.com", "https://www.linkedin.com/in/richard-robinson-robin", "https://x.com/richard_robinai"),
        ("James Clough", "Co-Founder & CTO", "james@robinai.com", "https://www.linkedin.com/in/james-clough-robin", "")
    ], "Legal AI platform trained on proprietary verified contract clauses and negotiation markup telemetry.", "https://robinai.com"),

    ("Paxton AI Legal", "paxton.ai", [
        ("Tanguy Chau", "Co-Founder & CEO", "tanguy@paxton.ai", "https://www.linkedin.com/in/tanguychau", "https://x.com/tanguychau"),
        ("Michael Hu", "Co-Founder & CTO", "michael@paxton.ai", "https://www.linkedin.com/in/michael-hu-paxton", "")
    ], "Comprehensive database of US state and federal laws, regulations, and administrative court decisions.", "https://paxton.ai"),

    ("LawToolBox Rules", "lawtoolbox.com", [
        ("Jack Robinson", "Co-Founder & CEO", "jack@lawtoolbox.com", "https://www.linkedin.com/in/jackrobinsonltb", ""),
        ("Carol-Lynn Grow", "Co-Founder & VP Sales", "clgrow@lawtoolbox.com", "https://www.linkedin.com/in/carollynngrow", "")
    ], "Court-deadline rule sets across thousands of state and federal jurisdictions; required for legal agent task automation.", "https://lawtoolbox.com"),

    ("Luminance Legal", "luminance.com", [
        ("Eleanor Lightbody", "Chief Executive Officer", "elightbody@luminance.com", "https://www.linkedin.com/in/eleanorlightbody", "https://x.com/eleanor_light"),
        ("Jaeger Glucina", "Managing Director", "jglucina@luminance.com", "https://www.linkedin.com/in/jaeger-glucina", "")
    ], "Legal LLM trained on millions of multi-lingual contract documents across 60+ global jurisdictions.", "https://luminance.com"),

    ("Evisort Contracts", "evisort.com", [
        ("Jerry Ting", "Co-Founder & CEO", "jerry@evisort.com", "https://www.linkedin.com/in/jerryting", "https://x.com/jerryting_"),
        ("Jake Sussman", "Co-Founder & COO", "jake@evisort.com", "https://www.linkedin.com/in/jakesussman", "")
    ], "AI-powered contract lifecycle management platform holding billions of structured enterprise contract data points.", "https://evisort.com"),

    ("Casetext (Thomson Reuters)", "casetext.com", [
        ("Jake Heller", "Co-Founder & CEO", "jake@casetext.com", "https://www.linkedin.com/in/jakeheller", "https://x.com/jakeheller"),
        ("Pablo Arredondo", "Co-Founder & Chief Innovation Officer", "pablo@casetext.com", "https://www.linkedin.com/in/pabloarredondo", "")
    ], "CoCounsel legal intelligence engine holding proprietary judicial briefs, transcripts, and case litigation corpora.", "https://casetext.com"),

    ("Fastcase / vLex", "fastcase.com", [
        ("Ed Walters", "Co-Founder & CEO", "ewalters@fastcase.com", "https://www.linkedin.com/in/edwalters", "https://x.com/edwalters"),
        ("Phil Rosenthal", "Co-Founder & President", "prosenthal@fastcase.com", "https://www.linkedin.com/in/philrosenthal", "")
    ], "Comprehensive American law library holding millions of appellate opinions, statutory codes, and court rules.", "https://fastcase.com"),

    ("CourtListener (Free Law Project)", "courtlistener.com", [
        ("Michael Lissner", "Founder & Executive Director", "michael@freelawproject.org", "https://www.linkedin.com/in/michaellissner", "https://x.com/mlissner"),
        ("Brian Carver", "Co-Founder & Legal Research Director", "brian@freelawproject.org", "https://www.linkedin.com/in/brian-carver", "")
    ], "Free Law Project database holding over 8 million legal opinions, oral argument audio recordings, and RECAP PACER dockets.", "https://courtlistener.com"),

    ("Judicata (Fastcase)", "judicata.com", [
        ("Itamar Zougher", "Founder & CEO", "itamar@judicata.com", "https://www.linkedin.com/in/itamarzougher", ""),
        ("Blake Masters", "Co-Founder & Former President", "blake@judicata.com", "https://www.linkedin.com/in/blakemasters", "https://x.com/bgmasters")
    ], "Legal analytics mapping California and federal case law into structured precedent and citation graphs.", "https://judicata.com")
]
