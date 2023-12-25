from gui.globalFunction import *
# 找到所有院系，返回院系号，院系名，院长工号，院长姓名
def find_all_department(connct):
    # 创建游标
    cursor = connct.cursor()
    # 找教师所教课程
    query = f"""SELECT department.dmpno, dname, teacher.tno, tname FROM department,teacher WHERE department.tno=teacher.tno"""

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()
    result_ = [list(row) for row in result]
    print(result_)
    return result_

#修改院系信息 输入院系号，院系名，院长工号
def admin_updateDepartment(connect,dmpno,dname,tno):
    # 创建游标
    cursor = connect.cursor()
    # 先查找teacher表中是否有该教师
    query = f"""SELECT * FROM teacher WHERE tno='{tno}'"""
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        # 找到教师，可以添加
        pass
    else:
        # 没有找到教师，添加失败
        show_msg_box("错误", "没有找到该教师，修改失败")
        return False

    # 找教师所教课程
    query = f"""UPDATE department SET dname='{dname}',tno='{tno}' WHERE dmpno='{dmpno}'"""

    # 执行查询
    cursor.execute(query)
    connect.commit()
    print("修改成功")
    return True

# 添加院系 输入院系号，院系名，院长工号
def admin_addDepartment(connect,dmpno,dname,tno):
    # 创建游标
    cursor = connect.cursor()
    # 先查找teacher表中是否有该教师
    query = f"""SELECT * FROM teacher WHERE tno='{tno}'"""
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        # 找到教师，可以添加
        pass
    else:
        # 没有找到教师，添加失败
        #show_msg_box("错误","没有找到该教师，添加失败")
        return False
    # 找教师所教课程
    query = f"""INSERT INTO department VALUES('{dmpno}','{dname}','{tno}')"""

    # 执行查询
    cursor.execute(query)
    connect.commit()
    print("添加成功")
    return True

# 因为没有该老师，所以添加该老师
def admin_addTeacher_for_addDmp(connect, tno, tname, tsex, tphone, dmpno, profess,dname):
    print("因为没有该老师，所以添加该老师")
    # 创建游标
    cursor = connect.cursor()
    # 先查找department表，找到第一个记录的院系号
    query = f"""SELECT dmpno FROM department LIMIT 1"""
    cursor.execute(query)
    print("找到第一个记录的院系号")
    dno_ = cursor.fetchone()
    dno1=dno_[0]
    print(tno)
    print(tname)
    print(tsex)
    print(tphone)
    print(dno_)
    print(profess)
    # 插入教师
    query = f"""INSERT INTO teacher VALUES('{tno}','{tname}','{tsex}','{tphone}','{dno1}','{profess}')"""
    # 执行查询
    cursor.execute(query)
    print("插入教师")
    # 插入这个教师之后，即可添加院系
    admin_addDepartment(connect, dmpno, dname, tno)
    #之后再将刚刚插入的教师的院系号改成dmpno
    query = f"""UPDATE teacher SET dmpno='{dmpno}' WHERE tno='{tno}'"""
    cursor.execute(query)
    # 将该老师信息插入到account表中
    query = f"""INSERT INTO account VALUES('{tno}','教师','11111')"""
    cursor.execute(query)
    print("将该老师信息插入到account表中")
    print("修改教师的院系号")
    connect.commit()
    print("添加成功")
    return True



def find_all_student(connect):
    # 创建游标
    cursor = connect.cursor()
    # 找教师所教课程
    query = f"""SELECT sno,sname,ssex,sage,dname,intime,password
                FROM student,account,department
                WHERE student.dmpno=department.dmpno AND student.sno=account.usrno"""

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()
    result_ = [list(row) for row in result]
    print(result_)
    return result_

def find_all_teacher(connect):
    # 创建游标
    cursor = connect.cursor()
    # 找教师所教课程
    query = f"""SELECT teacher.tno,tname,tsex,tphone,dname,profess,password
                FROM teacher,account,department
                WHERE teacher.dmpno=department.dmpno AND teacher.tno=account.usrno"""

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()
    result_ = [list(row) for row in result]
    print(result_)
    return result_