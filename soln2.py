

# Question 2(i)

# Define a function named calculate_bmi that takes a person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
def calclate_bmi(weight,height):
    BIM = weight/height
    if weight <=18.5:
        print("Underweight")
    elif 18.5<= weight <=24.9:
        print("Normal weight")
    elif 25<= weight <=29.9:
        print("Over weight")
    else:
        print("Obese")
weight = float(input("\n Enter weight in kg"))
height = float(input("\n enter your height in m"))
calclate_bmi(weight, height )
# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real pie value (import math)
def volume_of_a_cylinder(r,h):
    import math 
    pie = math.pi
    volume = pie *r**2*h
    print(f"The volume of the syphere with radius{r} is {volume:.2f}" )
r = int(input("\n Enter the radius"))
h = int(input("/n Enter the height "))
volume_of_a_cylinder(r,h)