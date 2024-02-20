from flask import Flask, render_template, request, url_for, flash, redirect, session, send_from_directory
import os
from pprint import pprint
from werkzeug.exceptions import abort
from urllib import parse
from zenora import APIClient
from src.py import database, discord
import vovSecrets
import sqlite3

"""
CONFIGURATION
"""
app = Flask(__name__, static_url_path='', static_folder='build', template_folder='build')
app.config['SECRET_KEY'] = vovSecrets.SECRET_KEY
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['TOKEN'] = vovSecrets.TOKEN
app.config['CLIENT_SECRET'] = vovSecrets.CLIENT_SECRET
app.config['REDIRECT'] = "http://localhost:5001/discord/login/callback"
app.config['OAUTH'] = f"https://discord.com/api/oauth2/authorize?client_id=1209242452519690342&response_type=code&redirect_uri={parse.quote(app.config['REDIRECT'])}&scope=identify"
discord_client = APIClient(app.config['TOKEN'], client_secret=app.config['CLIENT_SECRET'] )

"""
ROUTES
"""
"""
@app.route('/')
def index():
    user = discord.get_user()
    return render_template('index.j2', oauth=app.config['OAUTH'], user=user)
"""
@app.route("/discord/login")
def login():
    return discord.login(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/discord/login/callback")
def callback():
    return discord.callback(app, discord_client)

@app.route("/discord/logout")
def logout():
    return discord.logout(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@app.errorhandler(404)
def serve(path):
    return render_template('index.html')

@app.route('/about')
def about():
    user = discord.get_user()
    return render_template('index.j2', oauth=app.config['OAUTH'], user=user)

