import discord
from discord.ext import commands
import youtube_dl

bot = commands.Bot(command_prefix ="$", description = "Bot du Fab")

@bot.event
async def on_ready():
    print("--- Ready ---")
    channel = bot.get_channel(963007190308892702)
    await channel.send("Turned on")

@bot.command(aliases= ['hi'])
async def Hi(ctx):
    await ctx.send(f"Yoosh  #{ctx.author.mention} !", )

@bot.command(aliases=['sol','soline','Soline'])
async def Sol(ctx):
    await ctx.send(f"Yooooosh Soline !!", tts=True)

@bot.command(aliases= ['purge','Purge','prg','Prg','delete','Delete','del','Del','dl','Dl','suppr','clr','Clr','cl','Cl','Clear']) #clear command
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount: int = None):
    if amount == None:
        await ctx.channel.purge(limit=1000000)
    else:
       await ctx.channel.purge(limit=amount)

@bot.command()
async def Boom(ctx):
    await ctx.send("boom !", tts=True)

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg, tts = True)

#   /usr/bin/python3 "/Volumes/Macintosh HD - Données/FICHIERS/ESILV/VsCode/Bot-Discord/Bot.py"

bot.run("OTYzMzg1MTY3MjgyNTg5NzA3.YlVUWg.DAEkTP7NxDCOdSbbd6n6Qpg9o-U")