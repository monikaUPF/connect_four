import sys
#from user import User
from config import Token, User
from game import Grid

# Welcome message
print("==========")
print("Connect 4")
print("==========\n")

print("This is an interactive version of the traditional game CONNECT FOUR.\n")
print("Confidentiality NOTE: the system is not keeping any personal data from you.\n")
print("You are free to provide real, fake or no personal data at all:")
print("It does not affect the game's performance.")

print("---------------------\n")

# User set up 
user1 = User(1)
#Token()
user2 = User(2, user1.token)

# TODO Grid set up
Grid()

