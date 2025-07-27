import os
from flask import Flask, request
import telegram

# Your bot token from @BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN") or "YOUR_BOT_TOKEN_HERE"
bot = telegram.Bot(token=BOT_TOKEN)

app = Flask(__name__)

# Basic home route (useful for Render's health check)
@app.route('/')
def home():
    return "Bot is running!"

# Telegram will POST updates here
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # Respond to any text message
    if text:
        bot.send_message(chat_id=chat_id, text="Aur btao 👀")
    return "OK"

# Set webhook when starting (optional)
@app.route('/set_webhook')
def set_webhook():
    webhook_url = f"https://YOUR_RENDER_URL.onrender.com/{BOT_TOKEN}"
    success = bot.set_webhook(url=webhook_url)
    return "Webhook set!" if success else "Failed to set webhook."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
