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
