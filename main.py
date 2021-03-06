import sys
from config import User
from game import Grid, Turn

#--> Welcome message
print("==========")
print("Connect 4")
print("==========\n")

print("This is an interactive version of the traditional game CONNECT FOUR.\n")
print("Confidentiality NOTE: the system is not keeping any personal data from you.\n")
print("You are free to provide real, fake or no personal data at all:")
print("It does not affect the game's performance.")

print("---------------------\n")

#--> User set up 
user1 = User(1)
user2 = User(2, user1.token)

#--> Start game
#### TODO Instructions to insert token row - column
#--> Grid set up
mygame = Grid()

# Turns
turn1u1 = Turn(user1.user)
mygame.enter_token(turn1u1.new_entry, user1.token)


turn1u2 =Turn(user2.user)
mygame.enter_token(turn1u2.new_entry, user2.token)

