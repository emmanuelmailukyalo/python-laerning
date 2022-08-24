        # zip and enumerate

shop = list(zip(["mercedes-amg", "jeep-wrangler", "jeep-cherokee", "gmc-yukon",],[2e6,4e6,6e6,20e6]))
print (shop)   #it prints outs the dictionary and the details

cars, price = zip(*shop)  # this splits the dict into cars and price
print(cars)  # prints out cars only 

for deals,shop in enumerate(shop):
    print(deals, shop)  # prints out the deals in the shop in an ordely format (run to see output)
