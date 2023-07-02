import discord
from discord.ext import commands
client = commands.Bot(command_prefix="=", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run("OTg3NzM2MjI5MDc4NTE1NzQy.GJ8nvc.YVFJlpkWD6dFZuCd1cfD08cAvToU1_BfwUvwk8")