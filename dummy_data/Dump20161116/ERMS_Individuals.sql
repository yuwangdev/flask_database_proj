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
-- Table structure for table `Individuals`
--

DROP TABLE IF EXISTS `Individuals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Individuals` (
  `username` varchar(255) NOT NULL,
  `jobTitle` varchar(255) NOT NULL,
  `dateOfHired` date NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `individuals_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Usertable` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Individuals`
--

LOCK TABLES `Individuals` WRITE;
/*!40000 ALTER TABLE `Individuals` DISABLE KEYS */;
INSERT INTO `Individuals` VALUES ('tomindi0','tomindijobtitle0','2016-11-14'),('tomindi1','tomindijobtitle1','2016-11-14'),('tomindi10','tomindijobtitle10','2016-11-14'),('tomindi11','tomindijobtitle11','2016-11-14'),('tomindi12','tomindijobtitle12','2016-11-14'),('tomindi13','tomindijobtitle13','2016-11-14'),('tomindi14','tomindijobtitle14','2016-11-14'),('tomindi15','tomindijobtitle15','2016-11-14'),('tomindi16','tomindijobtitle16','2016-11-14'),('tomindi17','tomindijobtitle17','2016-11-14'),('tomindi18','tomindijobtitle18','2016-11-14'),('tomindi19','tomindijobtitle19','2016-11-14'),('tomindi2','tomindijobtitle2','2016-11-14'),('tomindi20','tomindijobtitle20','2016-11-14'),('tomindi21','tomindijobtitle21','2016-11-14'),('tomindi22','tomindijobtitle22','2016-11-14'),('tomindi23','tomindijobtitle23','2016-11-14'),('tomindi24','tomindijobtitle24','2016-11-14'),('tomindi25','tomindijobtitle25','2016-11-14'),('tomindi26','tomindijobtitle26','2016-11-14'),('tomindi27','tomindijobtitle27','2016-11-14'),('tomindi28','tomindijobtitle28','2016-11-14'),('tomindi29','tomindijobtitle29','2016-11-14'),('tomindi3','tomindijobtitle3','2016-11-14'),('tomindi30','tomindijobtitle30','2016-11-14'),('tomindi31','tomindijobtitle31','2016-11-14'),('tomindi32','tomindijobtitle32','2016-11-14'),('tomindi33','tomindijobtitle33','2016-11-14'),('tomindi34','tomindijobtitle34','2016-11-14'),('tomindi35','tomindijobtitle35','2016-11-14'),('tomindi36','tomindijobtitle36','2016-11-14'),('tomindi37','tomindijobtitle37','2016-11-14'),('tomindi38','tomindijobtitle38','2016-11-14'),('tomindi39','tomindijobtitle39','2016-11-14'),('tomindi4','tomindijobtitle4','2016-11-14'),('tomindi40','tomindijobtitle40','2016-11-14'),('tomindi41','tomindijobtitle41','2016-11-14'),('tomindi42','tomindijobtitle42','2016-11-14'),('tomindi43','tomindijobtitle43','2016-11-14'),('tomindi44','tomindijobtitle44','2016-11-14'),('tomindi45','tomindijobtitle45','2016-11-14'),('tomindi46','tomindijobtitle46','2016-11-14'),('tomindi47','tomindijobtitle47','2016-11-14'),('tomindi48','tomindijobtitle48','2016-11-14'),('tomindi49','tomindijobtitle49','2016-11-14'),('tomindi5','tomindijobtitle5','2016-11-14'),('tomindi6','tomindijobtitle6','2016-11-14'),('tomindi7','tomindijobtitle7','2016-11-14'),('tomindi8','tomindijobtitle8','2016-11-14'),('tomindi9','tomindijobtitle9','2016-11-14'),('tom_individual_00:57:52.690380','programmer','2015-04-12'),('tom_individual_22:50:44.346458','programmer','2015-04-12'),('tom_individual_22:52:28.519211','programmer','2015-04-12'),('tom_individual_22:53:25.049055','programmer','2015-04-12'),('tom_individual_22:53:52.054280','programmer','2015-04-12'),('tom_individual_22:54:20.676720','programmer','2015-04-12'),('tom_individual_22:55:28.981041','programmer','2015-04-12'),('tom_individual_22:55:55.646624','programmer','2015-04-12'),('tom_individual_22:56:16.478404','programmer','2015-04-12'),('tom_individual_23:42:12.597149','programmer','2015-04-12'),('tom_individual_23:42:50.253542','programmer','2015-04-12'),('tom_individual_23:43:01.524551','programmer','2015-04-12'),('tom_individual_23:43:54.847935','programmer','2015-04-12'),('tom_individual_23:44:29.594611','programmer','2015-04-12'),('tom_individual_23:44:48.380884','programmer','2015-04-12'),('tom_individual_23:45:50.379808','programmer','2015-04-12'),('tom_individual_23:46:33.616735','programmer','2015-04-12'),('tom_individual_23:46:53.506450','programmer','2015-04-12'),('tom_individual_23:47:35.169594','programmer','2015-04-12'),('tom_individual_23:50:08.337332','programmer','2015-04-12'),('tom_individual_23:52:38.618728','programmer','2015-04-12'),('tom_individual_23:53:13.045726','programmer','2015-04-12');
/*!40000 ALTER TABLE `Individuals` ENABLE KEYS */;
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
