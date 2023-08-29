-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 28, 2023 at 11:03 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rail`
--

-- --------------------------------------------------------

--
-- Table structure for table `data2`
--

CREATE TABLE `data2` (
  `trs1` varchar(50) NOT NULL,
  `trd1` varchar(50) NOT NULL,
  `cl1` varchar(10) NOT NULL,
  `nop1` varchar(50) NOT NULL,
  `pay1` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data2`
--

INSERT INTO `data2` (`trs1`, `trd1`, `cl1`, `nop1`, `pay1`) VALUES
('Punjab', 'Punjab', 'AC Chair c', '3', 'PhonePay'),
('Andhra Pradesh', 'Bihar', 'AC Chair c', '5', 'G-pay'),
('Bihar', 'Punjab', 'Sleeper', '5', 'G-pay'),
('Assam', 'Punjab', 'AC 2 Tier', '8', 'PhonePay');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
