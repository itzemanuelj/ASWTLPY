# if statement nested

# Translate this into nested ifs:

#if a == b and c == d:

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
x = 9
y = 10

if a == c:
    if c == d:
        print()           

# Translate this into a four-line if and elif:
if a == b or c == d:
    print("ok")  

if a == b:
    print("ok")
elif c == d:
    print("also ok")    

# If both the first and second test don't pass, something else happens. Write the next line.
if a == b:
    if c == d:
        e == f
    else:
        print()

# Rewrite the second line so it's legal.
if a == b:
    if c == d:
        g = h

# If a equals b and if c equals d, e equals f. Code all three lines using nesting.

if a == b:
    if c == d:
        if e == f:
            print("")

# Translate this into two lines with the second line nested:
if a == b:
    if c == d:
        print("")

# Translate this into three lines using nesting:
if a == 1: 
    if b == 2: 
        if c == 3:
            print("")

# Translate this into four lines using nesting:
if a == 1: 
    if b == 2: 
        if c == 3:
            d = 6
            print("")

# Translate this using nesting.
if a == b and (c == d or e == f):
    if g == h:
        print("")

# or

if a == b:
    if c == d:
        g = h
    elif e == f:
        g = h

# If the first test succeeds but the nested test fails, 
# code a second nested test for whether a is not equal to b. 
# Don't forget to indent it.
if c == d:
    if x == y:
        g = h        
elif a != b:
    print()

# Rewrite this code using a nested if statement.
if 1 + 1 == 2 and 2 + 2 == 4:
    print("ok")

if 1 + 1 == 2:
    if 2 + 2 == 4:
        print("ok")

# Rewrite the code in the box on the right using a nested if statement and nested elif statement.

if 1 == 1 and (2 == 3 or 4 == 4):
  print("ok")

if 1 == 1:
    if 2 == 3:
        print("ok")
    elif 4 == 4:
        print("ok")