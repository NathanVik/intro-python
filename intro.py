print("Hello from Python")

#variables and variable types

name = "Nathan"
print(name)

age = 32
total = 19.99
found = True

print(age, total, found)

print(name + name) #str + str concatenation
print(1 + age) # sum

print(name + str(age)) #can parse int to str and will work

if(age < 100):
    print("you are still young")
    print("another line inside the if")
elif(age == 100):
    print("you are on the very edge")
else:
    print("Sorry, you're just old")

print("this line is outside the if statement")


def test():             #Define a function
    print("Hello, I'm a test")

test()                  #Call the function
test()