from data.config import BOT_TOKEN

from loader import bot, create_db_pool, db


@bot.event
async def on_ready():
    await db.on_ready()
    print('Bot has been started!')
    print('_____________________________________________________________________________________')


if __name__ == '__main__':
    from bot import commands, events
    bot.loop.run_until_complete(create_db_pool())
    bot.run(BOT_TOKEN)
