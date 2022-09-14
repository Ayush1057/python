# IF_ELSE Practice~~

# 1
""" 
m = int(input("enter the value of m : "))

if m>0:
    n = 1
    print(n)

elif m==0:
    n = 1
    print(n)

else:
    n = 1
    print(n)
"""
#2
""" 
a = int(input("Enter first number "))
b = int(input("Enter second number "))
c = int(input("Enter third number "))

if (a>b) and (a>c):
    print(a,"is greater")
elif (b>a) and (b>c):
    print(b,"is greater")
else:
    print(c,"is greater")
"""

#3
""" 
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))

if (x>0) and (y>0):
    print(x,"and",y,"is in First Quadrant")
elif (x<0) and (y>0):
    print(x,"and",y,"is in Second Quadrant")
elif (x<0) and (y<0):
    print(x,"and",y,"is in Third Quadrant")
else:
    print(x,"and",y,"is in Fourth Quadrant")
"""

#4
""" 
x = int(input("1st side of traingle "))
y = int(input("2nd side of traingle "))
z = int(input("3rd side of traingle "))

if x==y==z:
    print("Equilateral Triangle")
elif x==y>z or y==z>x or z==x>y:
    print("Isosceles Triangle")
else:
    print("Scalane Triangle")
"""

#5
""" 
x = input("Enter the charachter ")

if x == 'a' or x == 'A':
    print(x,"is vovel")
elif x == 'e' or x == 'E':
    print(x,"is vovel")
elif x == 'i' or x == 'I':
    print(x,"is vovel")
elif x == 'o' or x == 'O':
    print(x,"is vovel")
elif x == 'u' or x == 'U':
    print(x,"is vovel")
else:
    print(x,"is consonent")
"""

#6
""" 
a = int(input("Enter first angle "))
b = int(input("Enter second angle "))
c = int(input("Enter third angle "))

if a+b+c==180:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
"""

#7

a = int(input("Enter cost price "))
b = int(input("Enter selling price "))

if a<b:
    x = b-a
    print("You got profit of",x,"!!!")
else:
    x = a-b
    print("You got loss of",x,"!!!")