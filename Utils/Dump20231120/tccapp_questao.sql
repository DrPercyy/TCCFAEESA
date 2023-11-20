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
-- Table structure for table `questao`
--

DROP TABLE IF EXISTS `questao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questao` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `TEXTO_QUESTAO` mediumtext NOT NULL,
  `NIVEL_QUESTAO` int DEFAULT NULL,
  `CONTEUDO_ID` int NOT NULL,
  `DISCIPLINA_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_QUESTAO_CONTEUDO1_idx` (`CONTEUDO_ID`,`DISCIPLINA_ID`),
  CONSTRAINT `fk_QUESTAO_CONTEUDO1` FOREIGN KEY (`CONTEUDO_ID`, `DISCIPLINA_ID`) REFERENCES `conteudo` (`ID`, `DISCIPLINA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questao`
--

LOCK TABLES `questao` WRITE;
/*!40000 ALTER TABLE `questao` DISABLE KEYS */;
INSERT INTO `questao` VALUES (63,'Em programação, o que é um vetor?',1,1,1),(64,'Qual é a principal diferença entre um vetor e uma matriz?',1,1,1),(65,'Em programação, como você acessa um elemento específico em um vetor?',1,1,1),(66,'Qual é a dimensão de uma matriz 3x4?',1,1,1),(67,'Qual é o principal propósito de um loop \"for\" em programação?',1,2,1),(68,'O que é um \"loop infinito\" em programação?',1,2,1),(69,'Qual é o objetivo da declaração \"break\" em um loop?',1,2,1),(70,'O que é um \"loop while\" em programação?',1,2,1),(71,'Qual é o principal propósito da estrutura condicional \"if\" em programação?',1,3,1),(72,'Em uma estrutura \"if-else\"  o que acontece se a condição no \"if\" for falsa?',1,3,1),(73,'Qual é a diferença entre \"if\" simples e \"if-else\" em uma estrutura condicional?',1,3,1),(74,'O que a estrutura condicional \"elif\" é usada para fazer?',1,3,1),(75,'Qual é a principal característica da linguagem Python?',1,4,1),(76,'Qual dos seguintes operadores é usado para realizar a multiplicação em Python?',1,4,1),(77,'Qual é a função da declaração if em Python?',1,4,1),(78,'O que é uma lista em Python?',1,4,1),(79,'Qual é a definição de algoritmo?',1,5,1),(80,'Qual é a principal diferença entre um algoritmo e um programa de computador?',1,5,1),(81,'O que é um loop em um algoritmo?',1,5,1),(82,'Imagine que você está projetando um sistema de recomendação para uma plataforma de streaming de música. Um algoritmo de recomendação é uma técnica complexa que envolve uma série de etapas, desde a coleta de dados até a implementação. Quais são as etapas fundamentais e como elas contribuem para a eficácia do sistema de recomendação?',1,5,1),(83,'Suponha que você esteja desenvolvendo um algoritmo de otimização para planejar a rota mais eficiente para a entrega de mercadorias em uma área urbana, quais são os desafios práticos, como congestionamento do tráfego e restrições de tempo, que você precisaria considerar ao criar um algoritmo de roteamento de entregas para o mundo real?',1,5,1),(84,'Qual é um componente essencial da comunicação eficaz?',1,6,2),(85,'Qual é uma das principais diferenças entre comunicação verbal e comunicação não verbal?',1,6,2),(86,'Qual é um dos principais objetivos da escrita científica e técnica?',1,7,2),(87,'Qual é uma boa prática ao escrever um relatório técnico ou científico?',1,7,2),(88,'Quando se trata de comunicação profissional por e-mail, qual é uma diretriz importante a ser seguida?',1,7,2),(89,'',1,8,2),(90,'Qual das seguintes estratégias é uma técnica eficaz para melhorar a retenção de informações ao estudar?',1,9,2),(91,'Qual das seguintes estratégias é útil para melhorar o gerenciamento de tempo durante o estudo?',1,9,2),(92,'Qual é o resultado da operação lógica \"E\" (AND) quando ambas as proposições são verdadeiras?',1,10,3),(93,'Qual é o resultado da operação lógica \"OU\" (OR) quando pelo menos uma das proposições é verdadeira?',1,10,3),(94,'Qual é o resultado da operação lógica \"NÃO\" (NOT) quando a proposição original é verdadeira?',1,10,3),(95,'Qual é a equivalência tautológica que representa a Lei da Identidade na álgebra booleana?',1,11,3),(96,'Qual é a equivalência tautológica que representa a Lei da Dupla Negação na lógica proposicional?',1,11,3),(97,'Qual é a equivalência tautológica que representa a Lei da Comutatividade na álgebra booleana?',1,11,3),(98,'Adriana, Breno, Carolina e Danilo são funcionários de uma empresa, sendo que dois deles são médicos e os outros dois são advogados. Cada uma das idades dos advogados é maior do que cada uma das idades dos médicos. Considere as quatro afirmações:\n    I. Breno e Carolina são ambos médicos ou um deles é advogado e o outro é médico. \n    II. Danilo é mais velho do que Breno. III. Adriana é mais nova do que Danilo. \n    IV. Adriana é mais velha do que Carolina.\nSabendo que duas das afirmações acima são verdadeiras e as outras duas são falsas, conclui-se, com certeza, que',1,12,3),(99,'Entre Maria, Natália, Olinda, Patrícia e Queila, apenas uma delas nasceu em Bento Gonçalves. Além disso, são verdadeiras as seguintes proposições:\nOu Maria nasceu em Bento Gonçalves, ou Queila não nasceu em Bento Gonçalves.  Natália nasceu em Bento Gonçalves se, e somente se, Olinda nasceu em Bento Gonçalves.\nLogo, é correto afirmar que quem nasceu em Bento Gonçalves foi ',1,12,3),(100,'O que representa a tabela verdade em lógica?',1,13,3),(101,'Quantas linhas uma tabela verdade deve ter para representar todas as combinações de valores lógicos para duas proposições?',1,13,3),(102,'O que representa o valor \"Falso\" (False) em uma tabela verdade?',1,13,3),(103,'O que é informação?',1,14,4),(104,'O que é um sistema de informação?',1,14,4),(105,'O que é a \"integridade da informação\"?',1,14,4),(106,'O que é Tecnologia da Informação (TI)?',1,15,4),(107,'Qual é o principal objetivo da gestão de TI em uma organização?',1,15,4),(108,'O que é um Data Center?\nResposta: D',1,15,4),(109,'O que é um Sistema de Informação de Negócio (SIN) em uma empresa?',1,16,4),(110,'Qual é o objetivo principal de um Sistema de Informação de Negócio (SIN)?',1,16,4),(111,'Como um Sistema de Informação de Negócio (SIN) pode beneficiar uma organização?',1,16,4),(112,'O que é um Sistema de Informação Gerencial (SIG) em uma organização?',1,17,4),(113,'Qual é o papel dos sistemas de informação em uma organização?',1,17,4),(114,'O que é um Sistema de Informação Executiva (SIE) nas organizações?',1,17,4),(115,'O que é um disco rígido (HD) em um computador?',1,18,5),(116,'Qual das seguintes opções é um exemplo de armazenamento de dados em nuvem?',1,18,5),(117,'O que é plágio em relação à ética na computação?',1,19,5),(118,'Qual é um dos principais princípios éticos na programação de computadores?',1,19,5),(119,'O que significa \"diversidade\" no contexto da ética na computação?',1,19,5),(120,'O que é um arquivo no contexto de computação?',1,20,5),(121,'O que é a memória RAM (Random Access Memory) em um computador?',1,20,5),(122,'O que é a programação orientada a objetos?',1,20,5),(123,'O que é a manipulação de dados em um contexto de tecnologia da informação?',1,21,5),(124,'O que é uma \"chave primária\" em um banco de dados relacional?',1,21,5),(125,'Qual é a finalidade da linguagem SQL (Structured Query Language) em relação à manipulação de dados?',1,21,5);
/*!40000 ALTER TABLE `questao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-20 12:41:13
