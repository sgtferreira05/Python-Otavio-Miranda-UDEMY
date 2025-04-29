# QWidget and QLayout from PySide6.QtWidgets
# QWidget > Generic
# QLayout > One layout widget that receives other widgets and arranges them in a specific way.



import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout


app = QApplication(sys.argv)


button1 = QPushButton("Hello World 1")
button1.setStyleSheet("font-size: 80px;")

button2 = QPushButton("Olá, mundo! 2")
button2.setStyleSheet("font-size: 40px;")

central_widget = QWidget()
# layout = QHBoxLayout()
# layout = QVBoxLayout()
layout = QGridLayout() #Com parâmetros (linhas, colunas)



central_widget.setLayout(layout)
layout.addWidget(button1, 1, 1)
layout.addWidget(button2, 2, 1)

central_widget.show()

app.exec()