import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

class TeamLayoutClass(pysidegui.QGridLayout):
   def __init__(self, teamList, team="Team", score="0", parent=None):
      super().__init__(parent)
      self.teamList = teamList
      self.team = team
      self.score = score
      self.setup()

   def setup(self):
      self.teamLabel = pysidegui.QLabel(self.team)
      self.scoreLabel = pysidegui.QLabel(self.score)
      self.addButton = pysidegui.QPushButton("x")
      self.addButton.setFixedSize(20, 20)
      self.addButton.clicked.connect(self.removeTeam)

      self.addWidget(self.teamLabel, 0, 0)
      self.addWidget(self.scoreLabel, 0, 1)
      self.addWidget(self.addButton, 0, 2)
      self.setColumnStretch(0, 5)
      self.setColumnStretch(1, 2)
      self.setColumnStretch(2, 1)

   def removeTeam(self):
      self.deleteLater()

   def deleteLater(self):
      super().deleteLater()

      self.teamLabel.deleteLater()
      self.scoreLabel.deleteLater()
      self.addButton.deleteLater()

      del self