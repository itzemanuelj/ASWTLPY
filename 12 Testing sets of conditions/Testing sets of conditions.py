# Testing sets of conditions

# You're testing whether both conditions are true. Fill in the blank.
a = 1
b = 2
c = 3
d = 4

if a == b == c == d:
    print("true")
    

# You're testing whether either condition is true. Fill in the blank.

if a == b != c == d:
    print("false")
    
# Code a line that tests whether the variable city is "London" or "Tel Aviv."

city = "London"

if city == "London" or city == "Tel Aviv":
    print("city is equal to london")
    
# Code a line that tests whether the variable total is 10 or 20.

total = 10

if total == 10:
    print("total is equal to")
    

# If the variable first_name is "Isaac" and the variable last_name is "Newton" display "Thanks!"

first_name = "Isaac"
last_name = "Newton"

if first_name == "Isaac" & last_name == "Newton":
    print("thanks")
    
# if x is smaller or equal to 5 or y is greater or equal to 10 display "yes".

x = 1
y = 2

if x <= 5 or y >= 10:
    print("yes")

# If the variable animal is "dog", "cat", or "mouse" display "mammal".

animal = "dog"

if animal == "dog" or animal == "cat" or animal == "mouse":
    print("mammal")


# If the variable nationality is "UK" and either the variable age is under 21 or it's over 64 display "qualified"

nationality = "UK"
age = 21
    
if nationality == "UK" and (age < 21 or age > 64):
    print("qualified")
  
# If the variable age is greater than or equal to 21 or the variable permission is "ok" display a message of your choice.

permission = "ok"
if age >= 21 or permission == "ok":
    print("ok")
    
# Code one line. If a equals b and c equals d, the test passes. Alternately, if e equals f or g equals h, the test passes. You could use elif to accomplish this, but don't. Use a combination of and, or, and parentheses.

e = 1
f = 2
g = 3
h = 4

if (a == b and c == d) or (e == f or g == h):
    print("test passes")    

# If 2 equals 3 or 3 doesn't equal 4, display ok

if 2 == 3 or 3 != 4:
    print("ok")
    
# If 1 plus 1 equals 2 and 2 plus 2 equals 4, display ok
if 1 + 1 == 2 and 2 + 2 == 4:
    print("ok")





