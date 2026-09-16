import convertor
# import specific function from the entire module
from convertor import lbs_to_kg

output = convertor.kg_to_lbs(60)
print(f'in lbs : {int(output)}')

outputTwo = convertor.lbs_to_kg(133.33333333333334)
print(f'in kgs : {int(outputTwo)}')