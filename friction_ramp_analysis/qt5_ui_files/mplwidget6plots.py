from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

import matplotlib.pyplot as plt

class mplwidget6plots (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())
        layout = QGridLayout()
        layout.addWidget(self.canvas)
        self.canvas.axes1 = self.canvas.figure.add_subplot(321)
        self.canvas.axes1.set_axis_off()
        self.canvas.axes2 = self.canvas.figure.add_subplot(322)
        self.canvas.axes2.set_axis_off()
        self.canvas.axes3 = self.canvas.figure.add_subplot(323)
        self.canvas.axes3.set_axis_off()
        self.canvas.axes4 = self.canvas.figure.add_subplot(324)
        self.canvas.axes4.set_axis_off()
        self.canvas.axes5 = self.canvas.figure.add_subplot(325)
        self.canvas.axes5.set_axis_off()
        self.canvas.axes6 = self.canvas.figure.add_subplot(326)
        self.canvas.axes6.set_axis_off()
        self.setLayout(layout)
        #self.canvas.figure.tight_layout()
