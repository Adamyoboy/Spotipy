
from discord import Spotify


import discord
import os
from discord.ext import commands
import asyncio
import random
import datetime



client = commands.Bot(command_prefix=commands.when_mentioned_or('.'), color=0x552E12, help_command=None,intents=discord.Intents.all(), case_insensitive=True)


def __init__(self, client):
    self.client = client

class Repo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["repo"])
    async def repository(self,ctx):
            embed = discord.Embed(
                title="Spotipy repository",
                url="https://github.com/Adamyoboy/Spotipy",
                description="Click on the title to go to the bot's repo!",
                color = 0xC902FF)

            embed.add_field(name="This repository includes of, all the commands that you are able to do.", value="For more information DM Adamyoboy#0001!")
            embed.add_field(name="The **Spotipy** bot is a open source non-profit way to view tracks of users with little effort.", value="This bot is written in Python!")
            await ctx.send (embed=embed)



async def setup(client):
    await client.add_cog(Repo(client))