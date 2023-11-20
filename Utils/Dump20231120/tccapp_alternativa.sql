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
-- Table structure for table `alternativa`
--

DROP TABLE IF EXISTS `alternativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alternativa` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ALTER_TEXTO` varchar(255) NOT NULL,
  `ALTER_CORR` tinyint(1) NOT NULL,
  `QUESTAO_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_ALTERNATIVA_QUESTAO1_idx` (`QUESTAO_ID`),
  CONSTRAINT `fk_ALTERNATIVA_QUESTAO1` FOREIGN KEY (`QUESTAO_ID`) REFERENCES `questao` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=631 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alternativa`
--

LOCK TABLES `alternativa` WRITE;
/*!40000 ALTER TABLE `alternativa` DISABLE KEYS */;
INSERT INTO `alternativa` VALUES (321,'Um tipo de dado usado apenas para armazenar números inteiros.',0,63),(322,'Uma variável que só pode conter caracteres de texto.',0,63),(323,'Uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo.',1,63),(324,'Uma função que calcula a média de um conjunto de números.',0,63),(325,'Um operador matemático.',0,63),(326,'Um vetor é unidimensional, enquanto uma matriz é bidimensional.',1,64),(327,'Um vetor pode armazenar diferentes tipos de dados, enquanto uma matriz não.',0,64),(328,'Um vetor é sempre mais eficiente do que uma matriz.',0,64),(329,'Um vetor pode conter apenas um elemento, enquanto uma matriz pode conter vários.',0,64),(330,'Vetores e matrizes são a mesma coisa em programação.',0,64),(331,'Usando a palavra-chave \"element\" seguida do índice desejado.',0,65),(332,'Utilizando a função \"get()\" com o índice como argumento.',0,65),(333,'Usando o operador \"()\" seguido do índice do elemento.',0,65),(334,'Utilizando o índice entre colchetes após o nome do vetor.',1,65),(335,'Apenas é possível acessar todos os elementos de uma vez.',0,65),(336,'Unidimensional.',0,66),(337,'Bidimensional.',1,66),(338,'Tridimensional.',0,66),(339,'Quadrilateral.',0,66),(340,'Hexagonal.',0,66),(341,'Realizar uma operação de divisão.',0,67),(342,'Executar um bloco de código repetidamente enquanto uma condição for verdadeira.',0,67),(343,'Tomar decisões com base em condições.',0,67),(344,'Criar uma lista de elementos.',1,67),(345,'Definir uma função.',0,67),(346,'Um loop que não tem condição de parada.',1,68),(347,'Um loop que executa apenas uma vez.',0,68),(348,'Um loop que nunca é executado.',0,68),(349,'Um loop que só pode ser usado em Python.',0,68),(350,'Um loop que não faz nada.',0,68),(351,'Encerrar o programa imediatamente.',0,69),(352,'Pular para o próximo loop \"for\".',0,69),(353,'Sair do loop imediatamente, interrompendo a repetição.',1,69),(354,'Ignorar completamente o loop.',0,69),(355,'Adicionar uma condição de repetição.',0,69),(356,'Um loop que não é mais usado em linguagens modernas.',0,70),(357,'Um loop que executa um número fixo de vezes.',0,70),(358,'Um loop que executa indefinidamente até que uma condição seja falsa.',0,70),(359,'Um loop que só pode ser usado em linguagens de baixo nível.',0,70),(360,'Um loop que inverte a ordem dos elementos em uma lista.',1,70),(361,'Executar um bloco de código repetidamente.',0,71),(362,'Realizar uma operação de multiplicação.',0,71),(363,'Tomar decisões com base em condições.',1,71),(364,'Criar uma lista de elementos.',0,71),(365,'Definir uma função.',0,71),(366,'O programa encerra a execução.',0,72),(367,'O programa pula para o próximo \"if\".',0,72),(368,'O bloco de código dentro do \"if\" é executado.',0,72),(369,'O bloco de código dentro do \"else\" é executado.',1,72),(370,'Nada acontece, o programa continua normalmente.',0,72),(371,'Não há diferença, ambos fazem a mesma coisa.',0,73),(372,'\"if\" simples só pode lidar com condições verdadeiras.',0,73),(373,'\"if-else\" pode lidar com múltiplas condições.',1,73),(374,'\"if\" simples é mais eficiente que \"if-else\".',0,73),(375,'\"if\" simples não é uma estrutura condicional válida em Python.',0,73),(376,'Encerrar o programa imediatamente.',0,74),(377,'Verificar a condição \"if\" em um loop.',0,74),(378,'Ignorar completamente a estrutura condicional.',0,74),(379,'Executar um bloco de código sem condição.',0,74),(380,'Lidar com múltiplas condições em sequência.',1,74),(381,'Linguagem de programação compilada.',0,75),(382,'Linguagem de programação orientada a objetos.',1,75),(383,'Linguagem de programação fortemente tipada.',0,75),(384,'Linguagem de programação de baixo nível.',0,75),(385,'Linguagem de programação baseada em lógica fuzzy.',0,75),(386,'+',0,76),(387,'-',0,76),(388,'*',1,76),(389,'/',0,76),(390,'%',0,76),(391,'Loop infinito.',0,77),(392,'Definir uma função.',0,77),(393,'Tomar decisões com base em condições.',1,77),(394,'Realizar operações aritméticas.',0,77),(395,'Imprimir valores na tela.',0,77),(396,'Um tipo de variável que só pode conter números inteiros.',0,78),(397,'Um tipo de estrutura de controle que repete um bloco de código.',0,78),(398,'Um tipo de dado que armazena valores em pares chave-valor.',0,78),(399,'Uma sequência ordenada de elementos que pode conter diversos tipos de dados.',1,78),(400,'Uma função embutida que calcula a raiz quadrada de um número.',0,78),(401,'Um programa de computador.',0,79),(402,'Um conjunto de instruções precisas para resolver um problema.',1,79),(403,'Um resultado de pesquisa na internet.',0,79),(404,'Um dispositivo de armazenamento de dados.',0,79),(405,'Um método de criptografia de dados.',0,79),(406,'Algoritmos só podem ser escritos em pseudocódigo.',0,80),(407,'Programas de computador não são usados na resolução de problemas.',0,80),(408,'Algoritmos são sempre mais eficientes que programas.',0,80),(409,'Algoritmos são abstrações de alto nível, enquanto programas são implementações concretas.',1,80),(410,'Algoritmos são puramente teóricos e não podem ser executados, enquanto programas de computador são implementações práticas dos algoritmos.',0,80),(411,'Uma estrutura de controle que repete um bloco de instruções enquanto uma condição é verdadeira.',1,81),(412,'Um erro de programação.',0,81),(413,'Um tipo de variável.',0,81),(414,'Uma função matemática.',0,81),(415,'Uma sequência de instruções que são executadas apenas uma vez, independentemente de qualquer condição.',0,81),(416,'Coleta de dados, treinamento de modelo, implementação do sistema.',1,82),(417,'Coleta de dados, análise de dados, desenvolvimento do aplicativo.',0,82),(418,'Coleta de dados, entrega de música, interação do usuário.',0,82),(419,'Coleta de dados, reprodução de música, feedbacks do usuário.',0,82),(420,'Coleta de dados, desenvolvimento do aplicativo, feedback.',0,82),(421,'Os desafios práticos não afetam a otimização do roteamento de entregas.',0,83),(422,'Os desafios práticos podem ser ignorados em favor da simplicidade.',0,83),(423,'Os desafios práticos, como o tráfego, são fatores críticos a serem considerados na otimização do roteamento de entregas.',1,83),(424,'Os desafios práticos só afetam algoritmos de roteamento em áreas rurais.',0,83),(425,'Os desafios práticos, como o tráfego e as restrições de tempo, são irrelevantes para algoritmos de roteamento de entregas, pois os algoritmos são capazes de criar rotas perfeitas independentemente das condições do mundo real.',0,83),(426,'Falar rapidamente para transmitir mais informações.',0,84),(427,'Usar terminologia técnica e jargões para impressionar o público.',0,84),(428,'Ignorar as reações e o feedback do interlocutor.',0,84),(429,'Ser claro e ouvir atentamente o interlocutor.',0,84),(430,'Falar apenas sobre tópicos pessoais durante a conversa.',1,84),(431,'Comunicação verbal envolve o uso de gestos e expressões faciais.',1,85),(432,'A comunicação não verbal é exclusivamente baseada em palavras faladas.',0,85),(433,'A comunicação verbal é mais eficaz para transmitir emoções.',0,85),(434,'Comunicação não verbal não envolve contato visual.',0,85),(435,'A comunicação verbal é mais rápida do que a comunicação não verbal.',0,85),(436,'Entreter o leitor com histórias interessantes.',0,86),(437,'Compartilhar opiniões pessoais e crenças.',0,86),(438,'Comunicar informações de forma clara e precisa.',1,86),(439,'Usar uma linguagem rebuscada e complexa para impressionar o leitor.',0,86),(440,'Evitar referências e citações para manter a originalidade.',0,86),(441,'Usar jargões técnicos complexos para mostrar expertise.',0,87),(442,'Evitar a revisão e edição do documento antes da publicação.',0,87),(443,'Incluir opiniões pessoais e conjecturas.',0,87),(444,'Organizar o conteúdo de forma lógica e estruturada.',1,87),(445,'Adicionar imagens e gráficos sem contexto.',0,87),(446,'Usar gírias e abreviações informais.',0,88),(447,'Ignorar as respostas rápidas para manter a formalidade.',0,88),(448,'Incluir anexos grandes em todos os e-mails.',0,88),(449,'Ser conciso e claro em sua comunicação.',1,88),(450,'Enviar e-mails apenas durante horário comercial.',0,88),(451,'Ler rapidamente todos os tópicos sem se concentrar em nenhum.',0,90),(452,'Cramming (estudar intensivamente) todas as informações na noite anterior ao exame.',0,90),(453,'Fazer anotações detalhadas e resumos durante o estudo.',1,90),(454,'Ignorar completamente os exercícios práticos e exemplos.',0,90),(455,'Estudar em um ambiente barulhento e com distrações.',0,90),(456,'Estudar durante longos períodos de tempo sem pausas.',0,91),(457,'Ignorar o planejamento e estudar apenas quando sentir vontade.',0,91),(458,'Usar um cronômetro para dividir o estudo em sessões de tempo definidas.',1,91),(459,'Multitarefa, como assistir a um vídeo enquanto estuda.',0,91),(460,'Evitar definir metas de estudo ou prazos.',0,91),(461,'Verdadeiro',1,92),(462,'Falso',0,92),(463,'Indefinido',0,92),(464,'Alternativo',0,92),(465,'Inverso',0,92),(466,'Verdadeiro',1,93),(467,'Falso',0,93),(468,'Indefinido',0,93),(469,'Exclusivo',0,93),(470,'Inverso',0,93),(471,'Verdadeiro',0,94),(472,'Falso',1,94),(473,'Indefinido',0,94),(474,'Contraditório',0,94),(475,'Inverso',0,94),(476,'¬p ∧ p ≡ F',0,95),(477,'p ∨ (¬p) ≡ T',0,95),(478,'¬p ∨ p ≡ T',0,95),(479,'p ∧ (¬p) ≡ F',0,95),(480,'(p ∨ q) ∨ r ≡ p ∨ (q ∨ r)',1,95),(481,'p ≡ ¬(¬p)',1,96),(482,'p ≡ ¬p',0,96),(483,'¬p ≡ ¬(¬p)',0,96),(484,'p ≡ (¬p)',0,96),(485,'¬p ≡ (¬¬p)',0,96),(486,'p ∨ q ≡ q ∨ p',1,97),(487,'p ∨ (q ∨ r) ≡ (p ∨ q) ∨ r',0,97),(488,'p ∨ p ≡ p',0,97),(489,'p ∧ (q ∨ r) ≡ (p ∧ q) ∨ r',0,97),(490,'¬(p ∧ q) ≡ ¬p ∧ ¬q',0,97),(491,'Breno e Carolina são um deles médico e o outro advogado. ',1,98),(492,'Breno e Carolina são ambos médicos. ',0,98),(493,'Breno e Carolina são ambos advogados. ',0,98),(494,' Danilo é mais velho do que Carolina.',0,98),(495,'Danilo é mais novo do que Breno.',0,98),(496,'Maria',0,99),(497,'Natália.',0,99),(498,'Olinda.',0,99),(499,'Patrícia.',1,99),(500,'Queila',0,99),(501,'Uma lista de proposições que não têm valor lógico definido.',0,100),(502,'Um método para criar argumentos inválidos.',0,100),(503,'Uma representação visual das operações lógicas entre proposições.',0,100),(504,'Uma tabela de valores lógicos que mostra todas as combinações possíveis de valores para proposições.',1,100),(505,'Uma lista de falácias lógicas comuns.',0,100),(506,'1',0,101),(507,'2',0,101),(508,'3',0,101),(509,'4',1,101),(510,'5',0,101),(511,'A proposição é verdadeira.',0,102),(512,'A proposição é falsa.',1,102),(513,'A proposição é indefinida.',0,102),(514,'A proposição é uma tautologia.',0,102),(515,'A proposição é contraditória.',0,102),(516,'Dados brutos sem significado.',0,103),(517,'Um conjunto de números aleatórios.',0,103),(518,'Conhecimento e dados organizados de forma significativa.',1,103),(519,'Informações sigilosas que não podem ser compartilhadas.',0,103),(520,'Um tipo de linguagem de programação.',0,103),(521,'Um software de edição de texto.',0,104),(522,'Uma rede social popular.',0,104),(523,'Uma ferramenta para armazenar dados sem processamento.',0,104),(524,'Um conjunto de componentes inter-relacionados que coletam, processam, armazenam e distribuem informações.',1,104),(525,'Uma unidade de processamento central em um computador.',0,104),(526,'A capacidade de uma informação ser acessada por qualquer pessoa a qualquer momento.',0,105),(527,'A qualidade da informação, garantindo que ela seja precisa e confiável.',0,105),(528,'A velocidade com que a informação é transmitida pela internet.',0,105),(529,'A quantidade de informações disponíveis em um sistema.',0,105),(530,'A complexidade das informações em um banco de dados.',1,105),(531,'Um programa de televisão sobre inovações tecnológicas.',0,106),(532,'A disciplina que estuda a história da informação.',0,106),(533,'Um conjunto de práticas e tecnologias usadas para gerenciar informações e processos.',1,106),(534,'Um método para criar arte digital.',0,106),(535,'Um tipo de linguagem de programação.',0,106),(536,'Aumentar o consumo de recursos de computação.',0,107),(537,'Reduzir a complexidade dos sistemas de informação.',0,107),(538,'Garantir a conformidade com leis de direitos autorais.',0,107),(539,'Maximizar o valor dos recursos de TI para atender às metas de negócios.',1,107),(540,'Desenvolver software personalizado para cada funcionário.',0,107),(541,'Um dispositivo de armazenamento de dados pessoais.',0,108),(542,'Um tipo de laptop.',0,108),(543,'Um centro de treinamento para profissionais de TI.',0,108),(544,'Uma instalação que abriga servidores e equipamentos de rede para armazenar, processar e gerenciar dados e aplicativos.',0,108),(545,'Um local para reciclagem de eletrônicos.',1,108),(546,'Um software de entretenimento para funcionários.',0,109),(547,'Um sistema de segurança de rede.',0,109),(548,'Um sistema que auxilia na coleta, armazenamento, processamento e distribuição de informações relacionadas aos processos de negócios.',1,109),(549,'Um sistema de transporte de mercadorias.',0,109),(550,'Um sistema de gerenciamento de recursos humanos.',0,109),(551,'Substituir completamente os funcionários da empresa.',0,110),(552,'Aumentar o entretenimento no local de trabalho.',0,110),(553,'Melhorar a segurança cibernética da organização.',0,110),(554,'Apoiar e otimizar as operações e processos de negócios.',1,110),(555,'Automatizar todas as tarefas administrativas.',0,110),(556,'Aumentando os custos operacionais.',0,111),(557,'Tornando os processos mais complexos.',0,111),(558,'Reduzindo a eficiência dos funcionários.',0,111),(559,'Melhorando a tomada de decisões, proporcionando acesso a informações em tempo real e ajudando na automação de tarefas.',1,111),(560,'Aumentando o tempo de inatividade dos sistemas de TI.',0,111),(561,'Um conjunto de regras e regulamentos internos.',0,112),(562,'Um sistema de segurança cibernética.',0,112),(563,'Um software de contabilidade.',0,112),(564,'Um sistema que fornece informações estruturadas para apoiar o processo de tomada de decisão.',1,112),(565,'Um sistema de gerenciamento de projetos.',0,112),(566,'Gerenciar pessoal e recursos humanos.',0,113),(567,'Automatizar todas as tarefas operacionais.',0,113),(568,'Coletar, armazenar, processar e distribuir informações relevantes para o funcionamento da organização.',1,113),(569,'Fornecer entretenimento para os funcionários.',0,113),(570,'Substituir completamente a necessidade de funcionários.',0,113),(571,'Um sistema de segurança de dados.',0,114),(572,'Um sistema de gerenciamento de projetos.',0,114),(573,'Um sistema de videoconferência.',0,114),(574,'Um sistema que fornece informações de nível estratégico para auxiliar na tomada de decisões de alto nível.',1,114),(575,'Um sistema de contabilidade.',0,114),(576,'Uma unidade de processamento central.',0,115),(577,'Um dispositivo de entrada de dados.',0,115),(578,'Uma unidade de armazenamento de dados não volátil que utiliza discos magnéticos para armazenar informações.',1,115),(579,'Um dispositivo de saída de dados.',0,115),(580,'Uma memória RAM.',0,115),(581,'Disco rígido externo.',0,116),(582,'Pen drive USB.',0,116),(583,'Servidor local.',0,116),(584,'Google Drive.',1,116),(585,'DVD virgem.',0,116),(586,'O ato de compartilhar abertamente o código-fonte de software.',0,117),(587,'A prática de copiar informações de uma fonte sem dar crédito adequado.',1,117),(588,'Aqueles que contribuem para projetos de código aberto.',0,117),(589,'A promoção de software proprietário.',0,117),(590,'O uso de recursos de TI no trabalho.',0,117),(591,'Manter segredo sobre todas as descobertas e inovações.',0,118),(592,'Evitar a colaboração com outros desenvolvedores.',0,118),(593,'Priorizar a velocidade de desenvolvimento sobre a qualidade do código.',0,118),(594,'Ser honesto e transparente sobre erros e vulnerabilidades de software.',1,118),(595,'Não documentar o código para manter a exclusividade.',0,118),(596,'A exclusão de diferentes perspectivas no desenvolvimento de software.',0,119),(597,'A criação de algoritmos que discriminam grupos específicos de pessoas.',0,119),(598,'A promoção de ambientes de trabalho inclusivos que valorizam as diferenças individuais.',1,119),(599,'A manutenção de sistemas de TI obsoletos.',0,119),(600,'A restrição do acesso à tecnologia apenas para grupos privilegiados.',0,119),(601,'Uma unidade de armazenamento de dados dentro do processador.',0,120),(602,'Um dispositivo de entrada de dados, como um teclado.',0,120),(603,'Um conjunto de instruções para um programa de computador.',0,120),(604,'Uma unidade organizacional em um sistema operacional.',0,120),(605,'Uma coleção de dados armazenados em um meio de armazenamento, como um disco rígido.',1,120),(606,'Uma unidade de armazenamento permanente para dados.',0,121),(607,'Um dispositivo de entrada para informações digitais.',0,121),(608,'Uma parte do processador que executa cálculos complexos.',0,121),(609,'Uma memória temporária que armazena dados enquanto o computador está ligado.',1,121),(610,'Uma unidade de processamento gráfico.',0,121),(611,'Uma técnica para criar programas sem a necessidade de código.',0,122),(612,'Um método de programação que não usa estruturas de controle.',0,122),(613,'Um paradigma de programação que se baseia na criação de objetos que podem interagir entre si.',1,122),(614,'Uma forma de programação que não requer linguagens de programação.',0,122),(615,'Um tipo de programação usada apenas em jogos de computador.',0,122),(616,'Um método para ocultar dados importantes.',0,123),(617,'Uma técnica para excluir permanentemente dados de um dispositivo.',0,123),(618,'O processo de coleta, organização, processamento e transformação de informações.',1,123),(619,'A codificação de dados em linguagem de programação.',0,123),(620,'A transferência de dados de um dispositivo para outro.',0,123),(621,'Um código de acesso para abrir o banco de dados.',0,124),(622,'Uma senha exclusiva para o administrador do banco de dados.',0,124),(623,'Um valor único que identifica cada registro em uma tabela.',1,124),(624,'Um campo que armazena informações confidenciais.',0,124),(625,'Uma função que calcula a média dos dados em uma tabela.',0,124),(626,'Armazenar arquivos em um servidor web.',0,125),(627,'Desenvolver aplicativos móveis.',0,125),(628,'Criar gráficos e visualizações de dados.',0,125),(629,'Consultar, atualizar e gerenciar bancos de dados relacionais.',1,125),(630,'Criar páginas da web dinâmicas.',0,125);
/*!40000 ALTER TABLE `alternativa` ENABLE KEYS */;
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
