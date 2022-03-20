from flask import Blueprint, Flask, render_template, redirect, request

import repositories.print_repository as print_repository 
import repositories.artist_repository as artist_repository

prints_blueprint = Blueprint("prints", __name__ )

@prints_blueprint.route("/prints")
def display_print_inventory():
    prints = print_repository.select_all()
    return render_template("prints/index.html", all_prints = prints)

@prints_blueprint.route("/prints/new", methods=['GET'])
def new_print():
    artists = artist_repository.select_all()
    return render_template("prints/new.html", artists = artists)

