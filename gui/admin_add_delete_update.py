# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_add_delete_update.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1060, 593)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(940, 530, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 60, 1041, 461))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.tableWidget = QtWidgets.QTableWidget(self.page)
        self.tableWidget.setGeometry(QtCore.QRect(240, 41, 761, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 51, 131, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(Form)
        self.stackedWidget_2.setGeometry(QtCore.QRect(10, 60, 1041, 461))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stackedWidget_2.setFont(font)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(140, 40, 861, 211))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(9)
        self.tableWidget_2.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(91)
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 40, 81, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(140, 290, 861, 171))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(9)
        self.tableWidget_3.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(91)
        self.label = QtWidgets.QLabel(self.page_3)
        self.label.setGeometry(QtCore.QRect(490, 10, 91, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(480, 260, 91, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 100, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_4.raise_()
        self.stackedWidget_2.raise_()
        self.stackedWidget.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "退出"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "院系号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "院系名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "院长工号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "院长"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "操作"))
        self.pushButton_5.setText(_translate("Form", "添加院系"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("Form", "11"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("Form", "12"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("Form", "13"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("Form", "14"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("Form", "15"))
        item = self.tableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("Form", "16"))
        item = self.tableWidget_2.verticalHeaderItem(17)
        item.setText(_translate("Form", "17"))
        item = self.tableWidget_2.verticalHeaderItem(18)
        item.setText(_translate("Form", "18"))
        item = self.tableWidget_2.verticalHeaderItem(19)
        item.setText(_translate("Form", "19"))
        item = self.tableWidget_2.verticalHeaderItem(20)
        item.setText(_translate("Form", "20"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "学号"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "性别"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "年龄"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "所属院系"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "入学时间"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "登录密码"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("Form", "操作"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("Form", "操作"))
        self.pushButton_6.setText(_translate("Form", "添加人员"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget_3.verticalHeaderItem(9)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget_3.verticalHeaderItem(10)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget_3.verticalHeaderItem(11)
        item.setText(_translate("Form", "11"))
        item = self.tableWidget_3.verticalHeaderItem(12)
        item.setText(_translate("Form", "12"))
        item = self.tableWidget_3.verticalHeaderItem(13)
        item.setText(_translate("Form", "13"))
        item = self.tableWidget_3.verticalHeaderItem(14)
        item.setText(_translate("Form", "14"))
        item = self.tableWidget_3.verticalHeaderItem(15)
        item.setText(_translate("Form", "15"))
        item = self.tableWidget_3.verticalHeaderItem(16)
        item.setText(_translate("Form", "16"))
        item = self.tableWidget_3.verticalHeaderItem(17)
        item.setText(_translate("Form", "17"))
        item = self.tableWidget_3.verticalHeaderItem(18)
        item.setText(_translate("Form", "18"))
        item = self.tableWidget_3.verticalHeaderItem(19)
        item.setText(_translate("Form", "19"))
        item = self.tableWidget_3.verticalHeaderItem(20)
        item.setText(_translate("Form", "20"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "工号"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "性别"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "电话"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "所属院系"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("Form", "职称"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("Form", "登录密码"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("Form", "操作"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("Form", "操作"))
        self.label.setText(_translate("Form", "学生信息表"))
        self.label_2.setText(_translate("Form", "教师信息表"))
        self.pushButton.setText(_translate("Form", "人员信息修改（account,teacher,student）"))
        self.pushButton_2.setText(_translate("Form", "学院信息修改（department）"))
        self.label_3.setText(_translate("Form", "院系信息表"))
