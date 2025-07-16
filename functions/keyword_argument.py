## Calling Function With Keyword Arguments
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
# by positional arguments
printinfo ("Naveen", 29)

# by keyword arguments
printinfo(name="miki", age = 30)


## Order of Keyword Arguments
def division(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))

division(10,5)
division(5,10)

def division2(num, den):
   quotient = num/den
   print ("num:{} den:{} quotient:{}".format(num, den, quotient))
   
division2(num=10, den=5)
division2(den=5, num=10)