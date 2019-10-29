CREATE DATABASE IF NOT EXISTS minicurso;

CREATE TABLE `minicurso.pessoa`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'campo chave da tabela',
  `nome` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL COMMENT 'nome da pessoa',
  `sobrenome` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL COMMENT 'sobrenome da pessoa',
  PRIMARY KEY (`id`) USING BTREE
);