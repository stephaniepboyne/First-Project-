from flask import Blueprint, Flask, render_template, redirect, request
from flask import Blueprint

from models.artist import Artist
from models.print import Print
from repositories import artist_repository

