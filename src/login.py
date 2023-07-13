from PyQt5 import QtWidgets
from loginsystem import Ui_Dialog
import requests
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMessageBox
from requests.adapters import HTTPAdapter, Response
from bs4 import BeautifulSoup

class QtLoginSystem(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(QtLoginSystem, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icon/img/logo.png"))
        self.setWindowTitle("Вход")
        self.ui.loginButton.clicked.connect(self.saveConfig)
        self.settings = QSettings('EFKO', 'spravochnik')
        site = "https://helpdesk.efko.ru"
        self.httpAdapter = HTTPAdapter(max_retries=2)
        self.httpSession = requests.Session()
        self.httpSession.mount(site, self.httpAdapter)
        self.httpSession.headers.update({
            'origin': site,
            'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Chrome/102.0.5005.63 Safari/537.36'
        })
        self.is_login = False
        self.config()

    def parseCSRF(self, html: str) -> str:
        """Получение csrf из html form"""
        soup = BeautifulSoup(html.replace('\\"', '"'), 'lxml')
        csrf = soup.select_one('input[name="_csrf"]')
        if csrf:
            return csrf.get('value')

    def authorize(self):
        if self.is_login:
            self.httpSession.get("https://helpdesk.efko.ru/user/login/logout", verify=True)
            self.is_login = False
        url = "https://helpdesk.efko.ru"
        response = self.httpSession.get(url, verify=True)
        token = self.parseCSRF(response.text)
        query_data = {'Login[username]': self.ui.loginBox.text(),
                      'Login[password]': self.ui.passwdBox.text(),
                      'Login[rememberMe]': 0,
                      '_csrf': token}
        print(token)
        response = self.httpSession.post(url+'/user/login', data=query_data, verify=True)
        if ('Неправильный логин или пароль' in response.text) | ('input type="text" id="login-username' in response.text):
            msg = QMessageBox()
            msg.about(self, "Ошибка", "Неправильный логин или пароль")
        else:
            self.hide()
            self.is_login = True

    def getUserPhoto(self, isui) -> str:
        url = 'https://helpdesk.efko.ru/user/edit/correct-data?code='
        print(url+isui)
        response = self.httpSession.get(url+isui, verify=True)
        soup = BeautifulSoup(response.text.replace('\\"', '"'), 'lxml')
        div = soup.find("div", {"class": "thumbnail"})
        img = div.find("img")
        if img.has_attr('src'):
            usrpic = img['src'].replace('data:image/jpg;base64,', '')
            return usrpic

    def saveConfig(self):
        login = self.ui.loginBox.text()
        passwd = self.ui.passwdBox.text()
        self.settings.setValue("Login", login)
        self.settings.setValue("Password", passwd)
        self.authorize()

    def config(self):
        login = self.settings.value("Login", '')
        self.ui.loginBox.setText(login)
        password = self.settings.value("Password", '')
        self.ui.passwdBox.setText(password)
        if login and password:
            self.authorize()
        else:
            self.show()

