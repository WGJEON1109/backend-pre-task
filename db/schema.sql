-- kidsnote.label definition

CREATE TABLE kidsnote.`label` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- kidsnote.`user` definition

CREATE TABLE kidsnote.`user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(30) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- kidsnote.profile definition

CREATE TABLE kidsnote.`profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `photo_url` varchar(200) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `company` varchar(100) DEFAULT NULL,
  `position` varchar(100) DEFAULT NULL,
  `memo` text,
  `address` text,
  `birthday` date DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `profile_user_id` (`user_id`),
  CONSTRAINT `profile_user_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- kidsnote.profile_label definition

CREATE TABLE kidsnote.`profile_label` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_id` bigint NOT NULL,
  `label_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `profile_id` (`profile_id`,`label_id`),
  KEY `label_id` (`label_id`),
  CONSTRAINT `profile_label_ibfk_1` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`id`) ON DELETE CASCADE,
  CONSTRAINT `profile_label_ibfk_2` FOREIGN KEY (`label_id`) REFERENCES `label` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;