# Get inputs from user
weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

# Calculate height and weight to metric measures
height_meters = height * 0.0254
weight_kilograms = weight * 0.453592

#Calculate the BMI
bmi =  weight / (height ** 2)* 703

# Using the round function to round the BMI value to 1 decimal
bmi = round(bmi, 2)
print(f"BMI: {bmi:.1f}")
