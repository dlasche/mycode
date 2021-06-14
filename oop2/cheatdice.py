#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Creating a simple dice program utilizing classes."""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
  def cheat(self):
      i = 0
      while i < len(self.dice):
          if self.dice[i] < 6:
              self.dice[i] += 1
          i += 1
class Cheat_5or6_Dice(Player):
    def five_or_six_dice(self):
        self.dice = [] # clear dice
        for i in range(3): # roll 3 dice
            self.dice.append(randint(5, 6))

