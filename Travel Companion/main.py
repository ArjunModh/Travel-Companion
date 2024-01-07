from flask import Flask , render_template
import cv2
import numpy as np
from PIL import Image
# from threading import Thread 

app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('landing.html')

    
@app.route("/index.html")
def hello_world():
    # return render_template('login.html')
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame = np.array(frame)
    cv2.imwrite('static/images/image.jpeg', frame)
    # Release the Capture Object and close the opencv window
    cap.release()
    cv2.destroyAllWindows()
    return render_template('index.html')

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














































