#
#system: Simple Calculator
#author:Nathan Vik
#functionality:
# sum, subtract, multiply, divide
#

#imports
from display import print_menu

#global variables


# functions

def message():
    try:
        msg = input("Type your Message:") + "\n"
        num = int(input("Number of times to repeat:"))
        print(msg*num)
    except:
            print("Invalid input, try again")

            
# plain instructions
opt = ""
while(opt != "x"):
    error = False

    print_menu()

    opt = input("Choose an option:")
    if(opt == "x"):
        break
    elif(opt == "5"):
        message()
    else:
        try:
            num1 = float(input("First number:"))
            num2 = float(input("Second number:"))

        except:
            error = True
            print("Invalid input, try again")

        if(not error):    
            if(opt == "1"):
                print(f"The Result is: {num1 + num2}")
            elif(opt == "2"):
                print(f"The Result is: {num1 - num2}")
            elif(opt == "3"):
                print(f"The Result is: {num1 * num2}")
            elif(opt == "4"):
                if(num2 == 0):
                    print("Can't divide by 0!")
                else:
                    print(f"The Result is: {num1 / num2}")
    
    input("Press Enter to Continue")


print("Goodbye!")