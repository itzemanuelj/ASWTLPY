## Lists: popping elements

## To strike an element off a list and assign it to a variable, what keyword do you use?

names = []

names.pop('')

## Fill in the blank to pop the third element off the list.
big_list = []

popped_element = big_list.pop(2)

## Complete the code to pop the first element off the list.

popped_element = big_list.pop(0)

## Pop the second element off the list y and assign it to the variable x.

x = []
y = []

x = y.pop(1)
print(y)

## Pop an element off a list and assign it to a variable. Make everything up.

teams = ['michihgan', 'ohio' , 'chicago']

new_teams = teams.pop(1)
print(teams)

## Pop the first element of list y and append it to the end of list x.

x = []
y = []

x.append(y.pop(0))

## Pop the fourth element of list y and insert it as the third element of list x.

x.insert(2, y.pop(3))

## Using minimal code, pop the last element off list y and assign it to the variable x.

x = y.pop()

## x equals 100 plus the sixth element popped off list y. Code it in a single statement.
x = 100 + y.pop(5)

## Using the keywords append and pop, move the first element of the list x to the end of list x.

x.append(x.pop(0))

## Pop the fourth element of y and assign it to x. Then display x.

y = [5, 11, 8, 2, 44]

x = y.pop(3)
print(x) ## 2

print(y) ## [5, 11, 8, 44]

hoppers = ["rabbit", "hare", "bunny", "cottontail"]
pets = ["dog", "cat", "fish"]

## Pop "bunny" off the hoppers list and append it to the pets list. Then display the pets list.

pets.append(hoppers.pop(2)) 
print(pets)