Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import mysql.connector
>>> conn=mysql.connector.connect(user="root",password="root",host="localhost")
>>> mycursor=conn.cursor()
>>> mycursor.execute("show databases")
>>> print(mycursor.fetchall())
[('information_schema',), ('mysql',), ('performance_schema',), ('sakila',), ('sys',), ('world',)]
>>> 
