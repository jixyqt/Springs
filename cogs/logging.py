from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import has_permissions
from utils.utils import utils, bot_id
import discord
from discord.ext import commands
import datetime


class Args:

    validargs = [
        "message-logging",
        "server-logging",
        "user-logging",
        "voice-logging",
        "mod-logging",
        "welcoming",
        "leaving",
        "boosting",
        "welcome-embed",
        "leave-embed",
        "boost-embed",
        
    ]





def author_check(message):
    if message.author.bot:
        return "bot"
    else:
        return "user"

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['set-logging', 'toggle-logging'])
    @commands.cooldown(3, 14, BucketType.user)
    async def togglelogging(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "logging", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "logging", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "logging")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "logging", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "logging", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the logging toggle.")

    @commands.command(aliases=['messagelogs', 'msglogs', 'toggle-message-logging', 'message-logging'])
    @commands.cooldown(3, 14, BucketType.user)
    async def togglemessagelogging(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "message-logging", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled message-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "message-logging", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled message-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "message-logging")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "message-logging", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled message-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "message-logging", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled message-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the message-logging toggle.")

    @commands.command(aliases=['voicelogs', 'voice-logs', 'toggle-voice-logging', 'voice-logging'])
    @commands.cooldown(3, 14, BucketType.user)
    async def togglevoicelogging(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "voice-logging", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled voice-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "voice-logging", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled voice-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "voice-logging")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "voice-logging", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled voice-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "voice-logging", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled voice-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the voice-logging toggle.")

    @commands.command(aliases=['userlogs', 'user-logs', 'toggle-user-logging', 'user-logging'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleuserlogging(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "user-logging", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled user-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "user-logging", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled user-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "user-logging")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "user-logging", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled user-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "user-logging", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled user-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the user-logging toggle.")

    @commands.command(aliases=['serverlogs', 'server-logs', 'toggle-server-logging', 'server-logging'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleserverlogging(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "server-logging", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled server-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "server-logging", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled server-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "server-logging")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "server-logging", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled server-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "server-logging", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled server-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the server-logging toggle.")

    @commands.command(aliases=['modlogs', 'mod-logs', 'toggle-mod-logging', 'toggle-mod-logs', 'mod-logging'])
    @commands.cooldown(3, 14, BucketType.user)
    async def togglemodlogging(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "mod-logging", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled mod-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "mod-logging", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled mod-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "mod-logging")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "mod-logging", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled mod-logging to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "mod-logging", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled mod-logging to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the mod-logging toggle.")

    @commands.command(aliases=['log-chan', 'log-channel'])
    @commands.cooldown(3, 14, BucketType.user)
    async def logchannel(self, ctx, channel : discord.TextChannel):
        check = utils.is_admin(ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server admins can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "log-channel", channel.id)
        tog = discord.Embed(description = f"<:Check:855128805056184321> Succesfully set log-channel for {ctx.guild} to {channel.mention}", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"The log channel has been set for {ctx.guild} to {channel.mention}", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=tog)

    @commands.command(aliases=['logs'])
    @commands.cooldown(3, 14, BucketType.user)
    async def logging(self, ctx):
        data = utils.find_data(ctx.guild)
        embed = discord.Embed(title=f"Logging", timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.description = f"**Example**: *log-channel `[channel]`*"
        if data['log-channel'] is not None:
            embed.add_field(name="**log-channel**", value=f"<#{data['log-channel']}>")
        else:
            embed.add_field(name="**log-channel**", value=f"Disabled: <a:no:849069815019995136>")

        if data['welcome-channel'] is not None:
            embed.add_field(name="**welcome-channel**", value=f"<#{data['welcome-channel']}>")
        else:
            embed.add_field(name="**welcome-channel**", value=f"Disabled: <a:no:849069815019995136>")

        if data['leave-channel'] is not None:
            embed.add_field(name="**leave-channel**", value=f"<#{data['leave-channel']}>")
        else:
            embed.add_field(name="**leave-channel**", value=f"Disabled: <a:no:849069815019995136>")
        
        if data['boost-channel'] is not None:
            embed.add_field(name="**boost-channel**", value=f"<#{data['boost-channel']}>")
        else:
            embed.add_field(name="**boost-channel**", value=f"Disabled: <a:no:849069815019995136>")

        if data['boost-message'] is not None:
            embed.add_field(name="**boost-message**", value=f"`{data['boost-message']}`")
        else:
            embed.add_field(name="**boost-message**", value=f"Disabled: <a:no:849069815019995136>")

        if data['welcome-message'] is not None:
            embed.add_field(name="**welcome-message**", value=f"`{data['welcome-message']}`")
        else:
            embed.add_field(name="**welcome-message**", value=f"Disabled: <a:no:849069815019995136>")

        if data['leave-message'] is not None:
            embed.add_field(name="**leave-message**", value=f"`{data['leave-message']}`")
        else:
            embed.add_field(name="**leave-message**", value=f"Disabled: <a:no:849069815019995136>")

        embed.set_footer(text=f"Requested by: {ctx.author}")
        embed.color = 0x5865f2

        for value in Args.validargs:
            if data[value] is True:
                embed.add_field(name=f"**{value}**", value="Enabled: <:yes:849069962014228490>\n")
            elif data[value] is False or data[value] is None:
                embed.add_field(name=f"**{value}**", value=f"Disabled: <a:no:849069815019995136>\n")
            else:
                pass
        
        await ctx.send(embed=embed)

    @commands.Cog.listener("on_message_delete")
    async def message_delete_logs(self, message):
        if message.guild:
            botbool = author_check(message)
            messagelogs = utils.has_messagelogs(message.guild)
            if messagelogs is True:
                    logchannel = self.bot.get_channel(id=utils.find_data(message.guild, "log-channel"))
                    embed = discord.Embed(title = f"Message Deleted:", timestamp =message.created_at)
                    embed.set_author(name=message.guild.name, icon_url=message.guild.icon_url)
                    embed.add_field(name='**Author**:', value=message.author.mention, inline=False)
                    embed.add_field(name = '**Content**:', value=message.content, inline=False)
                    embed.add_field(name='**Guild**:', value=message.guild, inline=False)
                    embed.add_field(name='**Channel**:', value=message.channel, inline=False)
                    embed.add_field(name='**User/Type**:', value=botbool, inline=False)
                    embed.add_field(name='**Time**:', value=message.created_at, inline=False)
                    embed.set_thumbnail(url = message.guild.icon_url)
                    embed.set_footer(text=f"Written by {message.author}", icon_url=message.author.avatar_url)
                    embed.color = 0x5865f2

                    try:
                        await logchannel.send(embed=embed)
                    except:
                        pass
        else:
            pass

    @commands.Cog.listener("on_message_edit")
    async def message_edit_logs(self, before, after):
        if before.guild:
            if before.author.bot:
                return
            botbool = author_check(before)
            messagelogs = utils.has_messagelogs(before.guild)
            if messagelogs is True:
                    logchannel = self.bot.get_channel(id=utils.find_data(before.guild, "log-channel"))
                    embed = discord.Embed(title = f"Message Edited:", timestamp =before.created_at)
                    embed.set_author(name=before.guild.name, icon_url=before.guild.icon_url)
                    embed.add_field(name='**Author**:', value=before.author.mention, inline=False)
                    embed.add_field(name = '**Content**:', value=f"{before.content}", inline=False)
                    embed.add_field(name = '**Edited Content**:', value=f"{after.content}", inline=False)
                    embed.add_field(name='**Guild**:', value=before.guild, inline=False)
                    embed.add_field(name='**Channel**:', value=before.channel, inline=False)
                    embed.add_field(name='**User/Type**:', value=botbool, inline=False)
                    embed.add_field(name='**Time**:', value=before.created_at, inline=False)
                    embed.set_thumbnail(url = before.guild.icon_url)
                    embed.set_footer(text=f"Written by {before.author}", icon_url=before.author.avatar_url)
                    embed.color = 0x5865f2

                    try:
                        
                        await logchannel.send(embed=embed)
                    except:
                        pass
        else:
            pass

    @commands.Cog.listener("on_voice_state_update")
    async def voice_disconnect_logs(self, member, before, after):
        voicelogs = utils.has_voicelogs(member.guild)
        if before.channel is not None and after.channel is None:
            if voicelogs is True:
                async for i in member.guild.audit_logs(limit=1, action=discord.AuditLogAction.member_disconnect):
                    embed = discord.Embed(title = f"Member Disconnected:", timestamp =datetime.datetime.utcnow())
                    embed.add_field(name='**Guild**:', value=member.guild, inline=False)
                    embed.add_field(name='**Channel**:', value=before.channel, inline=False)
                    embed.add_field(name='**Time**:', value=datetime.datetime.utcnow(), inline=False)
                    embed.set_author(name=member.name, icon_url=member.avatar_url)
                    embed.set_footer(text=f"Disconnected by {i.user}", icon_url=i.user.avatar_url)
                    embed.set_thumbnail(url =member.guild.icon_url)
                    embed.color = 0x5865f2
                    logchannel = self.bot.get_channel(id=utils.find_data(member.guild, "log-channel"))
                    try:
                        await logchannel.send(embed=embed)
                    except:
                        pass
            else:
                pass
        else:
            pass

    @commands.Cog.listener("on_voice_state_update")
    async def voice_connect_logs(self, member, before, after):
        voicelogs = utils.has_voicelogs(member.guild)
        if before.channel is None and after.channel is not None:
            if voicelogs is True:
                if before.deaf:
                    return
                else:
                    embed = discord.Embed(title = f"Member Connected:", timestamp =datetime.datetime.utcnow())
                    embed.add_field(name='**Guild**:', value=member.guild, inline=False)
                    embed.add_field(name='**Channel**:', value=after.channel, inline=False)
                    embed.add_field(name='**Time**:', value=datetime.datetime.utcnow(), inline=False)
                    embed.set_author(name=member.name, icon_url=member.avatar_url)
                    embed.set_thumbnail(url =member.guild.icon_url)
                    embed.color = 0x5865f2
                    logchannel = self.bot.get_channel(id=utils.find_data(member.guild, "log-channel"))
                    try:
                        await logchannel.send(embed=embed)
                    except:
                        pass
            else:
                pass
        else:
            pass

    @commands.Cog.listener("on_voice_state_update")
    async def voice_move_logs(self, member, before, after):
        voicelogs = utils.has_voicelogs(member.guild)
        if before.channel is None and after.channel is None:
            return
        
        if before.channel == after.channel:
            return
        
        if before.channel is not None and after.channel is not None:
            if voicelogs is True:
                embed = discord.Embed(title = f"Member Moved:", timestamp =datetime.datetime.utcnow())
                embed.add_field(name='**Guild**:', value=member.guild, inline=False)
                embed.add_field(name='**Channel From**:', value=before.channel, inline=False)
                embed.add_field(name='**Channel To:**:', value=after.channel, inline=False)
                embed.add_field(name='**Time**:', value=datetime.datetime.utcnow(), inline=False)
                embed.set_author(name=member.name, icon_url=member.avatar_url)
                embed.set_thumbnail(url =member.guild.icon_url)
                embed.color = 0x5865f2
                logchannel = self.bot.get_channel(id=utils.find_data(member.guild, "log-channel"))
                try:
                    await logchannel.send(embed=embed)
                except:
                    pass
        else:
            return

    @commands.Cog.listener("on_member_update")
    async def member_update_logs(self, before, after):
        if before == self.bot.user or after == self.bot.user:
            return
        if before.id == bot_id or after.id == bot_id:
            return
        if before.bot or after.bot:
            return
        userlogs = utils.has_userlogs(before.guild)
        if userlogs is True:
            logchannel = self.bot.get_channel(id=utils.find_data(before.guild, "log-channel"))
            if before.status != after.status:
                embed = discord.Embed(title = f"Status Updated:", timestamp =datetime.datetime.utcnow())
                embed.add_field(name="**Member**", value=before.mention, inline=False)
                embed.add_field(name="**Before**", value = f"`{before.status}`", inline=False)
                embed.add_field(name="**After**", value = f"`{after.status}`", inline=False)
                embed.color=0x5865f2
                embed.set_thumbnail(url=after.avatar_url)
                if logchannel is not None:
                    await logchannel.send(embed=embed)

            if before.activity != after.activity:
                embed = discord.Embed(title = f"Activity Updated:", timestamp=datetime.datetime.utcnow())
                embed.add_field(name="**Member**", value=before.mention, inline=False)
                embed.add_field(name="**Before**", value = f"Type: `{before.activity.type if before.activity != None else None}`\n Name: `{before.activity.name if before.activity != None else None}`", inline=False)
                embed.add_field(name="**After**", value = f"Type: `{after.activity.type if after.activity != None else None}`\n Name: `{after.activity.name if after.activity != None else None}`", inline=False)
                embed.color=0x5865f2
                embed.set_thumbnail(url=after.avatar_url)
                if logchannel is not None:
                    await logchannel.send(embed=embed)
            
            if len(before.roles) != len(after.roles):
                embed = discord.Embed(title= f"Roles Updated:", timestamp=datetime.datetime.utcnow())
                embed.add_field(name="**Member**", value=before.mention, inline=False)
                if len(before.roles) > 1:
                    role_string = ' '.join([r.mention for r in before.roles][1:])
                    embed.add_field(name=f"**Roles Before [{len(before.roles)-1}]**", value=role_string, inline=False)
                    embed.color=0x5865f2
                if len(after.roles) > 1:
                    role_string = ' '.join([r.mention for r in after.roles][1:])
                    embed.add_field(name=f"**Roles After [{len(after.roles)-1}]**", value=role_string, inline=False)
                    embed.color=0x5865f2
                if logchannel is not None:
                    await logchannel.send(embed=embed)

            if before.display_name != after.display_name:
                embed = discord.Embed(title = f"Nickname Updated", timestamp=datetime.datetime.utcnow())
                embed.add_field(name="**Member**", value=before.mention, inline=False)
                embed.add_field(name="**Before**", value=before.display_name)
                embed.add_field(name="**After**", value=after.display_name)
                embed.color=0x5865f2
                if logchannel is not None:
                    await logchannel.send(embed=embed)
        else:
            return

    @commands.Cog.listener("on_user_update")
    async def user_update_logs(self, before, after):
        if before == self.bot.user or after == self.bot.user:
            return
        if before.id == bot_id or after.id == bot_id:
            return
        if before.bot or after.bot:
            return
        for guild in before.mutual_guilds:
            userlogs = utils.has_userlogs(guild)
            if userlogs is True:
                logchannel = self.bot.get_channel(id=utils.find_data(guild, "log-channel"))
                if before.avatar != after.avatar:
                    embed = discord.Embed(title="Avatar Updated:", timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="**User**", value=before.mention, inline=False)
                    embed.add_field(name="**After**", value=before.avatar)
                    embed.set_thumbnail(url=after.avatar_url)
                    embed.set_author(name=before.avatar, icon_url=before.avatar_url)
                    embed.color=0x5865f2
                    if logchannel is not None:
                        await logchannel.send(embed=embed)

                if before.name != after.name:
                    embed = discord.Embed(title="Username Updated:", timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="**User**", value=before.mention, inline=False)
                    embed.add_field(name="**Before**", value=before.name)
                    embed.add_field(name="**After**", value=after.name)
                    embed.set_thumbnail(url=after.avatar_url)
                    embed.color=0x5865f2
                    if logchannel is not None:
                        await logchannel.send(embed=embed)
                    
                if before.discriminator != after.discriminator:
                    embed = discord.Embed(title="Discriminator Updated:", timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="**User**", value=before.mention, inline=False)
                    embed.add_field(name="**Before**", value=before.discriminator)
                    embed.add_field(name="**After**", value=after.discriminator)
                    embed.color=0x5865f2
                    embed.set_thumbnail(url=after.avatar_url)
                    if logchannel is not None:
                        await logchannel.send(embed=embed)
            else:
                return



    @commands.command(aliases=['voice-lock'])
    @commands.cooldown(3, 14, BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def voicelock(self, ctx, channel : commands.VoiceChannelConverter = None):
        channel = ctx.author.voice.channel if not channel else channel
        channel.set_permissions(ctx.guild.default_role, connect=False)
        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully locked {channel}.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Locked by: {ctx.author}")
        await ctx.send(embed=embed)

        voicelogs = utils.has_modlogs(ctx.guild)
        if voicelogs is True:
            logchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            embed = discord.Embed(description = f"{channel} has been locked in {ctx.guild} .")
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Locked by: {ctx.author}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            embed.color = 0x5865f2
            try:
                await logchannel.send(embed=embed)
            except:
                pass


    @commands.command(aliases=['voice-unlock'])
    @commands.cooldown(3, 14, BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def voiceunlock(self, ctx, channel : commands.VoiceChannelConverter = None):
        channel = ctx.author.voice.channel if not channel else channel
        channel.set_permissions(ctx.guild.default_role, connect=True)
        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully unlocked {channel}.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Unlocked by: {ctx.author}")
        await ctx.send(embed=embed)

        voicelogs = utils.has_modlogs(ctx.guild)
        if voicelogs is True:
            logchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            embed = discord.Embed(description = f"{channel} has been unlocked in {ctx.guild} .")
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Unlocked by: {ctx.author}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            embed.color = 0x5865f2
            try:
                await logchannel.send(embed=embed)
            except:
                pass


    @commands.command(aliases=['toggle-welcome', 'togglewelcome', 'welcoming'])
    @commands.cooldown(3, 14, BucketType.user)
    @has_permissions(manage_channels=True)
    async def welcome(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "welcoming", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcoming to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "welcoming", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcoming to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "welcoming")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "welcoming", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcoming to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "welcoming", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcoming to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the welcoming toggle.")

    @commands.command(aliases=['toggle-boost', 'toggleboost', 'boosting'])
    @commands.cooldown(3, 14, BucketType.user)
    @has_permissions(manage_channels=True)
    async def boost(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "boosting", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boosting to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "boosting", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boosting to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "boosting")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "boosting", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boosting to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "boosting", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boosting to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the boosting toggle.")

    @commands.command(aliases=['toggle-leave', 'togglegoodbye', 'goodbye', 'toggle-goodbye', 'leaving'])
    @commands.cooldown(3, 14, BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def leave(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "leaving", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leaving to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "leaving", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leaving to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "leaving")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "leaving", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leaving to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "leaving", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leaving to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the leaving toggle.")

    @commands.command(aliases=['welc-msg', 'welcome-msg', 'welcome-message'])
    @commands.cooldown(3, 14, BucketType.user)
    async def welcomemessage(self, ctx, *, message):
        utils.set_data("$set", ctx.guild, "welcome-message", message)
        utils.set_toggle("$set", ctx.guild, "welcome-embed", False)
        tog = discord.Embed(description = f"<:Check:855128805056184321> Succesfully set welcome message for {ctx.guild} to {message}.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=tog)

    @commands.command(aliases=['leave-msg', 'goodbye-msg', 'leave-message', 'goodbye-message'])
    @commands.cooldown(3, 14, BucketType.user)
    async def leavemessage(self, ctx, *, message):
        utils.set_data("$set", ctx.guild, "leave-message", message)
        utils.set_toggle("$set", ctx.guild, "leave-embed", False)
        tog = discord.Embed(description = f"<:Check:855128805056184321> Succesfully set leave message for {ctx.guild} to {message}.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=tog)

    @commands.command(aliases=['boost-msg', 'boost-message'])
    @commands.cooldown(3, 14, BucketType.user)
    async def boostmessage(self, ctx, *, message):
        utils.set_data("$set", ctx.guild, "boost-message", message)
        utils.set_toggle("$set", ctx.guild, "boost-embed", False)
        tog = discord.Embed(description = f"<:Check:855128805056184321> Succesfully set boost message for {ctx.guild} to {message}.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=tog)

    @commands.command(aliases=['welc-chan', 'welcome-chan', 'welcome-channel'])
    @commands.cooldown(3, 14, BucketType.user)
    async def welcomechannel(self, ctx, channel: discord.TextChannel):
        utils.set_data("$set", ctx.guild, "welcome-channel", channel.id)
        utils.set_toggle("$set", ctx.guild, "welcoming", True)
        tog = discord.Embed(description = f"<:Check:855128805056184321> Succesfully set welcome channel for {ctx.guild} to {channel.mention}.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=tog)

    @commands.command(aliases=['leave-chan', 'goodbye-chan', 'leave-channel', 'goodbye-channel'])
    @commands.cooldown(3, 14, BucketType.user)
    async def leavechannel(self, ctx, channel: discord.TextChannel):
        utils.set_data("$set", ctx.guild, "leave-channel", channel.id)
        utils.set_toggle("$set", ctx.guild, "leaving", True)
        tog = discord.Embed(description = f"<:Check:855128805056184321> Succesfully set leave channel for {ctx.guild} to {channel.mention}.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=tog)

    @commands.command(aliases=['boost-chan', 'boost-channel'])
    @commands.cooldown(3, 14, BucketType.user)
    async def boostchannel(self, ctx, channel: discord.TextChannel):
        utils.set_data("$set", ctx.guild, "boost-channel", channel.id)
        utils.set_toggle("$set", ctx.guild, "boosting", True)
        tog = discord.Embed(description = f"<:Check:855128805056184321> Succesfully set boost channel for {ctx.guild} to {channel.mention}.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
        tog.set_thumbnail(url = ctx.guild.icon_url)
        await ctx.send(embed=tog)

    @commands.command(aliases=['toggle-welcome-embed', 'togglewelcome-embed', 'welcome-embed'])
    @commands.cooldown(3, 14, BucketType.user)
    @has_permissions(manage_channels=True)
    async def welcomeembed(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "welcome-embed", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcome-embed to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "welcome-embed", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcome-embed to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "welcome-embed")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "welcome-embed", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcome-embed to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "welcome-embed", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled welcome-embed to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the welcome-embed toggle.")

    @commands.command(aliases=['toggle-boost-embed', 'toggleboost-embed', 'boost-embed'])
    @commands.cooldown(3, 14, BucketType.user)
    @has_permissions(manage_channels=True)
    async def boostembed(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "boost-embed", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boost-embed to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "boost-embed", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boost-embed to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "boost-embed")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "boost-embed", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boost-embed to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "boost-embed", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled boost-embed to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the boost-embed toggle.")

    @commands.command(aliases=['toggle-leave-embed', 'togglegoodbye-embed', 'goodbye-embed', 'toggle-goodbye-embed', 'leave-embed'])
    @commands.cooldown(3, 14, BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def leaveembed(self, ctx, toggle=None):
        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "leave-embed", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leave-embed to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "leave-embed", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leave-embed to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "leave-embed")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "leave-embed", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leave-embed to on.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "leave-embed", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled leave-embed to off.", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the leave-embed toggle.")

    @commands.command(aliases=['welc-test', 'welctester', 'welcome-tester'])
    @commands.cooldown(3, 14, BucketType.user)
    async def welcometester(self, ctx):
        member = ctx.author
        toggle = utils.find_data(ctx.guild, "welcoming")
        toggle2 = utils.find_data(ctx.guild, "welcome-embed")
        message = utils.find_data(ctx.guild, "welcome-message")
        if toggle is not True:
            return await ctx.send("Pleases enable welcoming to use this command.")
        else:
            if toggle2 is True:
                embed = discord.Embed(description=f"{member.mention} Welcome to {ctx.guild}, you are member number {len(list(ctx.guild.members))}!")
                embed.timestamp = datetime.datetime.utcnow()
                embed.color = member.color
                embed.set_footer(icon_url = member.guild.icon_url, text=f"{member.guild}")
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_author(name= member.name, icon_url=member.avatar_url)
                await ctx.send(embed=embed)
            else:
                if message != None:
                    await ctx.send(f"{member.mention}, {message}")

    @commands.command(aliases=['leave-tester', 'goodbye-tester', 'leave-test', 'goodbye-test', 'goodbyetester'])
    @commands.cooldown(3, 14, BucketType.user)
    async def leavetester(self, ctx):
        member = ctx.author
        toggle = utils.find_data(ctx.guild, "leaving")
        toggle2 = utils.find_data(ctx.guild, "leave-embed")
        message = utils.find_data(ctx.guild, "leave-message")
        if toggle is not True:
            return await ctx.send("Pleases enable leaving to use this command.")
        else:
            if toggle2 is True: 
                embed = discord.Embed(description=f"{member.mention}, sorry to see you go. Hope you have good luck in the future!")
                embed.timestamp = datetime.datetime.utcnow()
                embed.color = member.color
                embed.set_footer(icon_url = member.guild.icon_url, text=f"{ctx.guild}")
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_author(name= member.name, icon_url=member.avatar_url)
                await ctx.send(embed=embed)
            else:
                if message != None:
                    await ctx.send(f"{member.mention}, {message}")

    @commands.Cog.listener("on_member_join")
    async def welcome_event(self, member):
        toggle = utils.find_data(member.guild, "welcoming")
        toggle2 = utils.find_data(member.guild, "welcome-embed")
        message = utils.find_data(member.guild, "welcome-message")
        if toggle is not True:
            return
        if toggle is True:
            channelID = utils.find_data(member.guild, "welcome-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        if toggle2 is True:
            embed = discord.Embed(description=f"{member.mention} Welcome to {member.guild}, you are member number {len(list(member.guild.members))}!")
            embed.timestamp = datetime.datetime.utcnow()
            embed.color = member.color
            embed.set_footer(icon_url = member.guild.icon_url, text=f"{member.guild}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name= member.name, icon_url=member.avatar_url)
            if logchannel is not None:
                await logchannel.send(embed=embed)
            try:
                await member.send(embed=embed)
            except:
                pass
        else:
            if logchannel is not None and message is not None:
                await logchannel.send(f"{member.mention}, {message}")

    @commands.Cog.listener("on_member_remove")
    async def leave_event(self, member):
        toggle = utils.find_data(member.guild, "leaving")
        toggle2 = utils.find_data(member.guild, "leave-embed")
        message = utils.find_data(member.guild, "leave-message")
        if toggle is not True:
            return

        if toggle is True:
            channelID = utils.find_data(member.guild, "leave-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        if toggle2 is True:
            embed = discord.Embed(description=f"{member.mention}, sorry to see you go. Hope you have good luck in the future!")
            embed.timestamp = datetime.datetime.utcnow()
            embed.color = member.color
            embed.set_footer(icon_url = member.guild.icon_url, text=f"{member.guild}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_author(name= member.name, icon_url=member.avatar_url)
            await logchannel.send(embed=embed)
            try:
                await member.send(embed=embed)
            except:
                pass
        else:
            if logchannel is not None and message is not None:
                await logchannel.send(f"{member.mention}, {message}")

    @commands.Cog.listener("on_message")
    async def boost_event(self, message):
        toggle = utils.find_data(message.guild, "boosting")
        toggle2 = utils.find_data(message.guild, "boost-embed")
        messages = utils.find_data(message.guild, "boost-message")
        if toggle is not True:
            pass
        if toggle is True:
            channelID = utils.find_data(message.guild, "boost-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        if message is discord.MessageType.premium_guild_subscription:
            if toggle2 is True and toggle is True:
                embed = discord.Embed(description=f"Congrats, there is a new booster in the server!")
                embed.timestamp = datetime.datetime.utcnow()
                embed.color = 0x5865f2
                if logchannel != None:
                    await logchannel.send(embed=embed)
            else:
                if messages is not None and logchannel is not None and toggle is True:
                    await logchannel.send(messages)
        else:
            pass


def setup(bot):
    bot.add_cog(Logging(bot))