import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, Application,ContextTypes,CommandHandler
TOKEN = os.environ.get("BOT_TOKEN")
PREDICTIONS = {
    "love": [  
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
    "study": [ 
        "Сегодня информация будет усваиваться легко! 😊",
        "Сложная тема внезапно станет понятной ❤️",
        "Преподаватель оценит твои старания ⭐️",
        "Групповая работа принесёт отличные результаты 👥",
        "Сегодня лучший день для начала подготовки к экзаменам 📝",
        "Твоя внимательность поможет заметить важные детали 🔍",
        "Не бойся задавать вопросы — это твой день 💡",
        "Успех в учёбе уже рядом, продолжай в том же духе! 🎯"
    ],
    "friends": [  
        "Старый друн напомнит о себе неожиданным сообщением 📱",
        "Сегодня отличный день для встречи с друнами 🎉",
        "Твоя поддержка будет очень нужна подруне 👭",
        "Новое знакомство перерастёт в крепкую дружбу 🤝",
        "Друны удивят тебя приятным сюрпризом 🎊",
        "Совместные планы на будущее вдохновят тебя 🌟",
        "Честный разговор укрепит вашу дружбу 💬",
        "Ты — настоящий друн, и это ценят вокруг 💝"
    ],
    "family": [
        "Семейный вечер принесёт радость 🏠",
        "Разговор по душам с близкими поможет расслабиться 💬",
        "Твоя забота о семье возвращается вдвойне 🔄"
    ],
    "career": [
        "Твои идеи заметит руководство 💼",
        "Сегодня удачный день для новых проектов 🚀",
        "Навыки, которые ты развиваешь, скоро окупятся 📈",
        "Неожиданное предложение может изменить многое ✨",
        "Командная работа принесёт отличные результаты 👥",
        "Твоя ответственность не останется незамеченной",
    ]
}

def get_prediction(topic):
    predictions_list = PREDICTIONS[topic]
    return random.choice(predictions_list)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("💕 Любовь", callback_data="love"),
            InlineKeyboardButton("📚 Учёба", callback_data="study")
        ],
        [
            InlineKeyboardButton("👭 Дружба", callback_data="friends"),
            InlineKeyboardButton("🏠 Семья", callback_data="family")
        ],
        [
            InlineKeyboardButton("💼 Карьера", callback_data="career")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🔮 *Привет! Я бот-предсказатель!* 🔮\n\n"
        "Я каждый день могу отправлять тебе предсказания.\n"
        "Выбери тему, которая тебя интересует сегодня:\n\n"
        "*Как это работает:*\n"
        "1. Нажми на кнопку с темой\n"
        "2. Я дам тебе предсказание на сегодня\n"
        "3. Завтра можешь выбрать новую тему или ту же самую\n\n"
        "Или используй команды:\n"
        "/love - предсказание про любовь\n"
        "/study - про учёбу\n"
        "/friends - про дружбу\n"
        "/family - про семью\n"
        "/career - про карьеру",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  
    topic = query.data  
    prediction = get_prediction(topic)
    topic_names = {
        "love": "Любовь",
        "study": "Учёба",
        "friends": "Дружба",
        "family": "Семья",
        "career": "Карьера"
    }
    await query.edit_message_text(
        f"✨ *Твоё предсказание на тему {topic_names[topic]}* ✨\n\n"
        f"🔮 {prediction} 🔮\n\n"
        f"Завтра можешь спросить снова!\n"
        f"Нажми /start чтобы выбрать другую тему",
        parse_mode="Markdown"
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 *Помощь по боту-предсказателю* 🔮\n\n"
        "*Команды:*\n"
        "/start - главное меню с кнопками\n"
        "/love - предсказание про любовь\n"
        "/study - предсказание про учёбу\n"
        "/friends - предсказание про дружбу\n"
        "/family - предсказание про семью\n"
        "/career - предсказание про карьеру\n"
        "/help - это сообщение\n"
        "/about - о боте\n\n"
        "*Совет:* удобнее всего использовать кнопки после /start!",
        parse_mode="Markdown"
    )
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("love", love_command))
    application.add_handler(CommandHandler("study", study_command))
    application.add_handler(CommandHandler("friends", friends_command))
    application.add_handler(CommandHandler("family", family_command))
    application.add_handler(CommandHandler("career", career_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.run_polling()
if '__main__' == __name__:
    main()
