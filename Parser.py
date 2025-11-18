from abc import ABC, abstractmethod

class Parser(ABC):

    @abstractmethod
    def parse(self, raw_data: str) -> dict:
        pass
