from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtCore
import sys
from .readNanoscopeImages import *
from .callForceRampGUI import *
import matplotlib.pyplot as plt
from ..qt5_ui_files.frictionGUI import *
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import os
import math


class frictionRampGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        #Load the UI
        self.ui = Ui_FrictionGUI()
        self.ui.setupUi(self)
        self.ui.actionLoadImages.triggered.connect(self.openfiledialog)
        self.ui.actionClose.triggered.connect(QApplication.instance().quit)
        self.ui.actionViewRawData.triggered.connect(self.viewRawData)
        self.ui.actionViewCalibratedData.triggered.connect(self.viewCalibratedData)
        self.ui.actionExportMainRaw.triggered.connect(self.exportRawMainFrictionRamp)
        self.ui.actionExportMainCalibrated.triggered.connect(self.exportCalibratedMainFrictionRamp)
        self.ui.actionExportInterleaveRaw.triggered.connect(self.exportRawInterleaveFrictionRamp)
        self.ui.actionExportInterleaveCalibrated.triggered.connect(self.exportCalibratedInterleaveFrictionRamp)
        self.ui.actionOffsetFromFZ.triggered.connect(self.openForceRampGUI)
        self.ui.actionMainScan.triggered.connect(self.selectMainScan)
        self.ui.actionInterleaveScan.triggered.connect(self.selectInterleaveScan)
        self.ui.pushButtonPrevImage.clicked.connect(self.showPreviousImage)
        self.ui.pushButtonNextImage.clicked.connect(self.showNextImage)
        self.ui.pushButtonPrevRow.clicked.connect(self.showPreviousRow)
        self.ui.pushButtonNextRow.clicked.connect(self.showNextRow)
        self.ui.pushButtonUpdate.clicked.connect(self.update_graph)

        self.ui.lineEditImageNo.returnPressed.connect(self.updateImage)
        self.ui.lineEditRowNo.returnPressed.connect(self.updateRow)
        self.ui.pushButtonCalibrate.clicked.connect(self.calibrate)

        MplToolbar = NavigationToolbar(self.ui.mplWidget.canvas, self)
        self.addToolBar(MplToolbar)
        self.Files = []
        self.frictionRampV_mean = []
        self.frictionRampV_std = []
        self.frictionRampV_Interleave_mean = []
        self.frictionRampV_Interleave_std = []
        self.frictionCalibrationConstant = 0
        self.currentFileIndex = 0
        self.currentRow = 0
        self.numberOfFiles = 0
        self.fileList = []
        self.rawSetPoints = []
        self.loadForce = None
        self.dataCalibrated = False
        self.dataView = 'Raw'
        self.interleaveRegistered = False
        self.selectedScanMode = 'Main'
        self.show()

    def viewRawData(self):
        self.dataView = 'Raw'
        self.update_graph()

    def viewCalibratedData(self):
        if self.dataCalibrated == True:
            self.dataView = 'Calibrated'
            self.update_graph()

    def selectMainScan(self):
        self.selectedScanMode = 'Main'
        self.ui.actionInterleaveScan.setChecked(False)
        self.update_graph()

    def selectInterleaveScan(self):
        if self.interleaveRegistered == True:
            self.selectedScanMode = 'Interleave'
            self.ui.actionMainScan.setChecked(False)
            self.update_graph()

    def openfiledialog(self):
        caption = "Open File"
        directory = os.getcwd()
        filter_mask = "All Files (*)"
        filenames = QFileDialog.getOpenFileNames(self, caption, directory, filter_mask)[0]
        # Initially, and empty list that will contain the name of the
        # loaded files is created
        self.fileList = []
        self.numberOfFiles = len(filenames)
        self.currentFileIndex = 0
        self.currentRow = 0
        for i in range(self.numberOfFiles):
            self.fileList.append(filenames[i].split('/')[-1])
            self.Files.append(NanoscopeImage(filenames[i]))
            self.Files[i].readHeader()
            self.Files[i].readImages()
            self.Files[i].flattenImage('Height','Main','Retrace', 3)
            self.Files[i].equalizeImage('Friction','Main','Trace',3)
            self.Files[i].equalizeImage('Friction','Main','Retrace',3)
            try:
                self.Files[i].equalizeImage('Friction','Interleave','Trace',3)
                self.Files[i].equalizeImage('Friction','Interleave','Retrace',3)
                self.interleaveRegistered = True
            except:
                pass
            self.rawSetPoints.append(self.Files[i].Image[0]['Set Point'])
            self.rawSetPoints = np.asarray(self.rawSetPoints)
            self.loadForce = np.zeros(self.numberOfFiles)
            self.ui.lineEditMaxRow.setText(str(self.Files[0].Image[0]['Rows']-1))
            self.ui.lineEditMaxCol.setText(str(self.Files[0].Image[0]['Columns']-1))
            self.calculateFriction()
            self.update_graph()

    def exportRawMainFrictionRamp(self):
        caption = "Save File"
        directory = os.getcwd()
        filter_mask = "All Files (*)"
        name = QFileDialog.getSaveFileName(self, caption, directory, filter_mask)
        np.savetxt(name[0], np.transpose([self.rawSetPoints,self.frictionRampV_mean, self.frictionRampV_std]), delimiter="\t")

    def exportCalibratedMainFrictionRamp(self):
        caption = "Save File"
        directory = os.getcwd()
        filter_mask = "All Files (*)"
        name = QFileDialog.getSaveFileName(self, caption, directory, filter_mask)
        np.savetxt(name[0], np.transpose([self.loadForce,self.frictionRampV_mean*self.frictionCalibrationConstant,self.frictionRampV_std*self.frictionCalibrationConstant]), delimiter="\t")

    def exportRawInterleaveFrictionRamp(self):
        caption = "Save File"
        directory = os.getcwd()
        filter_mask = "All Files (*)"
        name = QFileDialog.getSaveFileName(self, caption, directory, filter_mask)
        np.savetxt(name[0], np.transpose([self.rawSetPoints,self.frictionRampV_Interleave_mean, self.frictionRampV_Interleave_std]), delimiter="\t")

    def exportCalibratedInterleaveFrictionRamp(self):
        caption = "Save File"
        directory = os.getcwd()
        filter_mask = "All Files (*)"
        name = QFileDialog.getSaveFileName(self, caption, directory, filter_mask)
        np.savetxt(name[0], np.transpose([self.loadForce,self.frictionRampV_Interleave_mean*self.frictionCalibrationConstant,self.frictionRampV_Interleave_std*self.frictionCalibrationConstant]), delimiter="\t")

    def openForceRampGUI(self):
        self.ForceRampGUI = forceRampGUI()
        self.ForceRampGUI.signal1.connect(self.slotVi)
        self.ForceRampGUI.signal2.connect(self.slotVf)
        self.ForceRampGUI.show()

    QtCore.pyqtSlot(str)
    def slotVi(self, addr):
        self.ui.lineEditInitV.setText(str(addr))

    QtCore.pyqtSlot(str)
    def slotVf(self, addr):
        self.ui.lineEditFinalV.setText(str(addr))

    def showPreviousImage(self):
        if self.currentFileIndex > 0:
            self.currentFileIndex -= 1
            self.ui.lineEditImageNo.setText(str(self.currentFileIndex))
            self.update_graph()

    def showNextImage(self):
        if self.currentFileIndex < self.numberOfFiles-1:
            self.currentFileIndex += 1
            self.ui.lineEditImageNo.setText(str(self.currentFileIndex))
            self.update_graph()

    def updateImage(self):
        newImage = int(self.ui.lineEditImageNo.text())
        if newImage< 0:
            self.currentFileIndex = 0
        elif newImage >= self.numberOfFiles:
            self.currentFileIndex = self.numberOfFiles-1
        else:
            self.currentFileIndex = newImage
        self.ui.lineEditImageNo.setText(str(self.currentFileIndex))
        self.update_graph()

    def updateRow(self):
        newRow = int(self.ui.lineEditRowNo.text())
        if newRow< 0:
            self.currentRow = 0
        elif newRow >= self.Files[self.currentFileIndex].Image[0]['Rows']:
            self.currentRow = self.Files[self.currentFileIndex].Image[0]['Rows']-1
        else:
            self.currentRow = newRow
        self.ui.lineEditRowNo.setText(str(self.currentRow))
        self.update_graph()

    def showPreviousRow(self):
        if self.currentRow > 0:
            self.currentRow -= 1
            self.ui.lineEditRowNo.setText(str(self.currentRow))
            self.update_graph()

    def showNextRow(self):
        if self.currentRow < self.Files[self.currentFileIndex].Image[0]['Rows']-1:
            self.currentRow += 1
            self.ui.lineEditRowNo.setText(str(self.currentRow))
            self.update_graph()

    def calculateFriction(self):
        self.frictionRampV_mean = []
        self.frictionRampV_Interleave_mean = []
        self.frictionRampV_std = []
        self.frictionRampV_Interleave_std = []
        x_min = int(self.ui.lineEditMinCol.text())
        x_max = int(self.ui.lineEditMaxCol.text()) + 1
        y_min = int(self.ui.lineEditMinRow.text())
        y_max = int(self.ui.lineEditMaxRow.text()) + 1
        for i in range(self.numberOfFiles):
            frictionTrace = self.Files[i].getChannel('Friction','Main','Trace')
            frictionRetrace = self.Files[i].getChannel('Friction','Main','Retrace')
            self.frictionRampV_mean.append(np.mean((frictionTrace['Image Data'][:,x_min:x_max] - frictionRetrace['Image Data'][:,x_min:x_max])/2))
            y_err = []
            for y in range(y_min,y_max):
                y_err.append((np.std(frictionTrace['Image Data'][y,x_min:x_max])+np.std(frictionRetrace['Image Data'][y,x_min:x_max]))/2)
            y_err = np.asarray(y_err)
            self.frictionRampV_std.append(np.mean(y_err))
            if self.interleaveRegistered == True:
                frictionTraceInterleave = self.Files[i].getChannel('Friction','Interleave','Trace')
                frictionRetraceInterleave = self.Files[i].getChannel('Friction','Interleave','Retrace')
                self.frictionRampV_Interleave_mean.append(np.mean((frictionTraceInterleave['Image Data'][:,x_min:x_max] - frictionRetraceInterleave['Image Data'][:,x_min:x_max])/2))
                y_err = []
                for y in range(y_min,y_max):
                    y_err.append((np.std(frictionTraceInterleave['Image Data'][y,x_min:x_max])+np.std(frictionRetraceInterleave['Image Data'][y,x_min:x_max]))/2)
                y_err = np.asarray(y_err)
                self.frictionRampV_Interleave_std.append(np.mean(y_err))
        self.frictionRampV_mean = np.asarray(self.frictionRampV_mean)
        self.frictionRampV_std = np.asarray(self.frictionRampV_std)
        if self.interleaveRegistered == True:
            self.frictionRampV_Interleave_mean = np.asarray(self.frictionRampV_Interleave_mean)
            self.frictionRampV_Interleave_std = np.asarray(self.frictionRampV_Interleave_std)

    def calibrate(self):
        self.calculateFriction()
        tipHeight = float(self.ui.lineEditTipHeight.text())
        latSens = float(self.ui.lineEditLatSens.text())
        torsConst = float(self.ui.lineEditTorsConst.text())
        vertSens = float(self.ui.lineEditVertSens.text())
        normConst = float(self.ui.lineEditNormConst.text())
        initV = float(self.ui.lineEditInitV.text())
        finalV = float(self.ui.lineEditFinalV.text())
        delta = (finalV-initV)/(max(self.numberOfFiles,2)-1)

        for i in range(self.numberOfFiles):
            self.loadForce[i] = (self.rawSetPoints[i] - (initV+i*delta)) * vertSens * normConst
        self.frictionCalibrationConstant = latSens*torsConst / tipHeight
        self.dataCalibrated = True
        self.dataView = 'Calibrated'
        self.update_graph()

    def update_graph(self):
        if int(self.ui.lineEditMinCol.text())<0:
            self.ui.lineEditMinCol.setText(str(0))
        if int(self.ui.lineEditMaxCol.text()) > self.Files[0].Image[0]['Columns']-1:
            self.ui.lineEditMaxCol.setText(str(self.Files[0].Image[0]['Columns']-1))
        if int(self.ui.lineEditMinRow.text())<0:
            self.ui.lineEditMinRow.setText(str(0))
        if int(self.ui.lineEditMaxRow.text()) > self.Files[0].Image[0]['Rows']-1:
            self.ui.lineEditMaxRow.setText(str(self.Files[0].Image[0]['Rows']-1))

        x_min = int(self.ui.lineEditMinCol.text())/self.Files[0].Image[0]['Columns']
        x_max = int(self.ui.lineEditMaxCol.text())/self.Files[0].Image[0]['Columns']
        x_profile = np.arange(int(self.ui.lineEditMinCol.text()),int(self.ui.lineEditMaxCol.text())+1,1)
        x_profile_full = np.arange(0,self.Files[0].Image[0]['Columns'],1)

        self.calculateFriction()
        

        self.ui.mplWidget.canvas.axes1.clear()
        self.ui.mplWidget.canvas.axes1.set_axis_off()
        topography = self.Files[self.currentFileIndex].getChannel('Height','Main','Retrace')
        self.ui.mplWidget.canvas.axes1.imshow(topography['Processed Image Data'], cmap='gray', aspect='auto')
        self.ui.mplWidget.canvas.axes1.axhline(y=self.currentRow,xmin=x_min,xmax=x_max,color='red')
        self.ui.mplWidget.canvas.axes1.set_title('Height')

        self.ui.mplWidget.canvas.axes2.clear()
        self.ui.mplWidget.canvas.axes2.plot(x_profile_full,topography['Processed Image Data'][self.currentRow,:],'--')
        self.ui.mplWidget.canvas.axes2.plot(x_profile,topography['Processed Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1],'b')
        self.ui.mplWidget.canvas.axes2.set_title('Height Profile')
        self.ui.mplWidget.canvas.axes2.set_ylabel('Height (nm)')

        self.ui.mplWidget.canvas.axes3.clear()
        self.ui.mplWidget.canvas.axes3.set_axis_off()
        if self.selectedScanMode == 'Interleave':
            frictionTrace = self.Files[self.currentFileIndex].getChannel('Friction','Interleave','Trace')
            self.ui.mplWidget.canvas.axes3.set_title('Friction Interleave Trace')
        elif self.selectedScanMode == 'Main':
            frictionTrace = self.Files[self.currentFileIndex].getChannel('Friction','Main','Trace')
            self.ui.mplWidget.canvas.axes3.set_title('Friction Trace')
        self.ui.mplWidget.canvas.axes3.imshow(frictionTrace['Processed Image Data'], cmap='gray', aspect='auto')
        self.ui.mplWidget.canvas.axes3.axhline(y=self.currentRow,xmin=x_min,xmax=x_max,color='red')

        self.ui.mplWidget.canvas.axes5.clear()
        self.ui.mplWidget.canvas.axes5.set_axis_off()
        if self.selectedScanMode == 'Interleave':
            frictionRetrace = self.Files[self.currentFileIndex].getChannel('Friction','Interleave','Retrace')
            self.ui.mplWidget.canvas.axes5.set_title('Friction Interleave Retrace')
        elif self.selectedScanMode == 'Main':
            frictionRetrace = self.Files[self.currentFileIndex].getChannel('Friction','Main','Retrace')
            self.ui.mplWidget.canvas.axes5.set_title('Friction Retrace')
        self.ui.mplWidget.canvas.axes5.imshow(frictionRetrace['Processed Image Data'], cmap='gray', aspect='auto')
        self.ui.mplWidget.canvas.axes5.axhline(y=self.currentRow,xmin=x_min,xmax=x_max,color='red')
        

        self.ui.mplWidget.canvas.axes4.clear()
        if self.selectedScanMode == 'Interleave':
            self.ui.mplWidget.canvas.axes4.set_title('Friction Interleave Profile')
            self.ui.mplWidget.canvas.axes4.set_ylabel('Friction Interleave (V)')
            if self.dataView == 'Calibrated':
                self.ui.mplWidget.canvas.axes4.set_ylabel('Friction (N)')
        elif self.selectedScanMode == 'Main':
            self.ui.mplWidget.canvas.axes4.set_title('Friction Profile')
            self.ui.mplWidget.canvas.axes4.set_ylabel('Friction (V)')
            if self.dataView == 'Calibrated':
                self.ui.mplWidget.canvas.axes4.set_ylabel('Friction (N)')
        if self.dataView == 'Raw':
            self.ui.mplWidget.canvas.axes4.plot(x_profile_full,frictionTrace['Image Data'][self.currentRow,:],'b--')
            self.ui.mplWidget.canvas.axes4.plot(x_profile_full,frictionRetrace['Image Data'][self.currentRow,:],'r--')
            self.ui.mplWidget.canvas.axes4.plot(x_profile,frictionTrace['Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1],'b')
            self.ui.mplWidget.canvas.axes4.plot(x_profile,frictionRetrace['Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1],'r')
        elif self.dataView == 'Calibrated':
            self.ui.mplWidget.canvas.axes4.plot(x_profile_full,frictionTrace['Image Data'][self.currentRow,:]*self.frictionCalibrationConstant,'b--')
            self.ui.mplWidget.canvas.axes4.plot(x_profile_full,frictionRetrace['Image Data'][self.currentRow,:]*self.frictionCalibrationConstant,'r--')
            self.ui.mplWidget.canvas.axes4.plot(x_profile,frictionTrace['Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1]*self.frictionCalibrationConstant,'b')
            self.ui.mplWidget.canvas.axes4.plot(x_profile,frictionRetrace['Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1]*self.frictionCalibrationConstant,'r')
                    
            

        self.ui.mplWidget.canvas.axes6.clear()
        if self.selectedScanMode == 'Interleave':
            self.ui.mplWidget.canvas.axes6.set_title('Friction Ramp Interleave')
            if self.dataView == 'Raw':
                self.ui.mplWidget.canvas.axes6.errorbar(
                    x=np.arange(self.frictionRampV_Interleave_mean.shape[0]),
                    y=self.frictionRampV_Interleave_mean,
                    yerr=self.frictionRampV_Interleave_std
                )
                self.ui.mplWidget.canvas.axes6.plot(self.frictionRampV_Interleave_mean[self.currentFileIndex],'ro')
                self.ui.mplWidget.canvas.axes6.set_ylabel('Friction Interleave(V)')
            elif self.dataView == 'Calibrated':
                self.ui.mplWidget.canvas.axes6.errorbar(
                    x=np.arange(self.frictionRampV_Interleave_mean.shape[0]),
                    y=self.frictionRampV_Interleave_mean*self.frictionCalibrationConstant,
                    yerr=self.frictionRampV_Interleave_std*self.frictionCalibrationConstant
                )
                self.ui.mplWidget.canvas.axes6.plot(self.frictionRampV_Interleave_mean[self.currentFileIndex]*self.frictionCalibrationConstant,'ro')
                self.ui.mplWidget.canvas.axes6.set_ylabel('Friction Interleave (N)')
        elif self.selectedScanMode == 'Main':
            self.ui.mplWidget.canvas.axes6.set_title('Friction Ramp')
            if self.dataView == 'Raw':
                self.ui.mplWidget.canvas.axes6.errorbar(
                    x=self.rawSetPoints,
                    y=self.frictionRampV_mean,
                    yerr=self.frictionRampV_std
                )
                self.ui.mplWidget.canvas.axes6.plot(self.rawSetPoints[self.currentFileIndex],self.frictionRampV_mean[self.currentFileIndex],'ro')
                self.ui.mplWidget.canvas.axes6.set_ylabel('Friction (V)')
            elif self.dataView == 'Calibrated':
                self.ui.mplWidget.canvas.axes6.errorbar(
                    x=self.loadForce,
                    y=self.frictionRampV_mean*self.frictionCalibrationConstant,
                    yerr=self.frictionRampV_std*self.frictionCalibrationConstant
                )
                self.ui.mplWidget.canvas.axes6.plot(self.loadForce[self.currentFileIndex],self.frictionRampV_mean[self.currentFileIndex]*self.frictionCalibrationConstant,'ro')
                self.ui.mplWidget.canvas.axes6.set_ylabel('Friction (N)')

        self.ui.mplWidget.canvas.figure.tight_layout()
        self.ui.mplWidget.canvas.draw()

        self.ui.labelImageName.setText(self.fileList[self.currentFileIndex])
