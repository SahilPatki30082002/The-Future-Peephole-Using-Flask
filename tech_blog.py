from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# for mysql -> 'mysql://username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/thefuturepeephole'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def age():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")

app.run()


