from discord.ext import commands
from discord import Intents

import asyncpg

from utils import DB

bot = commands.Bot(command_prefix='.', intents=Intents.all(), help_command=None)


async def create_db_pool():
    bot.db_con = await asyncpg.create_pool(
        user='tullamore',
        password='grats',
        host='127.0.0.1',
        port='5432',
        database='postgres'
    )

db = DB(bot)
