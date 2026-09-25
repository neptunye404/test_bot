import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def random_text_emoji(ctx):
    text_emoji_list = [":D",":)",":(",">:D",";)",";(",]
    await ctx.send(random.choice(text_emoji_list))

@bot.command()
async def random_number(ctx):
    await ctx.send(random.randint(1,100),"!")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("TOKEN")
