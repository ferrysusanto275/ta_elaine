-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for elaine_ta
DROP DATABASE IF EXISTS `elaine_ta`;
CREATE DATABASE IF NOT EXISTS `elaine_ta` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `elaine_ta`;

-- Dumping structure for view elaine_ta.all_isi
DROP VIEW IF EXISTS `all_isi`;
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `all_isi` (
	`id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`tp_id` VARCHAR(45) NULL COLLATE 'latin1_swedish_ci',
	`tp_nama` VARCHAR(255) NULL COLLATE 'latin1_swedish_ci',
	`x` DECIMAL(11,2) NULL,
	`y` DECIMAL(11,2) NULL,
	`year` YEAR NOT NULL,
	`i1` DECIMAL(11,2) NOT NULL,
	`bobot_i1` DECIMAL(11,2) NULL,
	`i2` DECIMAL(11,2) NULL,
	`bobot_i2` DECIMAL(11,2) NULL,
	`i3` DECIMAL(11,2) NULL,
	`bobot_i3` DECIMAL(11,2) NULL,
	`i4` DECIMAL(11,2) NULL,
	`bobot_i4` DECIMAL(11,2) NULL,
	`i5` DECIMAL(11,2) NULL,
	`bobot_i5` DECIMAL(11,2) NULL,
	`i6` DECIMAL(11,2) NULL,
	`bobot_i6` DECIMAL(11,2) NULL,
	`i7` DECIMAL(11,2) NULL,
	`bobot_i7` DECIMAL(11,2) NULL,
	`i8` DECIMAL(11,2) NULL,
	`bobot_i8` DECIMAL(11,2) NULL,
	`i9` DECIMAL(11,2) NULL,
	`bobot_i9` DECIMAL(11,2) NULL,
	`i10` DECIMAL(11,2) NULL,
	`bobot_i10` DECIMAL(11,2) NULL,
	`i11` DECIMAL(11,2) NULL,
	`bobot_i11` DECIMAL(11,2) NULL,
	`i12` DECIMAL(11,2) NULL,
	`bobot_i12` DECIMAL(11,2) NULL,
	`i13` DECIMAL(11,2) NULL,
	`bobot_i13` DECIMAL(11,2) NULL,
	`i14` DECIMAL(11,2) NULL,
	`bobot_i14` DECIMAL(11,2) NULL,
	`i15` DECIMAL(11,2) NULL,
	`bobot_i15` DECIMAL(11,2) NULL,
	`i16` DECIMAL(11,2) NULL,
	`bobot_i16` DECIMAL(11,2) NULL,
	`i17` DECIMAL(11,2) NULL,
	`bobot_i17` DECIMAL(11,2) NULL,
	`i18` DECIMAL(11,2) NULL,
	`bobot_i18` DECIMAL(11,2) NULL,
	`i19` DECIMAL(11,2) NULL,
	`bobot_i19` DECIMAL(11,2) NULL,
	`i20` DECIMAL(11,2) NULL,
	`bobot_i20` DECIMAL(11,2) NULL,
	`i21` DECIMAL(11,2) NULL,
	`bobot_i21` DECIMAL(11,2) NULL,
	`i22` DECIMAL(11,2) NULL,
	`bobot_i22` DECIMAL(11,2) NULL,
	`i23` DECIMAL(11,2) NULL,
	`bobot_i23` DECIMAL(11,2) NULL,
	`i24` DECIMAL(11,2) NULL,
	`bobot_i24` DECIMAL(11,2) NULL,
	`i25` DECIMAL(11,2) NULL,
	`bobot_i25` DECIMAL(11,2) NULL,
	`i26` DECIMAL(11,2) NULL,
	`bobot_i26` DECIMAL(11,2) NULL,
	`i27` DECIMAL(11,2) NULL,
	`bobot_i27` DECIMAL(11,2) NULL,
	`i28` DECIMAL(11,2) NULL,
	`bobot_i28` DECIMAL(11,2) NULL,
	`i29` DECIMAL(11,2) NULL,
	`bobot_i29` DECIMAL(11,2) NULL,
	`i30` DECIMAL(11,2) NULL,
	`bobot_i30` DECIMAL(11,2) NULL,
	`i31` DECIMAL(11,2) NULL,
	`bobot_i31` DECIMAL(11,2) NULL,
	`i32` DECIMAL(11,2) NULL,
	`bobot_i32` DECIMAL(11,2) NULL,
	`i33` DECIMAL(11,2) NULL,
	`bobot_i33` DECIMAL(11,2) NULL,
	`i34` DECIMAL(11,2) NULL,
	`bobot_i34` DECIMAL(11,2) NULL,
	`i35` DECIMAL(11,2) NULL,
	`bobot_i35` DECIMAL(11,2) NULL,
	`i36` DECIMAL(11,2) NULL,
	`bobot_i36` DECIMAL(11,2) NULL,
	`i37` DECIMAL(11,2) NULL,
	`bobot_i37` DECIMAL(11,2) NULL,
	`i38` DECIMAL(11,2) NULL,
	`bobot_i38` DECIMAL(11,2) NULL,
	`i39` DECIMAL(11,2) NULL,
	`bobot_i39` DECIMAL(11,2) NULL,
	`i40` DECIMAL(11,2) NULL,
	`bobot_i40` DECIMAL(11,2) NULL,
	`i41` DECIMAL(11,2) NULL,
	`bobot_i41` DECIMAL(11,2) NULL,
	`i42` DECIMAL(11,2) NULL,
	`bobot_i42` DECIMAL(11,2) NULL,
	`i43` DECIMAL(11,2) NULL,
	`bobot_i43` DECIMAL(11,2) NULL,
	`i44` DECIMAL(11,2) NULL,
	`bobot_i44` DECIMAL(11,2) NULL,
	`i45` DECIMAL(11,2) NULL,
	`bobot_i45` DECIMAL(11,2) NULL,
	`i46` DECIMAL(11,2) NULL,
	`bobot_i46` DECIMAL(11,2) NULL,
	`i47` DECIMAL(11,2) NULL,
	`bobot_i47` DECIMAL(11,2) NULL,
	`bobot_aspek1` DECIMAL(11,2) NULL,
	`bobot_aspek2` DECIMAL(11,2) NULL,
	`bobot_aspek3` DECIMAL(11,2) NULL,
	`bobot_aspek4` DECIMAL(11,2) NULL,
	`bobot_aspek5` DECIMAL(11,2) NULL,
	`bobot_aspek6` DECIMAL(11,2) NULL,
	`bobot_aspek7` DECIMAL(11,2) NULL,
	`bobot_aspek8` DECIMAL(11,2) NULL,
	`bobot_domain1` DECIMAL(11,2) NULL,
	`bobot_domain2` DECIMAL(11,2) NULL,
	`bobot_domain3` DECIMAL(11,2) NULL,
	`bobot_domain4` DECIMAL(11,2) NULL
) ENGINE=MyISAM;

-- Dumping structure for table elaine_ta.analisis
DROP TABLE IF EXISTS `analisis`;
CREATE TABLE IF NOT EXISTS `analisis` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `penanggung_jawab` varchar(255) NOT NULL,
  `target_tahun` varchar(45) NOT NULL,
  `grup` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.analisis_grup
DROP TABLE IF EXISTS `analisis_grup`;
CREATE TABLE IF NOT EXISTS `analisis_grup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `grup` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.analisis_indikator
DROP TABLE IF EXISTS `analisis_indikator`;
CREATE TABLE IF NOT EXISTS `analisis_indikator` (
  `analisis` int NOT NULL,
  `indikator` varchar(45) NOT NULL,
  PRIMARY KEY (`analisis`,`indikator`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.analisis_instansi
DROP TABLE IF EXISTS `analisis_instansi`;
CREATE TABLE IF NOT EXISTS `analisis_instansi` (
  `analisis` int NOT NULL,
  `instansi` varchar(45) NOT NULL,
  PRIMARY KEY (`analisis`,`instansi`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.area
DROP TABLE IF EXISTS `area`;
CREATE TABLE IF NOT EXISTS `area` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.aspek
DROP TABLE IF EXISTS `aspek`;
CREATE TABLE IF NOT EXISTS `aspek` (
  `id` varchar(25) NOT NULL,
  `domain` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `bobot` decimal(11,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view elaine_ta.aspek_isi
DROP VIEW IF EXISTS `aspek_isi`;
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `aspek_isi` (
	`id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`tp_id` VARCHAR(45) NULL COLLATE 'latin1_swedish_ci',
	`tp_nama` VARCHAR(255) NULL COLLATE 'latin1_swedish_ci',
	`x` DECIMAL(11,2) NULL,
	`y` DECIMAL(11,2) NULL,
	`year` YEAR NOT NULL,
	`i1` DECIMAL(11,2) NOT NULL,
	`bobot_i1` DECIMAL(11,2) NULL,
	`i2` DECIMAL(11,2) NULL,
	`bobot_i2` DECIMAL(11,2) NULL,
	`i3` DECIMAL(11,2) NULL,
	`bobot_i3` DECIMAL(11,2) NULL,
	`i4` DECIMAL(11,2) NULL,
	`bobot_i4` DECIMAL(11,2) NULL,
	`i5` DECIMAL(11,2) NULL,
	`bobot_i5` DECIMAL(11,2) NULL,
	`i6` DECIMAL(11,2) NULL,
	`bobot_i6` DECIMAL(11,2) NULL,
	`i7` DECIMAL(11,2) NULL,
	`bobot_i7` DECIMAL(11,2) NULL,
	`i8` DECIMAL(11,2) NULL,
	`bobot_i8` DECIMAL(11,2) NULL,
	`i9` DECIMAL(11,2) NULL,
	`bobot_i9` DECIMAL(11,2) NULL,
	`i10` DECIMAL(11,2) NULL,
	`bobot_i10` DECIMAL(11,2) NULL,
	`i11` DECIMAL(11,2) NULL,
	`bobot_i11` DECIMAL(11,2) NULL,
	`i12` DECIMAL(11,2) NULL,
	`bobot_i12` DECIMAL(11,2) NULL,
	`i13` DECIMAL(11,2) NULL,
	`bobot_i13` DECIMAL(11,2) NULL,
	`i14` DECIMAL(11,2) NULL,
	`bobot_i14` DECIMAL(11,2) NULL,
	`i15` DECIMAL(11,2) NULL,
	`bobot_i15` DECIMAL(11,2) NULL,
	`i16` DECIMAL(11,2) NULL,
	`bobot_i16` DECIMAL(11,2) NULL,
	`i17` DECIMAL(11,2) NULL,
	`bobot_i17` DECIMAL(11,2) NULL,
	`i18` DECIMAL(11,2) NULL,
	`bobot_i18` DECIMAL(11,2) NULL,
	`i19` DECIMAL(11,2) NULL,
	`bobot_i19` DECIMAL(11,2) NULL,
	`i20` DECIMAL(11,2) NULL,
	`bobot_i20` DECIMAL(11,2) NULL,
	`i21` DECIMAL(11,2) NULL,
	`bobot_i21` DECIMAL(11,2) NULL,
	`i22` DECIMAL(11,2) NULL,
	`bobot_i22` DECIMAL(11,2) NULL,
	`i23` DECIMAL(11,2) NULL,
	`bobot_i23` DECIMAL(11,2) NULL,
	`i24` DECIMAL(11,2) NULL,
	`bobot_i24` DECIMAL(11,2) NULL,
	`i25` DECIMAL(11,2) NULL,
	`bobot_i25` DECIMAL(11,2) NULL,
	`i26` DECIMAL(11,2) NULL,
	`bobot_i26` DECIMAL(11,2) NULL,
	`i27` DECIMAL(11,2) NULL,
	`bobot_i27` DECIMAL(11,2) NULL,
	`i28` DECIMAL(11,2) NULL,
	`bobot_i28` DECIMAL(11,2) NULL,
	`i29` DECIMAL(11,2) NULL,
	`bobot_i29` DECIMAL(11,2) NULL,
	`i30` DECIMAL(11,2) NULL,
	`bobot_i30` DECIMAL(11,2) NULL,
	`i31` DECIMAL(11,2) NULL,
	`bobot_i31` DECIMAL(11,2) NULL,
	`i32` DECIMAL(11,2) NULL,
	`bobot_i32` DECIMAL(11,2) NULL,
	`i33` DECIMAL(11,2) NULL,
	`bobot_i33` DECIMAL(11,2) NULL,
	`i34` DECIMAL(11,2) NULL,
	`bobot_i34` DECIMAL(11,2) NULL,
	`i35` DECIMAL(11,2) NULL,
	`bobot_i35` DECIMAL(11,2) NULL,
	`i36` DECIMAL(11,2) NULL,
	`bobot_i36` DECIMAL(11,2) NULL,
	`i37` DECIMAL(11,2) NULL,
	`bobot_i37` DECIMAL(11,2) NULL,
	`i38` DECIMAL(11,2) NULL,
	`bobot_i38` DECIMAL(11,2) NULL,
	`i39` DECIMAL(11,2) NULL,
	`bobot_i39` DECIMAL(11,2) NULL,
	`i40` DECIMAL(11,2) NULL,
	`bobot_i40` DECIMAL(11,2) NULL,
	`i41` DECIMAL(11,2) NULL,
	`bobot_i41` DECIMAL(11,2) NULL,
	`i42` DECIMAL(11,2) NULL,
	`bobot_i42` DECIMAL(11,2) NULL,
	`i43` DECIMAL(11,2) NULL,
	`bobot_i43` DECIMAL(11,2) NULL,
	`i44` DECIMAL(11,2) NULL,
	`bobot_i44` DECIMAL(11,2) NULL,
	`i45` DECIMAL(11,2) NULL,
	`bobot_i45` DECIMAL(11,2) NULL,
	`i46` DECIMAL(11,2) NULL,
	`bobot_i46` DECIMAL(11,2) NULL,
	`i47` DECIMAL(11,2) NULL,
	`bobot_i47` DECIMAL(11,2) NULL,
	`bobot_aspek1` DECIMAL(11,2) NULL,
	`bobot_aspek2` DECIMAL(11,2) NULL,
	`bobot_aspek3` DECIMAL(11,2) NULL,
	`bobot_aspek4` DECIMAL(11,2) NULL,
	`bobot_aspek5` DECIMAL(11,2) NULL,
	`bobot_aspek6` DECIMAL(11,2) NULL,
	`bobot_aspek7` DECIMAL(11,2) NULL,
	`bobot_aspek8` DECIMAL(11,2) NULL,
	`bobot_domain1` DECIMAL(11,2) NULL,
	`bobot_domain2` DECIMAL(11,2) NULL,
	`bobot_domain3` DECIMAL(11,2) NULL,
	`bobot_domain4` DECIMAL(11,2) NULL,
	`aspek1` DECIMAL(32,2) NULL,
	`aspek2` DECIMAL(26,2) NULL,
	`aspek3` DECIMAL(26,2) NULL,
	`aspek4` DECIMAL(24,2) NULL,
	`aspek5` DECIMAL(30,2) NULL,
	`aspek6` DECIMAL(25,2) NULL,
	`aspek7` DECIMAL(32,2) NULL,
	`aspek8` DECIMAL(28,2) NULL
) ENGINE=MyISAM;

-- Dumping structure for table elaine_ta.domain
DROP TABLE IF EXISTS `domain`;
CREATE TABLE IF NOT EXISTS `domain` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `bobot` decimal(11,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view elaine_ta.domain_isi
DROP VIEW IF EXISTS `domain_isi`;
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `domain_isi` (
	`id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`tp_id` VARCHAR(45) NULL COLLATE 'latin1_swedish_ci',
	`tp_nama` VARCHAR(255) NULL COLLATE 'latin1_swedish_ci',
	`x` DECIMAL(11,2) NULL,
	`y` DECIMAL(11,2) NULL,
	`year` YEAR NOT NULL,
	`i1` DECIMAL(11,2) NOT NULL,
	`bobot_i1` DECIMAL(11,2) NULL,
	`i2` DECIMAL(11,2) NULL,
	`bobot_i2` DECIMAL(11,2) NULL,
	`i3` DECIMAL(11,2) NULL,
	`bobot_i3` DECIMAL(11,2) NULL,
	`i4` DECIMAL(11,2) NULL,
	`bobot_i4` DECIMAL(11,2) NULL,
	`i5` DECIMAL(11,2) NULL,
	`bobot_i5` DECIMAL(11,2) NULL,
	`i6` DECIMAL(11,2) NULL,
	`bobot_i6` DECIMAL(11,2) NULL,
	`i7` DECIMAL(11,2) NULL,
	`bobot_i7` DECIMAL(11,2) NULL,
	`i8` DECIMAL(11,2) NULL,
	`bobot_i8` DECIMAL(11,2) NULL,
	`i9` DECIMAL(11,2) NULL,
	`bobot_i9` DECIMAL(11,2) NULL,
	`i10` DECIMAL(11,2) NULL,
	`bobot_i10` DECIMAL(11,2) NULL,
	`i11` DECIMAL(11,2) NULL,
	`bobot_i11` DECIMAL(11,2) NULL,
	`i12` DECIMAL(11,2) NULL,
	`bobot_i12` DECIMAL(11,2) NULL,
	`i13` DECIMAL(11,2) NULL,
	`bobot_i13` DECIMAL(11,2) NULL,
	`i14` DECIMAL(11,2) NULL,
	`bobot_i14` DECIMAL(11,2) NULL,
	`i15` DECIMAL(11,2) NULL,
	`bobot_i15` DECIMAL(11,2) NULL,
	`i16` DECIMAL(11,2) NULL,
	`bobot_i16` DECIMAL(11,2) NULL,
	`i17` DECIMAL(11,2) NULL,
	`bobot_i17` DECIMAL(11,2) NULL,
	`i18` DECIMAL(11,2) NULL,
	`bobot_i18` DECIMAL(11,2) NULL,
	`i19` DECIMAL(11,2) NULL,
	`bobot_i19` DECIMAL(11,2) NULL,
	`i20` DECIMAL(11,2) NULL,
	`bobot_i20` DECIMAL(11,2) NULL,
	`i21` DECIMAL(11,2) NULL,
	`bobot_i21` DECIMAL(11,2) NULL,
	`i22` DECIMAL(11,2) NULL,
	`bobot_i22` DECIMAL(11,2) NULL,
	`i23` DECIMAL(11,2) NULL,
	`bobot_i23` DECIMAL(11,2) NULL,
	`i24` DECIMAL(11,2) NULL,
	`bobot_i24` DECIMAL(11,2) NULL,
	`i25` DECIMAL(11,2) NULL,
	`bobot_i25` DECIMAL(11,2) NULL,
	`i26` DECIMAL(11,2) NULL,
	`bobot_i26` DECIMAL(11,2) NULL,
	`i27` DECIMAL(11,2) NULL,
	`bobot_i27` DECIMAL(11,2) NULL,
	`i28` DECIMAL(11,2) NULL,
	`bobot_i28` DECIMAL(11,2) NULL,
	`i29` DECIMAL(11,2) NULL,
	`bobot_i29` DECIMAL(11,2) NULL,
	`i30` DECIMAL(11,2) NULL,
	`bobot_i30` DECIMAL(11,2) NULL,
	`i31` DECIMAL(11,2) NULL,
	`bobot_i31` DECIMAL(11,2) NULL,
	`i32` DECIMAL(11,2) NULL,
	`bobot_i32` DECIMAL(11,2) NULL,
	`i33` DECIMAL(11,2) NULL,
	`bobot_i33` DECIMAL(11,2) NULL,
	`i34` DECIMAL(11,2) NULL,
	`bobot_i34` DECIMAL(11,2) NULL,
	`i35` DECIMAL(11,2) NULL,
	`bobot_i35` DECIMAL(11,2) NULL,
	`i36` DECIMAL(11,2) NULL,
	`bobot_i36` DECIMAL(11,2) NULL,
	`i37` DECIMAL(11,2) NULL,
	`bobot_i37` DECIMAL(11,2) NULL,
	`i38` DECIMAL(11,2) NULL,
	`bobot_i38` DECIMAL(11,2) NULL,
	`i39` DECIMAL(11,2) NULL,
	`bobot_i39` DECIMAL(11,2) NULL,
	`i40` DECIMAL(11,2) NULL,
	`bobot_i40` DECIMAL(11,2) NULL,
	`i41` DECIMAL(11,2) NULL,
	`bobot_i41` DECIMAL(11,2) NULL,
	`i42` DECIMAL(11,2) NULL,
	`bobot_i42` DECIMAL(11,2) NULL,
	`i43` DECIMAL(11,2) NULL,
	`bobot_i43` DECIMAL(11,2) NULL,
	`i44` DECIMAL(11,2) NULL,
	`bobot_i44` DECIMAL(11,2) NULL,
	`i45` DECIMAL(11,2) NULL,
	`bobot_i45` DECIMAL(11,2) NULL,
	`i46` DECIMAL(11,2) NULL,
	`bobot_i46` DECIMAL(11,2) NULL,
	`i47` DECIMAL(11,2) NULL,
	`bobot_i47` DECIMAL(11,2) NULL,
	`bobot_aspek1` DECIMAL(11,2) NULL,
	`bobot_aspek2` DECIMAL(11,2) NULL,
	`bobot_aspek3` DECIMAL(11,2) NULL,
	`bobot_aspek4` DECIMAL(11,2) NULL,
	`bobot_aspek5` DECIMAL(11,2) NULL,
	`bobot_aspek6` DECIMAL(11,2) NULL,
	`bobot_aspek7` DECIMAL(11,2) NULL,
	`bobot_aspek8` DECIMAL(11,2) NULL,
	`bobot_domain1` DECIMAL(11,2) NULL,
	`bobot_domain2` DECIMAL(11,2) NULL,
	`bobot_domain3` DECIMAL(11,2) NULL,
	`bobot_domain4` DECIMAL(11,2) NULL,
	`aspek1` DECIMAL(32,2) NULL,
	`aspek2` DECIMAL(26,2) NULL,
	`aspek3` DECIMAL(26,2) NULL,
	`aspek4` DECIMAL(24,2) NULL,
	`aspek5` DECIMAL(30,2) NULL,
	`aspek6` DECIMAL(25,2) NULL,
	`aspek7` DECIMAL(32,2) NULL,
	`aspek8` DECIMAL(28,2) NULL,
	`domain1` DECIMAL(44,2) NULL,
	`domain2` DECIMAL(40,2) NULL,
	`domain3` DECIMAL(43,2) NULL,
	`domain4` DECIMAL(44,1) NULL
) ENGINE=MyISAM;

-- Dumping structure for table elaine_ta.grup_instansi
DROP TABLE IF EXISTS `grup_instansi`;
CREATE TABLE IF NOT EXISTS `grup_instansi` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `titik_peta` varchar(45) NOT NULL,
  `tipe` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view elaine_ta.indeks_isi
DROP VIEW IF EXISTS `indeks_isi`;
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `indeks_isi` (
	`id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_id` VARCHAR(25) NOT NULL COLLATE 'latin1_swedish_ci',
	`gi_nama` VARCHAR(255) NOT NULL COLLATE 'latin1_swedish_ci',
	`tp_id` VARCHAR(45) NULL COLLATE 'latin1_swedish_ci',
	`tp_nama` VARCHAR(255) NULL COLLATE 'latin1_swedish_ci',
	`x` DECIMAL(11,2) NULL,
	`y` DECIMAL(11,2) NULL,
	`year` YEAR NOT NULL,
	`i1` DECIMAL(11,2) NOT NULL,
	`bobot_i1` DECIMAL(11,2) NULL,
	`i2` DECIMAL(11,2) NULL,
	`bobot_i2` DECIMAL(11,2) NULL,
	`i3` DECIMAL(11,2) NULL,
	`bobot_i3` DECIMAL(11,2) NULL,
	`i4` DECIMAL(11,2) NULL,
	`bobot_i4` DECIMAL(11,2) NULL,
	`i5` DECIMAL(11,2) NULL,
	`bobot_i5` DECIMAL(11,2) NULL,
	`i6` DECIMAL(11,2) NULL,
	`bobot_i6` DECIMAL(11,2) NULL,
	`i7` DECIMAL(11,2) NULL,
	`bobot_i7` DECIMAL(11,2) NULL,
	`i8` DECIMAL(11,2) NULL,
	`bobot_i8` DECIMAL(11,2) NULL,
	`i9` DECIMAL(11,2) NULL,
	`bobot_i9` DECIMAL(11,2) NULL,
	`i10` DECIMAL(11,2) NULL,
	`bobot_i10` DECIMAL(11,2) NULL,
	`i11` DECIMAL(11,2) NULL,
	`bobot_i11` DECIMAL(11,2) NULL,
	`i12` DECIMAL(11,2) NULL,
	`bobot_i12` DECIMAL(11,2) NULL,
	`i13` DECIMAL(11,2) NULL,
	`bobot_i13` DECIMAL(11,2) NULL,
	`i14` DECIMAL(11,2) NULL,
	`bobot_i14` DECIMAL(11,2) NULL,
	`i15` DECIMAL(11,2) NULL,
	`bobot_i15` DECIMAL(11,2) NULL,
	`i16` DECIMAL(11,2) NULL,
	`bobot_i16` DECIMAL(11,2) NULL,
	`i17` DECIMAL(11,2) NULL,
	`bobot_i17` DECIMAL(11,2) NULL,
	`i18` DECIMAL(11,2) NULL,
	`bobot_i18` DECIMAL(11,2) NULL,
	`i19` DECIMAL(11,2) NULL,
	`bobot_i19` DECIMAL(11,2) NULL,
	`i20` DECIMAL(11,2) NULL,
	`bobot_i20` DECIMAL(11,2) NULL,
	`i21` DECIMAL(11,2) NULL,
	`bobot_i21` DECIMAL(11,2) NULL,
	`i22` DECIMAL(11,2) NULL,
	`bobot_i22` DECIMAL(11,2) NULL,
	`i23` DECIMAL(11,2) NULL,
	`bobot_i23` DECIMAL(11,2) NULL,
	`i24` DECIMAL(11,2) NULL,
	`bobot_i24` DECIMAL(11,2) NULL,
	`i25` DECIMAL(11,2) NULL,
	`bobot_i25` DECIMAL(11,2) NULL,
	`i26` DECIMAL(11,2) NULL,
	`bobot_i26` DECIMAL(11,2) NULL,
	`i27` DECIMAL(11,2) NULL,
	`bobot_i27` DECIMAL(11,2) NULL,
	`i28` DECIMAL(11,2) NULL,
	`bobot_i28` DECIMAL(11,2) NULL,
	`i29` DECIMAL(11,2) NULL,
	`bobot_i29` DECIMAL(11,2) NULL,
	`i30` DECIMAL(11,2) NULL,
	`bobot_i30` DECIMAL(11,2) NULL,
	`i31` DECIMAL(11,2) NULL,
	`bobot_i31` DECIMAL(11,2) NULL,
	`i32` DECIMAL(11,2) NULL,
	`bobot_i32` DECIMAL(11,2) NULL,
	`i33` DECIMAL(11,2) NULL,
	`bobot_i33` DECIMAL(11,2) NULL,
	`i34` DECIMAL(11,2) NULL,
	`bobot_i34` DECIMAL(11,2) NULL,
	`i35` DECIMAL(11,2) NULL,
	`bobot_i35` DECIMAL(11,2) NULL,
	`i36` DECIMAL(11,2) NULL,
	`bobot_i36` DECIMAL(11,2) NULL,
	`i37` DECIMAL(11,2) NULL,
	`bobot_i37` DECIMAL(11,2) NULL,
	`i38` DECIMAL(11,2) NULL,
	`bobot_i38` DECIMAL(11,2) NULL,
	`i39` DECIMAL(11,2) NULL,
	`bobot_i39` DECIMAL(11,2) NULL,
	`i40` DECIMAL(11,2) NULL,
	`bobot_i40` DECIMAL(11,2) NULL,
	`i41` DECIMAL(11,2) NULL,
	`bobot_i41` DECIMAL(11,2) NULL,
	`i42` DECIMAL(11,2) NULL,
	`bobot_i42` DECIMAL(11,2) NULL,
	`i43` DECIMAL(11,2) NULL,
	`bobot_i43` DECIMAL(11,2) NULL,
	`i44` DECIMAL(11,2) NULL,
	`bobot_i44` DECIMAL(11,2) NULL,
	`i45` DECIMAL(11,2) NULL,
	`bobot_i45` DECIMAL(11,2) NULL,
	`i46` DECIMAL(11,2) NULL,
	`bobot_i46` DECIMAL(11,2) NULL,
	`i47` DECIMAL(11,2) NULL,
	`bobot_i47` DECIMAL(11,2) NULL,
	`bobot_aspek1` DECIMAL(11,2) NULL,
	`bobot_aspek2` DECIMAL(11,2) NULL,
	`bobot_aspek3` DECIMAL(11,2) NULL,
	`bobot_aspek4` DECIMAL(11,2) NULL,
	`bobot_aspek5` DECIMAL(11,2) NULL,
	`bobot_aspek6` DECIMAL(11,2) NULL,
	`bobot_aspek7` DECIMAL(11,2) NULL,
	`bobot_aspek8` DECIMAL(11,2) NULL,
	`bobot_domain1` DECIMAL(11,2) NULL,
	`bobot_domain2` DECIMAL(11,2) NULL,
	`bobot_domain3` DECIMAL(11,2) NULL,
	`bobot_domain4` DECIMAL(11,2) NULL,
	`aspek1` DECIMAL(32,2) NULL,
	`aspek2` DECIMAL(26,2) NULL,
	`aspek3` DECIMAL(26,2) NULL,
	`aspek4` DECIMAL(24,2) NULL,
	`aspek5` DECIMAL(30,2) NULL,
	`aspek6` DECIMAL(25,2) NULL,
	`aspek7` DECIMAL(32,2) NULL,
	`aspek8` DECIMAL(28,2) NULL,
	`domain1` DECIMAL(44,2) NULL,
	`domain2` DECIMAL(40,2) NULL,
	`domain3` DECIMAL(43,2) NULL,
	`domain4` DECIMAL(44,1) NULL,
	`i1_bobot` DECIMAL(21,2) NULL,
	`i2_bobot` DECIMAL(21,2) NULL,
	`i3_bobot` DECIMAL(21,2) NULL,
	`i4_bobot` DECIMAL(21,2) NULL,
	`i5_bobot` DECIMAL(21,2) NULL,
	`i6_bobot` DECIMAL(21,2) NULL,
	`i7_bobot` DECIMAL(21,2) NULL,
	`i8_bobot` DECIMAL(21,2) NULL,
	`i9_bobot` DECIMAL(21,2) NULL,
	`i10_bobot` DECIMAL(21,2) NULL,
	`i11_bobot` DECIMAL(21,2) NULL,
	`i12_bobot` DECIMAL(21,2) NULL,
	`i13_bobot` DECIMAL(21,2) NULL,
	`i14_bobot` DECIMAL(21,2) NULL,
	`i15_bobot` DECIMAL(21,2) NULL,
	`i16_bobot` DECIMAL(21,2) NULL,
	`i17_bobot` DECIMAL(21,2) NULL,
	`i18_bobot` DECIMAL(20,0) NULL,
	`i19_bobot` DECIMAL(21,2) NULL,
	`i20_bobot` DECIMAL(21,2) NULL,
	`i21_bobot` DECIMAL(21,2) NULL,
	`i22_bobot` DECIMAL(21,2) NULL,
	`i23_bobot` DECIMAL(21,2) NULL,
	`i24_bobot` DECIMAL(21,2) NULL,
	`i25_bobot` DECIMAL(21,2) NULL,
	`i26_bobot` DECIMAL(21,2) NULL,
	`i27_bobot` DECIMAL(21,2) NULL,
	`i28_bobot` DECIMAL(21,2) NULL,
	`i29_bobot` DECIMAL(21,2) NULL,
	`i30_bobot` DECIMAL(21,2) NULL,
	`i31_bobot` DECIMAL(21,2) NULL,
	`i32_bobot` DECIMAL(21,2) NULL,
	`i33_bobot` DECIMAL(21,2) NULL,
	`i34_bobot` DECIMAL(21,2) NULL,
	`i35_bobot` DECIMAL(21,2) NULL,
	`i36_bobot` DECIMAL(21,2) NULL,
	`i37_bobot` DECIMAL(21,2) NULL,
	`i38_bobot` DECIMAL(21,2) NULL,
	`i39_bobot` DECIMAL(21,2) NULL,
	`i40_bobot` DECIMAL(21,2) NULL,
	`i41_bobot` DECIMAL(21,2) NULL,
	`i42_bobot` DECIMAL(21,2) NULL,
	`i43_bobot` DECIMAL(21,2) NULL,
	`i44_bobot` DECIMAL(21,2) NULL,
	`i45_bobot` DECIMAL(21,2) NULL,
	`i46_bobot` DECIMAL(21,2) NULL,
	`i47_bobot` DECIMAL(21,2) NULL,
	`aspek1_bobot` DECIMAL(42,2) NULL,
	`aspek2_bobot` DECIMAL(36,2) NULL,
	`aspek3_bobot` DECIMAL(36,2) NULL,
	`aspek4_bobot` DECIMAL(34,2) NULL,
	`aspek5_bobot` DECIMAL(40,2) NULL,
	`aspek6_bobot` DECIMAL(35,2) NULL,
	`aspek7_bobot` DECIMAL(42,2) NULL,
	`domain1_bobot` DECIMAL(54,2) NULL,
	`domain2_bobot` DECIMAL(50,2) NULL,
	`domain3_bobot` DECIMAL(53,2) NULL,
	`domain4_bobot` DECIMAL(55,2) NULL,
	`indeks` DECIMAL(57,2) NULL
) ENGINE=MyISAM;

-- Dumping structure for table elaine_ta.indikator
DROP TABLE IF EXISTS `indikator`;
CREATE TABLE IF NOT EXISTS `indikator` (
  `id` varchar(25) NOT NULL,
  `aspek` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `nama_lengkap` varchar(255) NOT NULL,
  `bobot` decimal(11,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.instansi
DROP TABLE IF EXISTS `instansi`;
CREATE TABLE IF NOT EXISTS `instansi` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `group_instansi` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.isi
DROP TABLE IF EXISTS `isi`;
CREATE TABLE IF NOT EXISTS `isi` (
  `instansi` varchar(25) NOT NULL,
  `indikator` varchar(25) NOT NULL,
  `value` decimal(11,2) NOT NULL,
  `year` year NOT NULL,
  PRIMARY KEY (`instansi`,`indikator`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.predikat
DROP TABLE IF EXISTS `predikat`;
CREATE TABLE IF NOT EXISTS `predikat` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `batas_bawah` decimal(11,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table elaine_ta.titik_peta
DROP TABLE IF EXISTS `titik_peta`;
CREATE TABLE IF NOT EXISTS `titik_peta` (
  `id` varchar(45) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `x` decimal(11,2) NOT NULL,
  `y` decimal(11,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view elaine_ta.all_isi
DROP VIEW IF EXISTS `all_isi`;
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `all_isi`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `all_isi` AS select `i`.`id` AS `id`,`i`.`nama` AS `nama`,`gi`.`id` AS `gi_id`,`gi`.`nama` AS `gi_nama`,`tp`.`id` AS `tp_id`,`tp`.`nama` AS `tp_nama`,`tp`.`x` AS `x`,`tp`.`y` AS `y`,`m`.`year` AS `year`,`m`.`value` AS `i1`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400001')) AS `bobot_i1`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400002') and (`isi`.`year` = `m`.`year`))) AS `i2`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400002')) AS `bobot_i2`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400003') and (`isi`.`year` = `m`.`year`))) AS `i3`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400003')) AS `bobot_i3`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400004') and (`isi`.`year` = `m`.`year`))) AS `i4`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400004')) AS `bobot_i4`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400005') and (`isi`.`year` = `m`.`year`))) AS `i5`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400005')) AS `bobot_i5`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400006') and (`isi`.`year` = `m`.`year`))) AS `i6`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400006')) AS `bobot_i6`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400007') and (`isi`.`year` = `m`.`year`))) AS `i7`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400007')) AS `bobot_i7`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400008') and (`isi`.`year` = `m`.`year`))) AS `i8`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400008')) AS `bobot_i8`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400009') and (`isi`.`year` = `m`.`year`))) AS `i9`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400009')) AS `bobot_i9`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400010') and (`isi`.`year` = `m`.`year`))) AS `i10`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400010')) AS `bobot_i10`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400011') and (`isi`.`year` = `m`.`year`))) AS `i11`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400011')) AS `bobot_i11`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400012') and (`isi`.`year` = `m`.`year`))) AS `i12`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400012')) AS `bobot_i12`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400013') and (`isi`.`year` = `m`.`year`))) AS `i13`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400013')) AS `bobot_i13`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400014') and (`isi`.`year` = `m`.`year`))) AS `i14`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400014')) AS `bobot_i14`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400015') and (`isi`.`year` = `m`.`year`))) AS `i15`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400015')) AS `bobot_i15`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400016') and (`isi`.`year` = `m`.`year`))) AS `i16`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400016')) AS `bobot_i16`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400017') and (`isi`.`year` = `m`.`year`))) AS `i17`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400017')) AS `bobot_i17`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400018') and (`isi`.`year` = `m`.`year`))) AS `i18`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400018')) AS `bobot_i18`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400019') and (`isi`.`year` = `m`.`year`))) AS `i19`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400019')) AS `bobot_i19`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400020') and (`isi`.`year` = `m`.`year`))) AS `i20`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400020')) AS `bobot_i20`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400021') and (`isi`.`year` = `m`.`year`))) AS `i21`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400021')) AS `bobot_i21`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400022') and (`isi`.`year` = `m`.`year`))) AS `i22`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400022')) AS `bobot_i22`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400023') and (`isi`.`year` = `m`.`year`))) AS `i23`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400023')) AS `bobot_i23`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400024') and (`isi`.`year` = `m`.`year`))) AS `i24`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400024')) AS `bobot_i24`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400025') and (`isi`.`year` = `m`.`year`))) AS `i25`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400025')) AS `bobot_i25`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400026') and (`isi`.`year` = `m`.`year`))) AS `i26`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400026')) AS `bobot_i26`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400027') and (`isi`.`year` = `m`.`year`))) AS `i27`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400027')) AS `bobot_i27`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400028') and (`isi`.`year` = `m`.`year`))) AS `i28`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400028')) AS `bobot_i28`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400029') and (`isi`.`year` = `m`.`year`))) AS `i29`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400029')) AS `bobot_i29`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400030') and (`isi`.`year` = `m`.`year`))) AS `i30`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400030')) AS `bobot_i30`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400031') and (`isi`.`year` = `m`.`year`))) AS `i31`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400031')) AS `bobot_i31`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400032') and (`isi`.`year` = `m`.`year`))) AS `i32`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400032')) AS `bobot_i32`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400033') and (`isi`.`year` = `m`.`year`))) AS `i33`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400033')) AS `bobot_i33`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400034') and (`isi`.`year` = `m`.`year`))) AS `i34`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400034')) AS `bobot_i34`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400035') and (`isi`.`year` = `m`.`year`))) AS `i35`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400035')) AS `bobot_i35`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400036') and (`isi`.`year` = `m`.`year`))) AS `i36`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400036')) AS `bobot_i36`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400037') and (`isi`.`year` = `m`.`year`))) AS `i37`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400037')) AS `bobot_i37`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400038') and (`isi`.`year` = `m`.`year`))) AS `i38`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400038')) AS `bobot_i38`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400039') and (`isi`.`year` = `m`.`year`))) AS `i39`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400039')) AS `bobot_i39`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400040') and (`isi`.`year` = `m`.`year`))) AS `i40`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400040')) AS `bobot_i40`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400041') and (`isi`.`year` = `m`.`year`))) AS `i41`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400041')) AS `bobot_i41`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400042') and (`isi`.`year` = `m`.`year`))) AS `i42`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400042')) AS `bobot_i42`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400043') and (`isi`.`year` = `m`.`year`))) AS `i43`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400043')) AS `bobot_i43`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400044') and (`isi`.`year` = `m`.`year`))) AS `i44`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400044')) AS `bobot_i44`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400045') and (`isi`.`year` = `m`.`year`))) AS `i45`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400045')) AS `bobot_i45`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400046') and (`isi`.`year` = `m`.`year`))) AS `i46`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400046')) AS `bobot_i46`,(select `isi`.`value` from `isi` where ((`isi`.`instansi` = `i`.`id`) and (`isi`.`indikator` = 'in2023110400047') and (`isi`.`year` = `m`.`year`))) AS `i47`,(select `indikator`.`bobot` from `indikator` where (`indikator`.`id` = 'in2023110400047')) AS `bobot_i47`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400001')) AS `bobot_aspek1`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400002')) AS `bobot_aspek2`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400003')) AS `bobot_aspek3`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400004')) AS `bobot_aspek4`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400005')) AS `bobot_aspek5`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400006')) AS `bobot_aspek6`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400007')) AS `bobot_aspek7`,(select `aspek`.`bobot` from `aspek` where (`aspek`.`id` = 'a2023110400008')) AS `bobot_aspek8`,(select `domain`.`bobot` from `domain` where (`domain`.`id` = 'd2023110400001')) AS `bobot_domain1`,(select `domain`.`bobot` from `domain` where (`domain`.`id` = 'd2023110400002')) AS `bobot_domain2`,(select `domain`.`bobot` from `domain` where (`domain`.`id` = 'd2023110400003')) AS `bobot_domain3`,(select `domain`.`bobot` from `domain` where (`domain`.`id` = 'd2023110400004')) AS `bobot_domain4` from (((`instansi` `i` join `isi` `m` on(((`m`.`instansi` = `i`.`id`) and (`m`.`indikator` = 'in2023110400001')))) join `grup_instansi` `gi` on((`i`.`group_instansi` = `gi`.`id`))) left join `titik_peta` `tp` on((`gi`.`titik_peta` = `tp`.`id`)));

