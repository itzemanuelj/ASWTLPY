## Dictionaries: How to pick information out of them

## Targeting the correct element in the following list, assign "fi" to the variable giant_syllable.
giant_speak = ["fee", "fi", "fo", "fum"]

giant_syllable  = giant_speak[1]

## To target a value in a dictionary, you specify the dictionary name plus the item's _____.
## key

## To target the dictionary item whose key is "age" complete this code:
info = {}
customer_age = info["age"]

## To target the dictionary item whose key is 100 complete this code:
signups = {}
winner_name = signups[100] 

## Target the second item and assign its value to a variable. Make up the variable name.
cust = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
new_cust = cust["last name"]

## Target an item in a dictionary whose key is a string. Assign the item's value to a variable. Make everything up.
names = {"name": "justin", "age": 28}
new_name = names["name"]

x = {"a": "a", "b": "c", "c": "c", " ": " "}

## A dictionary's item key can be a string that contains spaces. Target an item in a dictionary whose key is a string that contains a space. Assign the item's value to a variable. Make everything up.

y = x[""]

## Assign a dictionary item's value to a variable using a key that's a string. Then append that value to a list. Make everything up.
age = info["age"]
##list_of_ages.append(age)

## Assign a dictionary item's value to a variable using a key that's a string. Then create a dictionary that contains only that value. Make everything up, including the key (a string) for the value in the new dictionary.
y = x["a"]
new_dict ={"a": "a"}


## Targeting the second item by its key, assign the second item's value to a variable. Then display the value by specifying the variable.
info = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
new_info = info["last name"]
print(new_info)

## In a single line of code, target the first item and display its value.
crazy = {1: 2, "three": 4, "cat": "dog"}
print(crazy[1])