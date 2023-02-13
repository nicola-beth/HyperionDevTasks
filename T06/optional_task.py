import math
length_1 = int(input("Enter length of side 1 of the triangle: "))
length_2 = int(input("Enter length of side 2 of the triangle: "))
length_3 = int(input("Enter length of side 3 of the triangle: "))
l = ((length_1+length_2+length_3)/2)
triangle_area = round(math.sqrt(((l)*(l-length_1))*(l-length_2)*(l-length_3)),2)
print(f'The area of your triangle is {triangle_area} units^2')