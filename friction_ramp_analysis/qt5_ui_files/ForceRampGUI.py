# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForceRampGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForceRampGUI(object):
    def setupUi(self, ForceRampGUI):
        ForceRampGUI.setObjectName("ForceRampGUI")
        ForceRampGUI.resize(714, 548)
        self.centralwidget = QtWidgets.QWidget(ForceRampGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 48, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = mplwidget1plot(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(371, 371))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonGetValue = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGetValue.setObjectName("pushButtonGetValue")
        self.verticalLayout_2.addWidget(self.pushButtonGetValue)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonForward = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonForward.setChecked(True)
        self.radioButtonForward.setObjectName("radioButtonForward")
        self.verticalLayout.addWidget(self.radioButtonForward)
        self.radioButtonBackward = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBackward.setObjectName("radioButtonBackward")
        self.verticalLayout.addWidget(self.radioButtonBackward)
        self.radioButtonBoth = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBoth.setObjectName("radioButtonBoth")
        self.verticalLayout.addWidget(self.radioButtonBoth)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.lineEditValue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValue.setObjectName("lineEditValue")
        self.verticalLayout_2.addWidget(self.lineEditValue)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonSendVi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSendVi.setObjectName("pushButtonSendVi")
        self.horizontalLayout.addWidget(self.pushButtonSendVi)
        self.pushButtonSendVi_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSendVi_2.setObjectName("pushButtonSendVi_2")
        self.horizontalLayout.addWidget(self.pushButtonSendVi_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 2, 1, 1)
        ForceRampGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ForceRampGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 22))
        self.menubar.setObjectName("menubar")
        ForceRampGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ForceRampGUI)
        self.statusbar.setObjectName("statusbar")
        ForceRampGUI.setStatusBar(self.statusbar)

        self.retranslateUi(ForceRampGUI)
        QtCore.QMetaObject.connectSlotsByName(ForceRampGUI)

    def retranslateUi(self, ForceRampGUI):
        _translate = QtCore.QCoreApplication.translate
        ForceRampGUI.setWindowTitle(_translate("ForceRampGUI", "Get Parameters from Force Ramp"))
        self.pushButtonGetValue.setText(_translate("ForceRampGUI", "Vertical \n"
"Offset"))
        self.radioButtonForward.setText(_translate("ForceRampGUI", "Forward"))
        self.radioButtonBackward.setText(_translate("ForceRampGUI", "Backward"))
        self.radioButtonBoth.setText(_translate("ForceRampGUI", "Both"))
        self.pushButtonSendVi.setText(_translate("ForceRampGUI", "Send\n"
"to Vi"))
        self.pushButtonSendVi_2.setText(_translate("ForceRampGUI", "Send\n"
"to Vf"))
from mplwidget1plot import mplwidget1plot
