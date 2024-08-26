from chemical_factory import ChemicalFactory
from chemical_factory import ChemicalMethod 

# Client 
def main():
    payment = ChemicalFactory.create(ChemicalMethod.FIRST)
    payment.pay(1000.00) 
    payment = ChemicalFactory.create(ChemicalMethod.SECOND)
    payment.pay(1340.00) 
    payment = ChemicalFactory.create(ChemicalMethod.THIRD)
    payment.pay(3300.00) 
    payment = ChemicalFactory.create(ChemicalMethod.FOURTH)
    payment.pay(555.00) 



if __name__ == "__main__":
    main()