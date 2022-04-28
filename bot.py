

from discord import Spotify


import discord
import os
from discord.ext import commands
import asyncio
import random
import datetime





client = commands.Bot(command_prefix=commands.when_mentioned_or('.'), color=0x552E12, help_command=None,intents=discord.Intents.all(), case_insensitive=True)


@client.event
async def on_ready():
   print('Started as:\n{0.user.name}\n{0.user.id}'.format(client))


@client.command()
async def load(ctx, extension):        
        await client.load_extension(f'cogs.{extension}')

        
@client.command()
async def unload(ctx, extension):
        await client.unload_extension(f'cogs.{extension}')

       
@client.command()
async def reload(ctx, extension):
        await client.unload_extension(f'cogs.{extension}')
        await client.load_extension(f'cogs.{extension}')

@client.command(name="ad")
async def addd(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                    url=(f"{activity.track_url}"),
                    title = "Listening to {}".format(activity.title).format(activity.artist),
                    description=f"This song is being played by {user.name}",
                    color = 0xC902FF)
        
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Artist", value=activity.artist)
                embed.add_field(name="Album", value=activity.album)
                embed.set_footer(text=f"Requested by {ctx.author}")
                message = await ctx.send(embed=embed)
                await message.add_reaction('⬆️')
                await message.add_reaction('⬇️')






async def ssss():
        for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                        await client.load_extension(f'cogs.{filename[:-3]}')



        



async def runner():
    async with client:
        await ssss()
        await client.start("")

asyncio.run(runner())
