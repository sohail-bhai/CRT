'''
try:
    a=int(input("Enter number: "))
    print(10/a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
    
    
pdb commandds :
l - list nearby code
n - execute next line
s - step into function
c - to continue execution until next breakpoint
p variable_name - print variable value
r - return from current function
q - quit debugger
help - list all commands
'''
import pdb 
def add(a,b):
    pdb.set_trace()
    return a+b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))   
print("Sum is:",add(a,b))
