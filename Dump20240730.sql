-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: mt_josim_db
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_customuser`
--

DROP TABLE IF EXISTS `accounts_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(100) NOT NULL,
  `role` varchar(10) NOT NULL,
  `mobile` varchar(30) DEFAULT NULL,
  `training_id` varchar(30) DEFAULT NULL,
  `date` date NOT NULL,
  `sign_image` varchar(100) DEFAULT NULL,
  `designation_id` bigint DEFAULT NULL,
  `office_id` bigint DEFAULT NULL,
  `updated_by` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `mobile` (`mobile`),
  UNIQUE KEY `training_id` (`training_id`),
  KEY `accounts_customuser_designation_id_176dd9cd_fk_accounts_` (`designation_id`),
  KEY `accounts_customuser_office_id_f5f1b1b5_fk_accounts_office_id` (`office_id`),
  CONSTRAINT `accounts_customuser_designation_id_176dd9cd_fk_accounts_` FOREIGN KEY (`designation_id`) REFERENCES `accounts_designation` (`id`),
  CONSTRAINT `accounts_customuser_office_id_f5f1b1b5_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser`
--

LOCK TABLES `accounts_customuser` WRITE;
/*!40000 ALTER TABLE `accounts_customuser` DISABLE KEYS */;
INSERT INTO `accounts_customuser` VALUES (1,'pbkdf2_sha256$720000$MROxIdlpmEYFBCTvHlSJxW$uGIb4T07v8CBorFKKg7lpX+6KoOja3qPKH9JnZl8jNA=','2024-08-15 07:43:25.596103',1,'Josim','Uddin','josimmsc@gmail.com',1,1,'2024-07-30 11:12:09.000000','Josim','admin','01736327270','1','2024-07-30','',1,1,NULL),(2,'pbkdf2_sha256$720000$aPyp3ErLG2e6cVYqSMhRnj$DoNFoCdRX8QuxlJ/1qOepqi56ACsJhwpxwR9h9UDtaE=','2024-08-15 07:55:32.246415',0,'Josim','Uddin','josimmsc@gmail.com',0,1,'2024-07-30 11:18:13.000000','524660','MT','017363272','524660','2024-07-30','',2,1,NULL),(3,'pbkdf2_sha256$720000$1wm9ub1S2Vs7VhfylwNvMV$YA9CTUtqAg6aoeu3/JfZ98lQrRrG6fymbEMaxOUhlDw=',NULL,0,'Habibur','Rahman','abc@gmail.com',0,1,'2024-08-15 07:21:00.000000','Habibur','AGM','0176940',NULL,'2024-08-15','',3,1,'1');
/*!40000 ALTER TABLE `accounts_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_groups`
--

DROP TABLE IF EXISTS `accounts_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq` (`customuser_id`,`group_id`),
  KEY `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_customuser__customuser_id_bc55088e_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_groups`
--

LOCK TABLES `accounts_customuser_groups` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_customuser_user_permissions`
--

DROP TABLE IF EXISTS `accounts_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_customuser_user_customuser_id_permission_9632a709_uniq` (`customuser_id`,`permission_id`),
  KEY `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_customuser__customuser_id_0deaefae_fk_accounts_` FOREIGN KEY (`customuser_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_customuser__permission_id_aea3d0e5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_customuser_user_permissions`
--

LOCK TABLES `accounts_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_designation`
--

DROP TABLE IF EXISTS `accounts_designation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_designation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_designation`
--

LOCK TABLES `accounts_designation` WRITE;
/*!40000 ALTER TABLE `accounts_designation` DISABLE KEYS */;
INSERT INTO `accounts_designation` VALUES (1,'Admin (IT)','Admin (IT) Meter Tester Josim'),(2,'Meter Tester','Meter Tester (MT)'),(3,'AGM(O&M)','AGM(O&M)');
/*!40000 ALTER TABLE `accounts_designation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_office`
--

DROP TABLE IF EXISTS `accounts_office`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_office` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `office_name` varchar(255) DEFAULT NULL,
  `office_code` varchar(10) DEFAULT NULL,
  `catagory` varchar(150) DEFAULT NULL,
  `pbs_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_office_pbs_id_b2c2da6d_fk_accounts_pbs_id` (`pbs_id`),
  CONSTRAINT `accounts_office_pbs_id_b2c2da6d_fk_accounts_pbs_id` FOREIGN KEY (`pbs_id`) REFERENCES `accounts_pbs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_office`
--

LOCK TABLES `accounts_office` WRITE;
/*!40000 ALTER TABLE `accounts_office` DISABLE KEYS */;
INSERT INTO `accounts_office` VALUES (1,'Nandina Zonal Office','09','zonal',1);
/*!40000 ALTER TABLE `accounts_office` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_officeemp`
--

DROP TABLE IF EXISTS `accounts_officeemp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_officeemp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `received_by` varchar(100) DEFAULT NULL,
  `checked_by_id` bigint DEFAULT NULL,
  `counter_sign_by_id` bigint DEFAULT NULL,
  `office_id` bigint NOT NULL,
  `tested_by_id` bigint DEFAULT NULL,
  `standered_meter_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `office_id` (`office_id`),
  KEY `accounts_officeemp_checked_by_id_06c0e719_fk_accounts_` (`checked_by_id`),
  KEY `accounts_officeemp_counter_sign_by_id_095e9685_fk_accounts_` (`counter_sign_by_id`),
  KEY `accounts_officeemp_tested_by_id_ad8d8c29_fk_accounts_` (`tested_by_id`),
  KEY `accounts_officeemp_standered_meter_id_650e30ca_fk_accounts_` (`standered_meter_id`),
  CONSTRAINT `accounts_officeemp_checked_by_id_06c0e719_fk_accounts_` FOREIGN KEY (`checked_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_officeemp_counter_sign_by_id_095e9685_fk_accounts_` FOREIGN KEY (`counter_sign_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `accounts_officeemp_office_id_a5da9b21_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`),
  CONSTRAINT `accounts_officeemp_standered_meter_id_650e30ca_fk_accounts_` FOREIGN KEY (`standered_meter_id`) REFERENCES `accounts_standard_meter` (`id`),
  CONSTRAINT `accounts_officeemp_tested_by_id_ad8d8c29_fk_accounts_` FOREIGN KEY (`tested_by_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_officeemp`
--

LOCK TABLES `accounts_officeemp` WRITE;
/*!40000 ALTER TABLE `accounts_officeemp` DISABLE KEYS */;
INSERT INTO `accounts_officeemp` VALUES (1,NULL,2,3,1,2,1);
/*!40000 ALTER TABLE `accounts_officeemp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_pbs`
--

DROP TABLE IF EXISTS `accounts_pbs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_pbs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pbs_code` varchar(10) DEFAULT NULL,
  `pbs_name` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_pbs`
--

LOCK TABLES `accounts_pbs` WRITE;
/*!40000 ALTER TABLE `accounts_pbs` DISABLE KEYS */;
INSERT INTO `accounts_pbs` VALUES (1,'23','Jamalpur Palli Bidyut Samity');
/*!40000 ALTER TABLE `accounts_pbs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_standard_meter`
--

DROP TABLE IF EXISTS `accounts_standard_meter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_standard_meter` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `std_serial` varchar(20) DEFAULT NULL,
  `std_name` varchar(20) DEFAULT NULL,
  `std_kh` varchar(5) DEFAULT NULL,
  `from_date` date NOT NULL,
  `pbs_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_standard_meter_pbs_id_f8158733_fk_accounts_pbs_id` (`pbs_id`),
  CONSTRAINT `accounts_standard_meter_pbs_id_f8158733_fk_accounts_pbs_id` FOREIGN KEY (`pbs_id`) REFERENCES `accounts_pbs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_standard_meter`
--

LOCK TABLES `accounts_standard_meter` WRITE;
/*!40000 ALTER TABLE `accounts_standard_meter` DISABLE KEYS */;
INSERT INTO `accounts_standard_meter` VALUES (1,'2604483','SANGAMO','21.6','2024-08-15',1);
/*!40000 ALTER TABLE `accounts_standard_meter` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add uploads',6,'add_uploads'),(22,'Can change uploads',6,'change_uploads'),(23,'Can delete uploads',6,'delete_uploads'),(24,'Can view uploads',6,'view_uploads'),(25,'Can add manufacturer',7,'add_manufacturer'),(26,'Can change manufacturer',7,'change_manufacturer'),(27,'Can delete manufacturer',7,'delete_manufacturer'),(28,'Can view manufacturer',7,'view_manufacturer'),(29,'Can add results',8,'add_results'),(30,'Can change results',8,'change_results'),(31,'Can delete results',8,'delete_results'),(32,'Can view results',8,'view_results'),(33,'Can add test_ data',9,'add_test_data'),(34,'Can change test_ data',9,'change_test_data'),(35,'Can delete test_ data',9,'delete_test_data'),(36,'Can view test_ data',9,'view_test_data'),(37,'Can add item',10,'add_item'),(38,'Can change item',10,'change_item'),(39,'Can delete item',10,'delete_item'),(40,'Can view item',10,'view_item'),(41,'Can add balance',11,'add_balance'),(42,'Can change balance',11,'change_balance'),(43,'Can delete balance',11,'delete_balance'),(44,'Can view balance',11,'view_balance'),(45,'Can add seal balance',12,'add_sealbalance'),(46,'Can change seal balance',12,'change_sealbalance'),(47,'Can delete seal balance',12,'delete_sealbalance'),(48,'Can view seal balance',12,'view_sealbalance'),(49,'Can add designation',13,'add_designation'),(50,'Can change designation',13,'change_designation'),(51,'Can delete designation',13,'delete_designation'),(52,'Can view designation',13,'view_designation'),(53,'Can add office',14,'add_office'),(54,'Can change office',14,'change_office'),(55,'Can delete office',14,'delete_office'),(56,'Can view office',14,'view_office'),(57,'Can add pbs',15,'add_pbs'),(58,'Can change pbs',15,'change_pbs'),(59,'Can delete pbs',15,'delete_pbs'),(60,'Can view pbs',15,'view_pbs'),(61,'Can add user',16,'add_customuser'),(62,'Can change user',16,'change_customuser'),(63,'Can delete user',16,'delete_customuser'),(64,'Can view user',16,'view_customuser'),(65,'Can add standard_ meter',17,'add_standard_meter'),(66,'Can change standard_ meter',17,'change_standard_meter'),(67,'Can delete standard_ meter',17,'delete_standard_meter'),(68,'Can view standard_ meter',17,'view_standard_meter'),(69,'Can add office emp',18,'add_officeemp'),(70,'Can change office emp',18,'change_officeemp'),(71,'Can delete office emp',18,'delete_officeemp'),(72,'Can view office emp',18,'view_officeemp'),(73,'Can add purchase order',19,'add_purchaseorder'),(74,'Can change purchase order',19,'change_purchaseorder'),(75,'Can delete purchase order',19,'delete_purchaseorder'),(76,'Can view purchase order',19,'view_purchaseorder'),(77,'Can add issue item',20,'add_issueitem'),(78,'Can change issue item',20,'change_issueitem'),(79,'Can delete issue item',20,'delete_issueitem'),(80,'Can view issue item',20,'view_issueitem'),(81,'Can add seal issue',21,'add_sealissue'),(82,'Can change seal issue',21,'change_sealissue'),(83,'Can delete seal issue',21,'delete_sealissue'),(84,'Can view seal issue',21,'view_sealissue');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `balance_reg_balance`
--

DROP TABLE IF EXISTS `balance_reg_balance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `balance_reg_balance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sl_start` varchar(10) DEFAULT NULL,
  `sl_end` varchar(10) DEFAULT NULL,
  `store_return_ticket` varchar(50) DEFAULT NULL,
  `date_start` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `ticket_no` varchar(50) DEFAULT NULL,
  `referance_name` varchar(50) DEFAULT NULL,
  `debit_qty` int NOT NULL,
  `credit_qty` int NOT NULL,
  `balance` int NOT NULL,
  `created_date` date DEFAULT NULL,
  `updated_date` date DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `office_id` bigint NOT NULL,
  `updated_by_id` bigint DEFAULT NULL,
  `item_id` bigint NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `balance_reg_balance_created_by_id_26e5b4b4_fk_accounts_` (`created_by_id`),
  KEY `balance_reg_balance_office_id_ff2e7bd1_fk_accounts_office_id` (`office_id`),
  KEY `balance_reg_balance_updated_by_id_50bf9c71_fk_accounts_` (`updated_by_id`),
  KEY `balance_reg_balance_item_id_4548da7e_fk_balance_reg_item_id` (`item_id`),
  CONSTRAINT `balance_reg_balance_created_by_id_26e5b4b4_fk_accounts_` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `balance_reg_balance_item_id_4548da7e_fk_balance_reg_item_id` FOREIGN KEY (`item_id`) REFERENCES `balance_reg_item` (`id`),
  CONSTRAINT `balance_reg_balance_office_id_ff2e7bd1_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`),
  CONSTRAINT `balance_reg_balance_updated_by_id_50bf9c71_fk_accounts_` FOREIGN KEY (`updated_by_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balance_reg_balance`
--

LOCK TABLES `balance_reg_balance` WRITE;
/*!40000 ALTER TABLE `balance_reg_balance` DISABLE KEYS */;
/*!40000 ALTER TABLE `balance_reg_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `balance_reg_item`
--

DROP TABLE IF EXISTS `balance_reg_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `balance_reg_item` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_no` varchar(100) NOT NULL,
  `details` varchar(255) NOT NULL,
  `order` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_no` (`item_no`),
  CONSTRAINT `balance_reg_item_chk_1` CHECK ((`order` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balance_reg_item`
--

LOCK TABLES `balance_reg_item` WRITE;
/*!40000 ALTER TABLE `balance_reg_item` DISABLE KEYS */;
INSERT INTO `balance_reg_item` VALUES (1,'J-39','Single Phrase Electronics Meter',0),(2,'J-3','200 Class 3Phrase Meter',1),(3,'J-4','20 Class 3Phrase Meter',2),(4,'J-1','Single Electrical Meter',3),(5,'J-2','Three Phrase Non Demand Meter',0);
/*!40000 ALTER TABLE `balance_reg_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `balance_reg_sealbalance`
--

DROP TABLE IF EXISTS `balance_reg_sealbalance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `balance_reg_sealbalance` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item` varchar(10) DEFAULT NULL,
  `sl_start` varchar(10) DEFAULT NULL,
  `sl_end` varchar(10) DEFAULT NULL,
  `store_return_ticket` varchar(50) DEFAULT NULL,
  `date_start` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `ticket_no` varchar(50) DEFAULT NULL,
  `referance_name` varchar(50) DEFAULT NULL,
  `debit_qty` int NOT NULL,
  `credit_qty` int NOT NULL,
  `balance` int NOT NULL,
  `created_date` date DEFAULT NULL,
  `updated_date` date DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `office_id` bigint NOT NULL,
  `updated_by_id` bigint DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `balance_reg_sealbala_created_by_id_9a779632_fk_accounts_` (`created_by_id`),
  KEY `balance_reg_sealbalance_office_id_c48d48b8_fk_accounts_office_id` (`office_id`),
  KEY `balance_reg_sealbala_updated_by_id_592a7808_fk_accounts_` (`updated_by_id`),
  CONSTRAINT `balance_reg_sealbala_created_by_id_9a779632_fk_accounts_` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `balance_reg_sealbala_updated_by_id_592a7808_fk_accounts_` FOREIGN KEY (`updated_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `balance_reg_sealbalance_office_id_c48d48b8_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balance_reg_sealbalance`
--

LOCK TABLES `balance_reg_sealbalance` WRITE;
/*!40000 ALTER TABLE `balance_reg_sealbalance` DISABLE KEYS */;
/*!40000 ALTER TABLE `balance_reg_sealbalance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `damage_meter_purchaseorder`
--

DROP TABLE IF EXISTS `damage_meter_purchaseorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `damage_meter_purchaseorder` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `purchase_order` varchar(100) NOT NULL,
  `remark` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `damage_meter_purchaseorder`
--

LOCK TABLES `damage_meter_purchaseorder` WRITE;
/*!40000 ALTER TABLE `damage_meter_purchaseorder` DISABLE KEYS */;
INSERT INTO `damage_meter_purchaseorder` VALUES (1,'-',NULL);
/*!40000 ALTER TABLE `damage_meter_purchaseorder` ENABLE KEYS */;
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
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-07-30 11:13:21.701704','1','Josim',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Role\"]}}]',16,1),(2,'2024-07-30 11:15:08.359118','1','23 Jamalpur Palli Bidyut Samity',1,'[{\"added\": {}}]',15,1),(3,'2024-07-30 11:15:35.883479','1','09 Nandina Zonal Office 23 Jamalpur Palli Bidyut Samity',1,'[{\"added\": {}}]',14,1),(4,'2024-07-30 11:16:13.880434','1','Meter Tester',1,'[{\"added\": {}}]',13,1),(5,'2024-07-30 11:16:26.358005','1','Josim',2,'[{\"changed\": {\"fields\": [\"Office\", \"Designation\"]}}]',16,1),(6,'2024-07-30 11:17:14.092396','1','Admin (IT)',2,'[{\"changed\": {\"fields\": [\"Title\", \"Details\"]}}]',13,1),(7,'2024-07-30 11:17:16.115857','1','Josim',2,'[]',16,1),(8,'2024-07-30 11:21:31.444174','2','Meter Tester',1,'[{\"added\": {}}]',13,1),(9,'2024-07-30 11:21:33.515857','2','524660',2,'[{\"changed\": {\"fields\": [\"Designation\"]}}]',16,1),(10,'2024-07-30 11:21:42.247763','2','524660',2,'[]',16,1),(11,'2024-07-30 11:25:12.721522','1','J-39',1,'[{\"added\": {}}]',10,1),(12,'2024-07-30 11:25:44.213982','2','J-3',1,'[{\"added\": {}}]',10,1),(13,'2024-07-30 11:26:05.749671','3','J-4',1,'[{\"added\": {}}]',10,1),(14,'2024-07-30 11:26:31.728901','4','J-1',1,'[{\"added\": {}}]',10,1),(15,'2024-07-30 11:26:49.531237','1','J-39',2,'[{\"changed\": {\"fields\": [\"Details\"]}}]',10,1),(16,'2024-07-30 11:37:47.723915','1','Techno-D',1,'[{\"added\": {}}]',7,1),(17,'2024-07-30 11:38:59.809427','2','B&T',1,'[{\"added\": {}}]',7,1),(18,'2024-07-30 11:39:44.944138','3','Pasha',1,'[{\"added\": {}}]',7,1),(19,'2024-07-30 11:41:06.585551','4','Holley',1,'[{\"added\": {}}]',7,1),(20,'2024-07-30 11:41:43.460339','5','Hexcell',1,'[{\"added\": {}}]',7,1),(21,'2024-07-30 11:42:03.165005','6','Hexing',1,'[{\"added\": {}}]',7,1),(22,'2024-07-30 11:42:47.426010','7','Meter D.Tech',1,'[{\"added\": {}}]',7,1),(23,'2024-07-30 11:43:14.519152','8','Power Plus',1,'[{\"added\": {}}]',7,1),(24,'2024-07-30 11:44:49.166719','9','Techno-A',1,'[{\"added\": {}}]',7,1),(25,'2024-07-30 11:45:33.075722','10','Hosaf-A',1,'[{\"added\": {}}]',7,1),(26,'2024-07-30 11:46:08.182940','11','Hosaf-D',1,'[{\"added\": {}}]',7,1),(27,'2024-07-30 11:51:19.694189','12','Hexing-3ϕ',1,'[{\"added\": {}}]',7,1),(28,'2024-07-30 11:52:41.570164','1','OK',1,'[{\"added\": {}}]',8,1),(29,'2024-07-30 11:54:39.331839','2','IMD',1,'[{\"added\": {}}]',8,1),(30,'2024-07-30 11:56:18.248706','3','3ϕ OK',1,'[{\"added\": {}}]',8,1),(31,'2024-07-30 13:44:07.666702','1','2024-05-16',3,'',12,1),(32,'2024-07-30 13:44:18.893941','3','2024-05-16',3,'',11,1),(33,'2024-07-30 13:44:19.050616','2','2024-05-16',3,'',11,1),(34,'2024-07-30 13:44:19.113055','1','2024-05-15',3,'',11,1),(35,'2024-07-30 13:51:34.991098','5','2024-05-16',3,'',11,1),(36,'2024-07-30 13:51:35.226954','4','2024-05-15',3,'',11,1),(37,'2024-07-30 13:51:41.803215','3','2024-05-16',3,'',12,1),(38,'2024-07-30 13:51:41.991592','2','2024-05-15',3,'',12,1),(39,'2024-08-15 06:05:17.352338','13','General',1,'[{\"added\": {}}]',7,1),(40,'2024-08-15 06:05:58.753281','14','Smart',1,'[{\"added\": {}}]',7,1),(41,'2024-08-15 06:06:35.079611','15','Fuji',1,'[{\"added\": {}}]',7,1),(42,'2024-08-15 06:07:14.880740','16','TVA',1,'[{\"added\": {}}]',7,1),(43,'2024-08-15 06:08:08.271298','17','Gaus',1,'[{\"added\": {}}]',7,1),(44,'2024-08-15 06:09:17.159869','18','Hay-A',1,'[{\"added\": {}}]',7,1),(45,'2024-08-15 06:09:51.999783','19','Hay-D',1,'[{\"added\": {}}]',7,1),(46,'2024-08-15 06:13:47.719253','20','Schlumberger',1,'[{\"added\": {}}]',7,1),(47,'2024-08-15 06:14:21.511734','21','Zhejeang',1,'[{\"added\": {}}]',7,1),(48,'2024-08-15 06:15:11.624337','22','HuaYi',1,'[{\"added\": {}}]',7,1),(49,'2024-08-15 06:17:20.509769','1','OK',2,'[]',8,1),(50,'2024-08-15 06:17:22.511472','1','OK',2,'[]',8,1),(51,'2024-08-15 06:17:50.895112','4','IMD',1,'[{\"added\": {}}]',8,1),(52,'2024-08-15 06:18:10.512562','5','ICD',1,'[{\"added\": {}}]',8,1),(53,'2024-08-15 06:18:29.095618','6','Rust',1,'[{\"added\": {}}]',8,1),(54,'2024-08-15 06:18:48.918383','7','IBD',1,'[{\"added\": {}}]',8,1),(55,'2024-08-15 06:19:10.422886','8','LCD',1,'[{\"added\": {}}]',8,1),(56,'2024-08-15 06:19:33.823233','9','WSP',1,'[{\"added\": {}}]',8,1),(57,'2024-08-15 06:20:38.562473','10','Broken',1,'[{\"added\": {}}]',8,1),(58,'2024-08-15 06:20:53.781853','11','Burn',1,'[{\"added\": {}}]',8,1),(59,'2024-08-15 06:21:10.943549','12','Burn base',1,'[{\"added\": {}}]',8,1),(60,'2024-08-15 06:21:35.344447','13','NGD',1,'[{\"added\": {}}]',8,1),(61,'2024-08-15 06:21:57.103317','14','ICB',1,'[{\"added\": {}}]',8,1),(62,'2024-08-15 06:22:22.326923','15','LB',1,'[{\"added\": {}}]',8,1),(63,'2024-08-15 06:22:39.487334','16','SB',1,'[{\"added\": {}}]',8,1),(64,'2024-08-15 06:22:58.047234','17','Red',1,'[{\"added\": {}}]',8,1),(65,'2024-08-15 06:23:24.998884','18','Down',1,'[{\"added\": {}}]',8,1),(66,'2024-08-15 06:23:48.137077','19','Auto_imp',1,'[{\"added\": {}}]',8,1),(67,'2024-08-15 06:24:08.630746','20','BLink',1,'[{\"added\": {}}]',8,1),(68,'2024-08-15 06:26:12.010311','4','3ϕ Burn',2,'[{\"changed\": {\"fields\": [\"Name\", \"Details\"]}}]',8,1),(69,'2024-08-15 06:28:32.567923','23','Wasion(LIBRA)',1,'[{\"added\": {}}]',7,1),(70,'2024-08-15 06:31:25.581411','5','J-2',1,'[{\"added\": {}}]',10,1),(71,'2024-08-15 06:31:47.495377','24','ChungHsin',1,'[{\"added\": {}}]',7,1),(72,'2024-08-15 07:00:26.608113','1','2604483',1,'[{\"added\": {}}]',17,1),(73,'2024-08-15 07:01:29.966250','1','OfficeEmp object (1)',1,'[{\"added\": {}}]',18,1),(74,'2024-08-15 07:11:34.837026','2','524660',2,'[]',16,1),(75,'2024-08-15 07:22:14.278230','1','OfficeEmp object (1)',2,'[{\"changed\": {\"fields\": [\"Counter sign by\"]}}]',18,1),(76,'2024-08-15 07:26:41.819920','3','AGM(O&M)',1,'[{\"added\": {}}]',13,1),(77,'2024-08-15 07:26:55.573990','3','Habibur',2,'[{\"changed\": {\"fields\": [\"Designation\"]}}]',16,1),(78,'2024-08-15 08:35:23.732567','1','2604483',2,'[{\"changed\": {\"fields\": [\"Tested by\", \"Checked by\"]}}]',18,1),(79,'2024-08-15 09:03:32.024873','23','Wasion(LIBRA)',2,'[]',7,1),(80,'2024-08-15 09:04:48.477941','25','MT(Hangzhou)',1,'[{\"added\": {}}]',7,1),(81,'2024-08-15 10:30:12.653895','26','Echo',1,'[{\"added\": {}}]',7,1),(82,'2024-08-15 10:30:46.563109','26','Echo',2,'[{\"changed\": {\"fields\": [\"Standerd rev req ll\", \"Standerd rev req fl\"]}}]',7,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (16,'accounts','customuser'),(13,'accounts','designation'),(14,'accounts','office'),(18,'accounts','officeemp'),(15,'accounts','pbs'),(17,'accounts','standard_meter'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(11,'balance_reg','balance'),(10,'balance_reg','item'),(12,'balance_reg','sealbalance'),(4,'contenttypes','contenttype'),(19,'damage_meter','purchaseorder'),(20,'issue_item','issueitem'),(21,'issue_item','sealissue'),(5,'sessions','session'),(7,'test_data','manufacturer'),(8,'test_data','results'),(9,'test_data','test_data'),(6,'test_data','uploads');
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
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-07-30 10:59:07.572551'),(2,'contenttypes','0002_remove_content_type_name','2024-07-30 10:59:09.422211'),(3,'auth','0001_initial','2024-07-30 10:59:13.281659'),(4,'auth','0002_alter_permission_name_max_length','2024-07-30 10:59:14.066519'),(5,'auth','0003_alter_user_email_max_length','2024-07-30 10:59:14.128831'),(6,'auth','0004_alter_user_username_opts','2024-07-30 10:59:14.223411'),(7,'auth','0005_alter_user_last_login_null','2024-07-30 10:59:14.286206'),(8,'auth','0006_require_contenttypes_0002','2024-07-30 10:59:14.364812'),(9,'auth','0007_alter_validators_add_error_messages','2024-07-30 10:59:14.459049'),(10,'auth','0008_alter_user_username_max_length','2024-07-30 10:59:14.553259'),(11,'auth','0009_alter_user_last_name_max_length','2024-07-30 10:59:14.600259'),(12,'auth','0010_alter_group_name_max_length','2024-07-30 10:59:14.725582'),(13,'auth','0011_update_proxy_permissions','2024-07-30 10:59:14.849950'),(14,'auth','0012_alter_user_first_name_max_length','2024-07-30 10:59:15.117745'),(15,'accounts','0001_initial','2024-07-30 10:59:32.578266'),(16,'admin','0001_initial','2024-07-30 10:59:34.681080'),(17,'admin','0002_logentry_remove_auto_add','2024-07-30 10:59:34.728590'),(18,'admin','0003_logentry_add_action_flag_choices','2024-07-30 10:59:34.854151'),(19,'balance_reg','0001_initial','2024-07-30 10:59:43.765995'),(20,'damage_meter','0001_initial','2024-07-30 10:59:44.487146'),(21,'issue_item','0001_initial','2024-07-30 10:59:56.969510'),(22,'sessions','0001_initial','2024-07-30 10:59:58.016251'),(23,'test_data','0001_initial','2024-07-30 11:00:10.427536'),(24,'test_data','0002_manufacturer_order_results_order','2024-07-30 12:04:21.769958'),(25,'accounts','0002_alter_customuser_date_alter_standard_meter_from_date','2024-08-15 05:59:05.343166'),(26,'accounts','0003_alter_customuser_date_alter_standard_meter_from_date','2024-08-15 05:59:05.516548'),(27,'accounts','0004_customuser_sidebar_alter_customuser_date_and_more','2024-08-15 05:59:08.186449'),(28,'accounts','0005_remove_customuser_sidebar','2024-08-15 05:59:08.587440'),(29,'accounts','0006_customuser_updated_by_alter_customuser_date_and_more','2024-08-15 05:59:08.922873'),(30,'accounts','0007_alter_customuser_date_alter_standard_meter_from_date','2024-08-15 05:59:08.987910'),(31,'balance_reg','0002_balance_remark','2024-08-15 05:59:09.288391'),(32,'balance_reg','0003_sealbalance_remark','2024-08-15 05:59:09.661092'),(33,'balance_reg','0004_alter_balance_options_alter_sealbalance_options','2024-08-15 05:59:09.755579'),(34,'issue_item','0002_alter_issueitem_options_alter_sealissue_options','2024-08-15 05:59:09.849599'),(35,'test_data','0003_alter_manufacturer_options_alter_results_options','2024-08-15 05:59:09.928352');
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
INSERT INTO `django_session` VALUES ('3221656cu8bk6ggi8ihz2d9ygrjn2yuj','.eJxVjEEOwiAUBe_C2hCBAtWle89AHvyPVA0kpV0Z765NutDtm5n3EgHrUsLaeQ4TibPQ4vC7RaQH1w3QHfXWZGp1macoN0XutMtrI35edvfvoKCXb52UzrDE2SlFHkmx9bDZjZ70gBMbq72HOw4mW5t0NGNm5KSMMmAPiPcH-ZM4hg:1seVKW:-L_2q9FQ7fhqP2JZJjsgv04ccW9LNMQa1xLPHlkx4U4','2024-08-29 07:55:32.304290'),('a0rtvl7u8v8mmwzii270tveecwk66crl','.eJxVjDEOwjAMRe-SGUW1SaOYkZ0zVHbikAJKpaadKu4OlTrA-t97fzMDr0sZ1qbzMCZzMWBOv5twfGrdQXpwvU82TnWZR7G7Yg_a7G1K-roe7t9B4Va-NXIgchGjUvAoCYIPQtq76DFp12UHCYUxZ1LMwoQEEUEIIJx715v3B-SvN6o:1sYn8l:8NvITsc-3YDEKYyGZI722sR7yRyZBluOD5sIMOg_clQ','2024-08-13 13:43:47.650686'),('vpl7evqmh20qi2o723qbhm5fyvcgo5pc','.eJxVjDEOwjAMRe-SGUW1SaOYkZ0zVHbikAJKpaadKu4OlTrA-t97fzMDr0sZ1qbzMCZzMWBOv5twfGrdQXpwvU82TnWZR7G7Yg_a7G1K-roe7t9B4Va-NXIgchGjUvAoCYIPQtq76DFp12UHCYUxZ1LMwoQEEUEIIJx715v3B-SvN6o:1seV8n:O7sz5VixM05BLjVvAHPz6A6yTCNYi4UxdoFk1MqP_-4','2024-08-29 07:43:25.648284');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue_item_issueitem`
--

DROP TABLE IF EXISTS `issue_item_issueitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issue_item_issueitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `serial` varchar(20) DEFAULT NULL,
  `cmo` varchar(20) DEFAULT NULL,
  `received_by` varchar(100) DEFAULT NULL,
  `meter_no` varchar(100) DEFAULT NULL,
  `reading` varchar(50) DEFAULT NULL,
  `main_seal` varchar(50) DEFAULT NULL,
  `body_seal1` varchar(50) DEFAULT NULL,
  `body_seal2` varchar(50) DEFAULT NULL,
  `mfg` varchar(50) DEFAULT NULL,
  `total_j31` int NOT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `updated_date` datetime(6) DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `item_id` bigint NOT NULL,
  `office_id` bigint NOT NULL,
  `updated_by_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `issue_item_issueitem_created_by_id_bc53ef87_fk_accounts_` (`created_by_id`),
  KEY `issue_item_issueitem_item_id_8b024667_fk_balance_reg_item_id` (`item_id`),
  KEY `issue_item_issueitem_office_id_16970a70_fk_accounts_office_id` (`office_id`),
  KEY `issue_item_issueitem_updated_by_id_4b9ee0c4_fk_accounts_` (`updated_by_id`),
  CONSTRAINT `issue_item_issueitem_created_by_id_bc53ef87_fk_accounts_` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `issue_item_issueitem_item_id_8b024667_fk_balance_reg_item_id` FOREIGN KEY (`item_id`) REFERENCES `balance_reg_item` (`id`),
  CONSTRAINT `issue_item_issueitem_office_id_16970a70_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`),
  CONSTRAINT `issue_item_issueitem_updated_by_id_4b9ee0c4_fk_accounts_` FOREIGN KEY (`updated_by_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_item_issueitem`
--

LOCK TABLES `issue_item_issueitem` WRITE;
/*!40000 ALTER TABLE `issue_item_issueitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `issue_item_issueitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue_item_sealissue`
--

DROP TABLE IF EXISTS `issue_item_sealissue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issue_item_sealissue` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item` varchar(20) DEFAULT NULL,
  `cmo` varchar(20) DEFAULT NULL,
  `book` varchar(10) DEFAULT NULL,
  `account` varchar(10) DEFAULT NULL,
  `received_by` varchar(100) DEFAULT NULL,
  `main_seal` varchar(50) DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `updated_date` datetime(6) DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `office_id` bigint NOT NULL,
  `updated_by_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `issue_item_sealissue_created_by_id_f3b9c3f7_fk_accounts_` (`created_by_id`),
  KEY `issue_item_sealissue_office_id_74f98e6e_fk_accounts_office_id` (`office_id`),
  KEY `issue_item_sealissue_updated_by_id_6dc5b7a9_fk_accounts_` (`updated_by_id`),
  CONSTRAINT `issue_item_sealissue_created_by_id_f3b9c3f7_fk_accounts_` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `issue_item_sealissue_office_id_74f98e6e_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`),
  CONSTRAINT `issue_item_sealissue_updated_by_id_6dc5b7a9_fk_accounts_` FOREIGN KEY (`updated_by_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_item_sealissue`
--

LOCK TABLES `issue_item_sealissue` WRITE;
/*!40000 ALTER TABLE `issue_item_sealissue` DISABLE KEYS */;
/*!40000 ALTER TABLE `issue_item_sealissue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_data_manufacturer`
--

DROP TABLE IF EXISTS `test_data_manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_data_manufacturer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `kh` varchar(5) DEFAULT NULL,
  `meter_class` varchar(5) DEFAULT NULL,
  `meter_type` varchar(20) DEFAULT NULL,
  `LL_TA` varchar(5) NOT NULL,
  `FL_TA` varchar(5) NOT NULL,
  `LL_rev` varchar(5) NOT NULL,
  `FL_rev` varchar(5) NOT NULL,
  `standerd_rev_req_ll` varchar(10) DEFAULT NULL,
  `standerd_rev_req_fl` varchar(10) DEFAULT NULL,
  `item_no_id` bigint NOT NULL,
  `order` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `test_data_manufactur_item_no_id_0cb1a15b_fk_balance_r` (`item_no_id`),
  CONSTRAINT `test_data_manufactur_item_no_id_0cb1a15b_fk_balance_r` FOREIGN KEY (`item_no_id`) REFERENCES `balance_reg_item` (`id`),
  CONSTRAINT `test_data_manufacturer_chk_1` CHECK ((`order` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_data_manufacturer`
--

LOCK TABLES `test_data_manufacturer` WRITE;
/*!40000 ALTER TABLE `test_data_manufacturer` DISABLE KEYS */;
INSERT INTO `test_data_manufacturer` VALUES (1,'Techno-D','0.5','40',NULL,'1','10','2','10','4.63','23.15',1,0),(2,'B&T','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(3,'Pasha','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(4,'Holley','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(5,'Hexcell','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(6,'Hexing','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(7,'Meter D.Tech','0.5','40',NULL,'1','10','2','10','5.79','28.94',1,0),(8,'Power Plus','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(9,'Techno-A','2.222','40',NULL,'1','10','2','10','20.57','102.87',4,0),(10,'Hosaf-A','0.625','40',NULL,'1','10','2','10','20.57','102.87',4,0),(11,'Hosaf-D','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(12,'Hexing-3ϕ','10','200',NULL,'1','10','2','10','0','0',2,0),(13,'General','2.5','40',NULL,'1','10','2','10','23.15','115.7',4,0),(14,'Smart','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(15,'Fuji','2.5','40',NULL,'1','10','2','10','23.15','115.7',4,0),(16,'TVA','2.222','40',NULL,'1','10','2','10','20.57','102.87',4,0),(17,'Gaus','2.222','40',NULL,'1','10','2','10','20.57','102.87',4,0),(18,'Hay-A','2.222','40',NULL,'1','10','2','10','20.57','102.87',4,0),(19,'Hay-D','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0),(20,'Schlumberger','2.4','40',NULL,'1','10','2','10','22.22','111.11',4,0),(21,'Zhejeang','2.222','40',NULL,'1','10','2','10','20.57','102.87',4,0),(22,'HuaYi','2.222','40',NULL,'1','10','2','10','20.57','102.87',4,0),(23,'Wasion(LIBRA)','21.6','200','LIBRA','1','10','2','10','0','0',2,0),(24,'ChungHsin','21.6','200',NULL,'1','10','2','10','0','0',5,0),(25,'MT(Hangzhou)','10.0','200',NULL,'1','10','2','10','0','0',2,0),(26,'Echo','0.625','40',NULL,'1','10','2','10','5.79','28.94',1,0);
/*!40000 ALTER TABLE `test_data_manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_data_results`
--

DROP TABLE IF EXISTS `test_data_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_data_results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `remark` longtext,
  `office_id` bigint NOT NULL,
  `order` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `test_data_results_office_id_b241d18e_fk_accounts_office_id` (`office_id`),
  CONSTRAINT `test_data_results_office_id_b241d18e_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`),
  CONSTRAINT `test_data_results_chk_1` CHECK ((`order` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_data_results`
--

LOCK TABLES `test_data_results` WRITE;
/*!40000 ALTER TABLE `test_data_results` DISABLE KEYS */;
INSERT INTO `test_data_results` VALUES (1,'OK','মিটারটি ভলো আছে।','ব্যবহার উপযোগী।',1,0),(2,'IMD','আভ্যন্তরীণ কারণে মিটারটির যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।',1,0),(3,'3ϕ OK','বাহ্যিক দৃষ্টিতে ত্রুটি পরিলক্ষিত হয়নি।','পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।',1,0),(4,'3ϕ Burn','মিটারটি পুড়া।','ব্যবহার অনুপযোগী।',1,0),(5,'ICD','আভ্যন্তরীণ কারণে মিটারটির সার্কিট নষ্ট।','ব্যবহার অনুপযোগী।',1,0),(6,'Rust','দীর্ঘদিন ব্যবহার ও মরিচা জনিত কারণে যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।',1,0),(7,'IBD','আভ্যন্তরীণ কারণে ব্যাটারী ও যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।',1,0),(8,'LCD','আভ্যন্তরীণ কারণে মিটারটির LCD মনিটর নষ্ট।','ব্যবহার অনুপযোগী।',1,0),(9,'WSP','মিটারটির কাঠ স্ক্রু পয়েন্ট ভাঙ্গা ।','ব্যবহার অনুপযোগী।',1,0),(10,'Broken','মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।',1,0),(11,'Burn','মিটারটি পুড়া।','ব্যবহার অনুপযোগী।',1,0),(12,'Burn base','মিটারটির বেস পুড়া।','ব্যবহার অনুপযোগী।',1,0),(13,'NGD','প্রাকৃতিক কারণে গ্লাস কভার লাল ও যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।',1,0),(14,'ICB','আভ্যন্তরীণ কারণে সার্কিট পোড়া।','ব্যবহার অনুপযোগী।',1,0),(15,'LB','মিটারটির লোড সাইড পোড়া।','ব্যবহার অনুপযোগী।',1,0),(16,'SB','মিটারটির সোর্স সাইড পোড়া।','ব্যবহার অনুপযোগী।',1,0),(17,'Red','আভ্যন্তরিন কারণে মিটারটির গ্লাস কভার  লাল ও যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।',1,0),(18,'Down','যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।',1,0),(19,'Auto_imp','যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।',1,0),(20,'BLink','আভ্যন্তরীণ কারণে মিটারটির রিডিং অস্থির বা এলোমেলো দেখায়।','ব্যবহার অনুপযোগী।',1,0);
/*!40000 ALTER TABLE `test_data_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_data_test_data`
--

DROP TABLE IF EXISTS `test_data_test_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_data_test_data` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tested_meter_no` varchar(20) DEFAULT NULL,
  `reading_as_found` varchar(20) NOT NULL,
  `reading_as_left` varchar(20) NOT NULL,
  `multiplier` varchar(20) NOT NULL,
  `cmo` varchar(20) DEFAULT NULL,
  `book` varchar(3) DEFAULT NULL,
  `account` varchar(4) DEFAULT NULL,
  `manufacturer` varchar(30) DEFAULT NULL,
  `meter_class` varchar(5) DEFAULT NULL,
  `meter_item` varchar(100) DEFAULT NULL,
  `kh` varchar(5) DEFAULT NULL,
  `LL_TA` varchar(5) NOT NULL,
  `FL_TA` varchar(5) NOT NULL,
  `LL_rev` varchar(5) NOT NULL,
  `FL_rev` varchar(5) NOT NULL,
  `as_found_ll` varchar(10) DEFAULT NULL,
  `as_found_fl` varchar(10) DEFAULT NULL,
  `percent_found_ll` varchar(10) DEFAULT NULL,
  `percent_found_fl` varchar(10) DEFAULT NULL,
  `error_ll` varchar(10) DEFAULT NULL,
  `error_fl` varchar(10) DEFAULT NULL,
  `as_left_ll` varchar(10) DEFAULT NULL,
  `as_left_fl` varchar(10) DEFAULT NULL,
  `percent_left_ll` varchar(10) DEFAULT NULL,
  `percent_left_fl` varchar(10) DEFAULT NULL,
  `error_left_ll` varchar(10) DEFAULT NULL,
  `error_left_fl` varchar(10) DEFAULT NULL,
  `standerd_rev_req_ll` varchar(10) DEFAULT NULL,
  `standerd_rev_req_fl` varchar(10) DEFAULT NULL,
  `terminal_seal` varchar(50) DEFAULT NULL,
  `terminal_seal_no` varchar(20) DEFAULT NULL,
  `terminal_seal_missing` varchar(100) DEFAULT NULL,
  `body_seal` varchar(50) DEFAULT NULL,
  `glass_cover` varchar(100) DEFAULT NULL,
  `test_clip` varchar(100) DEFAULT NULL,
  `remove_cause` varchar(255) DEFAULT NULL,
  `remove_date` date DEFAULT NULL,
  `comments` longtext,
  `remark` varchar(200) DEFAULT NULL,
  `cmo_type` varchar(50) DEFAULT NULL,
  `purchase_order` varchar(100) NOT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `updated_date` datetime(6) DEFAULT NULL,
  `checked_date` datetime(6) DEFAULT NULL,
  `counter_sign_date` datetime(6) DEFAULT NULL,
  `received_date` datetime(6) DEFAULT NULL,
  `checked_by_id` bigint DEFAULT NULL,
  `counter_sign_by_id` bigint DEFAULT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `office_id` bigint NOT NULL,
  `received_by_id` bigint DEFAULT NULL,
  `updated_by_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `test_data_test_data_checked_by_id_856fc401_fk_accounts_` (`checked_by_id`),
  KEY `test_data_test_data_counter_sign_by_id_0912c179_fk_accounts_` (`counter_sign_by_id`),
  KEY `test_data_test_data_created_by_id_2b9752ae_fk_accounts_` (`created_by_id`),
  KEY `test_data_test_data_office_id_f0d67f2f_fk_accounts_office_id` (`office_id`),
  KEY `test_data_test_data_received_by_id_910002cc_fk_accounts_` (`received_by_id`),
  KEY `test_data_test_data_updated_by_id_32a708fd_fk_accounts_` (`updated_by_id`),
  CONSTRAINT `test_data_test_data_checked_by_id_856fc401_fk_accounts_` FOREIGN KEY (`checked_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `test_data_test_data_counter_sign_by_id_0912c179_fk_accounts_` FOREIGN KEY (`counter_sign_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `test_data_test_data_created_by_id_2b9752ae_fk_accounts_` FOREIGN KEY (`created_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `test_data_test_data_office_id_f0d67f2f_fk_accounts_office_id` FOREIGN KEY (`office_id`) REFERENCES `accounts_office` (`id`),
  CONSTRAINT `test_data_test_data_received_by_id_910002cc_fk_accounts_` FOREIGN KEY (`received_by_id`) REFERENCES `accounts_customuser` (`id`),
  CONSTRAINT `test_data_test_data_updated_by_id_32a708fd_fk_accounts_` FOREIGN KEY (`updated_by_id`) REFERENCES `accounts_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_data_test_data`
--

LOCK TABLES `test_data_test_data` WRITE;
/*!40000 ALTER TABLE `test_data_test_data` DISABLE KEYS */;
INSERT INTO `test_data_test_data` VALUES (1,'18336154','2010','2010','1','31918','675','1026','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','সংযুক্ত','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:06:31.079325','2024-08-15 08:06:31.079325',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(2,'19593867','4452','4452','1','32336','576','9315','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:10:35.495566','2024-08-15 08:10:35.495566',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(3,'119751','3229','3229.1','1','30585','60','1429','Techno-D','40','J-39','0.5','1','10','2','10','4.61','23.11','99.57','99.83','-0.43','-0.17','4.61','23.11','99.57','99.83','-0.43','-0.17','4.63','23.15','ভালো','','','ভালো','','','',NULL,'মিটারটি ভলো আছে।','ব্যবহার উপযোগী।','Change','-','2024-08-15 08:11:25.953740','2024-08-15 08:11:25.953740',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(4,'182118','3686','3686','1','32430','39','5376','Hosaf-D','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:17:40.925368','2024-08-15 08:17:40.925368',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(5,'501400970863','4368','4368','1','28542','136','3104','Hexing','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে ব্যাটারী ও যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:23:45.002292','2024-08-15 08:23:45.002292',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(6,'1872515','288','288','1','29089','21','1125','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে মিটারটির সার্কিট নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:24:27.156092','2024-08-15 08:24:27.156092',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(7,'1696151','487','487','1','29090','21','2650','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো',NULL,NULL,'ভালো',NULL,NULL,NULL,NULL,'আভ্যন্তরীণ কারণে মিটারটির সার্কিট নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:29:12.470085','2024-08-15 08:29:52.450941',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(8,'2956305','182','182','1','29949','576','2085','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে মিটারটির সার্কিট নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:30:52.326755','2024-08-15 08:30:52.326755',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(9,'1759857','973','973','1','29950','576','2082','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে মিটারটির সার্কিট নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:31:16.796733','2024-08-15 08:31:16.796733',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(10,'00116002','8439','8439','1','30924','54','1094','Techno-D','40','J-39','0.5','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','4.63','23.15','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে মিটারটির সার্কিট নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:32:02.563887','2024-08-15 08:32:02.563887',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(11,'00014270','5967','5967.1','1','31404','294','2604','Techno-D','40','J-39','0.5','1','10','2','10','4.63','23.20','100.00','100.22','0.00','0.22','4.63','23.20','100.00','100.22','0.00','0.22','4.63','23.15','ভালো','','','ভালো','','','',NULL,'মিটারটি ভলো আছে।','ব্যবহার উপযোগী।','Change','-','2024-08-15 08:32:30.651877','2024-08-15 08:32:30.651877',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(12,'18250225','3460','3460','1','32542','318','1105','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:33:15.038849','2024-08-15 08:33:15.038849',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(13,'19901715','19908','19908','1','32397','118','2410','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','সংযুক্ত','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:36:52.855909','2024-08-15 08:36:52.871511',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(14,'19591749','2830','2830','1','32357','658','1392','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:37:22.681938','2024-08-15 08:37:22.681938',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(15,'20959356','1594','1594','1','32126','74','4233','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:37:47.679718','2024-08-15 08:37:47.679718',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(16,'00143602','1204','1204','1','32202','136','2201','Techno-D','40','J-39','0.5','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','4.63','23.15','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে মিটারটির যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:38:37.556137','2024-08-15 08:38:37.556137',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(17,'18485391','7076','7076','1','31967','808','2200','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:39:14.286286','2024-08-15 08:39:14.286286',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(18,'21378454','60','60','1','31556','487','1025','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:39:39.179085','2024-08-15 08:39:39.179085',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(19,'19906131','3849','3849','1','32403','772','1260','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:40:04.504791','2024-08-15 08:40:04.504791',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(20,'18537596','4697','4697','1','32121','808','1790','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:40:33.009544','2024-08-15 08:40:33.009544',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(21,'18835815','3398','3398','1','32237','817','2100','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:41:01.319993','2024-08-15 08:41:01.319993',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(22,'19320403','3927','3927','1','32449','850','1068','Hexing','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:41:31.480742','2024-08-15 08:41:31.480742',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(23,'21050224','2223','2223','1','32847','675','1733','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে সার্কিট ও ব্যাটারী নষ্ট হওয়ায় বিনা লোডে রিডিং পরিবর্তন হয়।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:41:59.619768','2024-08-15 08:41:59.619768',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(24,'56251','4272','4272','1','32079','59','1854','Techno-D','40','J-39','0.5','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','4.63','23.15','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে ব্যাটারী ও যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 08:42:35.583401','2024-08-15 08:42:35.583401',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(25,'19906515','1825','1825','1','32926','690','1670','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','সংযুক্ত','ভালো','','','',NULL,'মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:45:11.330406','2024-08-15 08:45:11.330406',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(26,'4019712','3612','3612','1','32815','606','3015','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:45:43.497887','2024-08-15 08:45:43.497887',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(27,'827143','15048','15048','1','32812','611','3830','Techno-A','40','J-1','2.222','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','20.57','102.87','ভালো','','','ভালো','','','',NULL,'দীর্ঘদিন ব্যবহার ও মরিচা জনিত কারণে যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:46:21.154612','2024-08-15 08:46:21.154612',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(28,'00221721','1956','1956','1','32741','796','1441','Techno-D','40','J-39','0.5','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','4.63','23.15','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:46:55.740117','2024-08-15 08:46:55.755715',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(29,'494235','3304','3304','1','32708','850','1128','Hosaf-D','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:47:32.109801','2024-08-15 08:47:32.125422',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(30,'0360580','3285','3285','1','32704','145','8672','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:48:04.940002','2024-08-15 08:48:04.940002',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(31,'21037770','1733','1733','1','32703','611','3818','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:48:34.435494','2024-08-15 08:48:34.435494',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(32,'2942749','x','x','1','32541','670','1755','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:49:03.222589','2024-08-15 08:49:03.222589',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(33,'21035726','1646','1646.1','1','32540','30','1773','B&T','40','J-39','0.625','1','10','2','10','5.78','28.88','99.83','99.79','-0.17','-0.21','5.78','28.88','99.83','99.79','-0.17','-0.21','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভলো আছে।','ব্যবহার উপযোগী।','Remove','-','2024-08-15 08:49:39.111290','2024-08-15 08:49:39.111290',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(34,'500891','x','x','1','32546','132','8595','Hosaf-D','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:50:24.623268','2024-08-15 08:50:24.623268',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(35,'2658156','602','602','1','32544','605','4716','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে মিটারটির সার্কিট নষ্ট।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:51:02.000323','2024-08-15 08:51:02.000323',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(36,'23416096','x','x','1','31916','508','1018','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:51:35.684220','2024-08-15 08:51:35.684220',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(37,'172606','6','6','1','32287','576','9436','Hosaf-D','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:52:34.779107','2024-08-15 08:52:34.779107',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(38,'2477455','847','847','1','32288','819','1215','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:53:05.880058','2024-08-15 08:53:05.880058',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(39,'2633303','3064','3064.1','1','31664','133','1058','Pasha','40','J-39','0.625','1','10','2','10','5.79','28.98','100.00','100.14','0.00','0.14','5.79','28.98','100.00','100.14','0.00','0.14','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভলো আছে।','ব্যবহার উপযোগী।','Remove','-','2024-08-15 08:53:37.262431','2024-08-15 08:53:37.278051',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(40,'00149541','x','x','1','32428','585','1635','Techno-D','40','J-39','0.5','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','4.63','23.15','ভালো','','','ভালো','','','',NULL,'মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:54:20.358150','2024-08-15 08:54:20.358150',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(41,'00097485','x','x','1','32424','720','4088','Techno-D','40','J-39','0.5','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','4.63','23.15','ভালো','','','ভালো','','','',NULL,'মিটারটির সোর্স সাইড পোড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:55:29.743371','2024-08-15 08:55:29.743371',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(42,'00165853','23074','23074','1','32194','479','1855','Techno-A','40','J-1','2.222','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','20.57','102.87','ভালো','','','ভালো','','','',NULL,'দীর্ঘদিন ব্যবহার ও মরিচা জনিত কারণে যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:56:31.870963','2024-08-15 08:56:31.870963',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(43,'0672295','x','x','1','32191','27','4156','Power Plus','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:57:07.076196','2024-08-15 08:57:07.076196',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(44,'501400146077','x','x','1','32322','611','6520','Hexcell','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে ব্যাটারী ও যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 08:57:49.971972','2024-08-15 08:57:49.971972',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(45,'15568234','8091','8091.1','1','31799','133','1020','Hexing','40','J-39','0.625','1','10','2','10','5.77','28.89','99.65','99.83','-0.35','-0.17','5.77','28.89','99.65','99.83','-0.35','-0.17','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভলো আছে।','ব্যবহার উপযোগী।','Remove','-','2024-08-15 08:58:34.299623','2024-08-15 08:58:34.299623',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(46,'22114032','8853','8853','1','32578','120','1120','MT(Hangzhou)','200','J-3','10.0','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','0','0','ভালো','107427453','সংযুক্ত','ভালো','ভালো','ভালো','আবেদনে রিমোভ','2024-08-01','বাহ্যিক দৃষ্টিতে ত্রুটি পরিলক্ষিত হয়নি।','পরীক্ষার জন্য বিআরইবিতে প্রেরণ প্রক্রিয়াধীন।','Remove','-','2024-08-15 09:07:33.881078','2024-08-15 09:07:33.881078',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(47,'00162412','21619','21619.1','1','32810','508','1275','Techno-A','40','J-1','2.222','1','10','2','10','20.48','102.66','99.56','99.80','-0.44','-0.20','20.48','102.66','99.56','99.80','-0.44','-0.20','20.57','102.87','ভালো','','','ভালো','','','',NULL,'দীর্ঘদিন ব্যবহার ও মরিচা জনিত কারণে যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 09:12:51.981167','2024-08-15 09:12:51.981167',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(48,'21054','3893','3893','1','32876','39','3292','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভাঙ্গা।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 09:13:39.449150','2024-08-15 09:13:39.449150',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(49,'21039805','9405','9405.1','1','32875','574','3046','B&T','40','J-39','0.625','1','10','2','10','5.81','28.86','100.35','99.72','0.35','-0.28','5.81','28.86','100.35','99.72','0.35','-0.28','5.79','28.94','ভালো','','সংযুক্ত','ভালো','','','',NULL,'মিটারটি ভলো আছে।','ব্যবহার উপযোগী।','Remove','-','2024-08-15 10:25:38.885310','2024-08-15 10:25:39.105019',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(50,'416162','1634','1634.1','1','32207','214','4135','Hosaf-D','40','J-39','0.625','1','10','2','10','5.81','28.86','100.35','99.72','0.35','-0.28','5.81','28.86','100.35','99.72','0.35','-0.28','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি ভলো আছে।','ব্যবহার উপযোগী।','Remove','-','2024-08-15 10:26:15.599445','2024-08-15 10:26:15.599445',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(51,'23440414','10234','10234','1','91826','122','1722','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটির সোর্স সাইড পোড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 10:26:49.467400','2024-08-15 10:26:49.467400',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(52,'2993097','x','x','1','92705','145','1585','Pasha','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'মিটারটি পুড়া।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 10:27:31.363261','2024-08-15 10:27:31.378882',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(53,'21423244','5','5','1','29078','41','3115','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 10:28:08.960921','2024-08-15 10:28:08.960921',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(54,'18825507','17','17','1','30939','27','4387','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Remove','-','2024-08-15 10:28:34.642984','2024-08-15 10:28:34.642984',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(55,'18805297','54','54','1','31505','817','2680','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 10:29:10.713795','2024-08-15 10:29:10.713795',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(56,'16691374','x','x','1','32101','776','1300','Echo','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','নাই','','','ভালো','','','',NULL,'আভ্যন্তরীণ কারণে মিটারটির যন্ত্রাংশ নষ্ট।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 10:31:34.129296','2024-08-15 10:31:34.129296',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(57,'18822392','15','15','1','30751','132','3037','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 10:33:36.964618','2024-08-15 10:33:36.964618',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(58,'21398906','27','27','1','30746','132','2264','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 10:34:08.895876','2024-08-15 10:34:08.895876',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(59,'17647617','5','5','1','30778','132','8582','Hexing','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 10:34:42.658245','2024-08-15 10:34:42.658245',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2),(60,'18534763','10','10','1','30754','132','4106','B&T','40','J-39','0.625','1','10','2','10','--','--','--','--','--','--','--','--','--','--','--','--','5.79','28.94','ভালো','','','ভালো','','','',NULL,'যান্ত্রিক কারণে মিটারটির সার্কিট ও ব্যাটারী নষ্ট হওয়ায় রিডিং অস্বাভাবিক।','ব্যবহার অনুপযোগী।','Change','-','2024-08-15 10:35:15.173007','2024-08-15 10:35:15.173007',NULL,NULL,NULL,NULL,NULL,2,1,NULL,2);
/*!40000 ALTER TABLE `test_data_test_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_data_uploads`
--

DROP TABLE IF EXISTS `test_data_uploads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_data_uploads` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `url` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_data_uploads`
--

LOCK TABLES `test_data_uploads` WRITE;
/*!40000 ALTER TABLE `test_data_uploads` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_data_uploads` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-15 17:40:54
