import math
from unit_converter import * # Module to convert dimensions to base unit 'm'

def cube(dictionary, target_unit = 'm'):
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for key, values in dictionary.items() for item in [key] + values]
    side_value = flat_list[1]
    side_unit = flat_list[0]
    
    # Convert side to target unit (default is meters)
    side = convert_to_base_unit(side_value, side_unit, target_unit)
    
    # Compute surface area in cube of the target unit
    TSA = 6 * side * side
    LSA = 4 * side * side
    BA = side * side
    result = f" \n Total Surface Area: {TSA} {target_unit}² \n Lateral Surface Area: {LSA} {target_unit}² \n Base Area: {BA} {target_unit}²"
    # Returns the surface area of a cube.
    return result

def cuboid(list, target_unit = 'm'):
    print(f"area:area-  {list}")
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for d in list for key, values in d.items() for item in [key] + values]
    # '1' and '3' i.e. odd numbers have values and even numbers have keys (units)
    length_value = flat_list[1]
    length_unit = flat_list[0]
    breadth_value = flat_list[3]
    breadth_unit = flat_list[2]
    height_value = flat_list[5]
    height_unit = flat_list[4]
    
    # Convert both to target unit (default is meters)
    l = convert_to_base_unit(length_value, length_unit, target_unit)
    b = convert_to_base_unit(breadth_value, breadth_unit, target_unit)
    h = convert_to_base_unit(height_value, height_unit, target_unit)
    
    # Compute area in cuboid of the target unit
    TSA = 2 * ((l * b) + (b * h) + (h * l))
    LSA = 2 * h * (l + b)
    BA = l * b
    result = f" \n Total Surface Area: {TSA} {target_unit}² \n Lateral Surface Area: {LSA} {target_unit}² \n Base Area: {BA} {target_unit}²"
    # Returns the area of a cuboid
    return result