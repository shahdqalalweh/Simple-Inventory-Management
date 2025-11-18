

import re
from Parser import Parser

class ParseReceipt(Parser):

    def parse(self, text: str) -> dict:

        lines = [l.strip() for l in text.split("\n") if l.strip()]

        data = {}
        items = []

        i = 0
        last_index = len(lines) - 1

        while i < len(lines):
            line = lines[i]

            # key : value
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
                i += 1
                continue

            # Date
            if re.match(r"\d{2}/\d{2}/\d{4}", line):
                data["Date"] = line
                i += 1
                continue

            # Last item (duplicate indicator)
            if i == last_index:
                data["Receipt Duplicate"] = line
                break

            # Item name
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
