# Primitive Variables
num = 23
# print(type(num))
str = "Hello World!"
# print(type(str))
double = 1.5
# print(type(double))
comp = 3.14j
# print(type(comp))
bool = False
# print(type(bool))
none = None
# print(type(none))

# Conversion
intConv = int(double)

# Non-primitive Variables
# List Data Type
lst = [2023, "Python", 3.11, 5+6j, 1.23E-4]
# Tuple Data Type
tple = (2023, "Python", 3.11, 5+6j, 1.23E-4)
# Range Data Type
rnge = range(5)
# Dictionary Data Type
dict = {1:'one', 2:'two', 3:'three'}
# Set Data Type
setVar = {2023, "Python", 3.11, 5+6j, 1.23E-4}

# Bytes Data Type
b1 = bytes([65, 66, 67, 68, 69])
b2 = b'Hello'

# ByteArray Data Type
ba1 = bytearray([72, 101, 108, 108, 111])
ba2 = bytearray("Hello", 'utf-8')

# Memoryview Data Type
data = bytearray(b'Hello, world!')
view = memoryview(data)

# if, elif, and else
if num == double:
  ifVar = num + double
elif num == double and double != comp:
  elifVar = double + comp
else:
  elseVar = comp

# match
match num:
  case 1:
    num = 1
  case 2:
    num = 2
  case _: "Invalid input"

# for else
for count in range(6):
   print ("Iteration no. {}".format(count))
else:
   print ("for loop over. Now in else block")
print ("End of for loop")

# while
count=0
while count < 5:
   count += 1
   print ("Iteration no. {}".format(count))

print ("End of while loop")

# break
for letter in 'Python':    
   if letter == 'h':
      break
   print ("Current Letter :", letter)
print ("Good bye!")

# continue
for letter in 'Python':
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
print ("Good bye!")

# pass
for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)
print ("Good bye!")