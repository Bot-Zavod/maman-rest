from flask import Flask, render_template, request, redirect
import csv
import requests
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

IMAGE_FOLDER = 'static'

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

def aggregate_by_first(input_list):
    categories = set([el[0] for el in input_list])
    categ_dict = {key:list(filter(lambda x: x[0] == key, input_list)) for key in categories}
    categ_dict = {key:[el[1:] for el in categ_dict[key]] for key in categ_dict.keys()}
    return categ_dict

def get_dishes():
    with open('maman-rest/static/example.csv', encoding='utf-16') as csvfile:
        menu = list(csv.reader(csvfile))
        menu = aggregate_by_first(menu)
        menu = {key:aggregate_by_first(menu[key]) for key in menu.keys()}
        return menu


@app.route("/", methods=["GET", "POST"])
def mapview():
    return render_template(
        'index.html',
        data=get_dishes(),
    )

if __name__ == "__main__":
    app.run(debug=False, use_reloader=True, host= '0.0.0.0')