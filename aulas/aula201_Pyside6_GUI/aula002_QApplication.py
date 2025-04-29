# QApplication and QPushButton from PySide6.QtWidgets
# QApplication is the main class for any PySide6 application. It manages the GUI application's control flow and main settings.
# It is responsible for initializing the application, managing the main event loop, and handling application-wide settings.
# QPushButton is a widget that represents a clickable button in the GUI. It can be used to trigger actions when clicked by the user.
# PySide6.QtWidgets is a module that contains classes for creating and managing GUI widgets in PySide6 applications.
# Documentation: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QApplication.html

import sys
from PySide6.QtWidgets import QApplication, QPushButton

# Create an instance of QApplication, passing the command line arguments to it.
app = QApplication(sys.argv)

# Create a button with the text "Hello World"
button = QPushButton("Hello World")


button.setStyleSheet("font-size: 40px;") # Set the button's background color to red, text color to white, and font size to 20px
button.setToolTip("This is a button") # Set the tooltip text for the button

button.show() # Show the button on the screen, add the widget to the application window
app.exec()