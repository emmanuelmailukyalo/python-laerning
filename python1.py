
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
