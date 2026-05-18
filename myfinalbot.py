import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, Application,ContextTypes,CommandHandler

TOKEN = os.environ.get("TOKEN")
PREDICTIONS = {
    "love": [  # предсказания про любовь
        "Оу да детка ты такая сладкая конфетка!",
        "Сегодня тебя ждёт неожиданная встреча! ❤️",
        "Твоя улыбка привлечёт внимание особенного человека ❤️",
        "Старые чувства могут вспыхнуть с новой силой ❤️",
        "Будь открыта новым знакомствам — судьба уже близко ❤️",
        "Сегодня звёзды говорят 'да' первому шагу с твоей стороны ❤️",
        "Твоё сердце найдёт отклик в неожиданном месте ❤️",
        "Не бойся проявлять нежность — это твой день ❤️",
        "Романтический сюрприз уже в пути! 🎉",
    ],
    "study": [  # предсказания про учёбу
        "Сегодня информация будет усваиваться легко! 😊",
        "Сложная тема внезапно станет понятной ❤️",
        "Преподаватель оценит твои старания ⭐️",
    ],
    "friends": [  # добавь остальные темы
        "Старый друг напомнит о себе! 📱",
    ],
    "family": [
        "Семейный вечер принесёт радость 🏠",
    ],
    "career": [
        "Твои идеи заметит руководство 💼",
    ]
}

def get_prediction(topic):
    return random.choice(PREDICTIONS[topic])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💕 Любовь", callback_data="love"), InlineKeyboardButton("📚 Учёба", callback_data="study")],
        [InlineKeyboardButton("👭 Дружба", callback_data="friends"), InlineKeyboardButton("🏠 Семья", callback_data="family")],
        [InlineKeyboardButton("💼 Карьера", callback_data="career")]
    ]
    await update.message.reply_text("🔮 Привет! Выбери тему:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    topic = query.data
    prediction = get_prediction(topic)
    topic_names = {"love": "Любовь", "study": "Учёба", "friends": "Дружба", "family": "Семья", "career": "Карьера"}
    await query.edit_message_text(f"✨ {topic_names[topic]} ✨\n\n🔮 {prediction} 🔮")

def main():
    print("Бот запускается...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    print("Бот работает!")
    application.run_polling()

if __name__ == '__main__':
    main()