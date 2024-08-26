from dynamic_chemical_factory import DynamicChemistryFactory
from chemical_factory import ChemicalFactory
from chemical_factory import ChemicalMethod 

# Client 
def main():
    factory = DynamicChemistryFactory()
    payment = factory.create("Chem1")
    payment.pay(20.00) 

    factory = DynamicChemistryFactory()
    payment = factory.create("Chem2")
    payment.pay(2330.00) 

    factory = DynamicChemistryFactory()
    payment = factory.create("Chem3")
    payment.pay(23440.00) 

    factory = DynamicChemistryFactory()
    payment = factory.create("Chem4")
    payment.pay(234550.00) 


if __name__ == "__main__":
    main()