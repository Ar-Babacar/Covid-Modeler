import mysql.connector
import json
import requests
import urllib.request, json 
from datetime import datetime
with urllib.request.urlopen("https://covid-modeler-api.herokuapp.com/mai") as url:
    data = json.loads(url.read().decode())
    print(data)
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
                                    auth_plugin='mysql_native_password'
                                )

    if db.is_connected():
        db_Info = db.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

    for item in data:
        idEtat =item.get("jour")
        print(idEtat)
        idRegion = item.get("jour")
        idcas = item.get("idcas")
        nomRegion = item.get("nomRegion")
        nbCas = item.get("nbCas")
        nbCasCom = item.get("nbCasCom")
        nbCasContact = item.get("nbCasContact")
        nbCasImp = item.get("nbCasImp")   
        Date =  item.get("DateHeureExtraction")
        print(Date)
        FormatedDate =  datetime.strptime(Date, '%d/%m/%y %H:%M:%S') 
        cursor.execute("INSERT INTO Etat values(%s,%s,%s,%s,%s)", (idEtat,FormatedDate, nbCasCom, nbCasContact, nbCasImp ))
        cursor.execute("INSERT INTO Region values(%s,%s)", (idRegion, nomRegion))
        db.commit()

except mysql.connector.Error as e:
    print(e)
finally:
    if(db.is_connected()):
        cursor.close()
        db.close()