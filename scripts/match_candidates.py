import json

existing = set(open(r'C:\Users\E-siva-dheeraj\applied-work\tracker_data\existing_companies_set.txt', encoding='utf-8').read().lower().splitlines())
pkg = json.load(open(r'C:\Users\E-siva-dheeraj\applied-work\exports\batch_150_20261016\complete_150_leads_package.json', encoding='utf-8'))
existing.update(r['Company'].lower() for r in pkg['daily_signals'])

candidates = [
    'Surge AI', 'Invisible Technologies', 'Mindrift', 'Oneforma', 'Alignerr',
    'Toloka AI', 'TaskUs', 'Appen', 'Pactera EDGE', 'CloudFactory',
    'Defined.ai', 'Shutterstock', 'Freepik', 'Getty Images', 'Pond5',
    'Veritone', 'SoundHound AI', 'Speechmatics', 'Deepgram', 'AssemblyAI',
    'Gretel.ai', 'Mostly AI', 'Hazy', 'Tonic.ai', 'Synthesis AI',
    'Parallel Domain', 'Betterdata', 'K2View', 'Datomize', 'Statice',
    'Codeium', 'Augment Code', 'Tabnine', 'Sourcegraph', 'Openlayer',
    'Confident AI', 'Arize AI', 'Galileo AI', 'Patronus AI', 'Braintrust',
    'Enigma Technologies', 'Crux Informatics', 'Thinknum', 'Eagle Alpha', 'Neudata',
    'Veraset', 'Gravy Analytics', 'SafeGraph', 'Similarweb', 'Bright Data'
]

for c in candidates:
    for e in existing:
        if c.lower() == e.strip().lower():
            print(f"EXACT MATCH: '{c}' == '{e}'")
            break
        elif len(c) > 4 and (c.lower() in e or (len(e) > 4 and e in c.lower())):
            print(f"SUBSTRING MATCH: '{c}' matched with '{e}'")
            break
