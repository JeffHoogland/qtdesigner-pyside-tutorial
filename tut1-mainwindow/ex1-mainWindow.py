import sys
from PySide.QtGui import *
from PySide.QtCore import *
from ui_mainWindow import Ui_mainWindow

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
        self.show()
    
    def assignWidgets(self):
        self.goButton.clicked.connect(self.goPushed)
    
    def goPushed(self):
        self.goText.append("Go, Go, Go!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
