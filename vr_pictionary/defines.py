categories = {}
_numCategories = 0

from os import listdir
from os.path import isdir, join, dirname, realpath

_path = dirname(realpath(__file__))
_categoryDirs = ["." + dir for dir in listdir(_path) if isdir(join(_path, dir))]

from importlib import import_module
for dir in _categoryDirs:
   try:
      mod = import_module(dir, "vr_pictionary")
      categories[_numCategories + 1] = (mod.NAME, mod.DECKS, mod.GET_CARDS)
      _numCategories += 1
   except (ImportError, AttributeError, TypeError):
      pass # TODO: Not sure what I should do here yet

NAME = 0
DECKS = 1
GET_CARDS = 2
