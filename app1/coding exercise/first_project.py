import random
"""Program returns a random number that falls between the two whole numbers 
    entered by the user
"""
user_lower = int(input("Enter a lower bound: "))
user_upper = int(input("Enter a upper bound: "))

random_num = random.randint(user_lower, user_upper)
print(random_num)
