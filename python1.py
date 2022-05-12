
# arithmetic operators
    # + Addition
    # - Subtraction
    # * Multiplication
    # / Division
    # % Mod (the remainder after dividing)
    # ** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
    # // Divides and rounds down to the nearest integer

# variables
    # Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or underscore.
    # You can’t use reserved words or built-in identifiers
    # use lowercase letters and underscores to separate words 

   


    mv_population=6000
    # 400 moved away out of mv 
    mv_population=6000-400
    print(mv_population)

    # this statement will lead to an error because this is not 
    # html and css.

    # for this statement to work you must assign an assignment operator
    # to display it new value. 

    # like so 
    mv_population= 7000
    mv_population= mv_population + 6000-400
    print(mv_population)

    # this will work 
    # but there is a better and easier way using assignment operators 
    # instead of reapeting mv_population again use an assignment operator 
    # += which shows we r increasing the variable in the left with the right 

    # eg
    mv_population= 7000
    mv_population += 6000-400
    print(mv_population)

    
    # assignment operators example using rainfall in a water reservoir
       
        # The current volume of a water reservoir (in cubic metres)
        reservoir_volume = 4.445e8
        # The amount of rainfall from a storm (in cubic metres)
        rainfall = 5e6

        # decrease the rainfall variable by 10% to account for runoff
        rainfall *= 0.9
        # add the rainfall variable to the reservoir_volume variable
        reservoir_volume += rainfall
        # increase reservoir_volume by 5% to account for stormwater that flows
        # into the reservoir in the days following the storm
        reservoir_volume *= 1.05
        # decrease reservoir_volume by 5% to account for evaporation
        reservoir_volume *= .95
        # subtract 2.5e5 cubic metres from reservoir_volume to account for water
        # that's piped to arid regions.
        reservoir_volume -= 2.5e5
        # print the new value of the reservoir_volume variable
        print(reservoir_volume)

    # Changing Variable Values
    
    # intergers and floats
    # int is a whole numbers
    # while float is a decimal number

     x= int(4.7)   # since 4.7 is not an interger it will be made to be an int resulting to it being (4) 
     y= float(4)

     print(x)
     print(type(x))   # to check the type
     #output results to
     #int

     print(y)  #print an in (4.0)
     print(type(y)) # prints type which is (class 'float')

    #  data types

    #  float
    #  integer
    #  boolean
    #  string
    comparison operators and  logical operators

    # # boolean 
    # true
    # false
    # # comparison operators
    # != not equal to
    # == equal to
    # >  greater than
    # <  less than
    # <= less than or equal to
    # >=  greater than or equal to
    # # logical operators 
    # (and) if both sides are true
    # (or) if one side is true
    # (not) flips the bool value

    # boolean comparison operators and  logical operators example

    age = 14
    is_teen = age >12 and age <20
    print(is_teen)


# Write code to compare these densities. Is the population of San Francisco more dense than that 
# of Rio de Janeiro? Print True if it is and False if not.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise
sf_population = 864816
sf_area = 231.89
rio_population = 6453682
rio_area = 486.5

san_francisco_pop_density = sf_population/sf_area
print(san_francisco_pop_density)
3729.423433524516
rio_de_janeiro_pop_density = rio_population/rio_area
print(rio_de_janeiro_pop_density)
13265.533401849949
denser_city = 3729.423433524516 < 13265.53340184994
print(denser_city)

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print (True)
else:
    print (False)
    

# string 
# len     is an inbuilt function to show the length of a string 

# eg 

my_name = mailu
print(len(my_name))
# ouput = 5

# you difine string by using a single or double quotes 

# to ignore a quote in a string use back slash (\) 
# eg 

simon = "simons\'s bike"  # if we use the single quotes python will close the string
print(simon)
# ouput = simon's bike 

#how to add a space between text

firstword = "hello"
secondword = "world"
print(firstword + ' ' + secondword)   # the (' ') single quotations reps a space

coconut_count = "34"
mango_count = "15"
tfc = coconut_count + mango_count
print(tfc)


    #  float
    #  integer
    #  boolean
    #  string

    #u can know which type a value is by using inbuilt function (type)
    # eg 

    print(type(633))  #<class 'int'>
    print(type("633"))  #<class 'str'>

    # Calculate and print the total sales for the week from 
    # the data provided. Print out a string of the form 
    # "This week's total sales: xxx", where xxx will be 
    # the actual total of all the numbers. You’ll need 
    # to change the type of the input data in order to 
    # calculate that total.

    mon_sales = "121"
    tues_sales = "105"
    wed_sales = "110"
    thurs_sales = "98"
    fri_sales = "95"  

    #TODO: Print a string with this format: This week's total sales: xxx
    # You will probably need to write some lines of code before the print statement.
    weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
    weekly_sales = str(weekly_sales)  #convert the type back!!
    print("This week's total sales: " + weekly_sales)
    
    # /n (n is for a new line) 

    # Python offers another mechanism for the passing of 
    # arguments, which can be helpful when you want to 
    # convince the print() function to change its behavior a bit. 

    # keyword arguments 
    
    # a keyword argument consists of three elements: a keyword identifying the argument (end here); 
    # an equal sign (=); and a value assigned to that argument;
    # any keyword arguments have to be put after the last positional argument (this is very important)

    # Keyword arguments are the ones whose meaning is not dictated by their location, but by a 
    # special word (keyword) used to identify them.

    # the end parameter specifies what to print at the end of the print statement.
    # if i want to write to print functions but i dant want them to be in two line i use "END" 
    # END Eg.
    print("My name is ")
    print("Monty Python.")
    #out put
    #>>> my name is
    #>>> monty python

    # end 
    print("My name is ", end="")
    print("Monty Python.")
    #output
    #>>> my name is Monty python.
    # end is used to change the behaviour of the print 
    # by hindering the code to create a new line 

    # here is another examole to show the exact work of end keyword arguments 
    print("My name is ", end="  ")
    print("Monty Python.")
    #>>> My name is   Monty Python
    #note the double spaces in the end argument
    #it pushes away the next output in the function 


    # keyword arguments
    #sep
    #sep for separotor

    print("My", "name", "is", "Monty", sep="-")
    #>>> My-name-is-Monty
    
    #note that the value assigned to that argument will determine what separates the txts
    #eg 
    print("My", "name", "is", "Monty", sep="!")
    #>>> My!name!is!Monty
    #we used period as the value assigned to the argument
    
    # Both keyword arguments may be mixed in one invocation, just like here below.

    print("My", "name", "is", sep="_", end="*")
    print("Monty", "Python.", sep="*", end="*")


#challenge 
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


# Try to:

#     minimize the number of print() function invocations by inserting the \n sequence into the strings
#     make the arrow twice as large (but keep the proportions)
#     duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using
#     the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
#     remove any of the quotes, and look carefully at Python's response; pay attention to where Python 
#     sees an error - is this the place where the error really exists?
#     do the same with some of the parentheses;
#     change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
#     replace some of the quotes with apostrophes; watch what happens carefully.
