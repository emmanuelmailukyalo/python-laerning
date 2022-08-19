
# create a program that gives the multiplication of the number by 1- 10

number = int(input("enter a number :"))

count = 1 
while count <= 10:
    product = number * count 
    print(number, "x",count, "=", product)
    count += 1
