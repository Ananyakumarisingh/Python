# Functions, Function Arguments and return statement
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

### There are two types of functions:

1. Built-in functions
2. User-defined functions

### Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

### User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

`Syntax:`
```bash
def function_name(parameters):
  pass
  # Code and Statements
```

- Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
- Any parameters and arguments should be placed within the parentheses.
- Rules to naming function are similar to that of naming variables.
- Any statements and other code within the function should be indented.

### Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

`Example:`
```bash
def name(fname, lname):
    print("Hello,", fname, lname)
name("Sam", "Wilson")

Output: Hello, Sam Wilson
```

# Function Arguments
There are four types of arguments that we can provide in a function:

1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments

#### Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

`Example:`
```bash
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
name("Amy")

Output: Hello, Amy Jhon Whatson
```

#### Keyword arguments:
We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

`Example:`
```bash
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Peter", lname = "Wesker", fname = "Jade")

Output: Hello, Jade Peter Wesker
```

#### Required arguments:
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

`Example 1:` when number of arguments passed does not match to the actual function definition.
```bash
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Quill")

Output: name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'lname'
```

`Example 2:` when number of arguments passed matches to the actual function definition.
```bash
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")

Output: Hello, Peter Ego Quill
```

### Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

__Arbitrary Arguments:__
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

`Example:`
```bash
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("James", "Buchanan", "Barnes")

Output: Hello, James Buchanan Barnes
```

__Keyword Arbitrary Arguments:__
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

`Example:`
```bash
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")

Output: Hello, James Buchanan Barnes
```

# return Statement
The return statement is used to return the value of the expression back to the calling function.

`Example:`
```bash
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("James", "Buchanan", "Barnes"))

Output: Hello, James Buchanan Barnes
```
# Enumerate function
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:
```bash
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

The output of this code will be:

0 apple
1 banana
2 mango
```

As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.

### Changing the start index
By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an argument to the enumerate function:
```bash
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

This will output:

1 apple
2 banana
3 mango
```

The enumerate function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:
```bash
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

This will output:

1: apple
2: banana
3: mango
```

In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:
```bash
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
```

And here's an example with a string:
```bash
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
```