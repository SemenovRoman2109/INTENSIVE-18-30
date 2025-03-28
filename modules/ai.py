r"""
    ## Модуль для роботи з API штучного інтелекту(OpenAI)
    ### у цьому файли генерувати відповіді від ШІ 
"""
import openai
import dotenv, os
import random
import io

list_voice = ['alloy', 'ash', 'coral', 'echo', 'fable', 'onyx', 'nova', 'sage', 'shimmer']
# 
dotenv.load_dotenv()
OPENAI_SECRETKEY = os.getenv("OPENAI_SECRETKEY")

# 
client_openai = openai.AsyncOpenAI(api_key= OPENAI_SECRETKEY)

# 
async def get_response_from_ai(request: str):
    """
        Функція для обробки запитів(промптів) користувачів штучним інтелектом, який повертає текстову відповідь.
        Штучний інтелект попередньо натренований нами, за допомогою Fine-Tuning
    """
    # 
    response = await client_openai.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:worldit::BFf7bJwz", #
        messages = [{
            "role": "user", #
            "content": request, #
        }]
    )
    # 
    return response.choices[0].message.content
        
async def get_image(prompt: str):
    """
        Функція для обробки запитання користувача та генерації зображення на його основі. 
    """
    response = await client_openai.images.generate(
        model = "dall-e-2",
        prompt = prompt,
        size="1024x1024",
        quality= "standard"
    )
    return response.data[0].url

async def get_voice(text: str):
    """ 
        Ця функція озвучує текст за допомогою випадкового голосу 
    """ 
    response = await client_openai.audio.speech.create(
        input=text,
        model="gpt-4o-mini-tts",
        voice = random.choice(list_voice)
    )
    audio_file = io.BytesIO(response.content)
    return audio_file
