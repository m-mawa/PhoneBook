# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtab.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newTab(object):
    def setupUi(self, newTab):
        newTab.setObjectName("newTab")
        newTab.resize(750, 646)
        newTab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(newTab)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 82, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(newTab)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_8 = QtWidgets.QLabel(newTab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_11 = QtWidgets.QLabel(newTab)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_6 = QtWidgets.QLabel(newTab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_2 = QtWidgets.QLabel(newTab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_12 = QtWidgets.QLabel(newTab)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_10 = QtWidgets.QLabel(newTab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(newTab)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_5 = QtWidgets.QLabel(newTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(newTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(newTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(newTab)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineLogin = QtWidgets.QLineEdit(newTab)
        self.lineLogin.setToolTip("")
        self.lineLogin.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineLogin.setReadOnly(True)
        self.lineLogin.setObjectName("lineLogin")
        self.horizontalLayout.addWidget(self.lineLogin)
        self.tbLogin = QtWidgets.QToolButton(newTab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/clipboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbLogin.setIcon(icon)
        self.tbLogin.setObjectName("tbLogin")
        self.horizontalLayout.addWidget(self.tbLogin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineName = QtWidgets.QLineEdit(newTab)
        self.lineName.setToolTip("")
        self.lineName.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineName.setReadOnly(True)
        self.lineName.setObjectName("lineName")
        self.horizontalLayout_3.addWidget(self.lineName)
        self.tbName = QtWidgets.QToolButton(newTab)
        self.tbName.setIcon(icon)
        self.tbName.setObjectName("tbName")
        self.horizontalLayout_3.addWidget(self.tbName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineOrg = QtWidgets.QLineEdit(newTab)
        self.lineOrg.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineOrg.setReadOnly(True)
        self.lineOrg.setObjectName("lineOrg")
        self.horizontalLayout_11.addWidget(self.lineOrg)
        self.tbOrg = QtWidgets.QToolButton(newTab)
        self.tbOrg.setIcon(icon)
        self.tbOrg.setObjectName("tbOrg")
        self.horizontalLayout_11.addWidget(self.tbOrg)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineUnit = QtWidgets.QLineEdit(newTab)
        self.lineUnit.setToolTip("")
        self.lineUnit.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineUnit.setReadOnly(True)
        self.lineUnit.setObjectName("lineUnit")
        self.horizontalLayout_4.addWidget(self.lineUnit)
        self.tbUnit = QtWidgets.QToolButton(newTab)
        self.tbUnit.setIcon(icon)
        self.tbUnit.setObjectName("tbUnit")
        self.horizontalLayout_4.addWidget(self.tbUnit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.linePosition = QtWidgets.QLineEdit(newTab)
        self.linePosition.setToolTip("")
        self.linePosition.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.linePosition.setReadOnly(True)
        self.linePosition.setObjectName("linePosition")
        self.horizontalLayout_5.addWidget(self.linePosition)
        self.tbPosition = QtWidgets.QToolButton(newTab)
        self.tbPosition.setIcon(icon)
        self.tbPosition.setObjectName("tbPosition")
        self.horizontalLayout_5.addWidget(self.tbPosition)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lineLast = QtWidgets.QLineEdit(newTab)
        self.lineLast.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineLast.setReadOnly(True)
        self.lineLast.setObjectName("lineLast")
        self.horizontalLayout_13.addWidget(self.lineLast)
        self.tbLast = QtWidgets.QToolButton(newTab)
        self.tbLast.setIcon(icon)
        self.tbLast.setObjectName("tbLast")
        self.horizontalLayout_13.addWidget(self.tbLast)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineSID = QtWidgets.QLineEdit(newTab)
        self.lineSID.setToolTip("")
        self.lineSID.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineSID.setReadOnly(True)
        self.lineSID.setObjectName("lineSID")
        self.horizontalLayout_10.addWidget(self.lineSID)
        self.tbSID = QtWidgets.QToolButton(newTab)
        self.tbSID.setIcon(icon)
        self.tbSID.setObjectName("tbSID")
        self.horizontalLayout_10.addWidget(self.tbSID)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEmail = QtWidgets.QLineEdit(newTab)
        self.lineEmail.setToolTip("")
        self.lineEmail.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineEmail.setReadOnly(True)
        self.lineEmail.setObjectName("lineEmail")
        self.horizontalLayout_7.addWidget(self.lineEmail)
        self.tbEmailTo = QtWidgets.QToolButton(newTab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/img/mail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbEmailTo.setIcon(icon1)
        self.tbEmailTo.setObjectName("tbEmailTo")
        self.horizontalLayout_7.addWidget(self.tbEmailTo)
        self.tbEmail = QtWidgets.QToolButton(newTab)
        self.tbEmail.setIcon(icon)
        self.tbEmail.setObjectName("tbEmail")
        self.horizontalLayout_7.addWidget(self.tbEmail)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineTel1 = QtWidgets.QLineEdit(newTab)
        self.lineTel1.setToolTip("")
        self.lineTel1.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineTel1.setReadOnly(True)
        self.lineTel1.setObjectName("lineTel1")
        self.horizontalLayout_8.addWidget(self.lineTel1)
        self.tbcall1 = QtWidgets.QToolButton(newTab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/img/telephone-call.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tbcall1.setIcon(icon2)
        self.tbcall1.setObjectName("tbcall1")
        self.horizontalLayout_8.addWidget(self.tbcall1)
        self.tbTel1 = QtWidgets.QToolButton(newTab)
        self.tbTel1.setIcon(icon)
        self.tbTel1.setObjectName("tbTel1")
        self.horizontalLayout_8.addWidget(self.tbTel1)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineTel2 = QtWidgets.QLineEdit(newTab)
        self.lineTel2.setToolTip("")
        self.lineTel2.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineTel2.setReadOnly(True)
        self.lineTel2.setObjectName("lineTel2")
        self.horizontalLayout_9.addWidget(self.lineTel2)
        self.tbcall2 = QtWidgets.QToolButton(newTab)
        self.tbcall2.setIcon(icon2)
        self.tbcall2.setObjectName("tbcall2")
        self.horizontalLayout_9.addWidget(self.tbcall2)
        self.tbTel2 = QtWidgets.QToolButton(newTab)
        self.tbTel2.setIcon(icon)
        self.tbTel2.setObjectName("tbTel2")
        self.horizontalLayout_9.addWidget(self.tbTel2)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineVPN = QtWidgets.QLineEdit(newTab)
        self.lineVPN.setToolTip("")
        self.lineVPN.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineVPN.setReadOnly(True)
        self.lineVPN.setObjectName("lineVPN")
        self.horizontalLayout_6.addWidget(self.lineVPN)
        self.tbcall3 = QtWidgets.QToolButton(newTab)
        self.tbcall3.setIcon(icon2)
        self.tbcall3.setObjectName("tbcall3")
        self.horizontalLayout_6.addWidget(self.tbcall3)
        self.tbVPN = QtWidgets.QToolButton(newTab)
        self.tbVPN.setIcon(icon)
        self.tbVPN.setObjectName("tbVPN")
        self.horizontalLayout_6.addWidget(self.tbVPN)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineLocation = QtWidgets.QLineEdit(newTab)
        self.lineLocation.setToolTip("")
        self.lineLocation.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineLocation.setReadOnly(True)
        self.lineLocation.setObjectName("lineLocation")
        self.horizontalLayout_2.addWidget(self.lineLocation)
        self.tbLocation = QtWidgets.QToolButton(newTab)
        self.tbLocation.setIcon(icon)
        self.tbLocation.setObjectName("tbLocation")
        self.horizontalLayout_2.addWidget(self.tbLocation)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_12, 0, 1, 3, 1)
        self.userIcon = QtWidgets.QLabel(newTab)
        self.userIcon.setEnabled(True)
        self.userIcon.setMinimumSize(QtCore.QSize(212, 212))
        self.userIcon.setMaximumSize(QtCore.QSize(212, 212))
        self.userIcon.setAutoFillBackground(False)
        self.userIcon.setText("")
        self.userIcon.setPixmap(QtGui.QPixmap(":/icon/img/user.png"))
        self.userIcon.setScaledContents(False)
        self.userIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.userIcon.setObjectName("userIcon")
        self.gridLayout.addWidget(self.userIcon, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.butOpenCreate = QtWidgets.QPushButton(newTab)
        self.butOpenCreate.setStyleSheet("background-color: #FAFBFC;\n"
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
        self.butOpenCreate.setObjectName("butOpenCreate")
        self.verticalLayout_4.addWidget(self.butOpenCreate)
        self.butOpenUser = QtWidgets.QPushButton(newTab)
        self.butOpenUser.setStyleSheet("background-color: #FAFBFC;\n"
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
        self.butOpenUser.setObjectName("butOpenUser")
        self.verticalLayout_4.addWidget(self.butOpenUser)
        self.butEditUser = QtWidgets.QPushButton(newTab)
        self.butEditUser.setStyleSheet("background-color: #FAFBFC;\n"
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
        self.butEditUser.setObjectName("butEditUser")
        self.verticalLayout_4.addWidget(self.butEditUser)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.pc_name = QtWidgets.QTreeWidget(newTab)
        self.pc_name.setMaximumSize(QtCore.QSize(16777215, 81))
        self.pc_name.setUniformRowHeights(False)
        self.pc_name.setObjectName("pc_name")
        self.gridLayout.addWidget(self.pc_name, 3, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(newTab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.textComment = QtWidgets.QTextEdit(self.groupBox)
        self.textComment.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;")
        self.textComment.setObjectName("textComment")
        self.verticalLayout_6.addWidget(self.textComment)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setMaximumSize(QtCore.QSize(139, 25))
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineTel3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineTel3.setToolTip("")
        self.lineTel3.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineTel3.setReadOnly(False)
        self.lineTel3.setObjectName("lineTel3")
        self.horizontalLayout_14.addWidget(self.lineTel3)
        self.tbcall4 = QtWidgets.QToolButton(self.groupBox)
        self.tbcall4.setIcon(icon2)
        self.tbcall4.setObjectName("tbcall4")
        self.horizontalLayout_14.addWidget(self.tbcall4)
        self.tbTel3 = QtWidgets.QToolButton(self.groupBox)
        self.tbTel3.setIcon(icon)
        self.tbTel3.setObjectName("tbTel3")
        self.horizontalLayout_14.addWidget(self.tbTel3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lineLocation2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineLocation2.setToolTip("")
        self.lineLocation2.setStyleSheet("border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 2px 15px;")
        self.lineLocation2.setReadOnly(False)
        self.lineLocation2.setObjectName("lineLocation2")
        self.horizontalLayout_16.addWidget(self.lineLocation2)
        self.tbLocation2 = QtWidgets.QToolButton(self.groupBox)
        self.tbLocation2.setIcon(icon)
        self.tbLocation2.setObjectName("tbLocation2")
        self.horizontalLayout_16.addWidget(self.tbLocation2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.butSave = QtWidgets.QPushButton(self.groupBox)
        self.butSave.setMinimumSize(QtCore.QSize(275, 0))
        self.butSave.setStyleSheet("background-color: #FAFBFC;\n"
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
        self.butSave.setObjectName("butSave")
        self.horizontalLayout_17.addWidget(self.butSave)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 2)

        self.retranslateUi(newTab)
        QtCore.QMetaObject.connectSlotsByName(newTab)

    def retranslateUi(self, newTab):
        _translate = QtCore.QCoreApplication.translate
        newTab.setWindowTitle(_translate("newTab", "Form"))
        self.label.setText(_translate("newTab", "Логин:"))
        self.label_8.setText(_translate("newTab", "ФИО:"))
        self.label_11.setText(_translate("newTab", "Организация:"))
        self.label_6.setText(_translate("newTab", "Подразделение:"))
        self.label_2.setText(_translate("newTab", "Должность:"))
        self.label_12.setText(_translate("newTab", "Последний вход:"))
        self.label_10.setText(_translate("newTab", "SID учетной записи:"))
        self.label_9.setText(_translate("newTab", "Адрес почты:"))
        self.label_5.setText(_translate("newTab", "Номер телефона:"))
        self.label_4.setText(_translate("newTab", "Номер телефона 2:"))
        self.label_3.setText(_translate("newTab", "Номер телефона VPN:"))
        self.label_7.setText(_translate("newTab", "Месторасположение:"))
        self.tbLogin.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbLogin.setText(_translate("newTab", "..."))
        self.tbName.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbName.setText(_translate("newTab", "..."))
        self.tbOrg.setText(_translate("newTab", "..."))
        self.tbUnit.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbUnit.setText(_translate("newTab", "..."))
        self.tbPosition.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbPosition.setText(_translate("newTab", "..."))
        self.tbLast.setText(_translate("newTab", "..."))
        self.tbSID.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbSID.setText(_translate("newTab", "..."))
        self.tbEmailTo.setToolTip(_translate("newTab", "Отправить письмо по адресу."))
        self.tbEmailTo.setText(_translate("newTab", "..."))
        self.tbEmail.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbEmail.setText(_translate("newTab", "..."))
        self.tbcall1.setToolTip(_translate("newTab", "Позвонить по номеру."))
        self.tbcall1.setText(_translate("newTab", "..."))
        self.tbTel1.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbTel1.setText(_translate("newTab", "..."))
        self.tbcall2.setToolTip(_translate("newTab", "Позвонить по номеру."))
        self.tbcall2.setText(_translate("newTab", "..."))
        self.tbTel2.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbTel2.setText(_translate("newTab", "..."))
        self.tbcall3.setToolTip(_translate("newTab", "Позвонить по номеру."))
        self.tbcall3.setText(_translate("newTab", "..."))
        self.tbVPN.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbVPN.setText(_translate("newTab", "..."))
        self.tbLocation.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbLocation.setText(_translate("newTab", "..."))
        self.butOpenCreate.setText(_translate("newTab", "Создание учетки"))
        self.butOpenUser.setText(_translate("newTab", "Заявки пользователя"))
        self.butEditUser.setText(_translate("newTab", "Редактировать пользователя"))
        self.pc_name.headerItem().setText(0, _translate("newTab", "Имя ПК\\IP адрес"))
        self.pc_name.headerItem().setText(1, _translate("newTab", "Время проверки"))
        self.groupBox.setTitle(_translate("newTab", "Редактируемые поля"))
        self.label_14.setText(_translate("newTab", "Коментарий к пользователю."))
        self.textComment.setHtml(_translate("newTab", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_13.setText(_translate("newTab", "Номер телефона:"))
        self.label_15.setText(_translate("newTab", "Месторасположение:"))
        self.tbcall4.setToolTip(_translate("newTab", "Позвонить по номеру."))
        self.tbcall4.setText(_translate("newTab", "..."))
        self.tbTel3.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbTel3.setText(_translate("newTab", "..."))
        self.tbLocation2.setToolTip(_translate("newTab", "Скопировать в буфер обмена."))
        self.tbLocation2.setText(_translate("newTab", "..."))
        self.butSave.setText(_translate("newTab", "Сохранить"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newTab = QtWidgets.QWidget()
    ui = Ui_newTab()
    ui.setupUi(newTab)
    newTab.show()
    sys.exit(app.exec_())
