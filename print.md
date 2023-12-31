# Comments, Escape sequence & Print in Python

### Python Comments
A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

### Single-Line Comments:
To write a comment just add a ‘#’ at the start of the line.

`Example 1`
```bash
#This is a 'Single-Line Comment'
print("This is a print statement.")

Output: This is a print statement.
```

`Example 2`
```bash
print("Hello World !!!") #Printing Hello World

Output: Hello World !!!
```

`Example 3:`
```bash
print("Python Program")
#print("Python Program")

Output: Python Program
```

### Multi-Line Comments:
To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

`Example 1:` The use of ‘#’.
```bash
#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

Output: p is greater than 5.
```

`Example 2:` The use of multiline string.
```bash
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

Output: p is greater than 5.
```

### Escape Sequence Characters
To insert characters that cannot be directly used in a string, we use an escape sequence character.

An escape sequence character is a backslash \ followed by the character you want to insert.

An `example` of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
```bash
print("This doesnt "execute") ❌
print("This will \"execute\"") ✅
```

### More on Print statement
The syntax of a print statement looks something like this: __print(object(s), sep=separator, end=end, file=file, flush=flush)__

#### Other Parameters of Print Statement
- object(s): Any object, and as many as you like. Will be converted to string before printed

`Example:`
```bash
print("Hi,", 7, "is my lucky number.", "What's yours?", sep="~", end="hihihi")
print(" hihihi!")

Output: Hi,~7~is my lucky number.~What's yours? hihihi!
```
- sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '

`Example:`
```bash
print("Hi,", 7, "is my lucky number.", "What's yours?", sep="~")

Output: Hi,~7~is my lucky number.~What's yours?
```
- end='end': Specify what to print at the end. Default is '\n' (line feed)

`Example:`
```bash
print("Hi,", 7, "is my lucky number.", end="")
print(" What's yours?")

Output: Hi, 7 is my lucky number. What's yours?

print("Hi,", 7, "is my lucky number.", end=" 1212\n")
print(" What's yours?")

Output: Hi, 7 is my lucky number. 1212
         What's yours?


print("Hi,", 7, "is my lucky number.", end=" ")
print("What's yours?")

Output: Hi, 7 is my lucky number. What's yours?

```
- file: An object with a write method. Default is sys.stdout

`Example:`
```bash
with open("output.txt", "w") as file:
    print("This line goes to a file.", file=file)

Output: This line goes to a file.   # In output.txt
```
- flush=True: forces the output to be flushed, which can be useful in situations where you want to ensure that the printed content is immediately visible, even if the program is still running.

`Example:`
```bash
import time

print("Loading", end='')
time.sleep(1)  # Simulating some time-consuming operation
print("...", end='', flush=True)
time.sleep(1)
print(" Complete!")

Output: Loading...
        Loading... Complete! # after 1 second
```

#### Timestamp
```bash
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

Output: 08:34:54
        08
        34
        54
```
