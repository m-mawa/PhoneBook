from PyQt5.QtWidgets import QMessageBox, QCompleter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings, QStringListModel
from PyQt5 import QtWidgets
from PyQt5.Qt import QApplication
from directory import Ui_MainWindow
import sys
from login import QtLoginSystem
import os
from tabwidget import TabWidget
from db import DataBase


class QtPhoneBook(QtWidgets.QMainWindow):
    def __init__(self):
        super(QtPhoneBook, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.settings = QSettings('PhoneBook', 'Телефонный справочник')

        self.loginwindow = QtLoginSystem(self)

        self.ui.stackedWidget.setCurrentIndex(0)
        # self.ui.spinBox.valueChanged.connect(self.spinbox)
        self.ui.pushButton.clicked.connect(self.search)
        self.ui.lineEdit.returnPressed.connect(self.search)
        self.ui.lineEdit.setClearButtonEnabled(True)
        self.ui.lineEdit.textChanged.connect(self.clearInput)
        self.ui.pushButton_2.clicked.connect(self.authorization)
        # self.ui.saveButton.clicked.connect(self.edit)
        self.setWindowIcon(QIcon(":/icon/img/logo.png"))
        self.setWindowTitle("Телефонный справочник")

        self.setGeometry(100, 100, 800, 500)
        self.setMinimumSize(200, 200)
        self.db = DataBase()

        self.completer()
        self.loadHistory()


    def completer(self):
        fios = self.db.get_fios()
        print(fios)
        data = []
        for fio in fios:
            data += fio
        model = QStringListModel()
        model.setStringList(data)
        completer = QCompleter()
        completer.setModel(model)
        self.ui.lineEdit.setCompleter(completer)

    def search(self):
        if not self.loginwindow.is_login:
            self.loginwindow.show()
            return
        self.ui.pushButton_2.hide()
        user_input = self.ui.lineEdit.text()
        self.ui.tabWidget.clear()
        try:
            result = self.db.get_ids_by_fio(user_input)
            print(result)
            if len(result) > 0:
                self.print_user_info(result)
                self.saveHistory(user_input)

                return
            user_input = user_input.replace("+", "")
            if len(user_input) == 11:
                user_input = user_input[1:]
            result = self.db.get_ids_by_number(user_input)
            if len(result) > 0:
                self.print_user_info(result)
                self.saveHistory(user_input)
                return
            self.ui.stackedWidget.setCurrentIndex(0)
            msg = QMessageBox()
            msg.about(self, "Ошибка", "Такого пользователя нет")
            self.ui.lineEdit.setText('')
            self.ui.lineEdit.setFocus()
            print('User not found')
        except Exception as e:
            print(e)

    def print_user_info(self, result):
        self.ui.stackedWidget.setCurrentIndex(1)
        print('ddd')
        for id in result:
            records = self.db.get_user_info(id[0])
            print(records)
            if records:
                tab = TabWidget()
                tab.setData(records)
                pic = self.loginwindow.getUserPhoto(records.isui)
                if pic:
                    tab.setPic(pic)
                tab.saveData.connect(self.db.saveData)
                self.ui.tabWidget.addTab(tab, records.Name)
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Пользователь не найден")
                msgBox.setWindowTitle("Ошибка")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()

    def loadHistory(self):
        user = os.getlogin()
        history = self.db.get_history(user)
        for story in history:
            self.ui.comboBox.addItem(story[0])
        self.ui.comboBox.currentTextChanged.connect(self.selectFromHistory)

    def selectFromHistory(self):
        text = self.ui.comboBox.currentText()
        self.ui.lineEdit.setText(text)
        self.ui.pushButton.click()

    def saveHistory(self, user_input):
        user = os.getlogin()
        self.db.save_history(user, user_input)
        self.ui.comboBox.addItem(user_input)

    def authorization(self):
        self.loginwindow.show()

    def clearInput(self, text):
        if not text:
            self.ui.stackedWidget.setCurrentIndex(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    main_window = QtPhoneBook()
    #StyleSetter.setWindowStyle(main_window)
    main_window.show()
    if '_PYIBoot_SPLASH' in os.environ:
        import pyi_splash
        pyi_splash.update_text('UI Loaded ...')
        pyi_splash.close()
    sys.exit(app.exec_())

