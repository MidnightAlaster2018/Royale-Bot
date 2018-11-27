import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
Client = discord.Client()
client = commands.Bot(command_prefix = "r!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content =="cookie":
        await client.send_message(message.channel, ":cookie:")

    if message.content =="hello":
        await client.send_message(message.channel, "Hi,hope you are having a nice day! https://orig11.deviantart.net/92db/f/2014/319/0/6/hello__i_am_baymax_by_cjsux-d86k5xq.gif ")
          
    if message.content =="bye":
        await client.send_message(message.channel, "See ya,hope you will be back soon,take care!:) https://media.giphy.com/media/kOnoObmFUE0k8/giphy.gif")

    if message.content =="good night":
        await client.send_message(message.channel, "Plesant Dreams,don't let the bed bugs kiss you! https://media.giphy.com/media/11kn6DFp9BNqWA/giphy.gif")

    if message.content =="good morning":
        await client.send_message(message.channel, "Rise and Shine,now go get some coffe https://tenor.com/view/coffee-time-coffee-to-the-rescue-coffee-adulting-mornings-gif-7960266")

    if message.content =="bored":
        await client.send_message(message.channel, " Really now? Well then do something then!:)https://66.media.tumblr.com/1d02d51249fa8a0c8f8bdad5de38f6f0/tumblr_og4h5cRQRV1u70edno1_500.gif ")

    if message.content =="cute":
        await client.send_message(message.channel, "https://i.gifer.com/3vIF.gif")


    if message.content =="Merry Christmas!":
        await client.send_message(message.channel, "https://i.gifer.com/2Kjg.gif")


    if message.content =="Happy Holidays!":
        await client.send_message(message.channel, "http://i.imgur.com/iCWTF3z.gif")

    if message.content =="Happy New Year!":
        await client.send_message(message.channel, "https://lefthandeddragon.files.wordpress.com/2018/07/amazing-electrc-feel-fireworks-gif.gif?w=687")

    if message.content =="welcome":
        await client.send_message(message.channel, "http://i.imgur.com/IZSZWTA.gif")

        
    if message.content == "Welcome!":
        await client.send_message(message.channel, "https://i.imgur.com/8GAOrWc.gif")


    if message.content.upper().startswith('r!SAY'):
        args = message.content.split(" ")
        #args[0] = r!SAY
        #args[1] =Hey
        #args[2] =There
        #args[1:] =Hey There
        await client.send_message(message.channel, "%s" %(" ".join(args[1:])))

token = os.environ.get("TOKEN")
client.run(f'{token}')
