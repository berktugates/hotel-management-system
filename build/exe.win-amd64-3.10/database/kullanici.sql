-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: otelveritabani
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `kullanici`
--

DROP TABLE IF EXISTS `kullanici`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kullanici` (
  `isim` varchar(45) DEFAULT NULL,
  `soyisim` varchar(45) DEFAULT NULL,
  `telefonno` varchar(45) DEFAULT NULL,
  `eposta` varchar(45) NOT NULL,
  `guvenliksorusu` varchar(45) DEFAULT NULL,
  `guvenlikcevabi` varchar(45) DEFAULT NULL,
  `sifre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`eposta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kullanici`
--

LOCK TABLES `kullanici` WRITE;
/*!40000 ALTER TABLE `kullanici` DISABLE KEYS */;
INSERT INTO `kullanici` VALUES ('Ayşe','Yılmaz','0483729823','ayilmaz@outlook.com','İlkokul Öğretmeninizin Adı','Mehmet','12345'),('Arda','Bekmez','537838033','bekmezarda@gmail.com','İlkokul Öğretmeninizin Adı','Ayşegül','20022002'),('Berk','Karataş','343489332','berkkaratas@gmail.com','İlkokul Öğretmeninizin Adı','Ali','110011'),('Berke','Ateş','9489430903','berktugates@gmail.com','İlkokul Öğretmeninizin Adı','Ali','19031903'),('Deneme','deneme','1234444','deneme@gmail.com','İlkokul Öğretmeninizin Adı','Robot','000'),('Kudret','Dinç','546434643','gshshrssrs','İlkokul Öğretmeninizin Adı','Ayşe','1111'),('İsmail','Çipe','05456531221','ismailgk@outlook.com','İlkokul Öğretmeninizin Adı','Alper','testt1999'),('Mehmet','Kaya','348257543','mehmetkaya@gmail.com','İlkokul Öğretmeninizin Adı','Fatma','123456'),('Mehmet','Taş','5445454543453','mehmettas@gmail.com','İlkokul Öğretmeninizin Adı','Fatma','112233'),('Melis','Saki','055555554422','melis@outlook.com','İlkokul Öğretmeninizin Adı','Meltem','12345678'),('Okan','Güler','05313747664','rambokan@gmail.com','İlkokul Öğretmeninizin Adı','Fatoş','aaaaa'),('Serhat','Gündoğdu','8372782372','serhatgun@gmail.com','İlkokul Öğretmeninizin Adı','Yasemin','serhatateshotel'),('Selim','Manav','7489403909034','sselimanav@outlook.com','İlkokul Öğretmeninizin Adı','Muhammed','101010'),('Mehmet','Tahtalı','2383820','tahtahlim@gmail.com','İlkokul Öğretmeninizin Adı','Harun','19861986'),('temel','yüce','05412578592','temely@gmail.com','İlkokul Öğretmeninizin Adı','oktay','123456');
/*!40000 ALTER TABLE `kullanici` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-29 12:55:47
