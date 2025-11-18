from ParseReceipt import ParseReceipt
from Parser import Parser

class POSFactory:

    def get_parser(self, data_type: str) -> Parser:
        if data_type.lower() == "txt":
            return ParseReceipt()
        else:
            raise ValueError("Unsupported POS format")
