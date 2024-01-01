print('Hi')

print('c', end='')
print('d')
print('e')
print('f', end="  ")
print('g')
print('h')

# use case of end
print('Loading:', end='')
# Some loading logic
print(' 50%', end='')
# More loading logic
print(' 100%')

# Escape Sequence

# \n: Newline character. Moves the cursor to the beginning of the next line.
print('Hi I am first\nand Hi I am second') # This is the first line.

# \t: Tab character. Inserts a horizontal tab.
print("This is the first line.\nThis is the second line.") # This is the second line.


# \\: Backslash character. Used to include a literal backslash in a string.
print("This is a\ttabbed\tline.") # This is a    tabbed  line.


# \': Single quote character. Used to include a literal single quote in a single-quoted string.
print("He said, \"Don't do that!\"") # He said, "Don't do that!"


# \": Double quote character. Used to include a literal double quote in a double-quoted string.
print('C:\\path\\to\\file') # C:\path\to\file

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


com = complex(2, -1)
print(com)

fruit = "Mango"
fruitLen = len(fruit)
print(fruit[0:len(fruit)]) # Mango
print(fruit[:5]) # [0 : 5]   Mango
print(fruit[:]) # [0 : len(fruit)]   Mango
print(fruit[1:4]) # ago
print(fruit[0:-3]) # [0 : len(fruit)-3]    Ma
print(fruit[-1:-3]) # [-1 : len(fruit)-3]   [4:2]   
print(fruit[-3:-1]) # [-3 : len(fruit)-1]   [2:4]   ng
print(fruit[:1]) # [0:1]   M

# Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())


x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")
    
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

for k in range(5):
  print(k + 1)
  
# for k in range(1, 20001):
#   print(k)

  
for k in range(1, 12, 3):
  print(k)