-- Dumping structure for view elaine_ta.aspek_isi
DROP VIEW IF EXISTS `aspek_isi`;
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `aspek_isi`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `aspek_isi` AS select `all_isi`.`id` AS `id`,`all_isi`.`nama` AS `nama`,`all_isi`.`gi_id` AS `gi_id`,`all_isi`.`gi_nama` AS `gi_nama`,`all_isi`.`tp_id` AS `tp_id`,`all_isi`.`tp_nama` AS `tp_nama`,`all_isi`.`x` AS `x`,`all_isi`.`y` AS `y`,`all_isi`.`year` AS `year`,`all_isi`.`i1` AS `i1`,`all_isi`.`bobot_i1` AS `bobot_i1`,`all_isi`.`i2` AS `i2`,`all_isi`.`bobot_i2` AS `bobot_i2`,`all_isi`.`i3` AS `i3`,`all_isi`.`bobot_i3` AS `bobot_i3`,`all_isi`.`i4` AS `i4`,`all_isi`.`bobot_i4` AS `bobot_i4`,`all_isi`.`i5` AS `i5`,`all_isi`.`bobot_i5` AS `bobot_i5`,`all_isi`.`i6` AS `i6`,`all_isi`.`bobot_i6` AS `bobot_i6`,`all_isi`.`i7` AS `i7`,`all_isi`.`bobot_i7` AS `bobot_i7`,`all_isi`.`i8` AS `i8`,`all_isi`.`bobot_i8` AS `bobot_i8`,`all_isi`.`i9` AS `i9`,`all_isi`.`bobot_i9` AS `bobot_i9`,`all_isi`.`i10` AS `i10`,`all_isi`.`bobot_i10` AS `bobot_i10`,`all_isi`.`i11` AS `i11`,`all_isi`.`bobot_i11` AS `bobot_i11`,`all_isi`.`i12` AS `i12`,`all_isi`.`bobot_i12` AS `bobot_i12`,`all_isi`.`i13` AS `i13`,`all_isi`.`bobot_i13` AS `bobot_i13`,`all_isi`.`i14` AS `i14`,`all_isi`.`bobot_i14` AS `bobot_i14`,`all_isi`.`i15` AS `i15`,`all_isi`.`bobot_i15` AS `bobot_i15`,`all_isi`.`i16` AS `i16`,`all_isi`.`bobot_i16` AS `bobot_i16`,`all_isi`.`i17` AS `i17`,`all_isi`.`bobot_i17` AS `bobot_i17`,`all_isi`.`i18` AS `i18`,`all_isi`.`bobot_i18` AS `bobot_i18`,`all_isi`.`i19` AS `i19`,`all_isi`.`bobot_i19` AS `bobot_i19`,`all_isi`.`i20` AS `i20`,`all_isi`.`bobot_i20` AS `bobot_i20`,`all_isi`.`i21` AS `i21`,`all_isi`.`bobot_i21` AS `bobot_i21`,`all_isi`.`i22` AS `i22`,`all_isi`.`bobot_i22` AS `bobot_i22`,`all_isi`.`i23` AS `i23`,`all_isi`.`bobot_i23` AS `bobot_i23`,`all_isi`.`i24` AS `i24`,`all_isi`.`bobot_i24` AS `bobot_i24`,`all_isi`.`i25` AS `i25`,`all_isi`.`bobot_i25` AS `bobot_i25`,`all_isi`.`i26` AS `i26`,`all_isi`.`bobot_i26` AS `bobot_i26`,`all_isi`.`i27` AS `i27`,`all_isi`.`bobot_i27` AS `bobot_i27`,`all_isi`.`i28` AS `i28`,`all_isi`.`bobot_i28` AS `bobot_i28`,`all_isi`.`i29` AS `i29`,`all_isi`.`bobot_i29` AS `bobot_i29`,`all_isi`.`i30` AS `i30`,`all_isi`.`bobot_i30` AS `bobot_i30`,`all_isi`.`i31` AS `i31`,`all_isi`.`bobot_i31` AS `bobot_i31`,`all_isi`.`i32` AS `i32`,`all_isi`.`bobot_i32` AS `bobot_i32`,`all_isi`.`i33` AS `i33`,`all_isi`.`bobot_i33` AS `bobot_i33`,`all_isi`.`i34` AS `i34`,`all_isi`.`bobot_i34` AS `bobot_i34`,`all_isi`.`i35` AS `i35`,`all_isi`.`bobot_i35` AS `bobot_i35`,`all_isi`.`i36` AS `i36`,`all_isi`.`bobot_i36` AS `bobot_i36`,`all_isi`.`i37` AS `i37`,`all_isi`.`bobot_i37` AS `bobot_i37`,`all_isi`.`i38` AS `i38`,`all_isi`.`bobot_i38` AS `bobot_i38`,`all_isi`.`i39` AS `i39`,`all_isi`.`bobot_i39` AS `bobot_i39`,`all_isi`.`i40` AS `i40`,`all_isi`.`bobot_i40` AS `bobot_i40`,`all_isi`.`i41` AS `i41`,`all_isi`.`bobot_i41` AS `bobot_i41`,`all_isi`.`i42` AS `i42`,`all_isi`.`bobot_i42` AS `bobot_i42`,`all_isi`.`i43` AS `i43`,`all_isi`.`bobot_i43` AS `bobot_i43`,`all_isi`.`i44` AS `i44`,`all_isi`.`bobot_i44` AS `bobot_i44`,`all_isi`.`i45` AS `i45`,`all_isi`.`bobot_i45` AS `bobot_i45`,`all_isi`.`i46` AS `i46`,`all_isi`.`bobot_i46` AS `bobot_i46`,`all_isi`.`i47` AS `i47`,`all_isi`.`bobot_i47` AS `bobot_i47`,`all_isi`.`bobot_aspek1` AS `bobot_aspek1`,`all_isi`.`bobot_aspek2` AS `bobot_aspek2`,`all_isi`.`bobot_aspek3` AS `bobot_aspek3`,`all_isi`.`bobot_aspek4` AS `bobot_aspek4`,`all_isi`.`bobot_aspek5` AS `bobot_aspek5`,`all_isi`.`bobot_aspek6` AS `bobot_aspek6`,`all_isi`.`bobot_aspek7` AS `bobot_aspek7`,`all_isi`.`bobot_aspek8` AS `bobot_aspek8`,`all_isi`.`bobot_domain1` AS `bobot_domain1`,`all_isi`.`bobot_domain2` AS `bobot_domain2`,`all_isi`.`bobot_domain3` AS `bobot_domain3`,`all_isi`.`bobot_domain4` AS `bobot_domain4`,round((((((((((((`all_isi`.`i1` * `all_isi`.`bobot_i1`) + (`all_isi`.`i2` * `all_isi`.`bobot_i2`)) + (`all_isi`.`i3` * `all_isi`.`bobot_i3`)) + (`all_isi`.`i4` * `all_isi`.`bobot_i4`)) + (`all_isi`.`i5` * `all_isi`.`bobot_i5`)) + (`all_isi`.`i6` * `all_isi`.`bobot_i6`)) + (`all_isi`.`i7` * `all_isi`.`bobot_i7`)) + (`all_isi`.`i8` * `all_isi`.`bobot_i8`)) + (`all_isi`.`i9` * `all_isi`.`bobot_i9`)) + (`all_isi`.`i10` * `all_isi`.`bobot_i10`)) / `all_isi`.`bobot_aspek1`),2) AS `aspek1`,round((((((`all_isi`.`i11` * `all_isi`.`bobot_i11`) + (`all_isi`.`i12` * `all_isi`.`bobot_i12`)) + (`all_isi`.`i13` * `all_isi`.`bobot_i13`)) + (`all_isi`.`i14` * `all_isi`.`bobot_i14`)) / `all_isi`.`bobot_aspek2`),2) AS `aspek2`,round((((((`all_isi`.`i15` * `all_isi`.`bobot_i15`) + (`all_isi`.`i16` * `all_isi`.`bobot_i16`)) + (`all_isi`.`i17` * `all_isi`.`bobot_i17`)) + (`all_isi`.`i18` * `all_isi`.`bobot_i18`)) / `all_isi`.`bobot_aspek3`),2) AS `aspek3`,round((((`all_isi`.`i19` * `all_isi`.`bobot_i19`) + (`all_isi`.`i20` * `all_isi`.`bobot_i20`)) / `all_isi`.`bobot_aspek4`),2) AS `aspek4`,round((((((((((`all_isi`.`i21` * `all_isi`.`bobot_i21`) + (`all_isi`.`i22` * `all_isi`.`bobot_i22`)) + (`all_isi`.`i23` * `all_isi`.`bobot_i23`)) + (`all_isi`.`i24` * `all_isi`.`bobot_i24`)) + (`all_isi`.`i25` * `all_isi`.`bobot_i25`)) + (`all_isi`.`i26` * `all_isi`.`bobot_i26`)) + (`all_isi`.`i27` * `all_isi`.`bobot_i27`)) + (`all_isi`.`i28` * `all_isi`.`bobot_i28`)) / `all_isi`.`bobot_aspek5`),2) AS `aspek5`,round(((((`all_isi`.`i29` * `all_isi`.`bobot_i29`) + (`all_isi`.`i30` * `all_isi`.`bobot_i30`)) + (`all_isi`.`i31` * `all_isi`.`bobot_i31`)) / `all_isi`.`bobot_aspek6`),2) AS `aspek6`,round((((((((((((`all_isi`.`i32` * `all_isi`.`bobot_i32`) + (`all_isi`.`i33` * `all_isi`.`bobot_i33`)) + (`all_isi`.`i34` * `all_isi`.`bobot_i34`)) + (`all_isi`.`i35` * `all_isi`.`bobot_i35`)) + (`all_isi`.`i36` * `all_isi`.`bobot_i36`)) + (`all_isi`.`i37` * `all_isi`.`bobot_i37`)) + (`all_isi`.`i38` * `all_isi`.`bobot_i38`)) + (`all_isi`.`i39` * `all_isi`.`bobot_i39`)) + (`all_isi`.`i40` * `all_isi`.`bobot_i40`)) + (`all_isi`.`i41` * `all_isi`.`bobot_i41`)) / `all_isi`.`bobot_aspek7`),2) AS `aspek7`,round((((((((`all_isi`.`i42` * `all_isi`.`bobot_i42`) + (`all_isi`.`i43` * `all_isi`.`bobot_i43`)) + (`all_isi`.`i44` * `all_isi`.`bobot_i44`)) + (`all_isi`.`i45` * `all_isi`.`bobot_i45`)) + (`all_isi`.`i46` * `all_isi`.`bobot_i46`)) + (`all_isi`.`i47` * `all_isi`.`bobot_i47`)) / `all_isi`.`bobot_aspek8`),2) AS `aspek8` from `all_isi`;

