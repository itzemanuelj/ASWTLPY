## for loops nested

## How many times will the if statement run? Answer with a numeral.
chosen_letter = "b"
letter_list = ["a", "b", "c", "d", "e", "f"]
for a_letter in letter_list:
  if a_letter == chosen_letter:
    print("It's a match.")
    break

## 2


## The next line interrupts the loop when there's a match. Code it. Remember to indent 2 tabs.
chosen_letter = "b"
letter_list = ["a", "b", "c", "d", "e", "f"]
for a_letter in letter_list:
  if a_letter == chosen_letter:
    print("It's a match.")
    break

## Code the first line of a for loop. The list name is letter_list. The variable name is a_letter.

for a_letter in letter_list:
    if a_letter == letter_list:
        print("")

## Code the first line of a loop that runs inside this loop. The list name is b and the variable name is a. Don't forget to indent.
a = 1
b = 2
x = 1
y = 2

for x in y:
    for a in b:
        print("")

## Code the first line of a for loop, and then the first line of an inner loop. Make up all the names. Don't forget to indent the second line.
for x in y:
    for a in b:
        print("")
        
## Code the first line of a for loop, then the first and second lines of an inner loop. The second line of the inner loop displays the element in the inner list. Make up the names. Remember to indent line 2 1 tab and line 3 2 tabs.

nums = [1,2,3,4,5]
my_num =[5]

for a_num in nums:
    if my_num == a_num:
        print("your number is 5")


## Code the first line of a for loop. The list name is letter_list. The variable name is a_letter.
for a_letter in letter_list:
    for a_letter in letter_list:
        print()

## Run an inner loop inside an outer loop. If the inner list contains an element with the value of 1, display "ok". Remember to indent correctly.

for a in b:
    for x in y:
        if c == 1:
            print("ok")


## Run an inner loop inside an outer loop. If the inner list contains an element less than 1, display "ok" and interrupt the loop. Remember to indent correctly.

date = 1

for a in b:
    for x in y:
        if date < 1:
            print("ok")
            break
## Code three lines: the first line of an outer loop, then the first line of a loop that runs inside the outer loop, and finally the first line of a loop that runs inside the first inner loop. This is about indenting correctly.

c = 1 
d = 2

for a in b:
    for x in y:
        for c in d:
            print("ok")     
            break

## When the looping completes, what number will display? Answer with a numeral. Hint: After the outer loop has run once through one country and the inner loop has run once through four cities, outer_loop_total + inner_loop_total is 5.

outer_loop_total = 0
inner_loop_total = 0
countries = ["Albania", "Morocco", "Brazil", "Denmark"]
capitals = ["Tel Aviv", "Abuja", "Brasília", "Islamabad"]
for country_to_check in countries:
  outer_loop_total += 1
  for city_to_check in capitals:
    inner_loop_total += 1
    if country_to_check == "Brazil" and city_to_check == "Brasília":
      print(outer_loop_total + inner_loop_total)
      
## 14

## Code an outer loop that loops through the first list and an innner loop that loops through the second list. The inner loop displays each inner list value.
a = 1
c = 2
b = [1, 2, 3, 4, 5, 6]
d = [7, 8, 9, 10, 11]

for a in b:
    for b in c:
        print("")
        
## Code nested for loops. When the outer tuple element is 4 and the inner tuple element is "b" display "ok"
