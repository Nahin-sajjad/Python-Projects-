student_height=input("Input a list of student heights ").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

total_height=0
number_of_students=0
for height in student_height:
    total_height += height
for i in student_height:
    number_of_students += 1
average = round(total_height/number_of_students)

print(average)    
