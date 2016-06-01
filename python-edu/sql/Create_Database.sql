CREATE DATABASE `mydatabase` /*!40100 DEFAULT CHARACTER SET utf8 */;
CREATE TABLE `mydatabase`.`employees` (
  `id` MEDIUMINT NOT NULL AUTO_INCREMENT,
  `age` int(11) NOT NULL,
  `first` varchar(255) NOT NULL,
  `last` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;