-- Dumping structure for view elaine_ta.domain_isi
DROP VIEW IF EXISTS `domain_isi`;
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `domain_isi`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `domain_isi` AS select `aspek_isi`.`id` AS `id`,`aspek_isi`.`nama` AS `nama`,`aspek_isi`.`gi_id` AS `gi_id`,`aspek_isi`.`gi_nama` AS `gi_nama`,`aspek_isi`.`tp_id` AS `tp_id`,`aspek_isi`.`tp_nama` AS `tp_nama`,`aspek_isi`.`x` AS `x`,`aspek_isi`.`y` AS `y`,`aspek_isi`.`year` AS `year`,`aspek_isi`.`i1` AS `i1`,`aspek_isi`.`bobot_i1` AS `bobot_i1`,`aspek_isi`.`i2` AS `i2`,`aspek_isi`.`bobot_i2` AS `bobot_i2`,`aspek_isi`.`i3` AS `i3`,`aspek_isi`.`bobot_i3` AS `bobot_i3`,`aspek_isi`.`i4` AS `i4`,`aspek_isi`.`bobot_i4` AS `bobot_i4`,`aspek_isi`.`i5` AS `i5`,`aspek_isi`.`bobot_i5` AS `bobot_i5`,`aspek_isi`.`i6` AS `i6`,`aspek_isi`.`bobot_i6` AS `bobot_i6`,`aspek_isi`.`i7` AS `i7`,`aspek_isi`.`bobot_i7` AS `bobot_i7`,`aspek_isi`.`i8` AS `i8`,`aspek_isi`.`bobot_i8` AS `bobot_i8`,`aspek_isi`.`i9` AS `i9`,`aspek_isi`.`bobot_i9` AS `bobot_i9`,`aspek_isi`.`i10` AS `i10`,`aspek_isi`.`bobot_i10` AS `bobot_i10`,`aspek_isi`.`i11` AS `i11`,`aspek_isi`.`bobot_i11` AS `bobot_i11`,`aspek_isi`.`i12` AS `i12`,`aspek_isi`.`bobot_i12` AS `bobot_i12`,`aspek_isi`.`i13` AS `i13`,`aspek_isi`.`bobot_i13` AS `bobot_i13`,`aspek_isi`.`i14` AS `i14`,`aspek_isi`.`bobot_i14` AS `bobot_i14`,`aspek_isi`.`i15` AS `i15`,`aspek_isi`.`bobot_i15` AS `bobot_i15`,`aspek_isi`.`i16` AS `i16`,`aspek_isi`.`bobot_i16` AS `bobot_i16`,`aspek_isi`.`i17` AS `i17`,`aspek_isi`.`bobot_i17` AS `bobot_i17`,`aspek_isi`.`i18` AS `i18`,`aspek_isi`.`bobot_i18` AS `bobot_i18`,`aspek_isi`.`i19` AS `i19`,`aspek_isi`.`bobot_i19` AS `bobot_i19`,`aspek_isi`.`i20` AS `i20`,`aspek_isi`.`bobot_i20` AS `bobot_i20`,`aspek_isi`.`i21` AS `i21`,`aspek_isi`.`bobot_i21` AS `bobot_i21`,`aspek_isi`.`i22` AS `i22`,`aspek_isi`.`bobot_i22` AS `bobot_i22`,`aspek_isi`.`i23` AS `i23`,`aspek_isi`.`bobot_i23` AS `bobot_i23`,`aspek_isi`.`i24` AS `i24`,`aspek_isi`.`bobot_i24` AS `bobot_i24`,`aspek_isi`.`i25` AS `i25`,`aspek_isi`.`bobot_i25` AS `bobot_i25`,`aspek_isi`.`i26` AS `i26`,`aspek_isi`.`bobot_i26` AS `bobot_i26`,`aspek_isi`.`i27` AS `i27`,`aspek_isi`.`bobot_i27` AS `bobot_i27`,`aspek_isi`.`i28` AS `i28`,`aspek_isi`.`bobot_i28` AS `bobot_i28`,`aspek_isi`.`i29` AS `i29`,`aspek_isi`.`bobot_i29` AS `bobot_i29`,`aspek_isi`.`i30` AS `i30`,`aspek_isi`.`bobot_i30` AS `bobot_i30`,`aspek_isi`.`i31` AS `i31`,`aspek_isi`.`bobot_i31` AS `bobot_i31`,`aspek_isi`.`i32` AS `i32`,`aspek_isi`.`bobot_i32` AS `bobot_i32`,`aspek_isi`.`i33` AS `i33`,`aspek_isi`.`bobot_i33` AS `bobot_i33`,`aspek_isi`.`i34` AS `i34`,`aspek_isi`.`bobot_i34` AS `bobot_i34`,`aspek_isi`.`i35` AS `i35`,`aspek_isi`.`bobot_i35` AS `bobot_i35`,`aspek_isi`.`i36` AS `i36`,`aspek_isi`.`bobot_i36` AS `bobot_i36`,`aspek_isi`.`i37` AS `i37`,`aspek_isi`.`bobot_i37` AS `bobot_i37`,`aspek_isi`.`i38` AS `i38`,`aspek_isi`.`bobot_i38` AS `bobot_i38`,`aspek_isi`.`i39` AS `i39`,`aspek_isi`.`bobot_i39` AS `bobot_i39`,`aspek_isi`.`i40` AS `i40`,`aspek_isi`.`bobot_i40` AS `bobot_i40`,`aspek_isi`.`i41` AS `i41`,`aspek_isi`.`bobot_i41` AS `bobot_i41`,`aspek_isi`.`i42` AS `i42`,`aspek_isi`.`bobot_i42` AS `bobot_i42`,`aspek_isi`.`i43` AS `i43`,`aspek_isi`.`bobot_i43` AS `bobot_i43`,`aspek_isi`.`i44` AS `i44`,`aspek_isi`.`bobot_i44` AS `bobot_i44`,`aspek_isi`.`i45` AS `i45`,`aspek_isi`.`bobot_i45` AS `bobot_i45`,`aspek_isi`.`i46` AS `i46`,`aspek_isi`.`bobot_i46` AS `bobot_i46`,`aspek_isi`.`i47` AS `i47`,`aspek_isi`.`bobot_i47` AS `bobot_i47`,`aspek_isi`.`bobot_aspek1` AS `bobot_aspek1`,`aspek_isi`.`bobot_aspek2` AS `bobot_aspek2`,`aspek_isi`.`bobot_aspek3` AS `bobot_aspek3`,`aspek_isi`.`bobot_aspek4` AS `bobot_aspek4`,`aspek_isi`.`bobot_aspek5` AS `bobot_aspek5`,`aspek_isi`.`bobot_aspek6` AS `bobot_aspek6`,`aspek_isi`.`bobot_aspek7` AS `bobot_aspek7`,`aspek_isi`.`bobot_aspek8` AS `bobot_aspek8`,`aspek_isi`.`bobot_domain1` AS `bobot_domain1`,`aspek_isi`.`bobot_domain2` AS `bobot_domain2`,`aspek_isi`.`bobot_domain3` AS `bobot_domain3`,`aspek_isi`.`bobot_domain4` AS `bobot_domain4`,`aspek_isi`.`aspek1` AS `aspek1`,`aspek_isi`.`aspek2` AS `aspek2`,`aspek_isi`.`aspek3` AS `aspek3`,`aspek_isi`.`aspek4` AS `aspek4`,`aspek_isi`.`aspek5` AS `aspek5`,`aspek_isi`.`aspek6` AS `aspek6`,`aspek_isi`.`aspek7` AS `aspek7`,`aspek_isi`.`aspek8` AS `aspek8`,round(((`aspek_isi`.`aspek1` * `aspek_isi`.`bobot_aspek1`) / `aspek_isi`.`bobot_domain1`),2) AS `domain1`,round(((((`aspek_isi`.`aspek2` * `aspek_isi`.`bobot_aspek2`) + (`aspek_isi`.`aspek3` * `aspek_isi`.`bobot_aspek3`)) + (`aspek_isi`.`aspek4` * `aspek_isi`.`bobot_aspek4`)) / `aspek_isi`.`bobot_domain2`),2) AS `domain2`,round((((`aspek_isi`.`aspek5` * `aspek_isi`.`bobot_aspek5`) + (`aspek_isi`.`aspek6` * `aspek_isi`.`bobot_aspek6`)) / `aspek_isi`.`bobot_domain3`),2) AS `domain3`,round((((`aspek_isi`.`aspek7` * `aspek_isi`.`bobot_aspek7`) + (`aspek_isi`.`aspek8` * `aspek_isi`.`bobot_aspek8`)) / `aspek_isi`.`bobot_domain4`),1) AS `domain4` from `aspek_isi`;

