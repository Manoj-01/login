from flask import Flask,render_template,request
from flaskext.mysql import MySQL


mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'postgres'
app.config['MYSQL_DATABASE_DB'] = 'login'
app.config['MYSQL_DATABASE_host'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def my_form():
    return render_template('login.html')

@app.route('/',methods=['POST'])
def Authenticate():
    username=request.form['u']
    password=request.form['p']
    cursor=mysql.connect().cursor()
    cursor.execute("SELECT * FROM logininfo WHERE USER_ID='" + username + "' and PASSWORD='" + password + "'")
    data=cursor.fetchone()
    if data is None:
        return "Username or Password is Wrong"
    else:
        return "Logged in Successfully"

if __name__=="__main__":
    app.run(debug=True)