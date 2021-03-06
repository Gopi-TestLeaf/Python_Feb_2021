# Step01: install sqlite3: - pip install db-sqlite3

import sqlite3

# Create Connection
con = sqlite3.connect('database.db')
print('Create DB')
#*********************************************************************************************************
# Create Table in DataBase
con.execute('CREATE TABLE IF NOT EXISTS leaf_db(fName, lName, email, password)')
print('Table created')
#*********************************************************************************************************
# Insert the records
con.execute(''' INSERT INTO leaf_db(fName, lName, email, password) 
            VALUES('Balaji', 'M', 'balaji@gmail.com', '4321567891') ''')
con.commit()
print("Inserted the Records")
#*********************************************************************************************
# Update the Records
qr = ''' UPDATE leaf_db set password = '1234554321' WHERE fName = 'Balaji' '''
con.execute(qr)
con.commit()
print("Updated the records")
#*********************************************************************************************
# Fetch all data's
data = con.execute('SELECT * FROM leaf_db')
for i in data:
    print(i)
#*********************************************************************************************
# close the connection
con.close()
print('Close DB')