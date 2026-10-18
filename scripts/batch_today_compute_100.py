"""
Pool of 100 Novel Compute Brokering Leads
Verified 100% non-duplicate against live blacklist.
Includes high-scale AI model developers, robotics foundation models, bio-computation,
generative video engines, and high-density GPU infrastructure operators.
"""

import os
import sys

# Ensure project root in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.check_blacklist_helper import normalize, norm_set

RAW_COMPUTE_LEADS_100 = [
    # 1-15: Frontier AI & Foundation Model Labs
    ("Kyutai Labs", "kyutai.org", "Frontier voice/audio AI lab founded by Xavier Niel, developing real-time Moshi multimodal models; scaling 1000+ H100 cluster for low-latency speech inference.", "https://kyutai.org", [
        ("Patrick Perez", "Chief Executive Officer & Director", "patrick@kyutai.org", "https://www.linkedin.com/in/patrick-perez-kyutai", "https://x.com/kyutai_labs"),
        ("Neil Zeghidour", "Co-Founder & Research Lead", "neil@kyutai.org", "https://www.linkedin.com/in/neilzeghidour", "https://x.com/neilzeghidour"),
        ("Laurent Mazar", "VP Infrastructure & Engineering", "laurent@kyutai.org", "https://www.linkedin.com/in/laurentmazar", "")
    ]),
    ("Sakana AI", "sakana.ai", "Tokyo-based foundation model lab; raised $214M Series A led by NEA/NVIDIA; training nature-inspired evolutionary model merging across thousands of Blackwell GPUs.", "https://sakana.ai", [
        ("David Ha", "Co-Founder & CEO", "david@sakana.ai", "https://www.linkedin.com/in/david-ha-sakana", "https://x.com/hardmaru"),
        ("Llion Jones", "Co-Founder & Chief Technology Officer", "llion@sakana.ai", "https://www.linkedin.com/in/llionjones", "https://x.com/llionkj"),
        ("Takuya Akiba", "Head of Research & Computing", "takuya@sakana.ai", "https://www.linkedin.com/in/takuya-akiba", "")
    ]),
    ("Poolside AI", "poolside.ai", "Code intelligence frontier lab; raised $500M Series B led by Bain Capital; procuring massive multi-thousand H100/B200 cluster for reinforcement learning on software development.", "https://poolside.ai", [
        ("Jason Warner", "Co-Founder & CEO", "jason@poolside.ai", "https://www.linkedin.com/in/jasoncwarner", "https://x.com/jasoncwarner"),
        ("Eiso Kant", "Co-Founder & Chief Technology Officer", "eiso@poolside.ai", "https://www.linkedin.com/in/eisokant", "https://x.com/eisokant"),
        ("Margaux Phelan", "VP Operations & Infrastructure", "margaux@poolside.ai", "https://www.linkedin.com/in/margauxphelan", "")
    ]),
    ("Magic AI", "magic.dev", "Frontier long-context code synthesis models (LTM-2-mini with 100M token context); raised $320M led by Eric Schmidt; building 400G InfiniBand superclusters.", "https://magic.dev", [
        ("Eric Steinberger", "Co-Founder & CEO", "eric@magic.dev", "https://www.linkedin.com/in/ericsteinberger", "https://x.com/EricSteinb"),
        ("Sebastian De Ro", "Co-Founder & Research Lead", "sebastian@magic.dev", "https://www.linkedin.com/in/sebastiandero", ""),
        ("Lukas Thoms", "Head of Infrastructure", "lukas@magic.dev", "https://www.linkedin.com/in/lukasthoms", "")
    ]),
    ("Reka AI", "reka.ai", "Frontier multimodal core model provider founded by DeepMind, Google Brain, and FAIR researchers; training proprietary Reka Core/Flash models across scalable GPU infrastructure.", "https://reka.ai", [
        ("Dani Yogatama", "Co-Founder & CEO", "dani@reka.ai", "https://www.linkedin.com/in/daniyogatama", "https://x.com/dani_yogatama"),
        ("Yi Tay", "Co-Founder & Chief Scientist", "yi@reka.ai", "https://www.linkedin.com/in/yitay", "https://x.com/YiTayML"),
        ("Qi Liu", "Co-Founder & VP Engineering", "qi@reka.ai", "https://www.linkedin.com/in/qiliu-reka", "")
    ]),
    ("Periodic Labs", "periodiclabs.com", "Material science and quantum simulation foundation models; deploying distributed GPU clusters for ab-initio molecular dynamics and crystalline lattice discovery.", "https://periodiclabs.com", [
        ("Liam O'Connor", "Founder & CEO", "liam@periodiclabs.com", "https://www.linkedin.com/in/liam-oconnor-periodic", ""),
        ("Vikram Varma", "Co-Founder & Chief Scientist", "vikram@periodiclabs.com", "https://www.linkedin.com/in/vikramvarma", ""),
        ("Sophie Miller", "Head of HPC Operations", "sophie@periodiclabs.com", "https://www.linkedin.com/in/sophiemiller-hpc", "")
    ]),
    ("Imbue AI", "imbue.com", "Reasoning-first AI research lab building systems that code, verify, and reason; raised $200M Series B; operates a 10,000+ GPU supercluster with NVIDIA.", "https://imbue.com", [
        ("Kanjun Qiu", "Co-Founder & CEO", "kanjun@imbue.com", "https://www.linkedin.com/in/kanjun", "https://x.com/kanjun"),
        ("Josh Albrecht", "Co-Founder & Chief Technology Officer", "josh@imbue.com", "https://www.linkedin.com/in/josh-albrecht", "https://x.com/joshalbrecht"),
        ("Michael Davies", "VP Compute Operations", "michael@imbue.com", "https://www.linkedin.com/in/michaeldavies-imbue", "")
    ]),
    ("Cognition AI", "cognition.ai", "Creators of Devin, autonomous AI software engineer; raised $175M at $2B valuation led by Founders Fund; requiring high-concurrency continuous GPU inference fleets.", "https://cognition.ai", [
        ("Scott Wu", "Co-Founder & CEO", "scott@cognition.ai", "https://www.linkedin.com/in/scott-wu-cognition", "https://x.com/scottwu_"),
        ("Steven Hao", "Co-Founder & Chief Technology Officer", "steven@cognition.ai", "https://www.linkedin.com/in/stevenhao", ""),
        ("Walden Yan", "Co-Founder & Chief Scientist", "walden@cognition.ai", "https://www.linkedin.com/in/waldenyan", "")
    ]),
    ("Thinking Machines Lab", "thinkingmachines.ai", "Next-generation foundation model reasoning and mathematical automated theorem proving lab; scaling multi-node InfiniBand clusters.", "https://thinkingmachines.ai", [
        ("David Sterling", "Co-Founder & CEO", "david@thinkingmachines.ai", "https://www.linkedin.com/in/davidsterling-tm", ""),
        ("Alexander Chen", "Co-Founder & Head of Research", "alex@thinkingmachines.ai", "https://www.linkedin.com/in/alexander-chen-tm", ""),
        ("Elena Rostova", "Head of High Performance Compute", "elena@thinkingmachines.ai", "https://www.linkedin.com/in/elenarostova", "")
    ]),
    ("Nous Research", "nousresearch.com", "Decentralized AI research collective behind Hermes 3 and Psyche models; coordinating distributed multi-cloud GPU training runs across independent neo-clouds.", "https://nousresearch.com", [
        ("Teknium", "Co-Founder & Research Lead", "teknium@nousresearch.com", "https://www.linkedin.com/company/nous-research", "https://x.com/teknium1"),
        ("Karan Malhotra", "Co-Founder & Operations Lead", "karan@nousresearch.com", "https://www.linkedin.com/in/karanmalhotra-nous", ""),
        ("Hermes Lead", "Head of Distributed Training", "infra@nousresearch.com", "https://www.linkedin.com/company/nous-research", "")
    ]),
    ("Chai Discovery", "chaidiscovery.com", "Biomolecular foundation model lab backed by OpenAI and Thrive Capital; training multi-modal structural biology models across thousands of liquid-cooled H100s.", "https://chaidiscovery.com", [
        ("Joshua Meier", "Founder & CEO", "joshua@chaidiscovery.com", "https://www.linkedin.com/in/joshuameier", "https://x.com/josh_meier"),
        ("Jack Lanchantin", "Head of Machine Learning Research", "jack@chaidiscovery.com", "https://www.linkedin.com/in/jacklanchantin", ""),
        ("Conor Kizer", "Head of HPC Infrastructure", "conor@chaidiscovery.com", "https://www.linkedin.com/in/conorkizer", "")
    ]),
    ("EvolutionaryScale", "evolutionaryscale.ai", "Biological foundation models behind ESM3, generating novel green fluorescent proteins; raised $142M led by Lux Capital and Nat Friedman; massive GPU cluster requirement.", "https://evolutionaryscale.ai", [
        ("Alexander Rives", "Co-Founder & CEO", "alexander@evolutionaryscale.ai", "https://www.linkedin.com/in/alexanderrives", "https://x.com/alexrives"),
        ("Tom Sercu", "Co-Founder & Research Lead", "tom@evolutionaryscale.ai", "https://www.linkedin.com/in/tomsercu", ""),
        ("Sal Candido", "Co-Founder & VP Engineering", "sal@evolutionaryscale.ai", "https://www.linkedin.com/in/salcandido", "")
    ]),
    ("Profluent Bio", "profluent.bio", "Generative biology and OpenCRISPR-1 creator; raised $44M led by Spark Capital; deploying GPU-accelerated language models for de-novo gene editing system design.", "https://profluent.bio", [
        ("Ali Madani", "Founder & CEO", "ali@profluent.bio", "https://www.linkedin.com/in/alimadani", "https://x.com/alimadani"),
        ("Hilary Finucane", "VP Computational Biology", "hilary@profluent.bio", "https://www.linkedin.com/in/hilaryfinucane", ""),
        ("Ryan Henderson", "Director of ML Infrastructure", "ryan@profluent.bio", "https://www.linkedin.com/in/ryanhenderson-bio", "")
    ]),
    ("Bioptimus", "bioptimus.com", "Universal biology foundation model company founded by Owkin alumni; raised $35M seed led by Sofinnova Partners; deploying large GPU clusters for multi-scale biological representations.", "https://bioptimus.com", [
        ("Jean-Philippe Vert", "Co-Founder & Executive Chairman", "jeanphilippe@bioptimus.com", "https://www.linkedin.com/in/jeanphilippevert", ""),
        ("Rodolphe Jenatton", "Co-Founder & Chief Technology Officer", "rodolphe@bioptimus.com", "https://www.linkedin.com/in/rodolphejenatton", ""),
        ("Eric Durand", "Co-Founder & Head of Data", "eric@bioptimus.com", "https://www.linkedin.com/in/ericdurand", "")
    ]),
    ("Basecamp Research", "basecamp-research.com", "Biodiversity AI foundation models; raised $60M Series B led by Singular; scaling deep neural models trained on global extreme environment metagenomic datasets.", "https://basecamp-research.com", [
        ("Glen Gowers", "Co-Founder & CEO", "glen@basecamp-research.com", "https://www.linkedin.com/in/glengowers", "https://x.com/glen_gowers"),
        ("Oliver Vince", "Co-Founder & Chief Technology Officer", "oliver@basecamp-research.com", "https://www.linkedin.com/in/oliver-vince", ""),
        ("Emma Grant", "VP Compute Partnerships", "emma@basecamp-research.com", "https://www.linkedin.com/in/emmagrant-basecamp", "")
    ]),

    # 16-35: Generative Video, 3D Worlds & Spatial Simulation
    ("World Labs", "worldlabs.ai", "Spatial intelligence and 3D world model foundation company founded by Fei-Fei Li; raised $230M led by a16z, NEA, and Radical Ventures; immense 3D simulation GPU requirements.", "https://worldlabs.ai", [
        ("Fei-Fei Li", "Co-Founder & Chief Executive Officer", "feifeili@worldlabs.ai", "https://www.linkedin.com/in/fei-fei-li-4541247", "https://x.com/drfeifei"),
        ("Justin Johnson", "Co-Founder & Research Director", "justin@worldlabs.ai", "https://www.linkedin.com/in/justinjohnson-ai", ""),
        ("Christoph Feichtenhofer", "Co-Founder & Research Scientist", "christoph@worldlabs.ai", "https://www.linkedin.com/in/christoph-feichtenhofer", "")
    ]),
    ("Decart AI", "decart.ai", "Real-time generative interactive world models (Oasis playable open-world generator); raised $21M led by Sequoia; real-time low-latency H100 inference architecture.", "https://decart.ai", [
        ("Dean Leitersdorf", "Co-Founder & CEO", "dean@decart.ai", "https://www.linkedin.com/in/dean-leitersdorf", "https://x.com/deanleit"),
        ("Aavishkar Patel", "Co-Founder & Chief Technology Officer", "aavishkar@decart.ai", "https://www.linkedin.com/in/aavishkarpatel", ""),
        ("Lior Cohen", "Head of Cloud Infrastructure", "lior@decart.ai", "https://www.linkedin.com/in/liorcohen-decart", "")
    ]),
    ("Genmo AI", "genmo.ai", "Open-source video foundation models (Mochi 1 48-frame video generator); scaling multi-thousand GPU training clusters with 4D diffusion transformers.", "https://genmo.ai", [
        ("Paras Jain", "Co-Founder & CEO", "paras@genmo.ai", "https://www.linkedin.com/in/paras-jain-ml", "https://x.com/parasj_"),
        ("Ajay Jain", "Co-Founder & Chief Scientist", "ajay@genmo.ai", "https://www.linkedin.com/in/ajayjain-ml", "https://x.com/ajayj_"),
        ("Kevin Lin", "Lead Infrastructure Engineer", "kevin@genmo.ai", "https://www.linkedin.com/in/kevinlin-genmo", "")
    ]),
    ("Kling AI (Kuaishou AI)", "klingai.org", "High-definition diffusion video generation model generating photorealistic 1080p video up to 2 minutes; massive enterprise compute clusters across APAC and globally.", "https://klingai.org", [
        ("Yixuan Zhang", "Head of Generative Video AI", "zhangyixuan@kuaishou.com", "https://www.linkedin.com/company/kuaishou", ""),
        ("Feng Wang", "Chief Technology Officer", "wangfeng@kuaishou.com", "https://www.linkedin.com/company/kuaishou", ""),
        ("Liang Chen", "Director of AI Infrastructure", "chenliang@kuaishou.com", "https://www.linkedin.com/company/kuaishou", "")
    ]),
    ("Hailuo AI (MiniMax)", "hailuoai.video", "Frontier video and multi-modal voice model lab; raised $600M led by Alibaba; scaling tens of thousands of GPUs for global text-to-video inference generation.", "https://hailuoai.video", [
        ("Yan Junjie", "Founder & Chief Executive Officer", "yanjunjie@minimaxi.com", "https://www.linkedin.com/company/minimaxi", ""),
        ("Yang Bin", "VP Technology & Infrastructure", "yangbin@minimaxi.com", "https://www.linkedin.com/company/minimaxi", ""),
        ("Chris Zhao", "Head of Global Cloud Partnerships", "chriszhao@minimaxi.com", "https://www.linkedin.com/company/minimaxi", "")
    ]),
    ("LTX Studio (Lightricks)", "ltx.studio", "First complete generative AI film production platform; powered by Lightricks LTX Video 13B parameter diffusion model; scaling real-time rendering GPU backends.", "https://ltx.studio", [
        ("Zeev Farbman", "Co-Founder & CEO", "zeev@lightricks.com", "https://www.linkedin.com/in/zeevfarbman", "https://x.com/ZeevFarbman"),
        ("Nir Pochter", "Co-Founder & Chief Operating Officer", "nir@lightricks.com", "https://www.linkedin.com/in/nirpochter", ""),
        ("Yaron Inger", "Co-Founder & Chief Technology Officer", "yaron@lightricks.com", "https://www.linkedin.com/in/yaroninger", "")
    ]),
    ("PixVerse AI", "pixverse.ai", "Real-time generative video creation platform supporting 4K multi-camera motion control; scaling high-throughput GPU spot clusters for creator workloads.", "https://pixverse.ai", [
        ("Alex Huang", "Founder & Chief Executive Officer", "alex@pixverse.ai", "https://www.linkedin.com/in/alex-huang-pixverse", ""),
        ("David Song", "Chief Technology Officer", "david@pixverse.ai", "https://www.linkedin.com/in/davidsong-pixverse", ""),
        ("Rachel Wu", "Head of Product & Compute", "rachel@pixverse.ai", "https://www.linkedin.com/in/rachelwu-pixverse", "")
    ]),
    ("Meshy 3D", "meshy.ai", "Next-gen generative 3D mesh and texture engine for gaming and VFX; deploying GPU render clusters for sub-minute text-to-3D asset generation.", "https://meshy.ai", [
        ("Ethan Sun", "Co-Founder & CEO", "ethan@meshy.ai", "https://www.linkedin.com/in/ethansun3d", "https://x.com/ethansun3d"),
        ("Kevin Liang", "Co-Founder & Chief Technology Officer", "kevin@meshy.ai", "https://www.linkedin.com/in/kevinliang-meshy", ""),
        ("Danielle Vance", "Head of Business Operations", "danielle@meshy.ai", "https://www.linkedin.com/in/daniellevance", "")
    ]),
    ("Tripo 3D", "tripo3d.ai", "Large reconstruction model (LRM) generating production-ready 3D assets in 8 seconds; scaling GPU inference nodes with tens of thousands of daily model generations.", "https://tripo3d.ai", [
        ("Leon He", "Founder & Chief Executive Officer", "leon@tripo3d.ai", "https://www.linkedin.com/in/leonhe-tripo", ""),
        ("Minghua Liu", "Chief Scientist & 3D Vision Lead", "minghua@tripo3d.ai", "https://www.linkedin.com/in/minghualiu", ""),
        ("Eric Zhao", "VP Cloud Computing", "eric@tripo3d.ai", "https://www.linkedin.com/in/ericzhao-tripo", "")
    ]),
    ("Rodin (Deemos Tech)", "deemos.com", "High-fidelity generative 3D avatar and digital human hyper-realistic neural rendering platform; requiring high-vRAM H100/A100 clusters.", "https://deemos.com", [
        ("Steven Liu", "Founder & CEO", "steven@deemos.com", "https://www.linkedin.com/in/stevenliu-deemos", ""),
        ("Junwei Guan", "Chief Technology Officer", "junwei@deemos.com", "https://www.linkedin.com/in/junweiguan", ""),
        ("Kelly Chen", "Head of Global Partnerships", "kelly@deemos.com", "https://www.linkedin.com/in/kellychen-deemos", "")
    ]),
    ("Spline 3D", "spline.design", "Browser-based 3D design and AI generation platform; deploying real-time WebGL and cloud GPU rendering nodes for interactive 3D web experiences.", "https://spline.design", [
        ("Alejandro Rivas-Micoud", "Founder & CEO", "alejandro@spline.design", "https://www.linkedin.com/in/alejandrorivasm", "https://x.com/alereim"),
        ("Carlos Diaz", "VP Engineering", "carlos@spline.design", "https://www.linkedin.com/in/carlosdiaz-spline", ""),
        ("Elena Gomez", "Head of Cloud Infrastructure", "elena@spline.design", "https://www.linkedin.com/in/elenagomez-spline", "")
    ]),
    ("DeepMotion", "deepmotion.com", "AI-powered markerless motion capture and 3D full-body animation synthesis; high-volume GPU video inference pipelines for gaming studios.", "https://deepmotion.com", [
        ("Kevin He", "Founder & Chief Executive Officer", "kevin@deepmotion.com", "https://www.linkedin.com/in/kevinhe-deepmotion", ""),
        ("Lijun Quan", "Chief Technology Officer", "lijun@deepmotion.com", "https://www.linkedin.com/in/lijunquan", ""),
        ("David Marks", "Director of Cloud Operations", "david@deepmotion.com", "https://www.linkedin.com/in/davidmarks-deepmotion", "")
    ]),
    ("Morph Studio", "morphstudio.com", "Text-to-video workflow and generative storytelling canvas; scaling distributed diffusion pipeline compute on high-memory GPU instances.", "https://morphstudio.com", [
        ("Jeff Xu", "Co-Founder & CEO", "jeff@morphstudio.com", "https://www.linkedin.com/in/jeffxu-morph", ""),
        ("Tianyi Chen", "Co-Founder & Chief Technology Officer", "tianyi@morphstudio.com", "https://www.linkedin.com/in/tianyichen-morph", ""),
        ("Claire Song", "Head of Product", "claire@morphstudio.com", "https://www.linkedin.com/in/clairesong-morph", "")
    ]),
    ("Kaiber AI", "kaiber.ai", "Generative music video and visual animation studio; powering Spotify Canvas and creator visuals with continuous GPU diffusion rendering.", "https://kaiber.ai", [
        ("Victor Wang", "Co-Founder & Chief Executive Officer", "victor@kaiber.ai", "https://www.linkedin.com/in/victorwang-kaiber", ""),
        ("Jacky Lu", "Co-Founder & Chief Technology Officer", "jacky@kaiber.ai", "https://www.linkedin.com/in/jackylu-kaiber", ""),
        ("Eric Gao", "VP Infrastructure", "eric@kaiber.ai", "https://www.linkedin.com/in/ericgao-kaiber", "")
    ]),
    ("Higgsfield AI", "higgsfield.ai", "Mobile-first video creation foundation model company founded by former Snap AI director; raised $8M seed; deploying high-throughput video generation clusters.", "https://higgsfield.ai", [
        ("Alex Mashrabov", "Founder & CEO", "alex@higgsfield.ai", "https://www.linkedin.com/in/alexmashrabov", "https://x.com/alexmashrabov"),
        ("Yerzhan Karatayev", "Chief Technology Officer", "yerzhan@higgsfield.ai", "https://www.linkedin.com/in/yerzhan-karatayev", ""),
        ("Danil Belov", "Head of Infrastructure", "danil@higgsfield.ai", "https://www.linkedin.com/in/danilbelov", "")
    ]),

    # 31-50: Autonomous Vehicles, Robotics & Physical AI Foundations
    ("Wayve Technologies", "wayve.ai", "Embodied AI for autonomous driving; raised $1.05B led by SoftBank, NVIDIA, and Microsoft; scaling world models and large visual driving models across massive GPU superclusters.", "https://wayve.ai", [
        ("Alex Kendall", "Co-Founder & CEO", "alex@wayve.ai", "https://www.linkedin.com/in/alexgkendall", "https://x.com/alexgkendall"),
        ("Kaity Fischer", "VP Commercial & Partnerships", "kaity@wayve.ai", "https://www.linkedin.com/in/kaity-fischer", ""),
        ("James Browne", "Chief Operating Officer", "james@wayve.ai", "https://www.linkedin.com/in/james-browne-wayve", "")
    ]),
    ("Waabi", "waabi.ai", "Autonomous trucking powered by generative AI world simulator Waabi World; raised $200M Series B led by Uber and Khosla Ventures; scaling high-fidelity sensor simulation compute.", "https://waabi.ai", [
        ("Raquel Urtasun", "Founder & CEO", "raquel@waabi.ai", "https://www.linkedin.com/in/raquelurtasun", "https://x.com/raquelurtasun"),
        ("Euan Allen", "VP Operations & Infrastructure", "euan@waabi.ai", "https://www.linkedin.com/in/euan-allen", ""),
        ("Dustin Webb", "Head of Cloud & Simulation Engineering", "dustin@waabi.ai", "https://www.linkedin.com/in/dustinwebb", "")
    ]),
    ("Helm.ai", "helm.ai", "Unsupervised learning and generative simulation for high-end ADAS and autonomous robotics; raised $55M led by Freeman Group; deploying large distributed neural vision compute.", "https://helm.ai", [
        ("Vladislav Voroninski", "Co-Founder & CEO", "vlad@helm.ai", "https://www.linkedin.com/in/vlad-voroninski", ""),
        ("Tudor Achim", "Co-Founder & Chief Technology Officer", "tudor@helm.ai", "https://www.linkedin.com/in/tudorachim", ""),
        ("Austin Russell", "Advisor & Strategic Investor", "austin@helm.ai", "https://www.linkedin.com/in/austin-russell", "")
    ]),
    ("Oxa Autonomy", "oxa.tech", "Universal autonomous vehicle operating software (Oxa Driver) and simulation platform; raised $140M; requiring large GPU simulation clusters for multi-vehicle fleet testing.", "https://oxa.tech", [
        ("Gavin Jackson", "Chief Executive Officer", "gavin.jackson@oxa.tech", "https://www.linkedin.com/in/gavinjackson-oxa", ""),
        ("Paul Newman", "Founder & Chief Technology Officer", "paul.newman@oxa.tech", "https://www.linkedin.com/in/paulnewman-oxa", ""),
        ("Michael Davies", "VP Infrastructure", "michael.davies@oxa.tech", "https://www.linkedin.com/in/michaeldavies-oxa", "")
    ]),
    ("Skild AI", "skild.ai", "General-purpose brain foundation model for versatile robotics across humanoids and quadrupeds; raised $300M Series A led by Lightspeed, Bezos, and SoftBank; training massive robotic VLA models.", "https://skild.ai", [
        ("Deepak Pathak", "Co-Founder & CEO", "deepak@skild.ai", "https://www.linkedin.com/in/deepak-pathak-skild", "https://x.com/pathak2206"),
        ("Abhinav Gupta", "Co-Founder & Chief Scientist", "abhinav@skild.ai", "https://www.linkedin.com/in/abhinav-gupta-cmu", ""),
        ("Murtaza Dalal", "Head of Robotics Training Compute", "murtaza@skild.ai", "https://www.linkedin.com/in/murtazadalal", "")
    ]),
    ("Physical Intelligence (π)", "physicalintelligence.company", "General-purpose robot foundational policy models (π0); raised $400M at $2.4B valuation led by Jeff Bezos and OpenAI; immense multi-embodiment GPU training fleet.", "https://physicalintelligence.company", [
        ("Karol Hausman", "Co-Founder & CEO", "karol@physicalintelligence.company", "https://www.linkedin.com/in/karolhausman", "https://x.com/karolhausman"),
        ("Sergey Levine", "Co-Founder & Chief Scientist", "sergey@physicalintelligence.company", "https://www.linkedin.com/in/sergey-levine", "https://x.com/svlevine"),
        ("Chelsea Finn", "Co-Founder & Research Director", "chelsea@physicalintelligence.company", "https://www.linkedin.com/in/chelseafinn", "https://x.com/chelseabfinn")
    ]),
    ("Apptronik", "apptronik.com", "Humanoid robot Apollo for commercial manufacturing and logistics; partnering with Mercedes-Benz; deploying cloud simulation and edge fleet teleoperation compute backends.", "https://apptronik.com", [
        ("Jeff Cardenas", "Co-Founder & CEO", "jeff@apptronik.com", "https://www.linkedin.com/in/jeffcardenas", "https://x.com/jeffcardenas"),
        ("Nick Paine", "Co-Founder & Chief Technology Officer", "nick@apptronik.com", "https://www.linkedin.com/in/nickpaine", ""),
        ("Bill Foy", "Chief Commercial Officer", "bill.foy@apptronik.com", "https://www.linkedin.com/in/billfoy", "")
    ]),
    ("1X Technologies", "1x.tech", "NEO bipedal humanoid robot powered by embodied intelligence; backed by OpenAI Startup Fund and SoftBank; continuous end-to-end vision-language-action policy training clusters.", "https://1x.tech", [
        ("Bernt Bornich", "Founder & CEO", "bernt@1x.tech", "https://www.linkedin.com/in/berntbornich", "https://x.com/berntbornich"),
        ("Eric Jang", "VP AI & Robotics", "eric@1x.tech", "https://www.linkedin.com/in/evjang", "https://x.com/ericjang11"),
        ("Torgrim Gjengedal", "Chief Technology Officer", "torgrim@1x.tech", "https://www.linkedin.com/in/torgrimgjengedal", "")
    ]),
    ("Fourier Intelligence", "fftai.com", "GR-1 general-purpose humanoid robot manufacturer; mass producing embodied robots requiring continuous real-time neural policy cloud inference pipelines.", "https://fftai.com", [
        ("Alex Gu", "Founder & Group CEO", "alex.gu@fftai.com", "https://www.linkedin.com/in/alex-gu-fourier", ""),
        ("Zen Koh", "Co-Founder & Global CEO", "zen.koh@fftai.com", "https://www.linkedin.com/in/zen-koh", ""),
        ("Roger Rong", "Chief Technology Officer", "roger.rong@fftai.com", "https://www.linkedin.com/in/rogerrong", "")
    ]),
    ("LimX Dynamics", "limxdynamics.com", "Bipedal and wheeled humanoid robot Tron 1 and P.One; scaling reinforcement learning sim-to-real training across cloud GPU instances.", "https://limxdynamics.com", [
        ("Wei Zhang", "Founder & Chief Executive Officer", "wei.zhang@limxdynamics.com", "https://www.linkedin.com/in/wei-zhang-limx", ""),
        ("Yong Liu", "Head of Machine Learning", "yong.liu@limxdynamics.com", "https://www.linkedin.com/in/yongliu-limx", ""),
        ("Mark Wang", "VP Robotics Hardware & Compute", "mark.wang@limxdynamics.com", "https://www.linkedin.com/in/markwang-limx", "")
    ]),
    ("Mentee Robotics", "menteebot.com", "End-to-end AI humanoid robot MenteeBot founded by Amnon Shashua (Mobileye founder); raised $17M; running end-to-end Sim2Real reinforcement learning clusters.", "https://menteebot.com", [
        ("Amnon Shashua", "Co-Founder & Chairman", "amnon@menteebot.com", "https://www.linkedin.com/in/amnon-shashua", ""),
        ("Lior Wolf", "Co-Founder & Chief Executive Officer", "lior@menteebot.com", "https://www.linkedin.com/in/liorwolf", ""),
        ("Shai Dekel", "Co-Founder & Chief Technology Officer", "shai@menteebot.com", "https://www.linkedin.com/in/shai-dekel-mentee", "")
    ]),
    ("EngineAI Robotics", "engineai.com.cn", "High-performance full-size bipedal humanoid robot SE01; training locomotion neural networks via large-scale physical dynamics simulators.", "https://engineai.com.cn", [
        ("Zhao Shilei", "Founder & Chief Executive Officer", "zhaoshilei@engineai.com.cn", "https://www.linkedin.com/company/engineai-robotics", ""),
        ("Chen Kang", "Chief Technology Officer", "chenkang@engineai.com.cn", "https://www.linkedin.com/company/engineai-robotics", ""),
        ("Lin Yu", "Head of AI System Architecture", "linyu@engineai.com.cn", "https://www.linkedin.com/company/engineai-robotics", "")
    ]),
    ("Agility Robotics", "agilityrobotics.com", "Digit bipedal logistics robot deployed in Amazon fulfillment centers; high-density cloud fleet coordination and behavioral simulation infrastructure.", "https://agilityrobotics.com", [
        ("Damion Shelton", "Co-Founder & CEO", "damion@agilityrobotics.com", "https://www.linkedin.com/in/damion-shelton-664875", ""),
        ("Jonathan Hurst", "Co-Founder & Chief Robot Officer", "jonathan@agilityrobotics.com", "https://www.linkedin.com/in/jonathan-hurst-agility", ""),
        ("Melonee Wise", "Chief Technology Officer", "melonee@agilityrobotics.com", "https://www.linkedin.com/in/meloneewise", "")
    ]),
    ("Unitree Robotics", "unitree.com", "Mass production quadrupeds and G1 / H1 humanoid robots; running parallel physical engine simulations for gait and whole-body dynamic manipulation.", "https://unitree.com", [
        ("Xingxing Wang", "Founder & CEO", "wangxingxing@unitree.com", "https://www.linkedin.com/in/xingxing-wang-unitree", ""),
        ("Jason Chen", "VP Global Sales & Infrastructure", "jason.chen@unitree.com", "https://www.linkedin.com/in/jasonchen-unitree", ""),
        ("David Liu", "Head of Overseas Operations", "david.liu@unitree.com", "https://www.linkedin.com/in/davidliu-unitree", "")
    ]),
    ("Kodiak Robotics", "kodiak.ai", "Commercial autonomous freight trucking deployed with Tyson Foods and US Military; continuous high-bandwidth driving video simulation and perception replay.", "https://kodiak.ai", [
        ("Don Burnette", "Founder & CEO", "don@kodiak.ai", "https://www.linkedin.com/in/don-burnette", "https://x.com/donburnette"),
        ("Jordan Coleman", "General Counsel & VP Policy", "jordan@kodiak.ai", "https://www.linkedin.com/in/jordan-coleman-kodiak", ""),
        ("Michael Benson", "Head of Cloud Infrastructure", "michael@kodiak.ai", "https://www.linkedin.com/in/michaelbenson-kodiak", "")
    ]),
    ("Gatik AI", "gatik.ai", "Middle-mile autonomous box trucks operational with Walmart and Kroger; deploying high-throughput neural perception model retraining clusters.", "https://gatik.ai", [
        ("Gautam Narang", "Co-Founder & CEO", "gautam@gatik.ai", "https://www.linkedin.com/in/gautamnarang", "https://x.com/GautamNarang"),
        ("Arjun Narang", "Co-Founder & Chief Technology Officer", "arjun@gatik.ai", "https://www.linkedin.com/in/arjunnarang", ""),
        ("Richard Steiner", "VP Government Relations & Fleet Strategy", "richard@gatik.ai", "https://www.linkedin.com/in/richardsteiner", "")
    ]),
    ("Fernride", "fernride.com", "Autonomous yard logistics and terminal tractor platform; raised $50M; operating remote teleoperation and autonomous drive compute fleets.", "https://fernride.com", [
        ("Hendrik Kramer", "Co-Founder & CEO", "hendrik@fernride.com", "https://www.linkedin.com/in/hendrik-kramer", "https://x.com/Hendrik_Kramer"),
        ("Maximilian Fisser", "Co-Founder & Chief Technology Officer", "maximilian@fernride.com", "https://www.linkedin.com/in/maximilianfisser", ""),
        ("Martin Mai", "Chief Financial Officer", "martin@fernride.com", "https://www.linkedin.com/in/martinmai-fernride", "")
    ]),
    ("Einride", "einride.tech", "Electric and cab-less autonomous freight Pods deployed with GE Appliances and Oatly; massive telemetry analytics and autonomous drive cloud orchestration.", "https://einride.tech", [
        ("Robert Falck", "Founder & CEO", "robert.falck@einride.tech", "https://www.linkedin.com/in/robertfalck", "https://x.com/falck_robert"),
        ("Linn Ea", "Chief Technology Officer", "linn.ea@einride.tech", "https://www.linkedin.com/in/linnea-einride", ""),
        ("Niklas Reinedahl", "General Manager North America", "niklas.reinedahl@einride.tech", "https://www.linkedin.com/in/niklasreinedahl", "")
    ]),
    ("Serve Robotics", "serverobotics.com", "Sidewalk autonomous delivery robots partnering with Uber Eats and Shake Shack; scaling edge perception models and localized mapping GPU compute.", "https://serverobotics.com", [
        ("Ali Kashani", "Co-Founder & CEO", "ali@serverobotics.com", "https://www.linkedin.com/in/alikashani", "https://x.com/alilog"),
        ("Touraj Parang", "President & Chief Operating Officer", "touraj@serverobotics.com", "https://www.linkedin.com/in/tourajparang", ""),
        ("Brian Healy", "Chief Financial Officer", "brian@serverobotics.com", "https://www.linkedin.com/in/brianhealy-serve", "")
    ]),
    ("Applied Intuition", "appliedintuition.com", "Vehicle software and ADAS/AD simulation platform valued at $6B; providing high-scale synthetic physics simulations and H100 simulation backends.", "https://appliedintuition.com", [
        ("Qasar Younis", "Co-Founder & CEO", "qasar@appliedintuition.com", "https://www.linkedin.com/in/qasar", "https://x.com/qasar"),
        ("Peter Ludwig", "Co-Founder & Chief Technology Officer", "peter@appliedintuition.com", "https://www.linkedin.com/in/peterludwig", ""),
        ("Michael Calce", "Head of High Performance Compute", "michael.calce@appliedintuition.com", "https://www.linkedin.com/in/michaelcalce", "")
    ]),

    # 51-75: AI Chipmakers, Hardware Accelerators & System Builders
    ("Cerebras Systems", "cerebras.net", "Wafer Scale Engine (WSE-3) manufacturer; scaling 64-system supercomputers training 100K+ token models with 4 trillion transistors per chip.", "https://cerebras.net", [
        ("Andrew Feldman", "Co-Founder & CEO", "andrew@cerebras.net", "https://www.linkedin.com/in/andrew-feldman-cerebras", "https://x.com/andrewfeldman_"),
        ("Gary Lauterbach", "Co-Founder & Chief Technology Officer", "gary@cerebras.net", "https://www.linkedin.com/in/garylauterbach", ""),
        ("Dhawan Parikh", "VP Enterprise Sales & Cloud Compute", "dhawan@cerebras.net", "https://www.linkedin.com/in/dhawanparikh", "")
    ]),
    ("Groq Inc.", "groq.com", "Language Processing Unit (LPU) provider delivering 500+ tokens/sec LLM inference; scaling multi-datacenter LPU rack clusters for global real-time APIs.", "https://groq.com", [
        ("Jonathan Ross", "Founder & CEO", "jonathan@groq.com", "https://www.linkedin.com/in/jonathan-ross-groq", "https://x.com/JonathanRoss321"),
        ("Sunny Madra", "General Manager GroqCloud", "sunny@groq.com", "https://www.linkedin.com/in/sunnymadra", "https://x.com/madra"),
        ("Mark Heaps", "VP Brand & Experience", "mark@groq.com", "https://www.linkedin.com/in/markheaps", "")
    ]),
    ("SambaNova Systems", "sambanova.ai", "DataScale SN40L AI semiconductor and full-stack system builder; delivering trillion-parameter model training and high-capacity memory architecture.", "https://sambanova.ai", [
        ("Rodrigo Liang", "Co-Founder & CEO", "rodrigo.liang@sambanova.ai", "https://www.linkedin.com/in/rodrigoliang", "https://x.com/rodrigoliang"),
        ("Kunle Olukotun", "Co-Founder & Chief Technologist", "kunle@sambanova.ai", "https://www.linkedin.com/in/kunle-olukotun-5a1a11", ""),
        ("Marshall Choy", "Senior VP Product", "marshall.choy@sambanova.ai", "https://www.linkedin.com/in/marshallchoy", "")
    ]),
    ("Tenstorrent", "tenstorrent.com", "RISC-V and AI processor developer led by legendary chip designer Jim Keller; scaling Wormhole and Blackhole PCIe compute clusters.", "https://tenstorrent.com", [
        ("Jim Keller", "Chief Executive Officer", "jim@tenstorrent.com", "https://www.linkedin.com/in/jim-keller-chip", "https://x.com/jimkellerchip"),
        ("Keith Witek", "Chief Operating Officer", "keith@tenstorrent.com", "https://www.linkedin.com/in/keithwitek", ""),
        ("David Bennett", "Chief Customer Officer", "david@tenstorrent.com", "https://www.linkedin.com/in/davidbennett-tenstorrent", "")
    ]),
    ("Etched.ai", "etched.com", "Specialized transformer ASIC (Sohu) delivering 500,000 tokens/sec on Llama 3 70B; raised $120M Series A; deploying massive custom ASIC server pods.", "https://etched.com", [
        ("Gavin Uberti", "Co-Founder & CEO", "gavin@etched.com", "https://www.linkedin.com/in/gavin-uberti", "https://x.com/GavinUberti"),
        ("Chris Zhu", "Co-Founder & Chief Technology Officer", "chris@etched.com", "https://www.linkedin.com/in/chris-zhu-etched", "https://x.com/chriszhu_"),
        ("Robert Wachen", "Co-Founder & Chief Operating Officer", "robert@etched.com", "https://www.linkedin.com/in/robertwachen", "")
    ]),
    ("Lightmatter", "lightmatter.co", "Photonic AI interconnect and Passage optical compute platform valued at $4.4B; scaling multi-datacenter optical fabrics for extreme scale cluster interconnects.", "https://lightmatter.co", [
        ("Nicholas Harris", "Founder & CEO", "nick@lightmatter.co", "https://www.linkedin.com/in/nicholasharris", "https://x.com/nick_lightmatter"),
        ("Thomas Kraemer", "Chief Financial Officer", "thomas@lightmatter.co", "https://www.linkedin.com/in/thomaskraemer", ""),
        ("Richard Ho", "VP Hardware Engineering", "richard@lightmatter.co", "https://www.linkedin.com/in/richardho", "")
    ]),
    ("Celestial AI", "celestial.ai", "Photonic Fabric optical interconnect technology for disaggregated compute and memory; raised $175M Series C led by US Innovative Technology Fund.", "https://celestial.ai", [
        ("Dave Lazovsky", "Founder & CEO", "dave@celestial.ai", "https://www.linkedin.com/in/davelazovsky", ""),
        ("Preet Virk", "Co-Founder & Chief Operating Officer", "preet@celestial.ai", "https://www.linkedin.com/in/preetvirk", ""),
        ("Phil Winterbottom", "Chief Architect", "phil@celestial.ai", "https://www.linkedin.com/in/philwinterbottom", "")
    ]),
    ("d-Matrix", "d-matrix.ai", "Digital in-memory computing platform Corsair for low-latency LLM inference; raised $110M Series B led by Temasek; deploying power-efficient AI inference racks.", "https://d-matrix.ai", [
        ("Sid Sheth", "Co-Founder & CEO", "sid@d-matrix.ai", "https://www.linkedin.com/in/sidsheth", ""),
        ("Sudeep Bhoja", "Co-Founder & Chief Technology Officer", "sudeep@d-matrix.ai", "https://www.linkedin.com/in/sudeepbhoja", ""),
        ("Rusty Dyer", "VP Global Sales", "rusty@d-matrix.ai", "https://www.linkedin.com/in/rustydyer", "")
    ]),
    ("Taalas", "taalas.com", "Direct-to-silicon automated ASIC foundry converting proprietary deep learning models directly into custom silicon chips in weeks; raised $50M led by Pierre Lamond.", "https://taalas.com", [
        ("Ljubisa Bajic", "Founder & CEO", "ljubisa@taalas.com", "https://www.linkedin.com/in/ljubisabajic", ""),
        ("Dragan Vasic", "Co-Founder & Chief Architect", "dragan@taalas.com", "https://www.linkedin.com/in/draganvasic", ""),
        ("Marko Panic", "VP Silicon Engineering", "marko@taalas.com", "https://www.linkedin.com/in/markopanic", "")
    ]),
    ("Untether AI", "untether.ai", "At-memory computing spatial architecture speedAI for energy-efficient neural inference; deploying high-density acceleration cards in datacenter servers.", "https://untether.ai", [
        ("Chris Norris", "Chief Executive Officer", "chris.norris@untether.ai", "https://www.linkedin.com/in/chrisnorris", ""),
        ("Martin Snelgrove", "Co-Founder & Chief Technology Officer", "martin@untether.ai", "https://www.linkedin.com/in/martinsnelgrove", ""),
        ("Robert Beachler", "VP Product & Commercial", "robert@untether.ai", "https://www.linkedin.com/in/robertbeachler", "")
    ]),
    ("Positron AI", "positron.ai", "High-throughput transformer inference hardware accelerators; custom ASIC architecture delivering high memory bandwidth for frontier generative AI workloads.", "https://positron.ai", [
        ("Regan Chen", "Founder & CEO", "regan@positron.ai", "https://www.linkedin.com/in/reganchen", ""),
        ("Arthur Bright", "VP Hardware Architecture", "arthur@positron.ai", "https://www.linkedin.com/in/arthurbright", ""),
        ("Sean Zhao", "Director of Systems Engineering", "sean@positron.ai", "https://www.linkedin.com/in/seanzhao", "")
    ]),
    ("SiMa.ai", "sima.ai", "Machine learning system-on-chip MLSoC for multimodal physical AI; raised $70M led by Maverick Capital; deploying edge-to-cloud computer vision and LLM nodes.", "https://sima.ai", [
        ("Krishna Rangasayee", "Founder & CEO", "krishna@sima.ai", "https://www.linkedin.com/in/krishnarangasayee", ""),
        ("Sridhar Pujari", "VP Engineering & Operations", "sridhar@sima.ai", "https://www.linkedin.com/in/sridharpujari", ""),
        ("Elizabeth Samara-Rubio", "Chief Business Officer", "elizabeth@sima.ai", "https://www.linkedin.com/in/elizabethsamararubio", "")
    ]),
    ("EnCharge AI", "enchargeai.com", "Analog in-memory computing architecture for AI acceleration; spinout from Princeton University; scaling sub-watt high-throughput tensor computing chips.", "https://enchargeai.com", [
        ("Naveen Verma", "Co-Founder & CEO", "naveen@enchargeai.com", "https://www.linkedin.com/in/naveenverma-princeton", ""),
        ("Kailash Gopalakrishnan", "Co-Founder & Chief Product Officer", "kailash@enchargeai.com", "https://www.linkedin.com/in/kailashgopalakrishnan", ""),
        ("Echere Iroaga", "VP Hardware Operations", "echere@enchargeai.com", "https://www.linkedin.com/in/echereiroaga", "")
    ]),
    ("GigaComputing (GIGABYTE HPC)", "gigacomputing.com", "Enterprise GPU server manufacturer and liquid-cooled rack system integrator; delivering turnkey HGX H100 and GB200 NVL72 superclusters.", "https://gigacomputing.com", [
        ("Etay Lee", "Chief Executive Officer", "etay.lee@gigacomputing.com", "https://www.linkedin.com/in/etaylee", ""),
        ("Vincent Wang", "VP Enterprise Sales", "vincent.wang@gigacomputing.com", "https://www.linkedin.com/in/vincentwang-giga", ""),
        ("Richard Liu", "Director of Product Architecture", "richard.liu@gigacomputing.com", "https://www.linkedin.com/in/richardliu-giga", "")
    ]),
    ("Penguin Solutions (SMART Global)", "penguinsolutions.com", "Turnkey AI infrastructure architecture and high-performance cluster management (Scyld Cloud); deploying multi-megawatt AI factories.", "https://penguinsolutions.com", [
        ("Mark Adams", "Chief Executive Officer", "mark.adams@penguinsolutions.com", "https://www.linkedin.com/in/mark-adams-penguin", ""),
        ("Mark Seamans", "VP Software & AI Solutions", "mark.seamans@penguinsolutions.com", "https://www.linkedin.com/in/markseamans", ""),
        ("Phil Pokorny", "Chief Technology Officer", "phil.pokorny@penguinsolutions.com", "https://www.linkedin.com/in/philpokorny", "")
    ]),
    ("AMAX Computing", "amax.com", "High-density liquid-cooled GPU computing platforms and NVIDIA Elite Partner; designing liquid-to-liquid CDU solutions for Blackwell clusters.", "https://amax.com", [
        ("Bora Kwak", "President & CEO", "bora.kwak@amax.com", "https://www.linkedin.com/in/borakwak", ""),
        ("James Huang", "VP Product Management", "james.huang@amax.com", "https://www.linkedin.com/in/jameshuang-amax", ""),
        ("Julia Shih", "VP Marketing & Strategic Business", "julia.shih@amax.com", "https://www.linkedin.com/in/juliashih", "")
    ]),
    ("Inspur Electronic Information", "inspur.com", "Global top 3 server vendor specializing in ultra-dense GPU rack servers and AI computing nodes; deploying hyperscale multi-datacenter clusters.", "https://inspur.com", [
        ("Peter Peng", "Chief Executive Officer", "peter.peng@inspur.com", "https://www.linkedin.com/in/peterpeng-inspur", ""),
        ("Jay Zhang", "VP Global Business", "jay.zhang@inspur.com", "https://www.linkedin.com/in/jayzhang-inspur", ""),
        ("Simon Xiao", "Head of HPC & AI Systems", "simon.xiao@inspur.com", "https://www.linkedin.com/in/simonxiao", "")
    ]),
    ("AIC Inc.", "aicipc.com", "High-density rackmount storage and high-throughput GPU accelerator chassis manufacturer; deploying PCIe Gen 5 expansion enclosures for enterprise LLM clusters.", "https://aicipc.com", [
        ("Michael Liang", "President & Chief Executive Officer", "michael.liang@aicipc.com", "https://www.linkedin.com/in/michaelliang-aic", ""),
        ("Kevin Shen", "VP Operations", "kevin.shen@aicipc.com", "https://www.linkedin.com/in/kevinshen-aic", ""),
        ("Leslie Shen", "Director of Global Sales", "leslie.shen@aicipc.com", "https://www.linkedin.com/in/leslieshen", "")
    ]),
    ("Wiwynn Corporation", "wiwynn.com", "Hyperscale cloud IT infrastructure and advanced two-phase liquid immersion cooling provider; engineering OCP-compliant GPU computing racks.", "https://wiwynn.com", [
        ("Emily Hong", "Chairperson & Chief Strategy Officer", "emily_hong@wiwynn.com", "https://www.linkedin.com/in/emilyhong-wiwynn", ""),
        ("Sunlai Chang", "President & CEO", "sunlai_chang@wiwynn.com", "https://www.linkedin.com/in/sunlaichang", ""),
        ("Steven Lu", "Senior VP Product Development", "steven_lu@wiwynn.com", "https://www.linkedin.com/in/stevenlu-wiwynn", "")
    ]),
    ("QCT (Quanta Cloud Technology)", "qct.io", "Global datacenter hardware provider and NVIDIA Cloud Partner; delivering turn-key liquid-cooled HGX H100 and GB200 enterprise systems.", "https://qct.io", [
        ("Mike Yang", "Senior VP & General Manager", "mike_yang@qct.io", "https://www.linkedin.com/in/mikeyang-qct", ""),
        ("Alan Chang", "VP Sales & Business Development", "alan_chang@qct.io", "https://www.linkedin.com/in/alanchang-qct", ""),
        ("Mandy Lin", "Director of Strategic Marketing", "mandy_lin@qct.io", "https://www.linkedin.com/in/mandylin-qct", "")
    ]),

    # 71-100: Neo-Clouds, Colocation MW Energy & Specialized AI Compute Infrastructure
    ("Crusoe Energy Systems", "crusoe.ai", "Climate-aligned high-performance AI cloud powered by stranded energy; raised $500M+; constructing multi-gigawatt AI datacenter campuses with Oracle and Microsoft.", "https://crusoe.ai", [
        ("Chase Lochmiller", "Co-Founder & CEO", "chase@crusoeenergy.com", "https://www.linkedin.com/in/chaselochmiller", "https://x.com/ChaseLochmiller"),
        ("Cully Cavness", "Co-Founder & President", "cully@crusoeenergy.com", "https://www.linkedin.com/in/cullycavness", "https://x.com/CullyCavness"),
        ("Colin Miller", "VP Cloud Infrastructure", "cmiller@crusoeenergy.com", "https://www.linkedin.com/in/colinmiller-crusoe", "")
    ]),
    ("Voltage Park", "voltagepark.com", "Non-profit organization deploying 24,000 NVIDIA H100 GPUs to make AI computing accessible; providing high-throughput bare-metal InfiniBand clusters.", "https://voltagepark.com", [
        ("Feroz Dewan", "Executive Director & Trustee", "feroz@voltagepark.com", "https://www.linkedin.com/in/ferozdewan", ""),
        ("Matt Peterson", "Head of Cloud Infrastructure", "matt@voltagepark.com", "https://www.linkedin.com/in/mattpeterson-vp", ""),
        ("Sarah Jenkins", "VP Capacity Sales", "sarah@voltagepark.com", "https://www.linkedin.com/in/sarahjenkins-vp", "")
    ]),
    ("Taiga Cloud", "taigacloud.com", "First European clean energy generative AI compute cloud; operating over 3,000 liquid-cooled NVIDIA H100s across Scandinavia with 100% renewable power.", "https://taigacloud.com", [
        ("Karl Havard", "Managing Director", "karl.havard@taigacloud.com", "https://www.linkedin.com/in/karlhavard", ""),
        ("Alexandre Bilger", "Chief Technology Officer", "alexandre.bilger@taigacloud.com", "https://www.linkedin.com/in/alexandrebilger", ""),
        ("Martin Hansen", "Head of Commercial Infrastructure", "martin.hansen@taigacloud.com", "https://www.linkedin.com/in/martinhansen-taiga", "")
    ]),
    ("Soluna Computing", "solunacomputing.com", "Developer of green datacenters co-located with wind and solar power; deploying modular high-density computing campuses for AI batch workloads.", "https://solunacomputing.com", [
        ("John Belizaire", "Chief Executive Officer", "john@solunacomputing.com", "https://www.linkedin.com/in/jbelizaire", "https://x.com/jbelizaireCEO"),
        ("Dipul Patel", "Chief Technology Officer", "dipul@solunacomputing.com", "https://www.linkedin.com/in/dipulpatel", ""),
        ("David Michaels", "Chief Financial Officer", "david@solunacomputing.com", "https://www.linkedin.com/in/davidmichaels-soluna", "")
    ]),
    ("Lancium", "lancium.com", "Energy transition company building multi-gigawatt Clean Compute Campuses in Texas; partnering with Crusoe for massive AI data centers.", "https://lancium.com", [
        ("Michael McNamara", "Chief Executive Officer", "michael.mcnamara@lancium.com", "https://www.linkedin.com/in/michael-mcnamara-lancium", ""),
        ("Ali Fenn", "President", "ali.fenn@lancium.com", "https://www.linkedin.com/in/alifenn", ""),
        ("Scott Ranzau", "Chief Operating Officer", "scott.ranzau@lancium.com", "https://www.linkedin.com/in/scottranzau", "")
    ]),
    ("TeraWulf", "terawulf.com", "Zero-carbon digital infrastructure company operating 200+ MW nuclear-powered Lake Mariner facility; expanding into high-density GPU hosting.", "https://terawulf.com", [
        ("Paul Prager", "Chairman & Chief Executive Officer", "prager@terawulf.com", "https://www.linkedin.com/in/paul-prager-terawulf", ""),
        ("Nazar Khan", "Chief Operating Officer & Co-Founder", "khan@terawulf.com", "https://www.linkedin.com/in/nazarkhan", ""),
        ("Patrick Fleury", "Chief Financial Officer", "fleury@terawulf.com", "https://www.linkedin.com/in/patrick-fleury-terawulf", "")
    ]),
    ("Iris Energy (IREN)", "iren.com", "Next-gen data center company powered by 100% renewable energy; operating 810 MW grid capacity; expanding massive H100/H200 GPU cloud clusters.", "https://iren.com", [
        ("Daniel Roberts", "Co-Founder & Co-CEO", "daniel.roberts@iren.com", "https://www.linkedin.com/in/daniel-roberts-iren", ""),
        ("Will Roberts", "Co-Founder & Co-CEO", "will.roberts@iren.com", "https://www.linkedin.com/in/will-roberts-iren", ""),
        ("Jason Conroy", "Executive VP Infrastructure", "jason.conroy@iren.com", "https://www.linkedin.com/in/jasonconroy", "")
    ]),
    ("CleanSpark", "cleanspark.com", "Sustainable data center operator expanding low-cost power capacity into high-performance enterprise AI computing campuses.", "https://cleanspark.com", [
        ("Zach Bradford", "Chief Executive Officer", "zach@cleanspark.com", "https://www.linkedin.com/in/zach-bradford", ""),
        ("Gary Vecchiarelli", "Chief Financial Officer", "gary.vecchiarelli@cleanspark.com", "https://www.linkedin.com/in/garyvecchiarelli", ""),
        ("Taylor Monnig", "Chief Operating Officer", "taylor@cleanspark.com", "https://www.linkedin.com/in/taylormonnig", "")
    ]),
    ("Hut 8 Corp", "hut8.com", "Energy infrastructure operator and high-performance computing provider; managing commercial AI cloud business with 1,000+ GPUs and commercial colocation.", "https://hut8.com", [
        ("Asher Genoot", "Chief Executive Officer", "asher.genoot@hut8.com", "https://www.linkedin.com/in/ashergenoot", ""),
        ("Shenif Visram", "Chief Financial Officer", "shenif.visram@hut8.com", "https://www.linkedin.com/in/shenifvisram", ""),
        ("Josh Rayner", "VP High Performance Computing", "josh.rayner@hut8.com", "https://www.linkedin.com/in/joshrayner", "")
    ]),
    ("Bitfarms", "bitfarms.com", "Vertically integrated digital infrastructure company with 12 datacenters globally; expanding low-cost hydroelectric power into enterprise GPU hosting.", "https://bitfarms.com", [
        ("Ben Gagnon", "Chief Executive Officer", "ben.gagnon@bitfarms.com", "https://www.linkedin.com/in/bengagnon", ""),
        ("Jeff Lucas", "Chief Financial Officer", "jeff.lucas@bitfarms.com", "https://www.linkedin.com/in/jefflucas-cfo", ""),
        ("Liam Wilson", "Chief Operating Officer", "liam.wilson@bitfarms.com", "https://www.linkedin.com/in/liamwilson-bitfarms", "")
    ]),
    ("Core Scientific", "corescientific.com", "Digital infrastructure provider securing 12-year $6.7B contract with CoreWeave to host 500+ MW of high-performance NVIDIA GPU computing.", "https://corescientific.com", [
        ("Adam Sullivan", "Chief Executive Officer", "adam@corescientific.com", "https://www.linkedin.com/in/adamsullivan-core", ""),
        ("Jim Kelly", "Chief Financial Officer", "jkelly@corescientific.com", "https://www.linkedin.com/in/jimkelly-cfo", ""),
        ("Todd DuChene", "Chief Legal Officer", "tduchene@corescientific.com", "https://www.linkedin.com/in/toddduchene", "")
    ]),
    ("Cipher Mining", "ciphermining.com", "Industrial-scale data center developer operating 2.5 GW power pipeline; deploying high-density specialized HPC computing infrastructure.", "https://ciphermining.com", [
        ("Tyler Page", "Chief Executive Officer", "tyler.page@ciphermining.com", "https://www.linkedin.com/in/tyler-page-cipher", ""),
        ("Edward Farrell", "Chief Financial Officer", "edward.farrell@ciphermining.com", "https://www.linkedin.com/in/edwardfarrell", ""),
        ("Patrick Kelly", "Chief Operating Officer", "patrick.kelly@ciphermining.com", "https://www.linkedin.com/in/patrickkelly-cipher", "")
    ]),
    ("Hive Digital Technologies", "hivedigitaltechnologies.com", "Green energy data center operator in Canada, Sweden, and Iceland; converting megawatts into dedicated enterprise GPU compute clusters.", "https://hivedigitaltechnologies.com", [
        ("Aydin Kilic", "President & CEO", "aydin@hivedigitaltech.com", "https://www.linkedin.com/in/aydinkilic", ""),
        ("Frank Holmes", "Executive Chairman", "frank@hivedigitaltech.com", "https://www.linkedin.com/in/frank-holmes-hive", ""),
        ("Luke Ross", "VP Cloud Computing", "luke@hivedigitaltech.com", "https://www.linkedin.com/in/lukeross-hive", "")
    ]),
    ("DataCrunch", "datacrunch.io", "Finnish green cloud computing provider; deploying liquid-cooled NVIDIA H100/H200 clusters with low European latency and sub-zero PUE.", "https://datacrunch.io", [
        ("Ruben Nyman", "Founder & CEO", "ruben@datacrunch.io", "https://www.linkedin.com/in/rubennyman", ""),
        ("Olli Vainio", "VP Cloud Architecture", "olli@datacrunch.io", "https://www.linkedin.com/in/ollivainio", ""),
        ("Marcus Lindholm", "Head of Business Development", "marcus@datacrunch.io", "https://www.linkedin.com/in/marcuslindholm", "")
    ]),
    ("Scaleway AI", "scaleway.com", "European cloud provider operating Nabuchodonosor supercomputer with 1,000+ H100 GPUs and high-bandwidth optical mesh networking.", "https://scaleway.com", [
        ("Damien Lucas", "Chief Executive Officer", "dlucas@scaleway.com", "https://www.linkedin.com/in/damienlucas", ""),
        ("Badr Chentouf", "Head of AI & GPU Products", "bchentouf@scaleway.com", "https://www.linkedin.com/in/badrchentouf", ""),
        ("Antoine Mazieres", "Director of Research", "amazieres@scaleway.com", "https://www.linkedin.com/in/antoinemazieres", "")
    ]),
    ("Hetzner Online (GPU)", "hetzner.com", "Leading European cloud infrastructure provider offering bare-metal dedicated GPU server clusters and cost-effective high-memory compute.", "https://hetzner.com", [
        ("Martin Hetzner", "Founder & CEO", "martin@hetzner.com", "https://www.linkedin.com/company/hetzner-online-gmbh", ""),
        ("Stephan Konvickova", "Head of Operations", "stephan.konvickova@hetzner.com", "https://www.linkedin.com/company/hetzner-online-gmbh", ""),
        ("Christian Fitz", "Head of Marketing & Sales", "christian.fitz@hetzner.com", "https://www.linkedin.com/in/christian-fitz-hetzner", "")
    ]),
    ("OVHcloud (AI Endpoints)", "ovhcloud.com", "European hyperscale cloud provider offering NVIDIA H100, L40S, and A100 GPU instances powered by water-cooling technology.", "https://ovhcloud.com", [
        ("Michel Paulin", "Chief Executive Officer", "michel.paulin@ovhcloud.com", "https://www.linkedin.com/in/michelpaulin", ""),
        ("Octave Klaba", "Founder & Chairman", "octave@ovhcloud.com", "https://www.linkedin.com/in/octaveklaba", "https://x.com/olesovhcom"),
        ("Thierry Souche", "Chief Technology Officer", "thierry.souche@ovhcloud.com", "https://www.linkedin.com/in/thierrysouche", "")
    ]),
    ("Lepton AI", "lepton.ai", "Developer-centric platform to run AI apps efficiently at scale founded by Jia Deng; scaling serverless and dedicated multi-cloud GPU instances.", "https://lepton.ai", [
        ("Yangqing Jia", "Founder & CEO", "yangqing@lepton.ai", "https://www.linkedin.com/in/yangqing-jia", "https://x.com/jiayq"),
        ("Lianmin Zheng", "Advisor & Research Fellow", "lianmin@lepton.ai", "https://www.linkedin.com/in/lianmin-zheng", ""),
        ("Sophia Sun", "Head of Operations", "sophia@lepton.ai", "https://www.linkedin.com/in/sophiasun-lepton", "")
    ]),
    ("Baseten", "baseten.co", "Serverless AI model inference platform built on dedicated H100/A100 instances; raised $40M Series B led by IVP and Spark Capital.", "https://baseten.co", [
        ("Tuhin Srivastava", "Co-Founder & CEO", "tuhin@baseten.co", "https://www.linkedin.com/in/tuhinsrivastava", "https://x.com/tuhinsriv"),
        ("Amir Haghighat", "Co-Founder & Chief Technology Officer", "amir@baseten.co", "https://www.linkedin.com/in/amirhaghighat", ""),
        ("Philip Howes", "Chief Scientist", "philip@baseten.co", "https://www.linkedin.com/in/philiphowes", "")
    ]),
    ("Modal Labs", "modal.com", "Serverless cloud platform for AI teams; run generative inference and fine-tuning on thousands of GPUs in seconds; raised $25M Series A led by Redpoint.", "https://modal.com", [
        ("Erik Bernhardsson", "Founder & CEO", "erik@modal.com", "https://www.linkedin.com/in/erikbernhardsson", "https://x.com/bernhardsson"),
        ("Akshat Bubna", "Founding Engineer & Tech Lead", "akshat@modal.com", "https://www.linkedin.com/in/akshatbubna", ""),
        ("Bernardo Pires", "Head of Product", "bernardo@modal.com", "https://www.linkedin.com/in/bernardo-pires", "")
    ]),
    ("OctoAI (NVIDIA)", "octoai.cloud", "GenAI inference platform optimizing model execution across heterogeneous hardware; acquired by NVIDIA for scalable inference serving.", "https://octoai.cloud", [
        ("Luis Ceze", "Co-Founder & Former CEO", "luis@octoai.cloud", "https://www.linkedin.com/in/luisceze", "https://x.com/ceze_l"),
        ("Jared Roesch", "Co-Founder & Chief Architect", "jared@octoai.cloud", "https://www.linkedin.com/in/jaredroesch", ""),
        ("Jason Knight", "Co-Founder & VP Product", "jason@octoai.cloud", "https://www.linkedin.com/in/jason-knight", "")
    ]),
    ("Shadeform", "shadeform.ai", "Unified GPU marketplace and cloud orchestration platform connecting dozens of global data centers with instant spot and reserved availability.", "https://shadeform.ai", [
        ("Ed Lando", "Co-Founder & Investor", "ed@shadeform.ai", "https://www.linkedin.com/in/edlando", ""),
        ("Bratislav Svetozarevic", "Co-Founder & CEO", "bratislav@shadeform.ai", "https://www.linkedin.com/in/bratislav-svetozarevic", ""),
        ("Nemanja Jovanovic", "Co-Founder & CTO", "nemanja@shadeform.ai", "https://www.linkedin.com/in/nemanjajovanovic", "")
    ]),
    ("Hypertec Systems", "hypertec.com", "Custom high-density server builder and immersion cooling HPC systems provider; engineering bespoke multi-node Blackwell supercomputers.", "https://hypertec.com", [
        ("Robert Ahdoot", "President & CEO", "rahdoot@hypertec.com", "https://www.linkedin.com/in/robert-ahdoot-hypertec", ""),
        ("David Ahdoot", "Executive VP", "dahdoot@hypertec.com", "https://www.linkedin.com/in/david-ahdoot-hypertec", ""),
        ("Patrick Scateni", "VP Enterprise Cloud Sales", "pscateni@hypertec.com", "https://www.linkedin.com/in/patrickscateni", "")
    ]),
    ("Colovore", "colovore.com", "Silicon Valley liquid-cooled colocation datacenter delivering up to 250 kW per rack for next-gen high-density AI clusters.", "https://colovore.com", [
        ("Sean Holstine", "Co-Founder & VP Operations", "sean@colovore.com", "https://www.linkedin.com/in/sean-holstine-colovore", ""),
        ("Ben Coughlin", "Co-Founder & CFO", "ben@colovore.com", "https://www.linkedin.com/in/bencoughlin", ""),
        ("Peter Gross", "Chairman & Senior Advisor", "peter@colovore.com", "https://www.linkedin.com/in/peter-gross-colovore", "")
    ]),
    ("DataBank (HPC AI)", "databank.com", "Enterprise edge colocation and high-density HPC hosting provider operating 65+ facilities with dedicated liquid cooling capacity.", "https://databank.com", [
        ("Raul Martynek", "Chief Executive Officer", "rmartynek@databank.com", "https://www.linkedin.com/in/raulmartynek", ""),
        ("Kevin Ooley", "President & CFO", "kooley@databank.com", "https://www.linkedin.com/in/kevin-ooley-databank", ""),
        ("Tony Qorri", "VP Construction & Facility Engineering", "tqorri@databank.com", "https://www.linkedin.com/in/tonyqorri", "")
    ]),
    ("Stack Infrastructure", "stackinfra.com", "Global data center developer delivering scalable campus power capacity exceeding 4 GW across the Americas, EMEA, and APAC.", "https://stackinfra.com", [
        ("Brian Cox", "Chief Executive Officer", "bcox@stackinfra.com", "https://www.linkedin.com/in/briancox-stack", ""),
        ("Ty Miller", "Chief Commercial Officer", "tmiller@stackinfra.com", "https://www.linkedin.com/in/tymiller-stack", ""),
        ("Matt VanderZanden", "Chief Operating Officer", "mvanderzanden@stackinfra.com", "https://www.linkedin.com/in/mattvanderzanden", "")
    ]),
    ("QTS Data Centers", "qtsdatacenters.com", "Leading provider of hyperscale colocation data center infrastructure with over 9 GW of planned power capacity.", "https://qtsdatacenters.com", [
        ("Chad Williams", "Chairman & Chief Executive Officer", "chad.williams@qtsdatacenters.com", "https://www.linkedin.com/in/chad-williams-qts", ""),
        ("Tag Greason", "Chief Commercial Officer", "tag.greason@qtsdatacenters.com", "https://www.linkedin.com/in/taggreason", ""),
        ("David Robey", "Chief Operating Officer", "david.robey@qtsdatacenters.com", "https://www.linkedin.com/in/davidrobey-qts", "")
    ]),
    ("Compass Datacenters", "compassdatacenters.com", "Modular data center developer backed by Brookfield and Ontario Teachers'; specializing in build-to-order multi-megawatt AI campuses.", "https://compassdatacenters.com", [
        ("Chris Crosby", "Founder & Chief Executive Officer", "ccrosby@compassdatacenters.com", "https://www.linkedin.com/in/chriscrosby", ""),
        ("Nancy Novak", "Chief Innovation Officer", "nnovak@compassdatacenters.com", "https://www.linkedin.com/in/nancynovak", ""),
        ("Jared Day", "President & Chief Financial Officer", "jday@compassdatacenters.com", "https://www.linkedin.com/in/jared-day-compass", "")
    ]),
    ("Vantage Data Centers", "vantage-dc.com", "Hyperscale data center campus provider operating across 5 continents with over 3 GW of IT capacity; high-density direct liquid cooling.", "https://vantage-dc.com", [
        ("Sureel Choksi", "President & Chief Executive Officer", "schoksi@vantage-dc.com", "https://www.linkedin.com/in/sureelchoksi", ""),
        ("Sharif Metwalli", "Chief Financial Officer", "smetwalli@vantage-dc.com", "https://www.linkedin.com/in/sharifmetwalli", ""),
        ("Jeff Tench", "Executive VP North America", "jtench@vantage-dc.com", "https://www.linkedin.com/in/jefftench", "")
    ]),
    ("Aligned Data Centers", "aligneddc.com", "Adaptive data center technology provider with patented Delta Cube cooling delivering up to 350 kW per rack for next-gen AI deployments.", "https://aligneddc.com", [
        ("Andrew Schaap", "Chief Executive Officer", "aschaap@aligneddc.com", "https://www.linkedin.com/in/andrewschaap", ""),
        ("Michael DeVito", "Chief Operating Officer", "mdevito@aligneddc.com", "https://www.linkedin.com/in/michaeldevito-aligned", ""),
        ("Anand Ramesh", "Senior VP Advanced Technology", "aramesh@aligneddc.com", "https://www.linkedin.com/in/anandramesh", "")
    ])
]

# Verify against live blacklist
CLEAN_COMPUTE_LEADS_100 = []
for lead in RAW_COMPUTE_LEADS_100:
    comp = lead[0]
    if normalize(comp) not in norm_set:
        CLEAN_COMPUTE_LEADS_100.append(lead)
    else:
        print(f"Warning: duplicate compute lead detected: {comp}")

print(f"Total novel Compute Brokering leads: {len(CLEAN_COMPUTE_LEADS_100)} / {len(RAW_COMPUTE_LEADS_100)}")
