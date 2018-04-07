use PetHospital;
insert into User value ('0', 'test', 'test', '2333', 'test@test.com', 'male', 'intern');
insert into User value ('1', 'test1', '12345677', '021-68512277', 'strongNow@gov.com', 'male', 'intern');


insert into Department value('CT', 'gateway', 'funny', 'CT Scan', 332, 332);
insert into Department value('血液科', '二楼楼梯口', '主任: 徳拉古拉·布拉德', '抽血', 233, 233);
insert into Department value('精神科', '地下室车库旁', '科室主任：磁暴步兵杨永信', '你需要被电一下', 123, 123);


insert into Flow value(1, 1, '', 'Video', 'test Flow');

insert into Equipment value(1, '电击治疗仪', '精神科', '用于电击小朋友', '', '精神科电击室', null);
insert into Equipment value(2, 'CT机', '精神科', '用于CT检查', '', '精神科电击室', null);
insert into Equipment value(3, '滑机', '精神科', '用于产生滑稽', '', '精神科滑稽室', null);
insert into Equipment value(4, '垃机', '精神科', '用于排除垃圾思想', '', '精神科排毒室', 1);


insert into Role value('杨永信', '有一定几率发动闪电攻击');
insert into Role value('开膛手杰克', '给病患执行腹部手术');
insert into Role value('Professor X', 'read patients\' mind');

insert into DepartmentRole value('精神科', '杨永信');
insert into DepartmentRole value('精神科', 'Professor X');

insert into Flow value(0, 0, '/flow/1.jpg', 'Picture',  '展示Doge图片');
insert into Flow value(0, 1, '/flow/2.avi', 'Video', '播放Doge视频');

insert into Job value('我觉得你需要被电一下', '判断病患是否需要点击', '注意观察', NULL);
insert into Job value('十万伏特', '释放10万伏特的电压', '注意接地', NULL);
insert into Job value('精神污染', '污染患者精神', '每天早晚各一次', 0);

insert into RoleJob value('杨永信', '精神科', '我觉得你需要被电一下');
insert into RoleJob value('杨永信', '精神科', '十万伏特');
insert into RoleJob value('Professor X', '精神科', '精神污染');


insert into Medicine value('滑稽准字FDA233', '伸腿瞪眼丸', '不论男女老幼,疑难杂症,服用此药后,即刻痊愈,只溶在口,不溶在手', 2.33);
insert into Medicine value('滑稽准字FDA2333', '脑残片', '用于提高智商', 250.0);


insert into DiseaseCategory value('缺心眼');
insert into DiseaseCategory value('嗜睡');

insert into Disease value('先天性心眼不足', '缺心眼', '精神科', '先天不足导致的缺心眼');
insert into Disease value('早上睡不醒', '嗜睡', '精神科', '人生从来没上午');
insert into Disease value('上课睡觉', '嗜睡', '精神科', '听取人生经验');


insert into `Case` value(1, '杨永信', '哈士奇', '2.333岁', 'unknown', '先天性心眼不足', '时常犯二', '经诊断为典型的先天性缺心眼', '使用脑残片进行药物治疗', 2.333, NULL);
insert into `Case` value(2, '杨永信', '阿拉斯加', '3岁', 'unknown', '先天性心眼不足', '雪橇三傻', '典型的先天性缺心眼', '使用脑残片进行药物治疗', 2.333, NULL);
insert into `Case` value(3, 'Professor X', 'Doge', '15个月', '雌性', '早上睡不醒', '早上睡到12点', '经诊断为典型的嗜睡', '使用精神污染进治疗', 23.33, NULL);


insert into Prescription value(1, 1, '针对哈士奇先天性心眼不足的药物治疗');

insert into PrescriptionMedicine value(1, '滑稽准字FDA2333', '脑残片', 12);
insert into PrescriptionMedicine value(1, '滑稽准字FDA233', '伸腿瞪眼丸', 2);


insert into Prescription value(2, 1, '针对哈士奇先天性心眼不足的药物治疗的补充');

insert into PrescriptionMedicine value(2, '滑稽准字FDA2333', '脑残片', 12);
insert into PrescriptionMedicine value(2, '滑稽准字FDA233', '伸腿瞪眼丸', 2);




