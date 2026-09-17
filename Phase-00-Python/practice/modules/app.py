import convertor
# import specific function from the entire module
from convertor import lbs_to_kg

output = convertor.kg_to_lbs(60)
print(f'in lbs : {int(output)}')

outputTwo = convertor.lbs_to_kg(133.33333333333334)
print(f'in kgs : {int(outputTwo)}')

# //// for ecommerce package

import ecommerce.shipping
# call calculator functions
ecommerce.shipping.calc_shipping()

# # import particular field 

from ecommerce.shipping import calc_shipping, add
# access functions
calc_shipping()
calc_shipping()
add()

# another method
from ecommerce import shipping

shipping.calc_shipping()
