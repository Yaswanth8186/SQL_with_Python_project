import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root', password='Yaswanth12.',database='inventory_control_management')
cur=my_db.cursor()
# Display all the “wooden chair” items that were manufactured before the 1st May 2023.
display='SELECT * FROM MANUFACTURE WHERE PRODUCT_NAME="WOODEN CHAIR" AND MANUFACTURE_DATE < "2023-05-01"'
cur.execute(display)
display1=cur.fetchall()
for x in display1:
    print(x)