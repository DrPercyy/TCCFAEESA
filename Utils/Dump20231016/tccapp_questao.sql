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
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questao`
--

LOCK TABLES `questao` WRITE;
/*!40000 ALTER TABLE `questao` DISABLE KEYS */;
INSERT INTO `questao` VALUES (1,'Qual é a definição de algoritmo?',1,5,1),(2,'Qual é a principal diferença entre um algoritmo e um programa de computador?',1,5,1),(3,'O que é um loop em um algoritmo?',1,5,1),(4,'Imagine que você está projetando um sistema de recomendação para uma plataforma de streaming de música. Um algoritmo de recomendação é uma técnica complexa que envolve uma série de etapas, desde a coleta de dados até a implementação. Quais são as etapas fundamentais e como elas contribuem para a eficácia do sistema de recomendação?',1,5,1),(5,'Suponha que você esteja desenvolvendo um algoritmo de otimização para planejar a rota mais eficiente para a entrega de mercadorias em uma área urbana, quais são os desafios práticos, como congestionamento do tráfego e restrições de tempo, que você precisaria considerar ao criar um algoritmo de roteamento de entregas para o mundo real?',1,5,1),(6,'Em programação, o que é um vetor?',1,1,1),(7,'Qual é a principal diferença entre um vetor e uma matriz?',1,1,1),(8,'Em programação, como você acessa um elemento específico em um vetor?',1,1,1),(9,'Qual é a dimensão de uma matriz 3x4?',1,1,1),(10,'Qual é o principal propósito de um loop \"for\" em programação?',1,2,1),(11,'O que é um \"loop infinito\" em programação?',1,2,1),(12,'Qual é o objetivo da declaração \"break\" em um loop?',1,2,1),(13,'O que é um \"loop while\" em programação?',1,2,1),(14,'Qual é o principal propósito da estrutura condicional \"if\" em programação?',1,3,1),(15,'Em uma estrutura \"if-else\"  o que acontece se a condição no \"if\" for falsa?',1,3,1),(16,'Qual é a diferença entre \"if\" simples e \"if-else\" em uma estrutura condicional?',1,3,1),(17,'O que a estrutura condicional \"elif\" é usada para fazer?',1,3,1),(18,'Qual é a principal característica da linguagem Python?',1,4,1),(19,'Qual dos seguintes operadores é usado para realizar a multiplicação em Python?',1,4,1),(20,'Qual é a função da declaração if em Python?',1,4,1),(21,'O que é uma lista em Python?',1,4,1),(22,'Qual é um componente essencial da comunicação eficaz?',1,6,2),(23,'Qual é uma das principais diferenças entre comunicação verbal e comunicação não verbal?',1,6,2),(24,'Qual é um dos principais objetivos da escrita científica e técnica?',1,7,2),(25,'Qual é uma boa prática ao escrever um relatório técnico ou científico?',1,7,2),(26,'Quando se trata de comunicação profissional por e-mail, qual é uma diretriz importante a ser seguida?',1,7,2),(27,'Qual é o primeiro passo essencial ao iniciar uma pesquisa acadêmica?',1,8,2),(28,'O que é uma revisão bibliográfica em pesquisa acadêmica?',1,8,2),(29,'Qual das seguintes estratégias é uma técnica eficaz para melhorar a retenção de informações ao estudar?',1,9,2),(30,'Qual das seguintes estratégias é útil para melhorar o gerenciamento de tempo durante o estudo?',1,9,2),(31,'Qual é o resultado da operação lógica \"E\" (AND) quando ambas as proposições são verdadeiras?',1,10,3),(32,'Qual é o resultado da operação lógica \"OU\" (OR) quando pelo menos uma das proposições é verdadeira?',1,10,3),(33,'Qual é o resultado da operação lógica \"NÃO\" (NOT) quando a proposição original é verdadeira?',1,10,3),(34,'Qual é a equivalência tautológica que representa a Lei da Identidade na álgebra booleana?',1,11,3),(35,'Qual é a equivalência tautológica que representa a Lei da Dupla Negação na lógica proposicional?',1,11,3),(36,'Qual é a equivalência tautológica que representa a Lei da Comutatividade na álgebra booleana?',1,11,3),(37,'Adriana, Breno, Carolina e Danilo são funcionários de uma empresa, sendo que dois deles são médicos e os outros dois são advogados. Cada uma das idades dos advogados é maior do que cada uma das idades dos médicos. Considere as quatro afirmações:\nI. Breno e Carolina são ambos médicos ou um deles é advogado e o outro é médico. II. Danilo é mais velho do que Breno. III. Adriana é mais nova do que Danilo. IV. Adriana é mais velha do que Carolina.\nSabendo que duas das afirmações acima são verdadeiras e as outras duas são falsas, conclui-se, com certeza, que',1,12,3),(38,'Entre Maria, Natália, Olinda, Patrícia e Queila, apenas uma delas nasceu em Bento Gonçalves. Além disso, são verdadeiras as seguintes proposições:\nOu Maria nasceu em Bento Gonçalves, ou Queila não nasceu em Bento Gonçalves.  Natália nasceu em Bento Gonçalves se, e somente se, Olinda nasceu em Bento Gonçalves.\nLogo, é correto afirmar que quem nasceu em Bento Gonçalves foi ',1,12,3),(39,'O que representa a tabela verdade em lógica?',1,13,3),(40,'Quantas linhas uma tabela verdade deve ter para representar todas as combinações de valores lógicos para duas proposições?',1,13,3),(41,'O que representa o valor \"Falso\" (False) em uma tabela verdade?',1,13,3),(42,'O que é informação?',1,14,4),(43,'O que é um sistema de informação?',1,14,4),(44,'O que é a \"integridade da informação\"?',1,14,4),(45,'O que é Tecnologia da Informação (TI)?',1,15,4),(46,'Qual é o principal objetivo da gestão de TI em uma organização?',1,15,4),(47,'O que é um Data Center?\nResposta: D',1,15,4),(48,'O que é um Sistema de Informação de Negócio (SIN) em uma empresa?\nResposta: C\n–-\nQual é o objetivo principal de um Sistema de Informação de Negócio (SIN)?\nResposta: D\n–-\nComo um Sistema de Informação de Negócio (SIN) pode beneficiar uma organização?',1,16,4),(49,'O que é um Sistema de Informação Gerencial (SIG) em uma organização?',1,17,4),(50,'Qual é o papel dos sistemas de informação em uma organização?',1,17,4),(51,'O que é um Sistema de Informação Executiva (SIE) nas organizações?',1,17,4),(52,'O que é um disco rígido (HD) em um computador?',1,18,5),(53,'Qual das seguintes opções é um exemplo de armazenamento de dados em nuvem?',1,18,5),(54,'O que é plágio em relação à ética na computação?',1,19,5),(55,'Qual é um dos principais princípios éticos na programação de computadores?',1,19,5),(56,'O que significa \"diversidade\" no contexto da ética na computação?',1,19,5),(57,'O que é um arquivo no contexto de computação?',1,20,5),(58,'O que é a memória RAM (Random Access Memory) em um computador?',1,20,5),(59,'O que é a programação orientada a objetos?',1,20,5),(60,'O que é a manipulação de dados em um contexto de tecnologia da informação?',1,21,5),(61,'O que é uma \"chave primária\" em um banco de dados relacional?',1,21,5),(62,'Qual é a finalidade da linguagem SQL (Structured Query Language) em relação à manipulação de dados?',1,21,5);
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

-- Dump completed on 2023-10-16 11:45:32
