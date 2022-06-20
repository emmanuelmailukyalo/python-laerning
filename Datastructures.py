# data structures 

                # lists 
# lists are is defined using square brackets it has data separated by a comma
#it can contain all data types

# list example
from distutils.log import error


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
print('gbg' not in VINIX) # true

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

    numbers = [1,2,3,4,5,6]
    print(sorted(numbers))
#[1, 2, 3, 4, 5, 6]
    
    print(max(numbers))
#6


        # join
name = "-".join(["ab", 'pq', 'rs'])
print(name)
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
            # dictionary  
# dictionary is mutable  and unorderd

random_dictionary = {'abc':1, 5:"hey"}

# the dictionary above has two keys ('abc') and (5) 
# the dictionary above has 2 values (1)and (hey) 

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
