import json


def second_solution(text: str) -> dict:

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    data = {}
    items = []

    # 1) date
    data["Date"] = lines[1]

    new_lines = lines[:]
    new_lines.remove(lines[1])         # remove date
    new_lines.remove(lines[-1])        # remove last line (duplicate code)
    
    cleaned = []
    for line in new_lines:
        
        if ":" in line and "$" in line:
            key_part, value_part = line.split(":", 1)
            key = key_part.strip()

            before_dollar, after_dollar = value_part.split("$", 1)
            value = after_dollar.strip()
            sign = "$"

            data[key] = value
            data[key + "_sign"] = sign
            continue
        
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
            continue
        
        cleaned.append(line)

    i = 0
    while i < len(cleaned):
        line = cleaned[i]

        if "x" not in line:
            item_name = line
            qty_line = cleaned[i + 1]

            qty_part, price_part = qty_line.split("x", 1)

            qty = int(qty_part.strip())
            price = float(price_part.strip().split("$")[1].split()[0])

            items.append({
                "name": item_name,
                "qty": qty,
                "price": price
            })

            i += 2
            continue
        
        i += 1

    data["items"] = items
    return data





with open("recipt.txt", "r", encoding="utf-16") as f:
    text = f.read()

parsed = second_solution(text)

print(json.dumps(parsed, indent=4))
