# here is where i shall do my python coding practises 

# this is a program that add the digits of any two numbers entered 

num = int(input("enter any number that has three digits"))
calc = [int(i) for i in str(num)]
x,y,z = calc
print(x+y+z)


# create a proram that adds the digits of any number entered 
num = int(input("enter any number that has 5 digits"))
calc = [int(i) for i in str(num)]
x,y,z,a,b = calc
print(x+y+z+a+b)

# if number has 2 digits then x+y
# if number has 3 digits the x+y+z
# if number has 4 digits the x+y+z+a
