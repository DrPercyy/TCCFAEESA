#insert into DISCIPLINA (NOME_DISCIPLINA)
#values('disci_test');

#insert into CONTEUDO (NOME_CONTEUDO, DISCIPLINA_ID)
#values('cont_test', 1);

#INSERT INTO QUESTAO (TEXTO_QUESTAO, NIVEL_QUESTAO, CONTEUDO_ID)
#VALUES ('A capital da França é Paris', 1,1);

#insert into alternativa (QUESTAO_ID,ALTER_TEXTO,ALTER_CORR)
#values(1,'Verdadeiro',1);
#insert into alternativa (QUESTAO_ID,ALTER_TEXTO,ALTER_CORR)
#values(1,'Falso',0);

delete from alternativa;
delete from questao;
delete from conteudo;
delete from disciplina;
delete from curso;

ALTER TABLE alternativa AUTO_INCREMENT=0;
ALTER TABLE questao AUTO_INCREMENT=0;
ALTER TABLE conteudo AUTO_INCREMENT=0;
ALTER TABLE disciplina AUTO_INCREMENT=0;
ALTER TABLE curso AUTO_INCREMENT=0;

commit;


