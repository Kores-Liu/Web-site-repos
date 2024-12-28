from flask import Flask, request, render_template, redirect, url_for,flash
import pyodbc  
import re  

app = Flask(__name__)  
  
# 填写你的数据库连接详情  
server = 'sql-server-for-web.database.windows.net'  
database = 'sql-server-for-web'  
sql_username = 'sihaol'  
sql_password = 'Qwerwsx1234!'  
driver = '{ODBC Driver 18 for SQL Server}'  
  
# 连接数据库  
def get_db_connection():  
    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + sql_username + ';PWD=' + sql_password)  
    return conn  
  

    
# 插入数据到数据库  
def insert_user(username, password):  
    conn = get_db_connection()  
    # 设置编码格式                                        
    conn.setencoding('utf-8')
    conn.setdecoding(pyodbc.SQL_WCHAR,encoding="UTF-8")
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO dbo.Users (username, password) VALUES (?, ?)", (username, password))  
    conn.commit()  
    cursor.close()  
    conn.close()  
  

def validate_credentials(username, password):  
    if len(username) <= 8 or len(password) <= 8:  
        return False, "用户名和密码的长度必须大于8位"  
      
    # 正则表达式来检查是否包含英文字母和数字  
    username_pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')  
    password_pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')  
  
    # 检查用户名和密码是否符合要求  
    if not re.match(username_pattern, username):  
        return False, "用户名必须包含至少一个字母和一个数字"  
    if not re.match(password_pattern, password):  
        return False, "密码必须包含至少一个字母和一个数字"  
    #检查是否用户新注册的用户名在数据库中已经存在
    #连接database
    conn = get_db_connection()                                   
    conn.setencoding('utf-8')
    conn.setdecoding(pyodbc.SQL_WCHAR,encoding="UTF-8")
    cursor = conn.cursor()
    cursor.execute("select * from dbo.Users")
    usernames_register = [row.Username for row in cursor]
    if username in usernames_register:
        return False, "用户名不唯一"
    return True, "用户名和密码验证成功"  

  
@app.route('/')  
def index():  
    return render_template('test.html')  
  
@app.route('/register', methods=['POST', 'GET'])  
def register():
    #如果是跳转请求，渲染signup页面
    if request.method == 'GET':
        return render_template('Signup.html')
    elif request.method == "POST":   
        username = request.form['username']  
        password = request.form['password']

    # 简单的验证  
        validation, message = validate_credentials(username, password)
        if not validation:
            return message
      
        # 插入到数据库  
        insert_user(username, password)  
        return redirect(url_for('/'))  

@app.route('/login')
def login():
    return render_template('login.html')
 
if __name__ == '__main__':  
    app.run(debug=True)  