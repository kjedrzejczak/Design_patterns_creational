from inspect import getmembers, isclass, isabstract
import chemicals_types  # our package

# Creator 
class DynamicChemistryFactory(object):
    chemical_dictionay = {} # przechowuje wszystkie możliwe klasy 

    def __init__(self):
        self.load_chemical_types()  # it will guarantee that load_payment_types append value to to class dictionary.chemical_dictionay
    
    def load_chemical_types(self):
        members = getmembers(chemicals_types, lambda m: isclass(m) and not isabstract(m))  # list of memebers as a dictionary
        for name, _type in members:
            if isclass(_type) and issubclass(_type, chemicals_types.Chemical):
                self.chemical_dictionay[name] = _type  # dodawanie do słownika


    def create(self, chemical_type:str):
        if chemical_type in self.chemical_dictionay:
            return self.chemical_dictionay[chemical_type]()
        else:
            raise ValueError(f"{chemical_type} is not currently supported.")