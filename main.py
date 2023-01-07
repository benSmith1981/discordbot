import bot
import dotenv
import os
from flask import Flask
dotenv.load_dotenv()
if __name__ == '__main__':
    bot.run_discord_bot()

    # app = Flask(__name__)
    # app.run(host=os.environ.get("IP"),
    #     port=int(os.environ.get("PORT")),
    #     debug=os.environ.get("DEBUG"),
    #     )
# import routes