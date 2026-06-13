import requests
import os
import asyncio
from telegram import Bot

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL_ID"]

def get_usdt_price():
    url = "https://api.bithumb.com/public/ticker/USDT_KRW"
    res = requests.get(url).json()
    return res["data"]["closing_price"]

async def send_message():
    price = get_usdt_price()

    text = f"""📈 빗썸 USDT 시세

💰 현재가: {price}원

#USDT #테더 #빗썸"""

    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHANNEL, text=text)
if __name__ == "__main__":
    asyncio.run(send_message())

