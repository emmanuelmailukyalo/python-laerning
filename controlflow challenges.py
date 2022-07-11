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
My_lists = [[0,1,2,3] for i in range(2)]
print(My_lists[2][0])


vals = [0,1,2]
vals.insert(0,1)
del vals[1]

My_lists = [3,1,-2]
print(My_lists[My_lists[-1]])

nums = [1,2,3]
vals = nums 
del vals[1:2]
print(nums)
print(vals)

for i in range (1):
    print('#')
else:
     print('#')


My_list = [1,2,3,4]
print(My_list[-3:-2])


z= 10
y = 10
x = y<z and z>y or y>z and z<y 
print(x)


x=1
x=x == x

a =1
b=0
c= a & b
d = a | b
e = a ^ b

print(c+d+e)

i = 0
while 1 <= 3:
    i += 2
    print("*")
