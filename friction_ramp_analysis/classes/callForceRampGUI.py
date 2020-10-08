from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys
from .readNanoscopeForceRamps import *
import matplotlib.pyplot as plt
from ..qt5_ui_files.ForceRampGUI import *
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import os
import math
from ..qt5_ui_files.mplwidget1plot import mplwidget1plot

class forceRampGUI(QMainWindow):
	signal1 = QtCore.pyqtSignal(float)
	signal2 = QtCore.pyqtSignal(float)

	def __init__(self):
		super().__init__()
		self.ui = Ui_GUI3()
		self.ui.setupUi(self)
		self.ui.pushButtonSendVi.clicked.connect(self.sendVi)
		self.ui.pushButtonSendVf.clicked.connect(self.sendVf)
		self.ui.pushButtonGetValue.clicked.connect(self.getValue)
		MplToolbar = NavigationToolbar(self.ui.widget.canvas, self)
		self.addToolBar(MplToolbar)
		filename = QFileDialog.getOpenFileNames(
			self, "Open File", os.getcwd(), "All Files (*)")[0][0]
		self.rampObject = NanoscopeRamp(filename)
		self.rampObject.readHeader()
		self.rampObject.readRamps()
		self.plotRamp()
		
		
		
		

	def getValue(self):
		x1,x2 = self.ui.widget.canvas.axes.get_xlim()
		condition = np.logical_and((self.rampObject.Ramp[0]['RawX']>x1),(self.rampObject.Ramp[0]['RawX']<x2))
		if self.ui.radioButtonForward.isChecked() == True:
			yf = self.rampObject.Ramp[0]['RawY'][0][condition]
			self.ui.lineEditValue.setText(str(format(yf.mean(),'.3f')))
		elif self.ui.radioButtonBackward.isChecked() == True:
			yb = self.rampObject.Ramp[0]['RawY'][1][condition]
			self.ui.lineEditValue.setText(str(format(yb.mean(),'.3f')))
		else:
			yf = self.rampObject.Ramp[0]['RawY'][0][condition]
			yb = self.rampObject.Ramp[0]['RawY'][1][condition]
			y2 = (yf+yb)/2
			self.ui.lineEditValue.setText(str(format(y2.mean(),'.3f')))


	QtCore.pyqtSlot()
	def sendVi(self):
		value = float(self.ui.lineEditValue.text())
		self.signal1.emit(value)

	QtCore.pyqtSlot()
	def sendVf(self):
		value = float(self.ui.lineEditValue.text())
		self.signal2.emit(value)

	def plotRamp(self):
		self.ui.widget.canvas.axes.clear()
		self.ui.widget.canvas.axes.plot(self.rampObject.Ramp[0]['RawX'], self.rampObject.Ramp[0]['RawY'][0][:])
		self.ui.widget.canvas.axes.plot(self.rampObject.Ramp[0]['RawX'], self.rampObject.Ramp[1]['RawY'][1][:])
		self.ui.widget.canvas.axes.set_ylabel('Photodiode Vertical Signal (V)')
		self.ui.widget.canvas.axes.set_xlabel('Sample Displacement (nm)')
		self.ui.widget.canvas.figure.tight_layout()
		self.ui.widget.canvas.draw()
		
