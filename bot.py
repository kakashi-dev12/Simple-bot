from flask import Flask, request
import telegram

# 🔑 Paste your bot token here directly
BOT_TOKEN = "8386051850:AAHCia0vg5MDpjwUjRW7q6FUjl6reuwa5uk"
bot = telegram.Bot(token=BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # 💬 Respond to any text message
    if text:
        bot.send_message(chat_id=chat_id, text="Aur btao 👀")
    return "OK"

@app.route('/set_webhook')
def set_webhook():
    webhook_url = f"https://YOUR_RENDER_URL.onrender.com/{BOT_TOKEN}"
    success = bot.set_webhook(url=webhook_url)
    return "Webhook set!" if success else "Failed to set webhook."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
