import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randint


class Design(QMainWindow):
    def __init__(self, place):
        super().__init__()
        self.btn = QPushButton('Хочу окружности', place)
        self.btn.resize(180, 30)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle('Цветные окружности')
        self.fl = 0
        des = Design(self)
        des.btn.move(130, 10)
        des.btn.show()
        des.btn.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.fl:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        d1 = randint(10, 200)
        qp.drawEllipse(d1 + 10, d1 + 60, d1, d1)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        d2 = randint(10, 100)
        qp.drawEllipse(d2 + 110, d2 + 100, d2, d2)

    def run(self):
        self.fl = 1
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())