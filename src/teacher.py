# coding=utf-8
#!use/bin/env python3
# 查询学生信息',
# 录入学生成绩',
# 更改学生成绩',
# 删除学生成绩',

from gui.globalFunction import *
# 获取教师基本信息和所教课程
def teacher_Information(connect,tno):
    # 查找教师号为tno的教师的基本信息
    # 创建游标
    print("_BasedInformation(")
    cursor = connect.cursor()

    query = f"""SELECT teacher.tno,tname,tsex,tphone,dname,profess
                FROM teacher,department
                WHERE teacher.dmpno=department.dmpno AND teacher.tno='{str(tno)}'
   """

    # 执行查询
    cursor.execute(query)
    # 获取结果
    result1 = cursor.fetchall()
    #将result1转换为list
    #初始化为list
    result1_ = list(result1[0])
    print(result1_)
    print("*********")
    return result1_


def teacher_Course(connect,tno):
    # 查找教师号为tno的教师的基本信息
    # 创建游标
    print("_BasedInformation(")
    cursor = connect.cursor()
    # 找教师所教课程
    query = f"SELECT `cno`, `cname`, `c_period`, `clocation`, `credit`, `ctime` FROM course WHERE tno='{tno}'"

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result2 = cursor.fetchall()
    result2_ = [list(row) for row in result2]
    print(result2_)
    return result2_

#找到选修这门课的学生的学号、姓名、成绩
def teacher_gradeStudent(connect,cno):
    # 创建游标
    cursor = connect.cursor()
    # 找教师所教课程
    query = f"""SELECT student.sno,sname,grade
                FROM student,stu_course
                WHERE student.sno=stu_course.sno AND cno='{cno}'"""

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result3 = cursor.fetchall()
    result3_ = [list(row) for row in result3]
    print(result3_)
    return result3_

# 录入学生成绩 传入学号、课程号、成绩
def teacher_addGrade(connect,sno,cno,grade):
    # 创建游标
    cursor = connect.cursor()
    print("录入成功")
    print(sno)
    print(cno)
    print(grade)
    # 检查学号是否存在
    query = f"""SELECT * FROM student WHERE sno='{sno}'"""
    # 执行查询
    cursor.execute(query)
    # 获取结果
    result = cursor.fetchall()
    print(result)
    if not result:
        show_msg_box("错误","该学号不存在")
        return

    # 检查是否已经录入过
    query = f"""SELECT * FROM stu_course WHERE sno='{sno}' AND cno='{cno}'"""
    # 执行查询
    cursor.execute(query)
    # 获取结果
    result = cursor.fetchall()
    print(result)
    if result:
        show_msg_box("错误","已经录入过该学生在该门课的成绩了")
        return
    # 找教师所教课程
    query = f"""INSERT INTO `stu_course` (`sno`, `cno`, `grade`) VALUES('{sno}', '{cno}', '{grade}')"""
    # 执行查询
    cursor.execute(query)
    #提交事务
    connect.commit()
    print("录入成功")

# 更改学生成绩 传入学号、课程号、成绩
def teacher_updateGrade(connect,sno,cno,grade):
    # 创建游标
    cursor = connect.cursor()
    print("更改成功")
    print(sno)
    print(cno)
    print(grade)
    # 找教师所教课程
    query = f"""UPDATE `stu_course` SET `grade`='{grade}' WHERE `sno`='{sno}' AND `cno`='{cno}'"""
    # 执行查询
    cursor.execute(query)
    #提交事务
    connect.commit()

    print("更改成功")
