# coding=utf-8
#!use/bin/env python3
# 专门写复杂的查询语句

# 1.1.找出目前该学校的未成年（年龄低于18岁）学生，并按照入学时间从早到晚为他们生成序号
def query1_1(connect):
    # 创建游标
    cursor = connect.cursor()

    # 查询未成年学生
    query = f"SELECT ROW_NUMBER() OVER (ORDER BY intime),sno,sname,intime\
              FROM student\
              WHERE sage < 18"

    # 执行查询
    cursor.execute(query)

    # 获取结果
    underage_students = cursor.fetchall()
    # 构建表头
    table_str = "{:<10} {:<15} {:<10} {:<20}\n".format("序号", "学号", "姓名", "入学时间")

    # 构建数据行
    for student in underage_students:
        formatted_date = student[3].strftime("%Y-%m-%d %H:%M:%S")
        table_str += "{:<10} {:<20} {:<10} {:<20}\n".format(student[0], student[1], student[2], formatted_date)

    # 打印结果
    print("未成年学生的学号姓名分别是：")
    for student in underage_students:
        print(f"序号: {student[0]},学号: {student[1]}, 姓名: {student[2]}，入学时间: {student[3]}")
    return table_str

#1.2排序原理：计算表里比当前学生入学晚且未成年的学生个数
def query1_2(connect):
    # 创建游标
    cursor = connect.cursor()

    # 查询未成年学生
    query = """
            select
                (
                select count(distinct intime)#表示计算 Score 列中不同值的数量，即去重后的分数种类数
                from student
                where intime <= sx.intime AND sage<18 #表里比当前学生入学早且未成年的学生个数
                ) as ranks ,
                sno,
                sname,
                intime
            from student as sx
            where sage<18
            ORDER BY intime;
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    underage_students = cursor.fetchall()

    # 构建表头
    table_str = "{:<10} {:<15} {:<10} {:<20}\n".format("序号", "学号", "姓名", "入学时间")

    # 构建数据行
    for student in underage_students:
        formatted_date = student[3].strftime("%Y-%m-%d %H:%M:%S")
        table_str += "{:<10} {:<20} {:<10} {:<20}\n".format(student[0], student[1], student[2], formatted_date)

    # 打印结果
    print("未成年学生的学号姓名分别是：")
    for student in underage_students:
        print(f"序号: {student[0]},学号: {student[1]}, 姓名: {student[2]}，入学时间: {student[3]}")
    return table_str


# 2.查找有科目不及格的学生，显示该学生的姓名学号、不及格课程的课程号和课程名称，该学生对应的成绩
# 使用连接查询，不能用嵌套查询，因为三个表中都有要找的属性
def query2(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        SELECT
            student.sno,
            sname,
            course.cno,
            cname,
            grade
        FROM
            student, stu_course, course
        WHERE
            student.sno = stu_course.sno
            AND stu_course.cno = course.cno
            AND grade < 60
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    results = cursor.fetchall()

    table_str="不及格学生的学号姓名、对应课程的课程号、课程名、成绩分别是：\n"

    # 构建表头
    table_str += "{:<15} {:<15} {:<10} {:<20} {:<20}\n".format("学号", "姓名", "课程号", "课程名", "成绩")

    # 构建数据行
    for result in results:
        table_str += "{:<15} {:<15} {:<10} {:<20} {:<20}\n".format(str(result[0]), str(result[1]), str(result[2]),
                                                                   str(result[3]), str(result[4]))

    # 打印结果
    for row in results:
        print(row)

    return table_str

# 3.用嵌套查询查找有科目不及格的学生，显示该学生的姓名学号、不及格课程的课程号，该学生对应的成绩
# 非关联嵌套
def query3(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        SELECT
            student.sno,
            sname,
            cno,
            grade
        FROM
            student,stu_course
        WHERE
            student.sno=stu_course.sno AND
            grade IS NOT NULL AND
            grade<60 AND
            student.sno in (
                SELECT sno
                FROM stu_course,course
                WHERE stu_course.cno=course.cno AND grade<60
    )

    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    table_str = "不及格学生的学号姓名、对应课程的课程号、成绩分别是：\n"

    # 构建表头
    table_str += "{:<15} {:<15} {:<10} {:<20}\n".format("学号", "姓名", "课程号", "成绩")

    # 构建数据行
    for row in result:
        table_str += "{:<15} {:<15} {:<10} {:<20}\n".format(str(row[0]), str(row[1]), str(row[2]), str(row[3]))

    return table_str


# 4.找出每个班级的课程号，任课老师姓名和平均分，按平均分降序排序
def query4(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        SELECT 
            course.cno,tname,AVG(grade) AS average_grade
        FROM 
            teacher,course,stu_course
        WHERE
            teacher.tno=course.tno AND
            course.cno=stu_course.cno AND
            grade IS NOT NULL #排除没有成绩的记录
        group by course.cno
        order by AVG(grade) desc
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    table_str = "每个班级的课程号、任课老师姓名和平均分为：\n"

    # 构建表头
    table_str += "{:<10} {:<15} {:<20}\n".format("课程号", "任课老师姓名", "平均分")

    # 构建数据行
    for row in result:
        table_str += "{:<10} {:<15} {:<20}\n".format(str(row[0]), str(row[1]), str(row[2]))

    return table_str


# 5.哪个班级的平均分最高？找出这个班级的课程号，任课老师姓名和平均分
def query5(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        SELECT 
            course.cno,tname,AVG(grade) AS average_grade
        FROM 
            teacher,course,stu_course
        WHERE
            teacher.tno=course.tno AND
            course.cno=stu_course.cno AND
            grade IS NOT NULL #排除没有成绩的记录
        group by course.cno
        HAVING avg(grade) =( #找出最高的平均分
        SELECT 
            AVG(grade)
        FROM 
            teacher,course,stu_course
        WHERE
            teacher.tno=course.tno AND
            course.cno=stu_course.cno AND
           grade IS NOT NULL
        GROUP BY course.cno
        ORDER BY AVG(grade) DESC
        LIMIT 1)
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    table_str = "平均分最高的课程的课程号、任课老师姓名和平均分为：\n"

    # 构建表头
    table_str += "{:<10} {:<15} {:<20}\n".format("课程号", "任课老师姓名", "平均分")

    # 构建数据行
    for row in result:
        table_str += "{:<10} {:<15} {:<20}\n".format(str(row[0]), str(row[1]), str(row[2]))

    return table_str


# 6.查找平均分第三高的那个班级的课程号，任课老师姓名和平均分，用视图
# 思路：先求平均分，用视图表示中间表，然后找“有两个班级比自己的平均分高”的班级
def query6(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query1 = """
        CREATE VIEW avgGrade
        AS 
            SELECT 
                course.cno AS cno,tname AS tname,AVG(grade) AS average_grade
            FROM 
                teacher,course,stu_course
            WHERE
                teacher.tno=course.tno AND
                course.cno=stu_course.cno AND
                grade IS NOT NULL
                GROUP BY course.cno;
    """

    query2 = """
            SELECT *
            FROM
            avgGrade as ax
            WHERE(SELECT
            count(distinct
            average_grade)
            FROM avgGrade
                WHERE
            average_grade > ax.average_grade
            )=2;
    """

    query3 = """DROP VIEW avgGrade;"""

    # 执行查询
    cursor.execute(query1)
    cursor.execute(query2)
    result = cursor.fetchall()
    cursor.execute(query3)

    table_str = "平均分第三高的班级的课程号、任课老师姓名和平均分为：\n"

    # 构建表头
    table_str += "{:<10} {:<15} {:<20}\n".format("课程号", "任课老师姓名", "平均分")

    # 构建数据行
    for row in result:
        table_str += "{:<10} {:<15} {:<20}\n".format(str(row[0]), str(row[1]), str(row[2]))

    return table_str


# 7.有两门及以上的课有有效成绩的同学的学号姓名
# 7.1用group+having

def query7_1(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
            SELECT 
                sno,sname
            FROM
                student
            WHERE sno IN (
                SELECT sno
                FROM stu_course
                WHERE grade IS NOT NULL
                GROUP BY sno
                HAVING COUNT(DISTINCT cno) > 1
            );
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    table_str = "有两门及以上的课有有效成绩的同学的学号姓名为：\n"

    # 构建表头
    table_str += "{:<10} {:<15}\n".format("学号", "姓名")

    # 构建数据行
    for row in result:
        table_str += "{:<10} {:<15}\n".format(str(row[0]), str(row[1]))

    return table_str

# 7.2不用group+having
def query7_2(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        select sx.sno,sname
from stu_course as sx,stu_course as sy,student
where sx.sno=student.sno and
	sy.sno=student.sno and
	sx.grade is not null and
		sy.grade is not null and 
        sx.cno<>sy.cno
group by sx.sno;
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    table_str = "有两门及以上的课有有效成绩的同学的学号姓名为：\n"

    # 构建表头
    table_str += "{:<10} {:<15}\n".format("学号", "姓名")

    # 构建数据行
    for row in result:
        table_str += "{:<10} {:<15}\n".format(str(row[0]), str(row[1]))

    return table_str


# 8.查找所属学院院长为马冬梅或韩宏的、所有师生的学号/工号和姓名 使用UNION
# 嵌套查询和连接查询都可以写，这里写嵌套查询
def query8(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
            SELECT 
                sno,sname
            FROM
                student
            WHERE dmpno in (
                SELECT dmpno
                FROM department
                WHERE tno in (
                    SELECT tno
                    FROM teacher
                    WHERE tname='马冬梅' OR tname='韩宏'
                )
            )
            UNION
            SELECT 
                tno,tname
            FROM
                teacher
            WHERE dmpno in (
                SELECT dmpno
                FROM department
                WHERE tno in (
                    SELECT tno
                    FROM teacher
                    WHERE tname='马冬梅' OR tname='韩宏'
                )
            )
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    # 构建字符串
    result_str = "所属学院院长为马冬梅或韩宏的师生的学号和姓名为：\n"

    # 构建数据行
    for row in result:
        result_str += "学号: {}, 姓名: {}\n".format(row[0], row[1])

    return result_str


# 9.查询只有一个学生的课程号
# 可以用group+having，但这里用否定谓词+关联嵌套
def query9(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
            select cno
            from stu_course as sx
            where cno not in (
                select cno
                from stu_course
                where sx.sno<>sno
            );
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    # 构建字符串
    result_str = "只有一个学生的课程号为：\n"

    # 构建数据行
    for row in result:
        result_str += "{}\n".format(row[0])

    return result_str

# 10.查询选修了所有课程的学生的学号姓名
# 10.1 找选修课程数等于课程数目的学生
def query10_1(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        select
            sno,sname
        from
            student
        where sno in (
            select sno 
            from stu_course
            group by sno
            having count(*)=(
                select count(*) from course
            )
        );
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    # 构建字符串
    result_str = "选修了所有课程的学生的学号和姓名为：\n"

    # 构建数据行
    for row in result:
        result_str += "学号: {}, 姓名: {}\n".format(row[0], row[1])

    return result_str

# 10.2 查询没有一门课没被该生选择的学生的学号姓名
def query10_2(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        select sno,sname
        from student
        where not exists(
            select *
            from course
            where not exists(
                select *
                from stu_course
            where stu_course.sno = student.sno and
                    stu_course.cno=course.cno
            )
        );
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    # 构建字符串
    result_str = "没有一门课没被选择的学生的学号和姓名为：\n"

    # 构建数据行
    for row in result:
        result_str += "学号: {}, 姓名: {}\n".format(row[0], row[1])

    return result_str


# 11.查询所有课程成绩的最高分、最低分、平均分。成绩不全的课程不参与统计，最终结果按平均分降序排列
def query11(connect):
    # 创建游标
    cursor = connect.cursor()

    # 定义 SQL 查询
    query = """
        SELECT cno, MAX(grade) AS max_grade, MIN(grade) AS min_grade, AVG(grade) AS avg_grade
        from stu_course
        where grade is not null
        group by cno
        having cno not in(
            select cno 
            from stu_course
            where grade is null
        )
        order by avg_grade desc;
    """

    # 执行查询
    cursor.execute(query)

    # 获取结果
    result = cursor.fetchall()

    # 构建字符串
    result_str = "课程成绩的最高分、最低分、平均分为：\n"

    # 构建表头
    result_str += "{:<10} {:<10} {:<10} {:<10}\n".format("课程号", "最高分", "最低分", "平均分")

    # 构建数据行
    for row in result:
        result_str += "{:<10} {:<10} {:<10} {:<10}\n".format(row[0], row[1], row[2], row[3])

    return result_str

codes = []
codes.append("""# 1.1ROW_NUMBER() 
SELECT ROW_NUMBER() OVER (ORDER BY intime) AS serial_number,sno,sname,intime
FROM student
WHERE sage < 18;

