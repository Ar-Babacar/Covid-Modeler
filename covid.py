import mysql.connector


import mysql.connector


sql_create1 = """
    CREATE TABLE IF NOT EXISTS Region(
        idRegion INT NOT NULL,
        nomRegion VARCHAR(45) NULL,
        PRIMARY KEY (idRegion))
        ENGINE = InnoDB;
    """

sql_create2 = """
    CREATE TABLE IF NOT EXISTS Departement(
    idDepartement INT NOT NULL AUTO_INCREMENT,
    nomDepartement VARCHAR(45) NULL,
    population INT NULL,
    latitude DECIMAL(10,8) NULL,
    longitude DECIMAL(11,8) NULL,
    `Region_idRegion` INT NOT NULL,
    `Etat_idEtat` INT NOT NULL,
    `Etat_date` DATETIME NOT NULL,
    `Etat_Communique_idCommunique` INT NOT NULL,
    `Etat_Communique_date` DATETIME NOT NULL,
    PRIMARY KEY (`idDepartement`, `Region_idRegion`, `Etat_idEtat`, `Etat_date`, `Etat_Communique_idCommunique`, `Etat_Communique_date`),
    INDEX `fk_Departement_Region1_idx` (`Region_idRegion` ASC) VISIBLE,
    INDEX `fk_Departement_Etat1_idx` (`Etat_idEtat` ASC, `Etat_date` ASC, `Etat_Communique_idCommunique` ASC, `Etat_Communique_date` ASC) VISIBLE,
    CONSTRAINT `fk_Departement_Region1`
    FOREIGN KEY (`Region_idRegion`)
    REFERENCES `Covid-Modeler`.`Region` (`idRegion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_Departement_Etat1`
    FOREIGN KEY (`Etat_idEtat` , `Etat_date` , `Etat_Communique_idCommunique` , `Etat_Communique_date`)
    REFERENCES `Covid-Modeler`.`Etat` (`idEtat` , `date` , `Communique_idCommunique` , `Communique_date`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

        ENGINE = InnoDB;
    """



sql_create3 = """
    CREATE TABLE IF NOT EXISTS Communique (
    `idCommunique` INT NOT NULL AUTO_INCREMENT,
    `nbTest` INT NOT NULL,
    `nbGueri` INT NULL,
    `nbDeces` INT NULL,
    `nbNvCas` INT NULL,
    `nbCasImp` INT NULL,
    `nbCasCom` INT NULL,
    `nbCasCont` INT NULL,
    `date` DATETIME NOT NULL,
    PRIMARY KEY (`idCommunique`, `date`))
ENGINE = InnoDB
"""

sql_create4 = """
    CREATE TABLE IF NOT EXISTS Etat (
    `idEtat` INT NOT NULL AUTO_INCREMENT,
    `date` DATETIME NOT NULL,
    `nbCas` INT NULL DEFAULT NULL,
    `Communique_idCommunique` INT NOT NULL,
    `Communique_date` DATETIME NOT NULL,
    PRIMARY KEY (`idEtat`, `date`, `Communique_date`),
    INDEX `fk_Etat_Communique1_idx` (`Communique_idCommunique` ASC, `Communique_date` ASC) VISIBLE,
    CONSTRAINT `fk_Etat_Communique1`
    FOREIGN KEY (`Communique_idCommunique` , `Communique_date`)
    REFERENCES `Covid-Modeler`.`Communique` (`idCommunique` , `date`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
    """

db = mysql.connector.connect(host="127.0.0.1", 
                                    user="testuser",
                                    password="test",
                                    database="covid", 
                                    auth_plugin='mysql_native_password'
                                )
try:
    db = mysql.connector.connect(host="127.0.0.1", 
                                    user="testuser",
                                    password="test",
                                    database="covid", 
                                    auth_plugin='mysql_native_password')

    if db.is_connected():
        db_Info = db.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)


    cursor = db.cursor()
    cursor.execute(sql_create1)
    cursor.execute(sql_create2)
    cursor.execute(sql_create3)
    cursor.execute(sql_create4)
    
    try:
        db.commit()

    except: 
        db.rollback()

except Exception as e:
    print("Error while connecting to MySQL", e)
finally:
    if (db.is_connected()):
        cursor.close()
        db.close()
        print("MySQL connection is closed")      