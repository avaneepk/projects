--
-- Host: localhost    Database: aether
-- ------------------------------------------------------
-- Server version	8.0.32



CREATE TABLE student (
  s_fname varchar(30) DEFAULT NULL,
  s_lname varchar(30) DEFAULT NULL,
  m_no int UNIQUE NOT NULL,
  s_no int UNIQUE NOT NULL,
  s_degree varchar(30) DEFAULT NULL,
  s_email varchar(50) DEFAULT NULL,
  PRIMARY KEY (s_no));


CREATE TABLE board_member (
  bm_fname varchar(30) DEFAULT NULL,
  bm_lname varchar(30) DEFAULT NULL,
  bm_email varchar(50) DEFAULT NULL,
  bm_degree varchar(30) DEFAULT NULL,
  bm_role varchar(30) DEFAULT NULL,
  s_no int NOT NULL,
  PRIMARY KEY (s_no));


CREATE TABLE membership (
  m_price int DEFAULT NULL,
  exp_date date DEFAULT NULL,
  s_no int NOT NULL,
  m_no int NOT NULL,
  PRIMARY KEY (m_no));


CREATE TABLE merchandise (
  p_no int NOT NULL,
  s_no int NOT NULL,
  p_type varchar(50) DEFAULT NULL,
  p_price int DEFAULT NULL,
  p_quantity int DEFAULT NULL,
  PRIMARY KEY (p_no));


CREATE TABLE sponsor (
  c_name varchar(30) DEFAULT NULL,
  c_id int NOT NULL,
  c_email varchar(50) DEFAULT NULL,
  money_amount int DEFAULT NULL,
  PRIMARY KEY (c_id));


CREATE TABLE sponsored_product (
	product_no int UNIQUE NOT NULL,
	company_id int UNIQUE NOT NULL);






