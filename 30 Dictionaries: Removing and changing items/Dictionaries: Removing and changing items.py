## Dictionaries: Removing and changing items

## Eliminate a list element using the element's value, which is "gold". Make up the name of the list.

metals = {'gold': 1}
metals.remove('gold')

## Eliminate a list element using the element's index number. Make up the name of the list and the index number.

del metals[0]

## Complete the code to eliminate the item whose key is "part 355".
maritime_equipment = {'part 355'}
del maritime_equipment['part 355']

## Eliminate the element whose key is "fifth place" from the dictionary winners.
winners = {'one', 'two'}

del winners['fifth place']

## Delete a dictionary item whose key is an integer. Make everything up.
del winners[1]

## Delete a dictionary item whose key is a string. Make everything up.

del winners['one']


## Delete the second item in this dictionary:
numbers = {
  "first": 1,
  "second": 2,
  "third": 3,
  "fourth": 4,
  'five': 5
}
del numbers['second']

## Code a three-item dictionary in five lines of code. Then delete the first item. The keys are numbers. The values are strings. Make everything up.

nums = {
  1: 1,
  2: 2,
  3: 3,
  4: 4,
  5: 4
}

del nums[1]

## Code a three-item dictionary using five lines of code. Then delete the first item. The keys are strings. The values are numbers. Make everything up.

del numbers['first']

''' 
Code a 3-item dictionary.
Delete one of the items.
Display the dictionary.
'''

first_names = {
    'justin': 28,
    'travis': 31,
    'brain': 34
    }

del first_names[1]
print(first_names)

first_names['justin'] = 'emanuel'
print(first_names)