# 1.2排序原理：计算表里比当前学生入学晚且未成年的学生个数
select 
    (
    select count(distinct intime)#表示计算 Score 列中不同值的数量，即去重后的分数种类数
    from student
    where intime <= sx.intime AND sage<18 #表里比当前学生入学早且未成年的学生个数
    ) as ranks,sno,sname,intime
from student as sx
where sage<18
ORDER BY intime;""")

codes.append("""# 使用连接查询，不能用嵌套查询，因为三个表中都有要找的属性
SELECT student.sno,sname,course.cno,cname,grade
FROM student,stu_course,course
WHERE student.sno=stu_course.sno AND
    stu_course.cno=course.cno AND
    grade<60;""")

codes.append(""""# 有嵌套，但总体算连接
SELECT student.sno,sname,cno,grade
FROM student,stu_course
WHERE student.sno=stu_course.sno AND
    grade IS NOT NULL AND
    grade<60 AND
    student.sno in (
        SELECT sno
        FROM stu_course,course
        WHERE stu_course.cno=course.cno AND grade<60
)
""")

codes.append("""SELECT course.cno,tname,AVG(grade) AS average_grade
FROM teacher,course,stu_course
WHERE teacher.tno=course.tno AND
    course.cno=stu_course.cno AND
    grade IS NOT NULL #排除没有成绩的记录
