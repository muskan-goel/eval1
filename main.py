
import div
import sub
import multiply
a=int(input("first no. "))
b=int(input("second no. "))
print("divide- ")
print("sub- ")
print("multiply- ")


#CALCULATOR
import sub
import multiply
import Add
import div
print("calculator")
print("1.Add \n2.Division \n3.Multiply \n4.Subtract")


def switch():

    a = int(input("enter first number"))
    b = int(input("enter second number"))
    option = int(input("choose the desired operation "))
    if option == 1:
       print(Add.add(a,b))
    if option == 2:
        print(div.divide(a,b))
    if option == 3:
        print(multiply.multiply(a, b))
    if option == 4:
        print(sub.sub(a, b))
while(True):
 switch()

