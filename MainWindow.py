# Copyright (C) 2021 Arbaaz Laskar
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 414)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 69))
        self.textEdit_2.setStyleSheet("font: 20pt \"Sans Serif\";")
        self.textEdit_2.setMarkdown("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 0, 0, 1, 6)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("font: 20pt \"Sans Serif\";")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(91, 31))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(151, 31))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(84, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(151, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(151, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(
            self.pushButton_7, 1, 3, 1, 3, QtCore.Qt.AlignRight)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowser_2.setStyleSheet("font: 20pt \"Sans Serif\";")
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 2, 0, 1, 6)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(84, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hermes"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.textEdit_2.setPlaceholderText(_translate(
            "MainWindow", "Enter the quote you want to find here "))
        self.pushButton_2.setText(_translate("MainWindow", "Previous Page"))
        self.pushButton.setText(_translate("MainWindow", "First Page"))
        self.pushButton_5.setText(_translate("MainWindow", "Search Book"))
        self.pushButton_3.setText(_translate("MainWindow", "Next Page"))
        self.pushButton_6.setText(_translate(
            "MainWindow", "Search Dictionary"))
        self.pushButton_7.setText(_translate(
            "MainWindow", "Show Dictionary Index"))
        self.pushButton_4.setText(_translate("MainWindow", "Last Page"))
