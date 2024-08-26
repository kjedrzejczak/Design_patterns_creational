from chemicals_types.chemical import Chemical
from decimal import Decimal 


#ConcreteProductB
class Chem2(Chemical):
    def pay(self, amount:Decimal):
        #return super().pay(amount)
        print(f"Second chemical ${amount}.")