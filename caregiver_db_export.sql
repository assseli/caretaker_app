-- MySQL dump 10.13  Distrib 9.5.0, for macos26.1 (arm64)
--
-- Host: localhost    Database: caregiver_db
-- ------------------------------------------------------
-- Server version	9.5.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'fcb51732-c952-11f0-93ef-f420c26acfcd:1-488';

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `id` int NOT NULL AUTO_INCREMENT,
  `street` varchar(100) NOT NULL,
  `house_number` varchar(10) NOT NULL,
  `city` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (1,'Abai Avenue','12A','Astana'),(2,'Dostyk Street','34B','Almaty'),(3,'Tauke Khan Street','56C','Shymkent'),(4,'Bukhar Zhyrau Boulevard','78D','Karaganda'),(5,'Satpayev Street','90E','Pavlodar'),(6,'Nazarbayev Avenue','15F','Astana'),(7,'Akmeshit Street','27G','Almaty'),(8,'Respublika Avenue','39H','Shymkent'),(9,'Auezov Street','41I','Karaganda'),(10,'Zhambyl Street','53J','Pavlodar'),(11,'Kunayev Street','65K','Astana'),(12,'Al-Farabi Avenue','77L','Almaty'),(13,'Mangilik El Avenue','89M','Astana'),(14,'Kabanbay Batyr Avenue','91N','Shymkent'),(15,'Seifullin Street','13O','Karaganda');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user`
--

DROP TABLE IF EXISTS `app_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `given_name` varchar(30) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `city` varchar(50) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `profile_description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user`
--

