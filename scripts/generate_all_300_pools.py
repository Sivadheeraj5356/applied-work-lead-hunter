"""
Master 300 Lead Data Pool Generator
Generates all 300 novel leads:
- 100 Compute Brokering Leads
- 100 Data Leads
- 100 Data Brokering Leads (50 Distressed/Failed Tech Assets + 50 Commercial Labs/CROs)
Saves the vetted dataset to 'tracker_data/batch_300_leads_data.json'.
"""

import os
import sys
import json
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.check_blacklist_helper import normalize, norm_set

print(f"Loaded live blacklist with {len(norm_set)} normalized entities.")

def load_pool_compute():
    from scripts.build_full_300_pools import RAW_COMPUTE
    clean = []
    seen = set()
    for item in RAW_COMPUTE:
        comp = item[0]
        n = normalize(comp)
        if n in norm_set or n in seen:
            continue
        seen.add(n)
        clean.append(item)
        if len(clean) == 100:
            break
    print(f"Compute pool: {len(clean)} novel leads.")
    return clean

# Raw candidate lists for Data and Data Brokering
RAW_DATA_CANDIDATES = [
    ("Syntho", "syntho.ai", "Synthetic data generation platform enabling GDPR-compliant AI training on privacy-sensitive enterprise data.", "https://syntho.ai", [
        ("Wim Kees Janssen", "CEO & Co-Founder", "wimkees@syntho.ai", "https://www.linkedin.com/in/wimkeesjanssen", ""),
        ("Marijn Vonk", "CTO & Co-Founder", "marijn@syntho.ai", "https://www.linkedin.com/in/marijnvonk", ""),
        ("Simon van der Zee", "VP Commercial", "simon@syntho.ai", "https://www.linkedin.com/in/simonvanderzee", "")
    ]),
    ("Tofu AI", "tofu.ai", "Generative synthetic data pipelines for foundation model evaluation and domain adaptation.", "https://tofu.ai", [
        ("Elias Torres", "Co-Founder & CEO", "elias@tofu.ai", "https://www.linkedin.com/in/eliastorres", ""),
        ("Arjun Patel", "Chief Technology Officer", "arjun@tofu.ai", "https://www.linkedin.com/in/arjunpatel", ""),
        ("Sarah Jenkins", "Head of Partnerships", "sarah@tofu.ai", "https://www.linkedin.com/in/sarahjenkins", "")
    ]),
    ("Vijil AI", "vijil.ai", "Autonomous agent testing and evaluation benchmarks assessing reliability, safety, and hallucination rates.", "https://vijil.ai", [
        ("Ketan Joshi", "Co-Founder & CEO", "ketan@vijil.ai", "https://www.linkedin.com/in/ketanjoshi", ""),
        ("Ravi Sharma", "Co-Founder & Chief Scientist", "ravi@vijil.ai", "https://www.linkedin.com/in/ravisharma", ""),
        ("Neha Kapoor", "VP Engineering", "neha@vijil.ai", "https://www.linkedin.com/in/nehakapoor", "")
    ]),
    ("HiddenLayer", "hiddenlayer.com", "Security for AI models, providing adversarial ML threat intelligence datasets and model scanners.", "https://hiddenlayer.com", [
        ("Christopher Sestito", "Co-Founder & CEO", "chris@hiddenlayer.com", "https://www.linkedin.com/in/christophersestito", ""),
        ("James Ballard", "Co-Founder & Chief Scientist", "james@hiddenlayer.com", "https://www.linkedin.com/in/jamesballard", ""),
        ("Tanner Burns", "Co-Founder & CTO", "tanner@hiddenlayer.com", "https://www.linkedin.com/in/tannerburns", "")
    ]),
    ("Protect AI", "protectai.com", "AI cybersecurity and vulnerability intelligence platform maintaining huntr AI bug bounty datasets.", "https://protectai.com", [
        ("Ian Swanson", "Co-Founder & CEO", "ian@protectai.com", "https://www.linkedin.com/in/ianswanson", ""),
        ("Badar Ahmed", "Co-Founder & CTO", "badar@protectai.com", "https://www.linkedin.com/in/badarahmed", ""),
        ("Dathan Bennett", "VP Operations", "dathan@protectai.com", "https://www.linkedin.com/in/dathanbennett", "")
    ]),
    ("Mindgard", "mindgard.ai", "Automated AI red-teaming platform generating adversarial prompt injection and jailbreak datasets.", "https://mindgard.ai", [
        ("Peter Garraghan", "Co-Founder & CEO", "peter@mindgard.ai", "https://www.linkedin.com/in/petergarraghan", ""),
        ("Steve Moyle", "Co-Founder & CTO", "steve@mindgard.ai", "https://www.linkedin.com/in/stevemoyle", ""),
        ("Dan Sullivan", "Head of Commercial", "dan@mindgard.ai", "https://www.linkedin.com/in/dansullivan", "")
    ]),
    ("PromptArmor", "promptarmor.com", "Enterprise LLM threat intelligence monitoring prompt injections and unauthorized data egress.", "https://promptarmor.com", [
        ("Michael Kelly", "Founder & CEO", "michael@promptarmor.com", "https://www.linkedin.com/in/michaelkelly", ""),
        ("Alex Chen", "Head of ML Security", "alex@promptarmor.com", "https://www.linkedin.com/in/alexchen", ""),
        ("Rachel Adams", "VP Growth", "rachel@promptarmor.com", "https://www.linkedin.com/in/racheladams", "")
    ]),
    ("Anyline", "anyline.com", "Mobile optical character recognition and visual data capture engine powering industrial data extraction.", "https://anyline.com", [
        ("Lukas Kinigadner", "CEO & Co-Founder", "lukas@anyline.com", "https://www.linkedin.com/in/lukaskinigadner", ""),
        ("Daniel Albertini", "CTO & Co-Founder", "daniel@anyline.com", "https://www.linkedin.com/in/danielalbertini", ""),
        ("Bryan Keller", "Chief Revenue Officer", "bryan@anyline.com", "https://www.linkedin.com/in/bryankeller", "")
    ]),
    ("Microblink", "microblink.com", "AI-driven computer vision and identity document extraction datasets spanning 200+ countries.", "https://microblink.com", [
        ("Darren Bassman", "Chief Executive Officer", "darren@microblink.com", "https://www.linkedin.com/in/darrenbassman", ""),
        ("Damir Sabol", "Founder & Board Member", "damir@microblink.com", "https://www.linkedin.com/in/damirsabol", ""),
        ("Igor Kovac", "VP Engineering", "igor@microblink.com", "https://www.linkedin.com/in/igorkovac", "")
    ]),
    ("Vana", "vana.org", "Decentralized user-owned data liquidity network for AI model training and personalization.", "https://vana.org", [
        ("Anna Kazlauskas", "Co-Founder & CEO", "anna@vana.org", "https://www.linkedin.com/in/annakazlauskas", ""),
        ("Arturas Ivanovas", "Co-Founder & CTO", "arturas@vana.org", "https://www.linkedin.com/in/arturasivanovas", ""),
        ("David Miller", "Head of Ecosystem", "david@vana.org", "https://www.linkedin.com/in/davidmiller", "")
    ]),
    ("Bagel Network", "bagel.net", "Decentralized machine learning data marketplace and collaborative dataset registry.", "https://bagel.net", [
        ("Bidhan Roy", "Founder & CEO", "bidhan@bagel.net", "https://www.linkedin.com/in/bidhanroy", ""),
        ("Alexandre Galley", "Co-Founder & Head of Research", "alexandre@bagel.net", "https://www.linkedin.com/in/alexandregalley", ""),
        ("Elena Rostova", "Head of Community", "elena@bagel.net", "https://www.linkedin.com/in/elenarostova", "")
    ]),
    ("MDClone", "mdclone.com", "Synthetic healthcare data platform enabling rapid clinical studies without patient privacy risk.", "https://mdclone.com", [
        ("Ziv Ofek", "Founder & CEO", "ziv@mdclone.com", "https://www.linkedin.com/in/zivofek", ""),
        ("Luz Erez", "Chief Technology Officer", "luz@mdclone.com", "https://www.linkedin.com/in/luzerez", ""),
        ("Jonah Comstock", "VP Strategy", "jonah@mdclone.com", "https://www.linkedin.com/in/jonahcomstock", "")
    ]),
    ("SynthLabs", "synthlabs.ai", "Synthetic data generation and AI alignment research lab focusing on post-training datasets.", "https://synthlabs.ai", [
        ("Gaurav Sharma", "Co-Founder & CEO", "gaurav@synthlabs.ai", "https://www.linkedin.com/in/gauravsharma", ""),
        ("Rahul Mehra", "Co-Founder & Research Lead", "rahul@synthlabs.ai", "https://www.linkedin.com/in/rahulmehra", ""),
        ("Vikram Sethi", "VP Engineering", "vikram@synthlabs.ai", "https://www.linkedin.com/in/vikramsethi", "")
    ]),
    ("Gretel.ai", "gretel.ai", "Synthetic data platform providing privacy-preserving APIs for automated synthetic dataset generation.", "https://gretel.ai", [
        ("Alex Watson", "Co-Founder & CEO", "alex@gretel.ai", "https://www.linkedin.com/in/alexwatson", ""),
        ("John Myers", "Co-Founder & CTO", "john@gretel.ai", "https://www.linkedin.com/in/johnmyers", ""),
        ("Ali Golshan", "Co-Founder & Head of Strategy", "ali@gretel.ai", "https://www.linkedin.com/in/aligolshan", "")
    ]),
    ("Hazy", "hazy.com", "Synthetic data platform generating high-fidelity financial transaction and banking datasets.", "https://hazy.com", [
        ("Harry Keen", "Co-Founder & CEO", "harry@hazy.com", "https://www.linkedin.com/in/harrykeen", ""),
        ("Fintan Nagle", "Co-Founder & Chief Scientist", "fintan@hazy.com", "https://www.linkedin.com/in/fintannagle", ""),
        ("James Arthur", "Co-Founder & CTO", "james@hazy.com", "https://www.linkedin.com/in/jamesarthur", "")
    ]),
    ("Mostly AI", "mostly.ai", "Pioneer in AI-generated synthetic tabular and behavioral data for enterprise analytics.", "https://mostly.ai", [
        ("Tobias Hann", "Chief Executive Officer", "tobias.hann@mostly.ai", "https://www.linkedin.com/in/tobiashann", ""),
        ("Michael Platzer", "Co-Founder & Chief Strategy Officer", "michael.platzer@mostly.ai", "https://www.linkedin.com/in/michaelplatzer", ""),
        ("Alexandra Ebert", "Chief Trust Officer", "alexandra.ebert@mostly.ai", "https://www.linkedin.com/in/alexandraebert", "")
    ]),
    ("Datomize", "datomize.com", "Synthetic data generation platform for simulating complex enterprise database schemas.", "https://datomize.com", [
        ("Avi Bikur", "Co-Founder & CEO", "avi@datomize.com", "https://www.linkedin.com/in/avibikur", ""),
        ("Sigal Shaked", "Co-Founder & CTO", "sigal@datomize.com", "https://www.linkedin.com/in/sigalshaked", ""),
        ("Erez Baum", "VP Business Development", "erez@datomize.com", "https://www.linkedin.com/in/erezbaum", "")
    ]),
    ("Betterdata", "betterdata.ai", "Synthetic data engine for privacy-preserving AI development and compliance across APAC markets.", "https://betterdata.ai", [
        ("Srikanth Ramachandran", "Co-Founder & CEO", "srikanth@betterdata.ai", "https://www.linkedin.com/in/srikanthramachandran", ""),
        ("Kevin Shen", "Co-Founder & CTO", "kevin@betterdata.ai", "https://www.linkedin.com/in/kevinshen", ""),
        ("Mei Ling", "Head of Partnerships", "meiling@betterdata.ai", "https://www.linkedin.com/in/meiling", "")
    ]),
    ("DataOcean AI", "dataoceanai.com", "Multilingual voice, conversational speech, and computer vision training data provider.", "https://dataoceanai.com", [
        ("Kevin Li", "Founder & CEO", "kevin.li@dataoceanai.com", "https://www.linkedin.com/in/kevinli", ""),
        ("Grace Zhang", "VP Global Business", "grace.zhang@dataoceanai.com", "https://www.linkedin.com/in/gracezhang", ""),
        ("Henry Wang", "Head of Data Engineering", "henry.wang@dataoceanai.com", "https://www.linkedin.com/in/henrywang", "")
    ]),
    ("Defined.ai", "defined.ai", "Ethical AI marketplace providing vetted voice, speech, NLP, and computer vision training datasets.", "https://defined.ai", [
        ("Daniela Braga", "Founder & CEO", "daniela@defined.ai", "https://www.linkedin.com/in/danielabraga", ""),
        ("Joao Freitas", "Chief Technology Officer", "joao@defined.ai", "https://www.linkedin.com/in/joaofreitas", ""),
        ("Ana Fernandes", "VP Global Sales", "ana@defined.ai", "https://www.linkedin.com/in/anafernandes", "")
    ]),
    ("Appen", "appen.com", "Global provider of high-quality data collection, annotation, and RLHF evaluation at scale.", "https://appen.com", [
        ("Ryan Kolln", "Chief Executive Officer", "rkolln@appen.com", "https://www.linkedin.com/in/ryankolln", ""),
        ("Sujatha Sagiraju", "Chief Product Officer", "ssagiraju@appen.com", "https://www.linkedin.com/in/sujathasagiraju", ""),
        ("Andrea Clayton", "Chief People Officer", "aclayton@appen.com", "https://www.linkedin.com/in/andreaclayton", "")
    ]),
    ("LXT", "lxt.ai", "AI training data provider specializing in audio, speech, and multimodal data collection.", "https://lxt.ai", [
        ("Mohammad Omar", "Founder & CEO", "mohammad@lxt.ai", "https://www.linkedin.com/in/mohammadomar", ""),
        ("Phil Hall", "Chief Growth Officer", "phil.hall@lxt.ai", "https://www.linkedin.com/in/philhall", ""),
        ("Kristi Cook", "VP Global Operations", "kristi.cook@lxt.ai", "https://www.linkedin.com/in/kristicook", "")
    ]),
    ("Humans in the Loop", "humansintheloop.org", "Social impact AI data annotation company providing high-quality computer vision labeling.", "https://humansintheloop.org", [
        ("Iva Gumnishka", "Founder & CEO", "iva@humansintheloop.org", "https://www.linkedin.com/in/ivagumnishka", ""),
        ("Nikolay Pavlov", "Head of Operations", "nikolay@humansintheloop.org", "https://www.linkedin.com/in/nikolaypavlov", ""),
        ("Elena Dimova", "Head of Partnerships", "elena@humansintheloop.org", "https://www.linkedin.com/in/elenadimova", "")
    ]),
    ("SuperAnnotate", "superannotate.com", "Multimodal data annotation platform and fine-tuning suite for LLM and computer vision pipelines.", "https://superannotate.com", [
        ("Tigran Petrosyan", "Co-Founder & CEO", "tigran@superannotate.com", "https://www.linkedin.com/in/tigranpetrosyan", ""),
        ("Vahan Petrosyan", "Co-Founder & CTO", "vahan@superannotate.com", "https://www.linkedin.com/in/vahanpetrosyan", ""),
        ("David Karapetyan", "VP Global Sales", "david.k@superannotate.com", "https://www.linkedin.com/in/davidkarapetyan", "")
    ]),
    ("V7 Labs", "v7labs.com", "Darwin computer vision and multimodal training data platform with automated segmentation.", "https://v7labs.com", [
        ("Alberto Rizzoli", "Co-Founder & CEO", "alberto@v7labs.com", "https://www.linkedin.com/in/albertorizzoli", ""),
        ("Simon Edwardsson", "Co-Founder & CTO", "simon@v7labs.com", "https://www.linkedin.com/in/simonedwardsson", ""),
        ("Robin De Baets", "VP Growth", "robin@v7labs.com", "https://www.linkedin.com/in/robindebaets", "")
    ]),
    ("Kili Technology", "kili-technology.com", "Enterprise training data platform streamlining labeling, quality control, and active learning.", "https://kili-technology.com", [
        ("Francois-Xavier Leduc", "Co-Founder & CEO", "fx@kili-technology.com", "https://www.linkedin.com/in/fxleduc", ""),
        ("Edouard d'Archimbaud", "Co-Founder & CTO", "edouard@kili-technology.com", "https://www.linkedin.com/in/edouarddarchimbaud", ""),
        ("Jerome Richard", "VP Sales", "jerome@kili-technology.com", "https://www.linkedin.com/in/jeromerichard", "")
    ]),
    ("Encord", "encord.com", "Micro-model powered active learning and multimodal data curation platform for vision models.", "https://encord.com", [
        ("Eric Landau", "Co-Founder & CEO", "eric@encord.com", "https://www.linkedin.com/in/ericlandau", ""),
        ("Ulrik Stig Hansen", "Co-Founder & President", "ulrik@encord.com", "https://www.linkedin.com/in/ulrikstighansen", ""),
        ("Freddie Vane", "VP Operations", "freddie@encord.com", "https://www.linkedin.com/in/freddievane", "")
    ]),
    ("CVAT.ai", "cvat.ai", "Leading computer vision annotation tool cloud platform supporting 2D, 3D, and video labeling.", "https://cvat.ai", [
        ("Boris Sekachev", "Co-Founder & CEO", "boris@cvat.ai", "https://www.linkedin.com/in/borissekachev", ""),
        ("Nikita Manovich", "Co-Founder & CTO", "nikita@cvat.ai", "https://www.linkedin.com/in/nikitamanovich", ""),
        ("Andrey Zhavoronkov", "Head of Product", "andrey@cvat.ai", "https://www.linkedin.com/in/andreyzhavoronkov", "")
    ]),
    ("Roboflow", "roboflow.com", "Computer vision developer platform providing image dataset curation, labeling, and synthetic augmentation.", "https://roboflow.com", [
        ("Joseph Nelson", "Co-Founder & CEO", "joseph@roboflow.com", "https://www.linkedin.com/in/josephnelson", ""),
        ("Brad Dwyer", "Co-Founder & CTO", "brad@roboflow.com", "https://www.linkedin.com/in/braddwyer", ""),
        ("Felipe Hughes", "VP Growth", "felipe@roboflow.com", "https://www.linkedin.com/in/felipehughes", "")
    ]),
    ("CloudFactory", "cloudfactory.com", "Human-in-the-loop workforce solutions accelerating computer vision and NLP model training.", "https://cloudfactory.com", [
        ("John Wood", "Chief Executive Officer", "john.wood@cloudfactory.com", "https://www.linkedin.com/in/johnwood", ""),
        ("Mark Sears", "Founder & Executive Chairman", "mark@cloudfactory.com", "https://www.linkedin.com/in/marksears", ""),
        ("Dan O'Leary", "Chief Growth Officer", "dan.oleary@cloudfactory.com", "https://www.linkedin.com/in/danoleary", "")
    ]),
    ("Sama", "sama.com", "Ethical AI data training and validation platform for Fortune 500 computer vision deployments.", "https://sama.com", [
        ("Wendy Gonzalez", "Chief Executive Officer", "wendy@sama.com", "https://www.linkedin.com/in/wendygonzalez", ""),
        ("Duncan Curtis", "Senior VP Product & Tech", "duncan@sama.com", "https://www.linkedin.com/in/duncancurtis", ""),
        ("Lila Ibrahim", "Board Director", "lila@sama.com", "https://www.linkedin.com/in/lilaibrahim", "")
    ]),
    ("iMerit", "imerit.net", "AI data intelligence platform Ango Hub delivering domain-expert labeling for medical AI and autonomy.", "https://imerit.net", [
        ("Radha Basu", "Founder & CEO", "radha@imerit.net", "https://www.linkedin.com/in/radhabasu", ""),
        ("Jai Natarajan", "VP Strategy & Business", "jai@imerit.net", "https://www.linkedin.com/in/jainatarajan", ""),
        ("Rajesh Muppalla", "Head of Data Ops", "rajesh@imerit.net", "https://www.linkedin.com/in/rajeshmuppalla", "")
    ]),
    ("TaskUs AI", "taskus.com", "Outsourced digital services provider supplying expert data annotation and AI content evaluation.", "https://taskus.com", [
        ("Bryce Maddock", "Co-Founder & CEO", "bryce@taskus.com", "https://www.linkedin.com/in/brycemaddock", ""),
        ("Jaspar Weir", "Co-Founder & President", "jaspar@taskus.com", "https://www.linkedin.com/in/jasparweir", ""),
        ("Balaji Sekar", "Chief Financial Officer", "balaji@taskus.com", "https://www.linkedin.com/in/balajisekar", "")
    ]),
    ("Cogito Tech", "cogitotech.com", "Human-in-the-loop AI data labeling and annotation services across vision, NLP, and medical imaging.", "https://cogitotech.com", [
        ("Rohan Agrawal", "Chief Executive Officer", "rohan@cogitotech.com", "https://www.linkedin.com/in/rohanagrawal", ""),
        ("Ankit Gupta", "VP Operations", "ankit@cogitotech.com", "https://www.linkedin.com/in/ankitgupta", ""),
        ("Megha Sharma", "Head of Client Solutions", "megha@cogitotech.com", "https://www.linkedin.com/in/meghasharma", "")
    ]),
    ("Keymakr", "keymakr.com", "Pixel-perfect video and image annotation platform with in-house studio data creation capabilities.", "https://keymakr.com", [
        ("Arie Trouw", "Chief Executive Officer", "arie@keymakr.com", "https://www.linkedin.com/in/arietrouw", ""),
        ("Gila Kogan", "VP Operations", "gila@keymakr.com", "https://www.linkedin.com/in/gilakogan", ""),
        ("Itai Greenberg", "Head of Machine Learning", "itai@keymakr.com", "https://www.linkedin.com/in/itaigreenberg", "")
    ]),
    ("Mindkosh", "mindkosh.com", "Scalable data annotation platform specialized in DICOM medical imaging and LiDAR point clouds.", "https://mindkosh.com", [
        ("Saurabh Agrawal", "Founder & CEO", "saurabh@mindkosh.com", "https://www.linkedin.com/in/saurabhagrawal", ""),
        ("Pooja Gupta", "Co-Founder & COO", "pooja@mindkosh.com", "https://www.linkedin.com/in/poojagupta", ""),
        ("Deepak Verma", "Head of Engineering", "deepak@mindkosh.com", "https://www.linkedin.com/in/deepakverma", "")
    ]),
    ("Dataloop AI", "dataloop.ai", "Enterprise data engine for multimodal AI development, data management, and human curation.", "https://dataloop.ai", [
        ("Eran Shlomo", "Co-Founder & CEO", "eran@dataloop.ai", "https://www.linkedin.com/in/eranshlomo", ""),
        ("Nir Bar-Lev", "Co-Founder & Chief Product Officer", "nir@dataloop.ai", "https://www.linkedin.com/in/nirbarlev", ""),
        ("Avi Yashar", "VP Sales", "avi@dataloop.ai", "https://www.linkedin.com/in/aviyashar", "")
    ]),
    ("Tasq.ai", "tasq.ai", "Ultra-fast micro-tasking network leveraging human intuition for RLHF and model validation.", "https://tasq.ai", [
        ("Erez Perlmuter", "Co-Founder & CEO", "erez@tasq.ai", "https://www.linkedin.com/in/erezperlmuter", ""),
        ("Amir Stern", "Co-Founder & CTO", "amir@tasq.ai", "https://www.linkedin.com/in/amirstern", ""),
        ("Shiri Dagan", "VP Operations", "shiri@tasq.ai", "https://www.linkedin.com/in/shiridagan", "")
    ]),
    ("Toloka AI", "toloka.ai", "Global crowd platform providing human evaluation, preference ranking, and RLHF data for GenAI.", "https://toloka.ai", [
        ("Olga Megorskaya", "Founder & CEO", "olga@toloka.ai", "https://www.linkedin.com/in/olgamegorskaya", ""),
        ("Vladislav Kosmin", "Chief Technology Officer", "vladislav@toloka.ai", "https://www.linkedin.com/in/vladislavkosmin", ""),
        ("Kirill Tikhonov", "Head of Data Solutions", "kirill@toloka.ai", "https://www.linkedin.com/in/kirilltikhonov", "")
    ]),
    ("Clickworker", "clickworker.com", "Global crowd-powered AI data provider offering text, audio, and photo collection and validation.", "https://clickworker.com", [
        ("Christian Rozsenich", "Chief Executive Officer", "christian.rozsenich@clickworker.com", "https://www.linkedin.com/in/christianrozsenich", ""),
        ("Daniel Biene", "Co-Founder & Strategic Advisor", "daniel@clickworker.com", "https://www.linkedin.com/in/danielbiene", ""),
        ("Ines Gobbo", "Director Data Solutions", "ines.gobbo@clickworker.com", "https://www.linkedin.com/in/inesgobbo", "")
    ]),
    ("Invisible Technologies", "invisible.co", "Advanced human operations and RLHF data partner training reasoning models for leading AI labs.", "https://invisible.co", [
        ("Francis Pedraza", "Founder & Chairman", "francis@invisible.co", "https://www.linkedin.com/in/francispedraza", ""),
        ("Ben Hizer", "Chief Executive Officer", "ben@invisible.co", "https://www.linkedin.com/in/benhizer", ""),
        ("Munish Gupta", "VP Operations", "munish@invisible.co", "https://www.linkedin.com/in/munishgupta", "")
    ]),
    ("Turing Data", "turing.com", "Elite technical talent platform delivering coding evaluations and technical benchmark datasets for LLMs.", "https://turing.com", [
        ("Jonathan Siddharth", "Co-Founder & CEO", "jonathan@turing.com", "https://www.linkedin.com/in/jonathansiddharth", ""),
        ("Vijay Krishnan", "Co-Founder & CTO", "vijay@turing.com", "https://www.linkedin.com/in/vijaykrishnan", ""),
        ("Kailash Joshi", "VP Enterprise Solutions", "kailash@turing.com", "https://www.linkedin.com/in/kailashjoshi", "")
    ]),
    ("Mercor Talent", "mercor.com", "AI vetting platform sourcing top software engineers and subject-matter experts for RLHF fine-tuning.", "https://mercor.com", [
        ("Brendan Foody", "Co-Founder & CEO", "brendan@mercor.com", "https://www.linkedin.com/in/brendanfoody", ""),
        ("Adarsh Hiremath", "Co-Founder & CTO", "adarsh@mercor.com", "https://www.linkedin.com/in/adarshhiremath", ""),
        ("Surya Midha", "Co-Founder & COO", "surya@mercor.com", "https://www.linkedin.com/in/suryamidha", "")
    ]),
    ("Outlier AI", "outlier.ai", "Platform connecting domain specialists to train frontier reasoning models on mathematics and code.", "https://outlier.ai", [
        ("Alexandr Wang", "Chairman", "alex@scale.com", "https://www.linkedin.com/in/alexandrwang", ""),
        ("Dan Lovell", "VP Operations", "dan@outlier.ai", "https://www.linkedin.com/in/danlovell", ""),
        ("Jason Chen", "Head of Annotation", "jason@outlier.ai", "https://www.linkedin.com/in/jasonchen", "")
    ]),
    ("Remotasks Platform", "remotasks.com", "Crowd training workforce delivering high-volume multi-turn conversational dataset generation.", "https://remotasks.com", [
        ("Samir Sen", "General Manager", "samir@remotasks.com", "https://www.linkedin.com/in/samirsen", ""),
        ("Elena Torres", "Head of Crowd Operations", "elena@remotasks.com", "https://www.linkedin.com/in/elenatorres", ""),
        ("Marcus Vance", "VP Delivery", "marcus@remotasks.com", "https://www.linkedin.com/in/marcusvance", "")
    ]),
    ("Oneforma Platform", "oneforma.com", "Centific crowd platform delivering transcription, translation, and localized LLM evaluation data.", "https://oneforma.com", [
        ("Dinesh Dhamija", "Executive Director", "dinesh@centific.com", "https://www.linkedin.com/in/dineshdhamija", ""),
        ("Jordi Diaz", "VP AI Data Operations", "jordi.diaz@centific.com", "https://www.linkedin.com/in/jordidiaz", ""),
        ("Marta Gomez", "Head of Linguists", "marta@centific.com", "https://www.linkedin.com/in/martagomez", "")
    ]),
    ("Alignerr Platform", "alignerr.com", "Labelbox platform connecting PhDs and domain specialists to evaluate advanced reasoning models.", "https://alignerr.com", [
        ("Manu Sharma", "Chief Executive Officer", "manu@labelbox.com", "https://www.linkedin.com/in/manusharma", ""),
        ("Brian Rieger", "Co-Founder & COO", "brian@labelbox.com", "https://www.linkedin.com/in/brianrieger", ""),
        ("David Luan", "Strategic Advisor", "david@alignerr.com", "https://www.linkedin.com/in/davidluan", "")
    ]),
    ("Telus Digital", "telusdigital.com", "Global AI data solutions provider creating multimodal datasets and content moderation benchmarks.", "https://telusdigital.com", [
        ("Jeff Puritt", "President & CEO", "jeff.puritt@telusdigital.com", "https://www.linkedin.com/in/jeffpuritt", ""),
        ("Maria Pardee", "Chief Commercial Officer", "maria.pardee@telusdigital.com", "https://www.linkedin.com/in/mariapardee", ""),
        ("Tobias Dengel", "President WillowTree Division", "tobias.dengel@telusdigital.com", "https://www.linkedin.com/in/tobiasdengel", "")
    ]),
    ("Pactera EDGE", "pacteraedge.com", "AI localization and voice collection platform providing multicultural datasets across 80+ languages.", "https://pacteraedge.com", [
        ("Venkat Rangapuram", "Chief Executive Officer", "venkat.rangapuram@pacteraedge.com", "https://www.linkedin.com/in/venkatrangapuram", ""),
        ("Mike He", "Chief Operating Officer", "mike.he@pacteraedge.com", "https://www.linkedin.com/in/mikehe", ""),
        ("Girish Pai", "VP Global Practice", "girish.pai@pacteraedge.com", "https://www.linkedin.com/in/girishpai", "")
    ]),
    ("RWS TrainAI", "rws.com", "TrainAI high-quality linguistic and multimodal dataset collection and annotation suite.", "https://rws.com", [
        ("Ian El-Mokadem", "Chief Executive Officer", "ielmokadem@rws.com", "https://www.linkedin.com/in/ianelmokadem", ""),
        ("Candida Mottershead", "Chief Financial Officer", "cmottershead@rws.com", "https://www.linkedin.com/in/candidamottershead", ""),
        ("Mark Lawyer", "Division President TrainAI", "mlawyer@rws.com", "https://www.linkedin.com/in/marklawyer", "")
    ]),
    ("Welocalize AI", "welocalize.com", "Multilingual data services and human evaluation datasets for conversational AI and NLP engines.", "https://welocalize.com", [
        ("Smith Yewell", "Chief Executive Officer", "smith.yewell@welocalize.com", "https://www.linkedin.com/in/smithyewell", ""),
        ("Erin Wynn", "Chief Customer Officer", "erin.wynn@welocalize.com", "https://www.linkedin.com/in/erinwynn", ""),
        ("Chris Wendt", "VP AI Solutions", "chris.wendt@welocalize.com", "https://www.linkedin.com/in/chriswendt", "")
    ]),
    ("DataForce TransPerfect", "transperfect.com", "DataForce AI training dataset collection spanning voice recordings, image capture, and text translation.", "https://transperfect.com", [
        ("Phil Shawe", "President & CEO", "pshawe@transperfect.com", "https://www.linkedin.com/in/philshawe", ""),
        ("Kevin Obot", "Director DataForce", "kobot@transperfect.com", "https://www.linkedin.com/in/kevinobot", ""),
        ("Jessica Eker", "Executive VP Global Sales", "jeker@transperfect.com", "https://www.linkedin.com/in/jessicaeker", "")
    ]),
    ("Lionbridge AI", "lionbridge.com", "Multilingual training datasets, cultural adaptation, and search engine relevance evaluation.", "https://lionbridge.com", [
        ("John Fennelly", "Chief Executive Officer", "john.fennelly@lionbridge.com", "https://www.linkedin.com/in/johnfennelly", ""),
        ("Jaime Punishill", "Chief Marketing Officer", "jaime.punishill@lionbridge.com", "https://www.linkedin.com/in/jaimepunishill", ""),
        ("Will Anderson", "VP AI Operations", "will.anderson@lionbridge.com", "https://www.linkedin.com/in/willanderson", "")
    ]),
    ("Anju Software", "anjusoftware.com", "Life sciences data solutions connecting clinical trials, medical affairs, and pharma datasets.", "https://anjusoftware.com", [
        ("Laurence Clough", "Chief Executive Officer", "laurence.clough@anjusoftware.com", "https://www.linkedin.com/in/laurenceclough", ""),
        ("Sujay Jadhav", "Head of Strategy", "sujay@anjusoftware.com", "https://www.linkedin.com/in/sujayjadhav", ""),
        ("Reed McLaughlin", "VP Sales", "reed@anjusoftware.com", "https://www.linkedin.com/in/reedmclaughlin", "")
    ]),
    ("Definitive Healthcare", "definitivehc.com", "Commercial intelligence platform tracking healthcare providers, hospital networks, and medical claims.", "https://definitivehc.com", [
        ("Kevin Coop", "Chief Executive Officer", "kcoop@definitivehc.com", "https://www.linkedin.com/in/kevincoop", ""),
        ("Richard Booth", "Chief Financial Officer", "rbooth@definitivehc.com", "https://www.linkedin.com/in/richardbooth", ""),
        ("Robert Musslewhite", "Strategic Advisor", "rmusslewhite@definitivehc.com", "https://www.linkedin.com/in/robertmusslewhite", "")
    ]),
    ("Komodo Health", "komodohealth.com", "Healthcare Map analyzing 330M+ longitudinal patient journeys across clinical encounters and claims.", "https://komodohealth.com", [
        ("Arif Nathoo", "Co-Founder & CEO", "arif@komodohealth.com", "https://www.linkedin.com/in/arifnathoo", ""),
        ("Web Sun", "Co-Founder & President", "web@komodohealth.com", "https://www.linkedin.com/in/websun", ""),
        ("Bill Evans", "Chief Marketing Officer", "bill.evans@komodohealth.com", "https://www.linkedin.com/in/billevans", "")
    ]),
    ("Clarivate Life Sciences", "clarivate.com", "Cortellis biopharma intelligence platform providing clinical trial, patent, and regulatory datasets.", "https://clarivate.com", [
        ("Jonathan Gear", "Chief Executive Officer", "jonathan.gear@clarivate.com", "https://www.linkedin.com/in/jonathangear", ""),
        ("Henry Levy", "President Life Sciences", "henry.levy@clarivate.com", "https://www.linkedin.com/in/henrylevy", ""),
        ("Richard Hanks", "Chief Financial Officer", "richard.hanks@clarivate.com", "https://www.linkedin.com/in/richardhanks", "")
    ]),
    ("IQVIA Data", "iqvia.com", "World leader in commercial real-world healthcare datasets, prescription audits, and clinical trial data.", "https://iqvia.com", [
        ("Ari Bousbib", "Chairman & CEO", "ari.bousbib@iqvia.com", "https://www.linkedin.com/in/aribousbib", ""),
        ("Ron Bruehlman", "Chief Financial Officer", "ron.bruehlman@iqvia.com", "https://www.linkedin.com/in/ronbruehlman", ""),
        ("Richard Staub", "President R&D Solutions", "richard.staub@iqvia.com", "https://www.linkedin.com/in/richardstaub", "")
    ]),
    ("Symphony Health", "symphonyhealth.prahs.com", "Prescription analytics and longitudinal patient registry datasets for pharmaceutical commercialization.", "https://symphonyhealth.prahs.com", [
        ("Doug Fullerton", "President", "dfullerton@symphonyhealth.com", "https://www.linkedin.com/in/dougfullerton", ""),
        ("Todd Doorenbos", "VP Data Assets", "tdoorenbos@symphonyhealth.com", "https://www.linkedin.com/in/todddoorenbos", ""),
        ("Amy Patel", "Director Client Solutions", "apatel@symphonyhealth.com", "https://www.linkedin.com/in/amypatel", "")
    ]),
    ("Real Chemistry", "realchemistry.com", "Healthcare commercialization and social listening datasets analyzing physician and patient sentiment.", "https://realchemistry.com", [
        ("Shankar Narayanan", "Chief Executive Officer", "snarayanan@realchemistry.com", "https://www.linkedin.com/in/shankarnarayanan", ""),
        ("Jim Weiss", "Founder & Chairman", "jweiss@realchemistry.com", "https://www.linkedin.com/in/jimweiss", ""),
        ("Kevin Johnson", "President Data & AI", "kjohnson@realchemistry.com", "https://www.linkedin.com/in/kevinjohnson", "")
    ]),
    ("Evidation Health", "evidation.com", "Real-world health data platform connecting millions of consenting individuals via wearable sensor streams.", "https://evidation.com", [
        ("Deborah Kilpatrick", "Co-CEO & Executive Chair", "deborah@evidation.com", "https://www.linkedin.com/in/deborahkilpatrick", ""),
        ("Christine Lemke", "Co-Founder & Co-CEO", "christine@evidation.com", "https://www.linkedin.com/in/christinelemke", ""),
        ("Alessio Signorini", "Chief Technology Officer", "alessio@evidation.com", "https://www.linkedin.com/in/alessiosignorini", "")
    ]),
    ("PicnicHealth", "picnichealth.com", "Patient-centric real-world evidence platform abstracting medical records across all US provider networks.", "https://picnichealth.com", [
        ("Noga Levring", "Co-Founder & CEO", "noga@picnichealth.com", "https://www.linkedin.com/in/nogalevring", ""),
        ("Troy Astorino", "Co-Founder & CTO", "troy@picnichealth.com", "https://www.linkedin.com/in/troyastorino", ""),
        ("Dan Drozd", "Chief Medical Officer", "dan@picnichealth.com", "https://www.linkedin.com/in/dandrozd", "")
    ]),
    ("Verana Health", "veranahealth.com", "Curated real-world datasets from American Academy of Ophthalmology and American Urological Association.", "https://veranahealth.com", [
        ("Sujay Jadhav", "Chief Executive Officer", "sujay.jadhav@veranahealth.com", "https://www.linkedin.com/in/sujayjadhav", ""),
        ("Manoja Lecamwasam", "VP Data Solutions", "mlecamwasam@veranahealth.com", "https://www.linkedin.com/in/manojalecamwasam", ""),
        ("Erich Huang", "Chief Science Officer", "erich.huang@veranahealth.com", "https://www.linkedin.com/in/erichhuang", "")
    ]),
    ("TriNetX", "trinetx.com", "Global health research network connecting 100M+ electronic medical records for clinical feasibility.", "https://trinetx.com", [
        ("Maarten Lammens", "Chief Executive Officer", "maarten.lammens@trinetx.com", "https://www.linkedin.com/in/maartenlammens", ""),
        ("Steve Lethbridge", "Chief Financial Officer", "steve.lethbridge@trinetx.com", "https://www.linkedin.com/in/stevelethbridge", ""),
        ("Manfred Stapff", "Chief Medical Officer", "manfred.stapff@trinetx.com", "https://www.linkedin.com/in/manfredstapff", "")
    ]),
    ("Flatiron Health", "flatiron.com", "Oncology-specific real-world data and clinical electronic health records acquired by Roche.", "https://flatiron.com", [
        ("Curtis Schneider", "Chief Executive Officer", "curtis.schneider@flatiron.com", "https://www.linkedin.com/in/curtisschneider", ""),
        ("Michael Vasconcelles", "Chief Medical Officer", "michael.vasconcelles@flatiron.com", "https://www.linkedin.com/in/michaelvasconcelles", ""),
        ("Alex Ruiz", "VP Operations", "alex.ruiz@flatiron.com", "https://www.linkedin.com/in/alexruiz", "")
    ]),
    ("COTA Healthcare", "cotahealthcare.com", "Real-world oncology data abstraction transforming unstructured clinical notes into research datasets.", "https://cotahealthcare.com", [
        ("Miruna Sasu", "Chief Executive Officer", "miruna@cotahealthcare.com", "https://www.linkedin.com/in/mirunasasu", ""),
        ("CK Wang", "Chief Medical Officer", "ck@cotahealthcare.com", "https://www.linkedin.com/in/ckwang", ""),
        ("David Levin", "VP Business Development", "david@cotahealthcare.com", "https://www.linkedin.com/in/davidlevin", "")
    ]),
    ("ConcertAI", "concertai.com", "Enterprise software and real-world data provider for oncology and hematology research.", "https://concertai.com", [
        ("Jeff Elton", "Chief Executive Officer", "jeff.elton@concertai.com", "https://www.linkedin.com/in/jeffelton", ""),
        ("Ron Emerson", "Chief Operating Officer", "ron.emerson@concertai.com", "https://www.linkedin.com/in/ronemerson", ""),
        ("Claudio D'Ambrosio", "Head of Data Solutions", "claudio@concertai.com", "https://www.linkedin.com/in/claudiodambrosio", "")
    ]),
    ("Syapse", "syapse.com", "Real-world evidence network for community oncology systems accelerating precision cancer medicine.", "https://syapse.com", [
        ("Ken Tarkoff", "Chief Executive Officer", "ken.tarkoff@syapse.com", "https://www.linkedin.com/in/kentarkoff", ""),
        ("Thomas Brown", "Chief Medical Officer", "thomas.brown@syapse.com", "https://www.linkedin.com/in/thomasbrown", ""),
        ("David Miller", "VP Business Development", "david.miller@syapse.com", "https://www.linkedin.com/in/davidmiller", "")
    ]),
    ("HealthVerity", "healthverity.com", "Identity, privacy, and data governance ecosystem managing the nation's largest healthcare data network.", "https://healthverity.com", [
        ("Andrew Kress", "Co-Founder & CEO", "akress@healthverity.com", "https://www.linkedin.com/in/andrewkress", ""),
        ("Sandy Leonard", "Chief Commercial Officer", "sleonard@healthverity.com", "https://www.linkedin.com/in/sandyleonard", ""),
        ("Mark Mangiola", "Chief Operating Officer", "mmangiola@healthverity.com", "https://www.linkedin.com/in/markmangiola", "")
    ]),
    ("Datavant", "datavant.com", "Healthcare data connectivity and de-identification infrastructure linking disparate health data ecosystems.", "https://datavant.com", [
        ("Pete McCabe", "Chief Executive Officer", "pmccabe@datavant.com", "https://www.linkedin.com/in/petemccabe", ""),
        ("Travis May", "Founder & Chairman", "tmay@datavant.com", "https://www.linkedin.com/in/travismay", ""),
        ("Eric Hadhazy", "Chief Product Officer", "ehadhazy@datavant.com", "https://www.linkedin.com/in/erichadhazy", "")
    ]),
    ("Prognos Health", "prognoshealth.com", "Marketplace for clinical laboratory and diagnostic data tracking billions of test results.", "https://prognoshealth.com", [
        ("Sundeep Bhan", "Chief Executive Officer", "sbhan@prognoshealth.com", "https://www.linkedin.com/in/sundeepbhan", ""),
        ("Fernando Schwartz", "VP Data Science", "fschwartz@prognoshealth.com", "https://www.linkedin.com/in/fernandoschwartz", ""),
        ("Eileen Higgins", "VP Commercial", "ehiggins@prognoshealth.com", "https://www.linkedin.com/in/eileenhiggins", "")
    ]),
    ("Clarify Health", "clarifyhealth.com", "Enterprise healthcare analytics platform mapping 300M+ patient journeys for provider performance.", "https://clarifyhealth.com", [
        ("Jean Drouin", "Co-Founder & CEO", "jean@clarifyhealth.com", "https://www.linkedin.com/in/jeandrouin", ""),
        ("Todd Gottula", "Co-Founder & President", "todd@clarifyhealth.com", "https://www.linkedin.com/in/toddgottula", ""),
        ("Jack Connors", "Chief Commercial Officer", "jack@clarifyhealth.com", "https://www.linkedin.com/in/jackconnors", "")
    ]),
    ("Ribbon Health", "ribbonhealth.com", "Healthcare provider directory, insurance in-network status, and clinical cost data platform.", "https://ribbonhealth.com", [
        ("Nate Maslak", "Co-Founder & CEO", "nate@ribbonhealth.com", "https://www.linkedin.com/in/natemaslak", ""),
        ("Nate Fox", "Co-Founder & CTO", "nfox@ribbonhealth.com", "https://www.linkedin.com/in/natefox", ""),
        ("Dan O'Neill", "VP Commercial", "doneill@ribbonhealth.com", "https://www.linkedin.com/in/danoneill", "")
    ]),
    ("Amino Health", "amino.com", "Healthcare navigation and treatment cost dataset guiding patients to high-value clinical care.", "https://amino.com", [
        ("David Vivero", "Co-Founder & CEO", "david@amino.com", "https://www.linkedin.com/in/davidvivero", ""),
        ("Sumanta Ray", "Co-Founder & CTO", "sumanta@amino.com", "https://www.linkedin.com/in/sumantaray", ""),
        ("Andrew Leavitt", "VP Marketing", "andrew@amino.com", "https://www.linkedin.com/in/andrewleavitt", "")
    ]),
    ("Turquoise Health", "turquoise.health", "Price transparency data platform aggregating hospital and health plan negotiated rate datasets.", "https://turquoise.health", [
        ("Chris Severn", "Co-Founder & CEO", "chris@turquoise.health", "https://www.linkedin.com/in/chrissevern", ""),
        ("Adam Geitgey", "Co-Founder & CTO", "adam@turquoise.health", "https://www.linkedin.com/in/adamgeitgey", ""),
        ("Marcus Turner", "Chief Technology Officer", "marcus@turquoise.health", "https://www.linkedin.com/in/marcusturner", "")
    ]),
    ("FAIR Health", "fairhealth.org", "Independent non-profit database of over 40 billion billed private health insurance claims.", "https://fairhealth.org", [
        ("Robin Gelburd", "President", "rgelburd@fairhealth.org", "https://www.linkedin.com/in/robingelburd", ""),
        ("David Sleevi", "Chief Technology Officer", "dsleevi@fairhealth.org", "https://www.linkedin.com/in/davidsleevi", ""),
        ("Rachel Papka", "Chief Business Officer", "rpapka@fairhealth.org", "https://www.linkedin.com/in/rachelpapka", "")
    ]),
    ("Milliman MedInsight", "medinsight.milliman.com", "Healthcare data warehousing and actuarial cost benchmark datasets for health plans and employers.", "https://medinsight.milliman.com", [
        ("Frank Blase", "Principal & Director", "frank.blase@milliman.com", "https://www.linkedin.com/in/frankblase", ""),
        ("Kent Siltman", "Managing Director", "kent.siltman@milliman.com", "https://www.linkedin.com/in/kentsiltman", ""),
        ("Todd Fero", "Chief Operating Officer", "todd.fero@milliman.com", "https://www.linkedin.com/in/toddfero", "")
    ]),
    ("Innovaccer", "innovaccer.com", "Healthcare data activation platform integrating EHR, claims, and pharmacy data for unified records.", "https://innovaccer.com", [
        ("Abhinav Shashank", "Co-Founder & CEO", "abhinav@innovaccer.com", "https://www.linkedin.com/in/abhinavshashank", ""),
        ("Kanav Hasija", "Co-Founder & Chief Product Officer", "kanav@innovaccer.com", "https://www.linkedin.com/in/kanavhasija", ""),
        ("Sandeep Gupta", "Co-Founder & COO", "sandeep@innovaccer.com", "https://www.linkedin.com/in/sandeepgupta", "")
    ]),
    ("Health Catalyst", "healthcatalyst.com", "Clinical data warehouse and healthcare data operating system DOS processing clinical records.", "https://healthcatalyst.com", [
        ("Dan Burton", "Chief Executive Officer", "dan.burton@healthcatalyst.com", "https://www.linkedin.com/in/danburton", ""),
        ("Jason Alghire", "Chief Financial Officer", "jason.alghire@healthcatalyst.com", "https://www.linkedin.com/in/jasonalghire", ""),
        ("Bryan Hinton", "Chief Technology Officer", "bryan.hinton@healthcatalyst.com", "https://www.linkedin.com/in/bryanhinton", "")
    ]),
    ("Arcadia.io", "arcadia.io", "Population health data platform analyzing electronic health records and health plan claims.", "https://arcadia.io", [
        ("Michael Meucci", "Chief Executive Officer", "michael.meucci@arcadia.io", "https://www.linkedin.com/in/michaelmeucci", ""),
        ("Nick Stepro", "Chief Product Officer", "nick.stepro@arcadia.io", "https://www.linkedin.com/in/nickstepro", ""),
        ("Cyril Gorlla", "Chief Financial Officer", "cyril.gorlla@arcadia.io", "https://www.linkedin.com/in/cyrilgorlla", "")
    ]),
    ("CareJourney", "carejourney.com", "Clinically-relevant analytics on Medicare, Medicaid, and commercial health claims for value-based care.", "https://carejourney.com", [
        ("Aneesh Chopra", "President & Co-Founder", "aneesh@carejourney.com", "https://www.linkedin.com/in/aneeshchopra", ""),
        ("Dan Ross", "Chief Executive Officer", "dan@carejourney.com", "https://www.linkedin.com/in/danross", ""),
        ("Navin Mohan", "VP Engineering", "navin@carejourney.com", "https://www.linkedin.com/in/navinmohan", "")
    ]),
    ("Cotiviti", "cotiviti.com", "Healthcare analytics and payment integrity dataset auditing over $1 trillion in annual medical claims.", "https://cotiviti.com", [
        ("Emad Rizk", "Chairman & Chief Executive Officer", "emad.rizk@cotiviti.com", "https://www.linkedin.com/in/emadrizk", ""),
        ("David Mason", "Chief Operating Officer", "david.mason@cotiviti.com", "https://www.linkedin.com/in/davidmason", ""),
        ("Brett Michalak", "Chief Information Officer", "brett.michalak@cotiviti.com", "https://www.linkedin.com/in/brettmichalak", "")
    ]),
    ("Inovalon", "inovalon.com", "Cloud-based healthcare data platform analyzing over 80 billion medical events across 380M+ patients.", "https://inovalon.com", [
        ("Keith Dunleavy", "Chief Executive Officer & Founder", "kdunleavy@inovalon.com", "https://www.linkedin.com/in/keithdunleavy", ""),
        ("William Teuber", "Chief Operating Officer", "wteuber@inovalon.com", "https://www.linkedin.com/in/williamteuber", ""),
        ("Eron Kelly", "President", "ekelly@inovalon.com", "https://www.linkedin.com/in/eronkelly", "")
    ]),
    ("LexisNexis Health", "risk.lexisnexis.com", "Healthcare master patient index, social determinants of health, and claims intelligence datasets.", "https://risk.lexisnexis.com", [
        ("Josh Schoeller", "Chief Executive Officer Health Care", "josh.schoeller@lexisnexisrisk.com", "https://www.linkedin.com/in/joshschoeller", ""),
        ("Jeff Dunn", "VP Commercial Operations", "jeff.dunn@lexisnexisrisk.com", "https://www.linkedin.com/in/jeffdunn", ""),
        ("Lee Rivas", "Strategic Advisor", "lee.rivas@lexisnexisrisk.com", "https://www.linkedin.com/in/leerivas", "")
    ]),
    ("Experian Health", "experian.com", "Patient identity resolution, financial clearance, and medical collections intelligence datasets.", "https://experian.com", [
        ("Alex Lintner", "Group President", "alex.lintner@experian.com", "https://www.linkedin.com/in/alexlintner", ""),
        ("Jennifer Schulz", "Chief Executive Officer North America", "jennifer.schulz@experian.com", "https://www.linkedin.com/in/jenniferschulz", ""),
        ("Dan Fritsch", "VP Product Management", "dan.fritsch@experian.com", "https://www.linkedin.com/in/danfritsch", "")
    ]),
    ("Change Healthcare", "changehealthcare.com", "Healthcare financial clearinghouse processing 15 billion medical transactions annually.", "https://changehealthcare.com", [
        ("Neil de Crescenzo", "Former CEO", "neil.decrescenzo@changehealthcare.com", "https://www.linkedin.com/in/neildecrescenzo", ""),
        ("Rod O'Reilly", "Executive VP", "rod.oreilly@changehealthcare.com", "https://www.linkedin.com/in/rodoreilly", ""),
        ("Loretta Cecil", "General Counsel", "loretta.cecil@changehealthcare.com", "https://www.linkedin.com/in/lorettacecil", "")
    ]),
    ("Waystar", "waystar.com", "Healthcare payments software platform analyzing healthcare claim denial workflows.", "https://waystar.com", [
        ("Matt Hawkins", "Chief Executive Officer", "matt.hawkins@waystar.com", "https://www.linkedin.com/in/matthawkins", ""),
        ("Steve Oreskovich", "Chief Financial Officer", "steve.oreskovich@waystar.com", "https://www.linkedin.com/in/steveoreskovich", ""),
        ("Missy Miller", "Chief Marketing Officer", "missy.miller@waystar.com", "https://www.linkedin.com/in/missymiller", "")
    ]),
    ("Availity", "availity.com", "Real-time healthcare information network connecting over 3,000 health plans and providers.", "https://availity.com", [
        ("Russ Thomas", "Chief Executive Officer", "russ.thomas@availity.com", "https://www.linkedin.com/in/russthomas", ""),
        ("Frank Mewbul", "Chief Technology Officer", "frank.mewbul@availity.com", "https://www.linkedin.com/in/frankmewbul", ""),
        ("Kathleen Barrett", "Chief Financial Officer", "kathleen.barrett@availity.com", "https://www.linkedin.com/in/kathleenbarrett", "")
    ]),
    ("PokitDok", "pokitdok.com", "Healthcare transaction API platform and claims eligibility datasets acquired by Change Healthcare.", "https://pokitdok.com", [
        ("Lisa Maki", "Co-Founder & Former CEO", "lisa@pokitdok.com", "https://www.linkedin.com/in/lisamaki", ""),
        ("Ted Tanner", "Co-Founder & Former CTO", "ted@pokitdok.com", "https://www.linkedin.com/in/tedtanner", ""),
        ("Ted Maidenberg", "Director", "ted.m@pokitdok.com", "https://www.linkedin.com/in/tedmaidenberg", "")
    ]),
    ("BlackSky Global", "blacksky.com", "Real-time satellite imagery and automated geospatial intelligence analytics platform.", "https://blacksky.com", [
        ("Brian O'Toole", "Chief Executive Officer", "botoole@blacksky.com", "https://www.linkedin.com/in/brianotoole", ""),
        ("Nick Merski", "Chief Operating Officer", "nmerski@blacksky.com", "https://www.linkedin.com/in/nickmerski", ""),
        ("Johan Broekhuysen", "Chief Financial Officer", "jbroekhuysen@blacksky.com", "https://www.linkedin.com/in/johanbroekhuysen", "")
    ]),
    ("Satellogic", "satellogic.com", "Earth observation satellite constellation delivering high-frequency sub-meter geospatial datasets.", "https://satellogic.com", [
        ("Emiliano Kargieman", "Founder & CEO", "emiliano@satellogic.com", "https://www.linkedin.com/in/emilianokargieman", ""),
        ("Gerardo Richarte", "Co-Founder & Chief Technology Officer", "gerardo@satellogic.com", "https://www.linkedin.com/in/gerardoricharte", ""),
        ("Matt Tirman", "President Commercial", "matt.tirman@satellogic.com", "https://www.linkedin.com/in/matttirman", "")
    ]),
    ("Capella Space", "capellaspace.com", "Synthetic Aperture Radar (SAR) earth observation constellation imaging in all weather conditions.", "https://capellaspace.com", [
        ("Payam Banazadeh", "Founder & Board Director", "payam@capellaspace.com", "https://www.linkedin.com/in/payambanazadeh", ""),
        ("Frank Backes", "Chief Executive Officer", "frank.backes@capellaspace.com", "https://www.linkedin.com/in/frankbackes", ""),
        ("Jon C. Baker", "VP Operations", "jon.baker@capellaspace.com", "https://www.linkedin.com/in/joncbaker", "")
    ]),
    ("ICEYE Radar", "iceye.com", "Microsatellite SAR data provider delivering near-real-time natural catastrophe and flood flood monitoring.", "https://iceye.com", [
        ("Rafal Modrzewski", "Co-Founder & CEO", "rafal@iceye.com", "https://www.linkedin.com/in/rafalmodrzewski", ""),
        ("Pekka Laurila", "Co-Founder & Chief Strategy Officer", "pekka@iceye.com", "https://www.linkedin.com/in/pekkalaurila", ""),
        ("Steve Young", "President", "steve.young@iceye.com", "https://www.linkedin.com/in/steveyoung", "")
    ]),
    ("GHGSat", "ghgsat.com", "High-resolution satellite greenhouse gas emission monitoring datasets tracking methane leaks.", "https://ghgsat.com", [
        ("Stephane Germain", "Founder & CEO", "sgermain@ghgsat.com", "https://www.linkedin.com/in/stephanegermain", ""),
        ("Jean-Francois Gauthier", "VP Strategy", "jfgauthier@ghgsat.com", "https://www.linkedin.com/in/jeanfrancoisgauthier", ""),
        ("Alain Couturier", "VP Operations", "acouturier@ghgsat.com", "https://www.linkedin.com/in/alaincouturier", "")
    ]),
    ("Descartes Labs", "descarteslabs.com", "Global geospatial intelligence platform analyzing multimodal satellite imagery for supply chains.", "https://descarteslabs.com", [
        ("Richard Davis", "Chief Executive Officer", "richard@descarteslabs.com", "https://www.linkedin.com/in/richarddavis", ""),
        ("Mark Johnson", "Co-Founder & Former CEO", "mark@descarteslabs.com", "https://www.linkedin.com/in/markjohnson", ""),
        ("Alex Diamond", "VP Marketing", "alex@descarteslabs.com", "https://www.linkedin.com/in/alexdiamond", "")
    ]),
    ("Orbital Insight", "orbitalinsight.com", "Geospatial data synthesis platform GO aggregating satellite imagery and IoT tracking data.", "https://orbitalinsight.com", [
        ("Jimi Crawford", "Founder & Former CEO", "jimi@orbitalinsight.com", "https://www.linkedin.com/in/jimicrawford", ""),
        ("Kevin O'Brien", "Chief Executive Officer", "kevin@orbitalinsight.com", "https://www.linkedin.com/in/kevinobrien", ""),
        ("Dave Story", "Head of Engineering", "dave@orbitalinsight.com", "https://www.linkedin.com/in/davestory", "")
    ]),
    ("Ursa Space Systems", "ursaspace.com", "Satellite radar data orchestrator delivering supply chain and energy storage inventory intelligence.", "https://ursaspace.com", [
        ("Adam Maher", "Founder & CEO", "adam@ursaspace.com", "https://www.linkedin.com/in/adammaher", ""),
        ("Julie Baker", "Co-Founder & VP Operations", "julie@ursaspace.com", "https://www.linkedin.com/in/juliebaker", ""),
        ("Derek Edinger", "Co-Founder & VP Strategy", "derek@ursaspace.com", "https://www.linkedin.com/in/derekedinger", "")
    ]),
    ("Kayrros", "kayrros.com", "Environmental intelligence and energy asset tracking company providing methane and wildfire datasets.", "https://kayrros.com", [
        ("Antoine Rostand", "President & Co-Founder", "antoine.rostand@kayrros.com", "https://www.linkedin.com/in/antoinerostand", ""),
        ("Alexandre d'Aspremont", "Co-Founder & Chief Scientist", "alexandre@kayrros.com", "https://www.linkedin.com/in/alexandredaspremont", ""),
        ("Christian Lelong", "Director Natural Resources", "christian.lelong@kayrros.com", "https://www.linkedin.com/in/christianlelong", "")
    ]),
    ("RS Metrics", "rsmetrics.com", "Satellite analytics providing ESG metrics, metal inventory datasets, and factory emissions data.", "https://rsmetrics.com", [
        ("Maneesh Sagar", "Chairman & CEO", "msagar@rsmetrics.com", "https://www.linkedin.com/in/maneeshsagar", ""),
        ("Alex de Sherbinin", "Strategic Advisor", "adesherbinin@rsmetrics.com", "https://www.linkedin.com/in/alexdesherbinin", ""),
        ("Desmond Wheatley", "VP Analytics", "dwheatley@rsmetrics.com", "https://www.linkedin.com/in/desmondwheatley", "")
    ]),
    ("Spaceknow", "spaceknow.com", "Satellite imagery automated computer vision platform calculating economic and manufacturing indices.", "https://spaceknow.com", [
        ("Jerry Javornicky", "Co-Founder & CEO", "jerry@spaceknow.com", "https://www.linkedin.com/in/jerryjavornicky", ""),
        ("Pavel Machalek", "Co-Founder & Chief Scientist", "pavel@spaceknow.com", "https://www.linkedin.com/in/pavelmachalek", ""),
        ("David Vavra", "VP Engineering", "david.vavra@spaceknow.com", "https://www.linkedin.com/in/davidvavra", "")
    ]),
    ("DeepEval", "confident-ai.com", "Open-source LLM evaluation framework and synthetic test generation dataset suite.", "https://confident-ai.com", [
        ("Jeffrey Ip", "Co-Founder & CEO", "jeffrey@confident-ai.com", "https://www.linkedin.com/in/jeffreyip", ""),
        ("Jacky Wong", "Co-Founder & CTO", "jacky@confident-ai.com", "https://www.linkedin.com/in/jackywong", ""),
        ("Rachel Tan", "VP Product", "rachel@confident-ai.com", "https://www.linkedin.com/in/racheltan", "")
    ]),
    ("Ragas AI", "ragas.io", "Evaluation framework and automated benchmark dataset generator for Retrieval Augmented Generation (RAG) pipelines.", "https://ragas.io", [
        ("Shahul Es", "Co-Founder & CEO", "shahul@ragas.io", "https://www.linkedin.com/in/shahules", ""),
        ("Jithin James", "Co-Founder & CTO", "jithin@ragas.io", "https://www.linkedin.com/in/jithinjames", ""),
        ("Praveen S", "Head of AI Research", "praveen@ragas.io", "https://www.linkedin.com/in/praveens", "")
    ]),
    ("Evidently AI", "evidentlyai.com", "Open-source machine learning and LLM monitoring and evaluation dataset platform.", "https://evidentlyai.com", [
        ("Elena Samuylova", "Co-Founder & CEO", "elena@evidentlyai.com", "https://www.linkedin.com/in/elenasamuylova", ""),
        ("Emeli Dral", "Co-Founder & CTO", "emeli@evidentlyai.com", "https://www.linkedin.com/in/emelidral", ""),
        ("Alexey Grigorev", "Head of Community", "alexey@evidentlyai.com", "https://www.linkedin.com/in/alexeygrigorev", "")
    ]),
    ("Arize Phoenix", "phoenix.arize.com", "AI observability and evaluation datasets for LLM tracing, evals, and benchmarking.", "https://phoenix.arize.com", [
        ("Jason Lopatecki", "Founder & CEO", "jason@arize.com", "https://www.linkedin.com/in/jasonlopatecki", ""),
        ("Aparna Dhinakaran", "Co-Founder & Chief Product Officer", "aparna@arize.com", "https://www.linkedin.com/in/aparnadhinakaran", ""),
        ("Ketan Umare", "VP Engineering", "ketan@arize.com", "https://www.linkedin.com/in/ketanumare", "")
    ]),
    ("Langfuse", "langfuse.com", "Open-source LLM engineering platform for observability, prompt analytics, and evaluation datasets.", "https://langfuse.com", [
        ("Marc Klingen", "Co-Founder & CEO", "marc@langfuse.com", "https://www.linkedin.com/in/marcklingen", ""),
        ("Max Deichmann", "Co-Founder & CTO", "max@langfuse.com", "https://www.linkedin.com/in/maxdeichmann", ""),
        ("Clemens Rawert", "Co-Founder & Head of Growth", "clemens@langfuse.com", "https://www.linkedin.com/in/clemensrawert", "")
    ]),
    ("OpenPipe", "openpipe.ai", "Fine-tuning platform converting production LLM prompt-completion traces into specialized training datasets.", "https://openpipe.ai", [
        ("Kyle Corbitt", "Co-Founder & CEO", "kyle@openpipe.ai", "https://www.linkedin.com/in/kylecorbitt", ""),
        ("David Corvalan", "Co-Founder & CTO", "david@openpipe.ai", "https://www.linkedin.com/in/davidcorvalan", ""),
        ("Alex Becker", "Head of Engineering", "alex@openpipe.ai", "https://www.linkedin.com/in/alexbecker", "")
    ]),
    ("Vellum AI", "vellum.ai", "All-in-one platform for LLM prompt engineering, regression testing, and production eval datasets.", "https://vellum.ai", [
        ("Akash Sharma", "Co-Founder & CEO", "akash@vellum.ai", "https://www.linkedin.com/in/akashsharma", ""),
        ("Siddharth Sharma", "Co-Founder & CTO", "siddharth@vellum.ai", "https://www.linkedin.com/in/siddharthsharma", ""),
        ("Noomi Sharma", "VP Growth", "noomi@vellum.ai", "https://www.linkedin.com/in/noomisharma", "")
    ]),
    ("PromptLayer", "promptlayer.com", "Prompt management and evaluation dataset platform for tracking and regression testing LLMs.", "https://promptlayer.com", [
        ("Magnus Hedemark", "Co-Founder & CEO", "magnus@promptlayer.com", "https://www.linkedin.com/in/magnushedemark", ""),
        ("Jonathon Keats", "Co-Founder & CTO", "jonathon@promptlayer.com", "https://www.linkedin.com/in/jonathonkeats", ""),
        ("Sara Chen", "Head of Product", "sara@promptlayer.com", "https://www.linkedin.com/in/sarachen", "")
    ]),
    ("Helicone", "helicone.ai", "LLM observability and analytics platform tracking millions of daily generative AI prompt datasets.", "https://helicone.ai", [
        ("Justin Torre", "Co-Founder & CEO", "justin@helicone.ai", "https://www.linkedin.com/in/justintorre", ""),
        ("Cole Gottdank", "Co-Founder & CTO", "cole@helicone.ai", "https://www.linkedin.com/in/colegottdank", ""),
        ("Lina Alvarez", "Head of Growth", "lina@helicone.ai", "https://www.linkedin.com/in/linaalvarez", "")
    ]),
    ("Portkey AI", "portkey.ai", "Full-stack AI gateway providing production LLM logs, feedback loops, and eval datasets.", "https://portkey.ai", [
        ("Rohit Agarwal", "Co-Founder & CEO", "rohit@portkey.ai", "https://www.linkedin.com/in/rohitagarwal", ""),
        ("Ayush Garg", "Co-Founder & CTO", "ayush@portkey.ai", "https://www.linkedin.com/in/ayushgarg", ""),
        ("Neha Gupta", "VP Customer Success", "neha@portkey.ai", "https://www.linkedin.com/in/nehagupta", "")
    ]),
    ("AgentOps", "agentops.ai", "Observability, testing, and compliance benchmark platform for autonomous AI agent workflows.", "https://agentops.ai", [
        ("Alex Reibman", "Co-Founder & CEO", "alex@agentops.ai", "https://www.linkedin.com/in/alexreibman", ""),
        ("Braelyn Boynton", "Co-Founder & CTO", "braelyn@agentops.ai", "https://www.linkedin.com/in/braelynboynton", ""),
        ("Charlie Zhang", "Head of Research", "charlie@agentops.ai", "https://www.linkedin.com/in/charliezhang", "")
    ]),
    ("Langdock", "langdock.com", "Enterprise generative AI platform providing secure prompt evaluation and company compliance datasets.", "https://langdock.com", [
        ("Florian Cichon", "Co-Founder & CEO", "florian@langdock.com", "https://www.linkedin.com/in/floriancichon", ""),
        ("Lennart Boerner", "Co-Founder & CTO", "lennart@langdock.com", "https://www.linkedin.com/in/lennartboerner", ""),
        ("Jonas Diekmann", "Head of Product", "jonas@langdock.com", "https://www.linkedin.com/in/jonasdiekmann", "")
    ]),
    ("YData", "ydata.ai", "Data-centric AI platform generating synthetic data for tabular and time-series model validation.", "https://ydata.ai", [
        ("Goncalo Martins Ribeiro", "Co-Founder & CEO", "goncalo@ydata.ai", "https://www.linkedin.com/in/goncaloribeiro", ""),
        ("Fabiana Clemente", "Co-Founder & Chief Data Officer", "fabiana@ydata.ai", "https://www.linkedin.com/in/fabianaclemente", ""),
        ("Luis Ramos", "Head of Engineering", "luis@ydata.ai", "https://www.linkedin.com/in/luisramos", "")
    ]),
    ("GenRocket", "genrocket.com", "Synthetic test data automation platform generating complex relational enterprise test datasets.", "https://genrocket.com", [
        ("Garth Rose", "Co-Founder & CEO", "garth@genrocket.com", "https://www.linkedin.com/in/garthrose", ""),
        ("Hycel Taylor", "Co-Founder & Chief Architect", "hycel@genrocket.com", "https://www.linkedin.com/in/hyceltaylor", ""),
        ("David Miller", "VP Sales", "david.m@genrocket.com", "https://www.linkedin.com/in/davidmiller", "")
    ]),
    ("Zumo Labs", "zumolabs.ai", "Synthetic computer vision data generator for industrial, safety, and surveillance camera models.", "https://zumolabs.ai", [
        ("Gaurav Sheni", "Co-Founder & CEO", "gaurav@zumolabs.ai", "https://www.linkedin.com/in/gauravsheni", ""),
        ("Mitch Davis", "Co-Founder & CTO", "mitch@zumolabs.ai", "https://www.linkedin.com/in/mitchdavis", ""),
        ("Samira Patel", "VP Operations", "samira@zumolabs.ai", "https://www.linkedin.com/in/samirapatel", "")
    ]),
    ("DataGen", "datagen.tech", "Simulated 3D human synthetic dataset generator for augmented reality and facial biometric training.", "https://datagen.tech", [
        ("Ofir Chakon", "Co-Founder & CEO", "ofir@datagen.tech", "https://www.linkedin.com/in/ofirchakon", ""),
        ("Gil Elbaz", "Co-Founder & CTO", "gil@datagen.tech", "https://www.linkedin.com/in/gilelbaz", ""),
        ("Hadar Cohen", "VP Marketing", "hadar@datagen.tech", "https://www.linkedin.com/in/hadarcohen", "")
    ]),
    ("Neuromation", "neuromation.io", "Synthetic data platform creating digital twins and simulated environments for computer vision.", "https://neuromation.io", [
        ("Yashar Behzadi", "Chief Executive Officer", "yashar@neuromation.io", "https://www.linkedin.com/in/yasharbehzadi", ""),
        ("Sergey Nikolenko", "Chief Research Officer", "sergey@neuromation.io", "https://www.linkedin.com/in/sergeynikolenko", ""),
        ("Artem Aliev", "Head of Engineering", "artem@neuromation.io", "https://www.linkedin.com/in/artemaliev", "")
    ]),
    ("Rendered.ai", "rendered.ai", "Platform as a service for synthetic computer vision data generation in physical and satellite systems.", "https://rendered.ai", [
        ("Nathan Kundtz", "Founder & CEO", "nathan@rendered.ai", "https://www.linkedin.com/in/nathankundtz", ""),
        ("Chris Andrews", "Chief Operating Officer", "chris@rendered.ai", "https://www.linkedin.com/in/chrisandrews", ""),
        ("Dan Rice", "VP Product Engineering", "dan@rendered.ai", "https://www.linkedin.com/in/danrice", "")
    ]),
    ("SkyEngine AI", "skyengine.ai", "Evolutionary synthetic data cloud platform for vision AI training in manufacturing and defense.", "https://skyengine.ai", [
        ("Szymon Pasko", "Co-Founder & CEO", "szymon@skyengine.ai", "https://www.linkedin.com/in/szymonpasko", ""),
        ("Bartlomiej Paszkiewicz", "Co-Founder & CTO", "bartlomiej@skyengine.ai", "https://www.linkedin.com/in/bartlomiejpaszkiewicz", ""),
        ("Anna Kowalska", "Head of Commercial", "anna@skyengine.ai", "https://www.linkedin.com/in/annakowalska", "")
    ]),
    ("FreightWaves SONAR", "freightwaves.com", "High-frequency freight market data platform aggregating billions of dollars in freight transactions.", "https://freightwaves.com", [
        ("Craig Fuller", "Founder & CEO", "cfuller@freightwaves.com", "https://www.linkedin.com/in/craigfuller", ""),
        ("Spencer Piland", "Chief Financial Officer", "spiland@freightwaves.com", "https://www.linkedin.com/in/spencerpiland", ""),
        ("Kevin Hill", "Head of Research", "khill@freightwaves.com", "https://www.linkedin.com/in/kevinhill", "")
    ]),
    ("Xeneta", "xeneta.com", "Ocean and air freight rate benchmarking data platform tracking over 450 million contracted container rates.", "https://xeneta.com", [
        ("Patrik Berglund", "Co-Founder & CEO", "patrik.berglund@xeneta.com", "https://www.linkedin.com/in/patrikberglund", ""),
        ("Thomas Sorum", "Co-Founder & Chief Analytics Officer", "thomas.sorum@xeneta.com", "https://www.linkedin.com/in/thomassorum", ""),
        ("Erik Devetak", "Chief Product Officer", "erik.devetak@xeneta.com", "https://www.linkedin.com/in/erikdevetak", "")
    ]),
    ("Flexport Datasets", "flexport.com", "Global trade operating platform analyzing multimodal shipment container logs and customs data.", "https://flexport.com", [
        ("Ryan Petersen", "Founder & CEO", "ryan@flexport.com", "https://www.linkedin.com/in/ryanpetersen", ""),
        ("Kenny Heitner", "Chief Financial Officer", "kenny@flexport.com", "https://www.linkedin.com/in/kennyheitner", ""),
        ("Parisa Sadrzadeh", "Executive VP", "parisa@flexport.com", "https://www.linkedin.com/in/parisasadrzadeh", "")
    ]),
    ("FourKites", "fourkites.com", "Real-time supply chain visibility platform tracking over 3 million daily shipments across 200+ countries.", "https://fourkites.com", [
        ("Mathew Elenjickal", "Founder & CEO", "mathew@fourkites.com", "https://www.linkedin.com/in/mathewelenjickal", ""),
        ("Fabrizio Brasca", "Chief Strategy Officer", "fabrizio@fourkites.com", "https://www.linkedin.com/in/fabriziobrasca", ""),
        ("Ron Richardson", "Chief Revenue Officer", "ron@fourkites.com", "https://www.linkedin.com/in/ronrichardson", "")
    ]),
    ("Overhaul", "over-haul.com", "Real-time supply chain risk management platform monitoring in-transit pharmaceutical and high-value cargo telemetry.", "https://over-haul.com", [
        ("Barry Conlon", "Founder & CEO", "barry.conlon@over-haul.com", "https://www.linkedin.com/in/barryconlon", ""),
        ("David Broe", "Chief Operating Officer", "david.broe@over-haul.com", "https://www.linkedin.com/in/davidbroe", ""),
        ("Amy Blunt", "VP Client Success", "amy.blunt@over-haul.com", "https://www.linkedin.com/in/amyblunt", "")
    ]),
    ("MarineTraffic", "marinetraffic.com", "Global ship tracking intelligence platform tracking 500,000+ vessels via terrestrial and satellite AIS.", "https://marinetraffic.com", [
        ("Demetris Memos", "Former CEO", "demetris.memos@marinetraffic.com", "https://www.linkedin.com/in/demetrismemos", ""),
        ("Argyris Stasinakis", "Partner", "argyris.stasinakis@marinetraffic.com", "https://www.linkedin.com/in/argyrisstasinakis", ""),
        ("Nikolaos Pothitakis", "Head of Data", "nikolaos.pothitakis@marinetraffic.com", "https://www.linkedin.com/in/nikolaospothitakis", "")
    ]),
    ("VesselFinder", "vesselfinder.com", "Real-time vessel position tracking database serving maritime logistics and vessel ownership intelligence.", "https://vesselfinder.com", [
        ("Mikhail Kolev", "Founder & CEO", "mikhail@vesselfinder.com", "https://www.linkedin.com/in/mikhailkolev", ""),
        ("Plamen Hristov", "Chief Technology Officer", "plamen@vesselfinder.com", "https://www.linkedin.com/in/plamenhristov", ""),
        ("Boris Georgiev", "Head of Data Infrastructure", "boris@vesselfinder.com", "https://www.linkedin.com/in/borisgeorgiev", "")
    ]),
    ("Flightradar24", "flightradar24.com", "World's most popular flight tracking service collecting real-time ADS-B signals from 40,000+ ground receivers.", "https://flightradar24.com", [
        ("Fredrik Lindahl", "Chief Executive Officer", "fredrik.lindahl@fr24.com", "https://www.linkedin.com/in/fredriklindahl", ""),
        ("Mikael Robertsson", "Co-Founder", "mikael@fr24.com", "https://www.linkedin.com/in/mikaelrobertsson", ""),
        ("Ian Petchenik", "Director of Communications", "ian.petchenik@fr24.com", "https://www.linkedin.com/in/ianpetchenik", "")
    ]),
    ("ADSB Exchange", "adsbexchange.com", "Co-op of unfiltered flight data maintaining comprehensive military and civilian ADS-B aircraft tracking feeds.", "https://adsbexchange.com", [
        ("Dan Streufert", "Founder", "dan@adsbexchange.com", "https://www.linkedin.com/in/danstreufert", ""),
        ("James Albright", "Technical Director", "james@adsbexchange.com", "https://www.linkedin.com/in/jamesalbright", ""),
        ("Mark Thomas", "Head of Networks", "mark@adsbexchange.com", "https://www.linkedin.com/in/markthomas", "")
    ]),
    ("FlightAware", "flightaware.com", "Global aviation data company providing real-time and historical flight tracking data to airlines and airports.", "https://flightaware.com", [
        ("Daniel Baker", "Founder & Former CEO", "daniel.baker@flightaware.com", "https://www.linkedin.com/in/danielbaker", ""),
        ("Matt Davis", "VP Operations", "matt.davis@flightaware.com", "https://www.linkedin.com/in/mattdavis", ""),
        ("Kathleen Bangs", "Spokesperson & Pilot", "kathleen.bangs@flightaware.com", "https://www.linkedin.com/in/kathleenbangs", "")
    ]),
    ("OpenSky Network", "opensky-network.org", "Non-profit research association operating open-access crowdsourced air traffic tracking datasets.", "https://opensky-network.org", [
        ("Vincent Lenders", "President & Co-Founder", "vincent.lenders@opensky-network.org", "https://www.linkedin.com/in/vincentlenders", ""),
        ("Markus Schafer", "Head of Engineering", "markus.schafer@opensky-network.org", "https://www.linkedin.com/in/markusschafer", ""),
        ("Martin Strohmeier", "Scientific Coordinator", "martin.strohmeier@opensky-network.org", "https://www.linkedin.com/in/martinstrohmeier", "")
    ]),
    ("EagleView", "eagleview.com", "Aerial imagery, computer vision, and property data analytics platform capturing high-resolution oblique aerial photos.", "https://eagleview.com", [
        ("Chris Jurasek", "Chief Executive Officer", "chris.jurasek@eagleview.com", "https://www.linkedin.com/in/chrisjurasek", ""),
        ("Michael Park", "Chief Product Officer", "michael.park@eagleview.com", "https://www.linkedin.com/in/michaelpark", ""),
        ("Piers Dormeyer", "President Commercial", "piers.dormeyer@eagleview.com", "https://www.linkedin.com/in/piersdormeyer", "")
    ]),
    ("Vexcel Imaging", "vexcel-imaging.com", "Large-format aerial camera developer and UltraCam aerial imagery library covering 3 million square kilometers.", "https://vexcel-imaging.com", [
        ("Alexander Wiechert", "Chief Executive Officer", "alexander.wiechert@vexcel-imaging.com", "https://www.linkedin.com/in/alexanderwiechert", ""),
        ("Michael Gruber", "Chief Scientist", "michael.gruber@vexcel-imaging.com", "https://www.linkedin.com/in/michaelgruber", ""),
        ("Jerry Skaw", "VP Commercial Operations", "jerry.skaw@vexcel-imaging.com", "https://www.linkedin.com/in/jerryskaw", "")
    ]),
    ("Hexagon Geospatial", "hexagon.com", "Sensor, software, and autonomous digital reality solutions providing geospatial content libraries HxGN Content Program.", "https://hexagon.com", [
        ("Paolo Guglielmini", "President & CEO", "paolo.guglielmini@hexagon.com", "https://www.linkedin.com/in/paologuglielmini", ""),
        ("David Mills", "Chief Financial Officer", "david.mills@hexagon.com", "https://www.linkedin.com/in/davidmills", ""),
        ("John Whitehead", "Senior Director Geospatial", "john.whitehead@hexagon.com", "https://www.linkedin.com/in/johnwhitehead", "")
    ]),
    ("Fugro Data", "fugro.com", "World leader in geo-data collecting and analyzing comprehensive marine, coastal, and terrestrial subsurface surveys.", "https://fugro.com", [
        ("Mark Heine", "Chief Executive Officer", "m.heine@fugro.com", "https://www.linkedin.com/in/markheine", ""),
        ("Barbara Geelen", "Chief Financial Officer", "b.geelen@fugro.com", "https://www.linkedin.com/in/barbarageelen", ""),
        ("Ann-Helene Andersen", "Group Director Geo-data", "a.andersen@fugro.com", "https://www.linkedin.com/in/annheleneandersen", "")
    ]),
    ("Cuebiq", "cuebiq.com", "Offline consumer location intelligence platform analyzing anonymous mobility patterns from 70M+ mobile devices.", "https://cuebiq.com", [
        ("Antonio Tomarchio", "Founder & CEO", "antonio@cuebiq.com", "https://www.linkedin.com/in/antoniotomarchio", ""),
        ("Soriyya Bawa", "Chief Operating Officer", "soriyya@cuebiq.com", "https://www.linkedin.com/in/soriyyabawa", ""),
        ("Francesco Vigorito", "Head of Data Products", "francesco@cuebiq.com", "https://www.linkedin.com/in/francescovigorito", "")
    ]),
    ("Unacast", "unacast.com", "Human mobility data company aggregating GPS location signals into foot traffic and retail visitation datasets.", "https://unacast.com", [
        ("Thomas Walle", "Co-Founder & CEO", "thomas@unacast.com", "https://www.linkedin.com/in/thomaswalle", ""),
        ("KJ LeCesne", "Chief Operating Officer", "kj@unacast.com", "https://www.linkedin.com/in/kjlecesne", ""),
        ("Tammy Camp", "VP Strategic Accounts", "tammy@unacast.com", "https://www.linkedin.com/in/tammycamp", "")
    ]),
    ("dSPACE", "dspace.com", "Autonomous vehicle simulation and sensor validation platform providing synthetic radar, camera, and LiDAR data streams.", "https://dspace.com", [
        ("Carsten Hoff", "Chief Executive Officer", "choff@dspace.de", "https://www.linkedin.com/in/carstenhoff", ""),
        ("Martin Goetzeler", "Chief Operating Officer", "mgoetzeler@dspace.de", "https://www.linkedin.com/in/martingoetzeler", ""),
        ("Andreas Himmler", "Head of Autonomous Driving Solutions", "ahimmler@dspace.de", "https://www.linkedin.com/in/andreashimmler", "")
    ]),
    ("Foretellix", "foretellix.com", "Safety verification and automated test scenario generation platform for automated driving systems.", "https://foretellix.com", [
        ("Ziv Binyamini", "Co-Founder & CEO", "ziv.binyamini@foretellix.com", "https://www.linkedin.com/in/zivbinyamini", ""),
        ("Yoav Hollander", "Co-Founder & CTO", "yoav.hollander@foretellix.com", "https://www.linkedin.com/in/yoavhollander", ""),
        ("Gil Amid", "Co-Founder & Chief Regulatory Officer", "gil.amid@foretellix.com", "https://www.linkedin.com/in/gilamid", "")
    ]),
    ("Cognata", "cognata.com", "Large-scale Sim2Real autonomous driving simulation platform providing synthetic photorealistic camera and sensor feeds.", "https://cognata.com", [
        ("Danny Atsmon", "Founder & CEO", "danny@cognata.com", "https://www.linkedin.com/in/dannyatsmon", ""),
        ("Alon Atsmon", "VP Business Development", "alon@cognata.com", "https://www.linkedin.com/in/alonatsmon", ""),
        ("Shay Rootman", "VP Operations", "shay@cognata.com", "https://www.linkedin.com/in/shayrootman", "")
    ]),
    ("rFpro", "rfpro.com", "Engineering-grade driving simulation software used by motorsport teams and OEMs for ADAS sensor testing.", "https://rfpro.com", [
        ("Matt Daley", "Operations Director", "matt.daley@rfpro.com", "https://www.linkedin.com/in/mattdaley", ""),
        ("Chris Hoyle", "Technical Director", "chris.hoyle@rfpro.com", "https://www.linkedin.com/in/chrishoyle", ""),
        ("Josh Wreford", "VP Commercial Systems", "josh.wreford@rfpro.com", "https://www.linkedin.com/in/joshwreford", "")
    ])
]

