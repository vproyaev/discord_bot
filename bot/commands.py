import discord

from loader import bot, db


@bot.command()
async def help(ctx):
    await ctx.send('Hi. This bot was made for a test task for "mello"!\n\n'
                   'We have 4 main command:\n'
                   '👉 .kick [nickname] - for kick anybody\n'
                   '👉 .ban [nickname] - for ban anybody\n'
                   '👉 .unban [nickname] - for unban anybody\n'
                   '👉 .level - for information about your level\n\n'
                   '**REMEMBER!**\n'
                   '*Use the special symbol before command* - **"."**'
                   )
    if ctx.message.author.guild_permissions.administrator:
        await db.add_user(ctx.message.author.id)


@bot.command()
async def kick(ctx, user_name: discord.User):
    await ctx.guild.kick(user=user_name, reason='You have been kicked!')
    await ctx.send(f'{user_name} had been kicked from this channel!')


@bot.command()
async def ban(ctx, user_name: discord.User):
    if not ctx.message.author.guild_permissions.administrator:
        await ctx.send(f"{user_name.mention} you don't have permission!")
    else:
        await ctx.guild.ban(user=user_name, reason='You have banned kicked!')
        await ctx.send(f'{user_name} had been banned from this channel!')


@bot.command()
async def unban(ctx, user_name: discord.User):
    await ctx.guild.unban(user=user_name, reason='You have unbanned kicked!')
    await ctx.send(f'{user_name} had been unbanned from this channel!')


@bot.command()
async def level(ctx):
    user_id = ctx.author.id
    user_name = ctx.author

    user_level = await db.user_level(user_id)
    user_level = user_level[0][0]

    await ctx.send(f'{user_name.mention} **your level - {user_level}**')