LOCK TABLES `app_user` WRITE;
/*!40000 ALTER TABLE `app_user` DISABLE KEYS */;
INSERT INTO `app_user` VALUES (1,'aigerim.akhmetova@example.com','Aigerim','Akhmetova','Astana','+77011234567','Caregiver: experienced, patient, and reliable'),(2,'daniyar.nursultanov@example.com','Daniyar','Nursultanov','Almaty','+77021234567','Caregiver: specializes in elderly care'),(3,'aliya.saparova@example.com','Aliya','Saparova','Shymkent','+77031234567','Caregiver: energetic and creative'),(4,'nursultan.abishev@example.com','Nursultan','Abishev','Karaganda','+77041234567','Caregiver: great with children'),(5,'zhanel.kairatova@example.com','Zhanel','Kairatova','Pavlodar','+77051234567','Caregiver: organized and punctual'),(6,'arman.armanov@example.com','Arman','Armanov','Astana','+77773414141','Caregiver: specializes in special needs care'),(7,'madina.tulegenova@example.com','Madina','Tulegenova','Almaty','+77071234567','Caregiver: friendly and responsible'),(8,'yerbolat.zhanibekov@example.com','Yerbolat','Zhanibekov','Shymkent','+77081234567','Caregiver: excellent communicator'),(9,'saule.amanova@example.com','Saule','Amanova','Karaganda','+77091234567','Caregiver: flexible and reliable'),(10,'maksat.nurlybekov@example.com','Maksat','Nurlybekov','Pavlodar','+77101234567','Caregiver: soft-spoken and caring'),(11,'olga.petrova@example.com','Olga','Petrova','Astana','+77111234567','Member: family member seeking care for elderly parent'),(12,'ivan.ivanov@example.com','Ivan','Ivanov','Almaty','+77121234567','Member: looking for a babysitter for two children'),(13,'elena.smirnova@example.com','Elena','Smirnova','Shymkent','+77131234567','Member: needs daily care for a disabled spouse'),(14,'sergey.pavlov@example.com','Sergey','Pavlov','Karaganda','+77141234567','Member: searching for weekend caregiver for grandmother'),(15,'daria.kozlova@example.com','Daria','Kozlova','Pavlodar','+77151234567','Member: requires after-school care for child'),(16,'dmitry.sokolov@example.com','Dmitry','Sokolov','Astana','+77161234567','Member: needs part-time help for elderly father'),(17,'anastasia.tikhonova@example.com','Anastasia','Tikhonova','Almaty','+77171234567','Member: seeking caregiver for post-surgery recovery'),(19,'maria.kuznetsova@example.com','Maria','Kuznetsova','Karaganda','+77191234567','Member: needs weekend babysitter'),(20,'amina.aminova@example.com','Amina','Aminova','Pavlodar','+77201234567','Member: searching for daily elderly care');
/*!40000 ALTER TABLE `app_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `caregiver_id` int NOT NULL,
  `member_id` int NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` time NOT NULL,
  `work_hours` decimal(4,2) NOT NULL,
  `status` enum('Pending','Accepted','Rejected') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`id`),
  KEY `caregiver_id` (`caregiver_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`caregiver_id`) REFERENCES `caregiver` (`id`) ON DELETE CASCADE,
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (1,1,1,'2024-07-01','10:00:00',4.00,'Pending'),(2,2,2,'2024-07-02','14:00:00',3.50,'Accepted'),(3,3,3,'2024-07-03','09:00:00',5.00,'Rejected'),(4,4,4,'2024-07-04','11:00:00',2.00,'Pending'),(5,5,5,'2024-07-05','15:00:00',4.50,'Accepted'),(6,6,6,'2024-07-06','13:00:00',3.00,'Rejected'),(7,7,7,'2024-07-07','10:30:00',4.00,'Pending'),(9,9,9,'2024-07-09','14:30:00',3.50,'Rejected'),(10,10,10,'2024-07-10','09:30:00',5.00,'Pending');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add address',8,'add_address'),(30,'Can change address',8,'change_address'),(31,'Can delete address',8,'delete_address'),(32,'Can view address',8,'view_address'),(33,'Can add appointment',9,'add_appointment'),(34,'Can change appointment',9,'change_appointment'),(35,'Can delete appointment',9,'delete_appointment'),(36,'Can view appointment',9,'view_appointment'),(37,'Can add job',10,'add_job'),(38,'Can change job',10,'change_job'),(39,'Can delete job',10,'delete_job'),(40,'Can view job',10,'view_job'),(41,'Can add caregiver',11,'add_caregiver'),(42,'Can change caregiver',11,'change_caregiver'),(43,'Can delete caregiver',11,'delete_caregiver'),(44,'Can view caregiver',11,'view_caregiver'),(45,'Can add job_ application',12,'add_job_application'),(46,'Can change job_ application',12,'change_job_application'),(47,'Can delete job_ application',12,'delete_job_application'),(48,'Can view job_ application',12,'view_job_application'),(49,'Can add member',13,'add_member'),(50,'Can change member',13,'change_member'),(51,'Can delete member',13,'delete_member'),(52,'Can view member',13,'view_member');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$NeNSs3ZUHGpOmNVZXrIaTw$sy8u3Ysr7nOjJE1woY+deg+rIqUeljeTgzW6qxQ/OBE=','2025-11-24 17:14:49.764998',1,'assel','','','assel@gmail.com',1,1,'2025-11-24 17:13:48.972124');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `care_type`
--

DROP TABLE IF EXISTS `care_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `care_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_name` varchar(50) NOT NULL,
  `type_description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_name` (`type_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `care_type`
--

LOCK TABLES `care_type` WRITE;
/*!40000 ALTER TABLE `care_type` DISABLE KEYS */;
INSERT INTO `care_type` VALUES (1,'Nurse','Provides medical care and assistance.'),(2,'Elderly Care','Offers companionship and support to elderly individuals.'),(3,'Babysitter','Cares for children.');
/*!40000 ALTER TABLE `care_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caregiver`
--

DROP TABLE IF EXISTS `caregiver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caregiver` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `hourly_rate` decimal(6,2) NOT NULL,
  `care_type_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `care_type_id` (`care_type_id`),
  CONSTRAINT `caregiver_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `caregiver_ibfk_2` FOREIGN KEY (`care_type_id`) REFERENCES `care_type` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caregiver`
--

LOCK TABLES `caregiver` WRITE;
/*!40000 ALTER TABLE `caregiver` DISABLE KEYS */;
INSERT INTO `caregiver` VALUES (1,1,'Female',19.80,1),(2,2,'Male',22.00,2),(3,3,'Female',19.25,3),(4,4,'Male',20.90,1),(5,5,'Female',23.10,2),(6,6,'Male',18.15,3),(7,7,'Female',24.20,1),(8,8,'Male',20.35,2),(9,9,'Female',22.55,3),(10,10,'Male',21.45,1);
/*!40000 ALTER TABLE `caregiver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(8,'caregiver','address'),(9,'caregiver','appointment'),(11,'caregiver','caregiver'),(10,'caregiver','job'),(12,'caregiver','job_application'),(13,'caregiver','member'),(7,'caregiver','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-11-24 17:13:03.116502'),(2,'auth','0001_initial','2025-11-24 17:13:03.292477'),(3,'admin','0001_initial','2025-11-24 17:13:03.323492'),(4,'admin','0002_logentry_remove_auto_add','2025-11-24 17:13:03.330571'),(5,'admin','0003_logentry_add_action_flag_choices','2025-11-24 17:13:03.335906'),(6,'contenttypes','0002_remove_content_type_name','2025-11-24 17:13:03.365483'),(7,'auth','0002_alter_permission_name_max_length','2025-11-24 17:13:03.378875'),(8,'auth','0003_alter_user_email_max_length','2025-11-24 17:13:03.384485'),(9,'auth','0004_alter_user_username_opts','2025-11-24 17:13:03.387168'),(10,'auth','0005_alter_user_last_login_null','2025-11-24 17:13:03.398697'),(11,'auth','0006_require_contenttypes_0002','2025-11-24 17:13:03.399398'),(12,'auth','0007_alter_validators_add_error_messages','2025-11-24 17:13:03.402177'),(13,'auth','0008_alter_user_username_max_length','2025-11-24 17:13:03.414208'),(14,'auth','0009_alter_user_last_name_max_length','2025-11-24 17:13:03.427831'),(15,'auth','0010_alter_group_name_max_length','2025-11-24 17:13:03.433852'),(16,'auth','0011_update_proxy_permissions','2025-11-24 17:13:03.436496'),(17,'auth','0012_alter_user_first_name_max_length','2025-11-24 17:13:03.448367'),(18,'sessions','0001_initial','2025-11-24 17:13:03.455582'),(19,'caregiver','0001_initial','2025-11-24 17:17:58.165737');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ys8a83dcf39ias0smw35m1viz4zgvpwx','.eJxVjDsOwjAQBe_iGlmO418o6TmDtfbu4gCypTipEHeHSCmgfTPzXiLCtpa4dVrijOIsBnH63RLkB9Ud4B3qrcnc6rrMSe6KPGiX14b0vBzu30GBXr41j8kZbS1rhYjKjSZxYEDDAKMzlpSiSUMgnVUA6wbyPnvOxjo9KfTi_QHwtjgA:1vNa9J:loPuKCmtzYScjM4U9avJIC2UgDWgIFV-9RVwDJRS3Z4','2025-12-08 17:14:49.766641');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_ad`
--

DROP TABLE IF EXISTS `job_ad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_ad` (
  `id` int NOT NULL AUTO_INCREMENT,
  `member_id` int NOT NULL,
  `required_caregiver_type_id` int DEFAULT NULL,
  `other_requirements` text,
  `date_posted` date NOT NULL DEFAULT (curdate()),
  `status` enum('Open','Closed') NOT NULL DEFAULT 'Open',
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  KEY `required_caregiver_type_id` (`required_caregiver_type_id`),
  CONSTRAINT `job_ad_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`) ON DELETE CASCADE,
  CONSTRAINT `job_ad_ibfk_2` FOREIGN KEY (`required_caregiver_type_id`) REFERENCES `care_type` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_ad`
--

LOCK TABLES `job_ad` WRITE;
/*!40000 ALTER TABLE `job_ad` DISABLE KEYS */;
INSERT INTO `job_ad` VALUES (1,1,1,'Experience with dementia patients','2025-11-25','Open'),(2,2,3,'CPR certified','2025-11-25','Open'),(3,3,2,'Able to assist with mobility','2025-11-25','Open'),(4,4,1,'Weekend availability','2025-11-25','Closed'),(5,5,3,'Creative and engaging','2025-11-25','Open'),(6,6,2,'Experience with elderly care, soft-spoken','2025-11-25','Open'),(7,7,1,'Post-surgery care experience','2025-11-25','Open'),(9,9,3,'Reliable and punctual','2025-11-25','Open');
/*!40000 ALTER TABLE `job_ad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_application`
--

DROP TABLE IF EXISTS `job_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_application` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_id` int NOT NULL,
  `caregiver_id` int NOT NULL,
  `date_applied` date NOT NULL DEFAULT (curdate()),
  `status` enum('Pending','Accepted','Rejected') NOT NULL DEFAULT 'Pending',
  PRIMARY KEY (`id`),
  KEY `job_id` (`job_id`),
  KEY `caregiver_id` (`caregiver_id`),
  CONSTRAINT `job_application_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `job_ad` (`id`) ON DELETE CASCADE,
  CONSTRAINT `job_application_ibfk_2` FOREIGN KEY (`caregiver_id`) REFERENCES `caregiver` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_application`
--

LOCK TABLES `job_application` WRITE;
/*!40000 ALTER TABLE `job_application` DISABLE KEYS */;
INSERT INTO `job_application` VALUES (1,1,1,'2025-11-25','Pending'),(2,1,3,'2025-11-25','Accepted'),(3,1,7,'2025-11-25','Rejected'),(4,2,2,'2025-11-25','Pending'),(5,2,5,'2025-11-25','Pending'),(6,3,1,'2025-11-25','Pending'),(7,3,4,'2025-11-25','Accepted'),(8,3,8,'2025-11-25','Rejected'),(9,3,10,'2025-11-25','Pending'),(10,4,4,'2025-11-25','Accepted'),(11,4,6,'2025-11-25','Pending'),(12,5,5,'2025-11-25','Rejected'),(13,5,9,'2025-11-25','Pending'),(14,5,2,'2025-11-25','Accepted'),(15,6,6,'2025-11-25','Pending'),(16,7,6,'2025-11-25','Pending'),(17,7,3,'2025-11-25','Accepted'),(18,7,7,'2025-11-25','Rejected'),(21,9,9,'2025-11-25','Rejected'),(22,9,2,'2025-11-25','Pending');
/*!40000 ALTER TABLE `job_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `job_applications_view`
--

DROP TABLE IF EXISTS `job_applications_view`;
/*!50001 DROP VIEW IF EXISTS `job_applications_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `job_applications_view` AS SELECT 
 1 AS `application_id`,
 1 AS `job_id`,
 1 AS `application_status`,
 1 AS `date_applied`,
 1 AS `caregiver_id`,
 1 AS `applicant_given_name`,
 1 AS `applicant_surname`,
 1 AS `applicant_email`,
 1 AS `applicant_phone`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `house_rules` text,
  `dependent_description` text,
  `dependent_age` int NOT NULL,
  `address_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `address_id` (`address_id`),
  CONSTRAINT `member_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `member_ibfk_2` FOREIGN KEY (`address_id`) REFERENCES `address` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,11,'No smoking, No pets','Elderly parent with mild dementia',87,1),(2,12,'No loud music','Two children aged 5 and 8',5,2),(3,13,'No outside visitors, No pets','Disabled spouse requiring daily assistance',44,3),(4,14,'Respectful behavior','Grandmother needing weekend care',78,4),(5,15,'Timely pickups','After-school care for child',10,5),(6,16,'No smoking, No pets','Elderly father with mobility issues',67,6),(7,17,'Gentle care','Post-surgery recovery assistance',22,9),(9,19,'Punctuality','Weekend babysitting for two kids',7,4),(10,20,'Compassionate care','Daily elderly care for father',77,9);
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sender_id` int NOT NULL,
  `receiver_id` int NOT NULL,
  `content` text NOT NULL,
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('Sent','Delivered','Read') NOT NULL DEFAULT 'Sent',
  PRIMARY KEY (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `receiver_id` (`receiver_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `app_user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`receiver_id`) REFERENCES `app_user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,11,'Hello, I am interested in the caregiver position.','2025-11-25 19:45:01','Sent'),(2,11,1,'Thank you for your interest. We will review your application.','2025-11-25 19:45:01','Delivered'),(3,2,12,'Can you provide more details about your experience?','2025-11-25 19:45:01','Sent'),(4,12,2,'Sure, I have 5 years of experience in childcare.','2025-11-25 19:45:01','Delivered'),(5,3,13,'When are you available to start?','2025-11-25 19:45:01','Sent');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `job_applications_view`
--

/*!50001 DROP VIEW IF EXISTS `job_applications_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `job_applications_view` AS select `ja`.`id` AS `application_id`,`ja`.`job_id` AS `job_id`,`ja`.`status` AS `application_status`,`ja`.`date_applied` AS `date_applied`,`c`.`id` AS `caregiver_id`,`u`.`given_name` AS `applicant_given_name`,`u`.`surname` AS `applicant_surname`,`u`.`email` AS `applicant_email`,`u`.`phone_number` AS `applicant_phone` from ((`job_application` `ja` join `caregiver` `c` on((`ja`.`caregiver_id` = `c`.`id`))) join `app_user` `u` on((`c`.`user_id` = `u`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-25 19:46:31
