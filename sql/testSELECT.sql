# 专门写查询语句

# 1.找出目前该学校的未成年学生，并按照入学时间从早到晚为他们生成序号
# 1.1ROW_NUMBER() 
SELECT
    ROW_NUMBER() OVER (ORDER BY intime) AS serial_number,
    sno,
    sname,
    intime
FROM
    student
WHERE
    sage < 18;

# 1.2排序原理：计算表里比当前学生入学晚且未成年的学生个数
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


 # 2.查找有科目不及格的学生，显示该学生的姓名学号、不及格课程的课程号和课程名称，该学生对应的成绩
 # 使用连接查询，不能用嵌套查询，因为三个表中都有要找的属性
 SELECT
    student.sno,
    sname,
    course.cno,
    cname,
    grade
FROM
    student,stu_course,course
WHERE
    student.sno=stu_course.sno AND
    stu_course.cno=course.cno AND
    grade<60;

 # 3.查找有科目不及格的学生，显示该学生的姓名学号、不及格课程的课程号，该学生对应的成绩
 # 有嵌套，但总体算连接
 SELECT
    student.sno,
    sname,
    cno,
    grade
FROM
    student,stu_course
WHERE
	student.sno=stu_course.sno AND
	student.sno in (
		SELECT sno
        FROM stu_course,course
        WHERE stu_course.cno=course.cno AND grade<60
    );
    
# 4.找出每个班级的课程号，任课老师姓名和平均分，按平均分降序排序
SELECT 
	course.cno,tname,AVG(grade) AS average_grade
FROM 
	teacher,course,stu_course
WHERE
	teacher.tno=course.tno AND
    course.cno=stu_course.cno AND
    grade IS NOT NULL #排除没有成绩的记录
group by course.cno
order by AVG(grade) desc;

# 5.哪个班级的平均分最高？找出这个班级的课程号，任课老师姓名和平均分
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
    grade IS NOT NULL #排除没有成绩的记录
group by course.cno
order by AVG(grade) desc #降序排序，取第一个，即为最高的平均分
limit 1);

# 6.查找平均分第三高的那个班级的课程号，任课老师姓名和平均分，用视图
# 思路：先求平均分，用视图表示中间表，然后找“有两个班级比自己的平均分高”的班级
CREATE VIEW avgGrade # 先找出每个班级的平均分
AS 
	SELECT 
		course.cno AS cno,tname AS tname,AVG(grade) AS average_grade
	FROM 
		teacher,course,stu_course
	WHERE
		teacher.tno=course.tno AND
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

# 7.有两门及以上的课有有效成绩的同学的学号姓名
# 7.1用group+having
SELECT 
	sno,sname
FROM
	student
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




# 8.查找所属学院院长为马冬梅或韩宏的、所有师生的学号/工号和姓名 使用UNION
# 嵌套查询和连接查询都可以写，这里写嵌套查询
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
);

# 9.查询只有一个学生的课程的课程号
# 可以用group+having，但这里用否定谓词+关联嵌套
select cno
from stu_course as sx
where cno not in (
	select cno
    from stu_course
    where sx.sno<>sno
);

# 10.查询选修了所有课程的学生的学号姓名
# 10.1 找选修课程数等于课程数目的学生
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

    
# 11.查询所有课程成绩的最高分、最低分、平均分。成绩不全的课程不参与统计，最终结果按平均分降序排列
SELECT cno, MAX(grade) AS max_grade, MIN(grade) AS min_grade, AVG(grade) AS avg_grade
from stu_course
where grade is not null
group by cno
having cno not in(# 找出有成绩不全的班级
	select cno 
    from stu_course
    where grade is null
	)
order by avg_grade desc;



SELECT sno,sname,ssex,sage,dname,intime
                FROM student,department
                WHERE student.dmpno=department.dmpno;
                
SELECT sno,sname,reward,punishment FROM stu_reward_punishment WHERE sno='201832120719';

SELECT teacher.tno,tname,tsex,tphone,dname,profess
                FROM teacher,department
                WHERE teacher.dmpno=department.dmpno AND teacher.tno='123110';
	
	
SELECT department.dmpno, dname, teacher.tno, tname FROM department,teacher WHERE department.tno=teacher.tno;


SELECT sno,sname,ssex,sage,dname,intime,password
                FROM student,account,department
                WHERE student.dmpno=department.dmpno AND student.sno=account.usrno;




	
SELECT teacher.tno,tname,tsex,tphone,dname,profess,password
                FROM teacher,account,department
                WHERE teacher.dmpno=department.dmpno AND teacher.tno=account.usrno;

    



