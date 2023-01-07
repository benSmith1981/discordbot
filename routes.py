import bot
import flask
from flask import app
bot.run_discord_bot()

@app.route("/")
def index():
    bot.run_discord_bot()

    pass