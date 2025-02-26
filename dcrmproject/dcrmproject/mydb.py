import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='Chris098765',
    database='chrisfirstapp'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS chrisfirstapp")
print("Database created successfully!")
