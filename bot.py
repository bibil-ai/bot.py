import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx):
    await ctx.send(f"aku laper")

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.lower().split('d'))
    except ValueError:
        await ctx.send("Format harus seperti 2d6!")
        return

    if rolls <= 0 or limit <= 0:
        await ctx.send("Jumlah dadu dan jumlah sisi harus lebih dari 0.")
        return

    hasil = [random.randint(1, limit) for _ in range(rolls)]

    await ctx.send(
        f"Hasil: {', '.join(map(str, hasil))}\n"
        f"Total: {sum(hasil)}"
    )


bot.run("cari sendiri token mu, XD")
