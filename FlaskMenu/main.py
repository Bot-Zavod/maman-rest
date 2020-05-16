from flask import Flask, render_template, request, redirect
import csv
import requests
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

IMAGE_FOLDER = 'static'

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

def get_dishes():
    with open('static/example.csv', encoding='utf-16') as csvfile:
        menu = csv.reader(csvfile)
        return list(menu)


@app.route("/", methods=["GET", "POST"])
def mapview():
    return render_template(
        'index.html',
        data=get_dishes(),
    )

if __name__ == "__main__":
    app.run(debug=False, use_reloader=True, host= '0.0.0.0')