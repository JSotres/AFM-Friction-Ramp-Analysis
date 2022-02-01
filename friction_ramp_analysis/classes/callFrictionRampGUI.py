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
from scipy.optimize import curve_fit

def functionSingleAsperity(x, a, b):
    return a*(x+b)**(2/3)

def functionMultipleAsperity(x, a, b):
    return a*(x+b)


class frictionRampGUI(QMainWindow):
    """
    Class for the main GUI of the program

    Attributes:
        ui: handle to the graphical interface.
        File: List of objects of the NanoscopeImage class, each one corresponding to, and calculated from, one of the loaded files.
        frictionRampV_mean: List with the mean friction value (in Volts) for each of the loaded "Main" scans.
        frictionRampV_std: List with the std friction value (in Volts) for each of the loaded "Main" scans.
        frictionRampV_Interleave_mean: List with the mean friction value (in Volts) for each of the loaded "Interleave" scans.
        frictionRampV_Interleave_std: List with the std friction value (in Volts) for each of the loaded "Interleave" scans.
        frictionCalibrationConstant: Float. Constant to transform friction data from Volts to Force Units (N).
        currentFileIndex: Int. Index for the current Scan.
        currentRow: Int. Index for the current row.
        numberOfFiles: Int. Total number of loaded files.
        fileList: List with the names of the loaded files.
        rawSetPoints: List with the loads (in Volts) of each of the loaded friction scans.
        loadForce: List with the loads (in Newtons) of each of the loaded friction scans.
        dataCalibrated: Boolean. Denoted whether friction data has been calibrated.
        dataView: String: "Raw" or "Calibrated". Determines whether the friction data is to be seen raw (as registered) or calibrated.
        interleaveRegistered: Boolean. Indicates whether the load scans contain Interleave data.
        selectedScanMode: String: "Main" or "Interleave". Determines whether the "Main" or "Interleave" scans is used to calculate friction data.
        popt: Numpy array. Contains parameters for friction fits.
        frictionFitted: String. Indicates if the calibrated friction data has been fitted to a model.
                        'No': It has not been fitted.
                        'SingleAsperity': fitted to a single asperity model.
                        'MultipleAsperity': fitted to a multiple asperity model.

    Methods:
        __init__(): Initiates the GUI
        viewRawData(): Updates graph with raw data.
        viewCalibratedData(): Updates graphs with calibrated data.
        selectMainScan(): Selects Main scans for friction data.
        selectInterleaveScan(): Selects Interleave scans for friction data. 
        openfiledialog(): Opens a QFileDialog for loading friction scans.
        exportRawMainFrictionRamp(): Exports the friction ramp (non-calibrated, in raw units) corresponding to the "Main" scans as an ASCII file.
        exportCalibratedMainFrictionRamp(): Exports the calibrated friction ramp corresponding to the "Main" scans as an ASCII file.
        exportRawInterleaveFrictionRamp(): Exports the friction ramp (non-calibrated, in raw units) corresponding to the "Interleave" scans as an ASCII file.
        exportCalibratedInterleaveFrictionRamp(): Exports the calibrated friction ramp corresponding to the "Interleave" scans as an ASCII file.
        exportFrictionProfiles(): Exports as an ASCII file the currently viewed friction profile (both the full profiles and the selected region as separate files).
        openForceRampGUI(): Opens the graphical interface ForceRampGUI, needed for determining the load offset at the beginning and end of the experiment.
        slotVi(): Updates the value in the Edit Box lineEditInitV with the signal emitted from ForceRampGUI.
        slotVf(): Updates the value in the Edit Box lineEditFinalV with the signal emitted from ForceRampGUI.
        showPreviousImage(): Updates the visualized image when the Push Button pushButtonPrevImage is pressed.
        showNextImage(): Updates the visualized image when the Push Button pushButtonNextImage is pressed.
        updateImage(): Updates the visualized image to that entered in the Edit Box lineEditImageNo.
        updateRow(): Updates the visualized image row to that entered in the Edit Box lineEditRowNo.
        showPreviousRow(): Updates the visualized image row when the Push Button pushButtonPrevRow is pressed.
        showNextRow(): Updates the visualized image row when the Push Button pushButtonNextRow is pressed.
        calculateFriction(): Calculates (raw) friction for the loaded set of scans.
        calibrate(): Calibrates friction data.
        fitMultipleAsperity(): fits load vs friction data to a multiple asperity model.
        fitSingleAsperity(): fits load vs friction data to a single asperity model.
        update_graph(): Updates graphs.
    """
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
        self.ui.actionExportFrictionProfiles.triggered.connect(self.exportFrictionProfiles)
        self.ui.actionOffsetFromFZ.triggered.connect(self.openForceRampGUI)
        self.ui.actionFitSingleAsperity.triggered.connect(self.fitSingleAsperity)
        self.ui.actionFitMultipleAsperity.triggered.connect(self.fitMultipleAsperity)
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
        self.popt = None
        self.frictionFitted = 'No'
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

    def exportFrictionProfiles(self):

        x_profile = np.arange(int(self.ui.lineEditMinCol.text()),int(self.ui.lineEditMaxCol.text())+1,1)
        x_profile_full = np.arange(0,self.Files[0].Image[0]['Columns'],1)

        if self.selectedScanMode == 'Interleave':
            frictionRetrace = self.Files[self.currentFileIndex].getChannel('Friction','Interleave','Retrace')
        elif self.selectedScanMode == 'Main':
            frictionRetrace = self.Files[self.currentFileIndex].getChannel('Friction','Main','Retrace')

        if self.selectedScanMode == 'Interleave':
            frictionTrace = self.Files[self.currentFileIndex].getChannel('Friction','Interleave','Trace')
        elif self.selectedScanMode == 'Main':
            frictionTrace = self.Files[self.currentFileIndex].getChannel('Friction','Main','Trace')
        
        

        trace_full = frictionTrace['Image Data'][self.currentRow,:]
        retrace_full = frictionRetrace['Image Data'][self.currentRow,:]
        trace = frictionTrace['Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1]
        retrace = frictionRetrace['Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1]

        
        caption1 = "Save File full"
        caption2 = "Save File short"
        directory = os.getcwd()
        filter_mask = "All Files (*)"
        name_full = QFileDialog.getSaveFileName(self, caption1, directory, filter_mask)
        name_short = QFileDialog.getSaveFileName(self, caption2, directory, filter_mask)
        np.savetxt(name_full[0], np.transpose([x_profile_full, trace_full, retrace_full]), delimiter="\t")
        np.savetxt(name_short[0], np.transpose([x_profile, trace, retrace]), delimiter="\t")

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

    def fitMultipleAsperity(self):
        if (self.selectedScanMode == 'Main' and self.dataCalibrated == True):
             x = self.loadForce
             y=self.frictionRampV_mean*self.frictionCalibrationConstant
             self.popt, pcov = curve_fit(functionMultipleAsperity, x, y)
             self.ui.frictionCoefficientLabel.setText('{0:.2f}'.format(self.popt[0]))
             self.ui.adhesionForceLabel.setText('{0:.2f}'.format(self.popt[1]))
             self.frictionFitted = 'MultipleAsperity'
             self.update_graph()
             
    def fitSingleAsperity(self):
        
         if (self.selectedScanMode == 'Main' and self.dataCalibrated == True):
             x = self.loadForce
             y=self.frictionRampV_mean*self.frictionCalibrationConstant
             self.popt, pcov = curve_fit(functionSingleAsperity, x, y)
             self.ui.frictionCoefficientLabel.setText('{0:.2f}'.format(self.popt[0]))
             self.ui.adhesionForceLabel.setText('{0:.2f}'.format(self.popt[1]))
             self.frictionFitted = 'SingleAsperity'
             self.update_graph()

    

    def update_graph(self):
        """
        Updates the graphs of the GUI.
        Specifically, there are 6 graphs with the lay out of 3 rows and 2 columns.
        Row 1, Column 1 (Axes1): Height Image.
        Row 1, Column 2 (Axes2): Height Profile.
        Row 2, Column 1 (Axes3): Friction Image (Trace).
        Row 2, Column 2 (Axes4): Friction Profiles.
        Row 3, Column 1 (Axes5): Friction Image (ReTrace).
        Row 3, Column 2 (Axes6): Friction Ramp.
        """

        # Check that Row and Column numbers are within limits. If not, set to boundaries.
        if int(self.ui.lineEditMinCol.text())<0:
            self.ui.lineEditMinCol.setText(str(0))
        if int(self.ui.lineEditMaxCol.text()) > self.Files[0].Image[0]['Columns']-1:
            self.ui.lineEditMaxCol.setText(str(self.Files[0].Image[0]['Columns']-1))
        if int(self.ui.lineEditMinRow.text())<0:
            self.ui.lineEditMinRow.setText(str(0))
        if int(self.ui.lineEditMaxRow.text()) > self.Files[0].Image[0]['Rows']-1:
            self.ui.lineEditMaxRow.setText(str(self.Files[0].Image[0]['Rows']-1))

        # Relative values of the min and max columns with respect to the total number of columns.
        # It is needed later on to draw a line over the images indicating the columns used for calculations.
        x_min = int(self.ui.lineEditMinCol.text())/self.Files[0].Image[0]['Columns']
        x_max = int(self.ui.lineEditMaxCol.text())/self.Files[0].Image[0]['Columns']

        # Creates numpy arrays containing the columns of relevance for the friction profiles. Both the selected and
        # the full profiles. It is used later on to plot the selected and full profiles with different type of lines.
        x_profile = np.arange(int(self.ui.lineEditMinCol.text()),int(self.ui.lineEditMaxCol.text())+1,1)
        x_profile_full = np.arange(0,self.Files[0].Image[0]['Columns'],1)

        # Calculates friction once more. I call this function here as the function update_graph()
        # is sometines called when friction relevant data/parametes have changed.
        self.calculateFriction()        

        # Axes 1: Height Image
        # Draws the image:
        self.ui.mplWidget.canvas.axes1.clear()
        self.ui.mplWidget.canvas.axes1.set_axis_off()
        topography = self.Files[self.currentFileIndex].getChannel('Height','Main','Retrace')
        self.ui.mplWidget.canvas.axes1.imshow(topography['Processed Image Data'], cmap='gray', aspect='auto')
        # Draws on to of the image a red line indicating the columns used for calculations
        self.ui.mplWidget.canvas.axes1.axhline(y=self.currentRow,xmin=x_min,xmax=x_max,color='red')
        self.ui.mplWidget.canvas.axes1.set_title('Height')

        # Axes 2: Height profile.
        # Draws a dashed line for the full profile
        # And on top a solid line for the selected profile.
        self.ui.mplWidget.canvas.axes2.clear()
        self.ui.mplWidget.canvas.axes2.plot(x_profile_full,topography['Processed Image Data'][self.currentRow,:],'--')
        self.ui.mplWidget.canvas.axes2.plot(x_profile,topography['Processed Image Data'][self.currentRow,int(self.ui.lineEditMinCol.text()):int(self.ui.lineEditMaxCol.text())+1],'b')
        self.ui.mplWidget.canvas.axes2.set_title('Height Profile')
        self.ui.mplWidget.canvas.axes2.set_ylabel('Height (nm)')

        # Axes 3: Friction Image (Trace)
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

        # Axes 5: Friction Image (ReTrace)
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
        

        # Axes 4: Friction Profiles
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
                    
            

        # Axes 6: Friction Ramp
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
                self.ui.mplWidget.canvas.axes6.set_xlabel('Load (V)')
            elif self.dataView == 'Calibrated':
                self.ui.mplWidget.canvas.axes6.errorbar(
                    x=self.loadForce,
                    y=self.frictionRampV_mean*self.frictionCalibrationConstant,
                    yerr=self.frictionRampV_std*self.frictionCalibrationConstant
                )
                self.ui.mplWidget.canvas.axes6.plot(self.loadForce[self.currentFileIndex],self.frictionRampV_mean[self.currentFileIndex]*self.frictionCalibrationConstant,'ro')
                self.ui.mplWidget.canvas.axes6.set_ylabel('Friction (N)')
                self.ui.mplWidget.canvas.axes6.set_xlabel('Load (N)')

                # Plot fit to friction
                if self.frictionFitted == 'SingleAsperity':
                    self.ui.mplWidget.canvas.axes6.plot(self.loadForce, functionSingleAsperity(self.loadForce, *self.popt), 'g--')
                elif self.frictionFitted == 'MultipleAsperity':
                    self.ui.mplWidget.canvas.axes6.plot(self.loadForce, functionMultipleAsperity(self.loadForce, *self.popt), 'g--')

        self.ui.mplWidget.canvas.figure.tight_layout()
        self.ui.mplWidget.canvas.draw()

        self.ui.labelImageName.setText("File: " + self.fileList[self.currentFileIndex])
