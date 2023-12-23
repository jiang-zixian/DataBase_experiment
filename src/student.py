# coding=utf-8
#!use/bin/env python3

#返回基本信息和奖惩记录
def studen_BasedInformation(connect,sno):
    # 查找学号为sno的学生的基本信息
    # 创建游标
    print("_BasedInformation(")
    cursor = connect.cursor()
    query="USE `python`"
    cursor.execute(query)

    query = f"""SELECT sno,sname,ssex,sage,dname,intime
                FROM student,department
                WHERE student.dmpno=department.dmpno AND sno='{str(sno)}'
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

    #找奖惩记录
    query = f"SELECT * FROM stu_reward_punishment WHERE sno='{sno}'"

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result2 = cursor.fetchall()
    print(result2)
    # 初始化奖励和惩罚列表
    rewards = []
    punishments = []

    # 遍历查询结果
    for row in result2:
        reward = row[2]  # 获取奖励字段的值
        punishment = row[3]  # 获取惩罚字段的值

        # 将非空的奖励添加到奖励列表中
        if reward:
            rewards.append(reward)

        # 将非空的惩罚添加到惩罚列表中
        if punishment:
            punishments.append(punishment)

    # 将奖励列表中的元素用逗号连接成一个字符串
    rewards_str = ', '.join(rewards)

    # 将惩罚列表中的元素用逗号连接成一个字符串
    punishments_str = ', '.join(punishments)

    # 输出整理后的结果
    print("奖励：", rewards_str)
    print("惩罚：", punishments_str)

    #将奖惩记录添加到result1_中
    result1_.append(rewards_str)
    result1_.append(punishments_str)

    # 打印结果
    for i in range(len(result1_)):
        print(result1_[i])

    return result1_

# 返回sno学生的所有课程及课程信息
def studen_CourseInformation(connect,sno):
    # 查找学号为sno的学生的课程信息
    # 创建游标
    cursor = connect.cursor()

    query = f"""SELECT cno,cname,tname,c_period,clocation,credit,ctime
                FROM course,teacher
                 WHERE course.tno=teacher.tno AND cno in (
                    select cno from stu_course where sno='{sno}'
                 )       
"""
    # 执行查询
    cursor.execute(query)
    # 获取结果
    result1 = cursor.fetchall()

    print(result1)

    result2 = [list(row) for row in result1]

    for row in result2:
        for item in row:
            print(item, end=' ')
        print()  # 打印换行符表示新的一行

    return result2



