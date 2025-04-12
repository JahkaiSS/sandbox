import math

def area(shape, p1, p2):
    a = 0
    if shape == "rect"  :
        print("Area = length × width")
        l = p1
        w = p2
        a = l * w
    if shape == "square":
        print("Area = a²")
        side = p1
        a = side ** 2
    if shape == "circle":
        print("Area = π × r²")
        radius = p1
        a = math.pi * radius ** 2
    if shape == "triangle":
        print("Area = ½ × base × height")
        base = p1
        height = p2
        a = 0.5 * base * height
        
    return a


