import json
from POSFactory import POSFactory

factory = POSFactory()
parser = factory.get_parser("txt")

with open("recipt.txt", "r", encoding="utf-16") as f:
    text = f.read()

parsed = parser.parse(text)

print(json.dumps(parsed, indent=4))
