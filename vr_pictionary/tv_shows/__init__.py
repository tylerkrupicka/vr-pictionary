# Change to the name of the category
NAME = "TV Shows"

#####################
#  Leave unchanged  #
#####################

_decks = {
   # "Name": [list]
}
DECKS = []

from os import listdir
from os.path import isfile, join, dirname, realpath, split, splitext

_path = dirname(realpath(__file__))
_cardFiles = ["." + splitext(file)[0] for file in listdir(_path) if isfile(join(_path, file))]

from importlib import import_module
for file in _cardFiles:
   try:
      mod = import_module(file, "vr_pictionary." + split(_path)[1])
      _decks[mod.NAME] = mod.CARDS
      DECKS.append(mod.NAME)
   except (ImportError, AttributeError, TypeError):
      pass # TODO: Not sure what I should do here yet

def GET_CARDS(difficulty):
   try:
      return _decks[DECKS[difficulty-1]]
   except TypeError:
      return _decks[difficulty]
   except (IndexError, KeyError):
      raise DifficultyNotFoundException(difficulty)