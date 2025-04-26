CREATE DATABASE  IF NOT EXISTS `kokani_bazaar` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `kokani_bazaar`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: kokani_bazaar
-- ------------------------------------------------------
-- Server version	9.2.0

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
-- Table structure for table `alembic_version`

--
-- Table structure for table `alembic_version`
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*DROP TABLE IF EXISTS `alembic_version`;*/
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
/*CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;*/
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('01ef5c6470c0');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text,
  `image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Fruits','Fresh, organic fruits sourced directly from farms','/static/images/categories/fruits.jpg'),(2,'Dry Fruits','Premium quality dry fruits and nuts','/static/images/categories/dry-fruits.jpg'),(3,'Spices','Authentic spices to enhance your culinary experience','/static/images/categories/spices.jpg'),(4,'Oils','Pure, cold-pressed oils for cooking and health','/static/images/categories/oils.jpg'),(5,'Pulp','Natural fruit pulps for refreshing beverages','/static/images/categories/pulp.jpg'),(6,'Beverages','Traditional and refreshing drinks','/static/images/categories/beverages.jpg');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `zip` varchar(20) NOT NULL,
  `country` varchar(100) NOT NULL,
  `email` varchar(120) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `notes` text,
  `total` float NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `upi_transaction_id` varchar(100) DEFAULT NULL,
  `payment_status` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,1,'omkar','dhuri','Ap wadivaravade mahapurushwadi','Kudal','Maharashtra','416520','IN','dhuri8973@gmail.com','08208463990','',1005,'upi',NULL,'pending','pending','2025-04-16 19:09:00'),(2,2,'OMKAR','DHURI','manishanagar kalwa, thane west 416520','thane','Maharashtra','416520','IN','dhuri8973@gmail.com','08208463990','',405,'upi',NULL,'pending','pending','2025-04-20 17:06:51');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_item`
--

DROP TABLE IF EXISTS `order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `order_item_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  CONSTRAINT `order_item_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_item`
--

LOCK TABLES `order_item` WRITE;
/*!40000 ALTER TABLE `order_item` DISABLE KEYS */;
INSERT INTO `order_item` VALUES (1,1,1,1,1000),(2,2,3,1,400);
/*!40000 ALTER TABLE `order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text,
  `price` float NOT NULL,
  `original_price` float DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `category_id` int NOT NULL,
  `featured` tinyint(1) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `origin` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Organic Alphonso Mangoes','Sweet and aromatic Alphonso mangoes, known as the king of fruits',1000,1100,'/static/images/products/alphonso-mangoes.jpg',1,1,4.8,999,'1 kg','Devgad, Maharashtra','2025-04-16 16:52:46'),(2,'Premium Cashews','Large, crunchy cashews, perfect for snacking or cooking',1000,1200,'/static/images/products/cashews.jpg',2,1,4.6,1000,'1 kg','vengurla,maharashtra','2025-04-16 16:52:47'),(3,'Kokam','Traditional fruit known for its culinary and medicinal properties',400,NULL,'/static/images/products/kokam.jpg',1,0,4.3,799,'1kg','vengurla,maharshtra','2025-04-16 16:52:47'),(4,'Cold Pressed Coconut Oil','Pure, cold-pressed coconut oil, ideal for cooking and skincare',300,350,'/static/images/products/coconut-oil.jpg',4,1,4.9,500,'1 L','vengurla,maharshtra','2025-04-16 16:52:47'),(5,'Natural Mango Pulp','Sweet mango pulp, perfect for smoothies, desserts, and beverages',300,NULL,'/static/images/products/mango-pulp.jpg',5,0,4.5,45,'500 ml','vengurla,Maharashtra','2025-04-16 16:52:47'),(6,'Kokam Sarbat','Refreshing traditional beverage with digestive properties',150,NULL,'/static/images/products/kokam-sarbat.jpg',6,1,4.4,60,'500 ml','Konkan Region','2025-04-16 16:52:47'),(7,'Amla Sarbat','Vitamin C rich traditional drink made from Indian gooseberries',150,NULL,'/static/images/products/amla-sarbat.jpg',6,0,4.2,55,'500 ml','vengurla,maharashtra','2025-04-16 16:52:47');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Omkar Dhuri','dhuri8973@gmail.com','pbkdf2:sha256:600000$gYSJc9i3XmiG9VJS$ded0929da11654b0ee09c64ac1e3c6f709d13328f3f39048c1c6908b8d2cce90','2025-04-16 16:52:47'),(2,'Shailesh Bhagat','bhagatshailu91@gmail.com','pbkdf2:sha256:600000$TMEQoIJSTBT9xD96$d30fb9165e44fa71f6bc9d9feb2057b71421ba7356369bb98f78eaa1d4e70274','2025-04-20 17:00:13');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'kokani_bazaar'
--

--
-- Dumping routines for database 'kokani_bazaar'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-25 12:43:07
