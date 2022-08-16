import discord
from discord.ext import commands
from decouple import config

TOKEN = 'MTAwODg5ODEyMDY4OTY2MDA2NA.GU6TwT.tScKSU39olqXR_YX-N36Nhdo17Efv_HDQ5hlzQ'
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot online.')

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command() 
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("You are not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)

@client.command()
async def play(ctx):
    voice_channel = ctx.author.voice.channel
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio('https://listen1.myradio24.com/8234'), after=lambda e: print('done', e))

client.run(TOKEN)
