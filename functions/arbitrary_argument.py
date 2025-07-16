## Arbitrary Arguments
# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)



## Required Arguments With Arbitrary Arguments
#avg of first test and best of following tests
def avg(first, *rest):
   second=max(rest)
   return (first+second)/2
   
result=avg(40,30,50,25)
print (result)



## Arbitrary Keyword Arguments (**kwargs)
def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")



## Multiple Arguments With Arbitrary Keyword Arguments
def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)