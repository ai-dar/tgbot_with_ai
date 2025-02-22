import telebot
from g4f.client import Client

# Инициализация бота
API_TOKEN = 'TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Инициализация клиента g4f
client = Client()

# Словарь для хранения истории разговоров
conversation_history = {}

# Функция для обрезки истории разговора
def trim_history(history, max_length=4096):
    current_length = sum(len(message["content"]) for message in history)
    while history and current_length > max_length:
        removed_message = history.pop(0)
        current_length -= len(removed_message["content"])
    return history

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def process_start_command(message):
    bot.reply_to(message, "Привет! Я бот с поддержкой GPT-4. Задай мне любой вопрос.")

# Обработчик команды /clear
@bot.message_handler(commands=['clear'])
def process_clear_command(message):
    user_id = message.from_user.id
    conversation_history[user_id] = []
    bot.reply_to(message, "История диалога очищена.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def send_gpt_response(message):
    user_id = message.from_user.id
    user_input = message.text

    # Инициализация истории пользователя, если ее нет
    if user_id not in conversation_history:
        conversation_history[user_id] = []

    # Добавляем сообщение пользователя в историю
    conversation_history[user_id].append({"role": "user", "content": user_input})
    conversation_history[user_id] = trim_history(conversation_history[user_id])

    try:
        # Отправка запроса к модели GPT
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history[user_id],
        )
        chat_gpt_response = response.choices[0].message.content  # Исправлено здесь

        # Добавляем ответ бота в историю
        conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})

        # Отправляем ответ пользователю
        bot.reply_to(message, chat_gpt_response)
    except Exception as e:
        print(f"Error while processing GPT request: {e}")
        bot.reply_to(message, "Извините, произошла ошибка. Попробуйте снова.")

# Запуск бота
if name == "main":
    bot.polling(none_stop=True)
