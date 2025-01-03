"""
用于连接到azure SQL database

"""

import pyodbc

#连接到数据库，和用户名及密码。 隐私数据
server = 'sql-server-for-web.database.windows.net'  
database = 'sql-server-for-web'  
sql_username = 'sihaol'  
sql_password = 'Qwerwsx1234!'  
driver = '{ODBC Driver 18 for SQL Server}'  

def sqlconnection(database):  
    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + sql_username + ';PWD=' + sql_password)
    #修改插入数据和提取数据时的格式
    conn.setencoding('utf-8')
    conn.setdecoding(pyodbc.SQL_WCHAR,encoding="UTF-8")
    return conn  