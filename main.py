import datetime
import discord
import os
import os.path
from io import BytesIO
import aiohttp
import json
from discord import shard
from discord.enums import PremiumType
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import command
import sys
from discord import embeds
from discord import activity
from discord.flags import Intents 
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from utils.utils import utils 
from utils.utils import db, bot_id
from discord import Permissions
from discord import Embed
import asyncio

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

token = utils.read_json("./jsons/config", "token")
intents = discord.Intents.all()
intents.members = True


bot = commands.AutoShardedBot(command_prefix=utils.get_prefix, case_insensitive=True, intents=intents, help_command=None, shard_count = 0, owner_ids={843641951005442058, 852285257088892928, 815203787253350436, 815078386287771728})

class Audits:
    audits = [
        "ban-audit",
        "unban-audit",
        "kick-audit",
        "channel-create-audit",
        "channel-delete-audit",
        "role-create-audit",
        "role-delete-audit",
        "webhook-create-audit",
        "webhook-delete-audit",
        "emoji-create-audit",
        "emoji-delete-audit",
        "widget-create-audit",
        "widget-delete-audit",
        "integration-create-audit",
        "integration-delete-audit"
    ]


@bot.listen("on_connect")
async def status():
    utils.setup(bot)
    print(len(bot.commands))
    print(f"{bot.user} is ready!")
    await utils.status_task(bot)

@bot.listen("on_ready")
async def ready():
    guilds = []
    for item in db.find():
        guilds.append(item['guild_id'])
    for guild in bot.guilds:
        if guild.id not in guilds:
            try:
                await utils.create_guild(guild)
                print(f"{guild} Added to database.")

            except:
                print(f"Couldn't add {guild} to databse.")
                
            
    await clear.start()

@bot.listen("on_guild_join")
async def load_db(guild : discord.Guild):
    guilds = []
    for item in db.find():
        guilds.append(item['guild_id'])
    if guild.id not in guilds:
        await utils.create_guild(guild)


@bot.listen("on_guild_remove")
async def delete_db(guild : discord.Guild):
    utils.delete_guild(guild)

@bot.command()
@commands.cooldown(1, 100, BucketType.guild)
async def setup(ctx):
    check = utils.is_guild_owner(ctx.guild, ctx.author)
    if check is not True:
        embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
        embed.timestamp = ctx.message.created_at
        return await ctx.send(embed=embed)

    first_embed = Embed(colour=0x5865f2,title='Springs Setup Will Begin in 3 Seconds')
    second_embed = Embed(colour=0x5865f2,title='Springs Setup Menu', description="<:RightArrow:852618991922053120> Creating the logging channel")
    third_embed = Embed(colour=0x5865f2,title='Springs Setup Menu', description='<:Check:855128805056184321> Creating the logging channel\n <:Check:855128805056184321> Created the logging channel')
    fourth_embed = Embed(colour=0x5865f2,title='Springs Setup Menu', description='<:Check:855128805056184321> Creating the logging channel\n <:Check:855128805056184321> Created the logging channel\n<:RightArrow:852618991922053120> Creating the Muted role ')
    fifth_embed = Embed(colour=0x5865f2,title='Springs Setup Menu', description='<:Check:855128805056184321> Creating the logging channel\n<:Check:855128805056184321> Created the logging channel\n<:Check:855128805056184321> Creating the Muted role\n<:Check:855128805056184321> Created the Muted role')
    sixth_embed = Embed(colour=0x5865f2,title='Springs Setup Menu', description='<:Check:855128805056184321> Creating the logging channel\n<:Check:855128805056184321> Created the logging channel\n<:Check:855128805056184321> Creating the Muted role\n<:Check:855128805056184321> Created the Muted role\n<:RightArrow:852618991922053120> Configuring settings')
    seventh_embed = Embed(colour=0x5865f2,title='Springs Setup Menu', description='<:Check:855128805056184321> Creating the logging channel\n<:Check:855128805056184321> Created the logging channel\n<:Check:855128805056184321> Creating the Muted role\n<:Check:855128805056184321> Created the Muted role\n<:Check:855128805056184321> Setting up settings\n <:Check:855128805056184321> Configured settings')
    eighth_embed = Embed(colour=0x5865f2,title='Springs Setup Menu', description=f'<:Check:855128805056184321> Creating the logging channel\n<:Check:855128805056184321> Created the logging channel\n<:Check:855128805056184321> Creating the Muted role\n<:Check:855128805056184321> Created the Muted role\n<:Check:855128805056184321> Setting up settings\n <:Check:855128805056184321> Configured settings\n Thank you for following the Springs setup process, for more info on me use `{utils.find_data(ctx.guild, "prefix")}help`')
    guild = ctx.guild

    # send a first message with an embed

    msg = await ctx.send(embed=first_embed)
    await asyncio.sleep(3)
    await msg.edit(embed=second_embed)
    channel = discord.utils.get(guild.channels, name="springs-logs")
    if not channel:
        channel = await ctx.guild.create_text_channel('springs-logs')
        utils.set_data("$set", ctx.guild, "log-channel", channel.id)
    else:
        pass
    await channel.set_permissions(guild.default_role, send_messages=False, read_messages=False)
    await channel.send(embed=utils.create_embed("This channel has been set as the default logging channel for Springs."))
    await asyncio.sleep(1)
    await msg.edit(embed=third_embed)
    await asyncio.sleep(3)
    await msg.edit(embed=fourth_embed)
    muted = discord.utils.get(guild.roles, name="Muted")
    if not muted:
        muted = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=True, connect=False)
    else:
        pass
    await asyncio.sleep(1)
    await msg.edit(embed=fifth_embed)
    await asyncio.sleep(3)
    await msg.edit(embed=sixth_embed)
    await asyncio.sleep(1)
    await msg.edit(embed=seventh_embed)
    await asyncio.sleep(1)
    await msg.edit(embed=eighth_embed)
    roles = await guild.fetch_roles()
    self_role = guild.self_role
    if self_role != roles[-1]:
        return await ctx.send(embed=utils.create_embed(text="Please move my role to the highest position for maximum protection."))



    
@tasks.loop(minutes=1)
async def clear():
    guilds = []
    for item in db.find():
        guilds.append(item['guild_id'])

    for guild in bot.guilds:
        if guild not in guilds:
            pass
        else:
            for arg in Audits.audits:
                utils.clear(guild, arg)



if __name__ == "__main__":
    bot.run(token, reconnect=True)