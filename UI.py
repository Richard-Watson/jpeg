# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTab = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTab.setGeometry(QtCore.QRect(0, 0, 331, 201))
        self.MainTab.setObjectName("MainTab")
        self.Encode = QtWidgets.QWidget()
        self.Encode.setObjectName("Encode")
        self.Encode_Container_LineEdit = QtWidgets.QLineEdit(self.Encode)
        self.Encode_Container_LineEdit.setGeometry(QtCore.QRect(0, 35, 290, 20))
        self.Encode_Container_LineEdit.setObjectName("Encode_Container_LineEdit")
        self.Encode_Container_Label = QtWidgets.QLabel(self.Encode)
        self.Encode_Container_Label.setGeometry(QtCore.QRect(0, 10, 325, 20))
        self.Encode_Container_Label.setObjectName("Encode_Container_Label")
        self.Encode_Container_ToolButton = QtWidgets.QToolButton(self.Encode)
        self.Encode_Container_ToolButton.setGeometry(QtCore.QRect(300, 35, 25, 20))
        self.Encode_Container_ToolButton.setObjectName("Encode_Container_ToolButton")
        self.Encode_InputFile_LineEdit = QtWidgets.QLineEdit(self.Encode)
        self.Encode_InputFile_LineEdit.setGeometry(QtCore.QRect(0, 90, 290, 20))
        self.Encode_InputFile_LineEdit.setObjectName("Encode_InputFile_LineEdit")
        self.Encode_InputFile_ToolButton = QtWidgets.QToolButton(self.Encode)
        self.Encode_InputFile_ToolButton.setGeometry(QtCore.QRect(300, 90, 25, 20))
        self.Encode_InputFile_ToolButton.setObjectName("Encode_InputFile_ToolButton")
        self.Encode_InputFile_Label = QtWidgets.QLabel(self.Encode)
        self.Encode_InputFile_Label.setGeometry(QtCore.QRect(0, 65, 325, 20))
        self.Encode_InputFile_Label.setObjectName("Encode_InputFile_Label")
        self.Encode_Password_LineEdit = QtWidgets.QLineEdit(self.Encode)
        self.Encode_Password_LineEdit.setGeometry(QtCore.QRect(0, 150, 240, 20))
        self.Encode_Password_LineEdit.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.Encode_Password_LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Encode_Password_LineEdit.setObjectName("Encode_Password_LineEdit")
        self.Encode_Password_Label = QtWidgets.QLabel(self.Encode)
        self.Encode_Password_Label.setGeometry(QtCore.QRect(0, 120, 325, 20))
        self.Encode_Password_Label.setObjectName("Encode_Password_Label")
        self.Encode_Password_pushButton = QtWidgets.QPushButton(self.Encode)
        self.Encode_Password_pushButton.setGeometry(QtCore.QRect(245, 150, 80, 20))
        self.Encode_Password_pushButton.setFlat(False)
        self.Encode_Password_pushButton.setObjectName("Encode_Password_pushButton")
        self.MainTab.addTab(self.Encode, "")
        self.Decode = QtWidgets.QWidget()
        self.Decode.setObjectName("Decode")
        self.Decode_Container_Label = QtWidgets.QLabel(self.Decode)
        self.Decode_Container_Label.setGeometry(QtCore.QRect(0, 10, 325, 20))
        self.Decode_Container_Label.setObjectName("Decode_Container_Label")
        self.Decode_Container_LineEdit = QtWidgets.QLineEdit(self.Decode)
        self.Decode_Container_LineEdit.setGeometry(QtCore.QRect(0, 35, 290, 20))
        self.Decode_Container_LineEdit.setObjectName("Decode_Container_LineEdit")
        self.Decode_Container_ToolButton = QtWidgets.QToolButton(self.Decode)
        self.Decode_Container_ToolButton.setGeometry(QtCore.QRect(300, 35, 25, 20))
        self.Decode_Container_ToolButton.setObjectName("Decode_Container_ToolButton")
        self.Decode_Password_Label = QtWidgets.QLabel(self.Decode)
        self.Decode_Password_Label.setGeometry(QtCore.QRect(0, 65, 325, 20))
        self.Decode_Password_Label.setObjectName("Decode_Password_Label")
        self.Decode_Password_LineEdit = QtWidgets.QLineEdit(self.Decode)
        self.Decode_Password_LineEdit.setGeometry(QtCore.QRect(0, 90, 237, 21))
        self.Decode_Password_LineEdit.setInputMethodHints(QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.Decode_Password_LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Decode_Password_LineEdit.setObjectName("Decode_Password_LineEdit")
        self.Decode_Password_pushButton = QtWidgets.QPushButton(self.Decode)
        self.Decode_Password_pushButton.setGeometry(QtCore.QRect(245, 90, 80, 20))
        self.Decode_Password_pushButton.setObjectName("Decode_Password_pushButton")
        self.MainTab.addTab(self.Decode, "")
        self.PNG_Converter = QtWidgets.QWidget()
        self.PNG_Converter.setObjectName("PNG_Converter")
        self.Converter_Container_Label = QtWidgets.QLabel(self.PNG_Converter)
        self.Converter_Container_Label.setGeometry(QtCore.QRect(0, 10, 325, 20))
        self.Converter_Container_Label.setObjectName("Converter_Container_Label")
        self.Converter_Container_LineEdit = QtWidgets.QLineEdit(self.PNG_Converter)
        self.Converter_Container_LineEdit.setGeometry(QtCore.QRect(0, 35, 290, 20))
        self.Converter_Container_LineEdit.setObjectName("Converter_Container_LineEdit")
        self.Converter_Container_ToolButton = QtWidgets.QToolButton(self.PNG_Converter)
        self.Converter_Container_ToolButton.setGeometry(QtCore.QRect(300, 35, 25, 20))
        self.Converter_Container_ToolButton.setObjectName("Converter_Container_ToolButton")
        self.Converter_pushButton = QtWidgets.QPushButton(self.PNG_Converter)
        self.Converter_pushButton.setGeometry(QtCore.QRect(0, 65, 325, 20))
        self.Converter_pushButton.setObjectName("Converter_pushButton")
        self.MainTab.addTab(self.PNG_Converter, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganographer"))
        self.Encode_Container_Label.setText(_translate("MainWindow", "Select Container:"))
        self.Encode_Container_ToolButton.setText(_translate("MainWindow", "..."))
        self.Encode_InputFile_ToolButton.setText(_translate("MainWindow", "..."))
        self.Encode_InputFile_Label.setText(_translate("MainWindow", "Select Input File:"))
        self.Encode_Password_Label.setText(_translate("MainWindow", "Write password:"))
        self.Encode_Password_pushButton.setText(_translate("MainWindow", "Encode"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.Encode), _translate("MainWindow", "Encode"))
        self.Decode_Container_Label.setText(_translate("MainWindow", "Select Container:"))
        self.Decode_Container_ToolButton.setText(_translate("MainWindow", "..."))
        self.Decode_Password_Label.setText(_translate("MainWindow", "Write password:"))
        self.Decode_Password_pushButton.setText(_translate("MainWindow", "Decode"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.Decode), _translate("MainWindow", "Decode"))
        self.Converter_Container_Label.setText(_translate("MainWindow", "Select image:"))
        self.Converter_Container_ToolButton.setText(_translate("MainWindow", "..."))
        self.Converter_pushButton.setText(_translate("MainWindow", "Convert"))
        self.MainTab.setTabText(self.MainTab.indexOf(self.PNG_Converter), _translate("MainWindow", "PNG Converter"))

