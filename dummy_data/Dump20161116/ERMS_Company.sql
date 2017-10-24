-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: ERMS
-- ------------------------------------------------------
-- Server version	5.7.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Company`
--

DROP TABLE IF EXISTS `Company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Company` (
  `username` varchar(255) NOT NULL,
  `headquarteres` varchar(255) NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `company_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Usertable` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Company`
--

LOCK TABLES `Company` WRITE;
/*!40000 ALTER TABLE `Company` DISABLE KEYS */;
INSERT INTO `Company` VALUES ('tomcompany0','tomcompany_headquater0'),('tomcompany1','tomcompany_headquater1'),('tomcompany10','tomcompany_headquater10'),('tomcompany11','tomcompany_headquater11'),('tomcompany12','tomcompany_headquater12'),('tomcompany13','tomcompany_headquater13'),('tomcompany14','tomcompany_headquater14'),('tomcompany15','tomcompany_headquater15'),('tomcompany16','tomcompany_headquater16'),('tomcompany17','tomcompany_headquater17'),('tomcompany18','tomcompany_headquater18'),('tomcompany19','tomcompany_headquater19'),('tomcompany2','tomcompany_headquater2'),('tomcompany20','tomcompany_headquater20'),('tomcompany21','tomcompany_headquater21'),('tomcompany22','tomcompany_headquater22'),('tomcompany23','tomcompany_headquater23'),('tomcompany24','tomcompany_headquater24'),('tomcompany25','tomcompany_headquater25'),('tomcompany26','tomcompany_headquater26'),('tomcompany27','tomcompany_headquater27'),('tomcompany28','tomcompany_headquater28'),('tomcompany29','tomcompany_headquater29'),('tomcompany3','tomcompany_headquater3'),('tomcompany30','tomcompany_headquater30'),('tomcompany31','tomcompany_headquater31'),('tomcompany32','tomcompany_headquater32'),('tomcompany33','tomcompany_headquater33'),('tomcompany34','tomcompany_headquater34'),('tomcompany35','tomcompany_headquater35'),('tomcompany36','tomcompany_headquater36'),('tomcompany37','tomcompany_headquater37'),('tomcompany38','tomcompany_headquater38'),('tomcompany39','tomcompany_headquater39'),('tomcompany4','tomcompany_headquater4'),('tomcompany40','tomcompany_headquater40'),('tomcompany41','tomcompany_headquater41'),('tomcompany42','tomcompany_headquater42'),('tomcompany43','tomcompany_headquater43'),('tomcompany44','tomcompany_headquater44'),('tomcompany45','tomcompany_headquater45'),('tomcompany46','tomcompany_headquater46'),('tomcompany47','tomcompany_headquater47'),('tomcompany48','tomcompany_headquater48'),('tomcompany49','tomcompany_headquater49'),('tomcompany5','tomcompany_headquater5'),('tomcompany6','tomcompany_headquater6'),('tomcompany7','tomcompany_headquater7'),('tomcompany8','tomcompany_headquater8'),('tomcompany9','tomcompany_headquater9'),('tom_company_00:57:52.690326','newyork'),('tom_company_22:49:44.469806','newyork'),('tom_company_22:50:05.490958','newyork'),('tom_company_22:50:21.227396','newyork'),('tom_company_22:50:44.346423','newyork'),('tom_company_22:52:28.519189','newyork'),('tom_company_22:53:25.049029','newyork'),('tom_company_22:53:52.054249','newyork'),('tom_company_22:54:20.676695','newyork'),('tom_company_22:55:28.981016','newyork'),('tom_company_22:55:55.646580','newyork'),('tom_company_22:56:16.478325','newyork'),('tom_company_23:42:12.597124','newyork'),('tom_company_23:42:50.253505','newyork'),('tom_company_23:43:01.524526','newyork'),('tom_company_23:43:54.847904','newyork'),('tom_company_23:44:29.594587','newyork'),('tom_company_23:44:48.380861','newyork'),('tom_company_23:45:50.379784','newyork'),('tom_company_23:46:33.616711','newyork'),('tom_company_23:46:53.506408','newyork'),('tom_company_23:47:35.169568','newyork'),('tom_company_23:50:08.337306','newyork'),('tom_company_23:52:38.618701','newyork'),('tom_company_23:53:13.045700','newyork');
/*!40000 ALTER TABLE `Company` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-16 23:27:46
