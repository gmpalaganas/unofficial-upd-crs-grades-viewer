# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(364, 122)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 151))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.unameLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.unameLineEdit.setObjectName(_fromUtf8("unameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.unameLineEdit)
        self.passwordLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwordLineEdit)
        self.unameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.unameLabel.setObjectName(_fromUtf8("unameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.unameLabel)
        self.passwordLabel = QtGui.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.passwordLabel)
        self.loginButton = QtGui.QPushButton(self.formLayoutWidget)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.loginButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Login", None))
        self.unameLabel.setText(_translate("MainWindow", "Username", None))
        self.passwordLabel.setText(_translate("MainWindow", "Password", None))
        self.loginButton.setText(_translate("MainWindow", "Login", None))

