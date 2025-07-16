## Python Modules
import math
print ("Square root of 100:", math.sqrt(100))


## Creating a Python Module
import mymodule
mymodule.SayHello("Harish")

import mymodule
print ("sum:",mymodule.sum(10,20))
print ("average:",mymodule.average(10,20))
print ("power:",mymodule.power(10, 2))


## The from ... import Statement
from mymodule import sum, average
print ("sum:",sum(10,20))
print ("average:",average(10,20))


## The from...import * Statement
from modname import *


## The import ... as Statement
import mymodule as x
print ("sum:",x.sum(10,20))
print ("average:", x.average(10,20))
print ("power:", x.power(10, 2))