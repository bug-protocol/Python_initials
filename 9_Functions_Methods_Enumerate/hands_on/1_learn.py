#Python Functions

# block of code which only runs when called
# can return data as result
# helps in achieving modularity in code

# Function creation
# created using def keyword

def my_function():
  print("Hello from a function")

my_function()

# Function naming conventions
# use _ or any character at the beginning also
# functions are case sensitive => myFunction and myfunction are different

# Return values

def func():
  return ("Call func!!")

message = func()
print(message)

# pass statement

# function can't remain undefined. Use pass statement to skip that particular part.
def func2():
  pass
func2()