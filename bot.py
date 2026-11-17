import discord
from discord.ext import commands
import requests

config = discord.Intents.default()
config.message_content = True

coiso = commands.Bot(command_prefix='thing_', intents=config)

def pegar_clima(cidade):
    url = f"https://wttr.in/{cidade}?format=%C+%t"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.text.strip()
    else:
        return "mestre,sei qual o clima não!"


@coiso.command()
async def hello(ctx):
    await ctx.send('tá funcionando,grande mestre pokemon!')

@coiso.command()
async def clima(ctx,*,cidade):
    info = pegar_clima(cidade)
    await ctx.send(f"O tempo em {cidade} é {info}")

coiso.run("")
