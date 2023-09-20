print("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
n=int(input("enter number from 1 to 4 according to your choice:"))
if (n==1):
    x=int(input("enter 1st number to add:"))
    y=int(input("enter 2nd number to add:"))
    z=x+y
    print("addition of two numbers is:",z)
elif(n==2):
    x=int(input("enter 1st number to subtract:"))
    y=int(input("enter 2nd number to subtract:"))
    z=x-y
    print("subtraction of two numbers is:",z)
elif(n==3):
    x=int(input("enter 1st number to multiply:"))
    y=int(input("enter 2nd number to multiply:"))
    z=x*y
    print("multiplication of two numbers is:",z)
elif(n==4):
    x=int(input("enter 1st number to divide:"))
    y=int(input("enter 2nd number to divide:"))
    z=x/y
    print("division of two numbers is:",z)

else:
    print("please enter coreect option")
