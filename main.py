import discord
import envvars
from discord.ext import commands
from discord.voice_client import VoiceClient
import episodes
import asyncio

token = envvars.BOT_TOKEN
bot = commands.Bot(command_prefix = '>')

players = []

@bot.command(pass_context=True)
async def nc(ctx, arg):
    episodes.get(arg)
    
    user = ctx.message.author
    voice_channel = user.voice.channel

    if voice_channel != None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('episodio.mp3'), after=lambda e: print('done', e))
        global players 
        players = vc

@bot.command(pass_context=True)        
async def pause(ctx):
    if players.is_playing():
        players.pause() 

@bot.command(pass_context=True)        
async def stop(ctx):
    players.stop()
    await asyncio.sleep(3)
    await players.disconnect()

@bot.command(pass_context=True)        
async def resume(ctx):
    if players.is_stopped():
       players.resume()

@bot.command(pass_context=True)
async def dc(ctx):
    await players.disconnect()

@bot.command(pass_context=True)
async def comandos(ctx):
    await ctx.send("Os comandos disponíveis são:\n\n>nc <link do episódio do nerdcast> -> toca o episódio\n>pause -> pausa o áudio\n>stop -> para o áudio (sem ter como dar resume depois) e sai do servidor\n>resume -> volta a tocar o áudio de onde parou\n>dc -> desconecta o bot do chat de voz")

bot.run(token)
