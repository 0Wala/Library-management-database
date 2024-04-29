import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@beth-53#",

)
mycursor = db.cursor()

#sql="CREATE DATABASE  library"
#ccmycursor.execute(sql)
#db.commit()

sql1 = ''' CREATE TABLE `library`.student (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `regno` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `role` VARCHAR(45) NULL,
  PRIMARY KEY (`Id`));'''
mycursor.execute(sql1 )
db.commit()

sql1 = ''' CREATE TABLE `library`.lecturer (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `role` VARCHAR(45) NULL,
  PRIMARY KEY (`Id`));'''
mycursor.execute(sql1 )
db.commit()
sql2 ='''CREATE TABLE `library`.`bookrecord` (
  `Bno` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `author` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `school` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`Bno`));'''
mycursor.execute(sql2)
db.commit()
sql3='''CREATE TABLE `library`.`issue` (
  `Bno` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `author` VARCHAR(45) NULL,
  `date_of_issue` VARCHAR (45) NULL,
  PRIMARY KEY (`Bno`));
'''
mycursor.execute(sql3)
db.commit()
