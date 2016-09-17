import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from .DeckWidget import DeckWidgetClass
from .ScoreBoardWidget import ScoreBoardWidgetClass
from .WordWidget import WordWidgetClass

class VrWidgetClass(pysidegui.QWidget):
   def __init__(self, parent=None):
      super().__init__(parent)
      self.setup()

   def setup(self):
      deckWidget = DeckWidgetClass()
      scoreBoardWidget = ScoreBoardWidgetClass()
      wordWidget = WordWidgetClass(deckWidget, scoreBoardWidget)

      self.layout = pysidegui.QVBoxLayout()
      self.layout.addWidget(deckWidget)
      self.layout.addWidget(scoreBoardWidget)
      self.layout.addWidget(wordWidget)

      self.setLayout(self.layout)