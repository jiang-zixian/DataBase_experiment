
# coding=utf-8
#!use/bin/env python3

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication

from src.mysqlSELECT import *
from src.student import *
from src.teacher import *
from src.admin import *
from src.login import *
from gui.globalFunction import *


# 导入 Qt designer 设计的页面
from gui.login import Ui_MainWindow as Login_Ui
from gui.courseDetail import Ui_Form_courseDetail as CourseDetail_Ui
from gui.admin_Menu import Ui_Form_admin_Menu as Admin_Menu_Ui
from gui.addstudent import Ui_Dialog_AddStudent as AddStudent_Ui
from gui.studentInformation import Ui_Form_studentInformation as StudentInformation_Ui
from gui.teacher_Menu import Ui_Form_teacherMenu as TeacherMenu_Ui
from gui.teacher_add_grade import Ui_Dialog_teacher_add_grade as Teacher_add_grade_Ui
from gui.mySELECT import Ui_Dialog_mySELECT as MySELECT_Ui
from gui.admin_add_delete_update import Ui_Form as Admin_add_delete_update_Ui
from gui.department_add_or_update import Ui_Form_department_add_or_update as Department_add_or_update_Ui
from gui.person_add_or_update import Ui_Form_person_add_or_update as Person_add_or_update_Ui

# 全局变量，用于存储当前登录的用户的连接
thisConnect= None

thisUsrNo=None

courseInformations=None #teacherMenu页面表格显示的课程信息
courseInformation=None #courseDetail页面表格显示的课程信息,也是courseInformations中被选中的课程信息
gradeStudent=None #courseDetail页面表格选中的选修这门课的学生的学号、姓名、成绩 一条记录
grade_add_or_update=None #教师当前是在修改成绩页还是录入成绩页,true为add,false为update
department=None #管理员当前选中的院系信息
department_add_or_update=None #管理员当前是在修改院系信息页还是添加院系信息页,true为add,false为update

student=None #管理员当前选中的学生信息
teacher=None #管理员当前选中的教师信息
dno=None #管理员当前要添加的院系编号
dmpname=None #管理员当前要添加的院系名称

# 主窗口
class HelloWindow( Login_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal() # 跳转信号 用于跳到管理员界面
    switch_window2 = QtCore.pyqtSignal() # 跳转信号 用于跳到学生界面
    switch_window3=QtCore.pyqtSignal() # 跳转信号 用于跳到教师界面
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Login)

    def Login(self):
        # 获得用户输入的信息
        type = self.comboBox_2.currentText()
        usrno = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        # 调用登录函数,连接各自的数据库
        global thisConnect,thisUsrNo
        thisConnect = login(type,usrno,pwd)
        if thisConnect[0] == 1:
            # 管理员登录
            thisUsrNo=usrno
            self.switch_window1.emit()
        elif thisConnect[0] == 2:
            # 教师登录
            thisUsrNo = usrno
            self.switch_window3.emit()
        elif thisConnect[0] == 3:
            # 学生登录
            thisUsrNo = usrno
            self.switch_window2.emit()
        else:
            # 登录失败
            print("11111")
            show_msg_box("登录失败","请检查输入")

