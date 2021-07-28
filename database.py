import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="")

cursor = db.cursor()
cursor.execute("CREATE DATABASE parking")




db = mysql.connector.connect(host="localhost", user="root", passwd="", database="parking")

mycursor = db.cursor()
sql = """CREATE TABLE data(
    nomor INT AUTO_INCREMENT PRIMARY KEY,
    plat VARCHAR(10)

)
"""
mycursor.execute(sql)
