
from flask import Flask, render_template, request, redirect
import sqlite3

app=Flask(__name__)

def init_db():
    conn=sqlite3.connect("words.db")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS words(id INTEGER PRIMARY KEY, english TEXT, russian TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    conn=sqlite3.connect("words.db")
    cur=conn.cursor()
    words=cur.execute("SELECT * FROM words").fetchall()
    conn.close()
    return render_template("index.html", words=words)

@app.route("/add", methods=["POST"])
def add():
    en=request.form.get("english")
    ru=request.form.get("russian")
    if en and ru:
        conn=sqlite3.connect("words.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO words(english,russian) VALUES (?,?)",(en,ru))
        conn.commit()
        conn.close()
    return redirect("/")

if __name__=="__main__":
    app.run()
