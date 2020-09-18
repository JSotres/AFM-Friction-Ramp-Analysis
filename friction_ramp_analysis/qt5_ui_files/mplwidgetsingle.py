from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5 import QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

class MplWidgetSingle(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.canvas = FigureCanvas(Figure(frameon=False))
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_axes([0., 0., 1., 1., ])
        self.setLayout(vertical_layout)
        """
        

        def onclick(event):
        	print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        		('double' if event.dblclick else 'single', event.button,
        			event.x, event.y, event.xdata, event.ydata))

        self.canvas.mpl_connect('button_press_event', onclick)

        """

        def on_xlims_change(event_ax):
            print("updated xlims: ", event_ax.get_xlim())

        def on_ylims_change(event_ax):
            print("updated ylims: ", event_ax.get_ylim())

        self.canvas.mpl_connect('xlim_changed', on_xlims_change)
        self.canvas.mpl_connect('ylim_changed', on_ylims_change)

        


