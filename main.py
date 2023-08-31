def calculator():
    print("Welcome to the calculator!\n")
    while(True):
        try:
            userInput1 = float(input("Enter the first number: "))
            userInput2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        operation=input("Enter the operation : ")
        while operation not in("+", "-", "*", "/"):
            print("Please enter a valid operation!")
            operation=input("Enter the operation : ")

        if operation=="+":
            print(userInput1+userInput2)
            
        elif operation=="-":
            print(userInput1-userInput2)
       
        elif operation=="*":
            print(userInput1*userInput2)
       
        elif operation=="/":
            if userInput2==0:
                print("Cannot divide by zero!")
                continue
            else:
                print(userInput1/userInput2)

        again=input("Do you want to perform another calculation? ( Y/N ) : ")

        while again.lower() not in("y","n"):
            print("Please enter a valid choice!")
            again=input("Do you want to perform another calculation? ( Y/N ) : ")

        if again.lower()=="y":
            continue
            
        elif again.lower()=="n":
            print("Thank You for using the Calculator. Goodbye!")
            break

calculator()