from dataclasses import replace
from operator import truediv
from flask import Flask , render_template ,request 
from importlib_metadata import method_cache
from flask import mysql


app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Siva@nil143'
app.config['MYSQL_DB'] = 'flask'
 
#mysql = MySQL(app)

@app.route("/" , methods=['GET','POST'])
def home():
    if request.method == "POST":
        #user = User(
        username=request.form["name"],
        age=request.form["age"],
        username=str(username)
        age=str(age)
        print(username,age)
        username=username.replace("(","")
        username=username.replace(",)","")
        age=age.replace("(","")
        age=age.replace(",)","")

        
        #db.session.add(user)
        #db.session.commit()
        print(username,age)
        return render_template("show.html",name=username,age=age)
    
    return render_template("form.html")


if __name__ == '__main__':
    app.run()