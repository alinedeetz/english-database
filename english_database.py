from flask import Flask, render_template, request, redirect
import psycopg2
from googletrans import Translator
import os

app = Flask(__name__)
english_database = []
DB_USERNAME = os.environ["ENGLISH_DATABASE_DB_USERNAME"]
DB_PASSWORD = os.environ["ENGLISH_DATABASE_DB_PASSWORD"]
DB_HOSTNAME = os.environ["ENGLISH_DATABASE_DB_HOSTNAME"]
DB_PORT = os.environ["ENGLISH_DATABASE_DB_PORT"]
DB_NAME = os.environ["ENGLISH_DATABASE_DB_NAME"]
POSTGRESQL_URI = "postgres://{}:{}@{}:{}/{}".format(
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOSTNAME,
    DB_PORT,
    DB_NAME
)

connection = psycopg2.connect(POSTGRESQL_URI)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        translator = Translator ()
        out = translator.translate(request.form.get("english_word"), dest="pt")
        print(out.text)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO words VALUES (%s, %s);",
                    (
                        request.form.get("english_word"),
                        (out.text)
                    )
                )
        return redirect("/results")
    return render_template("form.html")

app.run()

@app.route("/results")
def results():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM words;")
            data = cursor.fetchall()
    return render_template("table.html", data=data)
