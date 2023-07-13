# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spravochnik.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 760)
        MainWindow.setMinimumSize(QtCore.QSize(760, 760))
        MainWindow.setStyleSheet(" font-family: -apple-system, system-ui, \"Segoe UI\", Helvetica, Arial, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\";\n"
"background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("border-radius: 8px;\n"
"color: black;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setAccessibleName("")
        self.lineEdit.setStyleSheet("appearance: none; background-color: #FAFBFC; border: 1px solid rgba(27, 31, 35, 0.15);border-radius: 6px;box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;box-sizing: border-box;color: #24292E;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: #FAFBFC;\n"
"  border: 1px solid rgba(27, 31, 35, 0.15);\n"
"  border-radius: 6px;\n"
"  box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;\n"
"  box-sizing: border-box;\n"
"  color: #24292E;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: -apple-system, system-ui, \"Segoe UI\", Helvetica, Arial, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"  line-height: 20px;\n"
"  list-style: none;\n"
"  padding: 6px 16px;\n"
"  position: relative;\n"
"  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  white-space: nowrap;\n"
"  word-wrap: break-word;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("background-color: #FAFBFC;\n"
"  border: 1px solid rgba(27, 31, 35, 0.15);\n"
"  border-radius: 6px;\n"
"  box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;\n"
"  box-sizing: border-box;\n"
"  color: #24292E;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: -apple-system, system-ui, \"Segoe UI\", Helvetica, Arial, sans-serif, \"Apple Color Emoji\", \"Segoe UI Emoji\";\n"
"  font-size: 12px;\n"
"  font-weight: 500;\n"
"  line-height: 20px;\n"
"  list-style: none;\n"
"  padding: 6px 16px;\n"
"  position: relative;\n"
"  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  white-space: nowrap;\n"
"  word-wrap: break-word;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_43 = QtWidgets.QLabel(self.page_2)
        self.label_43.setGeometry(QtCore.QRect(20, 20, 921, 531))
        self.label_43.setStyleSheet("background-color: rgb(239, 238, 255);")
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap(":/icon/img/welcomescreen.png"))
        self.label_43.setObjectName("label_43")
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите ФИО или номер телефона или логин пользователя"))
        self.pushButton.setText(_translate("MainWindow", "Найти"))
        self.pushButton_2.setText(_translate("MainWindow", "Войти"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
