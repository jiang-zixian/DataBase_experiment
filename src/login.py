# coding=utf-8
#!use/bin/env python3
from src.connectSQL import *

def login(type,usrno,pwd):
    connect=root_connect();#root连接数据库
    cursor=connect.cursor();
    # 根据类型执行不同的查询语句
    if type == '管理员':
        query = f"SELECT * FROM account WHERE usrtype='管理员' AND usrno='{usrno}' AND password='{pwd}'"
    elif type == '教师':
        query = f"SELECT * FROM account WHERE usrtype='教师' AND usrno='{usrno}' AND password='{pwd}'"
    elif type == '学生':
        query = f"SELECT * FROM account WHERE usrtype='学生' AND usrno='{usrno}' AND password='{pwd}'"

    cursor.execute(query)
    result = cursor.fetchone()
    print(type)
    print(usrno)
    print(pwd)
    print(result)
    if result:
        # 找到用户，返回对应的类型
        if type == '管理员':
            connect.close()
            connect=admin_connect()
            return [1,connect]
        elif type == '教师':
            connect.close()
            connect=teacher_connect()
            return [2,connect]
        elif type == '学生':
            connect.close()
            connect=student_connect()
            return [3,connect]
    else:
        print("没有该用户或密码错误")
        connect.close()
        return [0,0]

