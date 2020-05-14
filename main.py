# from discord.ext import commands
from discord.ext.commands import bot, Bot
import discord
import combo_generator
import authentication

discord.client

TOKEN = authentication.secret
bot = Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def combo(ctx, *args):
    converted_combo = combo_generator.convert(args)
    await ctx.send(converted_combo)

@bot.command()
async def combo_bug(ctx, *args):
    await ctx.send('theres been a bug!')



bot.run(TOKEN)
