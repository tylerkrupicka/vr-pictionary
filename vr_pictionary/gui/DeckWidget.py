import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from random import shuffle

from vr_pictionary import categories, revLookupCategories, categoryGetNames, DECKS, GET_CARDS

class DeckWidgetClass(pysidegui.QWidget):
   deckChanged = pysidecore.Signal()

   def __init__(self, parent=None):
      super().__init__(parent)
      self.setup()

   def setup(self):
      catLayout = pysidegui.QHBoxLayout()
      catLabel = pysidegui.QLabel("Category: ")
      self.catSelect = pysidegui.QComboBox()
      self.catSelect.addItems(categoryGetNames(categories))
      self.catSelect.currentIndexChanged.connect(self.onDeckChanged)
      catLayout.addWidget(catLabel)
      catLayout.addWidget(self.catSelect)

      deckLayout = pysidegui.QHBoxLayout()
      deckLabel = pysidegui.QLabel("Deck: ")
      self.deckSelect = pysidegui.QComboBox()
      self.deckSelect.addItems(revLookupCategories[self.catSelect.currentText()][DECKS])
      self.deckSelect.currentIndexChanged.connect(self.onDeckChanged)
      deckLayout.addWidget(deckLabel)
      deckLayout.addWidget(self.deckSelect)

      self.onDeckChanged()

      self.layout = pysidegui.QGridLayout()
      self.layout.addLayout(catLayout,0,0)
      self.layout.addLayout(deckLayout,0,1)

      self.setLayout(self.layout)

   def getNextWord(self):
      try:
         return self.currDeck.pop()
      except IndexError:
         return None

   def onDeckChanged(self):
      self.currDeck = revLookupCategories[self.catSelect.currentText()][GET_CARDS](self.deckSelect.currentText())[:]
      shuffle(self.currDeck)
      self.deckChanged.emit()