-- Dumping structure for view elaine_ta.indeks_isi
DROP VIEW IF EXISTS `indeks_isi`;
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `indeks_isi`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `indeks_isi` AS select `domain_isi`.`id` AS `id`,`domain_isi`.`nama` AS `nama`,`domain_isi`.`gi_id` AS `gi_id`,`domain_isi`.`gi_nama` AS `gi_nama`,`domain_isi`.`tp_id` AS `tp_id`,`domain_isi`.`tp_nama` AS `tp_nama`,`domain_isi`.`x` AS `x`,`domain_isi`.`y` AS `y`,`domain_isi`.`year` AS `year`,`domain_isi`.`i1` AS `i1`,`domain_isi`.`bobot_i1` AS `bobot_i1`,`domain_isi`.`i2` AS `i2`,`domain_isi`.`bobot_i2` AS `bobot_i2`,`domain_isi`.`i3` AS `i3`,`domain_isi`.`bobot_i3` AS `bobot_i3`,`domain_isi`.`i4` AS `i4`,`domain_isi`.`bobot_i4` AS `bobot_i4`,`domain_isi`.`i5` AS `i5`,`domain_isi`.`bobot_i5` AS `bobot_i5`,`domain_isi`.`i6` AS `i6`,`domain_isi`.`bobot_i6` AS `bobot_i6`,`domain_isi`.`i7` AS `i7`,`domain_isi`.`bobot_i7` AS `bobot_i7`,`domain_isi`.`i8` AS `i8`,`domain_isi`.`bobot_i8` AS `bobot_i8`,`domain_isi`.`i9` AS `i9`,`domain_isi`.`bobot_i9` AS `bobot_i9`,`domain_isi`.`i10` AS `i10`,`domain_isi`.`bobot_i10` AS `bobot_i10`,`domain_isi`.`i11` AS `i11`,`domain_isi`.`bobot_i11` AS `bobot_i11`,`domain_isi`.`i12` AS `i12`,`domain_isi`.`bobot_i12` AS `bobot_i12`,`domain_isi`.`i13` AS `i13`,`domain_isi`.`bobot_i13` AS `bobot_i13`,`domain_isi`.`i14` AS `i14`,`domain_isi`.`bobot_i14` AS `bobot_i14`,`domain_isi`.`i15` AS `i15`,`domain_isi`.`bobot_i15` AS `bobot_i15`,`domain_isi`.`i16` AS `i16`,`domain_isi`.`bobot_i16` AS `bobot_i16`,`domain_isi`.`i17` AS `i17`,`domain_isi`.`bobot_i17` AS `bobot_i17`,`domain_isi`.`i18` AS `i18`,`domain_isi`.`bobot_i18` AS `bobot_i18`,`domain_isi`.`i19` AS `i19`,`domain_isi`.`bobot_i19` AS `bobot_i19`,`domain_isi`.`i20` AS `i20`,`domain_isi`.`bobot_i20` AS `bobot_i20`,`domain_isi`.`i21` AS `i21`,`domain_isi`.`bobot_i21` AS `bobot_i21`,`domain_isi`.`i22` AS `i22`,`domain_isi`.`bobot_i22` AS `bobot_i22`,`domain_isi`.`i23` AS `i23`,`domain_isi`.`bobot_i23` AS `bobot_i23`,`domain_isi`.`i24` AS `i24`,`domain_isi`.`bobot_i24` AS `bobot_i24`,`domain_isi`.`i25` AS `i25`,`domain_isi`.`bobot_i25` AS `bobot_i25`,`domain_isi`.`i26` AS `i26`,`domain_isi`.`bobot_i26` AS `bobot_i26`,`domain_isi`.`i27` AS `i27`,`domain_isi`.`bobot_i27` AS `bobot_i27`,`domain_isi`.`i28` AS `i28`,`domain_isi`.`bobot_i28` AS `bobot_i28`,`domain_isi`.`i29` AS `i29`,`domain_isi`.`bobot_i29` AS `bobot_i29`,`domain_isi`.`i30` AS `i30`,`domain_isi`.`bobot_i30` AS `bobot_i30`,`domain_isi`.`i31` AS `i31`,`domain_isi`.`bobot_i31` AS `bobot_i31`,`domain_isi`.`i32` AS `i32`,`domain_isi`.`bobot_i32` AS `bobot_i32`,`domain_isi`.`i33` AS `i33`,`domain_isi`.`bobot_i33` AS `bobot_i33`,`domain_isi`.`i34` AS `i34`,`domain_isi`.`bobot_i34` AS `bobot_i34`,`domain_isi`.`i35` AS `i35`,`domain_isi`.`bobot_i35` AS `bobot_i35`,`domain_isi`.`i36` AS `i36`,`domain_isi`.`bobot_i36` AS `bobot_i36`,`domain_isi`.`i37` AS `i37`,`domain_isi`.`bobot_i37` AS `bobot_i37`,`domain_isi`.`i38` AS `i38`,`domain_isi`.`bobot_i38` AS `bobot_i38`,`domain_isi`.`i39` AS `i39`,`domain_isi`.`bobot_i39` AS `bobot_i39`,`domain_isi`.`i40` AS `i40`,`domain_isi`.`bobot_i40` AS `bobot_i40`,`domain_isi`.`i41` AS `i41`,`domain_isi`.`bobot_i41` AS `bobot_i41`,`domain_isi`.`i42` AS `i42`,`domain_isi`.`bobot_i42` AS `bobot_i42`,`domain_isi`.`i43` AS `i43`,`domain_isi`.`bobot_i43` AS `bobot_i43`,`domain_isi`.`i44` AS `i44`,`domain_isi`.`bobot_i44` AS `bobot_i44`,`domain_isi`.`i45` AS `i45`,`domain_isi`.`bobot_i45` AS `bobot_i45`,`domain_isi`.`i46` AS `i46`,`domain_isi`.`bobot_i46` AS `bobot_i46`,`domain_isi`.`i47` AS `i47`,`domain_isi`.`bobot_i47` AS `bobot_i47`,`domain_isi`.`bobot_aspek1` AS `bobot_aspek1`,`domain_isi`.`bobot_aspek2` AS `bobot_aspek2`,`domain_isi`.`bobot_aspek3` AS `bobot_aspek3`,`domain_isi`.`bobot_aspek4` AS `bobot_aspek4`,`domain_isi`.`bobot_aspek5` AS `bobot_aspek5`,`domain_isi`.`bobot_aspek6` AS `bobot_aspek6`,`domain_isi`.`bobot_aspek7` AS `bobot_aspek7`,`domain_isi`.`bobot_aspek8` AS `bobot_aspek8`,`domain_isi`.`bobot_domain1` AS `bobot_domain1`,`domain_isi`.`bobot_domain2` AS `bobot_domain2`,`domain_isi`.`bobot_domain3` AS `bobot_domain3`,`domain_isi`.`bobot_domain4` AS `bobot_domain4`,`domain_isi`.`aspek1` AS `aspek1`,`domain_isi`.`aspek2` AS `aspek2`,`domain_isi`.`aspek3` AS `aspek3`,`domain_isi`.`aspek4` AS `aspek4`,`domain_isi`.`aspek5` AS `aspek5`,`domain_isi`.`aspek6` AS `aspek6`,`domain_isi`.`aspek7` AS `aspek7`,`domain_isi`.`aspek8` AS `aspek8`,`domain_isi`.`domain1` AS `domain1`,`domain_isi`.`domain2` AS `domain2`,`domain_isi`.`domain3` AS `domain3`,`domain_isi`.`domain4` AS `domain4`,round((`domain_isi`.`i1` * `domain_isi`.`bobot_i1`),2) AS `i1_bobot`,round((`domain_isi`.`i2` * `domain_isi`.`bobot_i2`),2) AS `i2_bobot`,round((`domain_isi`.`i3` * `domain_isi`.`bobot_i3`),2) AS `i3_bobot`,round((`domain_isi`.`i4` * `domain_isi`.`bobot_i4`),2) AS `i4_bobot`,round((`domain_isi`.`i5` * `domain_isi`.`bobot_i5`),2) AS `i5_bobot`,round((`domain_isi`.`i6` * `domain_isi`.`bobot_i6`),2) AS `i6_bobot`,round((`domain_isi`.`i7` * `domain_isi`.`bobot_i7`),2) AS `i7_bobot`,round((`domain_isi`.`i8` * `domain_isi`.`bobot_i8`),2) AS `i8_bobot`,round((`domain_isi`.`i9` * `domain_isi`.`bobot_i9`),2) AS `i9_bobot`,round((`domain_isi`.`i10` * `domain_isi`.`bobot_i10`),2) AS `i10_bobot`,round((`domain_isi`.`i11` * `domain_isi`.`bobot_i11`),2) AS `i11_bobot`,round((`domain_isi`.`i12` * `domain_isi`.`bobot_i12`),2) AS `i12_bobot`,round((`domain_isi`.`i13` * `domain_isi`.`bobot_i13`),2) AS `i13_bobot`,round((`domain_isi`.`i14` * `domain_isi`.`bobot_i14`),2) AS `i14_bobot`,round((`domain_isi`.`i15` * `domain_isi`.`bobot_i15`),2) AS `i15_bobot`,round((`domain_isi`.`i16` * `domain_isi`.`bobot_i16`),2) AS `i16_bobot`,round((`domain_isi`.`i17` * `domain_isi`.`bobot_i17`),2) AS `i17_bobot`,round(((`domain_isi`.`i18` * `domain_isi`.`bobot_i18`) * 2),0) AS `i18_bobot`,round((`domain_isi`.`i19` * `domain_isi`.`bobot_i19`),2) AS `i19_bobot`,round((`domain_isi`.`i20` * `domain_isi`.`bobot_i20`),2) AS `i20_bobot`,round((`domain_isi`.`i21` * `domain_isi`.`bobot_i21`),2) AS `i21_bobot`,round((`domain_isi`.`i22` * `domain_isi`.`bobot_i22`),2) AS `i22_bobot`,round((`domain_isi`.`i23` * `domain_isi`.`bobot_i23`),2) AS `i23_bobot`,round((`domain_isi`.`i24` * `domain_isi`.`bobot_i24`),2) AS `i24_bobot`,round((`domain_isi`.`i25` * `domain_isi`.`bobot_i25`),2) AS `i25_bobot`,round((`domain_isi`.`i26` * `domain_isi`.`bobot_i26`),2) AS `i26_bobot`,round((`domain_isi`.`i27` * `domain_isi`.`bobot_i27`),2) AS `i27_bobot`,round((`domain_isi`.`i28` * `domain_isi`.`bobot_i28`),2) AS `i28_bobot`,round((`domain_isi`.`i29` * `domain_isi`.`bobot_i29`),2) AS `i29_bobot`,round((`domain_isi`.`i30` * `domain_isi`.`bobot_i30`),2) AS `i30_bobot`,round((`domain_isi`.`i31` * `domain_isi`.`bobot_i31`),2) AS `i31_bobot`,round((`domain_isi`.`i32` * `domain_isi`.`bobot_i32`),2) AS `i32_bobot`,round((`domain_isi`.`i33` * `domain_isi`.`bobot_i33`),2) AS `i33_bobot`,round((`domain_isi`.`i34` * `domain_isi`.`bobot_i34`),2) AS `i34_bobot`,round((`domain_isi`.`i35` * `domain_isi`.`bobot_i35`),2) AS `i35_bobot`,round((`domain_isi`.`i36` * `domain_isi`.`bobot_i36`),2) AS `i36_bobot`,round((`domain_isi`.`i37` * `domain_isi`.`bobot_i37`),2) AS `i37_bobot`,round((`domain_isi`.`i38` * `domain_isi`.`bobot_i38`),2) AS `i38_bobot`,round((`domain_isi`.`i39` * `domain_isi`.`bobot_i39`),2) AS `i39_bobot`,round((`domain_isi`.`i40` * `domain_isi`.`bobot_i40`),2) AS `i40_bobot`,round((`domain_isi`.`i41` * `domain_isi`.`bobot_i41`),2) AS `i41_bobot`,round((`domain_isi`.`i42` * `domain_isi`.`bobot_i42`),2) AS `i42_bobot`,round((`domain_isi`.`i43` * `domain_isi`.`bobot_i43`),2) AS `i43_bobot`,round((`domain_isi`.`i44` * `domain_isi`.`bobot_i44`),2) AS `i44_bobot`,round((`domain_isi`.`i45` * `domain_isi`.`bobot_i45`),2) AS `i45_bobot`,round((`domain_isi`.`i46` * `domain_isi`.`bobot_i46`),2) AS `i46_bobot`,round((`domain_isi`.`i47` * `domain_isi`.`bobot_i47`),2) AS `i47_bobot`,round((`domain_isi`.`aspek1` * `domain_isi`.`bobot_aspek1`),2) AS `aspek1_bobot`,round((`domain_isi`.`aspek2` * `domain_isi`.`bobot_aspek2`),2) AS `aspek2_bobot`,round((`domain_isi`.`aspek3` * `domain_isi`.`bobot_aspek3`),2) AS `aspek3_bobot`,round((`domain_isi`.`aspek4` * `domain_isi`.`bobot_aspek4`),2) AS `aspek4_bobot`,round((`domain_isi`.`aspek5` * `domain_isi`.`bobot_aspek5`),2) AS `aspek5_bobot`,round((`domain_isi`.`aspek6` * `domain_isi`.`bobot_aspek6`),2) AS `aspek6_bobot`,round((`domain_isi`.`aspek7` * `domain_isi`.`bobot_aspek7`),2) AS `aspek7_bobot`,round((`domain_isi`.`domain1` * `domain_isi`.`bobot_domain1`),2) AS `domain1_bobot`,round((`domain_isi`.`domain2` * `domain_isi`.`bobot_domain2`),2) AS `domain2_bobot`,round((`domain_isi`.`domain3` * `domain_isi`.`bobot_domain3`),2) AS `domain3_bobot`,round((`domain_isi`.`domain4` * `domain_isi`.`bobot_domain4`),2) AS `domain4_bobot`,round((((((`domain_isi`.`domain1` * `domain_isi`.`bobot_domain1`) + (`domain_isi`.`domain2` * `domain_isi`.`bobot_domain2`)) + (`domain_isi`.`domain3` * `domain_isi`.`bobot_domain3`)) + (`domain_isi`.`domain4` * `domain_isi`.`bobot_domain4`)) / 100),2) AS `indeks` from `domain_isi`;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
