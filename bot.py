from pyrogram Client, filters
from yt_dlp import YoutubeDL


API_ID = 2040
API_HASH = "b18441a1ff607e10a989991a4502d31c"
BOT_TOKEN = "9047897146:AAEgX4S2VE5nq9IMan907LzVR5yv-qbXNTQ"
MY_TELEGRAM_ID = 8726422950

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(MY_TELEGRAM_ID) & filters.text)
def download_song(client, message):
    url = message.text
    if "youtube.com" in url or "youtu.be" in url:
        message.reply("⏳ جاري التحميل...")
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'song.mp3',
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        message.reply_audio("song.mp3")
    else:
        message.reply("يرجى إرسال رابط يوتيوب صالح.")

app.run()



API_ID = 2040
API_HASH = "b18441a1ff607e10a989991a4502d31c"
BOT_TOKEN = 9047897146:AAEgX4S2VE5nq9IMan907LzVR5yv-qbXNTQ

MY_TELEGRAM_ID =  8726422950

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(MY_TELEGRAM_ID) & filters.text)
def download_song(client, message):
    url = message.text
    if "youtube.com" in url or "youtu.be" in url:
        message.reply("⏳ جاري التحميل...")
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'song.mp3',
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        message.reply_audio("song.mp3")
    else:
        message.reply("يرجى إرسال رابط يوتيوب صالح.")

app.run()
