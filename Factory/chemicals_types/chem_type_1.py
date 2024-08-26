from chemicals_types.chemical import Chemical
from decimal import Decimal 


#ConcreteProductA
class Chem1(Chemical):
    def pay(self, amount:Decimal):
        #return super().pay(amount)
        print(f"First chemical ${amount}.")