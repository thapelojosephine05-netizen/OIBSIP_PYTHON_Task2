weight=float(input("what is your weight in kilograms ?"))
height=float(input("what is your height in meters ?"))
BMI= (weight/(height*height))
BMI=round(BMI,2)
if BMI < 18.5:
    print("Your BMI is", BMI, "therefore you are underweight")

elif 18.5 <= BMI <= 24.9:
    print("Your BMI is", BMI, "therefore you have normal weight")

elif 25.0 <= BMI <= 29.9:
    print("Your BMI is", BMI, "therefore you are overweight")

else:
    print("Your BMI is", BMI, "therefore you are obese")

