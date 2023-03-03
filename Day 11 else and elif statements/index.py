# else and elif statements
species = "cat"

# complete this code set

if species == "cat":
    print("Yep, it's cat.")
else:
    print("Nope, not cat.")


# If the condition tested in line 1 fails, line 3 tests for a different condition. 
# What keyword goes in the blank?

donut_condition = "high"
donut_price = 10

if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0   

# Code the next line that says what to do if the test fails.

a = 1
b = 2

if a == b:
    print("a equals b")
else:
    print("a !== b")

# Code the next line. If a doesn't equal b, test whether c equals d.

a = 1
b = 2
c = 3
d = 4

if a == b:
   print("a equals b")
elif c == d:


# Code four lines. If a equals b, c equals d. If the test fails, e equals f.

if a == b:
    c = d
else:
  e = f