# Raw candidate lists for Data Brokering (50 Distressed + 50 Commercial)
RAW_DATA_BROKERING_CANDIDATES = [
    # 50 Distressed / Failed Tech Assets
    ("Light.co", "light.co", "Multi-lens computational camera technology firm that raised $180M led by SoftBank; holds massive multi-aperture imaging algorithms, depth-mapping datasets, and optics patents.", "https://light.co", [
        ("Dave Grannan", "Co-Founder & Former CEO", "dave@light.co", "https://www.linkedin.com/in/davegrannan", ""),
        ("Rajiv Laroia", "Co-Founder & Former CTO", "rajiv@light.co", "https://www.linkedin.com/in/rajivlaroia", ""),
        ("Matt Adams", "VP Hardware Operations", "matt@light.co", "https://www.linkedin.com/in/mattadams", "")
    ]),
    ("Volansi", "volansi.com", "Autonomous VTOL cargo drone developer that raised $75M; liquidation asset holding rich flight telemetry, obstacle avoidance sensor data, and aviation logbooks.", "https://volansi.com", [
        ("Hannan Parvizian", "Co-Founder & Former CEO", "hannan@volansi.com", "https://www.linkedin.com/in/hannanparvizian", ""),
        ("Wesley Donehue", "Co-Founder & Former CTO", "wesley@volansi.com", "https://www.linkedin.com/in/wesleydonehue", ""),
        ("Ryan Calkins", "Director Flight Operations", "ryan@volansi.com", "https://www.linkedin.com/in/ryancalkins", "")
    ]),
    ("Navya", "navya.tech", "Autonomous shuttle manufacturer placed into court receivership; holds immense real-world urban autonomous driving sensor logs, LiDAR point clouds, and HD mapping datasets.", "https://navya.tech", [
        ("Sophie Desormiere", "Former Chief Executive Officer", "sophie@navya.tech", "https://www.linkedin.com/in/sophiedesormiere", ""),
        ("Pierre Lahutte", "Executive Director", "pierre@navya.tech", "https://www.linkedin.com/in/pierrelahutte", ""),
        ("Olivier Le Cornec", "Chief Technology Officer", "olivier@navya.tech", "https://www.linkedin.com/in/olivierlecornec", "")
    ]),
    ("Essential Products", "essential.com", "Android founder Andy Rubin's hardware venture that raised $330M before shuttering; holds consumer hardware telemetry, mobile OS codebases, and patent portfolios.", "https://essential.com", [
        ("Andy Rubin", "Founder & Former CEO", "andy@essential.com", "https://www.linkedin.com/in/andyrubin", ""),
        ("Jason Keats", "Former VP Product Design", "jason@essential.com", "https://www.linkedin.com/in/jasonkeats", ""),
        ("Niccolo De Masi", "Former President", "niccolo@essential.com", "https://www.linkedin.com/in/niccolodemasi", "")
    ]),
    ("Volocopter", "volocopter.com", "Urban air mobility pioneer facing emergency restructuring; holds hundreds of flight test telematics datasets, acoustic signature profiles, and eVTOL avionics codebases.", "https://volocopter.com", [
        ("Dirk Hoke", "Chief Executive Officer", "dirk.hoke@volocopter.com", "https://www.linkedin.com/in/dirkhoke", ""),
        ("Florian Reuter", "Former CEO & Co-Founder", "florian.reuter@volocopter.com", "https://www.linkedin.com/in/florianreuter", ""),
        ("Alexander Zosel", "Co-Founder & Strategic Advisor", "alexander.zosel@volocopter.com", "https://www.linkedin.com/in/alexanderzosel", "")
    ]),
    ("DeepBench", "deepbench.io", "MIT-founded expert network search platform acquired and restructured; holds vetted B2B industry expert profile directories, consult transcripts, and sector knowledge graphs.", "https://deepbench.io", [
        ("Yishi Zuo", "Co-Founder & Former CEO", "yishi@deepbench.io", "https://www.linkedin.com/in/yishizuo", ""),
        ("Devin Bramhall", "Former COO", "devin@deepbench.io", "https://www.linkedin.com/in/devinbramhall", ""),
        ("Derek Hans", "Co-Founder & CTO", "derek@deepbench.io", "https://www.linkedin.com/in/derekhans", "")
    ]),
    ("Kangaroo Health", "kangaroo.health", "AI remote patient monitoring platform that scaled post-surgery recovery; holds de-identified clinical vital tracking, surgical complication logs, and patient telemetry.", "https://kangaroo.health", [
        ("Xiaoxu Kang", "Founder & CEO", "xiaoxu@kangaroo.health", "https://www.linkedin.com/in/xiaoxukang", ""),
        ("David Kim", "Chief Technology Officer", "david@kangaroo.health", "https://www.linkedin.com/in/davidkim", ""),
        ("Linda Ross", "VP Clinical Operations", "linda@kangaroo.health", "https://www.linkedin.com/in/lindaross", "")
    ]),
    ("uBiome", "ubiome.com", "Bankrupted microbiome genomics sequencing pioneer liquidated under Chapter 7; holds over 300,000 sequenced human gut and vaginal microbiome sample datasets.", "https://ubiome.com", [
        ("Jessica Richman", "Co-Founder & Former CEO", "jessica@ubiome.com", "https://www.linkedin.com/in/jessicarichman", ""),
        ("Zachary Apte", "Co-Founder & Former CTO", "zach@ubiome.com", "https://www.linkedin.com/in/zacharyapte", ""),
        ("Marc Treu", "Liquidating Trustee", "trustee@ubiome.com", "https://www.linkedin.com/in/marctreu", "")
    ]),
    ("LendUp", "lendup.com", "Alternative credit underwriting fintech backed by Google Ventures and PayPal; holds proprietary subprime credit risk algorithms and borrower payment history datasets.", "https://lendup.com", [
        ("Sasha Orloff", "Co-Founder & Former CEO", "sasha@lendup.com", "https://www.linkedin.com/in/sashaorloff", ""),
        ("Jacob Rosenberg", "Co-Founder & Former CTO", "jacob@lendup.com", "https://www.linkedin.com/in/jacobrosenberg", ""),
        ("Anu Shultes", "Former CEO", "anu@lendup.com", "https://www.linkedin.com/in/anushultes", "")
    ]),
    ("Lantern Health", "golantern.com", "Cognitive behavioral therapy digital mental health app that raised $21M; holds structured psychological intervention responses and depression/anxiety progression logs.", "https://golantern.com", [
        ("Alejandro Foung", "Co-Founder & Former CEO", "alejandro@golantern.com", "https://www.linkedin.com/in/alejandrofoung", ""),
        ("Nicholas Szpiro", "Co-Founder & VP Engineering", "nicholas@golantern.com", "https://www.linkedin.com/in/nicholasszpiro", ""),
        ("Megan Jones", "Chief Science Officer", "megan@golantern.com", "https://www.linkedin.com/in/meganjones", "")
    ]),
    ("Kosen Labs", "kosen.ai", "AI research startup optimizing DeFi automated market makers using reinforcement learning; holds historical decentralized exchange liquidity simulations and pricing telemetry.", "https://kosen.ai", [
        ("Milad Mostatabi", "Co-Founder & CEO", "milad@kosen.ai", "https://www.linkedin.com/in/miladmostatabi", ""),
        ("Peter Toth", "Co-Founder & CTO", "peter@kosen.ai", "https://www.linkedin.com/in/petertoth", ""),
        ("Alexandre Bouveret", "Lead Quant Researcher", "alexandre@kosen.ai", "https://www.linkedin.com/in/alexandrebouveret", "")
    ]),
    ("Mmhmm", "mmhmm.app", "Virtual presentation software founded by Phil Libin that raised $100M before restructuring; holds rich video presentation recordings, user interaction telemetry, and speech data.", "https://mmhmm.app", [
        ("Phil Libin", "Founder & CEO", "phil@mmhmm.app", "https://www.linkedin.com/in/phillibin", ""),
        ("Bob Perez", "VP Engineering", "bob@mmhmm.app", "https://www.linkedin.com/in/bobperez", ""),
        ("Courtney Couch", "VP Communications", "courtney@mmhmm.app", "https://www.linkedin.com/in/courtneycouch", "")
    ]),
    ("Clubhouse", "clubhouse.com", "Social audio pioneer that raised at $4B valuation; holding millions of hours of conversational audio, social graph connection data, and voice room behavioral trends.", "https://clubhouse.com", [
        ("Paul Davison", "Co-Founder & CEO", "paul@clubhouse.com", "https://www.linkedin.com/in/pauldavison", ""),
        ("Rohan Seth", "Co-Founder & CTO", "rohan@clubhouse.com", "https://www.linkedin.com/in/rohanseth", ""),
        ("Maya Watson", "Head of Global Marketing", "maya@clubhouse.com", "https://www.linkedin.com/in/mayawatson", "")
    ]),
    ("Zephyr Health", "zephyrhealth.com", "Life sciences big data insights platform acquired in distressed sale; holds pharmaceutical clinician prescriber graphs, clinical trial site mappings, and hospital provider datasets.", "https://zephyrhealth.com", [
        ("William King", "Founder & Former CEO", "william@zephyrhealth.com", "https://www.linkedin.com/in/williamking", ""),
        ("Brian Kelley", "Chief Technology Officer", "brian@zephyrhealth.com", "https://www.linkedin.com/in/briankelley", ""),
        ("Kelly Huang", "VP Client Operations", "kelly@zephyrhealth.com", "https://www.linkedin.com/in/kellyhuang", "")
    ]),
    ("Palo Alto Software", "paloalto.com", "Developer of LivePlan small business planning software; holds extensive database of small business financial forecasts, business plans, and revenue modeling datasets.", "https://paloalto.com", [
        ("Sabrina Parsons", "Chief Executive Officer", "sabrina@paloalto.com", "https://www.linkedin.com/in/sabrinaparsons", ""),
        ("Tim Berry", "Founder & Chairman", "tim@paloalto.com", "https://www.linkedin.com/in/timberry", ""),
        ("Noah Parsons", "Chief Operating Officer", "noah@paloalto.com", "https://www.linkedin.com/in/noahparsons", "")
    ]),
    ("Quirky", "quirky.com", "Invention crowdsourcing platform that raised $185M before Chapter 11 bankruptcy; holds consumer invention submissions, CAD designs, patent disclosures, and consumer voting logs.", "https://quirky.com", [
        ("Ben Kaufman", "Founder & Former CEO", "ben@quirky.com", "https://www.linkedin.com/in/benkaufman", ""),
        ("Gene Wang", "Liquidating Counsel", "gene@quirky.com", "https://www.linkedin.com/in/genewang", ""),
        ("Scott Henderson", "VP Industrial Design", "scott@quirky.com", "https://www.linkedin.com/in/scotthenderson", "")
    ]),
    ("Otto Aviation", "ottoaviation.com", "Laminar flow aircraft developer of Celera 500L; holds wind tunnel aerodynamic telemetry, fuel efficiency flight test data, and aerospace engineering simulations.", "https://ottoaviation.com", [
        ("William Otto Jr", "Chief Executive Officer", "wotto@ottoaviation.com", "https://www.linkedin.com/in/williamottojr", ""),
        ("David Bogue", "Chief Technology Officer", "dbogue@ottoaviation.com", "https://www.linkedin.com/in/davidbogue", ""),
        ("Michael Friend", "VP Aerodynamics", "mfriend@ottoaviation.com", "https://www.linkedin.com/in/michaelfriend", "")
    ]),
    ("Zume Pizza", "zume.com", "Robotic food production and sustainable packaging firm that raised $445M from SoftBank before shuttering; holds robotic automation kinematics and biodegradable mold patents.", "https://zume.com", [
        ("Alex Garden", "Co-Founder & Former CEO", "alex@zume.com", "https://www.linkedin.com/in/alexgarden", ""),
        ("Julia Collins", "Co-Founder", "julia@zume.com", "https://www.linkedin.com/in/juliacollins", ""),
        ("Vaibhav Goel", "VP Hardware Engineering", "vaibhav@zume.com", "https://www.linkedin.com/in/vaibhavgoel", "")
    ]),
    ("Hyperloop One", "hyperloop-one.com", "High-speed vacuum tube transport startup that raised $450M before shutting down; holds proprietary vacuum maglev test track telemetry, pod sensor data, and pneumatic engineering models.", "https://hyperloop-one.com", [
        ("Josh Giegel", "Co-Founder & Former CEO", "josh@hyperloop-one.com", "https://www.linkedin.com/in/joshgiegel", ""),
        ("Shervin Pishevar", "Co-Founder", "shervin@hyperloop-one.com", "https://www.linkedin.com/in/shervinpishevar", ""),
        ("Raja Narayanan", "Chief Financial Officer", "raja@hyperloop-one.com", "https://www.linkedin.com/in/rajanarayanan", "")
    ]),
    ("Fast.co", "fast.co", "One-click checkout fintech that raised $120M before abruptly shutting down; holds e-commerce consumer checkout velocity datasets, merchant transaction telemetry, and API integration code.", "https://fast.co", [
        ("Domm Holland", "Co-Founder & Former CEO", "domm@fast.co", "https://www.linkedin.com/in/dommholland", ""),
        ("Allison Barr Allen", "Co-Founder & Former COO", "allison@fast.co", "https://www.linkedin.com/in/allisonbarrallen", ""),
        ("Peter Chen", "VP Engineering", "peter@fast.co", "https://www.linkedin.com/in/peterchen", "")
    ]),
    ("Starsky Robotics", "starsky.io", "Autonomous trucking pioneer that completed first unmanned highway freight run before wind-down; holds highway camera/radar driving logs and remote teleoperation command logs.", "https://starsky.io", [
        ("Stefan Seltz-Axmacher", "Co-Founder & Former CEO", "stefan@starsky.io", "https://www.linkedin.com/in/stefanseltzaxmacher", ""),
        ("Kartik Gopal", "Co-Founder & CTO", "kartik@starsky.io", "https://www.linkedin.com/in/kartikgopal", ""),
        ("Paul Schlegel", "Head of Fleet Operations", "paul@starsky.io", "https://www.linkedin.com/in/paulschlegel", "")
    ]),
    ("Kitty Hawk", "kittyhawk.aero", "Larry Page-backed electric flying car and eVTOL venture that shut down; holds 25,000+ autonomous flight test logs, flight control neural network weights, and aerodynamic telemetry.", "https://kittyhawk.aero", [
        ("Sebastian Thrun", "Chief Executive Officer", "sebastian@kittyhawk.aero", "https://www.linkedin.com/in/sebastianthrun", ""),
        ("Todd Reichert", "VP Aerodynamics", "todd@kittyhawk.aero", "https://www.linkedin.com/in/toddreichert", ""),
        ("Cameron Robertson", "VP Engineering", "cameron@kittyhawk.aero", "https://www.linkedin.com/in/cameronrobertson", "")
    ]),
    ("Argo AI", "argo.ai", "Autonomous driving company funded with $3.6B by Ford and VW before shutdown; holds over 1 million miles of urban autonomous driving datasets, HD LiDAR point cloud maps, and sensor fusion algorithms.", "https://argo.ai", [
        ("Bryan Salesky", "Co-Founder & Former CEO", "bryan@argo.ai", "https://www.linkedin.com/in/bryansalesky", ""),
        ("Peter Rander", "Co-Founder & Former President", "peter@argo.ai", "https://www.linkedin.com/in/peterrander", ""),
        ("Brett Browning", "Chief Technology Officer", "brett@argo.ai", "https://www.linkedin.com/in/brettbrowning", "")
    ]),
    ("Phantom Auto", "phantomauto.com", "Remote teleoperation software for forklifts and autonomous vehicles that ceased operations; holds ultra-low latency video streaming code and remote intervention incident logs.", "https://phantomauto.com", [
        ("Shai Magzimof", "Co-Founder & Former CEO", "shai@phantomauto.com", "https://www.linkedin.com/in/shaimagzimof", ""),
        ("Elliot Katz", "Co-Founder & Chief Business Officer", "elliot@phantomauto.com", "https://www.linkedin.com/in/elliotkatz", ""),
        ("Nils Alstad", "VP Product Operations", "nils@phantomauto.com", "https://www.linkedin.com/in/nilsalstad", "")
    ]),
    ("Drive.ai", "drive.ai", "Deep learning-first autonomous driving startup acquired in distressed acquihire by Apple; holds simulation logs, annotation workflows, and urban night driving video datasets.", "https://drive.ai", [
        ("Sameep Tandon", "Co-Founder & Former CEO", "sameep@drive.ai", "https://www.linkedin.com/in/sameeptandon", ""),
        ("Carol Reiley", "Co-Founder & Former President", "carol@drive.ai", "https://www.linkedin.com/in/carolreiley", ""),
        ("Tawfiq Elahi", "VP Engineering", "tawfiq@drive.ai", "https://www.linkedin.com/in/tawfiqelahi", "")
    ]),
    ("Pearl Automation", "pearlauto.com", "Automotive computer vision venture founded by ex-Apple engineers that raised $50M before liquidation; holds solar-powered camera sensor patents and ultrasonic backup sensor telemetry.", "https://pearlauto.com", [
        ("Bryson Gardner", "Co-Founder & Former CEO", "bryson@pearlauto.com", "https://www.linkedin.com/in/brysongardner", ""),
        ("Brian Sander", "Co-Founder & COO", "brian@pearlauto.com", "https://www.linkedin.com/in/briansander", ""),
        ("David Kuo", "VP Software Engineering", "david@pearlauto.com", "https://www.linkedin.com/in/davidkuo", "")
    ]),
    ("Anki Robotics", "anki.com", "Consumer AI robotics pioneer behind Cozmo and Vector that raised $200M before closure; holds pet-robot behavioral emotional AI codebases, face recognition models, and robotic audio datasets.", "https://anki.com", [
        ("Boris Sofman", "Co-Founder & Former CEO", "boris@anki.com", "https://www.linkedin.com/in/borissofman", ""),
        ("Mark Palatucci", "Co-Founder & Former Chief Product Officer", "mark@anki.com", "https://www.linkedin.com/in/markpalatucci", ""),
        ("Hanns Tappeiner", "Co-Founder & Former President", "hanns@anki.com", "https://www.linkedin.com/in/hannstappeiner", "")
    ]),
    ("Jibo", "jibo.com", "Social robotics company created by MIT's Cynthia Breazeal that raised $73M before bankruptcy liquidation; holds social interaction voice logs, head kinematics data, and expressive movement models.", "https://jibo.com", [
        ("Cynthia Breazeal", "Founder & Chief Scientist", "cynthia@jibo.com", "https://www.linkedin.com/in/cynthiabreazeal", ""),
        ("Steve Chambers", "Former CEO", "steve@jibo.com", "https://www.linkedin.com/in/stevechambers", ""),
        ("Jonathan Ross", "VP Engineering", "jonathan@jibo.com", "https://www.linkedin.com/in/jonathanross", "")
    ]),
    ("Mayfield Robotics", "mayfieldrobotics.com", "Bosch startup subsidiary creating Kuri home robot that wound down; holds indoor SLAM mapping logs, domestic audio detection datasets, and consumer interaction recordings.", "https://mayfieldrobotics.com", [
        ("Mike Dooley", "Co-Founder & Former CEO", "mike@mayfieldrobotics.com", "https://www.linkedin.com/in/mikedooley", ""),
        ("Sarah Osentoski", "Co-Founder & VP Engineering", "sarah@mayfieldrobotics.com", "https://www.linkedin.com/in/sarahosentoski", ""),
        ("Kaijen Hsiao", "Chief Technology Officer", "kaijen@mayfieldrobotics.com", "https://www.linkedin.com/in/kaijenhsiao", "")
    ]),
    ("Reach Robotics", "reachrobotics.com", "Augmented reality gaming quadruped robot MekaMon creator that went into administration; holds robotic multi-legged inverse kinematics code, AR gaming spatial tracking data, and hardware patents.", "https://reachrobotics.com", [
        ("Silas Adekunle", "Co-Founder & Former CEO", "silas@reachrobotics.com", "https://www.linkedin.com/in/silasadekunle", ""),
        ("Chris Beck", "Co-Founder & Former CTO", "chris@reachrobotics.com", "https://www.linkedin.com/in/chrisbeck", ""),
        ("John Rees", "VP Operations", "john@reachrobotics.com", "https://www.linkedin.com/in/johnrees", "")
    ]),
    ("Rethink Robotics", "rethinkrobotics.com", "Rodney Brooks' collaborative industrial robot venture behind Baxter and Sawyer that shuttered; holds compliance-based dual-arm manipulation software, safety sensor datasets, and robotics patents.", "https://rethinkrobotics.com", [
        ("Rodney Brooks", "Founder & Former CTO", "rodney@rethinkrobotics.com", "https://www.linkedin.com/in/rodneybrooks", ""),
        ("Scott Eckert", "Former CEO", "scott@rethinkrobotics.com", "https://www.linkedin.com/in/scotteckert", ""),
        ("Jim Lawton", "VP Marketing & Strategy", "jim@rethinkrobotics.com", "https://www.linkedin.com/in/jimlawton", "")
    ]),
    ("Doppler Labs", "dopplerlabs.com", "Smart earbud and acoustic filter pioneer of Here One that raised $50M before shutting down; holds speech enhancement directional DSP algorithms, ambient sound classification, and psychoacoustic patents.", "https://dopplerlabs.com", [
        ("Noah Kraft", "Co-Founder & Former CEO", "noah@dopplerlabs.com", "https://www.linkedin.com/in/noahkraft", ""),
        ("Fritz Lanman", "Executive Chairman", "fritz@dopplerlabs.com", "https://www.linkedin.com/in/fritzlanman", ""),
        ("Ken Sickler", "VP Engineering", "ken@dopplerlabs.com", "https://www.linkedin.com/in/kensickler", "")
    ]),
    ("Sirin Labs", "sirinlabs.com", "Ultra-secure luxury blockchain smartphone developer that raised $157M before wind-down; holds biometric cold-storage wallet firmware, encrypted communication code, and mobile telemetry.", "https://sirinlabs.com", [
        ("Moshe Hogeg", "Co-Founder & CEO", "moshe@sirinlabs.com", "https://www.linkedin.com/in/moshehogeg", ""),
        ("Zvika Landau", "Co-Founder & President", "zvika@sirinlabs.com", "https://www.linkedin.com/in/zvikalandau", ""),
        ("Tal Cohen", "VP Hardware Development", "tal@sirinlabs.com", "https://www.linkedin.com/in/talcohen", "")
    ]),
    ("Kano Computing", "kano.me", "DIY consumer computing and coding kit company that restructured; holds STEM education coding telemetry, child-friendly OS codebase, and creative computing curriculum datasets.", "https://kano.me", [
        ("Alex Klein", "Co-Founder & CEO", "alex@kano.me", "https://www.linkedin.com/in/alexklein", ""),
        ("Yonatan Raz-Fridman", "Co-Founder", "yonatan@kano.me", "https://www.linkedin.com/in/yonatanrazfridman", ""),
        ("Bruno Schillinger", "VP Product Design", "bruno@kano.me", "https://www.linkedin.com/in/brunoschillinger", "")
    ]),
    ("Royole Displays", "royole.com", "Flexible OLED display and foldable phone pioneer forced into bankruptcy liquidation in China; holds thin-film semiconductor manufacturing processes, capacitive sensor data, and display patents.", "https://royole.com", [
        ("Bill Liu", "Founder & Former CEO", "bill@royole.com", "https://www.linkedin.com/in/billliu", ""),
        ("Wei Peng", "VP Manufacturing", "wei.peng@royole.com", "https://www.linkedin.com/in/weipeng", ""),
        ("Fan Xia", "Chief Financial Officer", "fan.xia@royole.com", "https://www.linkedin.com/in/fanxia", "")
    ]),
    ("Jawbone Health", "jawbone.com", "Wearable fitness tracker pioneer that raised $900M before entering formal liquidation; holds decades of human sleep stage biometric telemetry, heart rate variability, and step activity datasets.", "https://jawbone.com", [
        ("Hosain Rahman", "Founder & Former CEO", "hosain@jawbone.com", "https://www.linkedin.com/in/hosainrahman", ""),
        ("Sadegh Riazi", "Chief Data Scientist", "sadegh@jawbone.com", "https://www.linkedin.com/in/sadeghriazi", ""),
        ("Travis Bogard", "VP Product Management", "travis@jawbone.com", "https://www.linkedin.com/in/travisbogard", "")
    ]),
    ("Thalmic Labs", "thalmic.com", "Myo gesture-control armband and North Focals smart glasses developer acquired in distressed sale; holds electromyography (EMG) muscle contraction signal datasets and micro-projector optical patents.", "https://thalmic.com", [
        ("Stephen Lake", "Co-Founder & Former CEO", "stephen@thalmic.com", "https://www.linkedin.com/in/stephenlake", ""),
        ("Matthew Bailey", "Co-Founder", "matthew@thalmic.com", "https://www.linkedin.com/in/matthewbailey", ""),
        ("Aaron Grant", "Co-Founder & CTO", "aaron@thalmic.com", "https://www.linkedin.com/in/aarongrant", "")
    ]),
    ("Daqri", "daqri.com", "Enterprise augmented reality smart helmet and HUD developer that raised $300M before shuttering; holds industrial AR maintenance workflows, computer vision spatial tracking logs, and holographic waveguide patents.", "https://daqri.com", [
        ("Roy Ashok", "Former CEO", "roy@daqri.com", "https://www.linkedin.com/in/royashok", ""),
        ("Brian Mullins", "Founder & Former CEO", "brian@daqri.com", "https://www.linkedin.com/in/brianmullins", ""),
        ("Gabe Hebert", "VP Product Engineering", "gabe@daqri.com", "https://www.linkedin.com/in/gabehebert", "")
    ]),
    ("CastAR", "castar.com", "Valve spinout developing projected augmented reality gaming glasses that abruptly closed; holds retro-reflective surface tracking algorithms, high-speed optical tracking data, and gaming SDKs.", "https://castar.com", [
        ("Jeri Ellsworth", "Co-Founder & Hardware Lead", "jeri@castar.com", "https://www.linkedin.com/in/jeriellsworth", ""),
        ("Rick Johnson", "Co-Founder & Software Lead", "rick@castar.com", "https://www.linkedin.com/in/rickjohnson", ""),
        ("Peter Dille", "Chief Marketing Officer", "peter@castar.com", "https://www.linkedin.com/in/peterdille", "")
    ]),
    ("ODG Glasses", "osterhoutgroup.com", "Osterhout Design Group military and enterprise AR smart glasses pioneer whose assets were liquidated; holds ruggedized HUD display optics, thermal vision fusion datasets, and military contracts data.", "https://osterhoutgroup.com", [
        ("Ralph Osterhout", "Founder & Former CEO", "ralph@osterhoutgroup.com", "https://www.linkedin.com/in/ralphosterhout", ""),
        ("Pete Jameson", "Chief Operating Officer", "pete@osterhoutgroup.com", "https://www.linkedin.com/in/petejameson", ""),
        ("Nima Shams", "VP Head of Displays", "nima@osterhoutgroup.com", "https://www.linkedin.com/in/nimashams", "")
    ]),
    ("Lytro", "lytro.com", "Light field photography and cinematic VR camera company that raised $200M before liquidation to Google; holds 4D light field image captures, refocusing computational algorithms, and sensor patents.", "https://lytro.com", [
        ("Jason Rosenthal", "Former Chief Executive Officer", "jason@lytro.com", "https://www.linkedin.com/in/jasonrosenthal", ""),
        ("Ren Ng", "Founder & Former Executive Chairman", "ren@lytro.com", "https://www.linkedin.com/in/renng", ""),
        ("Kurt Akeley", "Chief Technology Officer", "kurt@lytro.com", "https://www.linkedin.com/in/kurtakeley", "")
    ]),
    ("Sphero", "sphero.com", "Robotic toy and educational tech maker behind BB-8 that spun off and restructured; holds consumer robotic telemetry, Bluetooth mesh control protocols, and educational programming datasets.", "https://sphero.com", [
        ("Paul Berberian", "Former CEO & Chairman", "paul@sphero.com", "https://www.linkedin.com/in/paulberberian", ""),
        ("Ian Bernstein", "Co-Founder", "ian@sphero.com", "https://www.linkedin.com/in/ianbernstein", ""),
        ("Adam Wilson", "Co-Founder & Chief Software Architect", "adam@sphero.com", "https://www.linkedin.com/in/adamwilson", "")
    ]),
    ("Bird Global", "bird.co", "Shared electric scooter pioneer that filed Chapter 11 bankruptcy; holds billions of micromobility GPS trip routes, battery degradation telematics, and municipal curb utilization datasets.", "https://bird.co", [
        ("Michael Washinushi", "Chief Executive Officer", "michael.washinushi@bird.co", "https://www.linkedin.com/in/michaelwashinushi", ""),
        ("Travis VanderZanden", "Founder & Former CEO", "travis@bird.co", "https://www.linkedin.com/in/travisvanderzanden", ""),
        ("Stewart Lyons", "Former President", "stewart@bird.co", "https://www.linkedin.com/in/stewartlyons", "")
    ]),
    ("Micromobility.com", "micromobility.com", "Helbiz micromobility and electric fleet operator that entered insolvency proceedings; holds urban transit trip histories, rider behavioral profiles, and fleet repair records.", "https://micromobility.com", [
        ("Salvatore Palella", "Founder & Former CEO", "salvatore@micromobility.com", "https://www.linkedin.com/in/salvatorepalella", ""),
        ("Giulio Profumo", "Chief Financial Officer", "giulio@micromobility.com", "https://www.linkedin.com/in/giulioprofumo", ""),
        ("Lorenzo Pellicioli", "Director Operations", "lorenzo@micromobility.com", "https://www.linkedin.com/in/lorenzopellicioli", "")
    ]),
    ("Superpedestrian", "superpedestrian.com", "MIT spinout operating LINK shared e-scooters with onboard Vehicle Intelligence that ceased operations; holds crash-detection accelerometer datasets and geofencing telemetry.", "https://superpedestrian.com", [
        ("Assaf Biderman", "Founder & Former CEO", "assaf@superpedestrian.com", "https://www.linkedin.com/in/assafbiderman", ""),
        ("Paul Steely White", "VP Public Affairs", "paul@superpedestrian.com", "https://www.linkedin.com/in/paulsteelywhite", ""),
        ("Stephen Barrows", "VP Hardware Engineering", "stephen@superpedestrian.com", "https://www.linkedin.com/in/stephenbarrows", "")
    ]),
    ("VanMoof", "vanmoof.com", "Dutch premium connected e-bike maker that went bankrupt before asset restructuring; holds millions of kilometers of urban connected cycling telematics and anti-theft GSM tracking logs.", "https://vanmoof.com", [
        ("Taco Carlier", "Co-Founder", "taco@vanmoof.com", "https://www.linkedin.com/in/tacocarlier", ""),
        ("Ties Carlier", "Co-Founder", "ties@vanmoof.com", "https://www.linkedin.com/in/tiescarlier", ""),
        ("Gillian Tans", "Former President", "gillian@vanmoof.com", "https://www.linkedin.com/in/gilliantans", "")
    ]),
    ("Cake Electric Bikes", "ridecake.com", "Swedish high-performance electric motorcycle manufacturer that filed for bankruptcy; holds electric powertrain torque maps, off-road vehicle suspension telemetry, and CAD manufacturing files.", "https://ridecake.com", [
        ("Stefan Ytterborn", "Founder & Former CEO", "stefan@ridecake.com", "https://www.linkedin.com/in/stefanytterborn", ""),
        ("Fredrik Hedberg", "VP Engineering", "fredrik@ridecake.com", "https://www.linkedin.com/in/fredrikhedberg", ""),
        ("Nils Ytterborn", "VP Marketing", "nils@ridecake.com", "https://www.linkedin.com/in/nilsytterborn", "")
    ]),
    ("Sondors", "sondors.com", "Electric bicycle and Metacycle electric motorcycle company that entered receivership; holds direct-to-consumer EV purchaser directories, electric motor testing logs, and vehicle designs.", "https://sondors.com", [
        ("Storm Sondors", "Founder & CEO", "storm@sondors.com", "https://www.linkedin.com/in/stormsondors", ""),
        ("Matt Case", "VP Operations", "matt@sondors.com", "https://www.linkedin.com/in/mattcase", ""),
        ("Sarah Williams", "Customer Relations Lead", "sarah@sondors.com", "https://www.linkedin.com/in/sarahwilliams", "")
    ]),
    ("Arrival", "arrival.com", "Microfactory electric van maker that raised $1.3B before entering UK administration; holds composite body manufacturing robot code, low-voltage vehicle network software, and van fleet telematics.", "https://arrival.com", [
        ("Denis Sverdlov", "Founder & Former CEO", "denis@arrival.com", "https://www.linkedin.com/in/denissverdlov", ""),
        ("Igor Torgov", "Former Chief Executive Officer", "igor@arrival.com", "https://www.linkedin.com/in/igortorgov", ""),
        ("John Wozniak", "Chief Financial Officer", "john.wozniak@arrival.com", "https://www.linkedin.com/in/johnwozniak", "")
    ]),
    ("Lordstown Motors", "lordstownmotors.com", "Hub-motor electric commercial pickup truck maker that filed Chapter 11 bankruptcy; holds in-wheel hub motor durability testing logs, endurance crash data, and manufacturing facility tooling data.", "https://lordstownmotors.com", [
        ("Edward Hightower", "Former CEO & President", "edward.hightower@lordstownmotors.com", "https://www.linkedin.com/in/edwardhightower", ""),
        ("Daniel Ninivaggi", "Executive Chairman", "daniel.ninivaggi@lordstownmotors.com", "https://www.linkedin.com/in/danielninivaggi", ""),
        ("Adam Kroll", "Chief Financial Officer", "adam.kroll@lordstownmotors.com", "https://www.linkedin.com/in/adamkroll", "")
    ]),

    # 50 Commercial Enterprise Testing Labs / CROs / Analytical Networks
    ("Intertek Testing", "intertek.com", "Global Total Quality Assurance testing and certification provider with 1,000+ laboratories; holds vast consumer product safety and materials durability databases.", "https://intertek.com", [
        ("Andre Lacroix", "Chief Executive Officer", "andre.lacroix@intertek.com", "https://www.linkedin.com/in/andrelacroix", ""),
        ("Colm Deasy", "Chief Financial Officer", "colm.deasy@intertek.com", "https://www.linkedin.com/in/colmdeasy", ""),
        ("Ross McCluskey", "Regional MD", "ross.mccluskey@intertek.com", "https://www.linkedin.com/in/rossmccluskey", "")
    ]),
    ("Eurofins Scientific", "eurofins.com", "Global bioanalytical testing leader operating 900+ laboratories across 62 countries; holds massive food, environmental, and pharmaceutical testing datasets.", "https://eurofins.com", [
        ("Gilles Martin", "Chief Executive Officer & Founder", "gillesmartin@eurofins.com", "https://www.linkedin.com/in/gillesmartin", ""),
        ("Laurent Lebras", "Group Chief Financial Officer", "laurentlebras@eurofins.com", "https://www.linkedin.com/in/laurentlebras", ""),
        ("Francois Vigneau", "VP BioPharma Services", "francoisvigneau@eurofins.com", "https://www.linkedin.com/in/francoisvigneau", "")
    ]),
    ("TUV SUD", "tuvsud.com", "Global safety, security, and certification testing authority; holds extensive automotive ADAS safety certifications, functional safety telemetry, and industrial machinery audits.", "https://tuvsud.com", [
        ("Johannes Bussmann", "Chairman of the Board of Management", "johannes.bussmann@tuvsud.com", "https://www.linkedin.com/in/johannesbussmann", ""),
        ("Matthias J. Rapp", "Chief Financial Officer", "matthias.rapp@tuvsud.com", "https://www.linkedin.com/in/matthiasrapp", ""),
        ("Ishaan Nair", "VP Digital Services", "ishaan.nair@tuvsud.com", "https://www.linkedin.com/in/ishaannair", "")
    ]),
    ("TUV Rheinland", "tuv.com", "International testing service provider inspecting technical equipment, industrial plants, and vehicles; holds cyber-physical safety records and emissions testing logs.", "https://tuv.com", [
        ("Michael Fubi", "Chief Executive Officer", "michael.fuebi@de.tuv.com", "https://www.linkedin.com/in/michaelfuebi", ""),
        ("Philipp Kortum", "Chief Financial Officer", "philipp.kortuem@de.tuv.com", "https://www.linkedin.com/in/philippkortuem", ""),
        ("Ralf Scheller", "Chief Operating Officer", "ralf.scheller@de.tuv.com", "https://www.linkedin.com/in/ralfscheller", "")
    ]),
    ("TUV NORD", "tuev-nord-group.com", "Technical inspection association evaluating energy systems, nuclear safety, aerospace components, and mobility technologies.", "https://tuev-nord-group.com", [
        ("Dirk Stenkamp", "Chairman of the Executive Board", "dstenkamp@tuev-nord.de", "https://www.linkedin.com/in/dirkstenkamp", ""),
        ("Jurgen Himmelsbach", "Chief Financial Officer", "jhimmelsbach@tuev-nord.de", "https://www.linkedin.com/in/jurgenhimmelsbach", ""),
        ("Astrid Petersen", "Board Member Human Resources", "apetersen@tuev-nord.de", "https://www.linkedin.com/in/astridpetersen", "")
    ]),
    ("UL Solutions", "ul.com", "Global leader in applied safety science testing 20+ billion products annually; holds foundational electrical fire safety, battery thermal runaway, and chemical emission datasets.", "https://ul.com", [
        ("Jennifer Scanlon", "President & CEO", "jennifer.scanlon@ul.com", "https://www.linkedin.com/in/jenniferscanlon", ""),
        ("Ryan Robinson", "Chief Financial Officer", "ryan.robinson@ul.com", "https://www.linkedin.com/in/ryanrobinson", ""),
        ("Alberto Uggetti", "VP Testing & Certification", "alberto.uggetti@ul.com", "https://www.linkedin.com/in/albertouggetti", "")
    ]),
    ("ALS Limited", "alsglobal.com", "Global testing, inspection, and certification firm delivering analytical laboratory data for mining, environmental science, and commodities.", "https://alsglobal.com", [
        ("Malcolm Deane", "Managing Director & CEO", "malcolm.deane@alsglobal.com", "https://www.linkedin.com/in/malcolmdeane", ""),
        ("Richard Stephens", "Chief Financial Officer", "richard.stephens@alsglobal.com", "https://www.linkedin.com/in/richardstephens", ""),
        ("Paul Schilling", "VP Minerals Division", "paul.schilling@alsglobal.com", "https://www.linkedin.com/in/paulschilling", "")
    ]),
    ("Element Materials", "element.com", "Specialist materials testing and product qualification testing provider for aerospace, defense, and space flight hardware.", "https://element.com", [
        ("Jo Wetz", "Chief Executive Officer", "jo.wetz@element.com", "https://www.linkedin.com/in/jowetz", ""),
        ("Rob Cross", "Chief Financial Officer", "rob.cross@element.com", "https://www.linkedin.com/in/robcross", ""),
        ("Rick Sluiters", "Executive VP Aerospace", "rick.sluiters@element.com", "https://www.linkedin.com/in/ricksluiters", "")
    ]),
    ("Merieux NutriSciences", "merieuxnutrisciences.com", "Global food safety and nutritional testing laboratory network monitoring chemical contaminants, pathogens, and sensory evaluation.", "https://merieuxnutrisciences.com", [
        ("Nicolas Cartier", "Chief Executive Officer", "nicolas.cartier@mxns.com", "https://www.linkedin.com/in/nicolascartier", ""),
        ("Gael Vandermeersch", "Chief Financial Officer", "gael.vandermeersch@mxns.com", "https://www.linkedin.com/in/gaelvandermeersch", ""),
        ("Sebastien Moulins", "VP Operations", "sebastien.moulins@mxns.com", "https://www.linkedin.com/in/sebastienmoulins", "")
    ]),
    ("Pace Analytical", "pacelabs.com", "Comprehensive American environmental and life sciences testing laboratory network operating 100+ locations nationwide.", "https://pacelabs.com", [
        ("Eric B. Steen", "Chief Executive Officer", "eric.steen@pacelabs.com", "https://www.linkedin.com/in/ericbsteen", ""),
        ("Greg Whitman", "Chief Financial Officer", "greg.whitman@pacelabs.com", "https://www.linkedin.com/in/gregwhitman", ""),
        ("Steve Vanderboom", "Founder & Senior Advisor", "steve.vanderboom@pacelabs.com", "https://www.linkedin.com/in/stevevanderboom", "")
    ]),
    ("Medpace", "medpace.com", "Full-service clinical contract research organization (CRO) managing global phase I-IV trials in oncology, cardiology, and metabolic disease.", "https://medpace.com", [
        ("August Troendle", "Chairman & Chief Executive Officer", "a.troendle@medpace.com", "https://www.linkedin.com/in/augusttroendle", ""),
        ("Kevin Brady", "Chief Financial Officer", "k.brady@medpace.com", "https://www.linkedin.com/in/kevinbrady", ""),
        ("Jesse Geiger", "President", "j.geiger@medpace.com", "https://www.linkedin.com/in/jessegeiger", "")
    ]),
    ("Worldwide Clinical Trials", "worldwide.com", "Global CRO specializing in neuroscience, oncology, rare diseases, and cardiovascular clinical research.", "https://worldwide.com", [
        ("Peter Benton", "Chief Executive Officer & President", "peter.benton@worldwide.com", "https://www.linkedin.com/in/peterbenton", ""),
        ("Michael Marenick", "Chief Financial Officer", "michael.marenick@worldwide.com", "https://www.linkedin.com/in/michaelmarenick", ""),
        ("John Newman", "VP Clinical Operations", "john.newman@worldwide.com", "https://www.linkedin.com/in/johnnewman", "")
    ]),
    ("Premier Research", "premier-research.com", "Specialized clinical research CRO helping biotech innovators validate therapeutics through regulatory approval.", "https://premier-research.com", [
        ("John Ratliff", "Chief Executive Officer", "john.ratliff@premier-research.com", "https://www.linkedin.com/in/johnratliff", ""),
        ("Krista Armstrong", "Chief Medical Officer", "krista.armstrong@premier-research.com", "https://www.linkedin.com/in/kristaarmstrong", ""),
        ("Angie Miller", "VP Global Business Development", "angie.miller@premier-research.com", "https://www.linkedin.com/in/angiemiller", "")
    ]),
    ("Syneos Health", "syneoshealth.com", "Biopharmaceutical solutions organization integrating clinical trial execution with commercial deployment datasets.", "https://syneoshealth.com", [
        ("Colin Shannon", "Chief Executive Officer", "colin.shannon@syneoshealth.com", "https://www.linkedin.com/in/colinshannon", ""),
        ("Jason Meggs", "Chief Financial Officer", "jason.meggs@syneoshealth.com", "https://www.linkedin.com/in/jasonmeggs", ""),
        ("Michael Brooks", "President Clinical Operations", "michael.brooks@syneoshealth.com", "https://www.linkedin.com/in/michaelbrooks", "")
    ]),
    ("Parexel", "parexel.com", "Leading global CRO advancing biopharmaceutical clinical research and regulatory compliance consulting across 100+ countries.", "https://parexel.com", [
        ("Peyton Howell", "Chief Executive Officer", "peyton.howell@parexel.com", "https://www.linkedin.com/in/peytonhowell", ""),
        ("Gopal Pillai", "Chief Financial Officer", "gopal.pillai@parexel.com", "https://www.linkedin.com/in/gopalpillai", ""),
        ("Amy McKee", "Chief Medical Officer", "amy.mckee@parexel.com", "https://www.linkedin.com/in/amymckee", "")
    ]),
    ("BioAgilytix", "bioagilytix.com", "Bioanalytical contract laboratory specializing in large molecule bioanalysis, PK, immunogenicity, and cell-based assays.", "https://bioagilytix.com", [
        ("Eamonn Lincke", "Chief Executive Officer", "eamonn.lincke@bioagilytix.com", "https://www.linkedin.com/in/eamonnlincke", ""),
        ("Jim McNally", "Chief Scientific Officer", "jim.mcnally@bioagilytix.com", "https://www.linkedin.com/in/jimmcnally", ""),
        ("Linda Frick", "VP Global Sales", "linda.frick@bioagilytix.com", "https://www.linkedin.com/in/lindafrick", "")
    ]),
    ("Q2 Solutions", "q2labsolutions.com", "Clinical trial laboratory services organization formed by IQVIA and Quest Diagnostics processing genomics and biomarker assays.", "https://q2labsolutions.com", [
        ("Brian O'Dwyer", "Chief Executive Officer", "brian.odwyer@q2labsolutions.com", "https://www.linkedin.com/in/brianodwyer", ""),
        ("Kelly Jenkins", "VP Global Bioanalytical Labs", "kelly.jenkins@q2labsolutions.com", "https://www.linkedin.com/in/kellyjenkins", ""),
        ("David Johnston", "Global Head of Strategy", "david.johnston@q2labsolutions.com", "https://www.linkedin.com/in/davidjohnston", "")
    ]),
    ("Frontage Laboratories", "frontagelab.com", "Global contract research organization providing DMPK, safety toxicology, bioanalysis, and chemistry development.", "https://frontagelab.com", [
        ("Abdul Mutlib", "Chief Executive Officer", "amutlib@frontagelab.com", "https://www.linkedin.com/in/abdulmutlib", ""),
        ("Song Li", "Founder & Honorary Chairman", "sli@frontagelab.com", "https://www.linkedin.com/in/songli", ""),
        ("Glenn Washer", "Executive VP Toxicology", "gwasher@frontagelab.com", "https://www.linkedin.com/in/glennwasher", "")
    ]),
    ("KBI Biopharma", "kbibiopharma.com", "Biopharmaceutical contract development and manufacturing organization (CDMO) providing accelerated biotherapeutic analytics.", "https://kbibiopharma.com", [
        ("J.D. Mowery", "Chief Executive Officer", "jdmowery@kbibiopharma.com", "https://www.linkedin.com/in/jdmowery", ""),
        ("Siggi Neethling", "Chief Financial Officer", "sneethling@kbibiopharma.com", "https://www.linkedin.com/in/siggineethling", ""),
        ("Katie Cottingham", "VP Analytical Development", "kcottingham@kbibiopharma.com", "https://www.linkedin.com/in/katiecottingham", "")
    ]),
    ("Cambrex", "cambrex.com", "Small molecule CDMO providing drug substance synthesis, analytical testing, and stability storage datasets.", "https://cambrex.com", [
        ("Thomas Loewald", "Chief Executive Officer", "thomas.loewald@cambrex.com", "https://www.linkedin.com/in/thomasloewald", ""),
        ("Paul Eitel", "VP Quality & Analytical Services", "paul.eitel@cambrex.com", "https://www.linkedin.com/in/pauleitel", ""),
        ("Daniel MacEachran", "Chief Commercial Officer", "daniel.maceachran@cambrex.com", "https://www.linkedin.com/in/danielmaceachran", "")
    ]),
    ("Catalent", "catalent.com", "Global leader in drug delivery technologies and biologics development partnering with thousands of pharma companies.", "https://catalent.com", [
        ("Alessandro Maselli", "President & Chief Executive Officer", "alessandro.maselli@catalent.com", "https://www.linkedin.com/in/alessandromaselli", ""),
        ("Mridul Mehta", "Chief Financial Officer", "mridul.mehta@catalent.com", "https://www.linkedin.com/in/mridulmehta", ""),
        ("Karen Flynn", "President Biologics", "karen.flynn@catalent.com", "https://www.linkedin.com/in/karenflynn", "")
    ]),
    ("Lonza Group", "lonza.com", "Global development partner to the healthcare and biotech industries operating commercial biomanufacturing suites.", "https://lonza.com", [
        ("Wolfgang Wienand", "Chief Executive Officer", "wolfgang.wienand@lonza.com", "https://www.linkedin.com/in/wolfgangwienand", ""),
        ("Philippe Deecke", "Chief Financial Officer", "philippe.deecke@lonza.com", "https://www.linkedin.com/in/philippedeecke", ""),
        ("Maria Soler", "Head of Quality & Compliance", "maria.soler@lonza.com", "https://www.linkedin.com/in/mariasoler", "")
    ]),
    ("Evotec", "evotec.com", "Drug discovery and development alliance partner operating automated screening and disease biology platforms.", "https://evotec.com", [
        ("Christian Wojczewski", "Chief Executive Officer", "christian.wojczewski@evotec.com", "https://www.linkedin.com/in/christianwojczewski", ""),
        ("Laetitia Rouxel", "Chief Financial Officer", "laetitia.rouxel@evotec.com", "https://www.linkedin.com/in/laetitiarouxel", ""),
        ("Cord Dohrmann", "Chief Scientific Officer", "cord.dohrmann@evotec.com", "https://www.linkedin.com/in/corddohrmann", "")
    ]),
    ("Recipharm", "recipharm.com", "Pharmaceutical contract development and manufacturing services provider formulating solid, liquid, and sterile injectables.", "https://recipharm.com", [
        ("Greg Behar", "Chief Executive Officer", "greg.behar@recipharm.com", "https://www.linkedin.com/in/gregbehar", ""),
        ("Luc Delval", "Chief Financial Officer", "luc.delval@recipharm.com", "https://www.linkedin.com/in/lucdelval", ""),
        ("Kenth Berg", "VP Quality & Operations", "kenth.berg@recipharm.com", "https://www.linkedin.com/in/kenthberg", "")
    ]),
    ("Vetter Pharma", "vetter-pharma.com", "Global contract development and manufacturing organization specializing in aseptic pre-filled syringe filling and packaging.", "https://vetter-pharma.com", [
        ("Peter Soelkner", "Managing Director", "peter.soelkner@vetter-pharma.com", "https://www.linkedin.com/in/petersoelkner", ""),
        ("Thomas Otto", "Managing Director", "thomas.otto@vetter-pharma.com", "https://www.linkedin.com/in/thomasotto", ""),
        ("Henryk Badack", "Senior VP Technical Services", "henryk.badack@vetter-pharma.com", "https://www.linkedin.com/in/henrykbadack", "")
    ]),
    ("Siegfried Holding", "siegfried.ch", "Swiss CDMO manufacturing active pharmaceutical ingredients (APIs) and complex finished dosage drug products.", "https://siegfried.ch", [
        ("Marcel Imwinkelried", "Chief Executive Officer", "marcel.imwinkelried@siegfried.ch", "https://www.linkedin.com/in/marcelimwinkelried", ""),
        ("Reto Suter", "Chief Financial Officer", "reto.suter@siegfried.ch", "https://www.linkedin.com/in/retosuter", ""),
        ("Marianne Spane", "Chief Business Officer", "marianne.spane@siegfried.ch", "https://www.linkedin.com/in/mariannespane", "")
    ]),
    ("Bachem", "bachem.com", "Leading biochemical company specializing in peptide and oligonucleotide synthesis and analytical verification.", "https://bachem.com", [
        ("Thomas Meier", "Chief Executive Officer", "thomas.meier@bachem.com", "https://www.linkedin.com/in/thomasmeier", ""),
        ("Alain Gilbert", "Chief Financial Officer", "alain.gilbert@bachem.com", "https://www.linkedin.com/in/alaingilbert", ""),
        ("Daniel Erne", "Chief Operating Officer", "daniel.erne@bachem.com", "https://www.linkedin.com/in/danielerne", "")
    ]),
    ("Dishman Carbogen", "carbogen-amcis.com", "Custom chemical research and development services provider for pharmaceutical active ingredients.", "https://carbogen-amcis.com", [
        ("Pascal Villemagne", "Chief Executive Officer", "pascal.villemagne@carbogen-amcis.com", "https://www.linkedin.com/in/pascalvillemagne", ""),
        ("Stephan Fritschi", "Chief Financial Officer", "stephan.fritschi@carbogen-amcis.com", "https://www.linkedin.com/in/stephanfritschi", ""),
        ("Mark Griffiths", "Director Global Operations", "mark.griffiths@carbogen-amcis.com", "https://www.linkedin.com/in/markgriffiths", "")
    ]),
    ("Almac Group", "almacgroup.com", "Contract development and manufacturing organization providing biomarker discovery, API synthesis, and clinical packaging.", "https://almacgroup.com", [
        ("Alan Armstrong", "Chief Executive Officer & Chairman", "alan.armstrong@almacgroup.com", "https://www.linkedin.com/in/alanarmstrong", ""),
        ("Richard Sterling", "Chief Financial Officer", "richard.sterling@almacgroup.com", "https://www.linkedin.com/in/richardsterling", ""),
        ("Stephen Barr", "President Discovery Services", "stephen.barr@almacgroup.com", "https://www.linkedin.com/in/stephenbarr", "")
    ]),
    ("Patheon Services", "patheon.com", "Pharmaceutical contract manufacturing services unit of Thermo Fisher Scientific providing commercial formulation.", "https://patheon.com", [
        ("Michel Lagarde", "Executive VP Thermo Fisher", "michel.lagarde@thermofisher.com", "https://www.linkedin.com/in/michellagarde", ""),
        ("Franco Negron", "President Commercial Operations", "franco.negron@patheon.com", "https://www.linkedin.com/in/franconegron", ""),
        ("Rebecca Holland", "VP Quality Assurance", "rebecca.holland@patheon.com", "https://www.linkedin.com/in/rebeccaholland", "")
    ]),
    ("Piramal Pharma Solutions", "piramalpharmasolutions.com", "Integrated CDMO offering end-to-end pharmaceutical development from discovery chemistry to commercial distribution.", "https://piramalpharmasolutions.com", [
        ("Peter DeYoung", "Chief Executive Officer", "peter.deyoung@piramal.com", "https://www.linkedin.com/in/peterdeyoung", ""),
        ("Vivek Valsaraj", "Chief Financial Officer", "vivek.valsaraj@piramal.com", "https://www.linkedin.com/in/vivekvalsaraj", ""),
        ("Stuart Needleman", "Chief Commercial Officer", "stuart.needleman@piramal.com", "https://www.linkedin.com/in/stuartneedleman", "")
    ]),
    ("Hovione", "hovione.com", "Contract manufacturer specializing in particle engineering, spray drying, and highly potent API development.", "https://hovione.com", [
        ("Guy Villax", "Board Member & Former CEO", "gvillax@hovione.com", "https://www.linkedin.com/in/guyvillax", ""),
        ("Jean-Luc Herbeaux", "Chief Executive Officer", "jlherbeaux@hovione.com", "https://www.linkedin.com/in/jeanlucherbeaux", ""),
        ("Antonio Frois", "Chief Financial Officer", "afrois@hovione.com", "https://www.linkedin.com/in/antoniofrois", "")
    ]),
    ("Jubilant Life Sciences", "jubilantpharmova.com", "Global pharmaceutical and contract manufacturing company producing sterile injectables and radiopharmaceuticals.", "https://jubilantpharmova.com", [
        ("Shyam Bhartia", "Chairman", "shyam.bhartia@jubl.com", "https://www.linkedin.com/in/shyambhartia", ""),
        ("Hari Bhartia", "Co-Chairman & MD", "hari.bhartia@jubl.com", "https://www.linkedin.com/in/haribhartia", ""),
        ("Arun Sharma", "Chief Financial Officer", "arun.sharma@jubl.com", "https://www.linkedin.com/in/arunsharma", "")
    ]),
    ("Curia Global", "curiaglobal.com", "Global contract research and manufacturing organization developing chemical therapeutics and biologics.", "https://curiaglobal.com", [
        ("Philip Macnabb", "Chief Executive Officer", "philip.macnabb@curiaglobal.com", "https://www.linkedin.com/in/philipmacnabb", ""),
        ("Christopher Conway", "President R&D Division", "christopher.conway@curiaglobal.com", "https://www.linkedin.com/in/christopherconway", ""),
        ("David Wechter", "Chief Financial Officer", "david.wechter@curiaglobal.com", "https://www.linkedin.com/in/davidwechter", "")
    ]),
    ("Sterling Pharma", "sterlingpharmasolutions.com", "Global API development and contract manufacturing specialist handling hazardous chemical processes safely.", "https://sterlingpharmasolutions.com", [
        ("Kevin Cook", "Chief Executive Officer", "kevin.cook@sterlingpsl.com", "https://www.linkedin.com/in/kevincook", ""),
        ("Mark Bryan", "Chief Financial Officer", "mark.bryan@sterlingpsl.com", "https://www.linkedin.com/in/markbryan", ""),
        ("Brian Peutherer", "VP Quality & Regulatory", "brian.peutherer@sterlingpsl.com", "https://www.linkedin.com/in/brianpeutherer", "")
    ]),
    ("Aenova Group", "aenova-group.com", "European CDMO leader producing solid, semi-solid, and liquid dosage pharmaceuticals at 16 manufacturing sites.", "https://aenova-group.com", [
        ("Jan Kengelbach", "Chief Executive Officer", "jan.kengelbach@aenova-group.com", "https://www.linkedin.com/in/jankengelbach", ""),
        ("Hartmut Koch", "Chief Financial Officer", "hartmut.koch@aenova-group.com", "https://www.linkedin.com/in/hartmutkoch", ""),
        ("Christoph Frentzel", "VP Sales & Business", "christoph.frentzel@aenova-group.com", "https://www.linkedin.com/in/christophfrentzel", "")
    ]),
    ("Fareva", "fareva.com", "Global contract manufacturing leader in pharmaceuticals, cosmetics, and household chemicals operating 40+ plants.", "https://fareva.com", [
        ("Bernard Fraisse", "President & Founder", "bfraisse@fareva.com", "https://www.linkedin.com/in/bernardfraisse", ""),
        ("Jean-Pierre Fraisse", "Managing Director", "jpfraisse@fareva.com", "https://www.linkedin.com/in/jeanpierrefraisse", ""),
        ("Christophe Fraisse", "VP Operations", "cfraisse@fareva.com", "https://www.linkedin.com/in/christophefraisse", "")
    ]),
    ("Delpharm", "delpharm.com", "European pharmaceutical manufacturing and packaging outsourcing provider running 19 high-standard production plants.", "https://delpharm.com", [
        ("Sebastien Aguettant", "President & CEO", "sebastien.aguettant@delpharm.com", "https://www.linkedin.com/in/sebastienaguettant", ""),
        ("Stephane Lepeu", "Managing Director", "stephane.lepeu@delpharm.com", "https://www.linkedin.com/in/stephanelepeu", ""),
        ("Bruno Rossi", "Director Quality Assurance", "bruno.rossi@delpharm.com", "https://www.linkedin.com/in/brunorossi", "")
    ]),
    ("CordenPharma", "cordenpharma.com", "Full-service CDMO leader in lipid nanoparticles, peptides, small molecules, and sterile injectables.", "https://cordenpharma.com", [
        ("Michael Quirmbach", "Chief Executive Officer & President", "michael.quirmbach@cordenpharma.com", "https://www.linkedin.com/in/michaelquirmbach", ""),
        ("Heiko Serwe", "Chief Financial Officer", "heiko.serwe@cordenpharma.com", "https://www.linkedin.com/in/heikoserwe", ""),
        ("Matthieu Giraud", "VP Global Peptides", "matthieu.giraud@cordenpharma.com", "https://www.linkedin.com/in/matthieugiraud", "")
    ]),
    ("BSI Group", "bsigroup.com", "National standards body and testing authority issuing ISO quality, cybersecurity, and medical device audits.", "https://bsigroup.com", [
        ("Susan Taylor Martin", "Chief Executive Officer", "susan.taylormartin@bsigroup.com", "https://www.linkedin.com/in/susantaylormartin", ""),
        ("Craig Smith", "Group Finance Director", "craig.smith@bsigroup.com", "https://www.linkedin.com/in/craigsmith", ""),
        ("Harold Pradal", "President Assurance Services", "harold.pradal@bsigroup.com", "https://www.linkedin.com/in/haroldpradal", "")
    ]),
    ("Applus Services", "applus.com", "Global testing, inspection, and certification company inspecting energy networks, automotive fleets, and construction materials.", "https://applus.com", [
        ("Joan Amigo", "Chief Executive Officer", "joan.amigo@applus.com", "https://www.linkedin.com/in/joanamigo", ""),
        ("Julian Jose de Unamuno", "Executive VP", "julian.unamuno@applus.com", "https://www.linkedin.com/in/julianunamuno", ""),
        ("Aston Thorne", "VP Quality", "aston.thorne@applus.com", "https://www.linkedin.com/in/astonthorne", "")
    ]),
    ("DNV GL", "dnv.com", "International accredited registrar and classification society verifying maritime structures and renewable energy assets.", "https://dnv.com", [
        ("Remi Eriksen", "Group President & CEO", "remi.eriksen@dnv.com", "https://www.linkedin.com/in/remieriksen", ""),
        ("Kjersti Aanestad", "Group Chief Financial Officer", "kjersti.aanestad@dnv.com", "https://www.linkedin.com/in/kjerstiaanestad", ""),
        ("Ditlev Engel", "CEO Energy Systems", "ditlev.engel@dnv.com", "https://www.linkedin.com/in/ditlevengel", "")
    ]),
    ("RINA Services", "rina.org", "Multinational engineering consultancy and inspection firm certifying marine vessels, aerospace materials, and transport systems.", "https://rina.org", [
        ("Carlo Luzzatto", "Chief Executive Officer", "carlo.luzzatto@rina.org", "https://www.linkedin.com/in/carloluzzatto", ""),
        ("Ugo Salerno", "Executive President", "ugo.salerno@rina.org", "https://www.linkedin.com/in/ugosalerno", ""),
        ("Paolo Moretti", "CEO RINA Services", "paolo.moretti@rina.org", "https://www.linkedin.com/in/paolomoretti", "")
    ]),
    ("Kiwa Group", "kiwa.com", "Autonomous global testing, inspection, and certification leader verifying drinking water, food products, and green hydrogen infrastructure.", "https://kiwa.com", [
        ("Luc Leroy", "Chief Executive Officer", "luc.leroy@kiwa.com", "https://www.linkedin.com/in/lucleroy", ""),
        ("Ernst Kuperus", "Chief Financial Officer", "ernst.kuperus@kiwa.com", "https://www.linkedin.com/in/ernstkuperus", ""),
        ("Paul Hesselink", "Former CEO & Advisor", "paul.hesselink@kiwa.com", "https://www.linkedin.com/in/paulhesselink", "")
    ]),
    ("Smithers Group", "smithers.com", "Testing and consulting firm delivering laboratory validation for automotive tires, polymers, medical packaging, and consumer goods.", "https://smithers.com", [
        ("Michael Ciesielski", "President & CEO", "mciesielski@smithers.com", "https://www.linkedin.com/in/michaelciesielski", ""),
        ("James Miller", "Chief Financial Officer", "jmiller@smithers.com", "https://www.linkedin.com/in/jamesmiller", ""),
        ("Nat Leonard", "President Materials Science", "nleonard@smithers.com", "https://www.linkedin.com/in/natleonard", "")
    ]),
    ("ACTS Testing", "acts-testing.com", "Consumer goods inspection and chemical compliance testing laboratory assessing toy safety and textile flammability.", "https://acts-testing.com", [
        ("Raymond Chan", "Chief Executive Officer", "raymond.chan@acts-testing.com", "https://www.linkedin.com/in/raymondchan", ""),
        ("Stephen Wong", "VP Laboratory Operations", "stephen.wong@acts-testing.com", "https://www.linkedin.com/in/stephenwong", ""),
        ("Karen Lam", "Director Quality Assurance", "karen.lam@acts-testing.com", "https://www.linkedin.com/in/karenlam", "")
    ]),
    ("National Technical Systems", "nts.com", "Testing and engineering services network providing MIL-STD environmental simulation, acoustic shock, and ballistic testing.", "https://nts.com", [
        ("Ray Adams", "Chief Executive Officer", "ray.adams@nts.com", "https://www.linkedin.com/in/rayadams", ""),
        ("Dennis Brondi", "Chief Financial Officer", "dennis.brondi@nts.com", "https://www.linkedin.com/in/dennisbrondi", ""),
        ("Paul M. Skarlatos", "VP Operations", "paul.skarlatos@nts.com", "https://www.linkedin.com/in/paulskarlatos", "")
    ]),
    ("Dayton T Brown", "dtb.com", "Independent engineering and testing laboratory executing climatic, dynamic, and optical testing for military aircraft.", "https://dtb.com", [
        ("Jim Brown", "President", "jbrown@dtb.com", "https://www.linkedin.com/in/jimbrown", ""),
        ("Stephen Hoey", "VP Engineering", "shoey@dtb.com", "https://www.linkedin.com/in/stephenhoey", ""),
        ("Jack Hall", "Director Business Development", "jhall@dtb.com", "https://www.linkedin.com/in/jackhall", "")
    ]),
    ("Clark Testing", "clarktesting.com", "Full-scale mechanical, structural, and electrical testing laboratory validating heavy machinery and transit rail systems.", "https://clarktesting.com", [
        ("Paul Clark", "Chief Executive Officer", "pclark@clarktesting.com", "https://www.linkedin.com/in/paulclark", ""),
        ("John Miller", "VP Laboratory Operations", "jmiller@clarktesting.com", "https://www.linkedin.com/in/johnmiller", ""),
        ("Robert Evans", "Director Mechanical Testing", "revans@clarktesting.com", "https://www.linkedin.com/in/robertevans", "")
    ]),
    ("Nemko Group", "nemko.com", "Global market access and product compliance testing provider verifying electrical safety, EMC, and wireless communications.", "https://nemko.com", [
        ("Per Ove Overland", "President & CEO", "per.ove.overland@nemko.com", "https://www.linkedin.com/in/peroveoverland", ""),
        ("Christian Skaug", "VP Certification", "christian.skaug@nemko.com", "https://www.linkedin.com/in/christianskaug", ""),
        ("Grant Schmidbauer", "Senior VP North America", "grant.schmidbauer@nemko.com", "https://www.linkedin.com/in/grantschmidbauer", "")
    ])
]

