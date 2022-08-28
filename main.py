from youtube_search import YoutubeSearch

def searcher():
    res = YoutubeSearch('python FMS telegram bot', max_results=1).to_dict()
    with open('text.py', 'w', encoding='utf-8') as r:
        r.write(str(res))

searcher()


# import requests
# from bs4 import BeautifulSoup
# import re
#
# def searcher():
#     response = requests.get('https://www.youtube.com/results?search_query=python')
#     soup = BeautifulSoup(response.content, 'html.parser')
#     search = soup.find_all('script')[32]
#     key = '"videoId":"'
#     data = re.findall(key + r'([^*]{11})', str(search))
#     print(data)
#     print(search)
#
# searcher()








# from aiogram import Bot, types, utils
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
# import os
#
# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)
#
# executor.start_polling(dp, skip_updates=True)