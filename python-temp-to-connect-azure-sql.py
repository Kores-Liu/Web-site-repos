import pyodbc  
import register  

server = 'sql-server-for-web.database.windows.net'  
database = 'sql-server-for-web'  
username = 'sihaol'  
password = 'Qwerwsx1234!'  
driver = '{ODBC Driver 18 for SQL Server}'  

conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)  
conn.setencoding('utf-8')
conn.setdecoding(pyodbc.SQL_WCHAR,encoding="UTF-8")


cursor = conn.cursor()
# cursor.execute("insert into Users values('test0000', 'test1111')")
# conn.commit()
cursor.execute("select * from dbo.Users")
row = cursor.fetchone()
if row:
    print(row)

# if __name__ == '__main__':  
#     register.insert_user("sihaol1111", "sihaol22222")