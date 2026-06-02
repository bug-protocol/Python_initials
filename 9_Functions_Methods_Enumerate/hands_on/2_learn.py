# Function Arguments
# information can be passed into functions as arguments.

def func(name):
    print(name + " is a cool person.")

func("Abhay")
func("Steve")

# parameter => variable declared inside func 
# argument => actual value that is sent to the function.

# Multiple argument
def func2(first_name, last_name):
    print(first_name +" "+ last_name)
func2("Steve", "Harrington")

# Default Argument
# incase no argument is passed
def func3(name = "Steve"):
    print("Hello" + " " + name)

func3()

# Keyword Argument
func2(first_name="Harry", last_name="Potter")