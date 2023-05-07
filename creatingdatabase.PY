import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root',password='Yaswanth12.')
cur=my_db.cursor()
cur.execute('create database inventory_control_management')
