from discord.ext import commands
from discord import Intents

import asyncpg

from utils import DB

bot = commands.Bot(command_prefix='.', intents=Intents.all(), help_command=None)


async def create_db_pool():
    bot.db_con = await asyncpg.create_pool(
        user='cucbziofgbgzbf',
        password='59276a7be9242b541a4f3931b2112e3a853d77ff0486bfdcfbd0dae2634a0282',
        host='c2-54-73-110-26.eu-west-1.compute.amazonaws.com',
        port='5432',
        database='den8249gj7mdb2',
        URI='postgres://cucbziofgbgzbf:59276a7be9242b541a4f3931b2112e3a853d77ff0486bfdcfbd0dae2634a0282@ec2-54-73-110-26.eu-west-1.compute.amazonaws.com:5432/den8249gj7mdb2'
    )

db = DB(bot)
