from flask import Blueprint, Flask, render_template, redirect, request

import repositories.print_repository as print_repository 
import repositories.artist_repository as artist_repository

from models.artist import Artist

artists_blueprint = Blueprint("artists", __name__)

@artists_blueprint.route("/artists")
def display_artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", all_artists = artists)

@artists_blueprint.route("/artists/new", methods=['GET'])
def new_artist():
    return render_template("artists/new.html")

@artists_blueprint.route("/artists", methods=['POST'])
def create_new_artist(): 
    name = request.form["name"]
    artist = Artist(name)
    artist_repository.save(artist)
    return redirect("/artists")

@artists_blueprint.route("/artists/<id>")
def filter(id):
    artist = artist_repository.select(id)
    prints = artist_repository.prints(artist)
    return render_template("artists/filter.html", artist=artist, prints=prints)