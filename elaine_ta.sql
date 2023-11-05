-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 05, 2023 at 12:27 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elaine_ta`
--

-- --------------------------------------------------------

--
-- Table structure for table `aspek`
--

CREATE TABLE `aspek` (
  `id` varchar(25) NOT NULL,
  `domain` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `bobot` decimal(11,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `aspek`
--

INSERT INTO `aspek` (`id`, `domain`, `nama`, `bobot`) VALUES
('a2023110400001', 'd2023110400001', 'Aspek 1', '13.00'),
('a2023110400002', 'd2023110400002', 'Aspek 2', '10.00'),
('a2023110400003', 'd2023110400002', 'Aspek 3', '10.00'),
('a2023110400004', 'd2023110400002', 'Aspek 4', '5.00'),
('a2023110400005', 'd2023110400003', 'Aspek 5', '12.00'),
('a2023110400006', 'd2023110400003', 'Aspek 6', '4.50'),
('a2023110400007', 'd2023110400004', 'Aspek 7', '27.50'),
('a2023110400008', 'd2023110400004', 'Aspek 8', '18.00');

-- --------------------------------------------------------

--
-- Table structure for table `domain`
--

CREATE TABLE `domain` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `bobot` decimal(11,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `domain`
--

INSERT INTO `domain` (`id`, `nama`, `bobot`) VALUES
('d2023110400001', 'Domain 1', '13.00'),
('d2023110400002', 'Domain 2', '25.00'),
('d2023110400003', 'Domain 3', '16.50'),
('d2023110400004', 'Domain 4', '14.50');

-- --------------------------------------------------------

--
-- Table structure for table `grup_instansi`
--

CREATE TABLE `grup_instansi` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `grup_instansi`
--

INSERT INTO `grup_instansi` (`id`, `nama`) VALUES
('gi2023110400001', 'Kementrian Pusat'),
('gi2023110400002', 'Instansi Lainnya Pusat'),
('gi2023110400003', 'Lembaga Non Struktural Pusat'),
('gi2023110400004', 'Lembaga Pemerintah Non Kementerian Pusat'),
('gi2023110400005', 'Pemerintah Kabupaten Aceh'),
('gi2023110400006', 'Pemerintah Kabupaten Bali'),
('gi2023110400007', 'Pemerintah Kabupaten Banten'),
('gi2023110400008', 'Pemerintah Kabupaten Bengkulu'),
('gi2023110400009', 'Pemerintah Kabupaten Gorontalo'),
('gi2023110400010', 'Pemerintah Kabupaten Jambi'),
('gi2023110400011', 'Pemerintah Kabupaten Jawa Barat'),
('gi2023110400012', 'Pemerintah Kabupaten Jawa Tengah'),
('gi2023110400013', 'Pemerintah Kabupaten Jawa Timur'),
('gi2023110400014', 'Pemerintah Kabupaten Kalimantan Barat'),
('gi2023110400015', 'Pemerintah Kabupaten Kalimantan Selatan'),
('gi2023110400016', 'Pemerintah Kabupaten Kalimantan Tengah'),
('gi2023110400017', 'Pemerintah Kabupaten Kalimantan Timur'),
('gi2023110400018', 'Pemerintah Kabupaten Kalimantan Utara'),
('gi2023110400019', 'Pemerintah Kabupaten Kepulauan Bangka Belitung'),
('gi2023110400020', 'Pemerintah Kabupaten Lampung'),
('gi2023110400021', 'Pemerintah Kabupaten Maluku'),
('gi2023110400022', 'Pemerintah Kabupaten Maluku Utara'),
('gi2023110400023', 'Pemerintah Kabupaten Nusa Tengara Barat'),
('gi2023110400024', 'Pemerintah Kabupaten Nusa Tengara Timur'),
('gi2023110400025', 'Pemerintah Kabupaten Papua'),
('gi2023110400026', 'Pemerintah Kabupaten Papua Barat'),
('gi2023110400027', 'Pemerintah Kabupaten Riau'),
('gi2023110400028', 'Pemerintah Kabupaten Sulawesi Barat'),
('gi2023110400029', 'Pemerintah Kabupaten Sulawesi Selatan'),
('gi2023110400030', 'Pemerintah Kabupaten Sulawesi Tengah'),
('gi2023110400031', 'Pemerintah Kabupaten Sulawesi Tenggara'),
('gi2023110400032', 'Pemerintah Kabupaten Sulawesi Utara'),
('gi2023110400033', 'Pemerintah Kabupaten Sumatra Barat'),
('gi2023110400034', 'Pemerintah Kabupaten Sumatra Selatan'),
('gi2023110400035', 'Pemerintah Kabupaten Sumatra Utara'),
('gi2023110400036', 'Pemerintah Kabupaten Yogyakarta'),
('gi2023110400037', 'Pemerintah Kota Jambi'),
('gi2023110400038', 'Pemerintah Kota Jawa Barat'),
('gi2023110400039', 'Pemerintah Kota Jawa Tengah'),
('gi2023110400040', 'Pemerintah Kota Jawa Timur'),
('gi2023110400041', 'Pemerintah Kota Kalimantan Barat'),
('gi2023110400042', 'Pemerintah Kota Kalimantan Selatan'),
('gi2023110400043', 'Pemerintah Kota Kalimantan Tengah'),
('gi2023110400044', 'Pemerintah Kota Kalimantan Timur'),
('gi2023110400045', 'Pemerintah Kota Kalimantan Utara'),
('gi2023110400046', 'Pemerintah Kota Kepulauan Bangka Belitung'),
('gi2023110400047', 'Pemerintah Kota Lampung'),
('gi2023110400048', 'Pemerintah Kota Maluku'),
('gi2023110400049', 'Pemerintah Kota Maluku Utara'),
('gi2023110400050', 'Pemerintah Kota Nusa Tengara Barat'),
('gi2023110400051', 'Pemerintah Kota Papua'),
('gi2023110400052', 'Pemerintah Kota Papua Barat'),
('gi2023110400053', 'Pemerintah Kota Riau'),
('gi2023110400054', 'Pemerintah Kota Sulawesi Selatan'),
('gi2023110400055', 'Pemerintah Kota Sulawesi Tengah'),
('gi2023110400056', 'Pemerintah Kota Sulawesi Tenggara'),
('gi2023110400057', 'Pemerintah Kota Sulawesi Utara'),
('gi2023110400058', 'Pemerintah Kota Sumatra Barat'),
('gi2023110400059', 'Pemerintah Kota Sumatra Selatan'),
('gi2023110400060', 'Pemerintah Kota Sumatra Utara'),
('gi2023110400061', 'Pemerintah Kota Yogyakarta'),
('gi2023110400062', 'Pemerintah Provinsi Aceh'),
('gi2023110400063', 'Pemerintah Provinsi Bali'),
('gi2023110400064', 'Pemerintah Provinsi Banten'),
('gi2023110400065', 'Pemerintah Provinsi Bengkulu'),
('gi2023110400066', 'Pemerintah Provinsi Gorontalo'),
('gi2023110400067', 'Pemerintah Provinsi Jakarta'),
('gi2023110400068', 'Pemerintah Provinsi Jambi'),
('gi2023110400069', 'Pemerintah Provinsi Jawa Barat'),
('gi2023110400070', 'Pemerintah Provinsi Jawa Tengah'),
('gi2023110400071', 'Pemerintah Provinsi Jawa Timur'),
('gi2023110400072', 'Pemerintah Provinsi Kalimantan Selatan'),
('gi2023110400073', 'Pemerintah Provinsi Kalimantan Tengah'),
('gi2023110400074', 'Pemerintah Provinsi Kalimantan Timur'),
('gi2023110400075', 'Pemerintah Provinsi Kalimantan Utara'),
('gi2023110400076', 'Pemerintah Provinsi Kepulauan Bangka Belitung'),
('gi2023110400077', 'Pemerintah Provinsi Lampung'),
('gi2023110400078', 'Pemerintah Provinsi Maluku'),
('gi2023110400079', 'Pemerintah Provinsi Maluku Utara'),
('gi2023110400080', 'Pemerintah Provinsi Nusa Tengara Barat'),
('gi2023110400081', 'Pemerintah Provinsi Nusa Tengara Timur'),
('gi2023110400082', 'Pemerintah Provinsi Riau'),
('gi2023110400083', 'Pemerintah Provinsi Sulawesi Barat'),
('gi2023110400084', 'Pemerintah Provinsi Sulawesi Selatan'),
('gi2023110400085', 'Pemerintah Provinsi Sulawesi Tengah'),
('gi2023110400086', 'Pemerintah Provinsi Sulawesi Tenggara'),
('gi2023110400087', 'Pemerintah Provinsi Sulawesi Utara'),
('gi2023110400088', 'Pemerintah Provinsi Sumatra Barat'),
('gi2023110400089', 'Pemerintah Provinsi Sumatra Utara'),
('gi2023110400090', 'Pemerintah Provinsi Yogyakarta');

-- --------------------------------------------------------

--
-- Table structure for table `indikator`
--

CREATE TABLE `indikator` (
  `id` varchar(25) NOT NULL,
  `aspek` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `bobot` decimal(11,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `indikator`
--

INSERT INTO `indikator` (`id`, `aspek`, `nama`, `bobot`) VALUES
('in2023110400001', 'a2023110400001', 'I1', '1.30'),
('in2023110400002', 'a2023110400001', 'I2', '1.30'),
('in2023110400003', 'a2023110400001', 'I3', '1.30'),
('in2023110400004', 'a2023110400001', 'I4', '1.30'),
('in2023110400005', 'a2023110400001', 'I5', '1.30'),
('in2023110400006', 'a2023110400001', 'I6', '1.30'),
('in2023110400007', 'a2023110400001', 'I7', '1.30'),
('in2023110400008', 'a2023110400001', 'I8', '1.30'),
('in2023110400009', 'a2023110400001', 'I9', '1.30'),
('in2023110400010', 'a2023110400001', 'I10', '1.30'),
('in2023110400011', 'a2023110400002', 'I11', '2.50'),
('in2023110400012', 'a2023110400002', 'I12', '2.50'),
('in2023110400013', 'a2023110400002', 'I13', '2.50'),
('in2023110400014', 'a2023110400002', 'I14', '2.50'),
('in2023110400015', 'a2023110400003', 'I15', '2.50'),
('in2023110400016', 'a2023110400003', 'I16', '2.50'),
('in2023110400017', 'a2023110400003', 'I17', '2.50'),
('in2023110400018', 'a2023110400003', 'I18', '2.50'),
('in2023110400019', 'a2023110400004', 'I19', '2.50'),
('in2023110400020', 'a2023110400004', 'I20', '2.50'),
('in2023110400021', 'a2023110400005', 'I21', '1.50'),
('in2023110400022', 'a2023110400005', 'I22', '1.50'),
('in2023110400023', 'a2023110400005', 'I23', '1.50'),
('in2023110400024', 'a2023110400005', 'I24', '1.50'),
('in2023110400025', 'a2023110400005', 'I25', '1.50'),
('in2023110400026', 'a2023110400005', 'I26', '1.50'),
('in2023110400027', 'a2023110400005', 'I27', '1.50'),
('in2023110400028', 'a2023110400005', 'I28', '1.50'),
('in2023110400029', 'a2023110400006', 'I29', '1.50'),
('in2023110400030', 'a2023110400006', 'I30', '1.50'),
('in2023110400031', 'a2023110400006', 'I31', '1.50'),
('in2023110400032', 'a2023110400007', 'I32', '2.75'),
('in2023110400033', 'a2023110400007', 'I33', '2.75'),
('in2023110400034', 'a2023110400007', 'I34', '2.75'),
('in2023110400035', 'a2023110400007', 'I35', '2.75'),
('in2023110400036', 'a2023110400007', 'I36', '2.75'),
('in2023110400037', 'a2023110400007', 'I37', '2.75'),
('in2023110400038', 'a2023110400007', 'I38', '2.75'),
('in2023110400039', 'a2023110400007', 'I39', '2.75'),
('in2023110400040', 'a2023110400007', 'I40', '2.75'),
('in2023110400041', 'a2023110400007', 'I41', '2.75'),
('in2023110400042', 'a2023110400008', 'I42', '3.00'),
('in2023110400043', 'a2023110400008', 'I43', '3.00'),
('in2023110400044', 'a2023110400008', 'I44', '3.00'),
('in2023110400045', 'a2023110400008', 'I45', '3.00'),
('in2023110400046', 'a2023110400008', 'I46', '3.00'),
('in2023110400047', 'a2023110400008', 'I47', '3.00');

-- --------------------------------------------------------

--
-- Table structure for table `instansi`
--

CREATE TABLE `instansi` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `group_instansi` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `instansi`
--

INSERT INTO `instansi` (`id`, `nama`, `group_instansi`) VALUES
('i2023110200001', 'Kementerian Koordinator Bidang Politik, Hukum dan Keamanan', 'gi2023110400001'),
('i2023110200002', 'Kejaksaan Agung', 'gi2023110400002');

-- --------------------------------------------------------

--
-- Table structure for table `isi`
--

CREATE TABLE `isi` (
  `instansi` varchar(25) NOT NULL,
  `indikator` varchar(25) NOT NULL,
  `value` decimal(11,2) NOT NULL,
  `year` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `isi`
--

INSERT INTO `isi` (`instansi`, `indikator`, `value`, `year`) VALUES
('i2023110200001', 'in2023110400001', '3.00', 2022),
('i2023110200001', 'in2023110400002', '3.00', 2022),
('i2023110200001', 'in2023110400003', '3.00', 2022),
('i2023110200001', 'in2023110400004', '3.00', 2022),
('i2023110200001', 'in2023110400005', '3.00', 2022),
('i2023110200001', 'in2023110400006', '3.00', 2022),
('i2023110200001', 'in2023110400007', '3.00', 2022),
('i2023110200001', 'in2023110400008', '3.00', 2022),
('i2023110200001', 'in2023110400009', '2.00', 2022),
('i2023110200001', 'in2023110400010', '3.00', 2022),
('i2023110200001', 'in2023110400011', '1.00', 2022),
('i2023110200001', 'in2023110400012', '1.00', 2022),
('i2023110200001', 'in2023110400013', '3.00', 2022),
('i2023110200001', 'in2023110400014', '4.00', 2022),
('i2023110200001', 'in2023110400015', '3.00', 2022),
('i2023110200001', 'in2023110400016', '3.00', 2022),
('i2023110200001', 'in2023110400017', '3.00', 2022),
('i2023110200001', 'in2023110400018', '3.00', 2022),
('i2023110200001', 'in2023110400019', '3.00', 2022),
('i2023110200001', 'in2023110400020', '4.00', 2022),
('i2023110200001', 'in2023110400021', '2.00', 2022),
('i2023110200001', 'in2023110400022', '4.00', 2022),
('i2023110200001', 'in2023110400023', '2.00', 2022),
('i2023110200001', 'in2023110400024', '4.00', 2022),
('i2023110200001', 'in2023110400025', '2.00', 2022),
('i2023110200001', 'in2023110400026', '3.00', 2022),
('i2023110200001', 'in2023110400027', '1.00', 2022),
('i2023110200001', 'in2023110400028', '2.00', 2022),
('i2023110200001', 'in2023110400029', '1.00', 2022),
('i2023110200001', 'in2023110400030', '1.00', 2022),
('i2023110200001', 'in2023110400031', '1.00', 2022),
('i2023110200001', 'in2023110400032', '3.00', 2022),
('i2023110200001', 'in2023110400033', '3.00', 2022),
('i2023110200001', 'in2023110400034', '3.00', 2022),
('i2023110200001', 'in2023110400035', '3.00', 2022),
('i2023110200001', 'in2023110400036', '4.00', 2022),
('i2023110200001', 'in2023110400037', '4.00', 2022),
('i2023110200001', 'in2023110400038', '4.00', 2022),
('i2023110200001', 'in2023110400039', '4.00', 2022),
('i2023110200001', 'in2023110400040', '4.00', 2022),
('i2023110200001', 'in2023110400041', '3.00', 2022),
('i2023110200001', 'in2023110400042', '4.00', 2022),
('i2023110200001', 'in2023110400043', '1.00', 2022),
('i2023110200001', 'in2023110400044', '4.00', 2022),
('i2023110200001', 'in2023110400045', '3.00', 2022),
('i2023110200001', 'in2023110400046', '3.00', 2022),
('i2023110200001', 'in2023110400047', '3.00', 2022);

-- --------------------------------------------------------

--
-- Table structure for table `predikat`
--

CREATE TABLE `predikat` (
  `id` varchar(25) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `batas_bawah` decimal(11,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `predikat`
--

INSERT INTO `predikat` (`id`, `nama`, `batas_bawah`) VALUES
('p2023110200001', 'Cukup', '1.80'),
('p2023110200002', 'Baik', '2.60'),
('p2023110200003', 'Sangat Baik', '3.50'),
('p2023110200004', 'Memuaskan', '4.20');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aspek`
--
ALTER TABLE `aspek`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `domain`
--
ALTER TABLE `domain`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `indikator`
--
ALTER TABLE `indikator`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `instansi`
--
ALTER TABLE `instansi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `isi`
--
ALTER TABLE `isi`
  ADD PRIMARY KEY (`instansi`,`indikator`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
