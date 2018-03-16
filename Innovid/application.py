from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
import datetime, time
from sqlalchemy import DATE, cast
from flask_jsglue import JSGlue
import os
import re
import json
import random
import csv
import urllib.request
from functools import wraps
import requests
import config

app = Flask(__name__)
JSGlue(app)

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

config.health = 0
config.laptop = 0

@app.route("/")
#@login_required
def index():
    health1 = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=pcmcat242800050021))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,image,longDescription,url&pageSize=5&format=json")

    json_data1 = json.loads(health1.text)

    products1 = json_data1["products"]
    product1 = products1[4]

    laptop1 = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=abcat0502000))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,description,image,longDescription,url&pageSize=5&format=json")

    json_data2 = json.loads(laptop1.text)
    print(json_data2)
    products2 = json_data2["products"]

    product2 = products2[0]

    return render_template("index.html", product1=product1, product2=product2)

@app.route("/gallery")
#@login_required
def gallery():
    x = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=pcmcat242800050021))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,description,image,longDescription,url&pageSize=5&format=json")

    json_data = json.loads(x.text)

    products = json_data["products"]

    picture = products[config.health]

    return render_template("gallery.html", products=products, picture=picture)

@app.route("/gallery3")
#@login_required
def gallery3():
    if config.health == 0:
        config.health = 4
    else:
        config.health -= 1
    x = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=pcmcat242800050021))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,image,longDescription,url&pageSize=5&format=json")

    json_data = json.loads(x.text)

    products = json_data["products"]

    picture = products[config.health]

    return render_template("gallery.html", products=products, picture=picture)

@app.route("/gallery4")
#@login_required
def gallery4():
    if config.health == 4:
        config.health = 0
    else:
        config.health += 1
    x = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=pcmcat242800050021))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,image,longDescription,url&pageSize=5&format=json")

    json_data = json.loads(x.text)

    products = json_data["products"]

    picture = products[config.health]

    return render_template("gallery.html", products=products, picture=picture)

@app.route("/gallery2")
#@login_required
#global health == 0

#print(health)
def gallery2():
    x = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=abcat0502000))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,description,image,longDescription,url&pageSize=5&format=json")

    json_data = json.loads(x.text)

    products = json_data["products"]

    picture = products[0]

    return render_template("gallery2.html", products=products, picture=picture)

@app.route("/gallery5")
#@login_required
def gallery5():
    if config.laptop == 0:
        config.laptop = 4
    else:
        config.laptop -= 1
    x = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=abcat0502000))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,description,image,longDescription,url&pageSize=5&format=json")

    json_data = json.loads(x.text)

    products = json_data["products"]

    picture = products[config.laptop]

    return render_template("gallery2.html", products=products, picture=picture)

@app.route("/gallery6")
#@login_required
def gallery6():
    if config.laptop == 4:
        config.laptop = 0
    else:
        config.laptop += 1
    x = requests.get("https://api.bestbuy.com/v1/products(bestSellingRank>=5&(categoryPath.id=abcat0502000))?apiKey=U8IbiRwbJ9tleBTOnpqVQ00e&sort=regularPrice.asc&show=regularPrice,name,description,image,longDescription,url&pageSize=5&format=json")

    json_data = json.loads(x.text)

    products = json_data["products"]

    picture = products[config.laptop]

    return render_template("gallery2.html", products=products, picture=picture)




