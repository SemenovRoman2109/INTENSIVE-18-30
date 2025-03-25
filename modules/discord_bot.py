r"""
    ## Модуль для роботи з Discord ботом
    ### У цьому файлі прописується логіка взаємодії бота(WorldIT_Helper) з сервером
"""
import discord, dotenv, os

# 
dotenv.load_dotenv()
# 
TOKEN = os.getenv('TOKEN')

# 
intents = discord.Intents.default()
intents.message_content = True

#
bot = discord.Client(intents=intents)

# 
@bot.event
async def on_ready():
    print("Бот запущенно")


@bot.event
# 
async def on_message(message):
    # 
    if message.author != bot.user:
        # 
        content = message.content
        # 
        if content:
            # 
            await message.channel.send(content)