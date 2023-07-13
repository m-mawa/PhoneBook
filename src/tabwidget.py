from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt, QPoint, QByteArray
from PyQt5.QtGui import QIcon, QPixmap
import newtab
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QTreeWidgetItem, QAction, QMenu
from db import UserInfo

from utils import Utils


class TabWidget(QtWidgets.QWidget):

    saveData = pyqtSignal(str, str, str, int)

    def __init__(self):
        super(TabWidget, self).__init__()

        self.ui = newtab.Ui_newTab()
        self.ui.setupUi(self)

        self.ui.butOpenCreate.clicked.connect(self.openCreate)
        self.ui.butOpenUser.clicked.connect(self.openUser)
        self.ui.butEditUser.clicked.connect(self.editUser)
        self.ui.butSave.clicked.connect(self.edit)

        self.ui.tbLogin.pressed.connect(self.copyToClipboard)
        self.ui.tbName.pressed.connect(self.copyToClipboard)
        self.ui.tbOrg.pressed.connect(self.copyToClipboard)
        self.ui.tbUnit.pressed.connect(self.copyToClipboard)
        self.ui.tbPosition.pressed.connect(self.copyToClipboard)
        self.ui.tbLast.pressed.connect(self.copyToClipboard)
        self.ui.tbSID.pressed.connect(self.copyToClipboard)
        self.ui.tbEmail.pressed.connect(self.copyToClipboard)
        self.ui.tbTel1.pressed.connect(self.copyToClipboard)
        self.ui.tbTel2.pressed.connect(self.copyToClipboard)
        self.ui.tbVPN.pressed.connect(self.copyToClipboard)
        self.ui.tbLocation.pressed.connect(self.copyToClipboard)

        self.ui.pc_name.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.pc_name.customContextMenuRequested.connect(self.menuCreate)


    def menuCreate(self, pos: QPoint):
        print(pos)
        copyPC = QAction(QIcon(":/icon/img/clipboard.png"), "Копировать имя ПК")
        copyIP = QAction(QIcon(":/icon/img/clipboard.png"), "Копировать IP")
        copyMAC = QAction(QIcon(":/icon/img/clipboard.png"), "Копировать MAC")
        pingUser = QAction(QIcon(":/icon/img/clipboard.png"), "Выполнить пинг")
        openC = QAction(QIcon(":/icon/img/clipboard.png"), "Открыть диск С")
        openDir = QAction(QIcon(":/icon/img/clipboard.png"), "Открыть директорию профиля")
        copyPC.setData(0)
        copyIP.setData(1)
        copyMAC.setData(2)
        copyPC.triggered.connect(self.selectInfo)
        copyIP.triggered.connect(self.selectInfo)
        copyMAC.triggered.connect(self.selectInfo)
        pingUser.triggered.connect(self.ping)
        openC.triggered.connect(self.openC)
        openDir.triggered.connect(self.openDir)
        self.menu = QMenu()
        self.menu.addAction(copyPC)
        self.menu.addAction(copyIP)
        self.menu.addAction(copyMAC)
        self.menu.addSeparator()
        self.menu.addAction(pingUser)
        self.menu.addAction(openC)
        self.menu.addAction(openDir)

        point = QPoint(pos.x(), pos.y()+25)
        self.menu.exec(self.ui.pc_name.mapToGlobal(point))

    def ping(self):
        items = self.ui.pc_name.selectedItems()
        Utils().ping(items)

    def openCreate(self):
        Utils().openCreate(self.task_create)

    def openUser(self):
        Utils().openUser(self.isui)

    def openC(self):
        items = self.ui.pc_name.selectedItems()
        Utils().openC(items)

    def openDir(self):
        items = self.ui.pc_name.selectedItems()
        login = self.ui.lineLogin.text()
        Utils().openDir(items, login)

    def editUser(self):
        Utils().editUser(self.isui)

    def selectInfo(self):
        items = self.ui.pc_name.selectedItems()
        if len(items) <= 0:
            return
        item = items[0]
        info = item.text(0).split(' - ')
        print(info)
        action = self.sender()
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(info[action.data()], mode=cb.Clipboard)

        print('Content is copied')


    def copyToClipboard(self):
        if (self.sender().objectName() == 'tbLogin'):
            txt = self.ui.lineLogin.text()
        if (self.sender().objectName() == 'tbName'):
            txt = self.ui.lineName.text()
        if (self.sender().objectName() == 'tbOrg'):
            txt = self.ui.lineOrg.text()
        if (self.sender().objectName() == 'tbUnit'):
            txt = self.ui.lineUnit.text()
        if (self.sender().objectName() == 'tbPosition'):
            txt = self.ui.linePosition.text()
        if (self.sender().objectName() == 'tbLast'):
            txt = self.ui.lineLast.text()
        if (self.sender().objectName() == 'tbSID'):
            txt = self.ui.lineSID.text()
        if (self.sender().objectName() == 'tbEmail'):
            txt = self.ui.lineEmail.text()
        if (self.sender().objectName() == 'tbTel1'):
            txt = self.ui.lineTel1.text()
        if (self.sender().objectName() == 'tbTel2'):
            txt = self.ui.lineTel2.text()
        if (self.sender().objectName() == 'tbVPN'):
            txt = self.ui.lineVPN.text()
        if (self.sender().objectName() == 'tbLocation'):
            txt = self.ui.lineLocation.text()
        #...
        try:
            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(txt, mode=cb.Clipboard)
            print('Content is copied')
        except Exception as e:
            print(e)

    def setData(self, records: UserInfo):
        self.ui.lineLogin.setText(records.Login)
        self.ui.lineName.setText(records.Name)
        self.ui.lineOrg.setText(records.Org)
        self.ui.lineUnit.setText(records.Unit)
        self.ui.linePosition.setText(records.Position)
        self.ui.lineLast.setText(str(records.Last))
        self.ui.lineSID.setText(records.SID)
        self.ui.lineEmail.setText(records.Email)
        self.ui.lineLocation.setText(records.Location)
        self.task_create = records.task_create
        self.isui = records.isui
        self.id = records.id

        for nums in records.Numbers:
            if nums[1] == 0:
                self.ui.lineVPN.setText(nums[0])
            if nums[1] == 1:
                self.ui.lineTel1.setText(nums[0])
            if nums[1] == 2:
                self.ui.lineTel2.setText(nums[0])
            if nums[1] == 3:
                self.ui.lineTel3.setText(nums[0])

        if len(records.Comment) > 0:
            self.ui.textComment.setText(records.Comment)
        if len(records.Location_comment) > 0:
            self.ui.lineLocation.setText(records.Location_comment)

        for pc in records.pc_info:
            item = QTreeWidgetItem()
            item.setText(0, pc[0])
            item.setText(1, str(pc[1]))
            self.ui.pc_name.addTopLevelItem(item)
        self.ui.pc_name.setColumnWidth(0, 300)
        if records.is_fired:
            self.ui.userIcon.setDisabled(True)

        if records.is_vip:
            style = self.ui.linePosition.styleSheet()
            self.ui.linePosition.setStyleSheet(style + 'background-color: #FFA9A9')


    def setPic(self, usrpic):
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray.fromBase64(usrpic.encode('UTF-8')))
        pic = pixmap.scaledToHeight(212)
        self.ui.userIcon.setPixmap(pic)
        #self.ui.userIcon.setPixmap(QPixmap(":/icon/user-vip.png"))

    def edit(self):
        self.saveData.emit(self.ui.textComment.toPlainText(), self.ui.lineLocation2.text(), self.ui.lineTel3.text(), self.id)



