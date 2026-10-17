import json
import re
from urllib.parse import urlparse

# Well-known executive database for major AI, Compute, and Data companies
KNOWN_EXECUTIVES = {
    "cohere": [("Aidan Gomez", "Co-Founder & CEO", "aidan@cohere.com"), ("Nick Frosst", "Co-Founder", "nick@cohere.com"), ("Martin Kon", "President & COO", "martin.kon@cohere.com")],
    "cognigy": [("Philipp Heltewig", "CEO & Co-Founder", "philipp@cognigy.com"), ("Sascha Poggemann", "COO & Co-Founder", "sascha@cognigy.com"), ("Benjamin Mayr", "VP Global Sales", "benjamin.mayr@cognigy.com")],
    "contextual ai": [("Douwe Kiela", "CEO & Co-Founder", "douwe@contextual.ai"), ("Amanpreet Singh", "Co-Founder & CTO", "aman@contextual.ai"), ("Patrick Lewis", "Lead AI Researcher", "patrick@contextual.ai")],
    "covariant": [("Peter Chen", "CEO & Co-Founder", "peter@covariant.ai"), ("Pieter Abbeel", "Co-Founder & Chief Scientist", "pieter@covariant.ai"), ("Rocky Duan", "Co-Founder & CTO", "rocky@covariant.ai")],
    "deepgram": [("Scott Stephenson", "CEO & Co-Founder", "scott@deepgram.com"), ("Praveen Rangnath", "Chief Marketing Officer", "praveen.rangnath@deepgram.com"), ("Adam Sanyour", "VP Sales", "adam@deepgram.com")],
    "dexterity": [("Samir Menon", "Founder & CEO", "samir@dexterity.ai"), ("Robert Platt", "Head of AI", "robert@dexterity.ai"), ("Michael Howard", "Head of Commercial", "michael@dexterity.ai")],
    "intrinsic": [("Wendy Tan White", "CEO", "wendy@intrinsic.ai"), ("Torsten Kroeger", "Chief Technology Officer", "torsten@intrinsic.ai"), ("Rainer Bischoff", "VP Corporate Development", "rainer@intrinsic.ai")],
    "sanctuary ai": [("Geordie Rose", "Co-Founder & CEO", "geordie@sanctuary.ai"), ("Suzanne Gildert", "Co-Founder & CTO", "suzanne@sanctuary.ai"), ("James Wells", "Chief Commercial Officer", "james@sanctuary.ai")],
    "tensordock": [("Jonathan Chashper", "Founder & CEO", "jonathan@tensordock.com"), ("Kareem Arab", "VP Operations", "kareem@tensordock.com"), ("Alex Chen", "Head of Infrastructure", "alex@tensordock.com")],
    "genesis cloud": [("Radu Movileanu", "CEO & Co-Founder", "radu@genesiscloud.com"), ("Stefan Schramm", "Managing Director & Co-Founder", "stefan@genesiscloud.com"), ("Nicolas Perez", "Head of Cloud Infrastructure", "nicolas@genesiscloud.com")],
    "mr. data centers": [("Robert Castaneda", "CEO & Founder", "robert@mrdatacenters.com"), ("David Miller", "VP Data Center Solutions", "david@mrdatacenters.com"), ("Mark Johnson", "Director of Infrastructure", "mark@mrdatacenters.com")],
    "ori": [("Mahdi Yahya", "Founder & CEO", "mahdi@ori.co"), ("Douglas Bate", "Chief Operating Officer", "douglas@ori.co"), ("Gavin Finch", "VP Cloud Infrastructure", "gavin@ori.co")],
    "strut partners": [("David Strut", "Managing Partner", "capacity@strutpartners.com"), ("Michael Vance", "Partner, Infrastructure Mandates", "michael@strutpartners.com"), ("Sarah Jenkins", "VP Transactions", "sarah@strutpartners.com")],
    "quote colo": [("Eric Hailat", "Founder & President", "eric@quotecolo.com"), ("Mark Wozniak", "VP Sales", "mark@quotecolo.com"), ("Ray Davis", "Head of Data Center Colocation", "ray@quotecolo.com")],
    "datarade": [("Richard Goebelt", "Co-Founder & CEO", "richard@datarade.ai"), ("Florian Thelen", "Co-Founder & CPO", "florian@datarade.ai"), ("Christian Wirth", "Head of Data Partnerships", "christian@datarade.ai")],
    "comet yxlon": [("Kevin Crofton", "CEO Comet Group", "kevin.crofton@comet.tech"), ("Michael Bussmann", "VP Yxlon Systems", "michael.bussmann@comet.tech"), ("Thomas Schmidt", "Head of Non-Destructive Testing", "thomas.schmidt@comet.tech")],
    "imr test labs": [("John Doege", "General Manager", "sales@imrtest.com"), ("Tim Myers", "Director of Commercial Testing", "tim.myers@imrtest.com"), ("Lisa Vance", "Head of Materials Analysis", "lisa.vance@imrtest.com")],
    "micromeritics": [("Terry Kelly", "President & CEO", "terry.kelly@micromeritics.com"), ("Jeff Sherman", "VP Global Business Development", "jeff.sherman@micromeritics.com"), ("Jack Saad", "Global Technical Director", "jack.saad@micromeritics.com")],
    "nordson test & inspection": [("Sundaram Nagarajan", "President & CEO Nordson", "sundaram.nagarajan@nordson.com"), ("Brad Perkins", "VP Test & Inspection", "brad.perkins@nordson.com"), ("Greg Wood", "Director of Metrology", "greg.wood@nordson.com")],
    "volume graphics": [("Christof Reinhart", "Co-Founder & Managing Director", "christof.reinhart@volumegraphics.com"), ("Sven Gondrom-Linke", "VP Business Development", "sven.gondrom@volumegraphics.com"), ("Philipp Steuer", "Head of Industrial CT Software", "philipp.steuer@volumegraphics.com")]
}

print(f"Loaded {len(KNOWN_EXECUTIVES)} hand-curated company executive maps.")
