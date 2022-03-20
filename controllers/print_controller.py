from flask import Blueprint, Flask, render_template, redirect, request

import repositories.print_repository as print_repository 
import repositories.artist_repository as artist_repository
from models.print import Print

prints_blueprint = Blueprint("prints", __name__ )

@prints_blueprint.route("/prints")
def display_print_inventory():
    prints = print_repository.select_all()
    return render_template("prints/index.html", all_prints = prints)

@prints_blueprint.route("/prints/new", methods=['GET'])
def new_print():
    artists = artist_repository.select_all()
    return render_template("prints/new.html", artists = artists)

@prints_blueprint.route("/prints", methods=['POST'])
def create_new_print(): 
    title = request.form["title"]
    artist_id = request.form["artist_id"]
    size = request.form["size"]
    price = request.form["price"]
    printing_cost = request.form["printing_cost"]
    stock = request.form["stock"]
    artist = artist_repository.select(artist_id)
    print = Print(title, artist, size, price, printing_cost, stock)
    print_repository.save(print)
    return redirect("/prints")

@prints_blueprint.route("/")





