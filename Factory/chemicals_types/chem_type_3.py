from chemicals_types.chemical import Chemical
from decimal import Decimal 


#ConcreteProductC
class Chem3(Chemical):
    def pay(self, amount:Decimal):
        #return super().pay(amount)
        print(f"Third chemical ${amount}.")