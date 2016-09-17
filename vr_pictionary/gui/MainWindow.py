import PySide.QtCore as pysidecore
import PySide.QtGui as pysidegui

from .VrWidget import VrWidgetClass


class MainWindowClass(pysidegui.QMainWindow):

   def __init__(self, parent=None):
      super().__init__(parent)
      self.setup()

   def setup(self):
      centralWidget = VrWidgetClass()

      self.setCentralWidget(centralWidget)
      # self.resize(self.centralWidget().width(), self.centralWidget().height())
      self.show()
