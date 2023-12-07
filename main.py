from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Git и жёлтые окружности")
        self.SCREEN_SIZE = [680, 480]
        self.flag = False
        self.coords = []
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.figure = 'circle'
        self.size = random.randint(10, 100)
        self.color = 'yellow'
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(self.color))
            qp.setBrush(QColor(self.color))
            self.x = random.randint(100, self.SCREEN_SIZE[0] - 100)
            self.y = random.randint(100, self.SCREEN_SIZE[1] - 100)
            if self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
