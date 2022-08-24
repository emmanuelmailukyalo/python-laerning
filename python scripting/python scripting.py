# zip 

shop = list(zip(["mercedes-amg", "jeep-wrangler", "jeep-cherokee", "gmc-yukon",],[2e6,4e6,6e6,20e6]))
print (shop)
cars, price = zip(*shop)
print(cars)  
for deals,shop in enumerate(shop):
    print(deals, shop)
