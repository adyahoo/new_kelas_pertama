import discord
from discord.ext import commands

# import fungsi
from bot_logic import gen_pass

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {bot.user}')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def halo(ctx):
    await ctx.send(f'Hi! saya adalah bot python pro')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def generate_pass(ctx):
    await ctx.send(gen_pass(15))

bot.run("MTU3MzMyMTExNDY0NDUxMjgzOA.GgfnDV.h5t55JHcYNG8X0wGD2E1FYpo4m4Nra5W9KBkA0")
