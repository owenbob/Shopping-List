from flask import Flask,render_template
from data import Articles

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




if __name__ == "__main__":
    app.run(debug=True)