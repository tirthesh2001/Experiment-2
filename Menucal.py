#Experiment 2
#1) Basic Math Operation
#2) Menud driven with exit condition
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
x = int(input("Enter 1 no: "))
y = int(input("Enter 2 no: "))
print("Select option: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

a=0
while a==0:
    ch=int(input("Enter choice of operation:"))
    if ch in (1,2,3,4,5):	
            if ch ==1:
                print("Addition of the numbers: ",add(x,y))
                a=0	
            elif ch ==2:
                print("Substraction of the numbers: ",sub(x,y))
                a=0	
            elif ch==3:
                print("Multiplication of the numbers: ",mul(x,y))
                a=0
            elif ch==4:
                print("Division of the numbers: ",div(x,y))
            elif ch==5:
                a=1
                break
    else:
	    print("Invalid Input")
	    a=0

