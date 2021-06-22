import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import MemberConverter, RoleConverter, UserConverter, GuildConverter, Cog, has_permissions, Greedy
from colorama import Fore 
import json
import datetime
from utils.utils import utils
import asyncio
import time
from discord.ext.commands.converter import TextChannelConverter
from discord.ext.commands.cooldowns import BucketType
import giphy_client
import random
import libneko 
from libneko import pag
import asyncio
import platform
from utils.utils import utils
import random
import time
import discord
from discord.ext import commands
from datetime import datetime, timedelta
from platform import python_version
from time import time
import time
from discord import Activity, ActivityType, Embed
from discord import __version__ as discord_version
from discord.ext.commands import Cog
from discord.ext.commands import command
from psutil import Process, virtual_memory
import psutil
import discord
import asyncio
from discord.ext import commands
import time
import random
import math
import psutil
import datetime
from datetime import datetime, timedelta
import urllib
from urllib.request import Request, urlopen
import json
import traceback
import sys
import re

import os
import requests




class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.version = "1.0.1"

    
    @commands.command(aliases=['role-info'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def roleinfo(self, ctx, role: RoleConverter):
        guild = ctx.guild
        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = f"{role_created} ({since_created} days ago)"
        users = len([x for x in guild.members if role in x.roles])

        embed = discord.Embed(title=f"{role}'s information.", timestamp=ctx.message.created_at)
        embed.description = f"**Role Name:** - `{role.name}`\n **Role ID:** - `{role.id}`\n **Users with role:** - `{users}`\n **Mentionable** - `{role.mentionable}`\n **Hoisted** - `{role.hoist}`\n **Position** - `{role.position}`\n **Managed** - `{role.managed}`\n **Color** - `{role.color}`\n **Created At** - `{created_on}`"
        embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by: {ctx.author}")
        embed.color = role.color
        await ctx.send(embed=embed)

    @roleinfo.error
    async def roleinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="<a:no:849069815019995136> *You must select an role to get info from.*", color=discord.Color.red())
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    @commands.command(aliases=['channel-info', 'channelstats'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def channelinfo(self, ctx, channel: TextChannelConverter=None):
        channel = ctx.channel if not channel else channel
        users = len(channel.members)
        embed = Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f'Info for {channel.name}', icon_url=ctx.guild.icon_url)
        embed.description = f"**Channel ID:** - `{channel.id}`\n **Category:** - `{channel.category}`\n **Category Id:** - `{channel.category_id}`\n **Channel Topic:** - `{channel.topic}`\n**Channel Position:** - `{channel.position}`\n **Channel Users** - `{users}`\n **Slowmode** - `{channel.slowmode_delay}`\n **Type** - `{channel.type}`\n **Topic** - `{channel.topic}`\n **Created At** - `{channel.created_at}`"
#       embed.set_author(name=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by: {ctx.author}")
        embed.color = 0x5865f2
        await ctx.send(embed=embed)
    

 
    @commands.command(aliases=['emoji-info'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def emojiinfo(self, ctx, emoji : commands.EmojiConverter):
        try:
            emoji = await emoji.guild.fetch_emoji(emoji.id)
        except:
            return await ctx.send("Emoji not found.")
        embed = Embed(timestamp=ctx.message.created_at)
        embed.set_author(name=f'Info for {emoji.name}', icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by: {ctx.author}")
        embed.color = 0x5865f2
        is_managed = "Yes" if emoji.managed else "No"
        is_animated = "Yes" if emoji.animated else "No"
        requires_colons = "Yes" if emoji.require_colons else "No"
        creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
        can_use_emoji = (
            "Everyone"
            if not emoji.roles
            else " ".join(role.name for role in emoji.roles)
        )

        embed.description = f"**- Name:** - `{emoji.name}`\n **- Id:**  - `{emoji.id}`\n **- URL:** - [Link To Emoji]({emoji.url})\n **- Author:** - {emoji.user.mention}\n **- Time Created:** - `{creation_time}`\n **- Usable by:** - `{can_use_emoji}`\n **- Animated:** - `{is_animated}`\n **- Managed:** - `{is_managed}`\n **- Requires Colons:** - `{requires_colons}`\n **- Guild Name:** - `{emoji.guild.name}`\n  **- Guild Id:** - `{emoji.guild.id}`"

        await ctx.send(embed=embed)

    @emojiinfo.error
    async def emojiinfo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="<a:no:849069815019995136> *You must select an emoji to get info from.*", color=discord.Color.red())
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['user-info', 'whoami'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def whois(self, ctx, user: commands.MemberConverter = None):
        user = ctx.author if not user else user  
        embed = discord.Embed(timestamp=datetime.datetime.utcnow())
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="**Username:**", value=user, inline=True)
        embed.add_field(name="**ID:**", value=user.id, inline=True)
        embed.add_field(name="**Status:**", value=user.status, inline=True)
        embed.add_field(name="**Highest Role:**", value=user.top_role)
        embed.add_field(name="**Bot?:**", value=user.bot)

        userMade = user.created_at
        userMade2 = userMade.strftime("%B %d, %Y %I:%M %p")
        embed.add_field(name="**Registered:**", value="{}".format(userMade2))

        userJoin = user.joined_at
        userJoin2 = userJoin.strftime("%B %d, %Y %I:%M %p")
        embed.add_field(name="**Joined:**", value="{}".format(userJoin2))

        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name=f"**Roles [{len(user.roles)-1}]**", value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="**Key permissions:**", value=perm_string, inline=False)

        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.color = 0x5865f2
        await ctx.send(embed=embed)

    @commands.command(aliases=['av','pfp'],help="Shows the avatar of you or the person you mention.")
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def avatar(self, ctx, member: commands.MemberConverter = None):
        member = ctx.author if not member else member
        embed = discord.Embed(title =f"{member.name}'s avatar", url=member.avatar_url, timestamp = ctx.message.created_at)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Requested by : {ctx.author}",icon_url=ctx.author.avatar_url)
        embed.color = 0x5865f2
        await ctx.send(embed=embed)
    

    @commands.command(aliases=['guildinfo', 'si', 'gi', 'server-info'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def serverinfo(self, ctx):
        date_format = "%a, %d %b %Y"
        boosts = ctx.guild.premium_subscription_count
        embed = discord.Embed(title=f"{ctx.guild.name}'s info", url = ctx.guild.icon_url, timstamp=datetime.datetime.utcnow())
        embed.add_field(name='**Owner:**', value=f"{ctx.guild.owner}", inline=False)
        embed.add_field(name='**Region:**', value=f"{ctx.guild.region}", inline=False)
        embed.add_field(name='**Member Count:**', value=f"{ctx.guild.member_count}", inline=False)
        embed.add_field(name='**Creation Date:**', value=f"{ctx.guild.created_at.strftime(date_format)}", inline=False)
        embed.add_field(name='**Roles:**', value=f"{len(ctx.guild.roles)-1}",     inline=False)
        embed.add_field(name='**Text Channels:**', value=f"{len(ctx.guild.text_channels)}",     inline=False)
        embed.add_field(name='**Voice Channels:**', value=f"{len(ctx.guild.voice_channels)}",     inline=False)
        embed.add_field(name='**Boosts:**', value=f"{boosts}", inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.color = 0x5865f2
        await ctx.send(embed=embed)

    @commands.command(aliases=['guild-banner', 'server-banner'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def serverbanner(self, ctx):
        icon_url = ctx.guild.banner_url 
        if len(icon_url) == 0:
            return await ctx.send("This guild has no server banner.")
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f"{ctx.guild.name}'s Banner"
        )
        embed.set_image(url=icon_url)
        embed.set_footer(text=f"Requested by: {ctx.author}", url=ctx.author.avatar_url)
        embed.color = 0x5865f2

        await ctx.send(embed=embed)
    
    @commands.command(aliases=['server-av', 'server-icon'])
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def serverpfp(self, ctx):
        icon_url = ctx.guild.icon_url
        if len(icon_url) == 0:
            return await ctx.send("This guild has no server icon.")
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title=f"{ctx.guild.name}'s Icon", url = icon_url)
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.color = 0x5865f2
        await ctx.send(embed=embed)
    

    @commands.command(aliases=["banlist"])
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def bans(self, ctx):
            try:
                bans = await ctx.guild.bans()
                if len(bans) == 0:
                    return await ctx.send("This server has no banned users.")
            except:
                return await ctx.send("Couldn't fetch guild bans.")

            banned = ""

            @pag.embed_generator(max_chars=2048)
            def get_embed(paginator, page, page_index):
                em = discord.Embed(title = f"{ctx.guild.name}'s Ban List':", description=page, timestamp=datetime.datetime.utcnow())
                em.set_footer(text=f"{len(bans)} Members in Total.")
                em.color = 0x5865f2
                return em

            page = pag.EmbedNavigatorFactory(factory=get_embed)

            for ban_entry in bans:
                banned += f"{ban_entry.user.mention} - `{ban_entry.reason}`\n"

            page += banned
            page.start(ctx)
    

    
    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket and API latency."""

        process = psutil.Process(os.getpid())
        proc_memory = process.memory_info().rss
        total_memory = psutil.virtual_memory().total
        all_memory = str(round(total_memory/1073741824, 2)) + "GiB"
        process_memory = str(round(proc_memory/1073741824, 2)) + "GiB" if round(proc_memory/1048576) > 1024 else str(round(proc_memory/1048576)) + "MiB"
        mem_total = virtual_memory().total / (1024**2)
        start_time = time.time()
        end_time = time.time()
        pie = format(round((proc_memory/total_memory)*100, 1))


        embed = discord.Embed(
            title=f"<:Rocket:852618786716647464> Shard [1]",
            colour=0x5865f2,
        )

        embed.add_field(name="<:Connection:854518606180122664> **Latency**", value=f"`{round(self.bot.latency * 1000)}ms`",inline=False)
        embed.add_field(name="<:Cpu:854516106127605821> **CPU Usage**", value="`{}%`".format(psutil.cpu_percent()),inline=False)
        embed.add_field(name="<:Memory:854516040025112597> **Memory Usage**", value="`{}%`".format(round((proc_memory/total_memory)*100, 1)),inline=False)


        await ctx.send(embed=embed)

    @commands.command(aliases=['members'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def membercount(self, ctx):
        embed = discord.Embed(title=f"Members", timestamp=ctx.message.created_at, description=ctx.guild.member_count)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.color = 0x5865f2
        await ctx.send(embed=embed)


    @commands.command(aliases=['bot-info', 'info'])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def stats(self, ctx):
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1    

        embed = discord.Embed(
            title=f"{self.bot.user.name} Bot Stats",
            timestamp=ctx.message.created_at,
        )
        embed.add_field(name="Developers:", value="> <@843641951005442058> & <@852285257088892928> & <@815203787253350436> & <@815078386287771728>", inline=False)
        embed.add_field(name="Version:", value=f'> {self.bot.version}', inline=False)
        embed.add_field(name="Users:", value=f'> {(members)}', inline=False)
        embed.add_field(name="Guilds:", value=f'> {len(self.bot.guilds)}', inline=False)

        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.color = 0x5865f2

        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Info(bot))