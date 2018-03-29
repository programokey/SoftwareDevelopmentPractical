use PetHospital;
insert into PetHospital.User value (0, 'test', 'test', '2333', 'test@test.com', 'male', 'intern');
insert into PetHospital.User value (1, 'test1', '12345677', '021-68512277', 'strongNow@gov.com', 'male', 'intern');


insert into Department value('CT', 'gateway', 'funny', 'CT Scan', 332, 332);
insert into Department value('血液科', '二楼楼梯口', '主任: 徳拉古拉·布拉德', '抽血', 233, 233);
insert into Department value('精神科', '地下室车库旁', '科室主任：磁暴步兵杨永信', '你需要被电一下', 123, 123);


insert into Equipment value(0, '电击治疗仪', '精神科', '用于电击小朋友', '', '精神科电击室', NULL)
insert into Equipment value(1, 'CT机', '精神科', '用于电击小朋友', '', '精神科电击室', NULL)
insert into Equipment value(2, '滑机', '精神科', '用于产生滑稽', '', '精神科滑稽室', NULL)

insert into Role value('杨永信', '有一定几率发动闪电攻击')
insert into Role value('开膛手杰克', '给病患执行腹部手术')
insert into Role value('Professor X', 'read patients\' mind')

insert into DepartmentRole value('精神科', '杨永信')
insert into DepartmentRole value('精神科', 'Professor X')

insert into Job value('我觉得你需要被电一下', '判断病患是否需要点击', '注意观察', NULL)
insert into Job value('十万伏特', '释放10万伏特的电压', '注意接地', NULL)

insert into RoleJob value('精神科', '杨永信', '我觉得你需要被电一下')
insert into RoleJob value('精神科', '杨永信', '十万伏特')

