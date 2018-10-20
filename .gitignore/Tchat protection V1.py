import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Protéger ton Tchat"))
    print("Logged in as",client.user.name)
    print("ID :",client.user.id)

chat_filter = ["MERDE", "CON", "CONNARD", "CONARD", "PENIS", "PIPI", "CACA", "PROUT", "FESSE", "ZIZI", "NIQUE TA MERE", "PENIS", "FUMIER", "CUL", "CHATE", "TA MERE", "DIANTRE", "MERDIER", "MERDEUX", "MERDEUSE", "ENCULE", "FILS DE PUTE", "NICK TA MERE", "COUILLE", "PUTAIN", "BCP", "FDP", "ENCULER", "SUCEUSE", "PUTE", "SALOP", "SALOPE", "MERDE", "BITE", "SHIT", "MERD", "FUCK", "EMMERDE", "SUCE", "CROTTE", "CHIASSE", "PD", "FILS DE PUTE", "TA MERE", "FILS DE PUTE.", "FILS DE PUTE..", "FILS DE PUTE...", "TG", "CUL", "NTM", "COUILLES", "BATARD", "NICK", "TA MERE", "NIQUE TA MERE", "NIQUE", "CONNERIE", "VA TE FAIRE FOUTRE", "SALE MERDE", "TA GUEULE", "CONASSE", "CONNE"]
bypass_list = []

@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.send_message(message.channel,"**Hey** vous n'avez pas le droit d'écrire ça !!!")
    
client.run("NDkyOTcwMTU0NjA3NTA5NTA0.DoenGA._Jf5DZNHQOoMFda3WHx4Dj4mCpo")
