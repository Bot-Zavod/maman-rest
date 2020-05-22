from flask import Flask, render_template, request, redirect
import csv
import codecs
import requests
import os
from flask import Flask, redirect, url_for


app = Flask(__name__, template_folder="templates", static_folder="static")

IMAGE_FOLDER = 'static'

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

categories = {'center':['Завтраки','Raw bar','Брускетты','Закуски','Салаты','Рыба и морепродукты','Мясо и стейки','Горячие блюда', 'Супы', 'Котлетки', 'Паста и тесто', 'Десерты', 'Бар'],
              'fontan':['Завтраки','Закуски','Салаты','Raw bar','Брускетты','Паста и пицца','Рыба и морепродукты','Мясо и стейки','Горячие блюда', 'Котлетки', 'Десерты', 'Бар'],
              'sea':['Raw bar','Роллы','Брускетты','Закуски','Салаты','Супы','Рыба и морепродукты','Мясо и стейки','Горячее','Паста','Десерты','Бар']
              }


def aggregate_by_first(input_list):
    categories = set([el[0] for el in input_list])
    categ_dict = {key: list(filter(lambda x: x[0] == key, input_list)) 
                        for key in categories}
    categ_dict = {key: [el[1:] for el in categ_dict[key]] 
                        for key in categ_dict.keys()}
    return categ_dict


def get_dishes(csv_path='static/maman_fontan.csv',categories=None):
    with codecs.open(filename=csv_path, mode='r', encoding='utf-8') as csvfile:
        menu = list(csv.reader(csvfile))
        menu = aggregate_by_first(menu[1:])
        menu = {key:aggregate_by_first(menu[key]) for key in menu.keys()}
        return menu

@app.route("/sea", methods=["GET", "POST"])
def rest_1():
    dishes = get_dishes()
    buttons = list(filter(lambda x: x in dishes.keys(),categories['sea']))
    return render_template(
        'index.html',
        data=dishes, page_type="sea", btn_order=buttons
    )


@app.route("/fontan", methods=["GET", "POST"])
def rest_2():
    dishes = get_dishes('static/maman_fontan.csv')
    buttons = list(filter(lambda x: x in dishes.keys(),categories['fontan']))
    return render_template(
        'index.html',
        data=dishes, page_type="fontan", btn_order=buttons
    )


@app.route("/test", methods=["GET", "POST"])
def rest_3():
    dishes = get_dishes()
    buttons = list(filter(lambda x: x in dishes.keys(),categories['center']))
    return render_template(
        'index.html',
        data=dishes, page_type="center", btn_order=buttons
    )

@app.route("/", methods=["GET", "POST"])
def rest_default():
    return redirect(url_for('rest_1'))


if __name__ == "__main__":
    app.run(debug=False, use_reloader=True, host= '0.0.0.0', port=8080)
