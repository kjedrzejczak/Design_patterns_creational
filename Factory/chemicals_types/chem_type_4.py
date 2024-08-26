from chemicals_types.chemical import Chemical
from decimal import Decimal 


#ConcreteProductD
class Chem4(Chemical):
    def pay(self, amount:Decimal):
        #return super().pay(amount)
        print(f"Fourth chemical ${amount}.")