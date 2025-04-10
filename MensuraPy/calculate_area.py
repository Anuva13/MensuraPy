import math
from unit_converter import * # Module to convert dimensions to base unit 'm'

def square(dictionary, target_unit = 'm'):
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for key, values in dictionary.items() for item in [key] + values]
    side_value = flat_list[1]
    side_unit = flat_list[0]
    
    # Convert side to target unit (default is meters)
    side = convert_to_base_unit(side_value, side_unit, target_unit)
    
    # Compute area in square of the target unit
    area = side * side
    result = f"{area} {target_unit}²"
    # Returns the area of a square.
    return result

def rectangle(list, target_unit = 'm'):
    print(f"area:area-  {list}")
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for d in list for key, values in d.items() for item in [key] + values]
    # '1' and '3' i.e. odd numbers have values and even numbers have keys (units)
    length_value = flat_list[1]
    length_unit = flat_list[0]
    breadth_value = flat_list[3]
    breadth_unit = flat_list[2]
    
    # Convert both to target unit (default is meters)
    length = convert_to_base_unit(length_value, length_unit, target_unit)
    breadth = convert_to_base_unit(breadth_value, breadth_unit, target_unit)
    
    # Compute area in square of the target unit
    area = length * breadth
    result = f"{area} {target_unit}²"
    # Returns the area of a rectangle
    return result

def circle(dictionary, target_unit = 'm'):
    print(f"area:area-  {dictionary}")
    flat_list = [item for key, values in dictionary.items() for item in [key] + values]
    radius_value = flat_list[1]
    radius_unit = flat_list[0]
    
    # Convert radius to target unit (default is meters)
    radius = convert_to_base_unit(radius_value, radius_unit, target_unit)
    
    # Compute area in square of the target unit
    area = math.pi * radius ** 2
    result = f"{area} {target_unit}²"
    # Returns the area of a circle.
    return result

def triangle(list, target_unit = 'm'):
    print(f"area:area-  {list}")
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for d in list for key, values in d.items() for item in [key] + values]
    print(f"area:area-  {flat_list}")
    # '1' and '3' i.e. odd numbers have values and even numbers have keys (units)
    l = len(flat_list)
    
    if l == 2:
        unit = flat_list[0]
        side = convert_to_base_unit(flat_list[1], unit, target_unit)
        area = (math.sqrt(3) / 4) * side ** 2
        result = f"{area} {target_unit}²"
        return result
        
    elif l == 4:
        base_unit, base_value = flat_list[0], flat_list[1]
        height_unit, height_value = flat_list[2], flat_list[3]
        base = convert_to_base_unit(base_value, base_unit, target_unit)
        height = convert_to_base_unit(height_value, height_unit, target_unit)
        result = 0.5 * base * height
        result = f"{area} {target_unit}²"
        return result
        
    elif l == 6:
        unit_1 = flat_list[0]
        unit_2 = flat_list[2]
        unit_3 = flat_list[4]
        value_1 = flat_list[1]
        value_2 = flat_list[3]
        value_3 = flat_list[5]
        
        if unit_1 == 'degrees' and value_1 < 180:
            angle_radians = math.radians(value_1)
            a = convert_to_base_unit(value_2, unit_2, target_unit)
            b = convert_to_base_unit(value_3, unit_3, target_unit)
            area = 0.5 * a * b * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result
        
        elif unit_2 == 'degrees' and value_2 < 180:
            angle_radians = math.radians(value_2)
            a = convert_to_base_unit(value_1, unit_1, target_unit)
            b = convert_to_base_unit(value_3, unit_3, target_unit)
            area = 0.5 * a * b * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result
        
        elif unit_3 == 'degrees' and value_3 < 180:
            angle_radians = math.radians(value_3)
            a = convert_to_base_unit(value_1, unit_1, target_unit)
            b = convert_to_base_unit(value_2, unit_2, target_unit)
            area = 0.5 * a * b * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result
        
        else:
            a = convert_to_base_unit(value_1, unit_1, target_unit)
            b = convert_to_base_unit(value_2, unit_2, target_unit)
            c = convert_to_base_unit(value_3, unit_3, target_unit)
            s = (a + b + c)/2
            # Returns the area of a triangle when 3 sides are given
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            result = f"{area} {target_unit}²"
            return result
        
def parallelogram(list, target_unit = 'm'):
    print(f"area:area-  {list}")
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for d in list for key, values in d.items() for item in [key] + values]
    print(f"area:area-  {flat_list}")
    # '1' and '3' i.e. odd numbers have values and even numbers have keys (units)
    l = len(flat_list)
    
    if l == 4:
        base_value = flat_list[1]
        base_unit = flat_list[0]
        height_value = flat_list[3]
        height_unit = flat_list[2]
        base = convert_to_base_unit(base_value, base_unit, target_unit)
        height = convert_to_base_unit(height_value, height_unit, target_unit)
        area = base * height
        result = f"{area} {target_unit}²"
        return result
    
    elif l == 6:
        value_1 = flat_list[1]
        unit_1 = flat_list[0]
        value_2 = flat_list[3]
        unit_2 = flat_list[2]
        value_3 = flat_list[5]
        unit_3 = flat_list[4]
        
        if unit_1 == 'degrees' and value_1 < 180:
            angle_radians = math.radians(value_1)
            a = convert_to_base_unit(value_2, unit_2, target_unit)
            b = convert_to_base_unit(value_3, unit_3, target_unit)
            area = a * b * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result
        elif unit_2 == 'degrees' and value_2 < 180:
            angle_radians = math.radians(value_2)
            a = convert_to_base_unit(value_1, unit_1, target_unit)
            b = convert_to_base_unit(value_3, unit_3, target_unit)
            area = a * b * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result
        
        elif unit_3 == 'degrees' and value_3 < 180:
            angle_radians = math.radians(value_3)
            a = convert_to_base_unit(value_1, unit_1, target_unit)
            b = convert_to_base_unit(value_2, unit_2, target_unit)
            area = a * b * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result

def rhombus(list, target_unit = 'm'):
    print(f"area:area-  {list}")
    # Structure the recieved data in a flattened list displaying keys and values
    flat_list = [item for d in list for key, values in d.items() for item in [key] + values]
    print(f"area:area-  {flat_list}")
    # '1' and '3' i.e. odd numbers have values and even numbers have keys (units)
    l = len(flat_list)
    
    if l == 4:
        diagonal1_value = flat_list[1]
        diagonal1_unit = flat_list[0]
        diagonal2_value = flat_list[3]
        diagonal2_unit = flat_list[2]
        d1 = convert_to_base_unit(diagonal1_value, diagonal1_unit, target_unit)
        d2 = convert_to_base_unit(diagonal2_value, diagonal2_unit, target_unit)
        area = 0.5 * d1 * d2
        result = f"{area} {target_unit}²"
        return result
    
    else:
        value_1 = flat_list[1]
        unit_1 = flat_list[0]
        value_2 = flat_list[3]
        unit_2 = flat_list[2]
        
        if unit_1 == 'degrees' and value_1 < 180:
            angle_radians = math.radians(value_1)
            a = convert_to_base_unit(value_2, unit_2, target_unit)
            area = a * a * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result
        elif unit_2 == 'degrees' and value_2 < 180:
            angle_radians = math.radians(value_2)
            a = convert_to_base_unit(value_1, unit_1, target_unit)
            area = a * a * math.sin(angle_radians)
            result = f"{area} {target_unit}²"
            return result
        

    
    