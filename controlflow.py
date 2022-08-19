            # conditional statements 
        # if statements 




from ast import If
from doctest import set_unittest_reportflags
from optparse import Values
from subprocess import STARTF_USESHOWWINDOW


phone_balance = 3
bank_balance = 100

print(phone_balance, bank_balance)

# write a statement that when the phone balnce is below 5 , 
# some money (1$) is removed from the bank

if phone_balance < 5:
    bank_balance -= 10  #use equal to assign the outcome as the new value 
    phone_balance += 10 

    print(phone_balance, bank_balance)
    # 13, 90



# Practice: Which Prize 

# Write an if statement that lets a competitor know which of these prizes they won based on 
# the number of points they scored, which is stored in the integer variable points.
# Points 	Prize
# 1 - 50 	wooden rabbit
# 51 - 150 	no prize
# 151 - 180 	wafer-thin mint
# 181 - 200 	penguin

# All of the lower and upper bounds here are inclusive, and points can only take on positive
#  integer values up to 200.

# In your if statement, assign the result variable to a string holding the appropriate message
# based on the value of points. If they've won a prize, the message should state 
# "Congratulations! You won a [prize name]!" with the prize name. 
# If there's no prize, the message should state "Oh dear, no prize this time."

points = 174

# write your if statement here

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"


print(result)

#guess my number example
# # another elif Example
# You decide you want to play a game where you are hiding a number from someone.
# Store this number in a variable called 'answer'. Another user provides 
# a number called 'guess'. By comparing 'guess' to 'answer',
# you inform the user if their guess is too high or too low.

answer = 8
guess = 3

if guess <= 5:
    result = "Oops!  Your guess was too low."
elif guess > 8:
    result = "Oops!  Your guess was too high."
elif guess == 8:
    result = "Nice!  Your guess matched the answer!"

print(result)


# Quiz: Tax Purchase

# Depending on where an individual is from we need to tax them appropriately. 
# The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively. 
# Use this information to take the amount of a purchase and the corresponding 
# state to assure that they are taxed by the right amount.

state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)


print(result)

# kiasi 
weather =  "mvua"

if weather == "mvua":
    print("kuna nyesha")
else :
    print ("kuna jua")


# Write a program to check whether a person is eligible for voting or not.
#  (accept age from user)

age = 32

if age >= 18:
    print("you are eligible to vote")
else:
    print("not eligible to vote")


# Write a program to check whether a number entered by user is even or odd or divisible by 5. 
number = 3

if number %2==0:
    print("number is even")
elif number %5==0:
    print("number is divisible by 5")
else:
    print("number is odd")

# Write a program to check whether a number is divisible by 7 or not. 
number = 14 

if number %7==0:
    print("divisible by seven")
else:
    print("not divisible by 7")

#  Write a program to calculate the electricity bill (accept number of unit from user)
#   according to the following criteria :

#      Unit                                                       Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

total_bill = 0
electricity_bill = 150

if electricity_bill >= 100:
    total_bill= 0
# elif electricity_bill >= 200:
#     total_bill=(electricity_bill*5)
else:
    total_bill=(electricity_bill*10)

print(total_bill)


# write a program to accept percentage from the user and 
# display the grade according to the following criteria:

#          Marks                                    Grade
#          > 90                                         A
#          > 80 and <= 90                               B
#          >= 60 and <= 80                              C
#          below 60                                     D

grade = 79

if grade >= 91:
    print("A")
elif grade > 80 and grade <= 90:
    print("B")
elif grade >= 60 and grade <=80:
    print("C")
elif grade <=59:
    print("D")


# nested if statements 

weather = "good"
restaurant = "closed"

if weather == "good":
    if restaurant == "opened":
        print("go for lunch")
    else:
        print("eat_sandwich")
else:
   print(" stay_at_home")

# identify the larger of 3 numbers:

number_1 = 5
number_2 = 3
number_3 = 7

largest_number = number_1 

if number_1 > number_2:
    largest_number = number_2

if largest_number < number_3:
    largest_number = number_3

print("largest number is:", largest_number)



# question example  

# As you surely know, due to some astronomical reasons, years may be leap or common. 
# The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule 
# is used to determine the kind of year:

#     if the year number isn't divisible by four, it's a common year;
#     otherwise, if the year number isn't divisible by 100, it's a leap year;
#     otherwise, if the year number isn't divisible by 400, it's a common year;
#     otherwise, it's a leap year.

# Look at the code in the editor - it only reads a year number, and needs to be 
# completed with the instructions implementing the test we've just described.

# The code should output one of two possible messages, which are Leap year or 
# Common year, depending on the value entered.

# It would be good to verify if the entered year falls into the Gregorian era, 
# and output a warning otherwise: Not within the Gregorian calendar period. 

# Tip: use the != and % operators.

# Test your code using the data we've provided.


year = 2000

	
if year < 1582:
    print("Not within the Gregorian calendar period")
elif year%4!=0:
    print("common year")
