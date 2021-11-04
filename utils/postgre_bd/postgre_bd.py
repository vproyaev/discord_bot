from discord.ext import commands


class DB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print('DB has been connected')
        sql = """
            CREATE TABLE IF NOT EXISTS discord_users (
            DS_ID BIGINT PRIMARY KEY,
            MESSAGE_COUNT INTEGER NOT NULL DEFAULT 0,
            LEVEL INTEGER NOT NULL DEFAULT 0
            );
            """
        await self.bot.db_con.execute(sql)

    async def add_user(self, ds_id):
        sql = """
        INSERT INTO discord_users(DS_ID)
        VALUES($1)
        ON CONFLICT (DS_ID)
        DO NOTHING
        """
        await self.bot.db_con.execute(sql, ds_id)

    async def can_upgrade(self, ds_id):
        sql = """
        SELECT MESSAGE_COUNT
        FROM discord_users
        WHERE DS_ID = $1
        """
        return await self.bot.db_con.fetch(sql, ds_id)

    async def count_message(self, ds_id):
        sql = """
        UPDATE discord_users
        SET MESSAGE_COUNT = (SELECT MESSAGE_COUNT FROM discord_users WHERE DS_ID = $1) + 1
        WHERE DS_ID = $1
        """
        await self.bot.db_con.execute(sql, ds_id)

    async def upgrade_level(self, ds_id):
        sql = """
        UPDATE discord_users
        SET LEVEL = (SELECT LEVEL FROM discord_users WHERE DS_ID = $1) + 1
        WHERE DS_ID = $1
        """
        await self.bot.db_con.execute(sql, ds_id)

    async def user_level(self, ds_id):
        sql = """
        SELECT LEVEL
        FROM discord_users
        WHERE DS_ID = $1
        """
        return await self.bot.db_con.fetch(sql, ds_id)
