import discord
from discord.ext import commands
import youtube_dl
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix ="$", description = "On découvre python c nice",intents=intents)


###AU DEMARRAGE
@bot.event
async def on_ready():
    print("--- Ready ---")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Netflix"))
    channel = bot.get_channel(963007190308892702)
    await channel.send("< ON >")

    #guil=ctx.message.guild.id



###ENSEMBLE DE COMMANDES
#Recupération id
@bot.command()  
async def mem(ctx):
  members = await ctx.guild.fetch_members(limit=150).flatten()
  for member in members:
    await ctx.send(f"{member.name} = {member.id}")
    
@bot.command()
async def test(ctx,*reason):
    dic={}
    dic['aval']=" ".join(reason)
    print(dic['aval'])
    print(dic)


#Commande de CLEAR
@bot.command(aliases= ['clear','Cl','CL','cl']) #clear command
@commands.has_permissions(manage_messages=True)
async def Clear(ctx,amount: int = None):
    if amount == None:
        await ctx.channel.purge(limit=1000000)
    else:
       await ctx.channel.purge(limit=amount+1)

#Commande infoserveur
@bot.command(aliases= ['Infoserveur','Info','info'])
async def InfoServeur(ctx):
    server = ctx.guild
    NombreChanText = len(server.text_channels)
    NombreChanVoc = len(server.voice_channels)
    NombrePersonnes = server.member_count
    NomServeur = server.name
    message = f"Le serveur **{NomServeur}** contient {NombrePersonnes} personnes. \nLe serveur possède {NombreChanText} salons textuels et {NombreChanVoc} salons vocaux."
    await ctx.send(message)

#Commande de Kick
@bot.command()
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user , reason = reason)
    await ctx.send(f"{user} a été kick.")


@bot.command(aliases= ['hi'])
async def Hi(ctx):
    await ctx.send(f"Yoosh {ctx.author.mention} !", )
@bot.command()
async def Parrot(ctx, *arg):
    await ctx.send(" ".join(arg), tts = True)


@bot.command()
async def Poll(ctx, question, options, *choice):
 
    message = f"{question} \n"
    for i in range(int(options)):
        message += choice,"\n"
    
    await ctx.send(message)

#Youtube
musics = {}

ytdl = youtube_dl.YoutubeDL()

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url, before_options =  "-reconnect 1 - reconnect_streamed 1 - reconnect_delay_max 5"))
    
    async def next (_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.diconnect(), bot.loop)

    client.play(source, after = next)


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()

@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild]= []

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()

@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()

@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild]=[]
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)





#   /usr/bin/python3 "/Volumes/Macintosh HD - Données/FICHIERS/ESILV/VsCode/Bot-Discord/Bot.py"

bot.run("OTYzMzg1MTY3MjgyNTg5NzA3.YlVUWg.DAEkTP7NxDCOdSbbd6n6Qpg9o-U")