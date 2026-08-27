import math

def Triagle():
    
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    if(a+b)>c and (b+c)>a and (a+c)>b:
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f"The area of the triangle is: {area}")
    else:
        print("Area is not possible.")

Triagle()
