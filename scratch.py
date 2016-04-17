import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is my widget')
        btn = QPushButton('Push me', self)
        btn.setToolTip('This is a button')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tooltip test')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    root = Example()
    sys.exit(app.exec_())