import os

from discord.ext import commands
from discord import Intents

import asyncpg

from utils import DB

bot = commands.Bot(command_prefix='.', intents=Intents.all(), help_command=None)


async def create_db_pool():
    bot.db_con = await asyncpg.create_pool(
        os.environ['DATABASE_URL']
    )

db = DB(bot)
