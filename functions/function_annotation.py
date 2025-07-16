## Function Annotations
def myfunction(a: int, b: int):
   c = a+b
   return c
   
print (myfunction(10,20))
print (myfunction("Hello ", "Python"))


## Function Annotations With Return Type
def myfunction(a: int, b: int) -> int:
   c = a+b
   return c
print(myfunction(56,88))
print(myfunction.__annotations__)


## Function Annotations With Expression
def total(x : 'marks in Physics', y: 'marks in chemistry'):
   return x+y
print(total(86, 88))
print(total.__annotations__)


## Function Annotations With Default Arguments
def myfunction(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction(10))

def myfunction2(a: "physics", b:"Maths" = 20) -> int:
   c = a+b
   return c
print (myfunction2.__annotations__)

def myfunction3(*args: "arbitrary args", **kwargs: "arbitrary keyword args") -> int:
   pass
print (myfunction3.__annotations__)

def division(num: dict(type=float, msg='numerator'), den: dict(type=float, msg='denominator')) -> float:
   return num/den
print (division.__annotations__)