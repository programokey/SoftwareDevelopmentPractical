drop schema PetHospital;
create schema PetHospital;
use PetHospital;
create table User(
	id	varchar(20)	primary key,
	name	varchar(20),
	passwd	varchar(64),
	phoneNumber	varchar(20),
	email	varchar(20),
	gender	enum('male', 'female', 'unknown') default 'unknown'
);

create table UserGroup(
	id	varchar(20)	primary key,
	`group` enum('intern', 'admin', 'stuff') default 'intern',
	foreign key (id) references User(id)
);

create table Test(
	id int primary key auto_increment,
	name varchar(50),
	description	text,
	startTime	datetime,
	endTime	datetime,
	duration	time,
	confidential	boolean,
	creator	varchar(20),
	foreign key (creator) references User(id)
);

create table Problem(
	id int primary key auto_increment,
	problem	text,
	multipleAnswer	boolean,
	creator	varchar(20),
	foreign key (creator) references User(id)
);

create table Choice(
	id int auto_increment,
	problemID	int,
	choice	text,
	isAnswer	boolean,
	primary	key(id),
	foreign key (problemID) references Problem(id)
);

create table TestProblem(
	testID	int,
	problemID	int,
	point	float not null,
	primary key(testID, problemID),
	foreign key (testID) references Test(id),
	foreign key (problemID) references Problem(id)
);

create table TestParticipation(
	userID	varchar(20),
	testID	int,
	beginTime	datetime,
	score	float default NULL,
	primary key(userID, testID),
	foreign key (userID) references User(id),
	foreign key (testID) references Test(id)
);

create table Answer(
	userID	varchar(20),
	testID	int,
	problemID	int,
	choiceID	int,
	primary key(userID, testID, problemID, choiceID),
	foreign key (userID) references User(id),
	foreign key (testID) references Test(id),
	foreign key (problemID) references Problem(id),
	foreign key (choiceID) references Choice(id)
);

create table Flow(
	id int,
	`order` int,
	content	varchar(256),-- path to the picture or video
	type enum('Video', 'Picture'),
	description	text,
	primary key(id, `order`)
);

create table Equipment(
	id int primary key auto_increment,
	name varchar(128),
	description text,
	operationalApproach text,
	location	varchar(128),
	flowID	int  default NULL,
	foreign key (flowID) references Flow(id)
);

create table Department(
	name	varchar(128) primary key,
	location	varchar(128),
	basicStructure	text,
	function		text,
	x_pos	int,
	y_pos	int,
	radius	int
);

create table Job(
	name	varchar(128) primary key,
	description	text,
	dosAndDonots	text,
	jobFlowID	int default NULL,
	foreign key (jobFlowID) references Flow(id)
);

create table Role(
	name	varchar(128) primary key,
	description	text
);

create table DepartmentRole( /*jobs in the department*/
	department	varchar(128),
	role	varchar(128),
	primary key(department, role),
	foreign key (department) references Department(name),
	foreign key (role) references Role(name)
);

create table RoleJob(
	role	varchar(128),
	department	varchar(128),
	job	varchar(128),
	primary key(role, department, job),
	foreign key (role) references DepartmentRole(role),
	foreign key (department) references DepartmentRole(department),
	foreign key (job) references Job(name)
);

create table DiseaseCategory(
	name varchar(128) primary key
);

create table Disease(
	name	varchar(128),
	diseaseCategory	varchar(128),
	department	varchar(128),
	description text,
	primary key (name, diseaseCategory),
	foreign key (department) references DepartmentRole(department),
	foreign key (diseaseCategory) references DiseaseCategory(name)
);

create table Medicine(
	ApprovalNumber	varchar(128) primary key,
	name	varchar(128),
	description text,
	price	float
);

create table MedicalExamination(
	name	varchar(128) primary key,
	description text,
	price	float
);

create table NumericalIndex(-- Numerical indices of medical examinations
	id	int primary key auto_increment,
	examination	varchar(128),
	name	varchar(128),
	unit	varchar(32),
	description	text,
	low		float,
	high	float,
	foreign key (examination) references MedicalExamination(name)
);

create table Operation(
	name	varchar(128) primary key,
	description text,
	dosAndDonots	text,
	price	float -- exclude the medicine expense
	-- opeationFlowID	int references Flow(id)
);

create table OpeationEquipment(-- Equipments used in the opeation
	opeationName	varchar(128),
	equipmentID int references Equipment(id),
	primary key (opeationName, equipmentID),
	foreign key (opeationName) references Operation(name),
	foreign key (equipmentID) references Equipment(id)
);

create table OpeationMedicine(-- Medicines used in the opeation
	opeationName	varchar(128),
	medicineApprovalNumber	varchar(128),
	medicineName	varchar(128),-- redundance for performance
	primary key (opeationName, medicineApprovalNumber),
	foreign key (opeationName) references Operation(name),
	foreign key (medicineApprovalNumber) references Medicine(ApprovalNumber)
);

create table `Case`(
	id int primary key auto_increment,
	doctor	varchar(128),
	petType	varchar(128),
	petAge	varchar(128),
	petGender varchar(128),
	disease	varchar(128),
	symptoms 	text,
	diagnosis	text,
	treatment	text,
	expense		float,
	flow	int default NULL,
	foreign key (disease)  references Disease(name),
	foreign key (flow)  references Flow(id)
);

create table CaseExamination(
	id	int primary key auto_increment,
	caseId	int,
	examination	varchar(128),
	conclusion	text,
	foreign key (examination)  references MedicalExamination(name),
	foreign key (caseId)  references `Case`(id)
);-- cluster index on (caseId, operation)

create table CaseOperation(
	id	int auto_increment,
	caseId	int,
	operation varchar(128),
	primary key (id),
	foreign key (caseId)  references `Case`(id),
	foreign key (operation) references Operation(name)
);-- cluster index on (caseId, operation)

create table Prescription(
	id	int auto_increment primary key,
	caseId	int,
	description		text,
	foreign key (caseId)  references `Case`(id)
);

create table PrescriptionMedicine(
	PrescriptionID	int,
	medicineApprovalNumber	varchar(128),
	medicineName	varchar(128),-- redundance for performance
	unit	float,
	primary key (PrescriptionID, medicineApprovalNumber),
	foreign key (PrescriptionID) references Prescription(id),
	foreign key (medicineApprovalNumber) references Medicine(ApprovalNumber)
);

create table NumericalMedicalExaminationResult(
	caseExaminationID int,
	`type`	int,
	value float,
	primary key (caseExaminationID, type),
	foreign key (caseExaminationID)  references CaseExamination(id),
	foreign key (`type`)  references NumericalIndex(id)
);

create table GraphicMedicalExaminationResult(
	caseExaminationID int,
	picture	varchar(512),
	description text,
	primary key (caseExaminationID, picture),
	foreign key (caseExaminationID) references CaseExamination(id)
);
