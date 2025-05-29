-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: epic
-- ------------------------------------------------------
-- Server version	8.0.42

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

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `website_link` varchar(50) DEFAULT NULL,
  `system_user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  UNIQUE KEY `system_user_id_UNIQUE` (`system_user_id`),
  CONSTRAINT `system_user_id2` FOREIGN KEY (`system_user_id`) REFERENCES `system_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'oihfhwgr','None','None',NULL),(3,'oops','woo','wee',NULL),(4,'manna','adsfkjsdf','asdkjfh',NULL),(5,'Amazon Web Services','asdf','gdgfh',3),(6,'Intercom','jkfds','rweyhtrjdnf',NULL),(7,'Transact','fasdhjkhdfg','wihuhb',NULL),(8,'Dogpatch Labs','kjsahgv','mxncbvi',NULL);
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interview_ranking`
--

DROP TABLE IF EXISTS `interview_ranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interview_ranking` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ranking` int NOT NULL,
  `listing_id` int NOT NULL,
  `student_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idListing_idx` (`listing_id`),
  KEY `idStudent_idx` (`student_id`),
  CONSTRAINT `listing_id` FOREIGN KEY (`listing_id`) REFERENCES `listing` (`id`),
  CONSTRAINT `student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interview_ranking`
--

LOCK TABLES `interview_ranking` WRITE;
/*!40000 ALTER TABLE `interview_ranking` DISABLE KEYS */;
INSERT INTO `interview_ranking` VALUES (1,5,6,23),(2,1,8,23),(3,3,9,23),(4,4,10,23),(5,2,11,23),(6,1,6,24),(7,5,8,24),(8,4,9,24),(9,3,10,24),(11,2,11,24),(12,2,6,25),(13,3,8,25),(14,1,9,25),(15,4,10,25),(16,5,11,25),(17,1,6,42),(18,2,8,42),(19,5,9,42),(20,3,10,42),(21,4,11,42),(22,2,6,46),(23,5,8,46),(24,3,9,46),(25,4,10,46),(26,1,11,46),(27,2,6,51),(28,3,8,51),(29,5,9,51),(30,1,10,51),(31,4,11,51),(32,4,6,52),(33,3,8,52),(34,5,9,52),(35,1,10,52),(36,2,11,52),(37,2,6,53),(39,1,8,53),(40,3,9,53),(41,4,10,53),(42,5,11,53),(43,4,6,54),(44,1,8,54),(45,3,9,54),(46,5,10,54),(47,2,11,54);
/*!40000 ALTER TABLE `interview_ranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listing`
--

DROP TABLE IF EXISTS `listing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listing` (
  `id` int NOT NULL AUTO_INCREMENT,
  `job_title` varchar(45) NOT NULL,
  `description` text NOT NULL,
  `location` varchar(45) NOT NULL,
  `available_places` int NOT NULL,
  `residency_number` varchar(5) NOT NULL,
  `accommodation_support` varchar(45) DEFAULT NULL,
  `work_mode` varchar(100) DEFAULT NULL,
  `company_id` int NOT NULL,
  PRIMARY KEY (`id`,`company_id`),
  KEY `idCompany_idx` (`company_id`),
  CONSTRAINT `company_id` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listing`
--

LOCK TABLES `listing` WRITE;
/*!40000 ALTER TABLE `listing` DISABLE KEYS */;
INSERT INTO `listing` VALUES (6,'data person','jkdsfjkdfsjklfdsljkdsfd','Tipperary',1,'R1+R2','non','hybrid',4),(8,'intern','kasdgxcnncxv','Dublin',6,'R1+R2','yee','office!!1!',5),(9,'woohooo','mcxvncxvoieqwo','Dublin',4,'R1+R2','yee','offees!',6),(10,'programming person','xvzccxv','Limerick',2,'R1','nein','offish',7),(11,'bread','oiwerem','Dooblun',2,'R1','yah?','lol',8);
/*!40000 ALTER TABLE `listing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_history`
--

DROP TABLE IF EXISTS `process_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `process_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `state` varchar(40) NOT NULL,
  `state_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_history`
--

LOCK TABLES `process_history` WRITE;
/*!40000 ALTER TABLE `process_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `residency_ranking`
--

DROP TABLE IF EXISTS `residency_ranking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `residency_ranking` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `listing_id` int NOT NULL,
  `student_ranking` int DEFAULT NULL,
  `company_ranking` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id_idx` (`student_id`),
  KEY `listing_id3_idx` (`listing_id`),
  CONSTRAINT `listing_id3` FOREIGN KEY (`listing_id`) REFERENCES `listing` (`id`),
  CONSTRAINT `student_id2` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `residency_ranking`
--

LOCK TABLES `residency_ranking` WRITE;
/*!40000 ALTER TABLE `residency_ranking` DISABLE KEYS */;
INSERT INTO `residency_ranking` VALUES (2,51,10,2,6),(3,52,10,1,1),(4,24,10,3,2),(5,46,10,2,3),(6,42,10,1,4),(7,53,10,3,5),(16,23,6,1,2),(17,24,6,1,1),(18,25,6,2,3),(19,46,11,3,2),(20,54,11,1,1),(21,23,11,3,3),(22,52,11,3,6),(23,25,11,1,4),(24,42,11,2,5),(25,23,8,2,7),(26,42,8,3,1),(27,51,8,3,4),(28,24,8,2,9),(29,25,8,3,8),(30,54,8,2,2),(32,46,8,1,6),(33,53,8,2,3),(34,52,8,2,5),(35,53,9,1,2),(36,51,9,1,3),(37,54,9,3,1);
/*!40000 ALTER TABLE `residency_ranking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `score` int NOT NULL,
  `listing_id_selected` int DEFAULT NULL,
  `system_user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `score_UNIQUE` (`score`),
  UNIQUE KEY `system_user_id_UNIQUE` (`system_user_id`),
  KEY `listing_id2_idx` (`listing_id_selected`),
  CONSTRAINT `listing_id2` FOREIGN KEY (`listing_id_selected`) REFERENCES `listing` (`id`),
  CONSTRAINT `system_user_id1` FOREIGN KEY (`system_user_id`) REFERENCES `system_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (23,'April','Gilhool',3,NULL,NULL),(24,'Aaron','Odoherty',4,NULL,NULL),(25,'Skye','FitzPatrick',5,NULL,NULL),(42,'James','Hayes',2,NULL,NULL),(46,'Yasmin','Woodlock',1,NULL,2),(51,'Anna','Maughan',6,NULL,NULL),(52,'Ciaran','Lynch',7,NULL,NULL),(53,'Holly','Best',8,NULL,NULL),(54,'Ryan','Morissey',9,NULL,NULL),(55,'Sarah','McDonagh',10,NULL,NULL),(56,'Aoibheann','Mangan',11,NULL,NULL),(57,'Caitlin','Moloney',12,NULL,NULL);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_user`
--

DROP TABLE IF EXISTS `system_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_user`
--

LOCK TABLES `system_user` WRITE;
/*!40000 ALTER TABLE `system_user` DISABLE KEYS */;
INSERT INTO `system_user` VALUES (1,'admin'),(2,'yasmin'),(3,'aws');
/*!40000 ALTER TABLE `system_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'epic'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-29 10:00:10
