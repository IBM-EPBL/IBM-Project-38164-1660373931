import sqlite3

con=sqlite3.connect("details.db")
cursor=con.cursor()
stmt="""CREATE TABLE registration(
        name VARCHAR(20),
        email VARCHAR(20),
        gender VARCHAR(19),
        region VARCHAR(19),
        category VARCHAR(20),
        );"""

con.commit()
cursor.execute(stmt)
con.close()
print("Table Created")

#con=sqlite3.connect("details.db")
#stmt="""CREATE TABLE registration(
#        name VARCHAR(20),
#         email VARCHAR(20),
#         gender VARCHAR(19),
#         region VARCHAR(19),
#         category VARCHAR(20),
#         pswd VARCHAR(20),
#         );"""
#con.commit()
#cursor.execute(stmt)
#con.close()
#print("Table Created")
#cursor=con.cursor()
#stmt="""DROP TABLE Registered"""
#cursor.execute(stmt)
#con.commit()
#con.close()
#print("Table Deleted")



