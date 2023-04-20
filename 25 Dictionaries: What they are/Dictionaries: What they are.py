## Dictionaries: What they are

## This set of exercises reviews some things you learned in previous chapters.
## Code the first line of an if statement testing whether the value stored in x is greater or equal to the value stored in y.
x = 1
y = 2

if x >= y:
    print('is greater than')
    
## In a single statement, display the remainder when 9 is divided by 4.
x = 9 % 4
print(x)

## Code the shorthand version of this code:
total = 1
discount = 1

total = total - discount
total =- discount

## x equals 3 times 4 divided by the sum of 5 plus 3. Code it to eliminate ambiguity.
x = (3 * 4) / (5 + 3)
print(x)

## Concatenate the strings stored in two variables and assign the combination to a third variable. Make up all the variable names.
a = 'hello'
b = 'world'
c = a + "" + b
print(c)
print(f"{a} {b}")

## Write the first line that tests whether a equals b and either c is greater than d or e is less than f. Use a pair of parentheses to eliminate ambiguity
d = 1
e = 1
f = 1

if a == b and (c > d or e < f):
    print("")

## In a single line, display "yellowtail" by specifying the list name and index number.
fishes = ["cod", "trout", "yellowtail", "tuna", "salmon"]

print(fishes[2])

## In a single line, add two elements to a list. The elements are numbers. Make up the numbers and the list name.
nums = []
nums = nums + [1, 2]

## Slice "tablet" and "smart watch" from this list and assign the slice to the variable piece.
devices = ["computer", "smart phone", "tablet", "smart watch", "video game console"]

piece = devices[2,4]

## Eliminate "computer" by specifying the element's value.
devices = ["computer", "smart phone", "tablet", "smart watch", "video game console"]
devices.remove('computer')

  
