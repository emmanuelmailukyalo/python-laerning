# data structures 

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
print('gbg' not in VINIX) # true

# you can replace obleccts in strings1
# eg 
my_lst = [1,2,3,4,5]
my_lst[0] = 'one'
print(my_lst)

# >>> ['one',2,3,4,5]
