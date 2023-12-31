# Match Case Statements and Loop
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements. If this is your first language, dont worry as I will tell you everything you need to know about match case statements in this video!

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

1. The match keyword
2. One or more case clauses
3. Expression for each case

_The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches._

`Syntax:`
```bash
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n
```

`Example:`
```bash
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)

Output: x % 2 == 0 and case is 4
```

# Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

- for loop
- while loop

### The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

`Example:` __iterating over a string:__
```bash
name = 'Abhishek'
for i in name:
    print(i, end=", ")

Output: A, b, h, i, s, h, e, k,
```

`Example:` __iterating over a list:__
```bash
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

Output: Red
        Green
        Blue
        Yellow
```
_Similarly, we can use loops for lists, sets and dictionaries._

#### range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

`Example:`
```bash
for k in range(5):
    print(k)

Output: 0
        1
        2
        3
        4
```
_Here, we can see that the loop starts from 0 by default and increments at each iteration._

But we can also loop over a specific range.

`Example:`
```bash
for k in range(4,9):
    print(k)

Output: 4
        5
        6
        7
        8
```
#### Quick Quiz
Explore about third parameter of range (ie range(x, y, z))

## while Loop
As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

`Example:`
```bash
count = 5
while (count > 0):
  print(count)
  count = count - 1

Output: 5
        4
        3
        2
        1
```
_Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever._

### Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

`Example:`
```bash
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

Output: 5
        4
        3
        2
        1
        counter is 0
```
### Do-While loop in python
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

### How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

`Example:`
```bash
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break

Output Enter a positive number: 1
        1
        Enter a positive number: 4
        4
        Enter a positive number: -1
        -1
```
### Explanation
This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.
