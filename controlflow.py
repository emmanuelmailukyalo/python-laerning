            # conditional statements 
        # if statements 

phone_balance = 3
bank_balance = 100

print(phone_balance, bank_balance)

# write a statement that when the phone balnce is below 5 , 
# some money (1$) is removed from the bank

if phone_balance < 5:
    bank_balance -= 10  #use equal to assign the outcome as the new value 
    phone_balance += 10 

    print(phone_balance, bank_balance)
    # 13, 90



# Practice: Which Prize

# Write an if statement that lets a competitor know which of these prizes they won based on 
# the number of points they scored, which is stored in the integer variable points.
# Points 	Prize
# 1 - 50 	wooden rabbit
# 51 - 150 	no prize
# 151 - 180 	wafer-thin mint
# 181 - 200 	penguin

# All of the lower and upper bounds here are inclusive, and points can only take on positive
#  integer values up to 200.

# In your if statement, assign the result variable to a string holding the appropriate message
# based on the value of points. If they've won a prize, the message should state 
# "Congratulations! You won a [prize name]!" with the prize name. 
# If there's no prize, the message should state "Oh dear, no prize this time."
