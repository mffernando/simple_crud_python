import sqlite3 # sqlite3
#DDL (Data Definition Language) table manipulation (create, drop, alter ...)

connection = sqlite3.connect('base.db') #new database base.db
cursor = connection.cursor() #cursor

sql = """ 
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)
""" #create new table with id, name, phone, email

cursor.execute(sql) #execute sql
connection.commit() #commit
connection.close() #close conenction