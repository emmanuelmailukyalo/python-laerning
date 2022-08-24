# zip 

name = ["pear", "mango"]
size  = [2,6]
1
shop = (list(zip(name, size)))
print(shop)

fruit, quantity = zip(*shop)
print(fruit)
print(quantity)
