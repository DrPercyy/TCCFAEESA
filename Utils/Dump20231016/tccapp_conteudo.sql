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
-- Table structure for table `conteudo`
--

DROP TABLE IF EXISTS `conteudo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conteudo` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NOME_CONTEUDO` varchar(45) NOT NULL,
  `DISCIPLINA_ID` int NOT NULL,
  PRIMARY KEY (`ID`,`DISCIPLINA_ID`),
  KEY `fk_CONTEUDO_DISCIPLINA1_idx` (`DISCIPLINA_ID`),
  CONSTRAINT `fk_CONTEUDO_DISCIPLINA1` FOREIGN KEY (`DISCIPLINA_ID`) REFERENCES `disciplina` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conteudo`
--

LOCK TABLES `conteudo` WRITE;
/*!40000 ALTER TABLE `conteudo` DISABLE KEYS */;
INSERT INTO `conteudo` VALUES (1,'Arranjos',1),(2,'Estruturas de Repetição',1),(3,'Estruturas de Seleção',1),(4,'Introdução a Linguagem Python',1),(5,'Introdução ao Algoritmo',1),(6,'Comunicação',2),(7,'Escrita Ciêntifica, Técnica e Profissional',2),(8,'Pesquisas Academicas',2),(9,'Técnicas de Estudo',2),(10,'Conectivos Lógicos',3),(11,'Equivalencias Tautológicas',3),(12,'Lógica',3),(13,'Tabela Verdade',3),(14,'Conceitos de Informação e Sistemas',4),(15,'Conceitos de Tecnologia da Informação',4),(16,'Sistemas de Informação de Negócio',4),(17,'Sistemas de Informação nas Organizaçôes',4),(18,'Armazenamento de Dados',5),(19,'Etica na Computação',5),(20,'Imersão no Universo computacional',5),(21,'Manipulação de Dados',5);
/*!40000 ALTER TABLE `conteudo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-16 11:45:32
