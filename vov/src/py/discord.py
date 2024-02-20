from flask import Flask, render_template, request, url_for, flash, redirect, session
from zenora import APIClient

"""
HELPER FUNCTIONS
"""
def get_user():
    user = None
    if "token" in session:
        user = APIClient(session.get("token"), bearer=True).users.get_current_user()
        print(user)
    return user


"""
ROUTE FUNCTIONS
"""
def login(app):
    return redirect(app.config['OAUTH'])

def callback(app, discord_client):
    code = request.args['code']
    response = discord_client.oauth.get_access_token(code, app.config['REDIRECT'])
    token = response.access_token
    session['token'] = token
    return redirect(url_for("serve"))

def logout(app):
    session.clear()
    return redirect(url_for("serve"))