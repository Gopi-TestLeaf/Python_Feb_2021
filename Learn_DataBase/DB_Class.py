import sqlite3
from Learn_DataBase.TestData import Test_Data


class Data_Base:

    def __init__(self, fileName, table_name):
        self.fileName = fileName
        self.table_name = table_name

    def get_connection(self):
        con  = sqlite3.connect(self.fileName)
        print("DataBase is Opened")
        return con

    def create_table(self, con):
        con.execute(' CREATE TABLE IF NOT EXISTS ' + self.table_name +'''(fName, lName, email, pwd)''' )
        print('Create the Table')

    def insert_record(self, con, obj):
        qr = f''' INSERT INTO {self.table_name}(fName, lName, email, pwd) 
            VALUES(?, ?, ?, ?) '''
        con.execute(qr, (obj.fName, obj.lName, obj.email, obj.pwd))
        con.commit()
        print("Inserted the Records")

    def close_Connection(self, con):
        con.close()
        print("closed the Connection")


if __name__ == "__main__":
    db_obj = Data_Base('database123.db', 'leaf123')
    con = db_obj.get_connection()
    db_obj.create_table(con)
    obj = Test_Data(fName = "Sarath", lName = "M", email="sar@gmail.com", pwd = "123")
    print(obj.fName)
    db_obj.insert_record(con, obj)
    db_obj.close_Connection(con)
