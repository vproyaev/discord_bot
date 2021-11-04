from discord import Message

from loader import bot, db


@bot.event
async def on_member_join(member):
    member_id = member.id

    for channel in bot.get_guild(member.guild.id).channels:
        if channel.name == 'основной':
            await bot.get_channel(channel.id).send(f'{member.display_name} connected to the channel\n'
                                                   f'*Use ".help" to get information about commands*')
            await db.add_user(member_id)


@bot.event
async def on_member_remove(member):
    for channel in bot.get_guild(member.guild.id).channels:
        if channel.name == 'основной':
            await bot.get_channel(channel.id).send(f'{member.display_name} left channel')


@bot.event
async def on_message(message):
    if message.author != bot.user:
        user_id = message.author.id
        await bot.process_commands(message)

        await db.count_message(user_id)
        message_count = await db.can_upgrade(user_id)
        message_count = message_count[0][0]

        if message_count % 20 == 0:
            await db.upgrade_level(user_id)
            user_level = await db.user_level(user_id)
            user_level = user_level[0][0]

            await message.channel.send(f'{message.author.mention} increased the level to {user_level}')
