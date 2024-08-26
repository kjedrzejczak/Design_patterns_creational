from chemicals_types.chemical import Chemical
from chemical_method import ChemicalMethod
from chemicals_types.chem_type_1 import Chem1
from chemicals_types.chem_type_2 import Chem2
from chemicals_types.chem_type_3 import Chem3
from chemicals_types.chem_type_4 import Chem4



# Crator 
class ChemicalFactory:
    @staticmethod
    def create(chem_method:ChemicalMethod)  -> Chemical:
        match chem_method:
            case ChemicalMethod.FIRST:
                return Chem1()
            case ChemicalMethod.SECOND:
                return Chem2()
            case ChemicalMethod.THIRD:
                return Chem3()   
            case ChemicalMethod.FOURTH:
                return Chem4()          
            case _:
                raise ValueError(f"{chem_method} is not currently supported.")