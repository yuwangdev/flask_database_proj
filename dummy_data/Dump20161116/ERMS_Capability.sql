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
-- Table structure for table `Capability`
--

DROP TABLE IF EXISTS `Capability`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Capability` (
  `ResourceID` int(11) NOT NULL,
  `CapabilitiyStr` varchar(255) NOT NULL,
  PRIMARY KEY (`ResourceID`,`CapabilitiyStr`),
  CONSTRAINT `capability_ibfk_1` FOREIGN KEY (`ResourceID`) REFERENCES `Resource` (`ResourceID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Capability`
--

LOCK TABLES `Capability` WRITE;
/*!40000 ALTER TABLE `Capability` DISABLE KEYS */;
INSERT INTO `Capability` VALUES (13,'aaa'),(13,'bbb'),(14,'aaa'),(14,'bbb'),(17,'aaa'),(17,'bbb'),(18,'aaa'),(18,'bbb'),(123,'cap123-1'),(123,'cap123-10'),(123,'cap123-11'),(123,'cap123-2'),(123,'cap123-3'),(123,'cap123-4'),(123,'cap123-5'),(123,'cap123-8'),(123,'cap123-9'),(663,'capx'),(664,'capx'),(665,'capx'),(666,'capx'),(667,'capx'),(668,'capx'),(669,'capx'),(670,'capx'),(671,'capx'),(672,'capx'),(673,'capx'),(674,'capx'),(675,'capx'),(676,'capx'),(677,'capx'),(678,'capx'),(679,'capx'),(680,'capx'),(681,'capx'),(682,'capx'),(683,'capx'),(684,'capx'),(685,'capx'),(686,'capx'),(687,'capx'),(688,'capx'),(689,'capx'),(690,'capx'),(691,'capx'),(692,'capx'),(693,'capx'),(694,'capx'),(695,'capx'),(696,'capx'),(697,'capx'),(698,'capx'),(699,'capx'),(700,'capx'),(701,'capx'),(702,'capx'),(703,'capx'),(704,'capx'),(705,'capx'),(706,'capx'),(707,'capx'),(708,'capx'),(709,'capx'),(710,'capx'),(711,'capx'),(712,'capx'),(713,'capx'),(714,'capx'),(715,'capx'),(716,'capx'),(717,'capx'),(718,'capx'),(719,'capx'),(720,'capx'),(721,'capx'),(722,'capx'),(723,'capx'),(724,'capx'),(725,'capx'),(726,'capx'),(727,'capx'),(728,'capx'),(729,'capx'),(730,'capx'),(731,'capx'),(732,'capx'),(733,'capx'),(734,'capx'),(735,'capx'),(736,'capx'),(737,'capx'),(738,'capx'),(739,'capx'),(740,'capx'),(741,'capx'),(742,'capx'),(743,'capx'),(744,'capx'),(745,'capx'),(746,'capx'),(747,'capx'),(748,'capx'),(749,'capx'),(750,'capx'),(751,'capx'),(752,'capx'),(753,'capx'),(754,'capx'),(755,'capx'),(756,'capx'),(757,'capx'),(758,'capx'),(759,'capx'),(760,'capx'),(761,'capx'),(762,'capx'),(763,'capx'),(764,'capx'),(765,'capx'),(766,'capx'),(767,'capx'),(768,'capx'),(769,'capx'),(770,'capx'),(771,'capx'),(772,'capx'),(773,'capx'),(774,'capx'),(775,'capx'),(776,'capx'),(777,'capx'),(778,'capx'),(779,'capx'),(780,'capx'),(781,'capx'),(782,'capx'),(783,'capx'),(784,'capx'),(785,'capx'),(786,'capx'),(787,'capx'),(788,'capx'),(789,'capx'),(790,'capx'),(791,'capx'),(792,'capx'),(793,'capx'),(794,'capx'),(795,'capx'),(796,'capx'),(797,'capx'),(798,'capx'),(799,'capx'),(800,'capx'),(801,'capx'),(802,'capx'),(803,'capx'),(804,'capx'),(805,'capx'),(806,'capx'),(807,'capx'),(808,'capx'),(809,'capx'),(810,'capx'),(811,'capx'),(812,'capx'),(813,'capx'),(814,'capx'),(815,'capx'),(816,'capx'),(817,'capx'),(818,'capx'),(819,'capx'),(820,'capx'),(821,'capx'),(822,'capx'),(823,'capx'),(824,'capx'),(825,'capx'),(826,'capx'),(827,'capx'),(828,'capx'),(829,'capx'),(830,'capx'),(831,'capx'),(832,'capx'),(833,'capx'),(834,'capx'),(835,'capx'),(836,'capx'),(837,'capx'),(838,'capx'),(839,'capx'),(840,'capx'),(841,'capx'),(842,'capx'),(843,'capx'),(844,'capx'),(845,'capx'),(846,'capx'),(847,'capx'),(848,'capx'),(849,'capx'),(850,'capx'),(851,'capx'),(852,'capx'),(853,'capx'),(854,'capx'),(855,'capx'),(856,'capx'),(857,'capx'),(858,'capx');
/*!40000 ALTER TABLE `Capability` ENABLE KEYS */;
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
