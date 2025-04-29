# QMainWindow and centralWidget
# https://doc.qt.io/qt-5/qmainwindow.html
# -> QApplication(app)
#   -> QMainWindow(window ->setCentralWidget)
#     -> CentralWidget(central_widget)
#       -> Layout (layout)
#          -> Widget 1 (button1)
#          -> Widget 2 (button2)
#          -> Widget 3 (button3)
#   -> show()
# -> exec()

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMainWindow


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("My first window")


button1 = QPushButton("Hello World 1")
button1.setStyleSheet("font-size: 40px;")

button2 = QPushButton("Hello World 2")
button2.setStyleSheet("font-size: 40px;")

button3 = QPushButton("Hello World 3")
button3.setStyleSheet("font-size: 40px;")

# layout = QHBoxLayout()
# layout = QVBoxLayout()
layout = QGridLayout() #Com parâmetros (linhas, colunas)



central_widget.setLayout(layout)
layout.addWidget(button1, 1, 1)
layout.addWidget(button2, 1, 2)
layout.addWidget(button3, 2, 1, 1, 2)

def slot_example(status_bar):
    status_bar.showMessage("My slot was called!")

#StatusBar
status_bar = window.statusBar()
status_bar.showMessage("It's Ok!")

#menuBar
menu_bar = window.menuBar()
file_menu = menu_bar.addMenu("File")
new_action = file_menu.addAction("New")
new_action.triggered.connect(lambda: slot_example(status_bar))
open_action = file_menu.addAction("Open")


window.show()
app.exec() #Appilication loop