# 管理员菜单窗口
class Admin_MenuWindow(Admin_Menu_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 用于跳到查询题库页
    switch_window2=QtCore.pyqtSignal() # 跳转信号 用于退出
    switch_window3=QtCore.pyqtSignal() # 跳转信号 用于跳到表格增删改页
    def __init__(self):
        super(Admin_MenuWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goSelect)#查询题库按钮
        self.pushButton_2.clicked.connect(self.back)#退出按钮
        self.pushButton_5.clicked.connect(self.goAdd_delete_update)#表格增删改按钮


    def goSelect(self):
        self.switch_window1.emit()

    def back(self):
        self.switch_window2.emit()

    def goAdd_delete_update(self):
        self.switch_window3.emit()


# 查询题库窗口
class MySELECTWindow(MySELECT_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 用于退出管理员菜单页
    def __init__(self):
        super(MySELECTWindow, self).__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.query)#选中问题
        self.pushButton.clicked.connect(self.back)#退出按钮

    def query(self):
        global thisConnect,thisUsrNo,courseInformations,courseInformation,gradeStudent,grade_add_or_update
        num=self.comboBox.currentIndex()
        code,result=myselect(thisConnect[1],num)
        self.textEdit.setText(code)
        self.textEdit_3.setText(result)

    def back(self):
        self.switch_window1.emit()

# 表格增删改页
class Admin_add_delete_updateWindow(Admin_add_delete_update_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 用于跳到院系修改、添加页
    switch_window4 = QtCore.pyqtSignal()  # 跳转信号 用于退出
    def __init__(self):
        super(Admin_add_delete_updateWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goStackedWidget2)#用于跳到人员信息管理的stackedWidget
        self.pushButton_2.clicked.connect(self.goStackedWidget1)#院系管理按钮
        self.pushButton_5.clicked.connect(self.addDepartment)#添加院系按钮
        #添加人员
        # self.pushButton_6.clicked.connect()
        self.pushButton_4.clicked.connect(self.back)#退出按钮
        self.initStackedWidget()#初始化院系管理的stackedWidget
        #self.initStackedWidget2()#初始化人员信息管理的stackedWidget

        self.stackedWidget.setVisible(True)
        self.stackedWidget_2.setVisible(False)

    def initStackedWidget(self):
        global thisConnect,thisUsrNo,courseInformations,courseInformation,gradeStudent,grade_add_or_update
        print("initStackedWidget")
        self.pushButton_5.clicked.connect(self.addDepartment)#添加院系按钮
        print("initStackedWidget")
        #初始化tableWidget
        self.departments=find_all_department(thisConnect[1])
        rows=len(self.departments)
        columns=len(self.departments[0])
        # 遍历二维数组并将元素添加到表格中
        for row in range(rows):
            for column in range(columns):
                item = QtWidgets.QTableWidgetItem(str(self.departments[row][column]))
                self.tableWidget.setItem(row+1, column, item)
        # 在tableWidget最后一列添加“修改”按钮
        self.addbutton_update()

    # def initStackedWidget2(self):
    #     global thisConnect,thisUsrNo,courseInformations,courseInformation,gradeStudent,grade_add_or_update
    #     #初始化tableWidget_2 学生表
    #     self.students=find_all_student(thisConnect[1])
    #     rows=len(self.students)
    #     columns=len(self.students[0])
    #     # 遍历二维数组并将元素添加到表格中
    #     for row in range(rows):
    #         for column in range(columns):
    #             item = QtWidgets.QTableWidgetItem(str(self.students[row][column]))
    #             self.tableWidget_2.setItem(row+1, column, item)
    #     # 在tableWidget_2最后一列添加“删除”按钮
    #     self.addbutton_update2()
    #     # 在tableWidget_2最后一列添加“修改”按钮
    #     self.addbutton_delete2()
    #
    #     #初始化tableWidget_3 教师表
    #     self.teachers=find_all_teacher(thisConnect[1])
    #     rows=len(self.teachers)
    #     columns=len(self.teachers[0])
    #     # 遍历二维数组并将元素添加到表格中
    #     for row in range(rows):
    #         for column in range(columns):
    #             item = QtWidgets.QTableWidgetItem(str(self.teachers[row][column]))
    #             self.tableWidget_3.setItem(row+1, column, item)
    #     # 在tableWidget_3最后一列添加“删除”按钮
    #     self.addbutton_update3()
    #     # 在tableWidget_3最后一列添加“修改”按钮
    #     self.addbutton_delete3()

    # 在tableWidget倒数第二列添加“修改”按钮
    def addbutton_update(self):
        rows = len(self.departments)
        # 遍历行数
        for row in range(rows):
            # 创建按钮
            button = QtWidgets.QPushButton(self.tableWidget)
            # 设置按钮文本
            button.setText("修改")
            # 将按钮添加到单元格中
            self.tableWidget.setCellWidget(row + 1, 4, button)
            # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
            button.clicked.connect(lambda _, info=self.departments[row]: self.update_department(info))

    # # 在tableWidget_2最后一列添加“删除”按钮
    # def addbutton_update2(self):
    #     rows = len(self.students)
    #     # 遍历行数
    #     for row in range(rows):
    #         # 创建按钮
    #         button = QtWidgets.QPushButton(self.tableWidget_2)
    #         # 设置按钮文本
    #         button.setText("修改")
    #         # 将按钮添加到单元格中
    #         self.tableWidget_2.setCellWidget(row + 1, 5, button)
    #         # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
    #         button.clicked.connect(lambda _, info=self.students[row]: self.update_student(info))
    #
    # def update_student(self, info):
    #     global student,department_add_or_update
    #     student = info
    #
    #
    # # 在tableWidget_2最后一列添加“删除”按钮
    # def addbutton_delete2(self):
    #     rows = len(self.students)
    #     # 遍历行数
    #     for row in range(rows):
    #         # 创建按钮
    #         button = QtWidgets.QPushButton(self.tableWidget_2)
    #         # 设置按钮文本
    #         button.setText("删除")
    #         # 将按钮添加到单元格中
    #         self.tableWidget_2.setCellWidget(row + 1, 6, button)
    #         # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
    #         button.clicked.connect(lambda _, info=self.students[row]: self.delete_student(info))
    #
    # # 在tableWidget_3最后一列添加“修改”按钮
    # def addbutton_update3(self):
    #     rows = len(self.teachers)
    #     # 遍历行数
    #     for row in range(rows):
    #         # 创建按钮
    #         button = QtWidgets.QPushButton(self.tableWidget_3)
    #         # 设置按钮文本
    #         button.setText("修改")
    #         # 将按钮添加到单元格中
    #         self.tableWidget_3.setCellWidget(row + 1, 5, button)
    #         # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
    #         button.clicked.connect(lambda _, info=self.teachers[row]: self.update_teacher(info))
    #
    # # 在tableWidget_3最后一列添加“删除”按钮
    # def addbutton_delete3(self):
    #     rows = len(self.teachers)
    #     # 遍历行数
    #     for row in range(rows):
    #         # 创建按钮
    #         button = QtWidgets.QPushButton(self.tableWidget_3)
    #         # 设置按钮文本
    #         button.setText("删除")
    #         # 将按钮添加到单元格中
    #         self.tableWidget_3.setCellWidget(row + 1, 6, button)
    #         # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
    #         button.clicked.connect(lambda _, info=self.teachers[row]: self.delete_teacher(info))

    def addDepartment(self):
        global department_add_or_update
        department_add_or_update=True
        # 跳转到添加院系信息页
        self.switch_window1.emit()

    def update_department(self, info):
        global department,department_add_or_update
        department = info  # 找到当前被选中的院系
        department_add_or_update = False
        # 跳转到修改院系信息页
        self.switch_window1.emit()
    
    def goStackedWidget1(self):#院系管理
        #self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setVisible(True)
        self.stackedWidget_2.setVisible(False)

    def goStackedWidget2(self):#人员管理
        #self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setVisible(True)
        self.stackedWidget.setVisible(False)
        
    def back(self):
        self.switch_window4.emit()

    def refresh(self):
        # 清空tableWidget,包括文字和按钮
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        for row in range(rows):
            for column in range(columns):
                self.tableWidget.setItem(row, column, None)
                self.tableWidget.removeCellWidget(row, column)

        # 清空tableWidget_2,包括文字和按钮
        rows = self.tableWidget_2.rowCount()
        columns = self.tableWidget_2.columnCount()
        for row in range(rows):
            for column in range(columns):
                self.tableWidget_2.setItem(row, column, None)
                self.tableWidget_2.removeCellWidget(row, column)

        # 初始化tableWidget
        self.initStackedWidget()




# 院系修改、添加窗口
class Department_add_or_updateWindow(Department_add_or_update_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 确认按钮
    switch_window2=QtCore.pyqtSignal() # 跳转信号 跳转到添加老师的页面
    def __init__(self):
        super(Department_add_or_updateWindow, self).__init__()
        self.setupUi(self)
        global department_add_or_update
        if(department_add_or_update==False):#如果是修改院系信息页
            self.lineEdit.setText(department[0])
            self.lineEdit_2.setText(department[1])
            self.lineEdit_3.setText(department[2])
            self.pushButton.clicked.connect(self.update_department)
        else:#如果是添加院系信息页
            self.pushButton.clicked.connect(self.insert_department)
        #取消按钮
        self.pushButton_2.clicked.connect(self.close)

    def update_department(self):
        print("update")
        global thisConnect,thisUsrNo,courseInformations,courseInformation,gradeStudent,grade_add_or_update,department
        dmpno = self.lineEdit.text()
        dname = self.lineEdit_2.text()
        tno = self.lineEdit_3.text()
        flag=admin_updateDepartment(thisConnect[1],dmpno,dname,tno)
        if(flag==True):
            self.switch_window1.emit()  # 刷新院系管理页的信号
            self.close()
        else:
            pass


    def insert_department(self):
        print("insert")
        dmpno = self.lineEdit.text()
        dname_ = self.lineEdit_2.text()
        tno = self.lineEdit_3.text()
        global thisConnect, thisUsrNo, courseInformations, courseInformation, gradeStudent, grade_add_or_update,department
        flag=admin_addDepartment(thisConnect[1],dmpno,dname_,tno)
        if(flag==True):#表示添加成功
            print("insert")
            self.switch_window1.emit()#刷新院系信息页面
            self.close()
        else:#没有该老师
            global dno,dmpname
            dno=dmpno
            dmpname=dname_
            self.switch_window2.emit()#跳转到添加老师的页面

# 人员添加、修改窗口
class Person_add_or_updateWindow(Person_add_or_update_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 确认按钮

    def __init__(self):
        super(Person_add_or_updateWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.admin_insert_teacher)
        #取消按钮
        self.pushButton_2.clicked.connect(self.close)

    def admin_insert_teacher(self):
        print("admin_insert_teacher")
        global thisConnect,thisUsrNo,courseInformations,dno,dmpname
        tno = self.lineEdit.text()
        tname = self.lineEdit_2.text()
        tsex = self.comboBox_2.currentText()
        tphone = self.lineEdit_3.text()
        dmpno=dno
        profess=self.comboBox_3.currentText()
        admin_addTeacher_for_addDmp(thisConnect[1], tno, tname, tsex, tphone, dmpno, profess, dmpname)
        self.switch_window1.emit()

# 课程详情页
class CourseDetailWindow(CourseDetail_Ui,QtWidgets.QMainWindow):
    gradeStudents=None #选修这门课的学生的学号、姓名、成绩
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 用于跳到修改成绩页/录入成绩页
    switch_window2 = QtCore.pyqtSignal()  # 跳转信号 用于跳回教师菜单页
    def __init__(self):
        super(CourseDetailWindow, self).__init__()
        self.setupUi(self)
        print(courseInformation)
        self.lineEdit_2.setText(str(courseInformation[0]))
        self.lineEdit.setText(str(courseInformation[1]))
        self.lineEdit_3.setText(str(courseInformation[2]))
        self.lineEdit_4.setText(str(courseInformation[3]))
        self.lineEdit_6.setText(str(courseInformation[4]))
        self.lineEdit_5.setText(str(courseInformation[5]))
        print("courseInformation[0]:"+courseInformation[0])

        #找到选修这门课的学生的学号、姓名、成绩
        self.gradeStudents=teacher_gradeStudent(thisConnect[1],courseInformation[0])
        print("self.gradeStudents:"+str(self.gradeStudents))
        rows = len(self.gradeStudents)
        columns = len(self.gradeStudents[0])
        # 遍历二维数组并将元素添加到表格中
        for row in range(rows):
            for column in range(columns):
                item = QtWidgets.QTableWidgetItem(str(self.gradeStudents[row][column]))
                self.tableWidget.setItem(row + 1, column, item)

        # 在tableWidget倒数第二列添加“修改”按钮
        self.addbutton_update()

        # 在tableWidget最后一列添加“删除”按钮
        self.addbutton_delete()

        # 点击录入成绩按钮
        self.pushButton.clicked.connect(self.on_pushButton_clicked_insert)

        # 点击退出按钮
        self.pushButton_2.clicked.connect(self.back)

    # 在tableWidget倒数第二列添加“修改”按钮
    def addbutton_update(self):
        rows=len(self.gradeStudents)
        # 遍历行数
        for row in range(rows):
            # 创建按钮
            button = QtWidgets.QPushButton(self.tableWidget)
            # 设置按钮文本
            button.setText("修改")
            # 将按钮添加到单元格中
            self.tableWidget.setCellWidget(row+1, 3, button)
            # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
            button.clicked.connect(lambda _, info=self.gradeStudents[row]: self.update_grade(info))

    def update_grade(self,info):
        global gradeStudent,grade_add_or_update
        gradeStudent=info #找到当前被选中的学生的学号、姓名、成绩
        grade_add_or_update=False
        # 跳转到修改成绩页
        self.switch_window1.emit()

    # 在tableWidget最后一列添加“删除”按钮
    def addbutton_delete(self):
        global courseInformation
        rows=len(self.gradeStudents)
        # 遍历行数
        for row in range(rows):
            # 创建按钮
            button = QtWidgets.QPushButton(self.tableWidget)
            # 设置按钮文本
            button.setText("删除")
            # 将按钮添加到单元格中
            self.tableWidget.setCellWidget(row+1, 4, button)
            # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
            button.clicked.connect(lambda _, info=self.gradeStudents[row]: self.delete_grade(info))

    def delete_grade(self,info):
        reply = QMessageBox.question(
            None,
            "删除",
            "确定要删除吗？",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            print("OK")
            # 创建游标
            cursor = thisConnect[1].cursor()
            # 执行查询
            query = f"DELETE FROM stu_course WHERE sno='{info[0]}' AND cno='{courseInformation[0]}'"
            cursor.execute(query)
            # 提交事务
            thisConnect[1].commit()
            # 关掉当前页面
            print("OK-------")
            # 刷新页面
            self.refresh()
        else:
            pass


    # 点击录入成绩按钮
    def on_pushButton_clicked_insert(self):
        # 跳转到录入成绩页
        global grade_add_or_update
        grade_add_or_update=True
        self.switch_window1.emit()

    # 点击退出按钮
    def back(self):
        # 跳转到教师菜单页
        self.switch_window2.emit()

    # 刷新courseDetail页面
    def refresh(self):
        #清空tableWidget,包括文字和按钮
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        for row in range(rows):
            for column in range(columns):
                self.tableWidget.setItem(row, column, None)
                self.tableWidget.removeCellWidget(row, column)

        # 找到选修这门课的学生的学号、姓名、成绩
        self.gradeStudents = teacher_gradeStudent(thisConnect[1], courseInformation[0])
        rows = len(self.gradeStudents)
        columns = len(self.gradeStudents[0])
        # 遍历二维数组并将元素添加到表格中
        for row in range(rows):
            for column in range(columns):
                item = QtWidgets.QTableWidgetItem(str(self.gradeStudents[row][column]))
                self.tableWidget.setItem(row + 1, column, item)

        # 在tableWidget倒数第二列添加“修改”按钮
        self.addbutton_update()

        # 在tableWidget最后一列添加“删除”按钮
        self.addbutton_delete()


# 学生信息窗口
class StudentInformationWindow(StudentInformation_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 用于跳回登录页
    def __init__(self):
        super(StudentInformationWindow, self).__init__()
        self.setupUi(self)
        global thisConnect, thisUsrNo, courseInformations, courseInformation, gradeStudent, grade_add_or_update
        basedInformation = studen_BasedInformation(thisConnect[1], thisUsrNo)
        self.lineEdit_2.setText(basedInformation[0])
        self.lineEdit.setText(basedInformation[1])
        self.lineEdit_3.setText(basedInformation[2])
        self.lineEdit_4.setText(str(basedInformation[3]))
        self.lineEdit_6.setText(basedInformation[4])
        self.lineEdit_5.setText(str(basedInformation[5]))
        self.lineEdit_7.setText(str(basedInformation[6]))
        self.lineEdit_8.setText(str(basedInformation[7]))
        self.pushButton.clicked.connect(self.back)#退出按钮
        courseInformation=studen_CourseInformation(thisConnect[1], thisUsrNo)
        # 假设二维数组为 courseInformation，行数为 rows，列数为 columns
        rows = len(courseInformation)
        columns = len(courseInformation[0])

        # 遍历二维数组并将元素添加到表格中
        for row in range(rows):
            for column in range(columns):
                item = QtWidgets.QTableWidgetItem(str(courseInformation[row][column]))
                self.tableWidget.setItem(row+1, column, item)

    def back(self):
        self.switch_window1.emit()

# 教师菜单窗口
class TeacherMenuWindow(TeacherMenu_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 用于跳到课程详情页
    switch_window2= QtCore.pyqtSignal()  # 跳转信号 用于跳回登录页
    def __init__(self):
        super(TeacherMenuWindow, self).__init__()
        self.setupUi(self)
        print("TeacherMenuWindow")
        global thisConnect, thisUsrNo, courseInformations, courseInformation, gradeStudent, grade_add_or_update
        print("TeacherMenuWindow")
        print(thisUsrNo)
        basedInformation = teacher_Information(thisConnect[1], thisUsrNo)
        self.lineEdit_2.setText(basedInformation[0])
        self.lineEdit.setText(basedInformation[1])
        self.lineEdit_3.setText(basedInformation[2])
        self.lineEdit_4.setText(str(basedInformation[3]))
        self.lineEdit_6.setText(basedInformation[4])
        self.lineEdit_5.setText(str(basedInformation[5]))
        self.pushButton_4.clicked.connect(self.back)#退出按钮

        courseInformations = teacher_Course(thisConnect[1], thisUsrNo)
        rows = len(courseInformations)
        columns = len(courseInformations[0])
        # 遍历二维数组并将元素添加到表格中
        for row in range(rows):
            for column in range(columns):
                item = QtWidgets.QTableWidgetItem(str(courseInformations[row][column]))
                self.tableWidget.setItem(row + 1, column, item)

        # 在tableWidget最后一列添加“详情”按钮
        self.addbutton()

    # 点击退出按钮
    def back(self):
        self.switch_window2.emit()

    # 在tableWidget最后一列添加“详情”按钮
    def addbutton(self):
        global courseInformations
        rows=len(courseInformations)
        # 遍历行数
        for row in range(rows):
            # 创建按钮
            button = QtWidgets.QPushButton(self.tableWidget)
            # 设置按钮文本
            button.setText("详情")
            # 将按钮添加到单元格中
            self.tableWidget.setCellWidget(row+1, 6, button)
            # 为按钮添加点击事件，并使用闭包将课程信息传递给槽函数
            button.clicked.connect(lambda _, info=courseInformations[row]: self.show_courseDetail(info))

    # 跳转到课程详情页
    def show_courseDetail(self,info):
        global courseInformation
        courseInformation=info #找到当前被选中的课程信息
        print("show_courseDetail")
        self.switch_window1.emit()


# 教师：修改成绩页/录入成绩页
class Teacher_add_gradeWindow(Teacher_add_grade_Ui,QtWidgets.QMainWindow):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号 用于跳到课程详情页
    def __init__(self):
        super(Teacher_add_gradeWindow, self).__init__()
        self.setupUi(self)
        global thisConnect,thisUsrNo,courseInformations,courseInformation,gradeStudent,grade_add_or_update
        if(grade_add_or_update==False):#如果是修改成绩页
            self.lineEdit.setText(gradeStudent[0])
            self.lineEdit_3.setText(str(gradeStudent[2]))
            self.pushButton.clicked.connect(self.update_grade)
        else:#如果是录入成绩页
            self.pushButton.clicked.connect(self.insert_grade)
        #取消按钮
        self.pushButton_2.clicked.connect(self.close)

    def update_grade(self):
        print("update")
        global thisConnect,thisUsrNo,courseInformations,courseInformation,gradeStudent,grade_add_or_update
        sno = self.lineEdit.text()
        grade=int(self.lineEdit_3.text())
        teacher_updateGrade(thisConnect[1],sno,courseInformation[0],grade)
        self.switch_window1.emit()# 刷新课程详情页的信号
        self.close()


    # 教师录入学生成绩
    def insert_grade(self):
        print("insert")
        sno=self.lineEdit.text()
        grade=int(self.lineEdit_3.text())
        global thisConnect, thisUsrNo, courseInformations, courseInformation, gradeStudent, grade_add_or_update
        teacher_addGrade(thisConnect[1],sno,courseInformation[0],grade)
        print("insert")
        self.switch_window1.emit()
        self.close()

class Controller:
    def __init__(self):
        self.hello= None
        self.admin_Menu = None
        self.mySELECT = None
        self.add_delete_update = None
        self.department_add_or_update = None
        self.person_add_or_update = None
        self.studentInformation = None
        self.teacherMenu = None
        self.courseDetail = None
        self.teacher_add_grade = None
        pass

    # 跳转到 MainWindow 窗口
    def show_MainWindow(self):
        self.hello = HelloWindow()
        self.hello.switch_window1.connect(self.from_hello_to_admin_Menu)#跳到管理员
        self.hello.switch_window2.connect(self.from_hello_to_studentInformation)#跳到学生
        self.hello.switch_window3.connect(self.from_hello_to_teacherMenu)#跳到教师
        self.hello.show()

    # 从MainWindow跳转到admin_Menu窗口
    def from_hello_to_admin_Menu(self):
        self.admin_Menu = Admin_MenuWindow()
        self.admin_Menu.switch_window1.connect(self.from_admin_Menu_to_mySELECT)
        self.admin_Menu.switch_window2.connect(self.from_admin_Menu_to_hello)
        self.admin_Menu.switch_window3.connect(self.from_admin_Menu_to_add_delete_update)
        self.hello.close()
        self.admin_Menu.show()

    # 从admin_Menu跳回到MainWindow窗口
    def from_admin_Menu_to_hello(self):
        self.admin_Menu.close()
        self.show_MainWindow()

    # 从admin_Menu跳转到mySELECT窗口
    def from_admin_Menu_to_mySELECT(self):
        self.admin_Menu.close()
        self.mySELECT = MySELECTWindow()
        self.mySELECT.switch_window1.connect(self.from_mySELECT_to_admin_Menu)
        self.mySELECT.show()

    # 从admin_Menu跳转到add_delete_update窗口
    def from_admin_Menu_to_add_delete_update(self):
        self.admin_Menu.close()
        print("from_admin_Menu_to_add_delete_update")
        self.add_delete_update = Admin_add_delete_updateWindow()
        print("from_admin_Menu_to_add_delete_update")
        self.add_delete_update.switch_window1.connect(self.from_add_delete_update_to_Department_add_or_update)
        self.add_delete_update.switch_window4.connect(self.from_add_delete_update_to_admin_Menu)
        self.add_delete_update.show()

    # 从add_delete_update跳回到admin_Menu窗口
    def from_add_delete_update_to_admin_Menu(self):
        self.add_delete_update.close()
        self.admin_Menu.show()

    def from_add_delete_update_to_Department_add_or_update(self):
        self.department_add_or_update = Department_add_or_updateWindow()
        self.department_add_or_update.switch_window2.connect(self.from_department_add_or_update_to_Person_add_or_update)
        self.department_add_or_update.switch_window1.connect(self.refresh_add_delete_update)
        self.department_add_or_update.show()

    # 从院系修改页面跳到添加老师的页面
    def from_department_add_or_update_to_Person_add_or_update(self):
        self.person_add_or_update = Person_add_or_updateWindow()
        self.person_add_or_update.switch_window1.connect(self.refresh_add_delete_update)
        self.person_add_or_update.show()

    def refresh_add_delete_update(self):
        print("refresh_add_delete_update")
        if (self.person_add_or_update != None):
            self.person_add_or_update.close()
        if (self.department_add_or_update != None):
            self.department_add_or_update.close()
        self.add_delete_update.refresh()

    # 从mySELECT跳回到admin_Menu窗口
    def from_mySELECT_to_admin_Menu(self):
        self.mySELECT.close()
        self.admin_Menu.show()


    #跳转到 studentInformation 窗口, 注意关闭原页面
    def from_hello_to_studentInformation(self):
        self.studentInformation = StudentInformationWindow()
        self.studentInformation.switch_window1.connect(self.from_studentInformation_to_hello)
        self.hello.close()
        self.studentInformation.show()

    def from_studentInformation_to_hello(self):
        self.studentInformation.close()
        self.show_MainWindow()

    #跳转到 teacherMenu 窗口, 注意关闭原页面
    def from_hello_to_teacherMenu(self):
        print("from_hello_to_teacherMenu")
        self.teacherMenu = TeacherMenuWindow()
        self.teacherMenu.switch_window1.connect(self.from_teacherMenu_to_courseDetail)
        self.teacherMenu.switch_window2.connect(self.from_teacherMenu_to_hello)
        self.hello.close()
        self.teacherMenu.show()

    def from_teacherMenu_to_hello(self):
        self.teacherMenu.close()
        self.show_MainWindow()

    def from_teacherMenu_to_courseDetail(self):
        print("from_teacherMenu_to_courseDetail")
        self.courseDetail = CourseDetailWindow()
        self.courseDetail.switch_window1.connect(self.show_add_update_grade)
        self.courseDetail.switch_window2.connect(self.from_courseDetail_to_teacherMenu)
        self.teacherMenu.close()
        self.courseDetail.show()

    # 从课程详情页跳回到教师菜单页
    def from_courseDetail_to_teacherMenu(self):
        self.courseDetail.close()
        self.teacherMenu.show()


    # 课程详情页点击修改成绩
    def show_add_update_grade(self):
        self.teacher_add_grade = Teacher_add_gradeWindow()
        self.teacher_add_grade.switch_window1.connect(self.refresh_courseDetail)
        self.teacher_add_grade.show()

    # 教师录入和修改成绩页后刷新courseDetail页面
    def refresh_courseDetail(self):
        self.courseDetail.refresh()



if __name__ == "__main__":
    connect=admin_connect()
    query1_1(connect)
    print('-----------')
    query1_2(connect)
    print('-----------')
    query2(connect)
    print('-----------')
    query3(connect)
    print('-----------')
    query4(connect)
    print('-----------')
    query5(connect)
    print('-----------')
    query6(connect)
    print('-----------')
    query7_1(connect)
    print('-----------')
    query7_2(connect)
    print('-----------')
    query8(connect)
    print('-----------')
    query9(connect)
    print('-----------')
    query10_1(connect)
    print('-----------')
    query10_2(connect)
    print('-----------')
    query11(connect)

    # studen_BasedInformation(thisConnect[1], '201832120719')
    # studen_CourseInformation(thisConnect[2], '201832120719')
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()  # 控制器实例
    controller.show_MainWindow()


    sys.exit(app.exec_())                   # 使用exit()或者点击关闭按钮退出QApplication









