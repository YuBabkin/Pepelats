import sys
from OpenGL import GL
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtQuick import QQuickView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    print("hi")
    view = QQuickView()
    view.setSource(QUrl('./interface/stellarium.qml'))
    view.show()
    app.exec_()
    sys.exit()
