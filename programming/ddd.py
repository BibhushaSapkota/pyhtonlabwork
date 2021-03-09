#solve each of the following problems using python scripts. make sure you use appropriate variable names and comments
#. when there is a final answer have python print it to the screen.
#A person's body mass index(BMI) is defined as :
#BMI = mass in kg/(height in m)**2
mass=float(input("enter your mass in kg"))
height=float(input("enter your height in meter "))
BMI=mass/(height**2)
print("the BMI is", BMI)
if (BMI<18.5):
    print("underweight")
elif (BMI>= 18.5 and BMI<24.9):
    print("healthy")
elif (BMI>=24.9 and BMI<30):
    print("overweight")
else:
    print("obese")