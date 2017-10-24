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
-- Table structure for table `GovernmentAgencies`
--

DROP TABLE IF EXISTS `GovernmentAgencies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GovernmentAgencies` (
  `username` varchar(255) NOT NULL,
  `jurisdiction` varchar(255) NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `governmentagencies_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Usertable` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GovernmentAgencies`
--

LOCK TABLES `GovernmentAgencies` WRITE;
/*!40000 ALTER TABLE `GovernmentAgencies` DISABLE KEYS */;
INSERT INTO `GovernmentAgencies` VALUES ('tomgov0','tomgovjuris0'),('tomgov1','tomgovjuris1'),('tomgov10','tomgovjuris10'),('tomgov11','tomgovjuris11'),('tomgov12','tomgovjuris12'),('tomgov13','tomgovjuris13'),('tomgov14','tomgovjuris14'),('tomgov15','tomgovjuris15'),('tomgov16','tomgovjuris16'),('tomgov17','tomgovjuris17'),('tomgov18','tomgovjuris18'),('tomgov19','tomgovjuris19'),('tomgov2','tomgovjuris2'),('tomgov20','tomgovjuris20'),('tomgov21','tomgovjuris21'),('tomgov22','tomgovjuris22'),('tomgov23','tomgovjuris23'),('tomgov24','tomgovjuris24'),('tomgov25','tomgovjuris25'),('tomgov26','tomgovjuris26'),('tomgov27','tomgovjuris27'),('tomgov28','tomgovjuris28'),('tomgov29','tomgovjuris29'),('tomgov3','tomgovjuris3'),('tomgov30','tomgovjuris30'),('tomgov31','tomgovjuris31'),('tomgov32','tomgovjuris32'),('tomgov33','tomgovjuris33'),('tomgov34','tomgovjuris34'),('tomgov35','tomgovjuris35'),('tomgov36','tomgovjuris36'),('tomgov37','tomgovjuris37'),('tomgov38','tomgovjuris38'),('tomgov39','tomgovjuris39'),('tomgov4','tomgovjuris4'),('tomgov40','tomgovjuris40'),('tomgov41','tomgovjuris41'),('tomgov42','tomgovjuris42'),('tomgov43','tomgovjuris43'),('tomgov44','tomgovjuris44'),('tomgov45','tomgovjuris45'),('tomgov46','tomgovjuris46'),('tomgov47','tomgovjuris47'),('tomgov48','tomgovjuris48'),('tomgov49','tomgovjuris49'),('tomgov5','tomgovjuris5'),('tomgov6','tomgovjuris6'),('tomgov7','tomgovjuris7'),('tomgov8','tomgovjuris8'),('tomgov9','tomgovjuris9'),('tom_government_00:57:52.690399','state_gov'),('tom_government_22:50:05.490988','state_gov'),('tom_government_22:50:44.346462','state_gov'),('tom_government_22:52:28.519216','state_gov'),('tom_government_22:53:25.049060','state_gov'),('tom_government_22:53:52.054285','state_gov'),('tom_government_22:54:20.676724','state_gov'),('tom_government_22:55:28.981049','state_gov'),('tom_government_22:55:55.646634','state_gov'),('tom_government_22:56:16.478416','state_gov'),('tom_government_23:42:12.597154','state_gov'),('tom_government_23:42:50.253553','state_gov'),('tom_government_23:43:01.524557','state_gov'),('tom_government_23:43:54.847942','state_gov'),('tom_government_23:44:29.594617','state_gov'),('tom_government_23:44:48.380890','state_gov'),('tom_government_23:45:50.379813','state_gov'),('tom_government_23:46:33.616740','state_gov'),('tom_government_23:46:53.506456','state_gov'),('tom_government_23:47:35.169599','state_gov'),('tom_government_23:50:08.337337','state_gov'),('tom_government_23:52:38.618733','state_gov'),('tom_government_23:53:13.045732','state_gov');
/*!40000 ALTER TABLE `GovernmentAgencies` ENABLE KEYS */;
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
