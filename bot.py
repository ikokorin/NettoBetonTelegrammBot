from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот для запросов по методикам и материалам."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'ремонт' in text:
        await update.message.reply_text('Вот информация по методикам ремонта...')
    elif 'гидроизоляция' in text:
        await update.message.reply_text('Вот материалы для гидроизоляции...')
    else:
        await update.message.reply_text("Извините, я не понимаю ваш запрос.")

def main():
    token = '7727207924:AAEQKkLf9L6AQcvQn9NRf4QnSyHOzq7v4j4'  # Замените на ваш токен
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
