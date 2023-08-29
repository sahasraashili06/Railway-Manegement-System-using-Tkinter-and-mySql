-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 28, 2023 at 11:04 AM
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
-- Database: `railway`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `nm1` varchar(50) NOT NULL,
  `cont1` varchar(50) NOT NULL,
  `gen1` varchar(10) NOT NULL,
  `em2` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `pwd1` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`nm1`, `cont1`, `gen1`, `em2`, `pwd`, `pwd1`) VALUES
('sanku', '78994612', 'Male', 'sanku@gmail.com', '123', '123'),
('sanku', '78994612', 'Male', 'sanku@gmail.com', '123', '123'),
('sanku', '78994612', 'Male', 'sanku@gmail.com', '123', '123'),
('dhie', '58746986', 'Male', 'dhie@gmail.com', '123', '123'),
('hillo', '57741924', 'Male', 'hillo@gmail.com', '123', '123'),
('sandip', '47862130', 'Male', 'sandip@gmail.com', '456', '456'),
('abc', '47613513', 'Male', 'abc@gmail.com', '789', '789');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
