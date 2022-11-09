import sqlite3

con=sqlite3.connect("login.db")
cursor=con.cursor()
stmt="""CREATE TABLE login(
        name VARCHAR(20),
        pswd VARCHAR(20),
        );"""

con.commit()
cursor.execute(stmt)
con.close()
print("Table Created")

#con=sqlite3.connect("login.db")
#stmt="""CREATE TABLE login(
#        name VARCHAR(20),
#         pswd VARCHAR(20),
#         );"""
#con.commit()
#cursor.execute(stmt)
#con.close()
#print("Table Created")
#cursor=con.cursor()
#stmt="""DROP TABLE logged in"""
#cursor.execute(stmt)
#con.commit()
#con.close()
#print("Table Deleted")