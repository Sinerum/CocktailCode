import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from DataControll import Data

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        layout = QVBoxLayout()
        self.path = QLineEdit('Path to drinks.json')
        button = QPushButton('Load')
        button.setAutoDefault(True)
        button.clicked.connect(self.drinks_button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.path)
        layout.addWidget(button)
        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def drinks_button(self):
        t = Data.load_drinks(self.path.text())
        if not isinstance(t, str):
            self.createMenu()
        else:
            self.path.setText(t)

    def createMenu(self):
        rowsize = 4
        layout = QGridLayout()
        layout.setSpacing(0)
        for i in range(0, Data.drinks.__len__()):
            button = QPushButton(Data.drinks[i].name)
            button.clicked.connect(Data.drinks[i].pour)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout.addWidget(button, i/rowsize, i % rowsize)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
screen_resolution = app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()
app.setStyleSheet(open("style.css").read())
window = MainWindow()
window.show()
app.exec_()
