insert into Test value(1, 'test测试1', '测试测试的测试', '2018-1-1 12:00:00', '2018-4-1 12:00:00', '2:00', false, '22');
insert into Test value(2, 'test测试2', '测试测试的测试', '2018-4-1 12:00:00', '2018-5-1 12:00:00', '1:30', false, '22');
insert into Test value(4, 'test测试4', '测试测试的测试', '2018-5-1 12:00:00', '2018-6-1 12:00:00', '1:30', false, '22');

insert into Problem value(1, '测试测试的问题1', false, '22');
insert into Problem value(2, '测试测试的问题2', TRUE, '22');
insert into Problem value(3, '测试测试的问题3', false, '22');

insert into Choice value(1, 1, '测试测试的问题1的答案1', false);
insert into Choice value(2, 1, '测试测试的问题1的答案2', false);
insert into Choice value(3, 1, '测试测试的问题1的答案3', true);
insert into Choice value(4, 1, '测试测试的问题1的答案4', false);

insert into Choice value(5, 2, '测试测试的问题2的答案1', false);
insert into Choice value(6, 2, '测试测试的问题2的答案2', true);
insert into Choice value(7, 2, '测试测试的问题2的答案3', true);
insert into Choice value(8, 2, '测试测试的问题2的答案4', false);

insert into Choice value(9, 3, '测试测试的问题3的答案1', false);
insert into Choice value(10, 3, '测试测试的问题3的答案2', true);
insert into Choice value(11, 3, '测试测试的问题3的答案3', false);
insert into Choice value(12, 3, '测试测试的问题3的答案4', false);

insert into TestProblem value(1, 1, 20);
insert into TestProblem value(1, 2, 20);
insert into TestProblem value(1, 3, 20);

insert into TestProblem value(2, 1, 50);
insert into TestProblem value(2, 2, 50);

insert into TestProblem value(3, 2, 50);
insert into TestProblem value(3, 3, 50);

insert into TestParticipation value('0', 1, NULL, NULL);
insert into TestParticipation value('0', 2, '2018-4-1 12:00:00', NULL);
insert into TestParticipation value('0', 4, NULL, NULL);

insert into TestParticipation value('1', 1, NULL, NULL);
insert into TestParticipation value('1', 2, NULL, NULL);

insert into Answer value('0', 1, 1, 3);
insert into Answer value('0', 1, 2, 7);
insert into Answer value('0', 1, 3, 11);

insert into Answer value('0', 2, 1, 3);
insert into Answer value('0', 2, 2, 8);

insert into Answer value('1', 1, 1, 3);
insert into Answer value('1', 1, 2, 7);
insert into Answer value('1', 1, 2, 6);
insert into Answer value('1', 1, 3, 10);


insert into Answer value('1', 2, 1, 3);
insert into Answer value('1', 2, 2, 6);
insert into Answer value('1', 2, 2, 7);
