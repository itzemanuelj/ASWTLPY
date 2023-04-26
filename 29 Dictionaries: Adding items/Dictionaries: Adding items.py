## Dictionaries: Adding items

## Code an empty list. Make up the list name.
empty_list = []

## Code an empty dictionary. Make up the dictionary name.
empty_dict = {}

## The dictionary name is ranks. Add an item to it. The key is 10. The value is "Spain".
ranks = {}

ranks[10] = 'Spain'

## The dictionary name is products. Add an item to it. The key is "laptop". The value is 397.50.

products = {}
products['laptop'] = 397.50

## Add a string element to a list, using the plus sign. Make up the string and the list name.

empty_list += ["item"]
print(empty_list)

## Add an item to a dictionary. The key is a number. The value is a string. Make everything up.

empty_dict[0] = 'item 1'

##Add two elements to a list using the plus sign. The elements are numbers. Make everything up.

empty_list = ['item 2'] + ['item 3']

## Add two items to a dictionary. All keys and values are strings. Make everything up.

empty_dict['key'] = 'item'
empty_dict['key'] = 'item2'

## Add a string to the end of a list using the append keyword. Make up the list name and the string.

empty_list.append('item last')
print(empty_list)

prices = {
  "ethanol": 1.531,
  "natural gas": 2.892,
  "gasoline": 1.5646,
}

##Add an item to the dictionary. The key is "gold". The value is 1281. Targeting the gold item in the dictionary, display gold's price.

prices['gold'] = 1281
print(prices['gold'])

## Code a dictionary with three items. Then add a fourth item to the dictionary. Display the complete dictionary.

my_dict = {
    'key1': 'one',
    'key2': 'two',
    'key3': 'three'
}
my_dict['key4'] = 'four'

print(my_dict)