from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import cv2
import numpy as np
from PIL import Image
# from threading import Thread 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/travel_comapnion'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'
bcrypt = Bcrypt(app)

class user_details(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column( db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self,password):
        # password = password.encode('utf-8') if isinstance(password, str) else password
        return bcrypt.check_password_hash(self.password,password)
    
    with app.app_context():
        db.create_all()

@app.route("/")
def hello():
    return render_template('landing.html')

    
@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['Email']
        password = request.form['password']
        
        new_user = user_details(username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        success_message = f"User '{username}' registered successfully!"
        return render_template('/index.html',success_message=success_message)
    return render_template('/index.html')

@app.route("/index.html")
def indexcaller():
    return render_template('index.html')

@app.route("/signin",methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['Password']
        
        user = user_details.query.filter_by(username=username).first()
        
        if user and :
            session['username'] = user.username
            session['password'] = user.password
            return render_template('/home.html')
        else:
            failure_message = f"INVALID USERNAME OR PASSWORD!"
            return render_template('/index.html',failure_message=failure_message)
    return render_template('/index.html')

# def hello_world():
#     # return render_template('login.html')
#     cap = cv2.VideoCapture(0)
#     ret, frame = cap.read()
#     frame = np.array(frame)
#     cv2.imwrite('static/images/image.jpeg', frame)
#     # Release the Capture Object and close the opencv window
#     cap.release()
#     cv2.destroyAllWindows()
#     return render_template('index.html')

@app.route("/home.html")
def member1():
    return render_template('home.html')

@app.route("/member.html")
def member2():
    return render_template('member.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    


# # @app.route("/")
# # def hello_world():
# #     cap = cv2.VideoCapture(0)
# #     ret, frame = cap.read()
# #     frame = np.array(frame)
# #     cv2.imwrite('static/image.jpg', frame)  # Save image in the 'static' folder
# #     cap.release()

# #     return render_template('index.html', image_path='static/image.jpg')














































