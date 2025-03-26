r"""
    ## Модуль для роботи з Discord ботом
    ### У цьому файлі прописується логіка взаємодії бота(WorldIT_Helper) з сервером
"""
import discord, dotenv, os
from .ai import *

# Завантажуємо змінні середовища з файлу .env, там зберігаються  токен бота щоб не вкрали 
dotenv.load_dotenv()
# Отримуємо токен з .env файлу (змінних середовища)
TOKEN = os.getenv('TOKEN')

# Ініціалізуємо (створюємо) об'єкт, який налаштовує дозволи. З стандартними налаштуваннями
intents = discord.Intents.default()
intents.message_content = True

# Створюємо бота, з вказаними налаштуваннями
bot = discord.Client(intents=intents)

# Декоратор який реагує на подію запуск боту.
@bot.event
async def on_ready():
    print("Бот запущенно")

# Декоратор який реагує на подію отримання повідомлення, від користувача.
@bot.event
async def on_message(message: discord.Message):
    # Перевіряємо, що повідомлення не ботом
    if message.author != bot.user:
        # Зберігаємо повідомлення користувача
        content = message.content
        # Перевіряємо, що повідомлення не пусте
        if content:
            # 
            answer = await get_responce_from_ai(content)
            # 
            message_for_answer = await message.channel.fetch_message(message.id)
            # 
            await message_for_answer.reply(answer)