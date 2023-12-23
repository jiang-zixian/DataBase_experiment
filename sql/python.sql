drop database `python`;
create database `python`;
USE `python`;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- 数据库： `python`
--

-- --------------------------------------------------------

-- `account`

CREATE TABLE `account` (#用户
  `usrno` varchar(20) NOT NULL,#用户号，如果是学生是学号，如果是老师是工号
  `usrtype` varchar(20) NOT NULL,#用户类型 'admin' 'teacher' 'student'
  `password` varchar(20) NOT NULL#密码
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `account` (`usrno`,`usrtype`, `password`) VALUES
('666770', '管理员','00000000'),
('666771', '管理员','00000000'),
('201632120710', '学生', 'password1'),
('201632120711', '学生', 'password2'),
('201632120778', '学生', 'password3'),
('201732120762', '学生', 'password4'),
('201732120768', '学生', 'password5'),
('201732120777', '学生', 'password6'),
('201832120719', '学生', 'password7'),
('201832120779', '学生', 'password8'),
('201932120720', '学生', 'password9'),
('202005748273', '学生', 'password10'),
('202006738237', '学生', 'password11'),
('202006010300', '学生', 'password12'),
('202100000001', '学生', 'password13'),
('202100000002', '学生', 'password14'),
('202100000003', '学生', 'password15'),
('202100000004', '学生', 'password16'),
('202100000005', '学生', 'password17'),
('123110', '教师', 'password13'),
('123122', '教师', 'password14'),
('123123', '教师', 'password15'),
('123124', '教师', 'password16'),
('123125', '教师', 'password17');

-- --------------------------------------------------------

-- `student`

CREATE TABLE `student` (
  `sno` varchar(20) not null,#学号
  `sname` varchar(10) not null,#姓名
  `ssex` enum('男','女') not null default'男' comment'性别',#性别
  `sage` int(4) not null,#年龄
  `dmpno` varchar(10) not null,#所属院系
  `intime` datetime not null#入学时间
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `student` (`sno`, `sname`, `ssex`, `sage`, `dmpno`, `intime`) VALUES
('201632120710', '马花藤', '男', 23, 'd003', '2016-09-01 00:00:00'),
('201632120711', '马晕', '男', 23, 'd003', '2016-09-01 00:00:00'),
('201632120778', '李晓龙', '男', 21, 'd003', '2016-09-01 00:00:00'),
('201732120762', '鲁智深', '男', 21, 'd001', '2017-09-01 00:00:00'),
('201732120768', '李云隆', '男', 21, 'd003', '2017-09-01 00:00:00'),
('201732120777', '张晓梅', '女', 20, 'd001', '2017-09-01 00:00:00'),
('201832120719', '孙文空', '女', 19, 'd002', '2018-09-01 00:00:00'),
('201832120779', '黄飞红', '女', 20, 'd002', '2018-09-01 00:00:00'),
('201932120720', '张阿红', '女', 19, 'd002', '2019-09-01 00:00:00'),
('202005748273', 'smile', '男', 19, 'd004', '2006-04-30 00:00:00'),
('202006738237', 'xion', '男', 19, 'd002', '1002-03-04 00:00:00'),
('202006010300', 'zhangsan', '男', 19, 'd004', '2001-01-01 00:00:00'),
('202100000001', '小明', '男', 17, 'd001', '2021-09-01 00:00:00'),
('202100000002', '小红', '女', 16, 'd002', '2021-09-02 00:00:00'),
('202100000003', '小李', '男', 15, 'd003', '2021-10-01 00:00:00'),
('202100000004', '小丽', '女', 18, 'd004', '2021-12-01 00:00:00'),
('202100000005', '小张', '男', 17, 'd001', '2021-09-01 09:00:00');

-- --------------------------------------------------------

-- 表的结构 `teacher`
CREATE TABLE `teacher` (
  `tno` varchar(20) NOT NULL,#教工号
  `tname` varchar(10) NOT NULL,#姓名
  `tsex` varchar(2) NOT NULL,#性别
  `tphone` varchar(20) NOT NULL,#联系电话
  `dmpno` varchar(10) NOT NULL,#院系号
  `profess` varchar(10) NOT NULL#职称
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `teacher` (`tno`, `tname`, `tsex`, `tphone`, `dmpno`, `profess`) VALUES
('123110', '唐伯虎', '男', '17398443912', 'd001', '副教授'),
('123122', '谭英文', '男', '17398442121', 'd002', '副教授'),
('123123', '陈读', '男', '17398447611', 'd003', '副教授'),
('123124', '韩宏', '女', '17398440222', 'd002', '教授'),
('123125', '马冬梅', '女', '17398449123', 'd004', '副教授');

-- --------------------------------------------------------

-- `course`

CREATE TABLE `course` (
  `cno` varchar(10) NOT NULL,#课程号
  `cname` varchar(10) NOT NULL,#课程名
  `tno` varchar(10) NOT NULL,#授课老师号
  `c_period` varchar(10) NOT NULL,#上课时间
  `clocation` varchar(10) NOT NULL,#上课教室
  `credit` int(2) NOT NULL,#学分
  `ctime` int(2) NOT NULL#学时
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `course` (`cno`, `cname`, `tno`, `c_period`, `clocation`, `credit`, `ctime`) VALUES
('c001', '微观经济学', '123123', '周四 第10-12节', '25-101', 3, 80),
('c002', '宏观经济学', '123124', '周五 第10-12节', '22-402', 6, 60),
('c003', '英语名著欣赏', '123125', '周三 第1-3节', '16-301', 2, 60),
('c004', '数学分析', '123110', '周二 第1-4节', '20-201', 6, 80),
('c005', '高等数学', '123110', '周四 第1-4节', '20-301', 6, 80),
('c006', '商务英语写作', '123122', '周四 第8-9节', '15-201', 4, 80),
('c007', '数据库原理', '123110', '周四 第8-9节', '15-301', 3, 64);

-- --------------------------------------------------------

-- 表的结构 `department`

CREATE TABLE `department` (#院系(院系号、院系名、院长工号) 
  `dmpno` varchar(5) NOT NULL,
  `dname` varchar(10) NOT NULL,
  `tno` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `department` (`dmpno`, `dname`, `tno`) VALUES
('d001', '经济学院', '123110'),
('d002', '英语学院', '123124'),
('d003', '数学学院', '123123'),
('d004', '计算机学院', '123125');

-- --------------------------------------------------------

-- `stu_course`

CREATE TABLE `stu_course` (
  `sno` varchar(20) NOT NULL,#学号
  `cno` varchar(10) NOT NULL,#课程号
  `grade` int(3) DEFAULT NULL#成绩
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `stu_course` (`sno`, `cno`, `grade`) VALUES
('201632120778', 'c004', 36),
('201632120778', 'c005', 80),
('201632120778', 'c001', 80),
('201632120778', 'c002', 80),
('201632120778', 'c003', 80),
('201632120778', 'c006', 80),
('201632120778', 'c007', 90),
('201732120762', 'c002', 50),
('201732120768', 'c004', 70),
('201732120777', 'c001', NULL),
('201732120777', 'c002', 73),
('201832120719', 'c005', 90),
('201832120719', 'c006', 92),
('201832120779', 'c003', 75),
('202006010300', 'c002', 100),
('202006010300', 'c004', 67),
('202100000001', 'c006', 37),
('202100000002', 'c003', 98),
('202100000003', 'c001', 65),
('202100000004', 'c002', 32),
('202100000004', 'c007', 95),
('202100000005', 'c003', NULL);

INSERT INTO `stu_course` (`sno`, `cno`, `grade`) VALUES('202100000001', 'c007', 89);

-- --------------------------------------------------------

-- 表的结构 `teacher_course`

CREATE TABLE `teacher_course` (#教师授课（教工号，课程号）
  `tno` varchar(10) NOT NULL,
  `cno` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `teacher_course` (`tno`, `cno`) VALUES
('123110', 'c004'),
('123110', 'c005'),
('123122', 'c006'),
('123123', 'c001'),
('123124', 'c002'),
('123125', 'c003');
-- --------------------------------------------------------

--  `stu_reward_punishment`

CREATE TABLE `stu_reward_punishment` (#奖惩情况（奖惩记录号，学生学号，奖励，惩罚）
  `rpno` varchar(20) NOT NULL,
  `sno` varchar(20) NOT NULL,
  `reward` varchar(100) DEFAULT NULL,
  `punishment` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk;

INSERT INTO `stu_reward_punishment` (`rpno`,`sno`, `reward`, `punishment`) VALUES
('9998887770','201832120779', '校一等奖学金', NULL),
('9998887771','201832120719', NULL, '全校通告批评'),
('9998887772','202006738237', NULL, '校一等奖学金'),
('9998887773','201832120719', 'student good', 'lose off'),
('9998887774','202006738237', '', 'shi拾金不昧'),
('9998887775','201832120719', '拾金不昧，乐于助人', '');

-- --------------------------------------------------------

--
-- 替换视图以便查看 `jxj`
-- （参见下面的实际视图）
--
CREATE TABLE `jxj` (
`sno` varchar(20)
,`sname` varchar(10)
,`ssex` varchar(2)
,`reward` varchar(100)
,`punishment` varchar(100)
);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `jxjf`
-- （参见下面的实际视图）
--
CREATE TABLE `jxjf` (
`sno` varchar(20)
,`sname` varchar(10)
,`ssex` varchar(2)
,`reward` varchar(100)
,`punishment` varchar(100)
);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `jxjm`
-- （参见下面的实际视图）
--
CREATE TABLE `jxjm` (
`sno` varchar(20)
,`sname` varchar(10)
,`ssex` varchar(2)
,`reward` varchar(100)
,`punishment` varchar(100)
);

-- --------------------------------------------------------

--
-- 替换视图以便查看 `student_view`
-- （参见下面的实际视图）
--
CREATE TABLE `student_view` (
`username` varchar(20)
,`password` varchar(20)
);

-- --------------------------------------------------------

--
-- 视图结构 `jxj`
--
DROP TABLE IF EXISTS `jxj`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` 
SQL SECURITY DEFINER VIEW `jxj`  
AS SELECT `a`.`sno` AS `sno`, `a`.`sname` AS `sname`, `a`.`ssex` AS `ssex`, `b`.`reward` AS `reward`, `b`.`punishment` AS `punishment` 
FROM (`student` `a` join `stu_reward_punishment` `b` on((`a`.`sno` = `b`.`sno`))) ;

-- --------------------------------------------------------

--
-- 视图结构 `jxjf`
--
DROP TABLE IF EXISTS `jxjf`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `jxjf`  AS SELECT `a`.`sno` AS `sno`, `a`.`sname` AS `sname`, `a`.`ssex` AS `ssex`, `b`.`reward` AS `reward`, `b`.`punishment` AS `punishment` FROM (`student` `a` join `stu_reward_punishment` `b` on((`a`.`sno` = `b`.`sno`))) WHERE (`a`.`ssex` = '女') ;

-- --------------------------------------------------------

--
-- 视图结构 `jxjm`
--
DROP TABLE IF EXISTS `jxjm`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `jxjm`  AS SELECT `a`.`sno` AS `sno`, `a`.`sname` AS `sname`, `a`.`ssex` AS `ssex`, `b`.`reward` AS `reward`, `b`.`punishment` AS `punishment` FROM (`student` `a` join `stu_reward_punishment` `b` on((`a`.`sno` = `b`.`sno`))) WHERE (`a`.`ssex` = '男') ;

-- --------------------------------------------------------
-- 主键
ALTER TABLE `account`
ADD PRIMARY KEY (`usrno`);

ALTER TABLE `student`
ADD PRIMARY KEY (`sno`);

ALTER TABLE `teacher`
ADD PRIMARY KEY (`tno`);

ALTER TABLE `course`
ADD PRIMARY KEY (`cno`);

ALTER TABLE `department`
ADD PRIMARY KEY (`dmpno`);

ALTER TABLE `stu_course`
ADD PRIMARY KEY (`sno`, `cno`);

ALTER TABLE `teacher_course`
ADD PRIMARY KEY (`tno`, `cno`);

ALTER TABLE `stu_reward_punishment`
ADD PRIMARY KEY (`rpno`);

-- 外键
ALTER TABLE `student`
ADD FOREIGN KEY (`dmpno`) REFERENCES `department`(`dmpno`);

ALTER TABLE `teacher`
ADD FOREIGN KEY (`dmpno`) REFERENCES `department`(`dmpno`);

ALTER TABLE `course`
ADD FOREIGN KEY (`tno`) REFERENCES `teacher`(`tno`);

ALTER TABLE `department`
ADD FOREIGN KEY (`tno`) REFERENCES `teacher`(`tno`);

ALTER TABLE `stu_course`
ADD FOREIGN KEY (`sno`) REFERENCES `student`(`sno`),
ADD FOREIGN KEY (`cno`) REFERENCES `course`(`cno`);

ALTER TABLE `teacher_course`
ADD FOREIGN KEY (`tno`) REFERENCES `teacher`(`tno`),
ADD FOREIGN KEY (`cno`) REFERENCES `course`(`cno`);

ALTER TABLE `stu_reward_punishment`
ADD FOREIGN KEY (`sno`) REFERENCES `student`(`sno`);

