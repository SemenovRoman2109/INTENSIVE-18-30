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
    """
        Ця функція буде обробляти подію запуску бота і після запуску виводить нам повідомлення "Бот запущенно" 
    """
    print("Бот запущенно")

# Декоратор який реагує на подію отримання повідомлення, від користувача.
@bot.event
async def on_message(message: discord.Message):
    """
        Функція відповідає на повідомлення користувача згенероване ші. 
        Може розпізнавати різні види запитів (текст, картинка, аудіо) 
    """
    try:
        # Перевіряємо, що повідомлення не ботом
        if message.author != bot.user:
            # Зберігаємо повідомлення користувача
            content = message.content
            message_for_answer = await message.channel.fetch_message(message.id)
            # Перевіряємо, що повідомлення не пусте
            if content:
                # Обробка генерації зображень
                if content.startswith("!image"):
                    # Отримання відповіді згенерованого зображення
                    answer = await get_image(prompt = content[6:])
                    await message_for_answer.reply(answer)
                # Обробка генерації звуків
                elif content.startswith("!voice"):
                    # Отримання відповіді згенерованого звуку
                    audio = await get_voice(text = content[6:])
                    await message_for_answer.reply("Ось звук який ви отримали:", file = discord.File(audio, filename="speech.mp3"))
                # Обробка генерації тексту, відповіді на питання
                else:
                    # Отримання відповіді згенерованого тексту
                    answer = await get_response_from_ai(content)
                    await message_for_answer.reply(answer)
    # Обробка помилок
    except Exception as error:
        print(f"Error: {error} \n in message - ",message)