import mysql.connector
import pymysql
my_connector = pymysql.connect(host="localhost",user="root",password="root",database="AI_monkey")

my_cursor = my_connector.cursor()
def Add_Records(info):
    my_cursor.execute(f"insert into public values('{info}',curdate(),curtime())")
    my_connector.commit()
def Add_Personal_Records(info):
    info.encode("utf-8")
    my_cursor.execute(f"INSERT INTO personal (info,date,time) VALUES ('{info}',CURDATE(),CURTIME())")
    my_connector.commit()
    
def Retrive_Records():
    my_cursor.execute("SELECT * FROM public")
    my_records = my_cursor.fetchall()
    for i in my_records:
        print(i)
        
def Retrive_Personal_Records():
    my_cursor.execute("SELECT * FROM personal")
    my_records = my_cursor.fetchall()
    for i in my_records:
        print(i)


    
