# PySide6 to GUI(Graphical User Interface) with Qt in Python
# PySide6 is a set of Python bindings for The Qt Company’s(Nokia) Qt application framework.
# Qt is a free and open-source widget toolkit for creating graphical user interfaces (GUIs).
# PySide6 is a reference to the 6th version of the Qt framework.
# PySide6 is the official set of Python bindings for Qt libraries.
# Qt is multi-platform, meaning it can be used to create applications that run on various operating systems, including Windows, macOS, and Linux.
#  The biggest difference between PyQt and PySide is the licensing. PyQt is available under the GPL and a commercial license, while PySide is available under the LGPL.
#  This means that PySide can be used in proprietary applications without the need to release the source code, while PyQt requires the source code to be released under the GPL if used in a non-commercial application.
# https://doc.qt.io/qtforpython-6/index.html
# https://tldrlegal.com/license/gnu-lesser-general-public-license-v2-(gpl-2)

import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)