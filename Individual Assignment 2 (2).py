# Getting the input
temperature = float(input("Enter the temperature in Fahrenheit: "))

# Processing temperature in celcius
temperature_celsius = (temperature - 32) * 5/9

print('Temperature in Celcius:',round(temperature_celsius,1))

# I am starting with an if statement for the first solution
if temperature <= 0:
    print("Water is ice")
elif temperature >= 0 and temperature <= 100:
    print("Water is liquid")
else:
    print('Water is gas')
