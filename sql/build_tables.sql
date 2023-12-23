create table if not exists `student`(#学生
	sno varchar(20) primary key,#学号
	sname varchar(10) not null,#姓名
	ssex enum('男','女') not null default'男' comment'性别',#性别
	sage int(4) not null,#年龄
	dmpno varchar(10) not null,#所属院系
	intime datetime not null#入学时间
); #"创建一个表结构，设置为学生表"

create table if not exists `course` (
	cno varchar(10) primary key,#课程号
	cname varchar(10) not null,#课程名
	tno varchar(10) not null,#授课老师号
	cperiod varchar(10) not null,#上课时间
	clocation varchar(10) not null,#上课教室
	credit int(2) not null,#学分
	ctime int(2) #学时
);#"创建一个表结构，设置为课程信息表"

create table if not exists `teacher` (# 教师
	tno varchar(20) primary key,#教工号
	tname varchar(10) not null,#姓名
	tsex varchar(2) not null,#性别
	tphone varchar(20) not null,#联系电话
	dmpno varchar(10) not null,#院系号
	profess varchar(10) not null#职称
); #"创建一个表结构，设置为老师表"

create table if not exists `department` (#院系(院系号、院系名、院长名) 
	dmpno varchar(10) primary key,
	dname varchar(10) not null,
	dmphead varchar(10) not null
); #"创建一个表结构，设置为院系表，"

create table if not exists `stu_course` (#学生成绩表
	sno varchar(20),#学号
	cno varchar(10),#课程号
	grade int(3) default null,#成绩
	primary key (sno, cno)  
);#"创建一个表结构，设置为学生成绩表"

create table if not exists `teacher_course` (#教师授课（教工号，课程号）
	tno varchar(10),
	cno varchar(10),
	primary key (tno, cno)
);#"创建一个表结构，设置为老师授课表"

create table if not exists `class_stu_num` (
	class varchar(10) primary key,
	stu_num int default 0
);#"创建一个表结构，设置为学生上课对应教室的表"

create table if not exists `stu_reward_punishment` (#奖惩情况（学生学号，奖励，惩罚）
	sno varchar(20) not null,
	reward varchar(100) default null,
	punishment varchar(100) default null
);#"创建一个表结构，设置学生奖惩表"

create table if not exists `account` (
	username varchar(20) primary key,
	passward varchar(20) not null
);#"设置一个账户信息表，对应的是登陆用户的信息表"


show DATABASES;
show tables;