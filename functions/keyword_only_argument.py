## Using Keyword-Only argument in User-Defined Method
def intr(amt,*, rate):
   val = amt*rate/100
   return val
   
interest = intr(1000, rate=10)
print(interest)