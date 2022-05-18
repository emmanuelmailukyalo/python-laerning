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
