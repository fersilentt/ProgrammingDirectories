# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui/programming_language/list.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbAdd = QtWidgets.QPushButton(Frame)
        self.pbAdd.setText("")
        self.pbAdd.setObjectName("pbAdd")
        self.horizontalLayout.addWidget(self.pbAdd)
        self.pbEdit = QtWidgets.QPushButton(Frame)
        self.pbEdit.setText("")
        self.pbEdit.setObjectName("pbEdit")
        self.horizontalLayout.addWidget(self.pbEdit)
        self.pbDelete = QtWidgets.QPushButton(Frame)
        self.pbDelete.setText("")
        self.pbDelete.setObjectName("pbDelete")
        self.horizontalLayout.addWidget(self.pbDelete)
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.leSearch = QtWidgets.QLineEdit(Frame)
        self.leSearch.setObjectName("leSearch")
        self.horizontalLayout.addWidget(self.leSearch)
        self.line = QtWidgets.QFrame(Frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.line_4 = QtWidgets.QFrame(Frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lMessageList = QtWidgets.QLabel(Frame)
        self.lMessageList.setText("")
        self.lMessageList.setAlignment(QtCore.Qt.AlignCenter)
        self.lMessageList.setObjectName("lMessageList")
        self.verticalLayout.addWidget(self.lMessageList)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(Frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.leSearch.setPlaceholderText(_translate("Frame", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "C1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "C2"))
