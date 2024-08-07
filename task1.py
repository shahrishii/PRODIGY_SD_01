def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Conversion Program")
    print("Choose the unit of measurement for the input temperature:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    choice = input("Enter the number corresponding to the unit (1, 2, or 3): ")

    if choice not in ('1', '2', '3'):
        print("Invalid choice! Please select 1, 2, or 3.")
        return
    
    temp = float(input("Enter the temperature value: "))
    
    if choice == '1':
        # Celsius
        celsius = temp
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F and {kelvin:.2f}K")
    
    elif choice == '2':
        # Fahrenheit
        fahrenheit = temp
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit:.2f}°F is equivalent to {celsius:.2f}°C and {kelvin:.2f}K")
    
    elif choice == '3':
        # Kelvin
        kelvin = temp
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin:.2f}K is equivalent to {celsius:.2f}°C and {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
