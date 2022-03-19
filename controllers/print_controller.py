from flask import Blueprint, Flask, render_template, redirect, request
from flask import Blueprint

from models.artist import Artist
from models.print import Print
import repositories.print_repository as print_repository 

prints_blueprint = Blueprint("prints", __name__ )

@prints_blueprint.route("/prints")
def display_print_inventory():
    prints = print_repository.select_all()
    return render_template("prints/index.html", prints = prints)
