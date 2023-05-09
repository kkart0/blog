from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
with open('config.json', 'r') as c:
    params = json.load(c)["params"]
    params['websitename']
    
local_server = True
app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password'],
    

)
mail = Mail(app)
# app= Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/karthidata'
db = SQLAlchemy(app)
class Data1(db.Model):
    __tablename__ = 'data1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, )
    email = db.Column(db.String(100), nullable=False,)
    mobile = db.Column(db.String(10), nullable=False,)
    age = db.Column(db.String(2), nullable=False,   )
    gender = db.Column(db.String(10), nullable=False,)
    password = db.Column(db.String(100), nullable=False,)
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=''
# app.config['MYSQL_DB']='data1'
# app.config['MYSQL_CURSORCLASS']='dictcursor'
# mysql=MySQL(app)
# #creating a connection cursor
# with app.app_context():
#     cursor=mysql.connection.cursor()
# #executing SQL statment
# cursor.execute('''CREATE TABLE table_name(field1,field2..)''')
# cursor.execute('''INSERT INTO table_name values(v1,v1..)''')
# cursor.execute('''DELETE FORM table_name WHERE condition''')
# #saving the action perfornfor db
# mysql.connection.commit()
# #close the cursor
# cursor.close()
@app.route('/')
def index():

    return render_template("index.html",params=params)
@app.route('/1')
def first():
    return render_template("1.html")
@app.route('/2')
def secont():
    return render_template("2.html")
@app.route('/3')
def tried():
    return render_template("3.html")
@app.route('/sign',methods=['GET','POST'])
def sign():
    if (request.method=='POST'):
        name = request.form.get('name1')
        email = request.form.get('email1')
        Mobile = request.form.get('Mobile')
        age = request.form.get('age')
        gender = request.form.get('gender')
        passs = request.form.get('passs')
        # cur=mysql.connection.cursor()
        # cur.execute('''INSERT INTO info_table values(%s,%s)''',(name,email))
        # mysql.connection.commit()
        # cur.close()
        # return f'done'
        database=Data1(name=name,email=email,mobile=Mobile,age=age,gender=gender,password=passs)
        db.session.add(database)
        db.session.commit()
        # message="how are you"
        # phone='9750458118'
        # mail.send_message('New message from ' + name,
        #                   sender=email,
        #                   recipients = [params['gmail-user']],
        #                   body = message + "\n" + phone
        #                   )
    return render_template('signup.html', )
        # Data1.save()
    # return render_template("signup.html")
# app.run(host='localhost' port=5000)
def search():
    if request.method == "GET":
        print(request.form)
        print(request.form['search'])
    return "this page is"+request.form['search']
app.run(debug=True)