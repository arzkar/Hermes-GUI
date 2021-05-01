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
import sys
import os
from PySide2 import QtWidgets, QtGui
from MainWindow import Ui_MainWindow
from utils.pages import get_output


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.i = 0
        self.setWindowIcon(QtGui.QIcon(resource_path('icon.ico')))
        self.pushButton.clicked.connect(
            self.first_button)
        self.pushButton_2.clicked.connect(
            self.prev_button)
        self.pushButton_3.clicked.connect(
            self.next_button)
        self.pushButton_4.clicked.connect(
            self.last_button)
        self.pushButton_5.clicked.connect(
            self.quote_output)  # Click Search Book
        self.pushButton_6.clicked.connect(
            self.dict_output)  # Click Search Dictionary
        self.pushButton_7.clicked.connect(
            self.index_output)  # Click Show Dictionary Index

    def quote_output(self, *args, obj=None, **kwargs):
        self.x = 1
        self.arg = self.textEdit_2.toPlainText()
        self.title, self.description, self.url, self.page_limit = get_output(
            self.x, self.arg)
        self.textBrowser_2.setMarkdown(
            "<a href=\""+self.url+"\" >"+self.title+"</a>")
        self.textBrowser.setMarkdown(self.description)

    def dict_output(self, *args, obj=None, **kwargs):
        self.x = 2
        self.arg = self.textEdit_2.toPlainText()
        self.title, self.description, self.url, self.page_limit = get_output(self.x,
                                                                             self.arg)
        self.textBrowser_2.setPlainText(self.title)
        self.textBrowser.setMarkdown(self.description)

    def index_output(self, *args, obj=None, **kwargs):
        self.x = 3
        self.arg = self.textEdit_2.toPlainText()
        self.title, self.description, self.url, self.page_limit = get_output(self.x,
                                                                             self.arg)
        self.textBrowser_2.setPlainText(self.title)
        self.textBrowser.setMarkdown(self.description)

    def first_button(self):
        self.i = 0
        self.title, self.description, self.url, self.page_limit = get_output(
            self.x, self.arg, self.i)
        self.textBrowser_2.setMarkdown(
            "<a href=\""+self.url+"\" >"+self.title+"</a>")
        self.textBrowser.setMarkdown(self.description)

    def prev_button(self):
        if self.i > 0:
            self.i -= 1
            self.title, self.description, self.url, self.page_limit = get_output(self.x,
                                                                                 self.arg, self.i)
            self.textBrowser_2.setMarkdown(
                "<a href=\""+self.url+"\" >"+self.title+"</a>")
            self.textBrowser.setMarkdown(self.description)

    def next_button(self):
        if self.i < self.page_limit:
            self.i += 1
            self.title, self.description, self.url, self.page_limit = get_output(self.x,
                                                                                 self.arg, self.i)
            self.textBrowser_2.setMarkdown(
                "<a href=\""+self.url+"\" >"+self.title+"</a>")
            self.textBrowser.setMarkdown(self.description)

    def last_button(self):
        self.i = self.page_limit-1
        self.title, self.description, self.url, self.page_limit = get_output(self.x,
                                                                             self.arg, self.i)
        self.textBrowser_2.setMarkdown(
            "<a href=\""+self.url+"\" >"+self.title+"</a>")
        self.textBrowser.setMarkdown(self.description)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
