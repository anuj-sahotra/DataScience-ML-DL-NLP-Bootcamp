def convert_temperature(temp, unit):
    """This function convert temperature b/w celsius and fahrenheit"""
    
    if unit in ('c', 'celsius'):
        return temp * 9/5 + 32  ## Celsius to Fahrenheit
    elif unit in ('f', "fahrenheit"):
        return (temp - 32) * 5/9 ## Fahrenheit to Celsius
    else:
        return None
    
try:
    temp = float(input("Temperature : "))
    unit = input("Units (C/F) : ").strip().lower()
    result = convert_temperature(temp, unit)

    if result is None:
        print("Invalid unit. Use C or F.")
    else:
        target = "F" if unit in ('c', 'celsius') else "C"
        print(f"Result = {result:.2f} °{target}")
except ValueError:
    print("Invalid temperature")    
    