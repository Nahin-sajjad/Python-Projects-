import math
test_h=int(input("Enter the height of the wall: "))
test_w=int(input("Enter the width of the wall: "))

cover=5
def paint_calc(height, width, cover):
    area= height * width
    number_of_cans= math.ceil(area/cover)
    print(f"You'll need {number_of_cans} cans of paint.")
paint_calc(height=test_h, width=test_w, cover=cover)    
