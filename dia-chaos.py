import discord
from discord.ext import commands
import random
import typing
from dotenv import load_dotenv
import os

load_dotenv()

MIN_RANDINT = -2147483648
MAX_RANDINT = 2147483647
coin = ['heads', 'tails']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def flip(ctx):
    await ctx.send(f'Result: {random.choice(coin)}')

@bot.command()
async def rand(ctx, minimum: typing.Optional[int], maximum: typing.Optional[int]):
    if not minimum: minimum = MIN_RANDINT
    if not maximum: maximum = MAX_RANDINT

    if minimum > maximum:
        await ctx.send('Error: The minimum is greater than the maximum.')
        return
    elif minimum == maximum:
        await ctx.send('Error: The minimum and the maximum are equal.')
        return
    else:
        rand_result = random.randint(minimum, maximum)
        await ctx.send(f'Result: {rand_result}')
        return

bot.run(os.environ['BOT_TOKEN'])
