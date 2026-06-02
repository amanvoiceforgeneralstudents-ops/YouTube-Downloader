from pyrogram import Client, idle
from config import Config
from flask import Flask
from threading import Thread
# Pytubefix ka use karein error 400 fix karne ke liye
from pytubefix import YouTube 

# Web server taaki Render port detect kar sake
app = Flask(__name__)
@app.route('/')
def index():
    return "Bot is running!"

def run_server():
    app.run(host='0.0.0.0', port=10000)

bot = Client(
    "bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    workers=50,
    plugins=dict(root="plugins")
)

# Server aur Bot dono ko ek saath start karein
if __name__ == "__main__":
    Thread(target=run_server).start()
    bot.start()
    print("Bot Started ⚡")
    idle()
    bot.stop()
