from .defines import *
from random import shuffle
from time import sleep

class Engine:
   def __init__(self, cards):
      self._cards = cards
      self._teams = {}
      self._score = {}

      if input("\nKeep score? (y) ").lower() == 'y':
         try:
            numTeams = int(input("# of teams: "))
            for teamID in range(1, numTeams+1):
               teamName = input("%d) " % teamID);
               self._teams[teamID] = teamName
               self._score[teamName] = 0
            self._scoreKeeping = True
         except ValueError:
            print("Invalid number of teams.\nNot keeping score.")
            self._scoreKeeping = False
      else:
         self._scoreKeeping = False

   def letsPlay(self):
      print()
      print("Shuffling cards.")
      shuffle(self._cards)
      if self._scoreKeeping:
         print("Commands: (h, s, q)")

      prompt = "Command: "
      spaceBuff = 0

      try:
         while len(self._cards) != 0:
            # TODO: Should flush stdin. But apparently, there is no easy way to do this across platforms.

            card = self._cards.pop()
            spaceBuff = len(card)

            if (self._scoreKeeping):
               while True:
                  command = input(prompt)
                  # process command (e.g. print current score or show next card)
                  if command == "h":
                     print("Commands: (h, s)")
                  elif command == "s":
                     self.printScore();
                  elif command == "q":
                     raise KeyboardInterrupt
                  else:
                     break
            else:
               input("Press ENTER...")

            print(card, end='\r')

            sleep(1)
            print(" " * spaceBuff, end='\r')

            # for i in range(0, 30):
            #    sleep(1)

            # print("Time's Up!")
            
            if self._scoreKeeping:
               # Get score
               print("\nTeams: ")
               self.printTeams()
               try:
                  teamID = input("Point: ")
                  if teamID in self._score:
                     self._score[teamID] += 1
                  else:
                     self._score[self._teams[int(teamID)]] += 1
               except (KeyError, ValueError):
                  print("No point awarded")

         print("All out of cards!")
      except KeyboardInterrupt:
         pass
      finally:
         if self._scoreKeeping:
            print("\n\nFinal tally....")
            self.printScore()

   def printTeams(self):
      for teamID in self._teams:
         print("%d) %s" % (teamID, self._teams[teamID]))

   def printScore(self):
      print("---------------")
      for team in self._score:
         print(team + ": " + str(self._score[team]))