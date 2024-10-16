import discord
from discord.ext import commands
import random
import os
clasificacion_residuos = {
    "botellas": "Las botellan van en la caneca negra.",
    "cartones": "Los cartones van en la caneca marron.",
    "botellas de vidrio": "Las botellan van en la caneca blanca.",
    "Latas de aluminio": "Las latas de aluminio van en la caneca roja",

     
}
def clasificar_residuos(objeto):
    return clasificacion_residuos.get(objeto.lower(), "No tengo informacion sobre este objeto")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.command('clasificar')
async def clasificar(ctx, *, objeto:str):
    respuesta = clasificar_residuos(objeto)
    await ctx.send(f"Clasificacion: {respuesta}")
    
bot.run("MTI5NTkxOTk0NDI4NjA3NzAyOA.G7rtpA.giLLSinMMZ2MQqQ0TN9oSpFNOQ9qQQwOQU0zYA")