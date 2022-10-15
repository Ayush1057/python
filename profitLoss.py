a = int(input("Enter cost price "))
b = int(input("Enter selling price "))

if a<b:
    x = b-a
    print("You got profit of",x,"!!!")
else:
    x = a-b
    print("You got loss of",x,"!!!")
