import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix = '>', case_insensitive=True)
client.remove_command('help')

load_dotenv()
TOKEN = os.getenv("DISCORDTOKEN")

#@client.command()
#async def load(ctx, extension):
    #client.load_extension(f'cogs.{extension}')

#@client.command()
#async def unload(ctx, extension):
    #client.unload_extension(f'cogs.{extension}')

@client.event 
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You need to pass a argument.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
 
client.run(TOKEN)