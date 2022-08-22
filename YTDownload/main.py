import sys
from PySide6 import QtWidgets
from form import Form

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Form()
    
    widget.show()
    widget.resize(300, 50)

    sys.exit(app.exec())