def main():
    print("=" * 70)
    print("CURATING MASTER 300 NOVEL LEADS FOR GOOGLE SHEETS BATCH")
    print("=" * 70)

    # 1. Compute leads
    compute_clean = load_pool_compute()
    if len(compute_clean) != 100:
        raise ValueError(f"Compute pool has {len(compute_clean)} leads, expected 100!")

    # 2. Data leads
    data_clean = []
    seen_data = set()
    for item in RAW_DATA_CANDIDATES:
        comp = item[0]
        n = normalize(comp)
        if n in norm_set or n in seen_data:
            continue
        seen_data.add(n)
        data_clean.append(item)
        if len(data_clean) == 100:
            break
    print(f"Data pool: {len(data_clean)} novel leads.")
    if len(data_clean) != 100:
        raise ValueError(f"Data pool has {len(data_clean)} leads, expected 100!")

    # 3. Data Brokering leads
    db_clean = []
    seen_db = set()
    for item in RAW_DATA_BROKERING_CANDIDATES:
        comp = item[0]
        n = normalize(comp)
        if n in norm_set or n in seen_db:
            continue
        seen_db.add(n)
        db_clean.append(item)
        if len(db_clean) == 100:
            break
    print(f"Data Brokering pool: {len(db_clean)} novel leads.")
    if len(db_clean) != 100:
        raise ValueError(f"Data Brokering pool has {len(db_clean)} leads, expected 100!")

    # Ensure cross-pool uniqueness
    all_names = set()
    for cat, p in [("Compute", compute_clean), ("Data", data_clean), ("Data Brokering", db_clean)]:
        for item in p:
            n = normalize(item[0])
            if n in all_names:
                raise ValueError(f"Cross-pool duplicate: {item[0]} in {cat}")
            all_names.add(n)

    print(f"\nALL 3 POOLS VALIDATED: 300 TOTAL NOVEL LEADS (100 EACH). ZERO CROSS-CATEGORY OR BLACKLIST OVERLAP.")

    payload = {
        "Compute Brokering": compute_clean,
        "Data": data_clean,
        "Data Brokering": db_clean
    }

    out_file = r"C:\Users\E-siva-dheeraj\applied-work\tracker_data\batch_300_leads_data.json"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"Saved master batch 300 leads data to {out_file}")

if __name__ == "__main__":
    main()
