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
-- Table structure for table `Municipalities`
--

DROP TABLE IF EXISTS `Municipalities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Municipalities` (
  `username` varchar(255) NOT NULL,
  `populationSize` int(11) NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `municipalities_ibfk_1` FOREIGN KEY (`username`) REFERENCES `Usertable` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Municipalities`
--

LOCK TABLES `Municipalities` WRITE;
/*!40000 ALTER TABLE `Municipalities` DISABLE KEYS */;
INSERT INTO `Municipalities` VALUES ('muni0',1000),('muni1',1001),('muni10',1010),('muni11',1011),('muni12',1012),('muni13',1013),('muni14',1014),('muni15',1015),('muni16',1016),('muni17',1017),('muni18',1018),('muni19',1019),('muni2',1002),('muni20',1020),('muni21',1021),('muni22',1022),('muni23',1023),('muni24',1024),('muni25',1025),('muni26',1026),('muni27',1027),('muni28',1028),('muni29',1029),('muni3',1003),('muni30',1030),('muni31',1031),('muni32',1032),('muni33',1033),('muni34',1034),('muni35',1035),('muni36',1036),('muni37',1037),('muni38',1038),('muni39',1039),('muni4',1004),('muni40',1040),('muni41',1041),('muni42',1042),('muni43',1043),('muni44',1044),('muni45',1045),('muni46',1046),('muni47',1047),('muni48',1048),('muni49',1049),('muni5',1005),('muni6',1006),('muni7',1007),('muni8',1008),('muni9',1009),('tom_municipal_00:57:52.690409',888),('tom_municipal_22:50:05.490992',888),('tom_municipal_22:50:44.346467',888),('tom_municipal_22:52:28.519220',888),('tom_municipal_22:53:25.049064',888),('tom_municipal_22:53:52.054289',888),('tom_municipal_22:54:20.676727',888),('tom_municipal_22:55:28.981054',888),('tom_municipal_22:55:55.646640',888),('tom_municipal_22:56:16.478424',888),('tom_municipal_23:42:12.597158',888),('tom_municipal_23:42:50.253561',888),('tom_municipal_23:43:01.524561',888),('tom_municipal_23:43:54.847948',888),('tom_municipal_23:44:29.594621',888),('tom_municipal_23:44:48.380893',888),('tom_municipal_23:45:50.379817',888),('tom_municipal_23:46:33.616744',888),('tom_municipal_23:46:53.506460',888),('tom_municipal_23:47:35.169603',888),('tom_municipal_23:50:08.337340',888),('tom_municipal_23:52:38.618737',888),('tom_municipal_23:53:13.045736',888);
/*!40000 ALTER TABLE `Municipalities` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-16 23:27:45
