#pip install mysql-connector-python

import mysql.connector # Importálja a mysql.connector modult, amely lehetővé teszi a Python alkalmazásoknak, hogy kapcsolódjanak és interakcióba lépjenek egy MySQL adatbázissal.
cnx = mysql.connector.connect( # Létrehoz egy kapcsolatot a MySQL adatbázissal a megadott paraméterek alapján, mint például a host (a szerver címe), user (felhasználónév), password (jelszó) és database (adatbázis neve).
    host = "localhost",
    user = "root",
    password = "",
    database = "test"
)

cursor = cnx.cursor() #  Létrehoz egy kurzort, amelyet a lekérdezések végrehajtására használunk.
query = "INSERT INTO pythoninsertdatatomysql (title, content) VALUES (%s, %s)" # Előkészíti az SQL beszúrási lekérdezést. A %s helyőrzők helyére később kerülnek majd a tényleges adatok.
data = ("aa", "bb") #Definiálja a beszúrandó adatokat. Ebben az esetben két értéket ad meg a title és content oszlopokhoz.
cursor.execute(query, data) #Végrehajtja a SQL lekérdezést a kurzor segítségével, és az adatokat beilleszti a táblába.
cnx.commit()    #Elköveti a változásokat az adatbázisban. Fontos, hogy minden módosítás után meghívjuk ezt a függvényt, különben az adatbázis nem frissül.
cursor.close() # Bezárja a kurzort.
cnx.close() #Bezárja az adatbáziskapcsolatot.