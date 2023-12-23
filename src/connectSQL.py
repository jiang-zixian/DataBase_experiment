import pymysql

def root_connect():
    try:
        conn_root = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='2014913',
            db='python',
            port=3306,
            charset='utf8'
        )
        print("-------------python-root连接成功------------------------")

    except pymysql.Error as e:
        print("root数据库连接失败", e)

    return conn_root

def admin_connect():
    try:
        conn_admin = pymysql.connect(
            host='127.0.0.1',
            user='admin',
            passwd='***',
            db='python',
            port=3306,
            charset='utf8'
        )
        print("-------------python-admin连接成功------------------------")

    except pymysql.Error as e:
        print("admin数据库连接失败", e)

    return conn_admin


def teacher_connect():
    try:
        conn_teacher = pymysql.connect(
            host='127.0.0.1',
            user='teacher',
            passwd='***',
            db='python',
            port=3306,
            charset='utf8'
        )
        print("-------------python-teacher连接成功------------------------")

    except pymysql.Error as e:
        print("teacher数据库连接失败", e)

    return conn_teacher

def student_connect():
    try:
        conn_student = pymysql.connect(
            host='127.0.0.1',
            user='student',
            passwd='***',
            db='python',
            port=3306,
            charset='utf8'
        )
        print("-------------python-student连接成功------------------------")

    except pymysql.Error as e:
        print("student数据库连接失败", e)

    return conn_student



