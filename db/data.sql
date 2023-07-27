-- user data
INSERT INTO kidsnote.`user` (password,last_login,is_superuser,email,name,is_active,is_staff,created_at,updated_at,first_name,last_name) VALUES
	('pbkdf2_sha256$260000$bEdUK1Jp39x0ibEUEMQ7Id$5M15tZRHqE3UwtnDZ9AoOx8pKy95CXcQl+h53Xn7vSA=','2023-07-27 06:35:22.152458000',0,'tq1234@test.com','',1,0,'2023-07-27 05:56:13.035124000','2023-07-27 05:56:13.035163000','','');


-- label 테이블 데이터
INSERT INTO kidsnote.label (name) VALUES
    ('가족'),
    ('친구'),
    ('동료'),
    ('고객'),
    ('기타');

-- profile 테이블 데이터
INSERT INTO kidsnote.profile (photo_url,name,email,phone,company,`position`,memo,address,birthday,website,user_id) 
VALUES
	 ('https://i.pravatar.cc/300','홍길동','hong@example.com','010-1234-5678','A회사','부장','메모1','서울시 강남구','1990-01-01','https://hong-example.com',1),
	 ('https://i.pravatar.cc/300','김철수','kim@example.com','010-9876-5432','B회사','과장','메모2','서울시 종로구','1985-05-15','https://kim-example.com',1),
	 ('https://i.pravatar.cc/300','이영희','lee@example.com','010-5555-6666','C회사','대리','메모3','인천시 남동구','1992-11-30','https://lee-example.com',1),
	 ('https://i.pravatar.cc/300','박민준','park@example.com','010-7777-8888','D회사','사원','메모4','부산시 해운대구','1998-07-20','https://park-example.com',1),
	 ('https://i.pravatar.cc/300','장현우','jang@example.com','010-2222-3333','E회사','사장','메모5','대구시 서구','1977-03-10','https://jang-example.com',1);
	-- profile_label 테이블 데이터
INSERT INTO kidsnote.profile_label (profile_id, label_id) VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3),
    (3, 4),
    (4, 4),
    (5, 5);


