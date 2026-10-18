import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.check_blacklist_helper import normalize, norm_set

candidates_compute = [
    "Silo AI", "Aleph Alpha", "AI Singapore", "BharatGPT", "Kotoba Translation",
    "Stockmark AI", "Preferred Networks", "Upstage AI", "Wrtn Technologies", "Rebellions",
    "FuriosaAI", "DeepX", "Mobilint", "Oxford Semantic Technologies", "Cartesia AI",
    "Suno AI", "Udio AI", "Boomy AI", "Soundful AI", "Endel Sound",
    "Consensus AI", "SciSpace Typeset", "Robin AI", "Leya Legal", "Luminance AI",
    "Spellbook Legal", "Decagon AI", "Forethought AI", "Ada Support", "Observe.ai",
    "Level AI", "Replicant Voice", "Symbotic", "Berkshire Grey", "Locus Robotics",
    "Geekplus Robotics", "GreyOrange", "Exotec Skypod", "AutoStore Systems", "Gideon Brothers",
    "OTTO Motors", "Seegrid Corporation", "Vecna Robotics", "Canvas Construction", "Dusty Robotics",
    "Built Robotics", "Civils.ai", "Ambi Robotics", "Mujin Corp", "Fizyr Vision",
    "RightHand Robotics", "Micropsi Industries", "Osaro AI", "Soft Robotics Inc", "Robust.AI",
    "Iambic Therapeutics", "Genesis Therapeutics", "Generate Biomedicines", "Dyno Therapeutics", "Inceptive Bio",
    "Cradle Bio", "LabGenius", "Peptone Bio", "Aether Biomachines", "Shiru Protein",
    "Charm Therapeutics", "Atomic AI", "PostEra Chemistry", "Valence Discovery", "Standigm",
    "Simulations Plus", "Sabey Data Centers", "CyrusOne", "EdgeConneX", "Yondr Group",
    "Switch Citadel", "CoreSite Realty", "TierPoint Colocation", "Flexential Datacenters", "Netrality Data Centers",
    "Cologix Interconnect", "Telehouse KDDI", "Colt Data Centres", "Green Mountain Norway", "Verne Global Iceland",
    "Lefdal Mine Datacenter", "Bulk Infrastructure", "Kao Data UK", "Global Switch", "AirTrunk Hyperscale",
    "Princeton Digital Group", "BDx Datacenters", "STT GDC", "NEXTDC Australia", "Vnet Group",
    "GDS Holdings", "Chindata Group", "Keppel Data Centres", "Maincubes Datacenters", "Evoque Data Centers"
]

clean = []
dups = []
for c in candidates_compute:
    if normalize(c) in norm_set:
        dups.append(c)
    else:
        clean.append(c)

print(f"Total checked: {len(candidates_compute)}, Clean: {len(clean)}, Duplicates: {len(dups)}")
if dups:
    print("Duplicates:", dups)
