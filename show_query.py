import mysql.connector
my_db=mysql.connector.connect(host='localhost',user='root', password='Yaswanth12.',database='inventory_control_management')
cur=my_db.cursor()
# Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
show='SELECT S.PROFIT_MARGIN FROM MANUFACTURE M,SALE S WHERE M.MANUFACTURE_COMPANY="SS EXPORT" AND M.PRODUCT_NAME="WOODEN TABLE" AND S.STORE_NAME="MY CARE"'
show=cur.execute(show)
display=cur.fetchall()
print("values are:")
for value in display:
    print(value);