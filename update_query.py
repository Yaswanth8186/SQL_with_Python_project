import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root', password='Yaswanth12.',database='inventory_control_management')
cur=my_db.cursor()
# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
update='UPDATE MANUFACTURE SET NUMBER_ITEMS=10 WHERE PRODUCT_NAME="TOY CAR" AND COLOR="RED"'
cur.execute(update)
print("Updated the table Successfully")