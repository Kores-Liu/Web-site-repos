from flask import Flask, request, render_template, redirect, url_for, session
import checkusername
import messageboard


app = Flask(__name__)  
app.secret_key = '123liu456' 

  
@app.route('/')  
def index():  
    username = session.get('username')
    return render_template('index.html', username=username)  
  
@app.route('/register', methods=['POST', 'GET'])  
def register():
    #如果是跳转请求，渲染signup页面
    if request.method == 'GET':
        return render_template('Signup.html')
    elif request.method == "POST":   
        username = request.form['username']  
        password = request.form['password']

    # 简单的验证  
        validation, message = checkusername.validate_credentials(username, password)
        if not validation:
            return message
      
        # 插入到数据库  
        checkusername.insert_user(username, password)  
        return redirect(url_for('index'))  

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "GET":
        return render_template('login.html',validation=True)
    elif request.method == "POST":
        if checkusername.login_validation(request.form['username'], request.form['password']):
            session['username'] = request.form['username']  
            session['password'] = request.form['password']
            return redirect(url_for('index'))
        else:
            #登陆失败，forbidden
            return render_template('login.html', validation=False), 403
    

@app.route('/Logout')
def Logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/messageboard', methods=['POST', 'GET'])
def messages():
    if request.method == 'GET':
        messagelist = messageboard.get_content()
        return render_template('messageboard.html', messagelist=messagelist)
    
#渲染没有完成的功能, 404 NOT Found
@app.route('/commingsoon')
def commingsoon():
    return render_template('commingsoon.htm11l'), 404    
 
if __name__ == '__main__':  
    app.run(debug=True)  