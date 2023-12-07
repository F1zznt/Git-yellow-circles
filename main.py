from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Git и случайные окружности")
        self.SCREEN_SIZE = [680, 480]
        self.flag = False
        self.coords = []
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.figure = "circle"
        self.size = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            paint = QPainter()
            paint.begin(self)
            paint.setPen(QColor(*self.color))
            paint.setBrush(QColor(*self.color))
            self.x = random.randint(100, self.SCREEN_SIZE[0] - 100)
            self.y = random.randint(100, self.SCREEN_SIZE[1] - 100)
            if self.figure == 'circle':
                paint.drawEllipse(self.x, self.y, self.size, self.size)
            paint.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
