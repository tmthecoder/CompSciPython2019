"""
Name: Tejas Mehta
Date: October 17th, 2019
Lab Name: Lab2-Methods
Extra: Added fahrenheit to celsius
"""


# Method to find perimeter of rectangle(2l + 2w)
def perimeter(l, w):
    return 2 * l + 2 * w


# Method to find area of trapezoid(b1+b2 * h / 2)
def area_trapezoid(b1, b2, h):
    return ((b1 + b2) * h) / 2


# find volume of a cone
def volume(r, h):
    return (3.14159 * (r * r) * h) / 3


# surface area for a cube
def surface_area(s):
    return s * s * 6


# Get the area of a circle
def area_circle(r):
    return 3.14159 * r * r


# Find the slope of a line
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


# convert fahrenheit to celsius
def convert_to_c(f):
    return ((f - 32) * 5) / 9


# convert celsius to fahrenheit
def convert_to_f(c):
    return ((c * 9) / 5) + 32


print("Perimeter of a rectangle:")
print (perimeter(12, 5))
print (perimeter(131, 75))
print (perimeter(20, 25))
print (perimeter(9, 256))
print (perimeter(36, 72))
print (perimeter(8, 6))
print (perimeter(18, 16))
print("Area of a trapezoid:")
print("{0:.1f}".format(area_trapezoid(3, 3, 3)))
print("{0:.1f}".format(area_trapezoid(5, 6, 7)))
print("{0:.1f}".format(area_trapezoid(7, 10, 6)))
print("{0:.1f}".format(area_trapezoid(13, 9, 3)))
print("{0:.1f}".format(area_trapezoid(6, 11, 4)))
print("{0:.1f}".format(area_trapezoid(11, 8, 5)))
print("Volume of a cone:")
print("{0:.2f}".format(volume(4, 4)))
print("{0:.2f}".format(volume(4, 3)))
print("{0:.2f}".format(volume(9, 3)))
print("{0:.2f}".format(volume(1, 3)))
print("{0:.2f}".format(volume(1, 5)))
print("{0:.2f}".format(volume(7, 7)))
print("{0:.2f}".format(volume(1.5, 3)))
print("{0:.2f}".format(volume(1.5, 5)))
print("Surface area of a cube:")
print("{0:.1f}".format(surface_area(112)))
print("{0:.1f}".format(surface_area(4)))
print("{0:.1f}".format(surface_area(33)))
print("{0:.1f}".format(surface_area(50)))
print("{0:.1f}".format(surface_area(5)))
print("{0:.1f}".format(surface_area(19)))
print("{0:.1f}".format(surface_area(111)))
print("Area of a circle: ")
print("{0:.1f}".format(area_circle(7.5)))
print("{0:.1f}".format(area_circle(10)))
print("{0:.1f}".format(area_circle(72.534)))
print("{0:.1f}".format(area_circle(55)))
print("{0:.1f}".format(area_circle(101)))
print("{0:.1f}".format(area_circle(99.952)))
print("{0:.1f}".format(area_circle(100)))
print("Slope of a lime:")
print("{0:.2f}".format(slope(1, 9, 14, 2)))
print("{0:.2f}".format(slope(1, 7, 18, 3)))
print("{0:.2f}".format(slope(6, 4, 2, 2)))
print("{0:.2f}".format(slope(4, 4, 5, 3)))
print("{0:.2f}".format(slope(1, 1, 2, 9)))
print("{0:.2f}".format(slope(1, 7, 2, 9)))
print("Fahrenheit to Celsius")
print("{0:.2f}".format(convert_to_c(98.6)) + " degrees celsius")
print("{0:.2f}".format(convert_to_c(52.3)) + " degrees celsius")
print("{0:.2f}".format(convert_to_c(82.45)) + " degrees celsius")
print("{0:.2f}".format(convert_to_c(75)) + " degrees celsius")
print("{0:.2f}".format(convert_to_c(100)) + " degrees celsius")
print("Celsius to Fahrenheit")
print("{0:.2f}".format(convert_to_f(0)) + " degrees fahrenheit")
print("{0:.2f}".format(convert_to_f(100)) + " degrees fahrenheit")
