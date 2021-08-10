def get_numbers():
    num1 = float(input("First number:"))
    num2 = float(input("Second number:"))

def sum_2(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("Invalid input, try again")

def subtract_2(num1, num2):
    try:
        num1 = float(input("First number:"))
        num2 = float(input("Second number:"))
        print(num1 - num2)
    except:
        print("Invalid input, try again")

#def multiply_2():
