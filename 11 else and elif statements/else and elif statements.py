# else and elif statements

species = "cat"

if species == "cat":
  print("Yep, it's cat.")
else:
  print("Nope, not cat.")

# If the condition tested in line 1 fails, line 3 tests for a different condition. What keyword goes in the blank?

buy_score = 1
donut_condition = "fresh"
donut_price = "10"

if donut_condition == "fresh":
  buy_score = 10
elif donut_price == "low":
  buy_score = 5
else:
  buy_score = 0   

# Code the next line that says what to do if the test fails.

a = 1
b = 1

if a == b:
  print("a equals b")
else: 
  print("a doesnt equal b")

# Code the next line. If a doesn't equal b, test whether c equals d.

c = 2
d = 3

if a == b:
  print("a equals b")
elif a != b:
  print("a != b")
else:
  c != d

# Code four lines. If a equals b, c equals d. If the test fails, e equals f.

e = 4
f = 5

if a == b:
  c = d
else:
  e = f

# Code four lines. If a equals b, c equals d. If that test fails, then if e equals f, g equals h

g = 6
h = 7

if a == b :
    c == d
elif e == f:
    g == h

# What is the value of x?
if 2 + 3 == 4:      # 2 + 3 = 5 == 4 no
  x = 0             # so !== =
elif 2 - 1 == 1:     # 2 - 1 = 1 == 1 yes
  x = 1             # x = 1 yes
elif 3 + 3 == 6:  # else if not excuteded because a previos value is correct
  x = 2
else:
  x = 3

# x is equal to 1

# Code the next two lines. If the test fails, test if a equals 2. If so, display "a equals 2".

if a == 1:
  print("a equals 1")
else :
  a == 2
  print("a equals 2")   

# Code the next two lines. If the first two tests fail, display "failed".

if a == b:
  print("ok")
elif c == d:
  print("ok")
else:
  print("failed")



