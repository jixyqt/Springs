import discord
from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType
from utils.utils import utils, bot_id
import datetime
import asyncio

class Messaging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    discord.Guild.get_member
    @commands.Cog.listener("on_message")
    async def spam_check(self, message):
        if message.guild:
            user = message.guild.get_member(message.author.id)
            limit = utils.find_data(message.guild, "anti-spam-limit")
            punishment = utils.find_data(message.guild, "anti-spam-punishment")
            whitelisted = utils.find_data(message.guild, "whitelist-users")
            whitelist_roles = utils.find_data(message.guild, "whitelist-roles")
            logtoggle = utils.find_data(message.guild, "mod-logging")
            if logtoggle is True:
                channelID = utils.find_data(message.guild, "log-channel")
                logchannel = self.bot.get_channel(id=channelID)
            else:
                pass

            toggle = utils.find_data(message.guild, "anti-spam")
            if toggle is True:
                if message.author.bot or message.author.id == bot_id:
                    pass
                if user.id in whitelisted or user.guild_permissions.administrator or user.guild_permissions.manage_messages or user.guild_permissions.manage_guild:
                    pass
                if user in message.guild.members:
                    for role in user.roles:
                        if role.id in whitelist_roles:
                            pass

                utils.upsert_data(message.guild, "spam-audit", user.id)

                counter = 0
                data = utils.find_data(message.guild)
                for userID in data['spam-audit']:
                    if userID == user.id:
                        counter += 1
                       
                else:
                    if counter == limit:
                        if punishment == 'kick':
                            async for msg in message.channel.history(limit=limit):
                                if msg.author.id == message.author.id:
                                    await msg.delete()

                            await message.guild.kick(user, reason='Springs Moderation | Spamming Messages')
                            
                            if logtoggle is True:
                                if logchannel is None:
                                    pass
                                embed = utils.format_modlogs(user=user, reason="Spamming Messages", action="kicked")
                                await logchannel.send(embed=embed)

                            pass

                        if punishment == 'ban':
                            async for msg in message.channel.history(limit=limit):
                                if msg.author.id == message.author.id:
                                    await msg.delete()
                            await message.guild.ban(user, reason='Springs Moderation | Spamming Messages')
                            
                            if logtoggle is True:
                                if logchannel is None:
                                    pass
                                embed = utils.format_modlogs(user=user, reason="Spamming Messages", action="banned")
                                await logchannel.send(embed=embed)

                            pass

                        if punishment == 'mute':
                            async for msg in message.channel.history(limit=limit):
                                if msg.author.id == message.author.id:
                                    await msg.delete()
                            await utils.mute(guild=message.guild, member=user, reason='Springs Moderation | Spamming Messages')
                            
                            if logtoggle is True:
                                if logchannel is None:
                                    pass
                                embed = utils.format_modlogs(user=user, reason="Spamming Messages", action="muted")
                                await logchannel.send(embed=embed)
                            await message.channel.send(embed=embed)
                            await asyncio.sleep(60)
                            muted = discord.utils.get(message.guild.roles, name="Muted")
                            await user.remove_roles(muted, reason="Time Up")

                            pass
                        else:
                            embed = utils.format_modlogs(user=user, reason="Sending Invites", action="muted")
                            await message.channel.send(embed=embed)
                            await asyncio.sleep(60)
                            muted = discord.utils.get(message.guild.roles, name="Muted")
                            await user.remove_roles(muted, reason="Time Up")
                            pass
            else:
                pass

    @commands.Cog.listener("on_message")
    async def link_check(self, message):
        if message.guild and ('https://' in message.content or 'discord.gg' in message.content):
            user = message.author
            punishment = utils.find_data(message.guild, "anti-link-punishment")
            whitelisted = utils.find_data(message.guild, "whitelist-users")
            whitelist_roles = utils.find_data(message.guild, "whitelist-roles")
            whitelist_link_channels = utils.find_data(message.guild, "whitelist-link-channels")
            logtoggle = utils.find_data(message.guild, "mod-logging")
            if logtoggle is True:
                channelID = utils.find_data(message.guild, "log-channel")
                logchannel = self.bot.get_channel(id=channelID)
            else:
                pass

            
            toggle = utils.find_data(message.guild, "anti-link")
            if toggle is True:
                if message.channel.id in whitelist_link_channels:
                    pass
                if message.author.bot or message.author.id == bot_id:
                    pass
                if user.id in whitelisted or user.guild_permissions.administrator or user.guild_permissions.manage_messages or user.guild_permissions.manage_guild:
                    pass
                if user in message.guild.members:
                    for role in user.roles:
                        if role.id in whitelist_roles:
                            pass
                else:
                    if punishment == 'kick':
                        await message.delete()
                        await message.channel.send("⛔ Links aren't allowed here.")
                        await message.guild.kick(user, reason='Springs Moderation | Sending Links')
                        if logtoggle is True:
                            if logchannel is None:
                                pass
                            embed = utils.format_modlogs(user=user, reason="Sending Links", action="kicked")
                            await logchannel.send(embed=embed)
                            pass


                    if punishment == 'ban':
                        await message.delete()
                        await message.channel.send("⛔ Links aren't allowed here.")
                        await message.guild.ban(user, reason='Springs Moderation | Sending Links')
                        if logtoggle is True:
                            if logchannel is None:
                                pass
                            embed = utils.format_modlogs(user=user, reason="Sending Links", action="banned")
                            await logchannel.send(embed=embed)
                            pass

                    if punishment == 'mute':
                        await message.delete()
                        await message.channel.send("⛔ Links aren't allowed here.")
                        await utils.mute(guild=message.guild, member=user, reason='Springs Moderation | Sending Links')
                        if logtoggle is True:
                            if logchannel is None:
                                pass
                            embed = utils.format_modlogs(user=user, reason="Sending Links", action="muted")
                            await logchannel.send(embed=embed)
                            await message.channel.send(embed=embed)
                            await asyncio.sleep(60)
                            muted = discord.utils.get(message.guild.roles, name="Muted")
                            await user.remove_roles(muted, reason="Time Up")
                            pass
                        else:
                            embed = utils.format_modlogs(user=user, reason="Sending Invites", action="muted")
                            await message.channel.send(embed=embed)
                            await asyncio.sleep(60)
                            muted = discord.utils.get(message.guild.roles, name="Muted")
                            await user.remove_roles(muted, reason="Time Up")
                            pass
            else:
                pass

    discord.Member.guild_permissions
    @commands.Cog.listener("on_message")
    async def invite_check(self, message):
        if message.guild and 'discord.gg' in message.content:
            user = message.author
            punishment = utils.find_data(message.guild, "anti-invite-punishment")
            whitelisted = utils.find_data(message.guild, "whitelist-users")
            whitelist_roles = utils.find_data(message.guild, "whitelist-roles")
            whitelist_invite_channels = utils.find_data(message.guild, "whitelist-invite-channels")
            logtoggle = utils.find_data(message.guild, "mod-logging")
            if logtoggle is True:
                channelID = utils.find_data(message.guild, "log-channel")
                logchannel = self.bot.get_channel(id=channelID)
            else:
                pass
            
            toggle = utils.find_data(message.guild, "anti-invite")
            if toggle is True:
                if message.channel.id in whitelist_invite_channels:
                    pass
                if message.author.bot or message.author.id == bot_id:
                    pass
                if user.id in whitelisted or user.guild_permissions.administrator or user.guild_permissions.manage_messages or user.guild_permissions.manage_guild:
                    pass
                if user in message.guild.members:
                    for role in user.roles:
                        if role.id in whitelist_roles:
                            pass

                else:
                    if punishment == 'kick':
                        await message.delete()
                        await message.channel.send("⛔ Invites aren't allowed here.")
                        await message.guild.kick(user, reason='Springs Moderation | Sending invites')
                        if logtoggle is True:
                            if logchannel is None:
                                pass
                            embed = utils.format_modlogs(user=user, reason="Sending invites", action="kicked")
                            await logchannel.send(embed=embed)
                            pass


                    if punishment == 'ban':
                        await message.delete()
                        await message.channel.send("⛔ Invites aren't allowed here.")
                        await message.guild.ban(user, reason='Springs Moderation | Sending invites')
                        if logtoggle is True:
                            if logchannel is None:
                                pass
                            embed = utils.format_modlogs(user=user, reason="Sending Links", action="banned")
                            await logchannel.send(embed=embed)
                            pass

                    if punishment == 'mute':
                        await message.delete()
                        await message.channel.send("⛔ Invites aren't allowed here.")
                        await utils.mute(guild=message.guild, member=user, reason='Springs Moderation | Sending Invites')
                        if logtoggle is True:
                            if logchannel is None:
                                pass
                            embed = utils.format_modlogs(user=user, reason="Sending Invites", action="muted")
                            await logchannel.send(embed=embed)
                            await message.channel.send(embed=embed)
                            await asyncio.sleep(60)
                            muted = discord.utils.get(message.guild.roles, name="Muted")
                            await user.remove_roles(muted, reason="Time Up")
                            pass
                        else:
                            embed = utils.format_modlogs(user=user, reason="Sending Invites", action="muted")
                            await message.channel.send(embed=embed)
                            await asyncio.sleep(60)
                            muted = discord.utils.get(message.guild.roles, name="Muted")
                            await user.remove_roles(muted, reason="Time Up")
                            pass
            else:
                pass


    @tasks.loop(seconds=1.5)
    async def clear_spam(self):
        for guild in self.bot.guilds:
            utils.clear(guild, "spam-audit")

    @commands.Cog.listener("on_ready")
    async def clearspam(self):
        await self.clear_spam.start()

    @commands.command(aliases=['bl-word', 'banword', 'ban-word', 'blacklist-word', 'blword'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, BucketType.user)
    async def blacklistword(self, ctx, word):
        if word in utils.find_data(ctx.guild, "blacklist-words"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry **{word}** is already on the blacklist words list", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "blacklist-words", word)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully added **{word}** to the blacklist words list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['unbl-word', 'unbanword', 'unban-word', 'unblacklist-word', 'unblword'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, BucketType.user)
    async def unblacklistword(self, ctx, word):
        if word not in utils.find_data(ctx.guild, "blacklist-words"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry **{word}** is not on the blacklist words list", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "blacklist-words", word)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully removed **{word}** from the blacklist words list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['clear-blacklist-words', 'clear-bl-words', 'clearblwords', 'clearbannedwords'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, BucketType.user)
    async def clearblacklistwords(self, ctx):
        utils.clear(ctx.guild, "blacklist-words")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s blacklist words", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['blacklisted-words', 'bld-words', 'bldwords', 'bannedwords', 'banned-words'])
    async def blacklistedwords(self, ctx):
        embed = discord.Embed(title=f"**__Blacklisted Words__**", color=0x5865f2, timestamp=ctx.message.created_at, description = '')
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)

        data = utils.find_data(ctx.guild)
        for word in data['blacklist-words']:
            embed.description += (f"🧾 | Word: **{word}**\n")
        
        await ctx.send(embed=embed)

    @commands.Cog.listener("on_message")
    async def banned_word_check(self, message):
        if message.guild:
            logtoggle = utils.find_data(message.guild, "mod-logging")
            if logtoggle is True:
                channelID = utils.find_data(message.guild, "log-channel")
                logchannel = self.bot.get_channel(id=channelID)
            else:
                pass
            user = message.author
            bannedwords = utils.find_data(message.guild, "blacklist-words")
            try:
                if message.guild.id in bannedwords:
                    if len(bannedwords) == 0 or bannedwords is None or user.guild_permissions.manage_messages or user.guild_permissions.manage_guild or user.guild_permissions.administrator:
                        pass
                    else:
                        for bannedWord in bannedwords:
                            try:
                                if utils.msg_contains_word(message.content.lower(), bannedWord):
                                    await message.delete()                    
                                    embed = discord.Embed(title = "Watch your language! 😒", description = f"{message.author.mention} your message was removed as it contained a banned word.", timestamp = datetime.datetime.utcnow())
                                    embed.set_author(name = message.author.name, icon_url= message.author.avatar_url)  
                                    await message.channel.send(embed=embed, delete_after=3)
                                    await utils.mute(guild=message.guild, member=user, reason='Springs Moderation | Sending Blacklisted Word')
                                    if logtoggle is True:
                                        if logchannel is None:
                                            pass
                                        embed = utils.format_modlogs(user=user, reason="Sending Blacklisted Word", action="muted")
                                        await logchannel.send(embed=embed)
                                        pass 
                                    await self.bot.process_commands(message)
                            except KeyError:
                                pass
            except KeyError:
                pass 
        else:
            pass

    
def setup(bot):
    bot.add_cog(Messaging(bot))
    