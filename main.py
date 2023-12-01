from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from radius import Ui_Form
import random
import sys


class DZ(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.do_paint = None
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.create.clicked.connect(self.paint)



    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


    def draw_circle(self, qp):
        weight = random.randint(10, 170)
        coords = QPoint(300, 250)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(coords, weight, weight)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DZ()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())