import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from .TeamLayout import TeamLayoutClass

class ScoreBoardWidgetClass(pysidegui.QWidget):
   def __init__(self, parent=None):
      super().__init__(parent)
      self.parent = parent
      self.setup()

   def setup(self):
      self.addBox = pysidegui.QGridLayout()
      self.teamName = pysidegui.QLineEdit("")
      self.teamName.setMaxLength(10)
      self.addButton = pysidegui.QPushButton("+")
      self.addButton.setFixedSize(20, 20)
      self.addButton.clicked.connect(self.addTeam)
      self.addBox.addWidget(self.teamName, 0, 0)
      self.addBox.addWidget(self.addButton, 0, 1)
      self.addBox.setColumnStretch(0, 7)
      self.addBox.setColumnStretch(1, 1)

      self.headerBox = pysidegui.QGridLayout()
      self.teamLabel = pysidegui.QLabel("Team Name")
      self.scoreLabel = pysidegui.QLabel("Score")
      self.removeAll = pysidegui.QPushButton("x")
      self.removeAll.setFixedSize(20, 20)
      self.removeAll.clicked.connect(self.removeTeams)
      self.headerBox.addWidget(self.teamLabel, 0, 0)
      self.headerBox.addWidget(self.scoreLabel, 0, 1)
      self.headerBox.addWidget(self.removeAll, 0, 2)
      self.headerBox.setColumnStretch(0, 5)
      self.headerBox.setColumnStretch(1, 2)
      self.headerBox.setColumnStretch(2, 1)

      self.vbox = pysidegui.QVBoxLayout()
      self.vbox.addLayout(self.headerBox)
      self.vbox.addLayout(self.addBox)

      self.setLayout(self.vbox)
      self.setMinimumSize(0, 0)

   def addTeam(self):
      if self.teamName.text() != "":
         for i in range(1, self.vbox.count()-1):
            if self.vbox.itemAt(i).itemAt(0).widget().text() == self.teamName.text():
               return
         self.vbox.insertLayout(1, TeamLayoutClass(self.vbox, self.teamName.text(), "0"))
         self.teamName.setText("")

   def removeTeams(self):
      while self.vbox.count() > 2:
         self.vbox.takeAt(1).deleteLater()

   def getTeams(self):
      return [""] + [self.vbox.itemAt(i).itemAt(0).widget().text() for i in range(1, self.vbox.count()-1)]

   def applyPoint(self, team):
      for i in range(1, self.vbox.count()-1):
         if self.vbox.itemAt(i).itemAt(0).widget().text() == team:
            self.vbox.itemAt(i).itemAt(1).widget().setText(str(int(self.vbox.itemAt(i).itemAt(1).widget().text()) + 1))