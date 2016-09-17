import sys

class CategoryNotFoundException(Exception):
   def __init__(self, category):
      self.category = category

class DeckNotFoundException(Exception):
   def __init__(self, deck):
      self.deck = deck

def start():
   print()
   for id in categories:
      print("%d) %s" % (id, categories[id][NAME]))
   
   try:
      category = int(input("Pick a category: "))
      category = categories[category]
   except (ValueError, KeyError):
      print("Not a valid category")
      return


   id = 1
   print()
   for deck in category[DECKS]:
      print("%d) %s" % (id, deck))
      id += 1

   try:
      deck = int(input("Pick a deck: "))
      if deck not in range(1,id):
         raise ValueError
   except ValueError:
      print("Not a valid deck")
      return

   try:
      engine = Engine(category[GET_CARDS](deck))

      # Implement try/except to print score
      engine.letsPlay()
   except NotImplementedError as e:
      raise e

def main():
   print("Welcome to Pictionary!")

   if "--no-gui" in sys.argv:
      while True:
         try:
            start()
         except (EOFError, KeyboardInterrupt):
            pass
         finally:
            if input("\nPlay again? (y/n) ").lower() != "y":
               break
   else:
      import PySide.QtCore as pysidecore
      import PySide.QtGui as pysidegui

      from vr_pictionary.gui import MainWindow

      application = pysidegui.QApplication([])
      application.setStyle("Cleanlooks")
      mainWindow = MainWindow.MainWindowClass()
      exit(application.exec_())

if __name__ == '__main__':

   import os
   path = os.path.dirname(sys.modules[__name__].__file__)
   path = os.path.join(path, '..')
   if (path not in sys.path):
      sys.path.insert(0, path)

   from vr_pictionary import Engine, categories, NAME, DECKS, GET_CARDS

   try:
      main()
   except (EOFError, KeyboardInterrupt):
      pass

   print("\nAll done!\n")
   sys.exit()
