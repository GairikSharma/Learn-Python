#Global variable -> Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

x = 'Great'
def foo():
    print('Python is'+' '+x)
foo()

# If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

y='Great'
def foo1():
    y='Awsome'
    print('Python is'+' '+y)
foo1()
print('Python is'+' '+y)

# Normally, when you create a variable inside a function, that variable is local, 
# and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def foo3():
    global z
    z='Python'
    # print('Js is better than'+' '+z) -> z can be used outside of the function
foo3()
print('Js is better than'+' '+z)



z='Py'
def foo3():
    global z
    z='Python'
    # print('Js is better than'+' '+z) -> z can be used outside of the function
foo3()
print('Js is better than'+' '+z)