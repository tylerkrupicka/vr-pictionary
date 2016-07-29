
from .defines import *
from random import shuffle
from time import sleep

class CategoryNotFoundException(Exception):
   def __init__(self, category):
      self.category = category;

class DifficultyNotFoundException(Exception):
   def __init__(self, difficulty):
      self.difficulty = difficulty;

class Engine:
   def __init__(self, category = categories[DEFAULT_CAT], difficulty = EASY, cards = None):
      self._category = category;
      self._difficulty = difficulty;
      self._score = {}; # TODO: Implement scores, dictionary of team names/scores 
      if (cards == None):
         try:
            self._cards = self._getCards();
         except (CategoryNotFoundException, DifficultyNotFoundException) as e:
            print(e);
            raise NotImplementedError();
      else:
         self._cards = cards;

   def _getCards(self):
      cards = [];
      if (self._category == "Movies"):
         if (self._difficulty == EASY):
            from .movies import EASY_MOVIES as cards
         elif (self._difficulty == MEDIUM):
            from .movies import MEDIUM_MOVIES as cards
         elif (self._difficulty == HARD):
            from .movies import HARD_MOVIES as cards
         else:
            raise DifficultyNotFoundException(self._difficulty);
      else:
         raise CategoryNotFoundException(self._category);
      return cards;

   def letsPlay(self):
      print();
      shuffle(self._cards);
      i = 0;
      prompt = "Press ENTER..";
      spaceBuff = 0;

      while True:
         # TODO: Should flush stdin. But apparently, there is no easy way to do this across platforms.
         print(" " * spaceBuff, end='\r');
         input(prompt);
         print(self._cards[i], end='\r');
         spaceBuff = len(self._cards[i]);
         sleep(10);
         i += 1
         if (i > len(self._cards)):
            print("All out of %s" % category);
            break;

   def printScore(self):
      print(self._score);