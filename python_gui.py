from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#Tec with Tim

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    xpos = 200
    ypos = 200
    width = 500
    height = 500
    win.setGeometry(xpos,ypos,width,height)
    win.setWindowTitle("ROVR Systems - Easy Convert")

    label = QtWidgets.QLabel(win)
    label.setText("Label")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

    
window()
