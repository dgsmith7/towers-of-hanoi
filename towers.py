###############################
#  TOWERS OF HANOI            #
#  A simple python script     #
#  to practice basic skills   #
#  David G. Smith - Apr 2024  #
############################### 
import re
import os

tower1 = [5,4,3,2,1]
tower2 = []
tower3 = []
turns = 0
win = False
finished = False
restart = False
fr = None
to = None
holder = 0

def game_reset():
  global tower1
  global tower2
  global tower3
  global turns
  global win
  global finished
  global restart
  tower1 = [5,4,3,2,1]
  tower2 = []
  tower3 = []
  turns = 0
  win = False
  finished = False
  restart = False

def check_win():
  if (tower1 == [] and (tower2 == [5,4,3,2,1] or tower3 == [5,4,3,2,1])):
    return True
  else:
    return False

def input_is_valid(in_string):
  global finished
  global restart
  global to
  global fr
  match in_string:
    case "r"|"R":
      finished = False
      restart = True
      return True
    case "q"|"Q":
      finished = True
      restart = False
      return True
    case _:
      if not re.match("[123]-[123]", in_string):
        print("   >>> Please use the format 'from-to' (for example:  to move from tower 1 to tower 2 type '1-2')")
        return False
      elif in_string[0] == in_string[2]:
        print("   >>> You must choose two different towers.")
        return False
      else: 
        fr = in_string[0]
        to = in_string[2]
        return True

def get_input():
  global to
  global fr
  to = None
  fr = None
  return input("Please enter the 'from tower' and the 'to tower' separated by a dash (eg. 3-2)\n'r' to restart',\n'q' to quit:\n>>>");

def move_is_valid():
  return (from_is_valid() == True) and (to_is_valid() == True)

def from_is_valid():
  global holder
  valid = False
  if (fr == "1") and (len(tower1) >= 1):
    valid = True
    holder = tower1[-1]
  elif (fr == "2") and (len(tower2) >= 1):
    valid = True
    holder = tower2[-1]
  elif (len(tower3) >= 1):
    valid = True
    holder = tower3[-1]
  return valid

def to_is_valid():
  global holder
  valid = False
  match to:
    case "1":
      if (len(tower1) > 0):
        valid = (tower1[-1] > holder)
      else:
        valid = True
    case "2":
      if (len(tower2) > 0):
        valid = (tower2[-1] > holder)
      else:
        valid = True
    case "3": 
      if (len(tower3) > 0):
        valid = (tower3[-1] > holder)
      else:
        valid = True
  return valid

def change_board():
  match fr:
    case "1":
      holder = tower1.pop()
    case "2":
      holder = tower2.pop()
    case _:
      holder = tower3.pop()
  match to:
    case "1":
      tower1.append(holder)
    case "2":
      tower2.append(holder)
    case _:
      tower3.append(holder)

def display_board():
  os.system("clear")
  print("                   TOWERS OF HANOI")
  print("             Try to complete in 31 turns!")
  print("                     Turns: ", turns)
  print()
  print("           |             |             |") 
  for i in range(5):
    if (len(tower1) > (4-i)): 
      p1 = " "*(5-tower1[4-i])+"*"*((tower1[4-i]-1)*2)+"*"+" "*(5-tower1[4-i])
    else:
      p1 = " "*(4)+"|"+" "*(4)
    if (len(tower2) > (4-i)): 
      p2 = " "*(5-tower2[4-i])+"*"*((tower2[4-i]-1)*2)+"*"+" "*(5-tower2[4-i])  
    else:
      p2 = " "*(4)+"|"+" "*(4)
    if (len(tower3) > (4-i)): 
      p3 = " "*(5-tower3[4-i])+"*"*((tower3[4-i]-1)*2)+"*"+" "*(5-tower3[4-i])  
    else:
      p3 = " "*(4)+"|"+" "*(4)
    print("      ",p1,"   ",p2,"   ",p3)
  print("      -----------   -----------   -----------")
  print()

def congrats():
  global finished
  global win
  replay = ""
  print("You won!!!  It took ", turns, " turns.")
  while (replay != "y" and replay != "Y" and replay != "n" and replay != "N"):
    replay = input("Would you like to play again? (y/n) ")
  if replay == "y" or replay == "Y":
    game_reset()
    finished = False
    win = False
  else:
    finished = True

def play():
  global win
  global turns
  display_board()
  while not win and not finished:
    repeat = True
    while repeat:
      command = get_input()
      repeat = not input_is_valid(command)
    if command == 'q' or command == 'Q':
      exit()
    elif command == 'r' or command == 'R':
      game_reset()
      display_board()
    elif move_is_valid() == True:
      turns += 1
      change_board()
      display_board()
      win = check_win()
    if win:
      congrats()

play()
