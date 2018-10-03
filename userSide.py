# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ECE\ECE 146\projects\project1\client.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(958, 607)
        self.sendButton = QtWidgets.QPushButton(Dialog)
        self.sendButton.setGeometry(QtCore.QRect(670, 530, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.sendButton.setFont(font)
        self.sendButton.setAutoFillBackground(False)
        self.sendButton.setObjectName("sendButton")
        self.inputText = QtWidgets.QLineEdit(Dialog)
        self.inputText.setGeometry(QtCore.QRect(220, 530, 441, 20))
        self.inputText.setObjectName("inputText")

        self.messagesDisplay = QtWidgets.QListWidget(Dialog)
        self.messagesDisplay.setGeometry(QtCore.QRect(220, 160, 521, 351))
        self.messagesDisplay.setObjectName("messagesDisplay")

        self.connectToServer = QtWidgets.QPushButton(Dialog)
        self.connectToServer.setGeometry(QtCore.QRect(800, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.connectToServer.setFont(font)
        self.connectToServer.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.connectToServer.setObjectName("connectToServer")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 70, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Modern")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connections
        self.connectToServer.clicked.connect(self.connectServer)
        self.sendButton.clicked.connect(self.sendMessage)
        

        # Socket variables
        serverPort = 12000 # desire port to communicate

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sendButton.setText(_translate("Dialog", "Send"))
        self.connectToServer.setText(_translate("Dialog", "Connect"))
        self.label.setText(_translate("Dialog", "Immediate Messaging Application"))

        # added function to connect to server
    def connectServer(self):
        print("I clicked")


    def sendMessage(self):
        print("here n stuff")
        value = self.inputText.text() # input textbox
        self.inputText.clear()
        self.messagesDisplay.addItem(value)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

