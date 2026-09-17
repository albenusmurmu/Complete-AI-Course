import convertor
# import specific function from the entire module
from convertor import lbs_to_kg

output = convertor.kg_to_lbs(60)
print(f'in lbs : {int(output)}')

outputTwo = convertor.lbs_to_kg(133.33333333333334)
print(f'in kgs : {int(outputTwo)}')

# importing from out side

import sys
import os

# Adds the parent folder ('practice') to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Example usage:
# Success case
# from ecommerce.shipping import calculate_shipping
import ecommerce.shipping
print(ecommerce.shipping.calculate_shipping(2, 1, 3, warehouse_ready=True))  # Outputs: (2, 1, 3)

# Error case
print(ecommerce.shipping.calculate_shipping(2, 1, 3, warehouse_ready=False))  # Outputs: Warehouse is not ready...
