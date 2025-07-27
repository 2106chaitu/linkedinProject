def convert_temperature(value, unit):
    unit = unit.lower()

    if unit == 'celsius':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin

    elif unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin

    elif unit == 'kelvin':
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit

    else:
        raise ValueError("Unsupported unit. Choose Celsius, Fahrenheit, or Kelvin.")

# Prompt user input
try:
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (Celsius/Fahrenheit/Kelvin): ")

    if unit.lower() == "celsius":
        f, k = convert_temperature(temp, unit)
        print(f"{temp}°C is {f:.2f}°F and {k:.2f}K")

    elif unit.lower() == "fahrenheit":
        c, k = convert_temperature(temp, unit)
        print(f"{temp}°F is {c:.2f}°C and {k:.2f}K")

    elif unit.lower() == "kelvin":
        c, f = convert_temperature(temp, unit)
        print(f"{temp}K is {c:.2f}°C and {f:.2f}°F")

    else:
        print("Invalid unit entered. Please enter Celsius, Fahrenheit, or Kelvin.")

except ValueError as ve:
    print("Error:", ve)
