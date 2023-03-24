age=input("enter your age: ")

age_left=90-int(age)

age_in_days=int(age_left)*365

age_in_weeks=int(age_left)*52

age_in_months=int(age_left)*12

print(f"you have {age_in_days} days, {age_in_weeks} weeks, and {age_in_months} months left.")