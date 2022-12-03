            # data structures 
    # data structures 
# data structures 
 #data structures are very useful in collecting, storing and working with more 
 # information than simple strings or integers

                # lists 
# lists are is defined using square brackets it has data separated by a comma
#it can contain all data types

# list example



numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0])
# >>> 1
print(numbers[2])
# >>> 3
print(numbers[-1])  # -1 starts from behind
# >>> 10

                # slice 
#slice eg

print(numbers[:5])   #outputs
[1, 2, 3, 4, 5]

print(numbers[5:])  #outputs
[6, 7, 8, 9, 10]   

print(numbers[0:6])  # u r slicing 0 - 6  but the 6th value is not included it is excluded
[1, 2, 3, 4, 5, 6]

# here is how 
print(numbers[0:1])   # we expect the output to be [1, 2] but the upper index is excluded
[1]
print(numbers[0:2]) 
[1, 2]


# in or not in operators
# in evaluates if an element exists within our list
# not in evaluates if an element does not exist within our list
# this operator return a bool as output

print("this" in "this is a great morning")
# >>> True

print("in" in "this is a great morning")
# >>> true

print("ea" in "this is a great morning")
#>>> true 

print(5 not in [1,2,3,4,5])
# >>> false 

print(6 in [1,2,3,4,5])
# >>> false 

VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V',
        'UNH','WFC', 'CVX', 'BAC', 'JNJ','JPM', 'FB', 'AMZN', 'MSFT', 'AAPL'
        'GOOGL', 'GOOG', 'BRK.B', 'XOM', ]

print('C' in VINIX)  # true
print('gbdg' in VINIX) # false
print('gbg' not in VINIX) # true         (dec 2 ) - if u want to search for a string in
                                                #  large input u can use 'in' as a search tool

# you can replace obleccts in strings1
# eg 
my_lst = [1,2,3,4,5]
my_lst[0] = 'one'
print(my_lst)

# >>> ['one',2,3,4,5]
# in every data type ask yourself if it is MUTABLE OR ORDERD 

# strings are ordered but not mutable 
# they are immutable 

my_string = 'mailu'
print(my_string[1])
# >>> a   

name = "jim"
student = name
name = "tim"
print(name)
#tim
print(student)
#jim 
print(len(student))
#3   
print(max(student))
#m   
print(min(student)) 
#i


        # sorted  data structure
print(sorted(student))  
#['i', 'j', 'm']

# prints string in output in alphabetical order (a-z) or least int to greatest
#eg 

numbers = [1,2,3,4,5,6]
print(sorted(numbers))
#[1, 2, 3, 4, 5, 6]
    
print(max(numbers))
#6


        # join
douse = "-".join(["ab", 'pq', 'rs'])
print(douse)
# ab-pq-rs

# APPEND 

letters = ['a','b','c']
letters.append('z')
print(letters)

#[a,b,c,z]

                # tuples  
#they are immutable but orderd
#in tuples there is no need to add parenthesis []
# eg 

dimensions = 23, 45, 56
length, width, height = dimensions  #unpacking tuples

# eg 2  
tup_a = 1,2
tup_b = (1,2)
print(tup_a == tup_b)
#True
print(tup_a[1])
#2   


                # sets 
# sets are unordered meaning there is none which is in front and another at the back 
# sets are mutable 
# note the paranthesis sets uses [] 
# one application of sets is to quickly remove duplicates from a list 

# sets e.g 

numbers = [1,2,3,5,8,2,4,5,1,3]  
# there are duplicates of the numbers (1,2,3,5)
unique_figs = set(numbers)
print(unique_figs)
# {1, 2, 3, 4, 5, 8}
# the set function removes duplicates

# sets can support the 'in' function 

print(9 in numbers)  # checks if 9 is in the variable numbers
# false

# sets are mutable meaning u can add elements to it 
#You can add elements to sets using the add method
# eg 
unique_figs.add(9)
print(unique_figs)
{1, 2, 3, 4, 5, 8, 9}


                # arithmetics using sets 
a = [1,2,2,3,3,3,4,4,4,4]
b = set(a)
print(len(a) - len(b))
# 6 

            # dictionaries and identity operators 
            # dictionary    (to create dictionaries with ease use zip function(controlflow.py))
# dictionary is mutable  and unorderd

random_dictionary = {'abc':1, 5:"hey"}

# the dictionary above has two keys ('abc') and (5) 
# the dictionary above has 2 values (1)and (hey) 

#   here is a less confusing example 

less_confusing_dictionary = {'cars':7, 'chopper':2}

# {'key':value} 

#note the paranthesis of the dictionaries is {}

# to look for the values in a dictionary use square brackets like below  

print(random_dictionary['abc'])
# 1

# what if i want to look for a value in a key but the key is not present 
# what will be the output , a bool or an error 

# lets check it out, shall we 

print(random_dictionary['boy'])
#error

# to check if an key is in an element use the (in,not in) function or the (get) function 
# eg 
print("boy" in random_dictionary)
# false

# using get 
print(random_dictionary.get('boy'))
#none



# Compound dictionaries 
# this are dictionaries within a dictionary so as to provide for more information 

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

# we can access any element 

helium = elements["helium"]
# get the helium dictionary
#{'number': 2, 'weight': 4.002602, 'symbol': 'He'}

# since dictionaries are mutable u can add an element
#eg

oxygen =  {'number':5,
            'weight':15.999,
            'symbol':'O'}

# how to add to a dictionary 

elements['oxygen'] = oxygen
print(elements)
# {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'}, 
# 'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}, 
# 'oxygen': {'number': 5, 'weight': 15.999, 'symbol': 'O'}}


# data structures test examples

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse)

# question : # split verse into list of words 

# in python you do not need to split the lines manually there is a code for that 
verse_list = verse.split()
print(verse_list)

# the (split) function does the job for you 

# QUESTION ; # convert list to set to get unique words 
# use set 
#because set does not repeat un unique words 
# its output is purely unique words 
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)


 # question 2 

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 

# summary on data structures 

# Data Structure 	Ordered 	Mutable 	Constructor 	Example
# List 	                Yes 	        Yes 	        [ ] or list() 	[5.7, 4, 'yes', 5.7]
# Tuple 	        Yes 	        No 	        ( ) or tuple() 	(5.7, 4, 'yes', 5.7)
# Set 	                No 	        Yes 	        set() 	        {5.7, 4, 'yes'}
# Dictionary 	        No 	        No** 	        { } or dict() 	{'Jun': 75, 'Jul': 89}
