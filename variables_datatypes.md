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

