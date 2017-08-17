from flask import Flask,render_template,flash,redirect,url_for,session,logging
from data import Articles
from wtforms import Form ,StringField ,TextAreaField,PasswordField validators



app = Flask(__name__)

Articles = Articles()

@app.route("/")
def  index():
    return render_template("home.html")
@app.route("/lists")
def shoppingList():
    return render_template("list.html", articles=Articles)
@app.route("/listcreated/<string:id>/")
def List(id):
    return render_template("listcreated.html", id =id)
class registerForm():
    name = StringField("Name",[validators.Length(min=1 ,max=45)]))
    username = StringField("Username",[validators.Length(min=6,max=25)])
    email = StringField("Email",[validators.Length(min =6,max=50)])
    password = PasswordField("Password",[
        validators.dataRequired()
        validators.EqualTo("confirm",message="Passwords do not match")
    ])
    confirm = PasswordField("Confirm Password")
    @app.route("/register",methods=[])
    def register





if __name__ == "__main__":
    app.run(debug=True)