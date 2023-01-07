import bot
import flask
from flask import app

@app.route("/")
def index():
    bot.run_discord_bot()