import sqlite3 #sqlite3
#DML (Data Manipulation Language) data manipulation (CRUD (Create, Read, Update and Delete))

#depurate and commit
def commit_close(function):
    def decorator(*args):
        connection = sqlite3.connect('base.db') #database base.db
        cursor = connection.cursor() #cursor
        sql = function(*args) #sql function
        cursor.execute(sql) #execute sql
        connection.commit() #connection commit
        connection.close() #close connection
    return decorator
       
@commit_close
def db_insert(name, phone, email):
    return """INSERT INTO users(name, phone, email) 
              VALUES ('{}', '{}', '{}')""".format(name, phone, email)

@commit_close
def db_update(name, email):
    return """UPDATE users SET name = '{}' WHERE email = '{}'""".format(name, email)

@commit_close
def db_delete(email):
    return """DELETE FROM users WHERE email = '{}'""".format(email)

def db_select(data, field):
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    sql =  """SELECT id, name, phone, email FROM users WHERE {}={}""".format(data, field)
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    return data
    
    
#insert data into users to database
#EXAMPLE
#sql = """
#INSERT INTO users(name, phone, email)
#VALUES ('user2', '1234-1234', 'user2@email.com')
#"""

#connection = sqlite3.connect('base.db') #new database base.db
#cursor = connection.cursor() #cursor
#cursor.execute(db_insert('user3', '1234-1234', 'user3@mail.com')) #cursor.execute(sql) #execute sql
#cursor.execute(db_update('update1', 'user1@email.com')) #update user name user1 to update1 where email = user1@mail.com
#cursor.execute(db_delete('user3@mail.com')) #delete user where email = user3@mail.com
#cursor.execute(db_select('1', 'id')) #fetch and print the user with id = 1
#connection.commit() #commit
#data = cursor.fetchone() #fetch one register db_select
#connection.close() #close conenction
#print(data)

