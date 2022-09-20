import discord
import asyncio
import random

from discord import message

client = discord.Client()

token = 'MTAyMTg1ODgwMTQ3OTA2OTczNg.GUw0lI.DqaVm6QUaKuVsH69pRTWpeW6nfUmFfaFvd-i4s' #봇 토큰

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('잠자는 중') #봇 ~하는중 입력
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "안녕": #내가 '안녕'이라고 말하면
        await message.channel.send (f"안녕하세요") #봇이 '안녕하세요'라고 대답

client.run(token)