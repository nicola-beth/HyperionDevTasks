import math

building_shape = input("What shape is the building? (square, rectangle or round): ").lower() #user input for shape
building_area = 0 #empty variable for final building area

if building_shape == "square":
    square_length = float(input("What length are the sides of the square?: ")) #user input for sides
    building_area = square_length ** 2 #square area calc.
elif building_shape == "rectangle":
    rectangle_length = float(input("What is the length of the rectangle?: ")) #user input for length
    rectangle_width = float(input("What is the width of the rectangle?: ")) #user input for width
    building_area = rectangle_width * rectangle_length #rectangle area calc.
else:
    circle_radius = float(input("What is the radius of the circle?: ")) #user input for radius
    building_area = math.pi * (circle_radius ** 2) #circle area calc.

print(f"The area of the foundations for the building is {building_area} units squared.")