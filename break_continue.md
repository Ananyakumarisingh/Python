# break statement
The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

`Example`
```bash
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

Output: 1 Mississippi
        2 Mississippi
        3 Mississippi
        4 Mississippi
        5 Mississippi
        .
        .
        .
        50 Mississippi
```

# Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.

`Example`
```bash
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

Output: 2
        4
        6
        8
        0
```

