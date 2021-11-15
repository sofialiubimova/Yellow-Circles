import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import uic
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resize(500, 500)

    def initUI(self):
        uic.loadUi('circles.ui', self)
        self.setWindowTitle('Жёлтые окружности')
        self.fl = 0
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.fl:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        d1 = randint(10, 200)
        qp.drawEllipse(d1 + 10, d1 + 60, d1, d1)
        d2 = randint(10, 100)
        qp.drawEllipse(d2 + 110, d2 + 100, d2, d2)

    def run(self):
        self.fl = 1
        self.update()
        #self.fl = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())