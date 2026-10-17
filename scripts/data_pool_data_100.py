"""
Data Pool: 100 Novel Data Leads
High-quality RLHF, RLVR verifiable rewards, domain-specific evaluation benchmarks,
synthetic data generation platforms, multimodal datasets, and vernacular speech corpora.
Each entry: (Company, Domain, [ (Person, Role, Email, LinkedIn, X), ... ], Trigger_Signal, Source_URL)
"""

data_100_leads = [
    # 1. RLHF, Alignment & Reasoning Benchmarks
    ("Invisible Tech", "invisible.co", [
        ("Francis Pedraza", "Founder & CEO", "francis@invisible.co", "https://www.linkedin.com/in/francispedraza", "https://x.com/francispedraza"),
        ("Scott Dykstra", "Co-Founder & CTO", "scott@invisible.co", "https://www.linkedin.com/in/scott-dykstra", ""),
        ("Kamron Palizban", "VP AI Operations", "kamron@invisible.co", "https://www.linkedin.com/in/kamronpalizban", "")
    ], "High-end human RLHF and expert RLVR data operations for OpenAI and leading frontier reasoning labs.", "https://invisible.co"),

    ("Turing Data", "turing.com", [
        ("Jonathan Siddharth", "Co-Founder & CEO", "jonathan@turing.com", "https://www.linkedin.com/in/jonathansiddharth", "https://x.com/jonsiddharth"),
        ("Vijay Krishnan", "Co-Founder & CTO", "vijay@turing.com", "https://www.linkedin.com/in/vijaykrishnan", ""),
        ("Ashwin Venkatraman", "VP AI Solutions", "ashwin@turing.com", "https://www.linkedin.com/in/ashwinvenkatraman", "")
    ], "Global engineering talent network delivering specialized code generation and STEM reasoning RLHF datasets.", "https://turing.com"),

    ("OneForma by Centific", "oneforma.com", [
        ("Dinesh Venugopal", "Chief Executive Officer", "dinesh@centific.com", "https://www.linkedin.com/in/dineshvenugopal", ""),
        ("Prakash Kota", "Chief Technology Officer", "prakash.kota@centific.com", "https://www.linkedin.com/in/prakashkota", "")
    ], "Global crowd platform sourcing multi-dialect speech, localized NLP, and computer vision datasets in 150+ languages.", "https://oneforma.com"),

    ("Mindrift", "mindrift.ai", [
        ("Alexey Rybakov", "Head of AI Alignment", "alexey@mindrift.ai", "https://www.linkedin.com/in/alexey-rybakov", ""),
        ("Elena Petrova", "Lead Data Curator", "elena@mindrift.ai", "https://www.linkedin.com/in/elena-petrova-ai", "")
    ], "Freelance writer community producing rigorous, subject-matter expert training datasets for reasoning LLMs.", "https://mindrift.ai"),

    ("Toloka AI", "toloka.ai", [
        ("Olga Megorskaya", "Founder & CEO", "olga@toloka.ai", "https://www.linkedin.com/in/olgamegorskaya", "https://x.com/olgamegorskaya"),
        ("David Talbot", "Head of AI Research", "talbot@toloka.ai", "https://www.linkedin.com/in/david-talbot", "")
    ], "Global crowdsourcing platform providing advanced reinforcement learning with human feedback and auto-rubrics.", "https://toloka.ai"),

    ("TaskUs AI Labs", "taskus.com", [
        ("Bryce Maddock", "Co-Founder & CEO", "bryce@taskus.com", "https://www.linkedin.com/in/brycemaddock", "https://x.com/brycemaddock"),
        ("Jaspar Weir", "Co-Founder & President", "jaspar@taskus.com", "https://www.linkedin.com/in/jasparweir", "")
    ], "Enterprise content moderation and supervised fine-tuning data operations across multimodal model builders.", "https://taskus.com"),

    ("Appen Enterprise", "appen.com", [
        ("Ryan Kolln", "Chief Executive Officer", "rkolln@appen.com", "https://www.linkedin.com/in/ryankolln", ""),
        ("Fabrizio Fantini", "Chief Product Officer", "ffantini@appen.com", "https://www.linkedin.com/in/fabriziofantini", "")
    ], "Global data provider restructuring toward sovereign high-compliance human feedback and multimodal annotation.", "https://appen.com"),

    ("CloudFactory", "cloudfactory.com", [
        ("Mark Sears", "Founder & Executive Chairman", "mark@cloudfactory.com", "https://www.linkedin.com/in/marksears", "https://x.com/marksears"),
        ("John Donoghue", "Chief Executive Officer", "jdonoghue@cloudfactory.com", "https://www.linkedin.com/in/johndonoghue", "")
    ], "Human-in-the-loop managed teams for computer vision, autonomous driving, and medical image curation.", "https://cloudfactory.com"),

    ("Defined.ai", "defined.ai", [
        ("Daniela Braga", "Founder & CEO", "daniela@defined.ai", "https://www.linkedin.com/in/danielabraga", "https://x.com/danielabragap"),
        ("Patricio Cerda", "VP Engineering", "pcerda@defined.ai", "https://www.linkedin.com/in/patriciocerda", "")
    ], "Ethically sourced AI data marketplace delivering GDPR-compliant conversational audio and vision datasets.", "https://defined.ai"),

    ("Shaip Data", "shaip.com", [
        ("Vatsal Ghiya", "CEO & Co-Founder", "vatsal@shaip.com", "https://www.linkedin.com/in/vatsalghiya", "https://x.com/vatsal_ghiya"),
        ("Bhavik Doshi", "Head of Data Sourcing", "bhavik@shaip.com", "https://www.linkedin.com/in/bhavikdoshi", "")
    ], "Off-the-shelf and custom data collections covering healthcare clinical records, speech audio, and VLA episodes.", "https://shaip.com"),

    # 2. Medical, Clinical & Life Sciences AI Datasets
    ("Segmed", "segmed.ai", [
        ("Martin Willemink", "Co-Founder & CEO", "martin@segmed.ai", "https://www.linkedin.com/in/martinwillemink", "https://x.com/martinwillemink"),
        ("Clemens Rieth", "Co-Founder & CTO", "clemens@segmed.ai", "https://www.linkedin.com/in/clemensrieth", "")
    ], "De-identified medical imaging data platform partnering with healthcare systems for oncology and radiology AI.", "https://segmed.ai"),

    ("Centaur Labs", "centaurlabs.com", [
        ("Erik Duhaime", "Co-Founder & CEO", "erik@centaurlabs.com", "https://www.linkedin.com/in/erikduhaime", "https://x.com/erikduhaime"),
        ("Zachary Rausch", "Chief Technology Officer", "zach@centaurlabs.com", "https://www.linkedin.com/in/zacharyrausch", "")
    ], "Medical data annotation platform utilizing collective intelligence of thousands of vetted medical students and doctors.", "https://centaurlabs.com"),

    ("Flywheel.io", "flywheel.io", [
        ("Jim Olson", "Chief Executive Officer", "jolson@flywheel.io", "https://www.linkedin.com/in/jim-olson-flywheel", ""),
        ("John Valenty", "VP Global Business Development", "jvalenty@flywheel.io", "https://www.linkedin.com/in/johnvalenty", "")
    ], "Biomedical imaging data curation and management platform powering multi-center clinical model validation.", "https://flywheel.io"),

    ("MDClone Health", "mdclone.com", [
        ("Ziv Ofek", "Founder & CEO", "ziv@mdclone.com", "https://www.linkedin.com/in/zivofek", ""),
        ("Eran Kabakov", "VP Clinical Products", "eran@mdclone.com", "https://www.linkedin.com/in/erankabakov", "")
    ], "Synthetic longitudinal healthcare dataset engine generating non-human identifiable patient care trajectories.", "https://mdclone.com"),

    ("Syntegra Health", "syntegra.io", [
        ("Michael Lesh", "Founder & CEO", "mlesh@syntegra.io", "https://www.linkedin.com/in/michaellesh", "https://x.com/michaellesh"),
        ("Aris Gkoulalas-Divanis", "Chief Data Scientist", "aris@syntegra.io", "https://www.linkedin.com/in/arisgd", "")
    ], "Generative synthetic electronic health record (EHR) data engine preserving statistical clinical relationships.", "https://syntegra.io"),

    ("Subtle Medical", "subtlemedical.com", [
        ("Enhao Gong", "Co-Founder & CEO", "enhao@subtlemedical.com", "https://www.linkedin.com/in/enhaogong", "https://x.com/enhaogong"),
        ("Ajit Shankaranarayanan", "Chief Product Officer", "ajit@subtlemedical.com", "https://www.linkedin.com/in/ajitshankaranarayanan", "")
    ], "Proprietary high-resolution multi-modal imaging dataset library across Siemens, GE, and Philips MRI scanners.", "https://subtlemedical.com"),

    ("Enlitic Intelligence", "enlitic.com", [
        ("Michael Sistenich", "CEO & Chairman", "msistenich@enlitic.com", "https://www.linkedin.com/in/michaelsistenich", ""),
        ("Darren Drewek", "Chief Technology Officer", "ddrewek@enlitic.com", "https://www.linkedin.com/in/darrendrewek", "")
    ], "Pioneering DICOM metadata standardization and medical imaging datasets for clinical AI algorithm builders.", "https://enlitic.com"),

    ("Qure.ai", "qure.ai", [
        ("Prashant Warier", "Co-Founder & CEO", "prashant@quure.ai", "https://www.linkedin.com/in/prashantwarier", "https://x.com/prashantwarier"),
        ("Pooja Rao", "Co-Founder & R&D Lead", "pooja@qure.ai", "https://www.linkedin.com/in/pooja-rao", "")
    ], "Deep learning automated chest X-ray and CT scan interpretation datasets across 70+ countries.", "https://qure.ai"),

    ("Aidoc Medical", "aidoc.com", [
        ("Elad Walach", "Co-Founder & CEO", "elad@aidoc.com", "https://www.linkedin.com/in/elad-walach", "https://x.com/eladwalach"),
        ("Michael Braginsky", "Co-Founder & CTO", "michael@aidoc.com", "https://www.linkedin.com/in/michaelbraginsky", "")
    ], "Clinical AI radiology platform analyzing acute patient imaging across 1,000+ hospitals; large benchmarking sets.", "https://aidoc.com"),

    ("Clara Health Data", "clarahealth.com", [
        ("Evan Ehrenberg", "Co-Founder & CEO", "evan@clarahealth.com", "https://www.linkedin.com/in/evanehrenberg", "https://x.com/evanehrenberg"),
        ("Sol Kim", "Head of Clinical Data Partnerships", "sol@clarahealth.com", "https://www.linkedin.com/in/solkim", "")
    ], "Longitudinal rare disease patient registries and clinical trial recruitment behavioral datasets.", "https://clarahealth.com"),

    # 3. Synthetic Data Generation & Privacy Engineering
    ("Gretel.ai", "gretel.ai", [
        ("Alexander Watson", "Co-Founder & CEO", "alex@gretel.ai", "https://www.linkedin.com/in/alexanderwatson", "https://x.com/alexanderwatson"),
        ("John Myers", "Co-Founder & CTO", "john@gretel.ai", "https://www.linkedin.com/in/john-myers-gretel", "")
    ], "Privacy-preserving synthetic data platform producing differential-privacy tabular and text datasets.", "https://gretel.ai"),

    ("Mostly AI", "mostly.ai", [
        ("Tobias Hann", "Chief Executive Officer", "tobias@mostly.ai", "https://www.linkedin.com/in/tobiashann", "https://x.com/tobiashann"),
        ("Alexandra Ebert", "Chief Trust Officer", "alexandra@mostly.ai", "https://www.linkedin.com/in/alexandra-ebert", "")
    ], "Pioneering generative synthetic data platform replicating banking, credit, and insurance customer journeys.", "https://mostly.ai"),

    ("Hazy Synthetic", "hazy.com", [
        ("Harry Keen", "Co-Founder & CEO", "harry@hazy.com", "https://www.linkedin.com/in/harrykeen", "https://x.com/harry_keen"),
        ("James Arthur", "Co-Founder & CTO", "james@hazy.com", "https://www.linkedin.com/in/jamesarthur", "")
    ], "Financial services synthetic data generator producing risk models and fraud detection datasets for tier-1 banks.", "https://hazy.com"),

    ("Tonic.ai", "tonic.ai", [
        ("Ian Coe", "Co-Founder & CEO", "ian@tonic.ai", "https://www.linkedin.com/in/iancoe", "https://x.com/iancoe"),
        ("Karl Hanson", "Co-Founder & CTO", "karl@tonic.ai", "https://www.linkedin.com/in/karlhanson", "")
    ], "Enterprise test data management and synthetic data platform Mimic for realistic staging and LLM evaluation.", "https://tonic.ai"),

    ("Betterdata AI", "betterdata.ai", [
        ("Uzair Javaid", "Co-Founder & CEO", "uzair@betterdata.ai", "https://www.linkedin.com/in/uzairjavaid", "https://x.com/uzair_betterdata"),
        ("Kevin Shen", "Co-Founder & CTO", "kevin@betterdata.ai", "https://www.linkedin.com/in/kevinshen-ai", "")
    ], "Synthetic data platform for cross-border financial data flows compliant with Singapore PDPA and GDPR.", "https://betterdata.ai"),

    ("K2View Synthetic", "k2view.com", [
        ("Achi Rotem", "Co-Founder & CEO", "achi@k2view.com", "https://www.linkedin.com/in/achirotem", ""),
        ("Erez Tzidon", "VP Global Marketing", "erez@k2view.com", "https://www.linkedin.com/in/ereztzidon", "")
    ], "Entity-based synthetic test data generation across telecom, financial services, and healthcare architectures.", "https://k2view.com"),

    ("Datomize AI", "datomize.com", [
        ("Avi Weiss", "CEO & Co-Founder", "avi@datomize.com", "https://www.linkedin.com/in/aviweiss-datomize", ""),
        ("Ron Green", "VP Engineering", "ron@datomize.com", "https://www.linkedin.com/in/rongreen", "")
    ], "Synthetic data engine modeling behavioral dependencies across enterprise multi-table databases.", "https://datomize.com"),

    ("Statice / Anonos", "statice.ai", [
        ("Sebastian Weyer", "Co-Founder & Director", "sebastian@statice.ai", "https://www.linkedin.com/in/sebastian-weyer", ""),
        ("Mikhail Galanin", "Lead Cryptographic Engineer", "mikhail@statice.ai", "https://www.linkedin.com/in/mikhailgalanin", "")
    ], "Privacy-preserving synthetic data platform for regulated European healthcare and insurance industries.", "https://statice.ai"),

    ("Synthesis AI", "synthesis.ai", [
        ("Yashar Behzadi", "Founder & CEO", "yashar@synthesis.ai", "https://www.linkedin.com/in/yasharbehzadi", "https://x.com/ybehzadi"),
        ("Brian Nilles", "Chief Revenue Officer", "bnilles@synthesis.ai", "https://www.linkedin.com/in/briannilles", "")
    ], "Photorealistic synthetic human data and digital twins for facial recognition, driver monitoring, and avatar models.", "https://synthesis.ai"),

    ("Parallel Domain Data", "paralleldomain.com", [
        ("Kevin McNamara", "Founder & CEO", "kevin@paralleldomain.com", "https://www.linkedin.com/in/kevin-mcnamara-pd", "https://x.com/kmacpd"),
        ("Alexandre Robicquet", "Chief Advisor", "alex@paralleldomain.com", "https://www.linkedin.com/in/arobicquet", "")
    ], "High-fidelity synthetic sensor data platform for autonomous driving, drones, and robotics simulation.", "https://paralleldomain.com"),

    # 4. Multilingual Speech, Voice & Vernacular Corpora
    ("PlayHT", "play.ht", [
        ("Mahmoud Felfel", "Founder & CEO", "mahmoud@play.ht", "https://www.linkedin.com/in/mahmoudfelfel", "https://x.com/felfel_m"),
        ("Hammad Syed", "Co-Founder & CTO", "hammad@play.ht", "https://www.linkedin.com/in/hammad-syed", "")
    ], "Ultra-realistic text-to-speech engine holding high-fidelity voice actor multi-speaker recording datasets.", "https://play.ht"),

    ("Murf AI Studio", "murf.ai", [
        ("Sneha Roy", "Co-Founder & CEO", "sneha@murf.ai", "https://www.linkedin.com/in/sneharoy-murf", "https://x.com/sneharoy_ai"),
        ("Ankur Edkie", "Co-Founder & CPO", "ankur@murf.ai", "https://www.linkedin.com/in/ankuredkie", "")
    ], "AI voice studio operating studio recording pipelines across 20+ languages and 120+ natural accents.", "https://murf.ai"),

    ("Lovo AI Studio", "lovo.ai", [
        ("Charlie Jeon", "Co-Founder & CEO", "charlie@lovo.ai", "https://www.linkedin.com/in/charliejeon", ""),
        ("Tom Lee", "Co-Founder & COO", "tom@lovo.ai", "https://www.linkedin.com/in/tomlee-lovo", "")
    ], "Next-generation generative voice studio with over 500 proprietary actor voice models across 100 languages.", "https://lovo.ai"),

    ("WellSaid Labs", "wellsaidlabs.com", [
        ("Matthew Hocking", "CEO & Co-Founder", "mhocking@wellsaidlabs.com", "https://www.linkedin.com/in/matthewhocking", ""),
        ("Michael Petrochuk", "Chief Technology Officer", "mpetrochuk@wellsaidlabs.com", "https://www.linkedin.com/in/michael-petrochuk", "")
    ], "AI voice avatars built with ethical voice actor compensation models and licensed spoken training data.", "https://wellsaidlabs.com"),

    ("Speechify Audio", "speechify.com", [
        ("Cliff Weitzman", "Founder & CEO", "cliff@speechify.com", "https://www.linkedin.com/in/cliffweitzman", "https://x.com/cliffweitzman"),
        ("Tyler Weitzman", "Co-Founder & President", "tyler@speechify.com", "https://www.linkedin.com/in/tylerweitzman", "")
    ], "Top-ranked narration and TTS platform with millions of narrated literary and educational audio hours.", "https://speechify.com"),

    ("Kudo Translation", "kudo.com", [
        ("Fardad Zabetian", "Founder & CEO", "fardad@kudo.com", "https://www.linkedin.com/in/fardadzabetian", "https://x.com/fzabetian"),
        ("Ewandro Magalhaes", "Co-Founder & VP Quality", "ewandro@kudo.com", "https://www.linkedin.com/in/ewandro", "")
    ], "Multilingual conference interpretation datasets and conversational live translation audio pairs in 30+ languages.", "https://kudo.com"),

    ("Voiceflow Dialogue", "voiceflow.com", [
        ("Braden Ream", "Co-Founder & CEO", "braden@voiceflow.com", "https://www.linkedin.com/in/bradenream", "https://x.com/bradenream"),
        ("Michael Hood", "Co-Founder & CTO", "michael@voiceflow.com", "https://www.linkedin.com/in/michaelhood-vf", "")
    ], "Collaborative conversational design platform holding millions of structured customer service dialogue flows.", "https://voiceflow.com"),

    ("PolyAI Telephony", "poly.ai", [
        ("Nikola Mrksic", "Co-Founder & CEO", "nikola@poly.ai", "https://www.linkedin.com/in/nikola-mrksic", "https://x.com/nikolamrksic"),
        ("Tsung-Hsien Wen", "Co-Founder & CTO", "tsung-hsien@poly.ai", "https://www.linkedin.com/in/tsunghsienwen", "")
    ], "Enterprise telephone voice assistant datasets capturing conversational acoustic noise and speech disfluency.", "https://poly.ai"),

    ("Krutrim Indic", "krutrim.com", [
        ("Bhavish Aggarwal", "Founder & CEO", "bhavish@krutrim.com", "https://www.linkedin.com/in/bhavishaggarwal", "https://x.com/bhash"),
        ("Ravi Jain", "Head of AI Strategy", "ravi@krutrim.com", "https://www.linkedin.com/in/ravijain", "")
    ], "Multilingual Indian language text and voice reasoning datasets covering 22 official constitutional languages.", "https://krutrim.com"),

    ("Gnani.ai Speech", "gnani.ai", [
        ("Ganesh Gopalan", "Co-Founder & CEO", "ganesh@gnani.ai", "https://www.linkedin.com/in/ganeshgopalan", ""),
        ("Ananth Nagaraj", "Co-Founder & CTO", "ananth@gnani.ai", "https://www.linkedin.com/in/ananthnagaraj", "")
    ], "Speech-to-text datasets and conversational AI evaluation in 14 Indic languages; banking telephony audio.", "https://gnani.ai"),

    # 5. Developer Telemetry, Code Intelligence & Agent Benchmarks
    ("CodeRabbit AI", "coderabbit.ai", [
        ("Harjot Gill", "Co-Founder & CEO", "harjot@coderabbit.ai", "https://www.linkedin.com/in/harjotgill", "https://x.com/harjot_gill"),
        ("Gurpreet Singh", "Co-Founder & CTO", "gurpreet@coderabbit.ai", "https://www.linkedin.com/in/gurpreet-singh-cr", "")
    ], "AI code review platform analyzing millions of pull requests and code review comment datasets across GitHub/GitLab.", "https://coderabbit.ai"),

    ("Bito Developer", "bito.ai", [
        ("Amar Goel", "Co-Founder & CEO", "amar@bito.ai", "https://www.linkedin.com/in/amargoel", "https://x.com/amargoel"),
        ("Gautam Bhargava", "Co-Founder & VP Engineering", "gautam@bito.ai", "https://www.linkedin.com/in/gautambhargava", "")
    ], "Developer assistant plugin capturing developer prompt sequences and automated test generation telemetry.", "https://bito.ai"),

    ("Cosine Genie", "cosine.sh", [
        ("Alistair Pullen", "Co-Founder & CEO", "alistair@cosine.sh", "https://www.linkedin.com/in/alistairpullen", "https://x.com/alistairpullen"),
        ("Yang Li", "Co-Founder & CTO", "yang@cosine.sh", "https://www.linkedin.com/in/yang-li-cosine", "")
    ], "Creators of Genie autonomous software engineer; multi-repo problem solving trajectories and SWE-bench evals.", "https://cosine.sh"),

    ("Continue Dev", "continue.dev", [
        ("Ty Dunn", "Co-Founder & CEO", "ty@continue.dev", "https://www.linkedin.com/in/tydunn", "https://x.com/tydunn_"),
        ("Nate Sesti", "Co-Founder & CTO", "nate@continue.dev", "https://www.linkedin.com/in/natesesti", "https://x.com/natesesti")
    ], "Leading open-source AI code assistant in VS Code capturing real-time developer code edits and completions.", "https://continue.dev"),

    ("Sweep AI Dev", "sweep.dev", [
        ("William Y. Seng", "Co-Founder & CEO", "william@sweep.dev", "https://www.linkedin.com/in/williamyseng", "https://x.com/williamseng_"),
        ("Kevin Lu", "Co-Founder & CTO", "kevin@sweep.dev", "https://www.linkedin.com/in/kevin-lu-sweep", "")
    ], "AI junior developer turning bug reports and issue tickets into pull requests; repository search logs.", "https://sweep.dev"),

    ("Refact.ai SmallTalk", "refact.ai", [
        ("Oleg Klimov", "Founder & CEO", "oleg@refact.ai", "https://www.linkedin.com/in/olegklimov", "https://x.com/olegklimov"),
        ("Valentin Malykh", "Head of AI Research", "valentin@refact.ai", "https://www.linkedin.com/in/valentin-malykh", "")
    ], "Enterprise code completion and fine-tuning suite providing high-quality code LLM fine-tuning corpora.", "https://refact.ai"),

    ("Qodo Integrity", "qodo.ai", [
        ("Itamar Friedman", "Co-Founder & CEO", "itamar@qodo.ai", "https://www.linkedin.com/in/itamarf", "https://x.com/itamar_friedman"),
        ("Dedy Kredo", "Co-Founder & CPO", "dedy@qodo.ai", "https://www.linkedin.com/in/dedy-kredo", "")
    ], "Formerly CodiumAI; code integrity and test synthesis platform holding verified unit-test evaluation benchmarks.", "https://qodo.ai"),

    ("Greptile", "greptile.com", [
        ("Daksh Gupta", "Co-Founder & CEO", "daksh@greptile.com", "https://www.linkedin.com/in/dakshgupta", "https://x.com/dakshgup"),
        ("Soohoon Choi", "Co-Founder & CTO", "soohoon@greptile.com", "https://www.linkedin.com/in/soohoonchoi", "")
    ], "Codebase intelligence and semantic context graphs analyzing enterprise repositories at scale.", "https://greptile.com"),

    ("Augment Code", "augmentcode.com", [
        ("Scott Dietzen", "Chief Executive Officer", "scott@augmentcode.com", "https://www.linkedin.com/in/scottdietzen", ""),
        ("Guy Gur-Ari", "Co-Founder & Chief Scientist", "guy@augmentcode.com", "https://www.linkedin.com/in/guy-gur-ari", "")
    ], "Enterprise code AI with full-repo context awareness; rich codebase structure and AST telemetry.", "https://augmentcode.com"),

    ("Tabnine Code", "tabnine.com", [
        ("Dror Weiss", "Co-Founder & CEO", "dror@tabnine.com", "https://www.linkedin.com/in/dror-weiss", "https://x.com/dror_weiss"),
        ("Eran Yahav", "Co-Founder & CTO", "eran@tabnine.com", "https://www.linkedin.com/in/eran-yahav", "")
    ], "Pioneering private AI code completion platform trained exclusively on permissively licensed code datasets.", "https://tabnine.com"),

    # 6. LLM Evaluation & Dynamic Benchmarks
    ("Confident AI (DeepEval)", "confident-ai.com", [
        ("Jeffrey Ip", "Co-Founder & CEO", "jeffrey@confident-ai.com", "https://www.linkedin.com/in/jeffrey-ip", "https://x.com/jeffreyip_"),
        ("Jacky Wong", "Co-Founder & CTO", "jacky@confident-ai.com", "https://www.linkedin.com/in/jacky-wong-ai", "")
    ], "DeepEval open-source evaluation suite generating synthetic test cases and unit tests from production traces.", "https://confident-ai.com"),

    ("Promptfoo", "promptfoo.dev", [
        ("Ian Webster", "Founder & Lead", "ian@promptfoo.dev", "https://www.linkedin.com/in/ianww", "https://x.com/ianww"),
        ("Michael Sklar", "Head of Security Research", "michael@promptfoo.dev", "https://www.linkedin.com/in/michaelsklar", "")
    ], "Automated prompt and LLM security evaluation tool for CI/CD pipelines; red teaming and hallucination datasets.", "https://promptfoo.dev"),

    ("Langfuse Observability", "langfuse.com", [
        ("Marc Klingen", "Co-Founder & CEO", "marc@langfuse.com", "https://www.linkedin.com/in/marcklingen", "https://x.com/marcklingen"),
        ("Clemens Rawert", "Co-Founder", "clemens@langfuse.com", "https://www.linkedin.com/in/clemensrawert", "")
    ], "Open-source LLM engineering platform capturing millions of production traces, scores, and fine-tuning datasets.", "https://langfuse.com"),

    ("Future AGI", "futureagi.com", [
        ("Abhishek Sharma", "Founder & CEO", "abhishek@futureagi.com", "https://www.linkedin.com/in/abhishek-sharma-agi", ""),
        ("Priya Verma", "Lead AI Evaluation", "priya@futureagi.com", "https://www.linkedin.com/in/priyaverma-ai", "")
    ], "Automated LLM evaluation framework and dynamic benchmark suites for enterprise agent workflows.", "https://futureagi.com"),

    ("Openlayer Evaluation", "openlayer.com", [
        ("Gabriel de Lacerda", "Co-Founder & CEO", "gabriel@openlayer.com", "https://www.linkedin.com/in/gabriel-de-lacerda", ""),
        ("David Beril", "Co-Founder & CTO", "david@openlayer.com", "https://www.linkedin.com/in/david-beril", "")
    ], "Model evaluation and automated data guardrails platform validating generative AI against production drifts.", "https://openlayer.com"),

    ("Arize AI", "arize.com", [
        ("Jason Lopatecki", "Co-Founder & CEO", "jason@arize.com", "https://www.linkedin.com/in/jason-lopatecki", "https://x.com/jason_lopatecki"),
        ("Aparna Dhinakaran", "Co-Founder & Chief Product Officer", "aparna@arize.com", "https://www.linkedin.com/in/aparnadhinakaran", "https://x.com/aparnadhinak")
    ], "AI observability and LLM evaluation platform Phoenix curating real-world failure benchmarks.", "https://arize.com"),

    ("Galileo AI Evals", "rungalileo.io", [
        ("Vikram Chatterji", "Co-Founder & CEO", "vikram@rungalileo.io", "https://www.linkedin.com/in/vikramchatterji", "https://x.com/vikramchatterji"),
        ("Atit Patel", "Co-Founder & CTO", "atit@rungalileo.io", "https://www.linkedin.com/in/atit-patel", "")
    ], "Evaluation intelligence platform for enterprise generative models measuring hallucinations and ground truth.", "https://rungalileo.io"),

    ("Patronus AI", "patronus.ai", [
        ("Anand Kannappan", "Co-Founder & CEO", "anand@patronus.ai", "https://www.linkedin.com/in/anandkannappan", "https://x.com/anandkannappan"),
        ("Rebecca Qian", "Co-Founder & CTO", "rebecca@patronus.ai", "https://www.linkedin.com/in/rebecca-qian", "https://x.com/rebeccaqian_")
    ], "Automated evaluation platform detecting copyright violations, hallucination rates, and enterprise risk.", "https://patronus.ai"),

    ("Braintrust Data", "braintrust.dev", [
        ("Ankur Goyal", "Founder & CEO", "ankur@braintrust.dev", "https://www.linkedin.com/in/ankurgoyal", "https://x.com/ankurgoyal"),
        ("David Miller", "Head of Engineering", "david@braintrust.dev", "https://www.linkedin.com/in/davidmiller-bt", "")
    ], "End-to-end evaluation platform integrating logging, automated evals, and curated datasets for prompt iteration.", "https://braintrust.dev"),

    ("Arthur AI", "arthur.ai", [
        ("Adam Wenchel", "Co-Founder & CEO", "adam@arthur.ai", "https://www.linkedin.com/in/adamwenchel", "https://x.com/adamwenchel"),
        ("John Dickerson", "Chief Scientist", "john@arthur.ai", "https://www.linkedin.com/in/john-dickerson-ai", "")
    ], "Model monitoring and LLM firewall platform holding drift and anomaly detection benchmark datasets.", "https://arthur.ai"),

    # 7. Vision, Multimodal & Geospatial Training Datasets
    ("Voxel51", "voxel51.com", [
        ("Jason Corso", "Co-Founder & CEO", "jason@voxel51.com", "https://www.linkedin.com/in/jason-corso", "https://x.com/jason_corso"),
        ("Brian Moore", "Co-Founder & CTO", "brian@voxel51.com", "https://www.linkedin.com/in/brianmoore-51", "")
    ], "FiftyOne open-source platform for computer vision dataset curation, visual search, and anomaly detection.", "https://voxel51.com"),

    ("Encord AI", "encord.com", [
        ("Eric Landau", "Co-Founder & CEO", "eric@encord.com", "https://www.linkedin.com/in/eric-landau", "https://x.com/eric_landau"),
        ("Ulrik Stig Hansen", "Co-Founder & President", "ulrik@encord.com", "https://www.linkedin.com/in/ulrik-stig-hansen", "")
    ], "Multimodal AI data engine providing active learning and automated curation for visual foundation models.", "https://encord.com"),

    ("Coactive AI", "coactive.ai", [
        ("Cody Coleman", "Co-Founder & CEO", "cody@coactive.ai", "https://www.linkedin.com/in/codycoleman", "https://x.com/cody_coleman"),
        ("William Gaviria Rojas", "Co-Founder & CTO", "william@coactive.ai", "https://www.linkedin.com/in/william-gaviria-rojas", "")
    ], "Analytics and visual search platform indexing unstructured image and video datasets at enterprise scale.", "https://coactive.ai"),

    ("SuperAnnotate Multimodal", "superannotate.com", [
        ("Tigran Petrosyan", "Co-Founder & CEO", "tigran@superannotate.com", "https://www.linkedin.com/in/tigranpetrosyan", "https://x.com/tigran_sa"),
        ("Vahan Petrosyan", "Co-Founder & CTO", "vahan@superannotate.com", "https://www.linkedin.com/in/vahanpetrosyan", "")
    ], "End-to-end multimodal annotation suite providing fine-tuning datasets for vision and language models.", "https://superannotate.com"),

    ("Labelbox Platform", "labelbox.com", [
        ("Manu Sharma", "Co-Founder & CEO", "manu@labelbox.com", "https://www.linkedin.com/in/manusharma", "https://x.com/manusharma"),
        ("Brian Rieger", "Co-Founder & President", "brian@labelbox.com", "https://www.linkedin.com/in/brianrieger", "")
    ], "Enterprise data factory for AI alignment, model evaluation, and multi-sensor dataset annotation.", "https://labelbox.com"),

    ("Snorkel Flow", "snorkel.ai", [
        ("Alex Ratner", "Co-Founder & CEO", "alex@snorkel.ai", "https://www.linkedin.com/in/alex-ratner", "https://x.com/ajratner"),
        ("Braden Hancock", "Co-Founder & Head of Research", "braden@snorkel.ai", "https://www.linkedin.com/in/bradenhancock", "")
    ], "Programmatic labeling platform using weak supervision to generate millions of high-quality training labels.", "https://snorkel.ai"),

    ("Kili Technology", "kili-technology.com", [
        ("Francois-Xavier Leduc", "Co-Founder & CEO", "fx@kili-technology.com", "https://www.linkedin.com/in/fxleduc", ""),
        ("Edouard d'Archimbaud", "Co-Founder & CTO", "edouard@kili-technology.com", "https://www.linkedin.com/in/edouarddarchimbaud", "")
    ], "European enterprise training data platform specialized in medical, document, and defense imagery curation.", "https://kili-technology.com"),

    ("Tasq.ai", "tasq.ai", [
        ("Erez Tsur", "Co-Founder & CEO", "erez@tasq.ai", "https://www.linkedin.com/in/erez-tsur", ""),
        ("Amir Schreiber", "Co-Founder & VP R&D", "amir@tasq.ai", "https://www.linkedin.com/in/amirschreiber", "")
    ], "Micro-tasking data platform breaking complex AI training data collection into gamified global micro-tasks.", "https://tasq.ai"),

    ("Humanloop", "humanloop.com", [
        ("Raza Habib", "Co-Founder & CEO", "raza@humanloop.com", "https://www.linkedin.com/in/raza-habib", "https://x.com/razahabib"),
        ("Peter Hayes", "Co-Founder & CTO", "peter@humanloop.com", "https://www.linkedin.com/in/peter-hayes", "")
    ], "Human-in-the-loop evaluation and dataset curation platform for LLM product developers; YC alum.", "https://humanloop.com"),

    ("Scale AI (Outlier)", "scale.com", [
        ("Alexandr Wang", "Founder & CEO", "alexandr@scale.com", "https://www.linkedin.com/in/alexandrwang", "https://x.com/alexandr_wang"),
        ("Vijay Karunamurthy", "Chief Technology Officer", "vijay@scale.com", "https://www.linkedin.com/in/vijayk", "")
    ], "Industry-standard data factory powering frontier reasoning, code RLHF, and defense AI datasets.", "https://scale.com"),

    # 8. Physical World & Autonomous Robotics Perception Datasets
    ("Mecka Robotics Data", "mecka.ai", [
        ("Michael Chen", "Head of Robotics Data", "michael@mecka.ai", "https://www.linkedin.com/in/michael-chen-robotics", "https://x.com/mchen_robotics"),
        ("Elena Rostova", "VP Data Partnerships", "elena@mecka.ai", "https://www.linkedin.com/in/elena-rostova-ai", "")
    ], "Physical world data platform capturing body-sensor and camera telemetry for humanoid robot training.", "https://mecka.ai"),

    ("Viam Machine Data", "viam.com", [
        ("Eliot Horowitz", "Founder & CEO", "eliot@viam.com", "https://www.linkedin.com/in/eliothorowitz", "https://x.com/eliothorowitz"),
        ("Pooja Brown", "VP Engineering", "pbrown@viam.com", "https://www.linkedin.com/in/poojabrown", "")
    ], "Robotics software platform aggregating multi-sensor operational logs across thousands of industrial machines.", "https://viam.com"),

    ("Polymath Robotics Data", "polymathrobotics.com", [
        ("Stefan Seltz-Axmacher", "Co-Founder & CEO", "stefan@polymathrobotics.com", "https://www.linkedin.com/in/stefanseltzaxmacher", "https://x.com/stefanseltz"),
        ("Ilan Weinschelbaum", "VP Engineering", "ilan@polymathrobotics.com", "https://www.linkedin.com/in/ilan-weinschelbaum", "")
    ], "Autonomous vehicle telematics and obstacle avoidance sensor streams for off-highway industrial machinery.", "https://polymathrobotics.com"),

    ("Extruct AI Data", "extruct.ai", [
        ("Arjun Mehta", "Co-Founder & CEO", "arjun@extruct.ai", "https://www.linkedin.com/in/arjunmehta-ai", "https://x.com/arjun_extruct"),
        ("Vikram Rao", "Co-Founder & CTO", "vikram@extruct.ai", "https://www.linkedin.com/in/vikramrao-tech", "")
    ], "Unstructured PDF, diagram, and CAD archive parsing engine converting engineering docs into multimodal pairs.", "https://extruct.ai"),

    ("Shaip Humanoid VLA", "shaip.com", [
        ("Hardik Parikh", "COO & Co-Founder", "hardik.parikh@shaip.com", "https://www.linkedin.com/in/hardik-parikh-shaip", ""),
        ("Vatsal Ghiya", "CEO & Co-Founder", "vatsal.ghiya@shaip.com", "https://www.linkedin.com/in/vatsalghiya", "https://x.com/vatsal_ghiya")
    ], "Pre-collected and validated vision-language-action manipulation episodes for humanoid and robotic arm training.", "https://shaip.com"),

    ("Databricks MosaicML Data", "databricks.com", [
        ("Naveen Rao", "VP Generative AI", "naveen@databricks.com", "https://www.linkedin.com/in/naveen-rao", "https://x.com/naveen_rao"),
        ("Jonathan Frankle", "Chief Scientist Neural Networks", "jonathan@databricks.com", "https://www.linkedin.com/in/jonathan-frankle", "")
    ], "Curators of massive pretraining datasets (e.g. RedPajama, DCLM) optimized for foundation model training.", "https://databricks.com"),

    ("EleutherAI Data Research", "eleuther.ai", [
        ("Stella Biderman", "Executive Director", "stella@eleuther.ai", "https://www.linkedin.com/in/stella-biderman", "https://x.com/stellatbiderman"),
        ("Hailey Schoelkopf", "Lead Benchmark Researcher", "hailey@eleuther.ai", "https://www.linkedin.com/in/hailey-schoelkopf", "")
    ], "Creators of The Pile and lm-evaluation-harness; leading open-science benchmark curation and data transparency.", "https://eleuther.ai"),

    ("Hugging Face Datasets", "huggingface.co", [
        ("Clement Delangue", "Co-Founder & CEO", "clem@huggingface.co", "https://www.linkedin.com/in/clementdelangue", "https://x.com/ClementDelangue"),
        ("Thomas Wolf", "Co-Founder & CSO", "thomas@huggingface.co", "https://www.linkedin.com/in/thomas-wolf-a056857", "https://x.com/Thom_Wolf")
    ], "Largest global open data repository powering frontier model pre-training; FineWeb and Cosmos datasets.", "https://huggingface.co"),

    ("Ai2 (Allen Institute for AI)", "allenai.org", [
        ("Ali Farhadi", "Chief Executive Officer", "alif@allenai.org", "https://www.linkedin.com/in/ali-farhadi", "https://x.com/alifarhadi"),
        ("Luca Soldaini", "Senior Applied Research Scientist", "lucas@allenai.org", "https://www.linkedin.com/in/lucasoldaini", "")
    ], "Creators of Dolma 3-trillion token pretraining corpus and OLMo open language model evaluation suites.", "https://allenai.org"),

    ("Common Crawl", "commoncrawl.org", [
        ("Rich Skrenta", "Board Member & Advisory", "rich@commoncrawl.org", "https://www.linkedin.com/in/skrenta", "https://x.com/skrenta"),
        ("Pedro Ortiz", "Director of Infrastructure", "pedro@commoncrawl.org", "https://www.linkedin.com/in/pedroortiz", "")
    ], "Non-profit maintaining open web crawl datasets forming the foundation of virtually all modern frontier LLMs.", "https://commoncrawl.org"),

    # 9. Specialized Domain Text & Translation Corpora
    ("Intron Health Speech", "intron.io", [
        ("Tobi Olatunji", "Founder & CEO", "tobi@intron.io", "https://www.linkedin.com/in/tobitunji", "https://x.com/tobitunji"),
        ("Imaobong Ibanga", "Sales & Partnerships Lead", "imaobong@intron.io", "https://www.linkedin.com/in/imaobong-ibanga", "")
    ], "AfriSpeech clinical speech corpus and multi-accent African medical transcription benchmarks.", "https://intron.io"),

    ("Sarvam AI Corpora", "sarvam.ai", [
        ("Vivek Raghavan", "Co-Founder", "vivek@sarvam.ai", "https://www.linkedin.com/in/vivekraghavan", "https://x.com/vivekraghavan"),
        ("Pratyush Kumar", "Co-Founder", "pratyush@sarvam.ai", "https://www.linkedin.com/in/pratyushkumar", "")
    ], "Sovereign Indian language LLMs trained on curated vernacular audio and translation benchmark corpora.", "https://sarvam.ai"),

    ("Aya Data Medical", "ayadata.ai", [
        ("Freddie Monk", "Co-Founder & CEO", "freddie@ayadata.ai", "https://uk.linkedin.com/in/freddie-monk-38347456", ""),
        ("Ama Larbi-Siaw", "Co-Founder", "ama@ayadata.ai", "https://www.linkedin.com/in/ama-larbi-siaw", "")
    ], "Medical diagnostics and localized low-resource African dialect annotation and quality scoring.", "https://ayadata.ai"),

    ("Deccan AI STEM", "deccan.ai", [
        ("Siddharth Sharma", "Founder & CEO", "siddharth@deccan.ai", "https://www.linkedin.com/in/siddharthsharma-ai", ""),
        ("Pooja Nair", "Head of STEM Curriculum", "pooja@deccan.ai", "https://www.linkedin.com/in/poojanair", "")
    ], "High-complexity mathematical step-by-step reasoning proofs and engineering evaluation datasets.", "https://deccan.ai"),

    ("Soul AI Human QA", "soul.ai", [
        ("Abhishek Tiwari", "Co-Founder & CEO", "abhishek@soul.ai", "https://www.linkedin.com/in/abhishektiwari", ""),
        ("Rajat Verma", "Head of Data Quality", "rajat@soul.ai", "https://www.linkedin.com/in/rajatverma", "")
    ], "Multi-turn conversational human feedback and adversarial safety red-teaming for dialogue models.", "https://soul.ai"),

    ("Humyn Labs Code Evals", "humyn.ai", [
        ("Nikhil Gupta", "Founder & CEO", "nikhil@humyn.ai", "https://www.linkedin.com/in/nikhilguptalabs", ""),
        ("Tanmay Bansal", "Chief Architect", "tanmay@humyn.ai", "https://www.linkedin.com/in/tanmaybansal", "")
    ], "Independent expert human scoring and rubric evaluation for code LLMs and autonomous software agents.", "https://humyn.ai"),

    ("Dhvani AI Audio", "dhvani.ai", [
        ("Sanjay Kumar", "Director of Datasets", "sanjay@dhvani.ai", "https://www.linkedin.com/in/sanjaykumar-ai", ""),
        ("Sunita Rao", "Lead Acoustic Engineer", "sunita@dhvani.ai", "https://www.linkedin.com/in/sunitarao", "")
    ], "Field-recorded vernacular speech corpora across 18 regional Indian states for conversational AI training.", "https://dhvani.ai"),

    ("Dubverse Naturalness", "dubverse.ai", [
        ("Varshul Goyal", "Co-Founder & CEO", "varshul@dubverse.ai", "https://www.linkedin.com/in/varshulgoyal", "https://x.com/varshulgoyal"),
        ("Anuja Dhawan", "Co-Founder", "anuja@dubverse.ai", "https://www.linkedin.com/in/anujadhawan", "")
    ], "Human-evaluated multi-language audio dubbing datasets measuring emotional prosody and lip-sync naturalness.", "https://dubverse.ai"),

    ("Reverie Language Localization", "reverieinc.com", [
        ("Arvind Pani", "Co-Founder & CEO", "arvind@reverieinc.com", "https://www.linkedin.com/in/arvindpani", ""),
        ("Sachin Joshi", "VP Language Technologies", "sjoshi@reverieinc.com", "https://www.linkedin.com/in/sachinjoshi", "")
    ], "Localization and transliteration benchmark datasets covering government and banking portals in Indic languages.", "https://reverieinc.com"),

    ("Resemble AI Watermark", "resemble.ai", [
        ("Zohaib Ahmed", "Co-Founder & CEO", "zohaib@resemble.ai", "https://www.linkedin.com/in/zohaibahmed", "https://x.com/zohaibahmed"),
        ("Saad Bashir", "VP Engineering", "saad@resemble.ai", "https://www.linkedin.com/in/saadbashir", "")
    ], "Deepfake audio detection datasets and imperceptible synthetic speech watermarking evaluation corpora.", "https://resemble.ai"),

    # 10. Financial, Transactional & Consumer Spend Data
    ("Consumer Edge Intelligence", "consumer-edge.com", [
        ("Bill Peck", "Founder & CEO", "bpeck@consumer-edge.com", "https://www.linkedin.com/in/billpeck", ""),
        ("Michael Gunther", "Head of Data Strategy", "mgunther@consumer-edge.com", "https://www.linkedin.com/in/michaelgunther", "")
    ], "Real-time debit and credit card transaction data across 100M+ global consumers for macro predictive AI.", "https://consumer-edge.com"),

    ("Second Measure (Bloomberg)", "secondmeasure.com", [
        ("Mike Vax", "Head of Engineering", "mvax@secondmeasure.com", "https://www.linkedin.com/in/mikevax", ""),
        ("Lillian Chou", "Head of Data Operations", "lchou@secondmeasure.com", "https://www.linkedin.com/in/lillianchou", "")
    ], "Billion-dollar consumer transaction tracking analytics providing training signals for economic models.", "https://secondmeasure.com"),

    ("Earnest Analytics", "earnestanalytics.com", [
        ("Kevin Carson", "Founder & CEO", "kcarson@earnestanalytics.com", "https://www.linkedin.com/in/kevin-carson", ""),
        ("David Fagan", "Chief Technology Officer", "dfagan@earnestanalytics.com", "https://www.linkedin.com/in/davidfagan", "")
    ], "Consumer purchasing behavior datasets tracking over 40 million US credit cards across thousands of merchants.", "https://earnestanalytics.com"),

    ("Facteus Financial Data", "facteus.com", [
        ("Chris Marsh", "Chief Executive Officer", "cmarsh@facteus.com", "https://www.linkedin.com/in/chrismarsh", ""),
        ("Jonathan Chin", "Co-Founder & Head of Data Assets", "jchin@facteus.com", "https://www.linkedin.com/in/jonathanchin", "")
    ], "Synthetic and raw financial transaction data derived from commercial debit cards and banking pipelines.", "https://facteus.com"),

    ("YipitData Alternative", "yipitdata.com", [
        ("Vinicius Vacanti", "Co-Founder & CEO", "vin@yipitdata.com", "https://www.linkedin.com/in/viniciusvacanti", "https://x.com/vinvacanti"),
        ("Jim Moran", "Co-Founder", "jim@yipitdata.com", "https://www.linkedin.com/in/jimmoran", "")
    ], "Web-scraped merchant and marketplace datasets for financial institutions and enterprise forecasting models.", "https://yipitdata.com"),

    ("Dataminr Signals", "dataminr.com", [
        ("Ted Bailey", "Founder & CEO", "tbailey@dataminr.com", "https://www.linkedin.com/in/tedbailey", "https://x.com/tedbailey"),
        ("Jason Robinson", "President & COO", "jrobinson@dataminr.com", "https://www.linkedin.com/in/jason-robinson-dataminr", "")
    ], "Real-time AI event and breaking information detection datasets streaming from public web, sensor, and audio logs.", "https://dataminr.com"),

    ("Similarweb Digital", "similarweb.com", [
        ("Or Offer", "Founder & CEO", "or@similarweb.com", "https://www.linkedin.com/in/oroffer", "https://x.com/oroffer"),
        ("Benjamin Seror", "Chief Product Officer", "benjamin.seror@similarweb.com", "https://www.linkedin.com/in/benjaminseror", "")
    ], "Global web traffic, search behavior, and app usage datasets covering billions of digital customer journeys.", "https://similarweb.com"),

    ("Bright Data Datasets", "brightdata.com", [
        ("Or Lenchner", "Chief Executive Officer", "or@brightdata.com", "https://www.linkedin.com/in/orlenchner", "https://x.com/orlenchner"),
        ("Omri Orgad", "Chief Customer Officer", "omrio@brightdata.com", "https://www.linkedin.com/in/omriorgad", "")
    ], "Commercially cleared structured ecommerce, corporate registry, and public social datasets for AI pretraining.", "https://brightdata.com"),

    ("Veraset Mobility", "veraset.com", [
        ("Kevin Collins", "Chief Executive Officer", "kevin@veraset.com", "https://www.linkedin.com/in/kevin-collins-veraset", ""),
        ("Dan Scudder", "VP Data Partnerships", "dan@veraset.com", "https://www.linkedin.com/in/danscudder", "")
    ], "Anonymized global population movement and GPS mobility datasets delivering billions of spatial telemetry points.", "https://veraset.com"),

    ("Gravy Analytics Data", "gravyanalytics.com", [
        ("Jeff White", "Founder & CEO", "jwhite@gravyanalytics.com", "https://www.linkedin.com/in/jeffwhite-gravy", ""),
        ("Jeremy Pinkham", "Chief Financial Officer", "jpinkham@gravyanalytics.com", "https://www.linkedin.com/in/jeremypinkham", "")
    ], "Location-based consumer foot traffic and venue visitation datasets for retail forecasting and spatial AI.", "https://gravyanalytics.com")
]