elif year%100!=0:
    print("leap year")
elif year%400!=0:
    print("common year")
else:
    print("leap year")

    
        # for loop 

# for loop example 

# Practice: Quick Brown Fox

# Use a for loop to take a list and print each element of the list in its own line. 

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for text in sentence:
    print(text, end="\n")

    # output 
# the
# quick
# brown
# fox
# jumped
# over
# the
# lazy
# dog

# Practice: Multiples of 5

# Write a for loop below that will print out every whole number 
# that is a multiple of 5 and less than or equal to 30.

for i in range(5,31,5):
    print(i, end="\n")

#     # output
# 5
# 10
# 15
# 20
# 25
# 30

#  Create Usernames

# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces 
# with underscores. Running your for loop over the list:

# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should print out the usernames list:

# ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

# HINT: Use the .replace() method to replace the spaces with underscores. 


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)




# Quiz: Modify Usernames with Range

# Write a for loop that uses range() to iterate over the positions in 
# usernames to modify the list. Like you did in the previous quiz, 
# change each name to be lowercase and replace spaces with underscores. 
# After running your loop, this list

# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should change to this:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")

print(usernames)



# Quiz: Tag Counter

# Write a for loop that iterates over a list of strings, tokens, 
# and counts how many of them are XML tags. XML is a data language similar to HTML. 
# You can tell if a string is an XML tag if it begins with a left angle bracket 
# "<" and ends with a right angle bracket ">". 
# Keep track of the number of tags using the variable count.

# You can assume that the list of strings will not contain empty strings.


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

# Quiz: Create an HTML List

# Write some code, including a for loop, that iterates over a list of strings 
# and creates a single string, html_str, which is an HTML list. 
# For example, 
# if the list is items = ['first string', 'second string']
# printing html_str should output:

        # <ul>
        # <li>first string</li>
        # <li>second string</li>
        # </ul>

# That is, the string's first line should be the opening tag <ul>. 
# Following that is one line per element in the source list, 
# surrounded by <li> and </li> tags. The final line of the string should be 
# the closing tag </ul>.


items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)


# quiz make the colors list to become lower case

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(color.lower())

print(lower_colors)

            # counter dictionary 


book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock',
                'holmes','the','great','gasby','hamlet','adventures','of',
                'huckleberry','fin']

# create an empty dictionary  called word-counter

word_counter = {}

# Iterate through each element in the list. If an element is already included
# in the dictionary, add 1 to its value. If not, add the element to the dictionary
#  and set its value to 1.


for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# output
# {'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 
# 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}

# to get the key of a value in a dictionary use 

print(word_counter['great'])

# output
# 2

# or use the get function to do the same 
print(word_counter.get('great'))

# using for loop in dictionaries

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for key in cast:
    print(key)


# output
# Jerry Seinfeld
# Julia Louis-Dreyfus
# Jason Alexander
# Michael Richards

# note this example only prints out the keys and not the values
# yet the dictiolnary has both 

#if u want ur output to remove both the keys and values
# If you wish to iterate through both keys and values, 
# you can use the built-in method (items) like this:

for key, values in cast.items():
    print(key,values)

# output 
# Jerry Seinfeld Jerry Seinfeld
# Julia Louis-Dreyfus Elaine Benes
# Jason Alexander George Costanza
# Michael Richards Cosmo Kramer

# lets format the output so that it could make sense 
# since both the keys and values are both strings 
#it could be different to differentiate  what is key and what is value
# we shall use the format function to perform the task

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# this outputs 
# Actor: Jerry Seinfeld    Role: Jerry Seinfeld
# Actor: Julia Louis-Dreyfus    Role: Elaine Benes
# Actor: Jason Alexander    Role: George Costanza
# Actor: Michael Richards    Role: Cosmo Kramer

# i want to convert a list to a dictionary and merge it into a dictionary 
# the problem is that the dictionary is already defined 
# it has keys and values but the list doesn't have values only keys 

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

fruits.extend(basket_items)
fruits = {
            'pears':1,
            'peaches':1,
            'grapes':1,
            'bananas':1,
            'apples': 4,
            'oranges': 19,
            'kites': 3,
            'sandwiches': 8
         }
print(fruits)


# output 
{'pears': 1, 'peaches': 1, 'grapes': 1, 'bananas': 1, 
'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8} 

# use the get function to get the key of sandwiches 

print(fruits.get('sandwiches'))


# warming up 

# iterations 
# while loop 

# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)


# number we'll find the factorial of
number = 6
# start with our product equal to one
product = 1

# calculate factorial of number with a for loop
for num in range(2, number + 1):
    product *= num

# print the factorial of number
print(product)



# create a program that gives the multiplication of the number by 1- 10

number = int(input("enter a number :"))

count = 1 
while count <= 10:
    print(number, "x",count, "=", product)
    count += 1


# Write a while loop that finds the largest square number less than an integer 
# limit and stores it in a variable nearest_square. A square number is the product
#  of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
