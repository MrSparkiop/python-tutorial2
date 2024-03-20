# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2
# Може да не използваме горния метод или горния или долния
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)