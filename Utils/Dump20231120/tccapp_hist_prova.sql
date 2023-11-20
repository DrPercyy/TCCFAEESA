-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tccapp
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `hist_prova`
--

DROP TABLE IF EXISTS `hist_prova`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hist_prova` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `GAB_CODE` mediumtext,
  `DATA_PROVA` date DEFAULT NULL,
  `ALUNO_ID` int NOT NULL,
  PRIMARY KEY (`ID`,`ALUNO_ID`),
  KEY `fk_HIST_PROVA_ALUNO1_idx` (`ALUNO_ID`),
  CONSTRAINT `fk_HIST_PROVA_ALUNO1` FOREIGN KEY (`ALUNO_ID`) REFERENCES `aluno` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hist_prova`
--

LOCK TABLES `hist_prova` WRITE;
/*!40000 ALTER TABLE `hist_prova` DISABLE KEYS */;
INSERT INTO `hist_prova` VALUES (49,'5 - E -- 3 - C -- 5 - E -- 3 - C -- 4 - D -- 2 - B -- 1 - A -- 4 - D -- 1 - A -- 4 - D -- ','2023-11-16',3),(50,'2 - B -- 1 - A -- 4 - D -- 1 - A -- 3 - C -- 3 - C -- 1 - A -- 2 - B -- 4 - D -- 4 - D -- ','2019-10-18',3),(51,'3 - C -- 3 - C -- 3 - C -- 4 - D -- 4 - D -- 3 - C -- 4 - D -- 5 - E -- 2 - B -- 1 - A -- ','2023-10-17',3),(52,'1 - A -- 4 - D -- 4 - D -- 2 - B -- 4 - D -- 2 - B -- 3 - C -- 1 - A -- 1 - A -- 3 - C -- ','2023-10-17',3),(53,'4 - D -- 1 - A -- 5 - E -- 3 - C -- 5 - E -- 4 - D -- 1 - A -- 3 - C -- 3 - C -- 1 - A -- ','1974-10-10',3),(54,'5 - E -- 2 - B -- 3 - C -- 1 - A -- 4 - D -- 4 - D -- 5 - E -- 3 - C -- 3 - C -- 3 - C -- ','2010-10-10',3),(55,'1 - A -- 2 - B -- 2 - B -- 3 - C -- 4 - D -- 4 - D -- 1 - A -- 3 - C -- 3 - C -- 4 - D -- ','2010-10-10',4),(56,'3 - C -- 1 - A -- 5 - E -- 2 - B -- 3 - C -- 3 - C -- 4 - D -- 3 - C -- 1 - A -- 1 - A -- ','2010-10-10',5),(57,'1 - A -- 2 - B -- 4 - D -- 4 - D -- 3 - C -- 4 - D -- 3 - C -- 5 - E -- 3 - C -- 1 - A -- ','2010-10-10',6),(58,'5 - E -- 1 - A -- 2 - B -- 4 - D -- 4 - D -- 3 - C -- 4 - D -- 3 - C -- 1 - A -- 1 - A -- ','2010-10-10',7);
/*!40000 ALTER TABLE `hist_prova` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-20 12:41:12