group by course.cno
order by AVG(grade) desc;
""")

codes.append("""SELECT course.cno,tname,AVG(grade) AS average_grade
FROM teacher,course,stu_course
WHERE teacher.tno=course.tno AND
    course.cno=stu_course.cno AND
    grade IS NOT NULL #排除没有成绩的记录
group by course.cno
HAVING avg(grade) =( #找出最高的平均分
SELECT AVG(grade)
FROM teacher,course,stu_course
WHERE teacher.tno=course.tno AND
    course.cno=stu_course.cno AND
    grade IS NOT NULL #排除没有成绩的记录
group by course.cno
order by AVG(grade) desc #降序排序，取第一个，即为最高的平均分
limit 1);
""")

codes.append("""# 思路：先求平均分，用视图表示中间表，然后找“有两个班级比自己的平均分高”的班级
CREATE VIEW avgGrade # 先找出每个班级的平均分
AS 
	SELECT course.cno AS cno,tname AS tname,AVG(grade) AS average_grade
	FROM teacher,course,stu_course
	WHERE teacher.tno=course.tno AND
		course.cno=stu_course.cno AND
		grade IS NOT NULL #排除没有成绩的记录
	group by course.cno;

SELECT * 
FROM avgGrade as ax
WHERE (select count(distinct average_grade)#平均分去重
	from avgGrade
	where average_grade > ax.average_grade 
    )=2;#表里有两个班级平均分比自己高的班级
    
