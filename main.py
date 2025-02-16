import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = os.getenv("7809195287:AAE0KVR6PNbdlb9-dpNSwPXu11RI4iRZgMw")

# Start Command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm SpecterBot. How can I assist you?")

# Help Command
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Available commands:\n/start - Start the bot\n/help - Get help")

# Handle Messages
async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")

# Webhook Server for Vercel
class WebhookServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot is running')

# Run Telegram Bot
def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    run_bot()
