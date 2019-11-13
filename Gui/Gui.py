from PyQt5.QtWidgets import *
from DataControll import Data


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QVBoxLayout()
        self.path = QLineEdit('Path to drinks.json')
        button = QPushButton('Load')
        button.clicked.connect(self.drinks_button)
        layout.addWidget(self.path)
        layout.addWidget(button)
        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def drinks_button(self):
        Data.load_drinks(self.path.text())
        self.createMenu()

    def createMenu(self):
        layout = QGridLayout()
        for drink in Data.drinks:
            button = QPushButton(drink.name)
            button.clicked.connect(drink.pour)
            layout.addWidget(button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
