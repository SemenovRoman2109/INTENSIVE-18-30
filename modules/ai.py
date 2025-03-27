r"""
    ## Модуль для роботи з API штучного інтелекту(OpenAI)
    ### у цьому файли генерувати відповіді від ШІ 
"""
import openai
import dotenv, os

# 
dotenv.load_dotenv()
OPENAI_SECRETKEY = os.getenv("OPENAI_SECRETKEY")

# 
client_openai = openai.AsyncOpenAI(api_key= OPENAI_SECRETKEY)

# 
async def get_responce_from_ai(request: str):
    # 
    response = await client_openai.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:worldit::BFm4aTNw", #
        messages = [{
            "role": "user", #
            "content": request, #
        }]
    )
    # 
    return response.choices[0].message.content
        

