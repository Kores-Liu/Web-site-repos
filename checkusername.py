from connectsql import sqlconnection
import pyodbc  
import re




# 插入数据到数据库  
def insert_user(username, password):  
    conn = sqlconnection()                                  
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO dbo.Users (username, password) VALUES (?, ?)", (username, password))  
    conn.commit()  
    cursor.close()  
    conn.close()  

def validate_credentials(username, password):  
    #检查是否用户新注册的用户名在数据库中已经存在
    #连接database
    conn = sqlconnection()                                  
    conn.setencoding('utf-8')
    conn.setdecoding(pyodbc.SQL_WCHAR,encoding="UTF-8")
    cursor = conn.cursor()
    cursor.execute("select * from dbo.Users")
    usernames_register = [row.Username for row in cursor]
    if username in usernames_register:
        return False, "用户名不唯一"
    return True, "用户名和密码验证成功"  

def login_validation(username='test0000', password='test1111'):
    conn = sqlconnection()                                 
    conn.setencoding('utf-8')
    conn.setdecoding(pyodbc.SQL_WCHAR,encoding="UTF-8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.Users WHERE username = ? AND password = ?", (username, password))  
    user = cursor.fetchone()  
    if user:  
        return True  
    else:  
        return False  
    
if __name__ == '__main__':
    login_validation()