DROP VIEW avgGrade;
""")

codes.append("""# 7.1用group+having
SELECT sno,sname
FROM student
WHERE sno in(
	select sno
    from stu_course
    WHERE grade IS NOT NULL
    GROUP BY sno
    HAVING COUNT(DISTINCT cno) > 1
);
# 7.2不用group+having
select sx.sno,sname
from stu_course as sx,stu_course as sy,student
where sx.sno=student.sno and
	sy.sno=student.sno and
	sx.grade is not null and
		sy.grade is not null and 
        sx.cno<>sy.cno
group by sx.sno;
""")

codes.append("""# 嵌套查询和连接查询都可以写，这里写嵌套查询
SELECT sno,sname
FROM student
WHERE dmpno in (
	SELECT dmpno
    FROM department
    WHERE tno in (
		SELECT tno
        FROM teacher
        WHERE tname='马冬梅' OR tname='韩宏'
    )
)
UNION
SELECT tno,tname
FROM teacher
WHERE dmpno in (
	SELECT dmpno
    FROM department
    WHERE tno in (
		SELECT tno
        FROM teacher
        WHERE tname='马冬梅' OR tname='韩宏'
    )
);
""")

codes.append("""# 可以用group+having，但这里用否定谓词+关联嵌套
select cno
from stu_course as sx
where cno not in (
	select cno
    from stu_course
    where sx.sno<>sno
);
""")

codes.append("""# 10.1 找选修课程数等于课程数目的学生
select sno,sname
from student
where sno in (
	select sno 
    from stu_course
    group by sno
    having count(*)=(
		select count(*) from course
    )
);
# 10.2 查询没有一门课没被该生选择的学生的学号姓名
select sno,sname
from student
where not exists(
	select *
    from course
    where not exists(
		select *
        from stu_course
	where stu_course.sno = student.sno and
			stu_course.cno=course.cno
    )
);
""")

codes.append("""SELECT cno, MAX(grade) AS max_grade, MIN(grade) AS min_grade, AVG(grade) AS avg_grade
from stu_course
where grade is not null
group by cno
having cno not in(# 找出有成绩不全的班级
	select cno 
    from stu_course
    where grade is null
	)
order by avg_grade desc;
""")

# 找到第num个问题的代码和答案
def myselect(connect,num):
    print("myselect")
    print(codes)
    print(num)
    print(codes[0])
    print(type(num))
    code=codes[num-1]
    if num==1:
        result1=query1_1(connect)
        result1+="\n\n\n"
        result2=query1_2(connect)
        result=result1+result2
    elif num==2:
        result=query2(connect)
    elif num==3:
        result=query3(connect)
    elif num==4:
        result=query4(connect)
    elif num==5:
        result=query5(connect)
    elif num==6:
        result=query6(connect)
    elif num==7:
        result1=query7_1(connect)
        result1+="\n\n\n"
        result2=query7_2(connect)
        result=result1+result2
    elif num==8:
        result=query8(connect)
    elif num==9:
        result=query9(connect)
    elif num==10:
        result=query10_1(connect)
    elif num==11:
        result=query11(connect)
    return code,result