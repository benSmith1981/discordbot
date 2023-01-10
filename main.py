from bot import DragBot
import dotenv
import os
dotenv.load_dotenv()
if __name__ == '__main__':
    missDemeanor = DragBot()
    missDemeanor.run_discord_bot()
