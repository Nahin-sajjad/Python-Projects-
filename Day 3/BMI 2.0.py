weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))

Bmi= round(weight/(height**2))

if Bmi<18.5:
    print(f"Your BMI is {Bmi}.You are underweight")
elif Bmi<25:
    print(f"Your BMI is {Bmi}.You are normal weight")
elif Bmi<30:
    print(f"Your BMI is {Bmi}.You are slightly overweight")    
elif Bmi<35:
    print(f"Your BMI is {Bmi}.You are obese")
else:
    print(f"Your BMI is {Bmi}.You are clinically obese")    
    
        
        
    

