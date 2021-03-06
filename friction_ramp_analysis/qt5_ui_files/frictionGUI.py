# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frictionGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrictionGUI(object):
    def setupUi(self, FrictionGUI):
        FrictionGUI.setObjectName("FrictionGUI")
        FrictionGUI.resize(889, 811)
        self.centralwidget = QtWidgets.QWidget(FrictionGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.labelImageName = QtWidgets.QLabel(self.centralwidget)
        self.labelImageName.setMinimumSize(QtCore.QSize(350, 17))
        self.labelImageName.setObjectName("labelImageName")
        self.horizontalLayout_2.addWidget(self.labelImageName)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.mplWidget = mplwidget6plots(self.centralwidget)
        self.mplWidget.setMinimumSize(QtCore.QSize(400, 600))
        self.mplWidget.setAutoFillBackground(True)
        self.mplWidget.setObjectName("mplWidget")
        self.horizontalLayout.addWidget(self.mplWidget)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_19.addLayout(self.verticalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(45, 25))
        self.label.setMaximumSize(QtCore.QSize(41, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.lineEditImageNo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditImageNo.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditImageNo.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditImageNo.setFont(font)
        self.lineEditImageNo.setObjectName("lineEditImageNo")
        self.horizontalLayout_12.addWidget(self.lineEditImageNo)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButtonPrevImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPrevImage.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonPrevImage.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonPrevImage.setFont(font)
        self.pushButtonPrevImage.setObjectName("pushButtonPrevImage")
        self.horizontalLayout_14.addWidget(self.pushButtonPrevImage)
        self.pushButtonNextImage = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextImage.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonNextImage.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonNextImage.setFont(font)
        self.pushButtonNextImage.setObjectName("pushButtonNextImage")
        self.horizontalLayout_14.addWidget(self.pushButtonNextImage)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)
        spacerItem11 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(45, 25))
        self.label_2.setMaximumSize(QtCore.QSize(41, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        self.lineEditRowNo = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditRowNo.sizePolicy().hasHeightForWidth())
        self.lineEditRowNo.setSizePolicy(sizePolicy)
        self.lineEditRowNo.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditRowNo.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditRowNo.setFont(font)
        self.lineEditRowNo.setObjectName("lineEditRowNo")
        self.horizontalLayout_13.addWidget(self.lineEditRowNo)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonPrevRow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPrevRow.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonPrevRow.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonPrevRow.setFont(font)
        self.pushButtonPrevRow.setObjectName("pushButtonPrevRow")
        self.horizontalLayout_4.addWidget(self.pushButtonPrevRow)
        self.pushButtonNextRow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNextRow.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButtonNextRow.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonNextRow.setFont(font)
        self.pushButtonNextRow.setObjectName("pushButtonNextRow")
        self.horizontalLayout_4.addWidget(self.pushButtonNextRow)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_15.addWidget(self.label_3)
        self.lineEditMinRow = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMinRow.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditMinRow.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditMinRow.setFont(font)
        self.lineEditMinRow.setObjectName("lineEditMinRow")
        self.horizontalLayout_15.addWidget(self.lineEditMinRow)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_15.addWidget(self.label_4)
        self.lineEditMaxRow = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMaxRow.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditMaxRow.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditMaxRow.setFont(font)
        self.lineEditMaxRow.setObjectName("lineEditMaxRow")
        self.horizontalLayout_15.addWidget(self.lineEditMaxRow)
        spacerItem13 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_16.addWidget(self.label_10)
        self.lineEditMinCol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMinCol.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditMinCol.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditMinCol.setFont(font)
        self.lineEditMinCol.setObjectName("lineEditMinCol")
        self.horizontalLayout_16.addWidget(self.lineEditMinCol)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_16.addWidget(self.label_11)
        self.lineEditMaxCol = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMaxCol.setMinimumSize(QtCore.QSize(50, 25))
        self.lineEditMaxCol.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditMaxCol.setFont(font)
        self.lineEditMaxCol.setObjectName("lineEditMaxCol")
        self.horizontalLayout_16.addWidget(self.lineEditMaxCol)
        spacerItem14 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem15 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.pushButtonUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUpdate.setMinimumSize(QtCore.QSize(89, 25))
        self.pushButtonUpdate.setMaximumSize(QtCore.QSize(89, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonUpdate.setFont(font)
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.horizontalLayout_5.addWidget(self.pushButtonUpdate)
        spacerItem16 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem17 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem17)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lineEditTipHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTipHeight.setMinimumSize(QtCore.QSize(50, 16))
        self.lineEditTipHeight.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditTipHeight.setFont(font)
        self.lineEditTipHeight.setObjectName("lineEditTipHeight")
        self.horizontalLayout_8.addWidget(self.lineEditTipHeight)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        spacerItem18 = QtWidgets.QSpacerItem(21, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem18)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEditLatSens = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLatSens.setMinimumSize(QtCore.QSize(50, 16))
        self.lineEditLatSens.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditLatSens.setFont(font)
        self.lineEditLatSens.setObjectName("lineEditLatSens")
        self.horizontalLayout_7.addWidget(self.lineEditLatSens)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEditTorsConst = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTorsConst.setMinimumSize(QtCore.QSize(50, 16))
        self.lineEditTorsConst.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditTorsConst.setFont(font)
        self.lineEditTorsConst.setObjectName("lineEditTorsConst")
        self.horizontalLayout_7.addWidget(self.lineEditTorsConst)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        spacerItem19 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem19)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.lineEditVertSens = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditVertSens.setMinimumSize(QtCore.QSize(50, 16))
        self.lineEditVertSens.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditVertSens.setFont(font)
        self.lineEditVertSens.setObjectName("lineEditVertSens")
        self.horizontalLayout_6.addWidget(self.lineEditVertSens)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.lineEditNormConst = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNormConst.setMinimumSize(QtCore.QSize(50, 16))
        self.lineEditNormConst.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditNormConst.setFont(font)
        self.lineEditNormConst.setObjectName("lineEditNormConst")
        self.horizontalLayout_6.addWidget(self.lineEditNormConst)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_6)
        spacerItem20 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem20)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.lineEditInitV = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInitV.setMinimumSize(QtCore.QSize(50, 16))
        self.lineEditInitV.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditInitV.setFont(font)
        self.lineEditInitV.setObjectName("lineEditInitV")
        self.horizontalLayout_3.addWidget(self.lineEditInitV)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.lineEditFinalV = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFinalV.setMinimumSize(QtCore.QSize(50, 16))
        self.lineEditFinalV.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEditFinalV.setFont(font)
        self.lineEditFinalV.setObjectName("lineEditFinalV")
        self.horizontalLayout_3.addWidget(self.lineEditFinalV)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_3)
        spacerItem21 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem22 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem22)
        self.pushButtonCalibrate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCalibrate.setMinimumSize(QtCore.QSize(89, 25))
        self.pushButtonCalibrate.setMaximumSize(QtCore.QSize(89, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonCalibrate.setFont(font)
        self.pushButtonCalibrate.setObjectName("pushButtonCalibrate")
        self.horizontalLayout_11.addWidget(self.pushButtonCalibrate)
        spacerItem23 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem23)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem24 = QtWidgets.QSpacerItem(17, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem24)
        self.horizontalLayout_19.addLayout(self.verticalLayout_4)
        spacerItem25 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem25)
        self.gridLayout.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem26, 2, 0, 1, 1)
        FrictionGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrictionGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        self.menuFriction_Ramp = QtWidgets.QMenu(self.menuExport)
        self.menuFriction_Ramp.setObjectName("menuFriction_Ramp")
        self.menuInterleave_Ramp = QtWidgets.QMenu(self.menuExport)
        self.menuInterleave_Ramp.setObjectName("menuInterleave_Ramp")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuScan_Type = QtWidgets.QMenu(self.menubar)
        self.menuScan_Type.setObjectName("menuScan_Type")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        FrictionGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrictionGUI)
        self.statusbar.setObjectName("statusbar")
        FrictionGUI.setStatusBar(self.statusbar)
        self.actionLoadImages = QtWidgets.QAction(FrictionGUI)
        self.actionLoadImages.setObjectName("actionLoadImages")
        self.actionClose = QtWidgets.QAction(FrictionGUI)
        self.actionClose.setObjectName("actionClose")
        self.actionExportMainRaw = QtWidgets.QAction(FrictionGUI)
        self.actionExportMainRaw.setObjectName("actionExportMainRaw")
        self.actionExportMainCalibrated = QtWidgets.QAction(FrictionGUI)
        self.actionExportMainCalibrated.setObjectName("actionExportMainCalibrated")
        self.actionOffsetFromFZ = QtWidgets.QAction(FrictionGUI)
        self.actionOffsetFromFZ.setObjectName("actionOffsetFromFZ")
        self.actionMainScan = QtWidgets.QAction(FrictionGUI)
        self.actionMainScan.setCheckable(True)
        self.actionMainScan.setChecked(True)
        self.actionMainScan.setObjectName("actionMainScan")
        self.actionInterleaveScan = QtWidgets.QAction(FrictionGUI)
        self.actionInterleaveScan.setCheckable(True)
        self.actionInterleaveScan.setObjectName("actionInterleaveScan")
        self.actionViewRawData = QtWidgets.QAction(FrictionGUI)
        self.actionViewRawData.setObjectName("actionViewRawData")
        self.actionViewCalibratedData = QtWidgets.QAction(FrictionGUI)
        self.actionViewCalibratedData.setObjectName("actionViewCalibratedData")
        self.actionExportInterleaveRaw = QtWidgets.QAction(FrictionGUI)
        self.actionExportInterleaveRaw.setObjectName("actionExportInterleaveRaw")
        self.actionExportInterleaveCalibrated = QtWidgets.QAction(FrictionGUI)
        self.actionExportInterleaveCalibrated.setObjectName("actionExportInterleaveCalibrated")
        self.menuFile.addAction(self.actionLoadImages)
        self.menuFile.addAction(self.actionClose)
        self.menuFriction_Ramp.addAction(self.actionExportMainRaw)
        self.menuFriction_Ramp.addAction(self.actionExportMainCalibrated)
        self.menuInterleave_Ramp.addAction(self.actionExportInterleaveRaw)
        self.menuInterleave_Ramp.addAction(self.actionExportInterleaveCalibrated)
        self.menuExport.addAction(self.menuFriction_Ramp.menuAction())
        self.menuExport.addAction(self.menuInterleave_Ramp.menuAction())
        self.menuAnalysis.addAction(self.actionOffsetFromFZ)
        self.menuScan_Type.addAction(self.actionMainScan)
        self.menuScan_Type.addAction(self.actionInterleaveScan)
        self.menuView.addAction(self.actionViewRawData)
        self.menuView.addAction(self.actionViewCalibratedData)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuScan_Type.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())

        self.retranslateUi(FrictionGUI)
        QtCore.QMetaObject.connectSlotsByName(FrictionGUI)

    def retranslateUi(self, FrictionGUI):
        _translate = QtCore.QCoreApplication.translate
        FrictionGUI.setWindowTitle(_translate("FrictionGUI", "FrictionRampGUI"))
        self.labelImageName.setText(_translate("FrictionGUI", "-"))
        self.label.setText(_translate("FrictionGUI", "Image #"))
        self.lineEditImageNo.setText(_translate("FrictionGUI", "0"))
        self.pushButtonPrevImage.setText(_translate("FrictionGUI", "<"))
        self.pushButtonNextImage.setText(_translate("FrictionGUI", ">"))
        self.label_2.setText(_translate("FrictionGUI", "Row #"))
        self.lineEditRowNo.setText(_translate("FrictionGUI", "0"))
        self.pushButtonPrevRow.setText(_translate("FrictionGUI", "<"))
        self.pushButtonNextRow.setText(_translate("FrictionGUI", ">"))
        self.label_3.setText(_translate("FrictionGUI", "Min Row"))
        self.lineEditMinRow.setText(_translate("FrictionGUI", "0"))
        self.label_4.setText(_translate("FrictionGUI", "Max Row"))
        self.lineEditMaxRow.setText(_translate("FrictionGUI", "0"))
        self.label_10.setText(_translate("FrictionGUI", "Min Col"))
        self.lineEditMinCol.setText(_translate("FrictionGUI", "0"))
        self.label_11.setText(_translate("FrictionGUI", "Max Col"))
        self.lineEditMaxCol.setText(_translate("FrictionGUI", "0"))
        self.pushButtonUpdate.setText(_translate("FrictionGUI", "Update"))
        self.label_5.setText(_translate("FrictionGUI", "Tip Height (nm)"))
        self.lineEditTipHeight.setText(_translate("FrictionGUI", "1e3"))
        self.label_6.setText(_translate("FrictionGUI", "<html><head/><body><p align=\"center\">Lateral </p><p align=\"center\">Sensitivity (rad/V)</p></body></html>"))
        self.lineEditLatSens.setText(_translate("FrictionGUI", "3e-4"))
        self.label_7.setText(_translate("FrictionGUI", "<html><head/><body><p align=\"center\">Tors Const</p><p align=\"center\">(nN*nm/rad)</p></body></html>"))
        self.lineEditTorsConst.setText(_translate("FrictionGUI", "2e9"))
        self.label_8.setText(_translate("FrictionGUI", "<html><head/><body><p align=\"center\">Vertical </p><p align=\"center\">Sensitivity (nm/V)</p></body></html>"))
        self.lineEditVertSens.setText(_translate("FrictionGUI", "1"))
        self.label_9.setText(_translate("FrictionGUI", "<html><head/><body><p align=\"center\">Normal </p><p align=\"center\">Constant (N/m)</p></body></html>"))
        self.lineEditNormConst.setText(_translate("FrictionGUI", "1"))
        self.label_12.setText(_translate("FrictionGUI", "<html><head/><body><p align=\"center\">Initial</p><p align=\"center\">Voltage (V)</p></body></html>"))
        self.lineEditInitV.setText(_translate("FrictionGUI", "0"))
        self.label_13.setText(_translate("FrictionGUI", "<html><head/><body><p align=\"center\">Final</p><p align=\"center\">Voltage (V)</p></body></html>"))
        self.lineEditFinalV.setText(_translate("FrictionGUI", "0"))
        self.pushButtonCalibrate.setText(_translate("FrictionGUI", "Calibrate"))
        self.menuFile.setTitle(_translate("FrictionGUI", "File"))
        self.menuExport.setTitle(_translate("FrictionGUI", "Export"))
        self.menuFriction_Ramp.setTitle(_translate("FrictionGUI", "Friction Ramp"))
        self.menuInterleave_Ramp.setTitle(_translate("FrictionGUI", "Interleave Ramp"))
        self.menuAnalysis.setTitle(_translate("FrictionGUI", "Analysis"))
        self.menuScan_Type.setTitle(_translate("FrictionGUI", "Scan Type"))
        self.menuView.setTitle(_translate("FrictionGUI", "View"))
        self.actionLoadImages.setText(_translate("FrictionGUI", "Load Images"))
        self.actionClose.setText(_translate("FrictionGUI", "Close"))
        self.actionExportMainRaw.setText(_translate("FrictionGUI", "Raw"))
        self.actionExportMainCalibrated.setText(_translate("FrictionGUI", "Calibrated"))
        self.actionOffsetFromFZ.setText(_translate("FrictionGUI", "Offset from FZ"))
        self.actionMainScan.setText(_translate("FrictionGUI", "Main"))
        self.actionInterleaveScan.setText(_translate("FrictionGUI", "Interleave"))
        self.actionViewRawData.setText(_translate("FrictionGUI", "Raw Data"))
        self.actionViewCalibratedData.setText(_translate("FrictionGUI", "Calibrated Data"))
        self.actionExportInterleaveRaw.setText(_translate("FrictionGUI", "Raw"))
        self.actionExportInterleaveCalibrated.setText(_translate("FrictionGUI", "Calibrated"))
from .mplwidget6plots import mplwidget6plots
