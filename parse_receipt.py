import re
import json

def parse_receipt(text: str) -> dict:

    
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    data = {}
    items = []

    i = 0
    last_index = len(lines) - 1

    while i < len(lines):
        line = lines[i]

        
        if ":" in line:
            key, value = line.split(":", 1)

            data[key.strip()] = value.strip()
            i += 1
            continue

    
        if re.match(r"\d{2}/\d{2}/\d{4}", line):
            data["Date"] = line
            i += 1
            continue

        
        if i == last_index:
            data["Receipt Duplicate"] = line
            break

        
        item_name = line
        qty_line = lines[i + 1]

        
        match = re.search(
            r"(\d+)\s*x\s*\$(\d+\.\d+).*?\$(\d+\.\d+)",
            qty_line
        )

        if match:
            qty = int(match.group(1))
            price = float(match.group(2))
            total = float(match.group(3))

            items.append({
                "name": item_name,
                "qty": qty,
                "price": price,
                "total": total
            })

            
            i += 2
            continue

        i += 1

    
    data["items"] = items

    return data




with open("recipt.txt", "r", encoding="utf-16") as f:
    text = f.read()

parsed = parse_receipt(text)

print(json.dumps(parsed, indent=4))
