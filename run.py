num = int(input("enter any number that has three digits"))
calc = [int(i) for i in str(num)]
x,y,z = calc
print(x+y+z)


# create a proram that adds the digits of any number entered 
num = int(input("enter any number that has three digits"))
calc = [int(i) for i in str(num)]
x,y,z,a,b = calc
print(x+y+z+a+b)



# python exercises 

string = '''Twinkle, twinkle, little star,\n        How I wonder what you are!\n 
               Up above the world so high,\n
               Like a diamond in the sky. 
Twinkle, twinkle, little star,\n
                How I wonder what you are'''

# use the triple quotes to write a multiline sentence 


#  Write  a Python program which accepts the radius of a circle 
# from the user and compute the area.

radius = float (input("write the radius of the circle"))

# formula for area of a circle is 22/7 * radius*radius  
print (3.142857142857143* (radius**2))



# Write a Python program to display the first and last colors 
# from the following list. Go to the editor
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
first_color = (color_list[0])
last_color = (color_list[-1])
print (first_color,"and", last_color)


# Write a Python program to display the first and last colors 
#  that are input by a user 

colors = str(input("enter at least 4 of ur fav colors you can add more according to ur liking"))
colors = colors.split()
print(colors[0], colors[-1])
