from abc import ABC, abstractmethod
from decimal import Decimal 

# AbstarctProduct
class Chemical(ABC):
    @abstractmethod
    def pay(self, amount:Decimal):
        pass
    

