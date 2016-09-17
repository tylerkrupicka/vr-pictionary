import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

class WordWidgetClass(pysidegui.QWidget):
   def __init__(self, deckWidget, scoreBoardWidget, parent=None):
      super().__init__(parent)
      self.deckWidget = deckWidget
      self.deckWidget.deckChanged.connect(self.deckChanged)
      self.scoreBoardWidget = scoreBoardWidget
      self.setup()

   def setup(self):
      self.prompt = pysidegui.QPushButton("Welcome! Add teams, then click to get started")
      self.prompt.clicked.connect(self.hidePrompt)
      self.done = pysidegui.QLabel("Done!")
      self.done.hide()
      self.word = pysidegui.QPushButton("Dummy")
      self.word.clicked.connect(self.hideWord)
      self.applyPointHbox = pysidegui.QHBoxLayout()
      self.teamSelect = pysidegui.QComboBox()
      self.pointButton = pysidegui.QPushButton("Apply Point")
      self.pointButton.clicked.connect(self.applyPoint)
      self.teamSelect.hide()
      self.pointButton.hide()
      self.applyPointHbox.addWidget(self.teamSelect)
      self.applyPointHbox.addWidget(self.pointButton)

      self.hbox = pysidegui.QHBoxLayout()
      self.hbox.addWidget(self.prompt)
      self.hbox.addWidget(self.word)
      self.hbox.addLayout(self.applyPointHbox)
      self.hbox.addWidget(self.done)
      self.word.hide()
      # self.applyPointHbox.hide()

      self.setLayout(self.hbox)
      self.setMinimumSize(0, 0)

   def hidePrompt(self):
      self.prompt.hide()
      word = self.deckWidget.getNextWord()
      if word:
         self.word.setText(word)
         self.word.show()
      else:
         self.done.show()

   def hideWord(self):
      self.word.hide()

      teams = self.scoreBoardWidget.getTeams()
      if len(teams) <= 1:
         self.teamSelect.hide()
         self.pointButton.hide()
         if len(self.deckWidget.currDeck) == 0:
            self.done.show()
         else:
            self.prompt.setText("Click to continue...")
            self.prompt.show()
      else:
         self.teamSelect.clear()
         self.teamSelect.addItems(teams)

         self.teamSelect.show()
         self.pointButton.show()

   def applyPoint(self):
      self.scoreBoardWidget.applyPoint(self.teamSelect.currentText())

      self.teamSelect.hide()
      self.pointButton.hide()
      if len(self.deckWidget.currDeck) == 0:
         self.done.show()
      else:
         self.prompt.setText("Click to continue...")
         self.prompt.show()

   def deckChanged(self):
      if self.done.isVisible():
         self.done.hide()
         
         self.prompt.setText("New Deck! Click to continue...")
         self.prompt.show()

