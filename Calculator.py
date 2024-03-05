def add(a,b):
    result = a+b
    print (f"{a} + {b} = {result}")
def subtract(a,b):
    result = a-b
    print (f"{a} - {b} = {result}")
def multiply(a,b):
    result = a*b
    print (f"{a} * {b} = {result}")
def divide(a,b):
    if(b==0):
       print("float division by zero")
       print (f"{a} / {b} = None")
    else:
        result = a/b
        print (f"{a} / {b} = {result}")
def power(a,b):
    result = a**b
    print (f"{a} ^ {b} = {result}")
def remainder(a,b):
    result = a%b
    print (f"{a} % {b} = {result}")

def select_op(choice):
    
    if choice=="+":
        try:
            op1=input("Enter first number: ")
            if "$" in op1:
                print(op1)
                return 0
            elif "#" in op1:
                print(op1)
                return -1
            else:
                print(int(op1))
                    
            op2=input("Enter second number: ")
            if("$" in op2):
                print(op2)
                return 0
            elif "#" in op2:
                print(op2)
                return -1
            else:
                print(int(op2))
                add(float(op1),float(op2))
            if("#" in op1 or "#" in op2):
                return -1
        except:
            pass
        
    elif choice=="-":
        try:
            op1=input("Enter first number: ")
            if "$" in op1:
                print(op1)
                return 0
            elif "#" in op1:
                print(op1)
                return -1
            else:
                print(int(op1))
                    
            op2=input("Enter second number: ")
            if("$" in op2):
                print(op2)
                return 0
            elif "#" in op2:
                print(op2)
                return -1
            else:
                print(int(op2))
                subtract(float(op1),float(op2))
            if("#" in op1 or "#" in op2):
                return -1
        except:
            pass
    elif choice=="*":
        try:
            op1=input("Enter first number: ")
            if "$" in op1:
                print(op1)
                return 0
            elif "#" in op1:
                print(op1)
                return -1
            else:
                print(int(op1))
                    
            op2=input("Enter second number: ")
            if("$" in op2):
                print(op2)
                return 0
            elif "#" in op2:
                print(op2)
                return -1
            else:
                print(int(op2))
                multiply(float(op1),float(op2))
            if("#" in op1 or "#" in op2):
                return -1
        except:
            pass
    elif choice=="/":
        try:
            op1=input("Enter first number: ")
            if "$" in op1:
                print(op1)
                return 0
            elif "#" in op1:
                print(op1)
                return -1
            else:
                print(int(op1))
                    
            op2=input("Enter second number: ")
            if("$" in op2):
                print(op2)
                return 0
            elif "#" in op2:
                print(op2)
                return -1
            else:
                print(int(op2))
                divide(float(op1),float(op2))
            if("#" in op1 or "#" in op2):
                return -1
        except:
            pass
    elif choice=="^":
        try:
            op1=input("Enter first number: ")
            if "$" in op1:
                print(op1)
                return 0
            elif "#" in op1:
                print(op1)
                return -1
            else:
                print(int(op1))
                    
            op2=input("Enter second number: ")
            if("$" in op2):
                print(op2)
                return 0
            elif "#" in op2:
                print(op2)
                return -1
            else:
                print(int(op2))
                power(float(op1),float(op2))
            if("#" in op1 or "#" in op2):
                return -1
        except:
            pass
    elif choice=="%":
        try:
            op1=input("Enter first number: ")
            if "$" in op1:
                print(op1)
                return 0
            elif "#" in op1:
                print(op1)
                return -1
            else:
                print(int(op1))
                    
            op2=input("Enter second number: ")
            if("$" in op2):
                print(op2)
                return 0
            elif "#" in op2:
                print(op2)
                return -1
            else:
                print(int(op2))
                remainder(float(op1),float(op2))
            if("#" in op1 or "#" in op2):
                return -1
        except:
            pass
    elif choice=="#":
        return -1
    elif choice=="$":
        return 0
    else:
        return "Unrecognized operation"
#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")


  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()