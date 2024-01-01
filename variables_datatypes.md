# Variables, Data Types and Operators

### What is a variable?
Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

```bash
# These are four variables of different data types.
a = 1
b = True
c = "Harry"
d = None
```

### What is a Data Type?
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:

```bash
a = 1
print(type(a))
b = "1"
print(type(b))
```

### By default, python provides the following built-in data types:
__1. Numeric data: int, float, complex__
- int: 3, -8, 0
- float: 7.349, -9.0, 0.0000001
- complex: 6 + 2i

__2. Text data: str__
- str: "Hello World!!!", "Python Programming"

__3. Boolean data:__
- Boolean data consists of values True or False.

__4. Sequenced data: list, tuple__
- __list:__ A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

`Example:`
```bash
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

Output: [8, 2.3, [-4, 5], ['apple', 'banana']]
```

__Tuple:__ A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

`Example:`
```bash
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

Output: (('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

__5. Mapped data: dict__

__dict:__ A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

__Example:__
```bash
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)

Output: {'name': 'Sakshi', 'age': 20, 'canVote': True}
```

### Operators
Python has different types of operators for different operations. To create a calculator we require arithmetic operators.

__Arithmetic operators__
| Operator  | Operator Name  | Example |
| :------ | :------ | :------ |
| + | Addition | 15+7 |
| -	| Subtraction | 15-7 |
| * |	Multiplication	| 5*7 |
| ** | Exponential | 5**3 |
| / | Division | 5/3 |
| % | Modulus | 15%7 |
| // | Floor Division | 15//7 |


#### Exercise
```bash
n = 15
m = 7
ans1 = n+m
print("Addition of",n,"and",m,"is", ans1)
ans2 = n-m
print("Subtraction of",n,"and",m,"is", ans2)
ans3 = n*m
print("Multiplication of",n,"and",m,"is", ans3)
ans4 = n/m
print("Division of",n,"and",m,"is", ans4)
ans5 = n%m
print("Modulus of",n,"and",m,"is", ans5)
ans6 = n//m
print("Floor Division of",n,"and",m,"is", ans6)
```

#### Explaination
Here 'n' and 'm' are two variables in which the integer value is being stored. Variables 'ans1' , 'ans2' ,'ans3', 'ans4','ans5' and 'ans6' contains the outputs corresponding to addition, subtraction,multiplication, division, modulus and floor division respectively.

# local and global variables
Before we dive into the differences between local and global variables, let's first recall what a variable is in Python.

A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator =. For example:
```bash
x = 5
y = "Hello, World!"
```
Now, let's talk about local and global variables.


A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.

Here's an example to help clarify the difference:
```bash
x = 10 # global variable
def my_function():
  y = 5 # local variable
  print(y)
my_function()
print(x)
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
```

In this example, we have a global variable x and a local variable y. We can access the value of the global variable x from within the function, but we cannot access the value of the local variable y outside of the function.

The global keyword
Now, what if we want to modify a global variable from within a function? This is where the global keyword comes in.

The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope. Here's an example:
```bash
x = 10 # global variable
def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable
my_function()
print(x) # prints 5
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
```

In this example, we used the global keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is changed to 5.

It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.

I hope this tutorial has helped clarify the differences between local and global variables and how to use the global keyword in Python. Thank you for watching!