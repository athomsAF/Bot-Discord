import discord
from discord.ext import commands
import youtube_dl

bot = commands.Bot(command_prefix ="!", description = "Bot du Fab")
musics ={}
ytdl=""

@bot.event
async def on_ready():
    print("Ready !")
    channel = bot.get_channel(963007190308892702)
    await channel.send("Salut je suis allumé!!!")

bot.run("OTYyNzc4OTczODA3NDQ4MDk1.YlMfyg.XnRmFuH4O-iRFHeFcQ5Em26JiIU")