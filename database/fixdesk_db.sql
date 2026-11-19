CREATE DATABASE  IF NOT EXISTS `fixdesk_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `fixdesk_db`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: fixdesk_db
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `diagnostico`
--

DROP TABLE IF EXISTS `diagnostico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnostico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `orden_id` int NOT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `fecha_actualizacion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orden_id` (`orden_id`),
  CONSTRAINT `diagnostico_ibfk_1` FOREIGN KEY (`orden_id`) REFERENCES `orden_reparacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnostico`
--

LOCK TABLES `diagnostico` WRITE;
/*!40000 ALTER TABLE `diagnostico` DISABLE KEYS */;
INSERT INTO `diagnostico` VALUES (1,2,'Se detectó sobrecalentamiento del procesador por acumulación de polvo y pasta térmica deteriorada. Luego de la reparación las temperaturas se normalizaron.','2026-11-18 15:57:29','2026-11-18 21:26:10'),(2,3,'Se detectó lentitud general provocada por acumulación de archivos temporales y procesos innecesarios en segundo plano.','2026-11-18 23:05:17','2026-11-18 23:05:17'),(3,4,'Se detectó lentitud general provocada por acumulación de archivos temporales, programas innecesarios en el inicio y procesos ejecutándose en segundo plano.','2026-11-18 23:57:17','2026-11-18 23:57:17'),(4,5,'Definitivamente el celular no prende.','2026-11-19 01:12:00','2026-11-19 01:12:00');
/*!40000 ALTER TABLE `diagnostico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo`
--

DROP TABLE IF EXISTS `equipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `tipo` enum('NOTEBOOK','CELULAR','TABLET') COLLATE utf8mb4_unicode_ci NOT NULL,
  `marca` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `modelo` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `numero_serie` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_registro` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`),
  CONSTRAINT `equipo_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo`
--

LOCK TABLES `equipo` WRITE;
/*!40000 ALTER TABLE `equipo` DISABLE KEYS */;
INSERT INTO `equipo` VALUES (1,3,'NOTEBOOK','Lenovo','ThinkPad E14','FD-TEST-001',1,'2026-11-18 15:16:01'),(2,5,'NOTEBOOK','HP','Pavilion 15','HP-MARIA-001',1,'2026-11-18 23:51:11'),(3,6,'CELULAR','Samsung','Galaxy S20','Samsung-01 Pepito',1,'2026-11-19 01:06:14');
/*!40000 ALTER TABLE `equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_estado`
--

DROP TABLE IF EXISTS `historial_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_estado` (
  `id` int NOT NULL AUTO_INCREMENT,
  `orden_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `estado_anterior` enum('RECIBIDO','EN_DIAGNOSTICO','EN_REPARACION','LISTO_PARA_RETIRAR','FINALIZADO','CANCELADO') COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado_nuevo` enum('RECIBIDO','EN_DIAGNOSTICO','EN_REPARACION','LISTO_PARA_RETIRAR','FINALIZADO','CANCELADO') COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_cambio` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orden_id` (`orden_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `historial_estado_ibfk_1` FOREIGN KEY (`orden_id`) REFERENCES `orden_reparacion` (`id`),
  CONSTRAINT `historial_estado_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_estado`
--

LOCK TABLES `historial_estado` WRITE;
/*!40000 ALTER TABLE `historial_estado` DISABLE KEYS */;
INSERT INTO `historial_estado` VALUES (1,1,2,'RECIBIDO','EN_DIAGNOSTICO','2026-11-18 15:23:10'),(2,1,2,'EN_DIAGNOSTICO','EN_REPARACION','2026-11-18 15:36:01'),(3,1,2,'EN_REPARACION','LISTO_PARA_RETIRAR','2026-11-18 15:36:01'),(4,2,2,'RECIBIDO','EN_DIAGNOSTICO','2026-11-18 15:57:18'),(5,2,2,'EN_DIAGNOSTICO','EN_REPARACION','2026-11-18 15:57:38'),(6,2,2,'EN_REPARACION','LISTO_PARA_RETIRAR','2026-11-18 21:28:59'),(7,3,4,'RECIBIDO','EN_DIAGNOSTICO','2026-11-18 23:04:17'),(8,3,4,'EN_DIAGNOSTICO','EN_REPARACION','2026-11-18 23:05:52'),(9,3,4,'EN_REPARACION','LISTO_PARA_RETIRAR','2026-11-18 23:07:29'),(10,4,4,'RECIBIDO','EN_DIAGNOSTICO','2026-11-18 23:56:46'),(11,4,4,'EN_DIAGNOSTICO','EN_REPARACION','2026-11-18 23:57:44'),(12,4,4,'EN_REPARACION','LISTO_PARA_RETIRAR','2026-11-18 23:58:21'),(13,4,4,'LISTO_PARA_RETIRAR','FINALIZADO','2026-11-19 00:18:20'),(14,5,7,'RECIBIDO','EN_DIAGNOSTICO','2026-11-19 01:11:40'),(15,5,7,'EN_DIAGNOSTICO','EN_REPARACION','2026-11-19 01:12:35'),(16,5,7,'EN_REPARACION','LISTO_PARA_RETIRAR','2026-11-19 01:13:00');
/*!40000 ALTER TABLE `historial_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificacion`
--

DROP TABLE IF EXISTS `notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notificacion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `orden_id` int NOT NULL,
  `mensaje` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `leida` tinyint(1) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `orden_id` (`orden_id`),
  CONSTRAINT `notificacion_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `notificacion_ibfk_2` FOREIGN KEY (`orden_id`) REFERENCES `orden_reparacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificacion`
--

LOCK TABLES `notificacion` WRITE;
/*!40000 ALTER TABLE `notificacion` DISABLE KEYS */;
INSERT INTO `notificacion` VALUES (1,3,1,'Tu equipo ya se encuentra listo para retirar.',1,'2026-11-18 15:36:01'),(2,3,2,'Tu equipo ya se encuentra listo para retirar.',1,'2026-11-18 21:28:59'),(3,3,3,'Tu equipo ya se encuentra listo para retirar.',1,'2026-11-18 23:07:29'),(4,5,4,'Tu equipo ya se encuentra listo para retirar.',1,'2026-11-18 23:58:21'),(5,6,5,'Tu equipo ya se encuentra listo para retirar.',1,'2026-11-19 01:13:00');
/*!40000 ALTER TABLE `notificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden_reparacion`
--

DROP TABLE IF EXISTS `orden_reparacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_reparacion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `equipo_id` int NOT NULL,
  `tecnico_id` int DEFAULT NULL,
  `problema_reportado` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `prioridad` enum('BAJA','NORMAL','ALTA','URGENTE') COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado_actual` enum('RECIBIDO','EN_DIAGNOSTICO','EN_REPARACION','LISTO_PARA_RETIRAR','FINALIZADO','CANCELADO') COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_recepcion` datetime NOT NULL,
  `fecha_estimada` date DEFAULT NULL,
  `fecha_finalizacion` datetime DEFAULT NULL,
  `observaciones` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `equipo_id` (`equipo_id`),
  KEY `tecnico_id` (`tecnico_id`),
  CONSTRAINT `orden_reparacion_ibfk_1` FOREIGN KEY (`equipo_id`) REFERENCES `equipo` (`id`),
  CONSTRAINT `orden_reparacion_ibfk_2` FOREIGN KEY (`tecnico_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_reparacion`
--

LOCK TABLES `orden_reparacion` WRITE;
/*!40000 ALTER TABLE `orden_reparacion` DISABLE KEYS */;
INSERT INTO `orden_reparacion` VALUES (1,1,2,'La notebook no enciende y no muestra señales de energía.','NORMAL','LISTO_PARA_RETIRAR','2026-11-18 15:18:34',NULL,NULL,'Equipo recibido con cargador.'),(2,1,2,'La notebook enciende pero se apaga después de unos minutos.','NORMAL','LISTO_PARA_RETIRAR','2026-11-18 15:57:13',NULL,NULL,'Posible problema de temperatura.'),(3,1,4,'El equipo presenta lentitud general y reinicios inesperados.','URGENTE','LISTO_PARA_RETIRAR','2026-11-18 22:32:18',NULL,NULL,'Se solicita revisión general del sistema.'),(4,2,4,'La notebook presenta lentitud general y se reinicia inesperadamente.','ALTA','FINALIZADO','2026-11-18 23:53:48',NULL,'2026-11-19 00:18:20','El cliente solicita revisión general del equipo.'),(5,3,7,'Se mojó el celular y no prendió mas.','ALTA','LISTO_PARA_RETIRAR','2026-11-19 01:08:07',NULL,NULL,'El cliente necesita con urgencia su dispositivo ya que lo utiliza para trabajar.');
/*!40000 ALTER TABLE `orden_reparacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarea_reparacion`
--

DROP TABLE IF EXISTS `tarea_reparacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarea_reparacion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `orden_id` int NOT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_realizacion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orden_id` (`orden_id`),
  CONSTRAINT `tarea_reparacion_ibfk_1` FOREIGN KEY (`orden_id`) REFERENCES `orden_reparacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarea_reparacion`
--

LOCK TABLES `tarea_reparacion` WRITE;
/*!40000 ALTER TABLE `tarea_reparacion` DISABLE KEYS */;
INSERT INTO `tarea_reparacion` VALUES (1,2,'Limpieza interna completa del sistema de refrigeración.','2026-11-18 15:57:45'),(2,2,'Reemplazo de pasta térmica y prueba de temperaturas.','2026-11-18 15:57:56'),(3,2,'Prueba final de estabilidad y control de temperatura.','2026-11-18 21:25:20'),(4,3,'Limpieza de archivos temporales y optimización del inicio del sistema.','2026-11-18 23:06:32'),(5,3,'Revisión de procesos en segundo plano y prueba general de rendimiento.','2026-11-18 23:07:03'),(6,4,'Limpieza de archivos temporales y optimización de programas de inicio.','2026-11-18 23:57:56'),(7,4,'Revisión de procesos en segundo plano y prueba general de rendimiento.','2026-11-18 23:58:02'),(8,5,'El celular se estuvo revisando por dentro.','2026-11-19 01:12:43'),(9,5,'Queremos terminar de revisarlo.','2026-11-19 01:13:48');
/*!40000 ALTER TABLE `tarea_reparacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `apellido` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rol` enum('ADMINISTRADOR','TECNICO','CLIENTE') COLLATE utf8mb4_unicode_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_usuario_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Admin','FixDesk','admin@fixdesk.com','scrypt:32768:8:1$ipFNLWWdLKWSgJuS$d73df918628b9bdfdf9c656916bb3927aa15bea812840de3ba6352f6f7bc6f7a54a64f530ff6f7650c180cc0d47acd0ef5baa175d25bb862785d705c6bb01213','ADMINISTRADOR',1,'2026-11-18 15:13:18'),(2,'Tecnico','FixDesk','tecnico@fixdesk.com','scrypt:32768:8:1$OPrdtINUzia1mrIN$897f6c4bc6bb9ec63a39fff1d92c1aeaac6ee083759cb9828fc5e1815bcb51a1a0646be7681b12549dcfd11f0859399ea4462341f7bf1be07b302a69ec5f6f3f','TECNICO',1,'2026-11-18 15:13:18'),(3,'Cliente','Prueba','cliente@fixdesk.com','scrypt:32768:8:1$Y3WzwCpJDW0XYCaZ$db33fcd886ecc896066da6a2a2eb02833f54ba99bd4479cb9ea64e76149cb613250b9d82b2503381b1713d98f5b1987fba895c1587ffdc761b7513ea3743506a','CLIENTE',1,'2026-11-18 15:13:18'),(4,'Juan','Pérez','tecnico2@fixdesk.com','scrypt:32768:8:1$AfZCg9pkzVnNu7cl$f59a59eeaf6696b450fb8bbb530035f811e40f9457ff5c374c6127273d2d9d7e58c7aeeea17b303a3c7efff7115a89e2d623d24d319d3ded4577f50db002d6a4','TECNICO',1,'2026-11-18 22:55:56'),(5,'María','Gómez','cliente2@fixdesk.com','scrypt:32768:8:1$wEq5ceuLSVEj3Epz$75d1f805d0cf951d66fca2f09c3cd679a037011d8afe01c9d00c1b157728bab91170a6d51d35d5488bff9ebe9c5e81fe978705ef32e494d07b24ca11790d8edb','CLIENTE',1,'2026-11-18 23:36:14'),(6,'Pepito','Pepe','cliente3@fixdesk.com','scrypt:32768:8:1$JX0K5cE5y3yA0AUC$088b1ac260e44cf82d05f32011c6cb45e50f9560032ba1b720357b48510a9623a7eab4093cb1d561f41f3506cba3884d7c94ce0f8da541361556df748377df36','CLIENTE',1,'2026-11-19 01:04:26'),(7,'Pepita','Pepa','tecnica3@fixdesk.com','scrypt:32768:8:1$ERkJauxdl6Wji68Z$63624c54ad96ebc1c71434fdc8ca745e09f4c409d6cfdd9f0d74944854539400eaad497ee233199f4857f65c2c4416553183cc7718b1ec500c339fce59649485','TECNICO',1,'2026-11-19 01:05:05');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-18 22:21:28
