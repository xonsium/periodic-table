from flask import Blueprint, render_template, url_for, flash, request, redirect
import datetime
import os
import csv

def get_element_from_symbol(symbol):
    with open('table.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = {}
        column_names = []
        for row in csv_reader:
            if line_count == 0:
                for column_name in row:
                    column_names.append(column_name)
                line_count += 1
            else:
                if symbol == row[2]:
                    for index, column_name in enumerate(column_names):
                        data[column_name] = row[index]
    return data

def get_element_from_an(an):
    with open('table.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = {}
        column_names = []
        for row in csv_reader:
            if line_count == 0:
                for column_name in row:
                    column_names.append(column_name)
                line_count += 1
            else:
                if str(an) == row[0]:
                    for index, column_name in enumerate(column_names):
                        data[column_name] = row[index]
    return data


views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@views.route('/element', methods=["POST", "GET"])
def element():
    name = request.args.get('element')
    if name == "":
        print("re")
        return redirect(request.referrer or url_for('home'))
    try:
        name = int(name)
        data = get_element_from_an(name)
    except ValueError:
        name = request.args.get('element')
        data = get_element_from_symbol(name.capitalize())

    if data:
        return render_template('element.html', data=data)
    else:
        return redirect(request.referrer or url_for('home'))
    

@views.route("/about")
def about():
    return render_template("about.html")