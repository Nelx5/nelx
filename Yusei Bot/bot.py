import random
import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

TOKEN = config.TOKEN



@bot.event
async def on_ready():
    print("Success: Bot is connected to Discord")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def おみくじ(ctx):
    results = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '大凶']
    result = random.choice(results)
    await ctx.send(f'{ctx.author.mention}さんの今日の運勢は{result}です！')

@bot.command()
async def pantu(ctx):
   #ランダムに選択して表示
    pantuir = ['あか','くろ','しろ']
    pantuiro =random.choice(pantuir)
    await ctx.send(f'あなたのパンツの色は{pantuiro}どえす')

@bot.command()
async def roulette(ctx) :
        members = ctx.guild.members
        #botを除外する  
        members =  [member for member in members if not member.bot]
        winer = random.choice(members)
        await ctx.channel.send(f'勝者は{winer.mention}です！おめでとうございます！')


bot.run(TOKEN)