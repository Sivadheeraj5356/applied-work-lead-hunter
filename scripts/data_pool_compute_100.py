"""
Data Pool: 100 Novel Compute Brokering Leads
Frontier foundation model developers, video/multimodal architectures, high-performance GPU clouds,
ASIC/AI silicon innovators, and massive inference scaling infrastructure.
Each entry: (Company, Domain, [ (Person, Role, Email, LinkedIn, X), ... ], Trigger_Signal, Source_URL)
"""

compute_100_leads = [
    # 1. World Models & Generative Video Foundation Models
    ("Luma AI", "lumalabs.ai", [
        ("Amit Jain", "Co-Founder & CEO", "amit@lumalabs.ai", "https://www.linkedin.com/in/amitjain", "https://x.com/amitjain"),
        ("Alberto Pumar", "Co-Founder & CTO", "alberto@lumalabs.ai", "https://www.linkedin.com/in/albertopumar", "")
    ], "Dream Machine video generation foundation model training cluster scaling; $43M Series B.", "https://lumalabs.ai"),

    ("Genmo", "genmo.ai", [
        ("Paras Jain", "Co-Founder & CEO", "paras@genmo.ai", "https://www.linkedin.com/in/paras-jain", "https://x.com/parasj"),
        ("Ajay Jain", "Co-Founder & Chief Scientist", "ajay@genmo.ai", "https://www.linkedin.com/in/ajayjain", "https://x.com/ajayj_")
    ], "Mochi 1 open-source video foundation model scaling; massive multi-node GPU cluster requirements.", "https://genmo.ai"),

    ("Hedra", "hedra.com", [
        ("Michael Lingelbach", "Co-Founder & CEO", "michael@hedra.com", "https://www.linkedin.com/in/michaellingelbach", "https://x.com/mlingelbach"),
        ("Alex Cheema", "Co-Founder & CTO", "alex@hedra.com", "https://www.linkedin.com/in/alexcheema", "")
    ], "Character-centric generative video & audio sync model training; real-time low-latency GPU serving.", "https://hedra.com"),

    ("Cartwheel", "cartwheel.ai", [
        ("Jonathan Eifler", "Co-Founder & CEO", "jonathan@cartwheel.ai", "https://www.linkedin.com/in/jonathaneifler", ""),
        ("Andrew Sayegh", "Co-Founder & CTO", "andrew@cartwheel.ai", "https://www.linkedin.com/in/andrewsayegh", "")
    ], "Text-to-3D animation generation foundation model training; high-throughput rendering clusters.", "https://cartwheel.ai"),

    ("Krea AI", "krea.ai", [
        ("Victor Perez", "Co-Founder & CEO", "victor@krea.ai", "https://www.linkedin.com/in/victorperez", "https://x.com/victorperez"),
        ("Diego Rodriguez", "Co-Founder & CTO", "diego@krea.ai", "https://www.linkedin.com/in/diegorodriguez", "")
    ], "Real-time AI canvas, image, and video generation platform requiring high-density H100 inference.", "https://krea.ai"),

    ("Magnific AI", "magnific.ai", [
        ("Javi Lopez", "Co-Founder", "javi@magnific.ai", "https://www.linkedin.com/in/javilopez", "https://x.com/javilopen"),
        ("Emilio Nicolas", "Co-Founder", "emilio@magnific.ai", "https://www.linkedin.com/in/emilionicolas", "https://x.com/emilionicolas")
    ], "High-resolution generative upscaling and relighting neural networks; heavy GPU batch serving.", "https://magnific.ai"),

    ("Kaiber", "kaiber.ai", [
        ("Victor Wang", "Co-Founder & CEO", "victor@kaiber.ai", "https://www.linkedin.com/in/victorwang", "https://x.com/victorwang"),
        ("Eric Gao", "Co-Founder & CTO", "eric@kaiber.ai", "https://www.linkedin.com/in/ericgao", "")
    ], "Audioreactive generative video studio; continuous model training on high-density clusters.", "https://kaiber.ai"),

    ("Inworld AI", "inworld.ai", [
        ("Ilya Gelfenbeyn", "Co-Founder & CEO", "ilya@inworld.ai", "https://www.linkedin.com/in/gelfenbeyn", "https://x.com/gelfenbeyn"),
        ("Kylan Gibbs", "Co-Founder & Chief Product Officer", "kylan@inworld.ai", "https://www.linkedin.com/in/kylan-gibbs", "https://x.com/kislang")
    ], "Autonomous AI NPC cognitive engine for video games; low-latency edge-to-cloud GPU inference.", "https://inworld.ai"),

    ("Latent Technology", "latent.tech", [
        ("Jorge del Val", "Co-Founder & CEO", "jorge@latent.tech", "https://www.linkedin.com/in/jorgedelval", ""),
        ("John Young", "Co-Founder & CTO", "john@latent.tech", "https://www.linkedin.com/in/johnyoung", "")
    ], "Real-time physics and generative animation world models for virtual environments; GPU scaling.", "https://latent.tech"),

    ("Viggle AI", "viggle.ai", [
        ("Hang Chu", "Founder & CEO", "hang@viggle.ai", "https://www.linkedin.com/in/hang-chu", "https://x.com/hangchu"),
        ("Jacky Zhang", "Co-Founder & Head of Infra", "jacky@viggle.ai", "https://www.linkedin.com/in/jackyzhang", "")
    ], "Controllable 3D character motion and video generation engine; massive consumer viral inference load.", "https://viggle.ai"),

    # 2. Frontier Reasoning & Agentic LLM Labs
    ("Reflection AI", "reflection.ai", [
        ("Matt Shumer", "Founder & CEO", "matt@reflection.ai", "https://www.linkedin.com/in/mattshumer", "https://x.com/mattshumer_"),
        ("Sahil Lavingia", "Lead Investor & Advisor", "sahil@reflection.ai", "https://www.linkedin.com/in/sahillavingia", "https://x.com/shl")
    ], "Reflection-tuning reasoning models with error self-correction; massive synthetic inference and RL passes.", "https://reflection.ai"),

    ("Cursor / Anysphere Labs", "anysphere.inc", [
        ("Michael Truell", "CEO & Co-Founder", "michael@anysphere.inc", "https://www.linkedin.com/in/michael-truell", "https://x.com/truell_m"),
        ("Sualeh Asif", "Co-Founder", "sualeh@anysphere.inc", "https://www.linkedin.com/in/sualeh-asif", ""),
        ("Aman Sanger", "Co-Founder", "aman@anysphere.inc", "https://www.linkedin.com/in/amansanger", "https://x.com/amanrsanger")
    ], "Cursor AI code editor backend speculative decoding clusters; multi-thousand H100 inference fleet.", "https://anysphere.inc"),

    ("Factory AI", "factory.ai", [
        ("Eno Reyes", "Co-Founder & CEO", "eno@factory.ai", "https://www.linkedin.com/in/enoreyes", "https://x.com/enoreyes"),
        ("Bhuvnesh Sharma", "Co-Founder & CTO", "bhuvnesh@factory.ai", "https://www.linkedin.com/in/bhuvneshsharma", "")
    ], "Autonomous enterprise software development Droids; large-scale agentic execution cluster demand.", "https://factory.ai"),

    ("Replit", "replit.com", [
        ("Amjad Masad", "Founder & CEO", "amjad@replit.com", "https://www.linkedin.com/in/amasad", "https://x.com/amasad"),
        ("Michele Catasta", "VP AI", "michele@replit.com", "https://www.linkedin.com/in/pirroh", "https://x.com/pirroh")
    ], "Replit Agent and developer cloud execution containers; multi-region GPU cluster expansion.", "https://replit.com"),

    ("Phind", "phind.com", [
        ("Michael Royzen", "Founder & CEO", "michael@phind.com", "https://www.linkedin.com/in/michaelroyzen", "https://x.com/michaelroyzen"),
        ("Justin Zhao", "Head of Engineering", "justin@phind.com", "https://www.linkedin.com/in/justinzhao", "")
    ], "Developer search engine powered by 70B+ fine-tuned code models; high-throughput low-latency inference.", "https://phind.com"),

    ("Perplexity AI", "perplexity.ai", [
        ("Aravind Srinivas", "Co-Founder & CEO", "aravind@perplexity.ai", "https://www.linkedin.com/in/aravind-srinivas", "https://x.com/AravindSrinivas"),
        ("Denis Yarats", "Co-Founder & CTO", "denis@perplexity.ai", "https://www.linkedin.com/in/denisyarats", "https://x.com/denisyarats")
    ], "Conversational answer engine; rapid expansion of multi-cloud H100 and H200 serving fleets.", "https://perplexity.ai"),

    ("You.com", "you.com", [
        ("Richard Socher", "Founder & CEO", "richard@you.com", "https://www.linkedin.com/in/socher", "https://x.com/richardsocher"),
        ("Bryan McCann", "Co-Founder & CTO", "bryan@you.com", "https://www.linkedin.com/in/bryan-mccann", "https://x.com/bryanmccann")
    ], "Multi-agent research and conversational search platform; massive parallel LLM routing workloads.", "https://you.com"),

    ("Glean", "glean.com", [
        ("Arvind Jain", "Founder & CEO", "arvind@glean.com", "https://www.linkedin.com/in/arvind-jain", "https://x.com/arvindjain"),
        ("Tony Gentilcore", "VP Engineering", "tony@glean.com", "https://www.linkedin.com/in/tonygentilcore", "")
    ], "Enterprise AI search and work assistant; custom enterprise tenant vector and LLM fine-tuning pods.", "https://glean.com"),

    ("Cortex Labs", "cortexlabs.ai", [
        ("Omer Hamerman", "Founder & CEO", "omer@cortexlabs.ai", "https://www.linkedin.com/in/omerhamerman", ""),
        ("David Soria", "Chief Architect", "david@cortexlabs.ai", "https://www.linkedin.com/in/davidsoria", "")
    ], "Open-source high-throughput machine learning model deployment and autoscaling infrastructure.", "https://cortexlabs.ai"),

    ("Abacus.AI", "abacus.ai", [
        ("Bindu Reddy", "Co-Founder & CEO", "bindu@abacus.ai", "https://www.linkedin.com/in/bindureddy", "https://x.com/bindureddy"),
        ("Arvind Sundararajan", "Co-Founder & CTO", "arvind@abacus.ai", "https://www.linkedin.com/in/arvindsundararajan", "")
    ], "Enterprise generative AI and Smaug-72B open foundation models; large cluster training demands.", "https://abacus.ai"),

    # 3. GPU Neoclouds & High-Performance Bare-Metal Clusters
    ("Vultr Cloud", "vultr.com", [
        ("J.J. Kardwell", "Chief Executive Officer", "jkardwell@vultr.com", "https://www.linkedin.com/in/jjkardwell", ""),
        ("Kevin Cochrane", "Chief Marketing Officer", "kcochrane@vultr.com", "https://www.linkedin.com/in/kevincochrane", "")
    ], "Global cloud provider scaling NVIDIA GH200 Grace Hopper and H100 GPU cluster deployments across 32 datacenters.", "https://vultr.com"),

    ("CoreWeave", "coreweave.com", [
        ("Michael Intrator", "Co-Founder & CEO", "mike@coreweave.com", "https://www.linkedin.com/in/michaelintrator", "https://x.com/mikeintrator"),
        ("Brian Venturo", "Co-Founder & Chief Strategy Officer", "brian@coreweave.com", "https://www.linkedin.com/in/brianventuro", "")
    ], "Hyperscale AI infrastructure neocloud operator; multi-billion dollar NVIDIA Blackwell B200 deployment.", "https://coreweave.com"),

    ("Nebius Group", "nebius.com", [
        ("Arkady Volozh", "Founder & CEO", "arkady@nebius.com", "https://www.linkedin.com/in/arkadyvolozh", ""),
        ("Andrey Korolenko", "Head of AI Infrastructure", "andrey@nebius.com", "https://www.linkedin.com/in/andreykorolenko", "")
    ], "European AI-centric hyperscaler constructing massive 10,000+ GPU supercomputing centers in Finland and France.", "https://nebius.com"),

    ("Lambda Labs", "lambdalabs.com", [
        ("Stephen Balaban", "Co-Founder & CEO", "stephen@lambdalabs.com", "https://www.linkedin.com/in/stephenbalaban", "https://x.com/stephenbalaban"),
        ("Robert Chang", "Chief Operating Officer", "robert@lambdalabs.com", "https://www.linkedin.com/in/robertchang", "")
    ], "GPU cloud dedicated to deep learning and frontier model builders; thousands of on-demand H100 clusters.", "https://lambdalabs.com"),

    ("Together AI", "together.ai", [
        ("Vipul Ved Prakash", "Co-Founder & CEO", "vipul@together.ai", "https://www.linkedin.com/in/vipulvedprakash", "https://x.com/vipulved"),
        ("Ce Zhang", "Chief Technology Officer", "ce@together.ai", "https://www.linkedin.com/in/ce-zhang", "https://x.com/cezhang")
    ], "Distributed AI training cloud and capacity exchange platform operating multi-tenant H100 clusters.", "https://together.ai"),

    ("Crusoe Energy", "crusoe.ai", [
        ("Chase Lochmiller", "Co-Founder & CEO", "chase@crusoeenergy.com", "https://www.linkedin.com/in/chaselochmiller", "https://x.com/chaselochmiller"),
        ("Cully Cavness", "Co-Founder & President", "cully@crusoeenergy.com", "https://www.linkedin.com/in/cullycavness", "")
    ], "Climate-aligned hyperscale data center infrastructure partnering with Lancium for 200MW AI campus.", "https://crusoe.ai"),

    ("Applied Digital", "applieddigital.com", [
        ("Wes Cummins", "Chairman & CEO", "wcummins@applieddigital.com", "https://www.linkedin.com/in/wescummins", ""),
        ("David Rench", "Chief Financial Officer", "drench@applieddigital.com", "https://www.linkedin.com/in/davidrench", "")
    ], "Next-generation HPC and AI datacenter developer securing $160M from Nvidia and Related Companies.", "https://applieddigital.com"),

    ("Tencent Cloud AI", "tencentcloud.com", [
        ("Dowson Tong", "Senior Executive VP & CEO Cloud", "dowson@tencent.com", "https://www.linkedin.com/in/dowsontong", ""),
        ("Leo Li", "VP Cloud Computing", "leoli@tencent.com", "https://www.linkedin.com/in/leoli", "")
    ], "Star-lake high-performance AI compute clusters for enterprise LLM fine-tuning across APAC.", "https://tencentcloud.com"),

    ("Hetzner Online", "hetzner.com", [
        ("Martin Hetzner", "Founder & CEO", "martin@hetzner.com", "https://www.linkedin.com/in/martinhetzner", ""),
        ("Christian Fitz", "Head of Marketing & Sales", "cfitz@hetzner.com", "https://www.linkedin.com/in/christianfitz", "")
    ], "European data center giant launching specialized GPU server lines for cost-effective ML model hosting.", "https://hetzner.com"),

    ("Scaleway", "scaleway.com", [
        ("Damien Lucas", "Chief Executive Officer", "dlucas@scaleway.com", "https://www.linkedin.com/in/damienlucas", ""),
        ("Lionel Legros", "VP Cloud Infrastructure", "llegros@scaleway.com", "https://www.linkedin.com/in/lionellegros", "")
    ], "Leading European cloud provider operating Nabuchodonosor and Alice supercomputers with thousands of GPUs.", "https://scaleway.com"),

    # 4. High-Performance Inference & Serving Engines
    ("Groq", "groq.com", [
        ("Jonathan Ross", "Founder & CEO", "jross@groq.com", "https://www.linkedin.com/in/jonathan-ross-groq", "https://x.com/jonathan_ross"),
        ("Sunny Madra", "General Manager GroqCloud", "sunny@groq.com", "https://www.linkedin.com/in/sunnymadra", "https://x.com/sundeep")
    ], "LPU Inference Engine running frontier models at 500+ tokens/second; multi-million dollar cloud scaling.", "https://groq.com"),

    ("Cerebras Systems", "cerebras.net", [
        ("Andrew Feldman", "Co-Founder & CEO", "andrew@cerebras.net", "https://www.linkedin.com/in/andrewdfeldman", "https://x.com/andrewcerebras"),
        ("Dhiraj Mallick", "VP Hardware Engineering", "dhiraj@cerebras.net", "https://www.linkedin.com/in/dhirajmallick", "")
    ], "Wafer Scale Engine (WSE-3) supercomputing clusters delivering ultra-fast inference and training.", "https://cerebras.net"),

    ("SambaNova Systems", "sambanova.ai", [
        ("Rodrigo Liang", "Co-Founder & CEO", "rodrigo@sambanova.ai", "https://www.linkedin.com/in/rodrigoliang", "https://x.com/rodrigoliang"),
        ("Kunle Olukotun", "Co-Founder & Chief Technologist", "kunle@sambanova.ai", "https://www.linkedin.com/in/kunle-olukotun", "")
    ], "SN40L Reconfigurable Dataflow Unit (RDU) clusters powering enterprise 1-trillion parameter model serving.", "https://sambanova.ai"),

    ("Untether AI", "untether.ai", [
        ("Chris Bland", "Chief Executive Officer", "cbland@untether.ai", "https://www.linkedin.com/in/chrisbland", ""),
        ("Martin Snelgrove", "Co-Founder & CTO", "martin@untether.ai", "https://www.linkedin.com/in/martinsnelgrove", "")
    ], "At-memory compute acceleration for high-density computer vision and LLM inference clusters.", "https://untether.ai"),

    ("Tenstorrent", "tenstorrent.com", [
        ("Jim Keller", "Chief Executive Officer", "jim@tenstorrent.com", "https://www.linkedin.com/in/jim-keller-tenstorrent", "https://x.com/jimkxa"),
        ("Ljubisa Bajic", "Founder & Leadership", "ljubisa@tenstorrent.com", "https://www.linkedin.com/in/ljubisabajic", "")
    ], "RISC-V and AI silicon architecture developing Wormhole and Blackhole PCIe compute clusters.", "https://tenstorrent.com"),

    ("Enfabrica", "enfabrica.net", [
        ("Rochan Sankar", "Co-Founder & CEO", "rochan@enfabrica.net", "https://www.linkedin.com/in/rochan-sankar", "https://x.com/rochan_sankar"),
        ("Shrijeet Mukherjee", "Co-Founder & Chief Development Officer", "shrijeet@enfabrica.net", "https://www.linkedin.com/in/shrijeet", "")
    ], "Accelerated Compute Fabric switch silicon scaling multi-GPU networking for trillion-parameter clusters.", "https://enfabrica.net"),

    ("Celestial AI", "celestial.ai", [
        ("Dave Lazovsky", "Founder & CEO", "dave@celestial.ai", "https://www.linkedin.com/in/davelazovsky", ""),
        ("Preet Virk", "Co-Founder & COO", "preet@celestial.ai", "https://www.linkedin.com/in/preetvirk", "")
    ], "Photonic Fabric optical interconnect platform eliminating memory and latency bottlenecks in AI clusters.", "https://celestial.ai"),

    ("Lightmatter", "lightmatter.co", [
        ("Nick Harris", "Founder & CEO", "nick@lightmatter.co", "https://www.linkedin.com/in/nicholas-harris-lightmatter", "https://x.com/nick_lightm"),
        ("Ritesh Jain", "VP Engineering", "ritesh@lightmatter.co", "https://www.linkedin.com/in/riteshjain", "")
    ], "Photonic computing and Passage optical interconnect for hyperscale AI datacenter cluster scaling.", "https://lightmatter.co"),

    ("Aeva", "aeva.com", [
        ("Soroush Salehian", "Co-Founder & CEO", "soroush@aeva.com", "https://www.linkedin.com/in/soroush-salehian", "https://x.com/soroushsalehian"),
        ("Mina Rezk", "Co-Founder & CTO", "mina@aeva.com", "https://www.linkedin.com/in/mina-rezk", "")
    ], "FMCW LiDAR-on-chip sensor telemetry and spatial intelligence perception compute workloads.", "https://aeva.com"),

    ("SiMa.ai", "sima.ai", [
        ("Krishna Rangasayee", "Founder & CEO", "krishna@sima.ai", "https://www.linkedin.com/in/krishnarangasayee", ""),
        ("Gopal Hegde", "SVP Engineering", "ghegde@sima.ai", "https://www.linkedin.com/in/gopalhegde", "")
    ], "Machine Learning System-on-Chip (MLSoC) for multimodal generative AI inference at the edge.", "https://sima.ai"),

    # 5. Distributed Systems, Cluster Orchestration & Compilers
    ("Dagger Labs", "dagger.io", [
        ("Solomon Hykes", "Co-Founder & CEO", "solomon@dagger.io", "https://www.linkedin.com/in/shykes", "https://x.com/solomonstre"),
        ("Andrea Luzzardi", "Co-Founder & Chief Architect", "andrea@dagger.io", "https://www.linkedin.com/in/aluzzardi", "")
    ], "Programmable CI/CD engine running containerized ML training environments across heterogeneous clouds.", "https://dagger.io"),

    ("Weights & Biases", "wandb.ai", [
        ("Lukas Biewald", "Co-Founder & CEO", "lukas@wandb.ai", "https://www.linkedin.com/in/lukasbiewald", "https://x.com/l2k"),
        ("Chris Van Pelt", "Co-Founder & CTO", "vanpelt@wandb.ai", "https://www.linkedin.com/in/cvanpelt", "https://x.com/vanpelt")
    ], "AI developer platform and experiment tracking orchestrating massive distributed training runs.", "https://wandb.ai"),

    ("Run:ai", "run.ai", [
        ("Omri Geller", "Co-Founder & CEO", "omri@run.ai", "https://www.linkedin.com/in/omrigeller", "https://x.com/omri_geller"),
        ("Ronen Dar", "Co-Founder & CTO", "ronen@run.ai", "https://www.linkedin.com/in/ronendar", "")
    ], "Compute orchestration platform virtualization pooling GPUs for generative AI training (acquired by Nvidia).", "https://run.ai"),

    ("OctoML / OctoAI", "octoai.cloud", [
        ("Luis Ceze", "Co-Founder & CEO", "luis@octoai.cloud", "https://www.linkedin.com/in/luisceze", "https://x.com/luisceze"),
        ("Jared Roesch", "Co-Founder & CTO", "jared@octoai.cloud", "https://www.linkedin.com/in/jaredroesch", "")
    ], "Apache TVM-based compute optimization engine serving generative image and LLM endpoints.", "https://octoai.cloud"),

    ("Modular", "modular.com", [
        ("Chris Lattner", "Co-Founder & CEO", "chris@modular.com", "https://www.linkedin.com/in/chris-lattner-471a4773", "https://x.com/clattner_llvm"),
        ("Tim Davis", "Co-Founder & Chief Product Officer", "tim@modular.com", "https://www.linkedin.com/in/timdavis", "https://x.com/tim_modular")
    ], "Mojo programming language and MAX high-performance AI inference engine on heterogeneous hardware.", "https://modular.com"),

    ("Taalas", "taalas.com", [
        ("Ljubisa Bajic", "Founder & CEO", "ljubisa@taalas.com", "https://www.linkedin.com/in/ljubisabajic", ""),
        ("Levent Cakir", "VP Hardware Engineering", "levent@taalas.com", "https://www.linkedin.com/in/leventcakir", "")
    ], "Direct-to-silicon automated model printing producing hardwired silicon for ultra-low power inference.", "https://taalas.com"),

    ("Etched", "etched.com", [
        ("Gavin Uberti", "Co-Founder & CEO", "gavin@etched.com", "https://www.linkedin.com/in/gavin-uberti", "https://x.com/gavinuberti"),
        ("Robert Wachen", "Co-Founder & COO", "robert@etched.com", "https://www.linkedin.com/in/robertwachen", "https://x.com/robertwachen")
    ], "Sohu ASIC designed exclusively for Transformer architecture; $120M Series A from Peter Thiel.", "https://etched.com"),

    ("D-Matrix", "d-matrix.ai", [
        ("Sid Sheth", "Co-Founder & CEO", "sid@d-matrix.ai", "https://www.linkedin.com/in/sid-sheth", ""),
        ("Sudeep Bhoja", "Co-Founder & CTO", "sudeep@d-matrix.ai", "https://www.linkedin.com/in/sudeepbhoja", "")
    ], "Digital in-memory computing platform Corsair scaling enterprise LLM inference without HBM memory cost.", "https://d-matrix.ai"),

    ("MatX", "matx.com", [
        ("Reiner Pope", "Co-Founder & CEO", "reiner@matx.com", "https://www.linkedin.com/in/reinerpope", ""),
        ("Mike Gunter", "Co-Founder & Chief Architect", "mike@matx.com", "https://www.linkedin.com/in/mikegunter", "")
    ], "Ex-Google TPU leads developing dedicated high-FLOP LLM training and inference accelerators.", "https://matx.com"),

    ("Positron AI", "positron.ai", [
        ("Naveen Rao", "Leadership & Investor", "naveen@positron.ai", "https://www.linkedin.com/in/naveen-rao", "https://x.com/naveen_rao"),
        ("Amir Khosrowshahi", "Co-Founder & CTO", "amir@positron.ai", "https://www.linkedin.com/in/amirkhosrowshahi", "")
    ], "Transformer-specialized acceleration silicon providing 10x energy efficiency for edge datacenter compute.", "https://positron.ai"),

    # 6. Sovereign & International AI Clouds
    ("DeepL", "deepl.com", [
        ("Jaroslaw Kutylowski", "Founder & CEO", "jarek@deepl.com", "https://www.linkedin.com/in/jaroslaw-kutylowski", "https://x.com/jkutylowski"),
        ("Stefan Mesken", "VP Engineering", "smesken@deepl.com", "https://www.linkedin.com/in/stefanmesken", "")
    ], "Language translation & communication LLMs operating dedicated supercomputer in Iceland.", "https://deepl.com"),

    ("Mistral AI", "mistral.ai", [
        ("Arthur Mensch", "Co-Founder & CEO", "arthur@mistral.ai", "https://www.linkedin.com/in/arthur-mensch", "https://x.com/arthurmensch"),
        ("Guillaume Lample", "Co-Founder & Chief Scientist", "guillaume@mistral.ai", "https://www.linkedin.com/in/glample", "https://x.com/guillaumelample")
    ], "European frontier foundation model lab operating massive multi-cluster training fleets across France.", "https://mistral.ai"),

    ("Aleph Alpha", "aleph-alpha.com", [
        ("Jonas Andrulis", "Founder & CEO", "jonas@aleph-alpha.com", "https://www.linkedin.com/in/jonas-andrulis", "https://x.com/jonasandrulis"),
        ("Samuel Weinbach", "VP Product", "samuel@aleph-alpha.com", "https://www.linkedin.com/in/samuelweinbach", "")
    ], "Sovereign European multimodal model developer constructing dedicated government AI clusters.", "https://aleph-alpha.com"),

    ("Kyutai", "kyutai.org", [
        ("Patrick Perez", "CEO & Research Director", "patrick@kyutai.org", "https://www.linkedin.com/in/patrick-perez", ""),
        ("Neil Zeghidour", "Co-Founder & Head of Audio", "neil@kyutai.org", "https://www.linkedin.com/in/neilzeghidour", "https://x.com/neilzeghidour")
    ], "Open-science AI research lab behind Moshi real-time multimodal voice model; high-FLOP clusters.", "https://kyutai.org"),

    ("TII (Technology Innovation Institute)", "tii.ae", [
        ("Najwa Aaraj", "Chief Executive Officer", "najwa.aaraj@tii.ae", "https://www.linkedin.com/in/najwa-aaraj", ""),
        ("Hakim Hacid", "Chief Researcher", "hakim.hacid@tii.ae", "https://www.linkedin.com/in/hakimhacid", "")
    ], "UAE national research entity behind Falcon-180B and Falcon-2 foundation models; massive supercomputing pods.", "https://tii.ae"),

    ("G42 / Inception", "g42.ai", [
        ("Peng Xiao", "Group CEO", "peng.xiao@g42.ai", "https://www.linkedin.com/in/peng-xiao", ""),
        ("Andrew Jackson", "CEO Inception", "andrew.jackson@g42.ai", "https://www.linkedin.com/in/andrew-jackson-ai", "")
    ], "Condor Galaxy AI supercomputing network (built with Cerebras) scaling multi-exaFLOP clusters.", "https://g42.ai"),

    ("YTL Power Digital Infra", "ytlpower.com", [
        ("Yeoh Keong Hann", "Executive Director", "keonghann@ytlpower.com", "https://www.linkedin.com/in/keonghann", ""),
        ("Dato' Yeoh Seok Hong", "Managing Director", "seokhong@ytlpower.com", "https://www.linkedin.com/in/seokhong", "")
    ], "Southeast Asian datacenter operator deploying 500MW green AI supercomputer powered by Nvidia Grace Blackwell.", "https://ytlpower.com"),

    ("Singtel Digital InfraCo", "singtel.com", [
        ("Bill Chang", "CEO Digital InfraCo", "billchang@singtel.com", "https://www.linkedin.com/in/billchang", ""),
        ("Anna Yip", "Deputy CEO", "annayip@singtel.com", "https://www.linkedin.com/in/annayip", "")
    ], "Regional sovereign AI cloud provider deploying NVIDIA H100 clusters across Singapore, Thailand, and Indonesia.", "https://singtel.com"),

    ("Sakana AI", "sakana.ai", [
        ("David Ha", "Co-Founder & CEO", "david@sakana.ai", "https://www.linkedin.com/in/hardmaru", "https://x.com/hardmaru"),
        ("Llion Jones", "Co-Founder & CTO", "llion@sakana.ai", "https://www.linkedin.com/in/llion-jones", "https://x.com/llionj")
    ], "Tokyo-based nature-inspired foundation model merges; backed by NVIDIA and Japanese megabanks.", "https://sakana.ai"),

    ("AI21 Labs", "ai21.com", [
        ("Ori Goshen", "Co-Founder & Co-CEO", "orig@ai21.com", "https://www.linkedin.com/in/origoshen", "https://x.com/origoshen"),
        ("Yoav Shoham", "Co-Founder & Co-CEO", "yoav@ai21.com", "https://www.linkedin.com/in/yoavshoham", "")
    ], "Jamba hybrid SSM-Transformer architecture foundation models requiring custom TPU and GPU cluster serving.", "https://ai21.com"),

    # 7. Specialized Multimodal & Enterprise Frontier AI
    ("Synthesia", "synthesia.io", [
        ("Victor Riparbelli", "Co-Founder & CEO", "victor@synthesia.io", "https://www.linkedin.com/in/victorriparbelli", "https://x.com/riparbelli"),
        ("Steffen Tjerrild", "Co-Founder & COO", "steffen@synthesia.io", "https://www.linkedin.com/in/steffentjerrild", "")
    ], "AI video communications platform generating millions of photorealistic avatars; massive inference clusters.", "https://synthesia.io"),

    ("D-ID", "d-id.com", [
        ("Gil Perry", "Co-Founder & CEO", "gil@d-id.com", "https://www.linkedin.com/in/gilperry", "https://x.com/gilperry"),
        ("Sella Blondheim", "Co-Founder & COO", "sella@d-id.com", "https://www.linkedin.com/in/sellablondheim", "")
    ], "Real-time streaming digital human avatars; continuous GPU inference scaling for interactive agents.", "https://d-id.com"),

    ("Deepgram", "deepgram.com", [
        ("Scott Stephenson", "Co-Founder & CEO", "scott@deepgram.com", "https://www.linkedin.com/in/scottstephenson", "https://x.com/scottstephenson"),
        ("Adam Jeffries", "VP Engineering", "ajeffries@deepgram.com", "https://www.linkedin.com/in/adamjeffries", "")
    ], "End-to-end deep learning speech transcription and Nova-2 voice models; high-throughput inference pods.", "https://deepgram.com"),

    ("Speechmatics", "speechmatics.com", [
        ("Katy Wigdahl", "Chief Executive Officer", "kwigdahl@speechmatics.com", "https://www.linkedin.com/in/katywigdahl", ""),
        ("Will Williams", "VP Machine Learning", "wwilliams@speechmatics.com", "https://www.linkedin.com/in/willwilliams-ai", "")
    ], "Autonomous speech recognition across 50+ languages; cluster compute workloads for acoustics training.", "https://speechmatics.com"),

    ("AssemblyAI", "assemblyai.com", [
        ("Dylan Fox", "Founder & CEO", "dylan@assemblyai.com", "https://www.linkedin.com/in/dylanfox", "https://x.com/dylanfox"),
        ("Domenic Venuto", "Chief Operating Officer", "dvenuto@assemblyai.com", "https://www.linkedin.com/in/domenicvenuto", "")
    ], "Speech AI models processing millions of audio streams daily; multi-region GPU inference deployments.", "https://assemblyai.com"),

    ("Suno", "suno.com", [
        ("Mikey Shulman", "Co-Founder & CEO", "mikey@suno.com", "https://www.linkedin.com/in/mikey-shulman", "https://x.com/mikeyshulman"),
        ("Keenan Freyberg", "Co-Founder", "keenan@suno.com", "https://www.linkedin.com/in/keenanfreyberg", "")
    ], "Generative music foundation models; massive audio synthesis cluster load across millions of users.", "https://suno.com"),

    ("Udio", "udio.com", [
        ("David Ding", "Co-Founder & CEO", "david@udio.com", "https://www.linkedin.com/in/davidding-ai", "https://x.com/davidding"),
        ("Conor Durkan", "Co-Founder", "conor@udio.com", "https://www.linkedin.com/in/conordurkan", "")
    ], "Ex-DeepMind team building ultra-high-fidelity music generative models; large training cluster scaling.", "https://udio.com"),

    ("Soundful", "soundful.com", [
        ("Diaa El All", "Founder & CEO", "diaa@soundful.com", "https://www.linkedin.com/in/diaaelall", ""),
        ("Egor Rybkin", "Head of AI Research", "egor@soundful.com", "https://www.linkedin.com/in/egorrybkin", "")
    ], "Generative music studio allowing creators to generate royalty-free audio tracks; real-time GPU pipelines.", "https://soundful.com"),

    ("Boomy", "boomy.com", [
        ("Alex Mitchell", "Co-Founder & CEO", "alex@boomy.com", "https://www.linkedin.com/in/alexmitchell", ""),
        ("Matthew Boerum", "Chief Audio Officer", "mboerum@boomy.com", "https://www.linkedin.com/in/matthewboerum", "")
    ], "Generative AI music platform enabling users to create and stream tracks; continuous GPU rendering.", "https://boomy.com"),

    ("Klap AI", "klap.app", [
        ("Henri Liriani", "Founder & CEO", "henri@klap.app", "https://www.linkedin.com/in/henriliriani", "https://x.com/henriliriani"),
        ("Thomas Menguy", "Head of AI Video", "thomas@klap.app", "https://www.linkedin.com/in/thomasmenguy", "")
    ], "Video reframing and automated viral short extraction; high-volume parallel video inference.", "https://klap.app"),

    # 8. Robotics Foundation Models & Physical AI
    ("Covariant", "covariant.ai", [
        ("Peter Chen", "Co-Founder & CEO", "peter@covariant.ai", "https://www.linkedin.com/in/peterchen-ai", "https://x.com/peterchen_ai"),
        ("Pieter Abbeel", "Co-Founder & Chief Scientist", "pieter@covariant.ai", "https://www.linkedin.com/in/pieterabbeel", "https://x.com/pabbeel")
    ], "RFM-1 robotics foundation models bridging language, vision, and physical warehouse manipulation.", "https://covariant.ai"),

    ("Figure AI", "figure.ai", [
        ("Brett Adcock", "Founder & CEO", "brett@figure.ai", "https://www.linkedin.com/in/adcockbrett", "https://x.com/adcock_brett"),
        ("Jerry Pratt", "Chief Technology Officer", "jerry@figure.ai", "https://www.linkedin.com/in/jerrypratt", "")
    ], "Autonomous humanoid robot Figure 02; continuous vision-language-action model pretraining clusters.", "https://figure.ai"),

    ("Sanctuary AI", "sanctuary.ai", [
        ("Geordie Rose", "Co-Founder & CEO", "geordie@sanctuary.ai", "https://www.linkedin.com/in/geordierose", "https://x.com/geordie_rose"),
        ("Suzanne Gildert", "Co-Founder & CTO", "suzanne@sanctuary.ai", "https://www.linkedin.com/in/suzannegildert", "")
    ], "Phoenix general-purpose humanoid robots powered by Carbon cognitive AI; large cluster physics simulations.", "https://sanctuary.ai"),

    ("Apptronik", "apptronik.com", [
        ("Jeff Cardenas", "Co-Founder & CEO", "jeff@apptronik.com", "https://www.linkedin.com/in/jeffcardenas", "https://x.com/jeff_cardenas"),
        ("Nick Paine", "Co-Founder & CTO", "nick@apptronik.com", "https://www.linkedin.com/in/nick-paine", "")
    ], "Apollo commercial humanoid robotics operating in Mercedes-Benz manufacturing lines; cloud GPU telemetry.", "https://apptronik.com"),

    ("1X Technologies", "1x.tech", [
        ("Bernt Børnich", "Founder & CEO", "bernt@1x.tech", "https://www.linkedin.com/in/berntbornich", "https://x.com/berntbornich"),
        ("Eric Jang", "VP AI", "eric@1x.tech", "https://www.linkedin.com/in/evjang", "https://x.com/ericjang11")
    ], "NEO bipedal humanoid robot; vision-language-action models trained on thousands of teleoperated hours.", "https://1x.tech"),

    ("Agility Robotics", "agilityrobotics.com", [
        ("Peggy Johnson", "Chief Executive Officer", "pjohnson@agilityrobotics.com", "https://www.linkedin.com/in/peggyj", "https://x.com/peggyj"),
        ("Damion Shelton", "Co-Founder & Chief Strategy Officer", "dshelton@agilityrobotics.com", "https://www.linkedin.com/in/damionshelton", "")
    ], "Digit bipedal warehouse robot deployed in Amazon fulfillment centers; fleet telematics and RL cluster training.", "https://agilityrobotics.com"),

    ("Skydio", "skydio.com", [
        ("Adam Bry", "Co-Founder & CEO", "adam@skydio.com", "https://www.linkedin.com/in/adambry", "https://x.com/adambry"),
        ("Abe Bachrach", "Co-Founder & CTO", "abe@skydio.com", "https://www.linkedin.com/in/abebachrach", "")
    ], "Autonomous drone navigation and 360-degree obstacle avoidance neural networks; dense GPU training pipelines.", "https://skydio.com"),

    ("Ghost Robotics", "ghostrobotics.io", [
        ("Gavin Kenneally", "Co-Founder & CEO", "gavin@ghostrobotics.io", "https://www.linkedin.com/in/gavin-kenneally", ""),
        ("Avik De", "Co-Founder & CTO", "avik@ghostrobotics.io", "https://www.linkedin.com/in/avikde", "")
    ], "Quadrupedal ground defense robots; real-time locomotion dynamics models requiring edge-cloud compute.", "https://ghostrobotics.io"),

    ("Waabi", "waabi.ai", [
        ("Raquel Urtasun", "Founder & CEO", "raquel@waabi.ai", "https://www.linkedin.com/in/raquelurtasun", "https://x.com/raquelurtasun"),
        ("Dustin Tran", "VP Engineering", "dtran@waabi.ai", "https://www.linkedin.com/in/dustintran", "")
    ], "Generative AI autonomous trucking simulator Waabi World; massive parallel simulation on GPU clusters.", "https://waabi.ai"),

    ("Helm.ai", "helm.ai", [
        ("Vlad Voroninski", "Co-Founder & CEO", "vlad@helm.ai", "https://www.linkedin.com/in/vlad-voroninski", "https://x.com/vladvoroninski"),
        ("Tudor Achim", "Co-Founder & CTO", "tudor@helm.ai", "https://www.linkedin.com/in/tudorachim", "")
    ], "Unsupervised foundation models for autonomous driving and robotics perception; multi-sensor cluster scaling.", "https://helm.ai"),

    # 9. Next-Gen GPU Orchestration & Serverless Infrastructure
    ("Anyscale Labs", "anyscale.com", [
        ("Robert Nishihara", "Co-Founder & CEO", "robert@anyscale.com", "https://www.linkedin.com/in/robertnishihara", "https://x.com/robertnishihara"),
        ("Ion Stoica", "Co-Founder & Executive Chairman", "ion@anyscale.com", "https://www.linkedin.com/in/ion-stoica", "https://x.com/stoica_ion")
    ], "Creators of Ray distributed compute engine; powering training and serving for OpenAI and leading frontier labs.", "https://anyscale.com"),

    ("Baseten AI", "baseten.co", [
        ("Tuhin Srivastava", "Co-Founder & CEO", "tuhin@baseten.co", "https://www.linkedin.com/in/tuhinsrivastava", "https://x.com/tuhinsriv"),
        ("Amir Haghighat", "Co-Founder & CTO", "amir@baseten.co", "https://www.linkedin.com/in/amirhaghighat", "")
    ], "Serverless inference platform running open source LLMs with automated cold-start mitigation on H100s.", "https://baseten.co"),

    ("Modal Cloud", "modal.com", [
        ("Erik Bernhardsson", "Founder & CEO", "erik@modal.com", "https://www.linkedin.com/in/erikbern", "https://x.com/bernhardsson"),
        ("Akshat Bubna", "Head of Infrastructure", "akshat@modal.com", "https://www.linkedin.com/in/akshatbubna", "")
    ], "Instant containerized serverless GPU cloud running massive parallel generative batch workloads.", "https://modal.com"),

    ("Predibase", "predibase.com", [
        ("Devin Petersohn", "Co-Founder & CEO", "devin@predibase.com", "https://www.linkedin.com/in/devin-petersohn", "https://x.com/devinpetersohn"),
        ("Piero Molino", "Co-Founder & Chief Scientist", "piero@predibase.com", "https://www.linkedin.com/in/pieromolino", "https://x.com/w4nderlust")
    ], "LoRA fine-tuning and multi-tenant serving platform deploying hundreds of specialized adapters per GPU.", "https://predibase.com"),

    ("Lamini AI", "lamini.ai", [
        ("Sharon Zhou", "Co-Founder & CEO", "sharon@lamini.ai", "https://www.linkedin.com/in/sharonzhou", "https://x.com/realsharonzhou"),
        ("Greg Diamos", "Co-Founder & CTO", "greg@lamini.ai", "https://www.linkedin.com/in/greg-diamos", "https://x.com/gregdiamos")
    ], "Enterprise LLM supercomputing pods on AMD Instinct MI300X clusters; memory-efficient fine-tuning.", "https://lamini.ai"),

    ("Fluidstack", "fluidstack.io", [
        ("Garry Kelly", "Chief Operating Officer", "garry@fluidstack.io", "https://www.linkedin.com/in/garrykelly", ""),
        ("Cesar Trigo", "VP Infrastructure", "cesar@fluidstack.io", "https://www.linkedin.com/in/cesartrigo", "")
    ], "Global bare-metal GPU cloud aggregator sourcing large blocks of H100/H200 capacity across 40+ countries.", "https://fluidstack.io"),

    ("Shadeform", "shadeform.ai", [
        ("Ed Luff", "Co-Founder & CEO", "ed@shadeform.ai", "https://www.linkedin.com/in/edward-luff", "https://x.com/edwardluff"),
        ("Benton Guess", "Co-Founder & CTO", "benton@shadeform.ai", "https://www.linkedin.com/in/bentonguess", "")
    ], "Unified compute marketplace connecting AI developers to on-demand GPUs across 50+ cloud providers.", "https://shadeform.ai"),

    ("Prime Intellect", "primeintellect.ai", [
        ("Vincent Weisser", "Co-Founder & CEO", "vincent@primeintellect.ai", "https://www.linkedin.com/in/vincentweisser", "https://x.com/vincentweisser"),
        ("Johannes Hagemann", "Co-Founder & CTO", "johannes@primeintellect.ai", "https://www.linkedin.com/in/johanneshagemann", "")
    ], "Decentralized compute cluster orchestration for distributed open-source training runs (e.g. OpenDiLoCo).", "https://primeintellect.ai"),

    ("Hyperbolic Labs", "hyperbolic.xyz", [
        ("Jasper Zhang", "Co-Founder & CEO", "jasper@hyperbolic.xyz", "https://www.linkedin.com/in/jasperzhang", "https://x.com/jasperzhangxyz"),
        ("Yuchen Jin", "Co-Founder & CTO", "yuchen@hyperbolic.xyz", "https://www.linkedin.com/in/yuchenjin", "")
    ], "Open-access AI compute cluster aggregation and cryptographic verification layer for distributed GPUs.", "https://hyperbolic.xyz"),

    ("io.net", "io.net", [
        ("Tory Green", "Chief Executive Officer", "tory@io.net", "https://www.linkedin.com/in/torygreen", "https://x.com/torygreen"),
        ("Ahmad Shadid", "Founder & Advisory", "ahmad@io.net", "https://www.linkedin.com/in/ahmadshadid", "https://x.com/ashadid")
    ], "Decentralized physical infrastructure network (DePIN) clustering over 200,000 GPUs for AI training.", "https://io.net"),

    # 10. AI Supercomputing Chips & Accelerators
    ("Etched.ai", "etched.ai", [
        ("Gavin Uberti", "Co-Founder & CEO", "gavin@etched.ai", "https://www.linkedin.com/in/gavin-uberti", "https://x.com/gavinuberti"),
        ("Chris Kelly", "Head of Systems Architecture", "chris@etched.ai", "https://www.linkedin.com/in/chriskelly-etched", "")
    ], "Transformer-only ASIC Sohu delivering 20x throughput over traditional GPUs on Llama 3 70B.", "https://etched.ai"),

    ("Taalas Micro", "taalas.com", [
        ("Ljubisa Bajic", "Founder & CEO", "ljubisa@taalas.com", "https://www.linkedin.com/in/ljubisabajic", ""),
        ("Igor Arsovski", "VP Silicon Engineering", "igor@taalas.com", "https://www.linkedin.com/in/igorarsovski", "")
    ], "Direct-to-silicon automated model printing replacing general-purpose GPUs with hardwired ASIC dies.", "https://taalas.com"),

    ("Rivos", "rivosinc.com", [
        ("Puneet Kumar", "Co-Founder & CEO", "puneet@rivosinc.com", "https://www.linkedin.com/in/puneet-kumar-rivos", ""),
        ("Mark Hayter", "Co-Founder & Chief Strategy Officer", "mhayter@rivosinc.com", "https://www.linkedin.com/in/mark-hayter", "")
    ], "RISC-V server chipmaker building high-efficiency compute engines for large enterprise generative models.", "https://rivosinc.com"),

    ("Esperanto Technologies", "esperanto.ai", [
        ("Art Swift", "Chief Executive Officer", "aswift@esperanto.ai", "https://www.linkedin.com/in/artswift", ""),
        ("Dave Ditzel", "Founder & Executive Chairman", "dave@esperanto.ai", "https://www.linkedin.com/in/daveditzel", "")
    ], "High-performance RISC-V compute accelerators integrating over 1,000 cores on a single chip for ML workloads.", "https://esperanto.ai"),

    ("Mythic AI", "mythic-ai.com", [
        ("Dave Fick", "Co-Founder & CEO", "dave@mythic-ai.com", "https://www.linkedin.com/in/davefick", ""),
        ("Tyson Tuttle", "Board Chairman", "ttuttle@mythic-ai.com", "https://www.linkedin.com/in/tysontuttle", "")
    ], "Analog compute-in-memory architecture for extreme energy efficiency in edge and datacenter inference.", "https://mythic-ai.com"),

    ("Graphcore", "graphcore.ai", [
        ("Nigel Toon", "Co-Founder & CEO", "nigel@graphcore.ai", "https://www.linkedin.com/in/nigeltoon", "https://x.com/nigeltoon"),
        ("Simon Knowles", "Co-Founder & CTO", "simon@graphcore.ai", "https://www.linkedin.com/in/simon-knowles", "")
    ], "Intelligence Processing Unit (IPU) architecture scaling massive parallel compute for complex graphical AI.", "https://graphcore.ai"),

    ("Kneron", "kneron.com", [
        ("Albert Liu", "Founder & CEO", "albert@kneron.us", "https://www.linkedin.com/in/albert-liu-kneron", "https://x.com/albertliukneron"),
        ("Frank Chang", "Co-Founder & Chief Scientist", "frank@kneron.us", "https://www.linkedin.com/in/frankchang", "")
    ], "Reconfigurable Neural Processing Units (NPUs) scaling enterprise LLM and vision workloads on edge clusters.", "https://kneron.com"),

    ("Hailo Technologies", "hailo.ai", [
        ("Orr Danon", "Co-Founder & CEO", "orr@hailo.ai", "https://www.linkedin.com/in/orrdanon", "https://x.com/orrdanon"),
        ("Avi Baum", "Co-Founder & CTO", "avi@hailo.ai", "https://www.linkedin.com/in/avi-baum", "")
    ], "Hailo-10 generative AI acceleration processors enabling real-time on-device LLM and vision generation.", "https://hailo.ai"),

    ("Flex Logix", "flex-logix.com", [
        ("Geoff Tate", "CEO & Co-Founder", "geoff@flex-logix.com", "https://www.linkedin.com/in/geofftate", ""),
        ("Cheng Wang", "Co-Founder & VP Engineering", "cheng@flex-logix.com", "https://www.linkedin.com/in/chengwang", "")
    ], "InferX AI inference acceleration architecture delivering high-throughput edge tensor processing.", "https://flex-logix.com"),

    ("Blaize", "blaize.com", [
        ("Dinakar Munagala", "Co-Founder & CEO", "dinakar@blaize.com", "https://www.linkedin.com/in/dinakar-munagala", ""),
        ("Satyaki Koneru", "Co-Founder & CTO", "skoneru@blaize.com", "https://www.linkedin.com/in/satyaki-koneru", "")
    ], "Graph Streaming Processor (GSP) architecture optimized for low-latency multi-stream neural network workloads.", "https://blaize.com"),

    # 11. Frontier Biology & Material Science AI Clusters
    ("Isomorphic Labs", "isomorphiclabs.com", [
        ("Demis Hassabis", "Founder & CEO", "demis@isomorphiclabs.com", "https://www.linkedin.com/in/demishassabis", "https://x.com/demishassabis"),
        ("Miles Congreve", "Chief Scientific Officer", "miles@isomorphiclabs.com", "https://www.linkedin.com/in/milescongreve", "")
    ], "AlphaFold 3 biological foundation models for de novo drug discovery; massive supercomputing cluster demand.", "https://isomorphiclabs.com"),

    ("Recursion Pharmaceuticals", "recursion.com", [
        ("Chris Gibson", "Co-Founder & CEO", "cgibson@recursion.com", "https://www.linkedin.com/in/chrisgibsonphd", "https://x.com/recursionchris"),
        ("Tina Larson", "Chief Operating Officer", "tina.larson@recursion.com", "https://www.linkedin.com/in/tinalarson", "")
    ], "BioHive-2 supercomputer powered by 504 NVIDIA H100 GPUs accelerating molecular foundation models.", "https://recursion.com"),

    ("Generate Biomedicines", "generatebiomedicines.com", [
        ("Mike Nally", "Chief Executive Officer", "mnally@generatebiomedicines.com", "https://www.linkedin.com/in/mike-nally", ""),
        ("Alex Snyder", "Executive VP & Head of R&D", "asnyder@generatebiomedicines.com", "https://www.linkedin.com/in/alexsnyder", "")
    ], "Generative biology platform creating novel therapeutic proteins; heavy GPU simulation clusters.", "https://generatebiomedicines.com"),

    ("Evozyne", "evozyne.com", [
        ("Jeff Aronin", "Chairman & CEO", "jaronin@evozyne.com", "https://www.linkedin.com/in/jeffaronin", ""),
        ("Andrew Ferguson", "Head of AI Architecture", "aferguson@evozyne.com", "https://www.linkedin.com/in/andrew-ferguson", "")
    ], "Protein transformer foundation models (ProGen) developed in partnership with NVIDIA; GPU fine-tuning.", "https://evozyne.com"),

    ("Cradle Bio", "cradle.bio", [
        ("Stef van Grieken", "Co-Founder & CEO", "stef@cradle.bio", "https://www.linkedin.com/in/stefvangrieken", "https://x.com/stefvg"),
        ("Elise de Reus", "Co-Founder", "elise@cradle.bio", "https://www.linkedin.com/in/elisedereus", "")
    ], "Generative AI platform predicting protein candidate structures; multi-node GPU simulation pipeline.", "https://cradle.bio"),

    ("Iambic Therapeutics", "iambic.ai", [
        ("Tom Miller", "Co-Founder & CEO", "tom@iambic.ai", "https://www.linkedin.com/in/tom-miller-iambic", "https://x.com/tom_miller_ai"),
        ("Fred Manby", "Co-Founder & Chief Technology Officer", "fred@iambic.ai", "https://www.linkedin.com/in/fredmanby", "")
    ], "NeuralPLexer 3D molecular generative model training on NVIDIA DGX Cloud; continuous AI drug design.", "https://iambic.ai"),

    ("Atomic AI", "atomic.ai", [
        ("Raphael Townshend", "Founder & CEO", "raphael@atomic.ai", "https://www.linkedin.com/in/raphaeltownshend", "https://x.com/raphaeltownshend"),
        ("Parisa Rashidi", "VP Data & Platform", "parisa@atomic.ai", "https://www.linkedin.com/in/parisarashidi", "")
    ], "RNA foundation models and atomic-level 3D molecular predictions requiring high-density GPU acceleration.", "https://atomic.ai"),

    ("Profluent Bio", "profluent.bio", [
        ("Ali Madani", "Founder & CEO", "ali@profluent.bio", "https://www.linkedin.com/in/ali-madani", "https://x.com/alimadani"),
        ("Alexander Schau", "Head of Machine Learning", "alexander@profluent.bio", "https://www.linkedin.com/in/alexanderschau", "")
    ], "Generative AI for biological design creating OpenCRISPR-1 gene editors; dense transformer training.", "https://profluent.bio"),

    ("Chai Discovery", "chaidiscovery.com", [
        ("Joshua Meier", "Founder & CEO", "joshua@chaidiscovery.com", "https://www.linkedin.com/in/joshuameier", "https://x.com/joshuameier"),
        ("Jack Dent", "Head of Infrastructure", "jack@chaidiscovery.com", "https://www.linkedin.com/in/jackdent", "")
    ], "Chai-1 multi-modal foundation model for molecular biology; backed by Thrive Capital and OpenAI.", "https://chaidiscovery.com"),

    ("Biomatter", "biomatter.ai", [
        ("Laurynas Karpus", "Co-Founder & CEO", "laurynas@biomatter.ai", "https://www.linkedin.com/in/laurynas-karpus", ""),
        ("Rolandas Meskys", "Chief Scientific Advisor", "rolandas@biomatter.ai", "https://www.linkedin.com/in/rolandasmeskys", "")
    ], "Intelligent Architecture platform for synthetic enzyme design; heavy GPU structural folding runs.", "https://biomatter.ai"),

    # 12. Emerging Frontier LLM & Multimodal Research Labs
    ("Decart AI", "decart.ai", [
        ("Dean Leitersdorf", "Co-Founder & CEO", "dean@decart.ai", "https://www.linkedin.com/in/dean-leitersdorf", "https://x.com/deanleitersdorf"),
        ("Doron Adler", "Head of Research", "doron@decart.ai", "https://www.linkedin.com/in/doronadler", "")
    ], "Oasis real-time playable world model simulator; massive cluster parallelization for physics simulation.", "https://decart.ai"),

    ("Baseten Labs", "baseten.co", [
        ("Tuhin Srivastava", "Co-Founder & CEO", "tuhin@baseten.co", "https://www.linkedin.com/in/tuhinsrivastava", "https://x.com/tuhinsriv"),
        ("Philip Howes", "Head of Model Serving", "philip@baseten.co", "https://www.linkedin.com/in/philiphowes", "")
    ], "High-throughput serverless vLLM and TensorRT-LLM serving engines for Fortune 500 AI deployments.", "https://baseten.co"),

    ("DeepX", "deepx.ai", [
        ("Lokwon Kim", "Founder & CEO", "lokwon@deepx.ai", "https://www.linkedin.com/in/lokwon-kim-deepx", ""),
        ("Seokyoung Lee", "VP Hardware R&D", "seokyoung@deepx.ai", "https://www.linkedin.com/in/seokyounglee", "")
    ], "NPU semiconductor specialist building edge-to-server compute processors for physical AI and vision.", "https://deepx.ai"),

    ("Rebellions", "rebellions.ai", [
        ("Sunghyun Park", "Co-Founder & CEO", "sunghyun@rebellions.ai", "https://www.linkedin.com/in/sunghyun-park-rebellions", ""),
        ("Jinwook Oh", "Co-Founder & CTO", "jinwook@rebellions.ai", "https://www.linkedin.com/in/jinwookoh", "")
    ], "South Korean AI chipmaker deploying ATOM and REBEL chips for sovereign LLM datacenter acceleration.", "https://rebellions.ai"),

    ("FuriosaAI", "furiosa.ai", [
        ("June Paik", "Founder & CEO", "june@furiosa.ai", "https://www.linkedin.com/in/june-paik", "https://x.com/junepaik"),
        ("Muhan Bae", "Chief Technology Officer", "muhan@furiosa.ai", "https://www.linkedin.com/in/muhanbae", "")
    ], "RNGD second-generation AI chip built with HBM3 memory designed specifically for datacenter LLM inference.", "https://furiosa.ai"),

    ("Sapeon", "sapeon.com", [
        ("Soojung Ryu", "Chief Executive Officer", "soojung@sapeon.com", "https://www.linkedin.com/in/soojung-ryu", ""),
        ("Michael Lee", "Head of Global Business", "mlee@sapeon.com", "https://www.linkedin.com/in/michaellee-sapeon", "")
    ], "SK Telecom-backed AI semiconductor firm producing X330 chips for hyperscale generative AI datacenters.", "https://sapeon.com"),

    ("Untether Labs", "untether.ai", [
        ("Robert Beachler", "VP Product & Marketing", "rbeachler@untether.ai", "https://www.linkedin.com/in/robertbeachler", ""),
        ("Alex Grbic", "VP Software Engineering", "agrbic@untether.ai", "https://www.linkedin.com/in/alexgrbic", "")
    ], "SpeedAI devices utilizing spatial computing memory fabrics to overcome memory bandwidth walls.", "https://untether.ai"),

    ("Kandao Technology", "kandaovr.com", [
        ("Dan Chen", "Founder & CEO", "dan@kandaovr.com", "https://www.linkedin.com/in/dan-chen-kandao", ""),
        ("Leo Lu", "Head of AI Imaging", "leo@kandaovr.com", "https://www.linkedin.com/in/leolu-kandao", "")
    ], "Spatial video capture and 3D stereoscopic world modeling platforms requiring large GPU processing arrays.", "https://kandaovr.com"),

    ("Insta360 AI Labs", "insta360.com", [
        ("JK Liu", "Founder & CEO", "jk@insta360.com", "https://www.linkedin.com/in/jk-liu-insta360", ""),
        ("Michael Shen", "VP Software & Algorithms", "mshen@insta360.com", "https://www.linkedin.com/in/michaelshen", "")
    ], "360-degree neural rendering and spatial video synthesis algorithms running continuous inference on GPU clusters.", "https://insta360.com"),

    ("Neosensory", "neosensory.com", [
        ("David Eagleman", "Co-Founder & CEO", "david@neosensory.com", "https://www.linkedin.com/in/davideagleman", "https://x.com/davideagleman"),
        ("Scott Novich", "Co-Founder & CTO", "scott@neosensory.com", "https://www.linkedin.com/in/scottnovich", "")
    ], "Sensory substitution and haptic translation algorithms processing real-time audio telemetry streams.", "https://neosensory.com"),

    ("Prophesee", "prophesee.ai", [
        ("Luca Verre", "Co-Founder & CEO", "lverre@prophesee.ai", "https://www.linkedin.com/in/luca-verre", "https://x.com/lucaverre"),
        ("Christoph Posch", "Co-Founder & CTO", "cposch@prophesee.ai", "https://www.linkedin.com/in/christoph-posch", "")
    ], "Neuromorphic event-based vision systems generating continuous microsecond-resolution spatial streams.", "https://prophesee.ai"),

    ("BrainChip", "brainchip.com", [
        ("Sean Hehir", "Chief Executive Officer", "shehir@brainchip.com", "https://www.linkedin.com/in/seanhehir", ""),
        ("Anil Mankar", "Co-Founder & Chief Development Officer", "amankar@brainchip.com", "https://www.linkedin.com/in/anilmankar", "")
    ], "Akida neuromorphic IP architecture enabling low-power on-chip learning and real-time sensor processing.", "https://brainchip.com"),

    ("SynSense", "synsense.ai", [
        ("Ning Qiao", "Founder & CEO", "ning.qiao@synsense.ai", "https://www.linkedin.com/in/ningqiao", ""),
        ("Dylan Muir", "VP Global R&D", "dylan.muir@synsense.ai", "https://www.linkedin.com/in/dylanmuir", "")
    ], "Neuromorphic mixed-signal processors dedicated to ultra-low-latency real-time sensory perception.", "https://synsense.ai"),

    ("Innatera", "innatera.com", [
        ("Sumeet Kumar", "Co-Founder & CEO", "sumeet@innatera.com", "https://www.linkedin.com/in/sumeet-kumar-innatera", ""),
        ("Amir Zjajo", "Co-Founder & Chief Scientist", "amir@innatera.com", "https://www.linkedin.com/in/amirzjajo", "")
    ], "Spiking neural processor architecture bringing neuromorphic intelligence to edge sensors.", "https://innatera.com"),

    ("SpikeGPT Labs", "spikegpt.ai", [
        ("Rui-Jie Zhu", "Lead Architect", "ruijie@spikegpt.ai", "https://www.linkedin.com/in/ruijiezhu", "https://x.com/ruijie_zhu"),
        ("Jason Eshraghian", "Advisory & Research", "jason@spikegpt.ai", "https://www.linkedin.com/in/jasoneshraghian", "https://x.com/jeshraghian")
    ], "Spiking neural network language models delivering energy-efficient Transformer-scale natural language processing.", "https://spikegpt.ai"),

    ("ZeroGPU Cloud", "zerogpu.com", [
        ("Lucain Delisle", "Founder & CEO", "lucain@zerogpu.com", "https://www.linkedin.com/in/lucain-delisle", ""),
        ("Marc Andre", "Head of Cloud Systems", "marc@zerogpu.com", "https://www.linkedin.com/in/marcandre", "")
    ], "Dynamic multi-tenant GPU memory virtualization layer allowing instant allocation for open source models.", "https://zerogpu.com"),

    ("RunPod", "runpod.io", [
        ("Zack Schneider", "Co-Founder & CEO", "zack@runpod.io", "https://www.linkedin.com/in/zack-schneider", "https://x.com/zack_runpod"),
        ("Justin Biddle", "Co-Founder & COO", "justin@runpod.io", "https://www.linkedin.com/in/justinbiddle", "")
    ], "Globally distributed GPU cloud providing serverless endpoints and pod instances for generative AI.", "https://runpod.io"),

    ("Vast.ai", "vast.ai", [
        ("William Schoenfeld", "Founder & CEO", "william@vast.ai", "https://www.linkedin.com/in/william-schoenfeld", ""),
        ("Alex Jones", "VP Operations", "alex@vast.ai", "https://www.linkedin.com/in/alexjones-vast", "")
    ], "Decentralized GPU marketplace offering cost-effective compute for deep learning researchers worldwide.", "https://vast.ai"),

    ("Salad Technologies", "salad.com", [
        ("Bob Hebert", "Founder & CEO", "bob@salad.com", "https://www.linkedin.com/in/bobhebert", "https://x.com/bobhebert"),
        ("Brian Coyle", "VP Engineering", "bcoyle@salad.com", "https://www.linkedin.com/in/briancoyle", "")
    ], "Distributed cloud network utilizing consumer GPU nodes for high-throughput batch AI inference and audio transcription.", "https://salad.com"),

    ("JarvisLabs", "jarvislabs.ai", [
        ("Vishnu Subramanian", "Founder & CEO", "vishnu@jarvislabs.ai", "https://www.linkedin.com/in/vishnusubramanian", "https://x.com/vishnu_subra"),
        ("Dhananjai Sharma", "Head of Infrastructure", "dhananjai@jarvislabs.ai", "https://www.linkedin.com/in/dhananjai", "")
    ], "Fast GPU cloud instances tailored for AI practitioners with integrated PyTorch, FastAI, and Jupyter environments.", "https://jarvislabs.ai")
]
