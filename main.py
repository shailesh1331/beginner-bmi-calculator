height=float(input("Enter your height in meters:\n"))
weight=float(input("Enter your weight in kgs:\n"))
bmi=(weight/(height*height)).__round__(2)
print(bmi)