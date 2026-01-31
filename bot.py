from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8391518472:AAHQ-t-A3y0p9D4XKwC2H_ySXcXGwi4H9_0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك!\n\n"
        "اضغط على الرابط التالي للمتابعة 👇\n"
        "https://example.com"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()