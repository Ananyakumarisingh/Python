# Condition
### if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:

- if
- if-else
- if-else-elif
- nested if-else-elif.

#### An if……else statement evaluates like this:
__if the expression evaluates True:__
Execute the block of code inside if statement. After execution return to the code out of the if……else block.

__if the expression evaluates False:__
Execute the block of code inside else statement. After execution return to the code out of the if……else block.

`Example:`
```bash
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

Output: Alexa, do not add Apples to the cart.
```

### elif Statements
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

Working of an elif statement
Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
.
.
.
Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

`Example:`
```bash
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")

Output: Number is Zero.
```

### Nested if statements
We can use if, if-else, elif statements inside other if statements as well.
`Example:`
```bash
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

Output: Number is between 11-20
```

## else in Loop
As you have learned before, the else clause is used along with the if statement.

Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

`Syntax`
```bash
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block

Example:
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

Output: iteration no 1 in for loop
        iteration no 2 in for loop
        iteration no 3 in for loop
        iteration no 4 in for loop
        iteration no 5 in for loop
        else block in loop
        Out of loop
```

## If ... Else in One Line
There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:
```bash
a = 2
b = 330
print("A") if a > b else print("B")
```
You can also have multiple else statements on the same line:

__One line if else statement, with 3 conditions:__
`Example`
```bash
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```
__Another Example__
```bash
result = value_if_true if condition else value_if_false
```
This syntax is equivalent to the following if-else statement:

```bash
if condition:
    result = value_if_true
else:
    result = value_if_false
```

### Conclusion
The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full if-else syntax.

## Exception Handling
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

### Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

### Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

`Syntax:`
```bash
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception

Example:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

Output: Enter an integer: 6.022
        Number entered is not an integer.
```

### Finally Clause
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

`Syntax:`
```bash
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
```

The finally block is executed irrespective of the outcome of try……except…..else blocks
One of the important use cases of finally block is in a function which returns a value.

`Example:`
```bash
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

Output1: Enter an integer: 19
         Integer Accepted.
         This block is always executed.

Output2: Enter an integer: 3.142
         Number entered is not an integer.
         This block is always executed.
```
