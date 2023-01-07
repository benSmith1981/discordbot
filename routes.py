import bot
import flask
from flask import (app, render_template)
bot.run_discord_bot()

@app.route("/")
def index():
    bot.run_discord_bot()
    return render_template("base.html")