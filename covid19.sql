-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3308
-- Généré le :  lun. 12 avr. 2021 à 19:07
-- Version du serveur :  8.0.18
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `covid19`
--

-- --------------------------------------------------------

--
-- Structure de la table `cas`
--

DROP TABLE IF EXISTS `cas`;
CREATE TABLE IF NOT EXISTS `cas` (
  `idcas` int(11) NOT NULL,
  `nbCas` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `cas`
--

INSERT INTO `cas` (`idcas`, `nbCas`) VALUES
(1, '12'),
(2, '12');

-- --------------------------------------------------------

--
-- Structure de la table `commune`
--

DROP TABLE IF EXISTS `commune`;
CREATE TABLE IF NOT EXISTS `commune` (
  `idCommune` int(11) NOT NULL,
  `nomCommune` varchar(45) DEFAULT NULL,
  `Departement_idDepartement` int(11) NOT NULL,
  PRIMARY KEY (`idCommune`),
  KEY `fk_Commune_Departement_idx` (`Departement_idDepartement`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `departement`
--

DROP TABLE IF EXISTS `departement`;
CREATE TABLE IF NOT EXISTS `departement` (
  `idDepartement` int(11) NOT NULL,
  `nomDepartement` varchar(45) DEFAULT NULL,
  `population` varchar(45) DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT NULL,
  `longitude` decimal(11,8) DEFAULT NULL,
  `Region_idRegion` int(11) NOT NULL,
  PRIMARY KEY (`idDepartement`),
  KEY `fk_Departement_Region1_idx` (`Region_idRegion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `departement_has_etat`
--

DROP TABLE IF EXISTS `departement_has_etat`;
CREATE TABLE IF NOT EXISTS `departement_has_etat` (
  `Departement_idDepartement` int(11) NOT NULL,
  `Etat_idEtat` int(11) NOT NULL,
  `Etat_Date` datetime NOT NULL,
  PRIMARY KEY (`Departement_idDepartement`,`Etat_idEtat`,`Etat_Date`),
  KEY `fk_Departement_has_Etat_Etat1_idx` (`Etat_idEtat`,`Etat_Date`),
  KEY `fk_Departement_has_Etat_Departement1_idx` (`Departement_idDepartement`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `etat`
--

DROP TABLE IF EXISTS `etat`;
CREATE TABLE IF NOT EXISTS `etat` (
  `idEtat` int(11) NOT NULL,
  `Date` datetime NOT NULL,
  `nbCasContact` int(11) DEFAULT NULL,
  `nbCasCom` int(11) DEFAULT NULL,
  `nbCasImp` int(11) DEFAULT NULL,
  PRIMARY KEY (`idEtat`,`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `etat`
--

INSERT INTO `etat` (`idEtat`, `Date`, `nbCasContact`, `nbCasCom`, `nbCasImp`) VALUES
(1, '2000-04-24 00:00:00', 424, 424, 0),
(2, '2000-04-24 00:00:00', 424, 424, 0);

-- --------------------------------------------------------

--
-- Structure de la table `region`
--

DROP TABLE IF EXISTS `region`;
CREATE TABLE IF NOT EXISTS `region` (
  `idRegion` int(11) NOT NULL,
  `nomRegion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idRegion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `region`
--

INSERT INTO `region` (`idRegion`, `nomRegion`) VALUES
(1, 'Dakar'),
(2, 'Thies');

-- --------------------------------------------------------

--
-- Structure de la table `region_has_etat`
--

DROP TABLE IF EXISTS `region_has_etat`;
CREATE TABLE IF NOT EXISTS `region_has_etat` (
  `Region_idRegion` int(11) NOT NULL,
  `Etat_idEtat` int(11) NOT NULL,
  `Etat_Date` datetime NOT NULL,
  PRIMARY KEY (`Region_idRegion`,`Etat_idEtat`,`Etat_Date`),
  KEY `fk_Region_has_Etat_Etat1_idx` (`Etat_idEtat`,`Etat_Date`),
  KEY `fk_Region_has_Etat_Region1_idx` (`Region_idRegion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `commune`
--
ALTER TABLE `commune`
  ADD CONSTRAINT `fk_Commune_Departement` FOREIGN KEY (`Departement_idDepartement`) REFERENCES `departement` (`idDepartement`);

--
-- Contraintes pour la table `departement`
--
ALTER TABLE `departement`
  ADD CONSTRAINT `fk_Departement_Region1` FOREIGN KEY (`Region_idRegion`) REFERENCES `region` (`idRegion`);

--
-- Contraintes pour la table `departement_has_etat`
--
ALTER TABLE `departement_has_etat`
  ADD CONSTRAINT `fk_Departement_has_Etat_Departement1` FOREIGN KEY (`Departement_idDepartement`) REFERENCES `departement` (`idDepartement`),
  ADD CONSTRAINT `fk_Departement_has_Etat_Etat1` FOREIGN KEY (`Etat_idEtat`,`Etat_Date`) REFERENCES `etat` (`idEtat`, `Date`);

--
-- Contraintes pour la table `region_has_etat`
--
ALTER TABLE `region_has_etat`
  ADD CONSTRAINT `fk_Region_has_Etat_Etat1` FOREIGN KEY (`Etat_idEtat`,`Etat_Date`) REFERENCES `etat` (`idEtat`, `Date`),
  ADD CONSTRAINT `fk_Region_has_Etat_Region1` FOREIGN KEY (`Region_idRegion`) REFERENCES `region` (`idRegion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
