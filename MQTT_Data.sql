-- MySQL dump 10.13  Distrib 5.5.53, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: MQTT_Data
-- ------------------------------------------------------
-- Server version	5.5.53-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_dev`
--

DROP TABLE IF EXISTS `tb_dev`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_dev` (
  `device_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `device_name_foreign` char(4) NOT NULL,
  `device_intodepot_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `device_location_mode` tinyint(3) unsigned DEFAULT NULL,
  `device_batter_lowpower` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `device_batter_level` float(5,4) NOT NULL DEFAULT '0.0000',
  `device_location_gps_longitude` double(16,10) DEFAULT NULL,
  `device_location_gps_latitude` double(16,10) DEFAULT NULL,
  `device_location_gps_altitude` double(16,10) DEFAULT NULL,
  `device_location_gps_speed` double(16,10) DEFAULT NULL,
  `device_location_gps_longitude_direction` tinyint(3) unsigned DEFAULT NULL,
  `device_location_gps_latitude_direction` tinyint(3) unsigned DEFAULT NULL,
  `device_location_gps_altitude_direction` tinyint(3) unsigned DEFAULT NULL,
  `device_location_wifi_mac` char(20) DEFAULT NULL,
  `device_location_lbs_movecityid` char(4) DEFAULT NULL,
  `device_location_lbs_locationid` char(4) DEFAULT NULL,
  `device_location_lbs_villageid` char(4) DEFAULT NULL,
  `device_location_lbs_movenetid` char(4) DEFAULT NULL,
  `device_location_publish_intervaltime` char(2) DEFAULT NULL,
  `device_location_publish_phonenumber` char(26) DEFAULT NULL,
  `device_payload` char(100) DEFAULT NULL,
  PRIMARY KEY (`device_id`),
  KEY `foreign_key_dev` (`device_name_foreign`),
  CONSTRAINT `tb_dev_ibfk_1` FOREIGN KEY (`device_name_foreign`) REFERENCES `tb_usr_dev` (`dev_name_reference`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dev`
--

LOCK TABLES `tb_dev` WRITE;
/*!40000 ALTER TABLE `tb_dev` DISABLE KEYS */;
INSERT INTO `tb_dev` VALUES (1,'0005','2017-06-15 07:31:12',1,0,0.4118,121.9723600000,37.3874580000,2.0000000000,1.0000000000,1,1,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0169023a7cc2074526880002000101355907f2c607'),(2,'0005','2017-06-15 07:31:19',1,0,0.3961,121.9723600000,37.3874580000,2.0000000000,1.0000000000,1,1,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0165023a7cc2074526880002000101355907f2c607'),(3,'0005','2017-06-15 07:31:27',1,0,0.4118,121.9723600000,37.3874580000,2.0000000000,1.0000000000,1,1,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0169023a7cc2074526880002000101355907f2c607'),(4,'0005','2017-06-15 07:31:36',1,0,0.4118,121.9723600000,37.3874580000,2.0000000000,1.0000000000,1,1,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0169023a7cc2074526880002000101355907f2c607');
/*!40000 ALTER TABLE `tb_dev` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_usr`
--

DROP TABLE IF EXISTS `tb_usr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_usr` (
  `usr_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usr_name_reference` char(20) NOT NULL,
  `usr_pw` char(20) NOT NULL,
  PRIMARY KEY (`usr_id`),
  UNIQUE KEY `usr_name_reference` (`usr_name_reference`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_usr`
--

LOCK TABLES `tb_usr` WRITE;
/*!40000 ALTER TABLE `tb_usr` DISABLE KEYS */;
INSERT INTO `tb_usr` VALUES (1,'lz','123');
/*!40000 ALTER TABLE `tb_usr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_usr_dev`
--

DROP TABLE IF EXISTS `tb_usr_dev`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tb_usr_dev` (
  `usr_dev_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usr_name_foreign` char(20) NOT NULL,
  `dev_name_reference` char(4) NOT NULL,
  PRIMARY KEY (`usr_dev_id`),
  UNIQUE KEY `dev_name_reference` (`dev_name_reference`),
  KEY `foreign_key_usr` (`usr_name_foreign`),
  CONSTRAINT `tb_usr_dev_ibfk_1` FOREIGN KEY (`usr_name_foreign`) REFERENCES `tb_usr` (`usr_name_reference`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_usr_dev`
--

LOCK TABLES `tb_usr_dev` WRITE;
/*!40000 ALTER TABLE `tb_usr_dev` DISABLE KEYS */;
INSERT INTO `tb_usr_dev` VALUES (1,'lz','0005');
/*!40000 ALTER TABLE `tb_usr_dev` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-15  4:38:12
