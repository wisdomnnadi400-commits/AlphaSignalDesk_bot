import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ✅ Get the bot token from Render environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN is not set! Please add it in Render → Environment Variables.")

# Example start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Your bot is live and working on Render 🚀")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register commands
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()
