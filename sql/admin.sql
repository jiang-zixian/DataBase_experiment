USE `admin`;

CREATE TABLE IF NOT EXISTS `user` (
    username VARCHAR(20) PRIMARY KEY,
    password VARCHAR(20) NOT NULL
);

INSERT INTO `user` VALUES ('admin', '00000000');
INSERT INTO `user` VALUES ('张三', '00000000');
INSERT INTO `user` VALUES ('李四', '00000000');
INSERT INTO `user` VALUES ('王五', '00000000');
INSERT INTO `user` VALUES ('何嘉', '00000000');
INSERT INTO `user` VALUES ('张武', '00000000');
INSERT INTO `user` VALUES ('李华', '00000000');

select * from `user`;#把student表格内所有资料搜寻出来
