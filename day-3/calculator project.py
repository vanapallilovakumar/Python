def add (a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiplication (a,b):
    return a * b
def division (a,b):
    return a == b
    return "division is by zero is not possible."
    return a / b

while True:
    print("\n-----simple Calculator-----")
    print("1. addition (+)")
    print("2.subtraction(-)")
    print("3.multiplication(*)")
    print("4.division(/)")
    print("5.exit")

    choice=input("Enter your choice (1-5):")

    if choice == "5" :
         print("thank you!!")
         break

    if choice in ["1", "2", "3" ,"4"]:

        num1=float(input("Enter your first number : "))
        num2=float(input("Enter your second number: "))
    if choice =="1":
        print("result: add (num1, num2:")
    elif choice =="2":
        print=("result: subtract (num1, num2:)")
    elif choice =="3":
        print=("result: multiplication (num1, num2:)")
    elif choice =="4":
        print("result: division (num1, num2)")
    elif choice =="5":
         print=("result=exit!")
    else :
           print("invalid error!!")

