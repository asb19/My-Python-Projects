from flask import Flask,render_template,request,redirect,url_for
# from flask_pymongo import PyMongo, MongoClient
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/<name>')
def displayUser(name):
    return "hey %s"%name
@app.route('/create', methods=["POST","GET"])
def form():
    if request.method == "POST":
        db = request.form["db"]
        client = MongoClient('localhost', 27017)
        mydbase = client[db]
        collection = mydbase[db]
        collection.create_index('Roll no', unique = True)
        print("List of databases after creating new one")
        print(client.list_database_names())
        return redirect(url_for("index"))
    else:
        return render_template("formm.html")



if __name__ == "__main__":
    app.run(debug=True)