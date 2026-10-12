import discord, os, random
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

def get_duck_image_url():    
    url = 'https://www.pngarts.com/files/2/Duck-Transparent-Image.png'
    return url

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ecology_fact(ctx):
    await ctx.send("Here is a random ecology fact.")
    facts = ["Underground wood networks: trees in a forest are connected together through roots, this network is called \"Wood Wide Web\" ",
            "Sahara dust feeds the Amazon: Wind blows millions of tons of dust from the Sahara Desert across the Atlantic Ocean every year, dropping essential minerals like iron that fertilize the Amazon Rainforest.",
            "Soil biodiversity: More than half of all species on Earth live in the soil, making the ground beneath our feet one of the most biodiverse habitats on the planet.",
            "Kelp forest climate powerhouses: Kelp forests can store up to 20 times more carbon per acre than land-based forests, and sea otters help keep them healthy by eating sea urchins that would otherwise destroy them.",
            "Oceans make half our oxygen: Tiny drifting marine organisms called phytoplankton produce about 50% of the oxygen in Earth's atmosphere through photosynthesis."]
    await ctx.send(random.choice(facts))
    # all of these facts come from "https://www.worldenvironmentday.global/did-you-know/fun-facts"
    
bot.run("TOKEN")
