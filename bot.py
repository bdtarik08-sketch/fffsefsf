from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import jwt
import datetime

BOT_TOKEN = "8411147426:AAGkTZx4uawOYg2jLX-2TsZlTtsdq1qx2sg"
SECRET = "Shuvo123!@#SuperSecretKey"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send your UID")

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.message.text
    
    payload = {
        "uid": uid,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    await update.message.reply_text(f"Generated Token:\n{token}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))

app.run_polling()