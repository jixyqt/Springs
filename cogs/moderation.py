import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter, RoleConverter, UserConverter, Cog, context, has_permissions, Greedy
import datetime
import asyncio
from discord.ext.commands.converter import TextChannelConverter
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import is_owner
import giphy_client
import random
from giphy_client.rest import ApiException
import libneko
from libneko import pag
from utils.utils import utils, db

def has_modlogs(guild: discord.Guild):
    if utils.find_data(guild, "mod-logging") is True and utils.find_data(guild, "logging") is True:
        return True
    elif utils.find_data(guild, "log-channel") is None:
        return False
    else:
        return False


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ban-these', 'ban/these'])
    @has_permissions(ban_members=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def banthese(self, ctx, targets : Greedy[MemberConverter], *, reason=None):
        if reason == None:
            reason = f"{self.bot.user.name} | Ban"
        if not len(targets):
            embed = discord.Embed(description="<:Error:852619009714683924> One or more members are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)
        elif len(targets) > 5:
            embed = discord.Embed(description="<:Error:852619009714683924> Only can bulk action up to 5 members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)

        else:
            embed = discord.Embed(description=f"<:Check:855128805056184321> Successfully banned **{len(targets)}** members.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Banned by: {ctx.author}")
            await ctx.send(embed=embed)

            for target in targets:
                if utils.is_admin(target) is True or utils.is_owner(target) is True:
                    embed = discord.Embed(description="<:Error:852619009714683924> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)
                
                await target.ban(reason=reason)
                try:
                    embed = discord.Embed(description = f"You have been banned from {ctx.guild} for {reason}.")
                    embed.timestamp = ctx.message.created_at
                    embed.footer = f"Banned by: {ctx.author}"
                    embed.set_author(icon_url = target.avatar_url)
                    await target.send(embed=embed)
                    
                except:
                    pass
        
        
        if has_modlogs(ctx.guild) is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            try:
                for target in targets:
                    embed = utils.format_modlogs(user=target, reason=reason, action="banned")
                    await modchannel.send(embed=embed)
            except:
                pass


    @commands.command()
    @has_permissions(ban_members=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def ban(self, ctx, member: MemberConverter, *, reason=None):
        if reason == None:
            reason = f"{self.bot.user.name} | Ban"

        if utils.is_admin(member) is True or utils.is_owner(member) is True:
            embed = discord.Embed(description="<:Error:852619009714683924> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        
        embed = discord.Embed(description=f"<:Check:855128805056184321> Succesfully banned {member.mention}.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Banned by: {ctx.author}")
        await ctx.send(embed=embed)
        
        await member.ban(reason=reason)
        try:
            embed = discord.Embed(description = f"You have been banned from {ctx.guild} for {reason}.")
            embed.timestamp = ctx.message.created_at
            embed.footer = f"Banned by: {ctx.author}"
            embed.set_author(icon_url = member.avatar_url)
            await member.send(embed=embed)
        except:
            pass
    
        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            embed = utils.format_modlogs(user=member, reason=reason, action="banned")
            try:
                await modchannel.send(embed=embed)
            except:
                pass
    
    @commands.command()
    @has_permissions(ban_members=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def softban(self, ctx, member: UserConverter, *, reason=None):
        if reason == None:
            reason = f"{self.bot.user.name} | Softban"

        if utils.is_admin(member) is True or utils.is_owner(member) is True:
            embed = discord.Embed(description="<:Error:852619009714683924> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)

        embed = discord.Embed(description=f"<:Check:855128805056184321> Succesfully softbanned {member.mention}.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text= f"Softbanned by: {ctx.author}")
        await ctx.send(embed=embed)

        await ctx.guild.ban(member, reason=reason)
        await asyncio.sleep(2)
        await ctx.guild.unban(member, reason=reason)
        try:
            embed = discord.Embed(description = f"You have been softbanned from {ctx.guild} for {reason}.")
            embed.timestamp = ctx.message.created_at
            embed.footer = f"Banned by: {ctx.author}"
            embed.set_author(icon_url = member.avatar_url)
            await member.send(embed=embed)
        except:
            pass
        
        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            try:
                embed = utils.format_modlogs(user=member, reason=reason, action="softbanned")
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['softban-these', 'softban/these'])
    @has_permissions(ban_members=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def softbanthese(self, ctx, targets : Greedy[UserConverter], *, reason=None):
        if utils.is_admin(ctx.author) is not True:
            embed = discord.Embed(title="<a:no:849069815019995136> **Sorry only administrators can use this command.**", color=discord.Color.red())
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
            

        if reason == None:
            reason = f"{self.bot.user.name} | Softban"
        if not len(targets):
            embed = discord.Embed(description="<:Error:852619009714683924> One or more members are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)

        elif len(targets) > 5:
            embed = discord.Embed(description="<:Error:852619009714683924> Only can bulk action up to 5 members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)

        else:
            for target in targets:
                if utils.is_admin(target) is True or utils.is_owner(target) is True:
                    embed = discord.Embed(description="<:Error:852619009714683924> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)

                await ctx.guild.ban(target, reason=reason)
                await asyncio.sleep(2)
                await ctx.guild.unban(target, reason=reason)
                try:
                    embed = discord.Embed(description = f"You have been softbanned from {ctx.guild} for {reason}.")
                    embed.timestamp = ctx.message.created_at
                    embed.footer = f"Banned by: {ctx.author}"
                    embed.set_author(icon_url = target.avatar_url)
                    await target.send(embed=embed)
                except:
                    pass
            
            embed = discord.Embed(description=f"<:Check:855128805056184321> Successfully softbanned **{len(targets)}** members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Banned by: {ctx.author}")
            await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            try:
                for target in targets:
                    embed = utils.format_modlogs(user=target, reason=reason, action="softbanned")
                    await modchannel.send(embed=embed)
            except:
                pass
    
    @commands.command(aliases=['unban-these', 'unban/these'])
    @has_permissions(ban_members=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def unbanthese(self, ctx, targets : Greedy[UserConverter], *, reason=None):
        if utils.is_admin(ctx.author) is not True:
            embed = discord.Embed(title="<a:no:849069815019995136> **Sorry only administrators can use this command.**", color=discord.Color.red())
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if reason == None:
            reason = f"{self.bot.user.name} | Unban"
        if not len(targets):
            embed = discord.Embed(description="<a:no:849069815019995136> One or more members are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)
        elif len(targets) > 5:
            embed = discord.Embed(description="<a:no:849069815019995136> Only can bulk action up to 5 members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)

        else:
            embed = discord.Embed(description=f"<:yes:849069962014228490> Successfully unbanned **{len(targets)}** users.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Unbanned by: {ctx.author}") 
            await ctx.send(embed=embed)
            for target in targets:
                if utils.is_owner(target) is True or utils.is_admin(target) is True:
                    embed = discord.Embed(description="<a:no:849069815019995136> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)

                await ctx.guild.unban(target, reason=reason)
                try:
                    embed = discord.Embed(description = f"You have been unbanned from {ctx.guild} for {reason}.")
                    embed.timestamp = ctx.message.created_at
                    embed.set_footer(text=f"Unbanned by: {ctx.author}")
                    embed.set_author(icon_url = target.avatar_url)
                    await target.send(embed=embed)
                except:
                    pass
            
        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))

            try:
                for target in targets:
                    embed = utils.format_modlogs(user=target, reason=reason, action="unbanned")
                    await modchannel.send(embed=embed)
            except:
                pass



    @commands.command()
    @has_permissions(ban_members=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def unban(self, ctx, member: UserConverter, *, reason=None):
        if utils.is_admin(ctx.author) is not True:
            embed = discord.Embed(title="<a:no:849069815019995136> **Sorry only administrators can use this command.**", color=discord.Color.red())
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
            
        if reason == None:
            reason = f"{self.bot.user.name} | Unban"


        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully unbanned {member.mention}.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Unbanned by: {ctx.author}")
        await ctx.send(embed=embed)
        
        await ctx.guild.unban(member, reason=reason)
        try:
            embed = discord.Embed(description = f"You have been unbanned from {ctx.guild} for {reason}.")
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Unbanned by: {ctx.author}")
            embed.set_author(icon_url = member.avatar_url)
            await member.send(embed=embed)
        except:
            pass
        
        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            embed = utils.format_modlogs(user=member, reason=reason, action="unbanned")
            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['unban/all','unban-all'], help="Unbans all members who were banned.")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 100, commands.BucketType.guild)
    async def unbanall(self, ctx):
       
        guild = ctx.guild
        banned_users = await guild.bans()
        if len(banned_users) == 0:
            return await ctx.send("This server has no banned users.")
        embed1 = discord.Embed(description=f"<:yes:849069962014228490> Unbanning **{len(banned_users)}** members...", timestamp=ctx.message.created_at)
        await ctx.send(embed=embed1)
        unbanned = ""
        start = datetime.datetime.now()
        for ban_entry in banned_users:
            user = ban_entry.user
            guild = ctx.guild
            try:
                await guild.unban(user)
                unbanned += f"{ban_entry.user.mention}, "
            except:
                pass

        @pag.embed_generator(max_chars=2048)
        def get_embed(paginator, page, page_index):
            em = discord.Embed(description=page, timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
            elapsed = datetime.datetime.now() - start
            em.title = f"<:yes:849069962014228490> Unbanned {len(banned_users)} users in {elapsed.seconds}.{elapsed.microseconds} seconds."
            return em

        page = pag.EmbedNavigatorFactory(factory=get_embed)

        page += unbanned
        page.start(ctx)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:

            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            try:
                page.start(modchannel)
            except:
                pass

    @commands.command(aliases=['mute-these', 'mute/these'])
    @has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def mutethese(self, ctx, targets: Greedy[MemberConverter], *, reason=None):
        if utils.is_admin(ctx.author) is not True:
            embed = discord.Embed(title="<a:no:849069815019995136> **Sorry only administrators can use this command.**", color=discord.Color.red())
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted:
            muted = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=True, connect=False)
        if reason == None:
            reason = f"{self.bot.user.name} | Mute"
        if not len(targets):
            embed = discord.Embed(description="<a:no:849069815019995136> One or more members are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        elif len(targets) > 5:
            embed = discord.Embed(description="<a:no:849069815019995136> Only can bulk action up to 5 members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        else:
            for target in targets:
                if utils.is_admin(target) is True or utils.is_owner(target) is True:
                    embed = discord.Embed(description="<a:no:849069815019995136> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)
                if muted in target.roles:
                    embed = discord.Embed(description="<a:no:849069815019995136> One or more members are already muted.", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)
                elif target == ctx.author:
                    embed = discord.Embed(description="<a:no:849069815019995136> You can't mute yourself.", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)
                else:
                    await target.add_roles(muted, reason=reason)
                    try:
                        embed = discord.Embed(description = f"You have been muted in {ctx.guild} for {reason}.")
                        embed.timestamp = ctx.message.created_at
                        embed.set_footer(text=f"Muted by: {ctx.author}")
                        embed.set_author(icon_url = target.avatar_url)
                        await target.send(embed=embed)
                    except:
                        pass
            embed = discord.Embed(description=f"<:yes:849069962014228490> Successfully muted **{len(targets)}** members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Muted by: {ctx.author}")
            await ctx.send(embed=embed)


        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            try:
                for target in target:
                    embed = utils.format_modlogs(user=target, reason=reason, action="muted")
                    await modchannel.send(embed=embed)
            except:
                pass

                    

    @commands.command()
    @has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def mute(self, ctx, target: MemberConverter, *, reason=None):
        if utils.is_owner(target) is True or utils.is_admin(target) is True:
            embed = discord.Embed(description="<a:no:849069815019995136> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)

        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted:
            muted = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=True, connect=False)
        if reason == None:
            reason = f"{self.bot.user.name} | Mute"
        if target is None:
            embed = discord.Embed(description="<a:no:849069815019995136> You must select a user to mute.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        else:
            if muted in target.roles:
                embed = discord.Embed(description=f"<a:no:849069815019995136> {target} is already muted.", timestamp=ctx.message.created_at)
                embed.color = discord.Color.red()
                return await ctx.send(embed=embed)
            elif target == ctx.author:
                embed = discord.Embed(description="<a:no:849069815019995136> You can't mute yourself.", timestamp=ctx.message.created_at)
                embed.color = discord.Color.red()
                return await ctx.send(embed=embed)
            else:
                await target.add_roles(muted, reason=reason)
                try:
                    embed = discord.Embed(description = f"You have been muted in {ctx.guild} for {reason}.")
                    embed.timestamp = ctx.message.created_at
                    embed.set_footer(text=f"Muted by: {ctx.author}")
                    embed.set_author(icon_url = target.avatar_url)
                    await target.send(embed=embed)
                except:
                    pass
                embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully muted {target.mention}.", timestamp=ctx.message.created_at)
                embed.color = discord.Color.green()
                embed.set_footer(text=f"Muted by: {ctx.author}")
                await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
 
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            try:
                embed = utils.format_modlogs(user=target, reason=reason, action="muted")
                await modchannel.send(embed=embed)
            except:
                pass
                


    @commands.command(aliases=['unmute-these', 'unmute/these'])
    @has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def unmutethese(self, ctx, targets: Greedy[MemberConverter], *, reason=None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if reason == None:
            reason = f"{self.bot.user.name} | Unmute"
        if not len(targets):
            embed = discord.Embed(description="<a:no:849069815019995136> One or more members are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        elif len(targets) > 5:
            embed = discord.Embed(description="<a:no:849069815019995136> Only can bulk action up to 5 members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        else:
            for target in targets:
                if muted not in target.roles:
                    embed = discord.Embed(description="<a:no:849069815019995136> One or more members are not muted.", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)
                elif target == ctx.author:
                    embed = discord.Embed(description="<a:no:849069815019995136> You can't unmute yourself.", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)
                else:
                    await target.remove_roles(muted, reason=reason)
                    try:
                        embed = discord.Embed(description = f"You have been unmuted in {ctx.guild} for {reason}.")
                        embed.timestamp = ctx.message.created_at
                        embed.set_footer(text=f"Unmuted by: {ctx.author}")
                        embed.set_author(icon_url = target.avatar_url)
                        await target.send(embed=embed)
                    except:
                        pass
            embed = discord.Embed(description=f"<:yes:849069962014228490> Successfully unmuted **{len(targets)}** members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Unmuted by: {ctx.author}")
            await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(ctx.guild, "log-channel"))
            try:
                for target in targets:
                    embed = utils.format_modlogs(user=target, reason=reason, action="unmuted")
                    await modchannel.send(embed=embed)
            except:
                pass
                    

    @commands.command()
    @has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def unmute(self, ctx, target: MemberConverter, *, reason=None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if reason == None:
            reason = f"{self.bot.user.name} | Unmute"
        if target is None:
            embed = discord.Embed(description="<a:no:849069815019995136> You must select a user to unmute.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        else:
            if muted not in target.roles:
                embed = discord.Embed(description=f"<a:no:849069815019995136> {target} is not muted.", timestamp=ctx.message.created_at)
                embed.color = discord.Color.red()
                return await ctx.send(embed=embed)
            elif target == ctx.author:
                embed = discord.Embed(description="<a:no:849069815019995136> You can't unmute yourself.", timestamp=ctx.message.created_at)
                embed.color = discord.Color.red()
                return await ctx.send(embed=embed)
            else:
                await target.remove_roles(muted, reason=reason)
                try:
                    embed = discord.Embed(description = f"You have been unmuted in {ctx.guild} for {reason}.")
                    embed.timestamp = ctx.message.created_at
                    embed.set_footer(text=f"Unmuted by: {ctx.author}")
                    embed.set_author(icon_url = target.avatar_url)
                    await target.send(embed=embed)
                except:
                    pass
                embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully unmuted {target.mention}.", timestamp=ctx.message.created_at)
                embed.color = discord.Color.green()
                embed.set_footer(text=f"Unmuted by: {ctx.author}")
                await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            embed = utils.format_modlogs(user=target, reason=reason, action="unmuted")

            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['lock'], help="Locks the channel!")
    @commands.has_permissions(manage_channels = True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def lockdown(self, ctx, channel: commands.TextChannelConverter = None):      
        channel = ctx.channel if not channel else channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully locked {channel}.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Locked by: {ctx.author}")
        await ctx.send(embed=embed)
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            embed = discord.Embed(description = f"{channel} has been locked in {ctx.guild} .")
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Locked by: {ctx.author}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            try:
                await modchannel.send(embed=embed)
            except:
                pass
        
    @commands.command(aliases=['lock/these', 'lock-these'])
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def lockthese(self, ctx, targets: Greedy[TextChannelConverter]):
        if not len(targets):
            embed = discord.Embed(description="<a:no:849069815019995136> One or more channels are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        elif len(targets) > 5:
            embed = discord.Embed(description="<a:no:849069815019995136> Only can bulk action up to 5 channels.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        else:
            for target in targets:
                try:
                    overwrite = target.overwrites_for(ctx.guild.default_role)
                    overwrite.send_messages = False
                    await target.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                except:
                    pass
            embed = discord.Embed(description=f"<:yes:849069962014228490> Successfully locked **{len(targets)}** channels.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Locked by: {ctx.author}")
            await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            embed = discord.Embed(title = f"__{len(targets)} Channels Locked:__", description= "")
            for target in targets:
                embed.description += target
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Locked by: {ctx.author}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['unlock'], help="Locks the channel!")
    @commands.has_permissions(manage_channels = True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def unlockdown(self, ctx, channel: commands.TextChannelConverter = None):  
        
        channel = ctx.channel if not channel else channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = None
        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully unlocked {channel}.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Unlocked by: {ctx.author}")
        await ctx.send(embed=embed)
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            embed = discord.Embed(description = f"{channel} has been unlocked in {ctx.guild} .")
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Unlocked by: {ctx.author}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['unlock/these', 'unlock-these'])
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def unlockthese(self, ctx, targets: Greedy[TextChannelConverter]):
        if not len(targets):
            embed = discord.Embed(description="<a:no:849069815019995136> One or more channels are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        elif len(targets) > 5:
            embed = discord.Embed(description="<a:no:849069815019995136> Only can bulk action up to 5 channels.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        else:
            for target in targets:
                try:
                    overwrite = target.overwrites_for(ctx.guild.default_role)
                    overwrite.send_messages = None
                    await target.set_permissions(ctx.guild.default_role, overwrite=overwrite)                    
                except:
                    pass
            embed = discord.Embed(description=f"<:yes:849069962014228490> Successfully unlocked **{len(targets)}** channels.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Unlocked by: {ctx.author}")
            await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            embed = discord.Embed(title = f"__{len(targets)} Channels Unlocked:__", description = "")
            for target in targets:
                embed.description += target
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Unlocked by: {ctx.author}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['clear','cl','pur'], help="Deletes the amount (int) of messages you want to delete.")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def purge(self, ctx, amount : int):
        await ctx.message.delete()
        deleted = await ctx.channel.purge(limit=amount)
        embed = discord.Embed(description=f"<:yes:849069962014228490> Successfully deleted **{len(deleted)}** messages.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Deleted by: {ctx.author}")
        await ctx.send(embed=embed)


        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['n','nu'], help="Nukes the channel mentioned.")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def nuke(self, ctx, channel: commands.TextChannelConverter = None, *,q="nuke"):
        api_key="kyFBqt0ZA68EMsAhO6XaNnYDBQdVuiBk"
        api_instance = giphy_client.DefaultApi()

        try: 
            api_response = api_instance.gifs_search_get(api_key, q, limit=10, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e) 
    
        if not channel: 
            new_channel = await ctx.channel.clone(reason="Has been Nuked!")
            pos = ctx.channel.position
            await ctx.channel.delete()
            await new_channel.edit(position=pos)
            embed = discord.Embed(title = f"Nuked:", description = f"{ctx.channel} has been nuked!", timestamp = datetime.datetime.utcnow())
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            embed.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")
            await new_channel.send(embed=embed)
            
            modlogs = has_modlogs(ctx.guild)
            if modlogs is True:
                modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
                embed = discord.Embed(description = f"{channel.mention} has been nuked in {ctx.guild} .")
                embed.timestamp = ctx.message.created_at
                embed.set_footer(text=f"Nuked by: {ctx.author}")
                embed.set_thumbnail(url = ctx.author.avatar_url)
                embed.color = 0x5865f2
                try:
                    await modchannel.send(embed=embed)
                except:
                    pass
        
        else:
            pos = channel.position
            await channel.delete()
            newchannel = await channel.clone(reason="Has been nuked!")
            await newchannel.edit(position=pos)
            embed = discord.Embed(title = f"Nuked:", description = f"{channel} has been nuked!", timestamp = datetime.datetime.utcnow())
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            embed.set_image(url=f"https://media.giphy.com/media/{giff.id}/giphy.gif")    
            await newchannel.send(embed=embed)


            modlogs = has_modlogs(ctx.guild)
            if modlogs is True:
                modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
                embed = discord.Embed(description = f"{channel.mention} has been nuked in {ctx.guild} .")
                embed.timestamp = ctx.message.created_at
                embed.set_footer(text=f"Nuked by: {ctx.author}")
                embed.set_thumbnail(url = ctx.author.avatar_url)
                embed.color = 0x5865f2
                try:
                    await modchannel.send(embed=embed)
                except:
                    pass

    @commands.command(aliases=['kick-these', 'kick/these'])
    @commands.has_permissions(kick_members=True)
    async def kickthese(self, ctx, targets : Greedy[MemberConverter], *, reason=None):
        if reason == None:
            reason = f"{self.bot.user.name} | Kick"
        if not len(targets):
            embed = discord.Embed(description="<a:no:849069815019995136> One or more members are missing.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:yes:849069962014228490> Successfully kicked **{len(targets)}** members.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Kicked by: {ctx.author}")
            await ctx.send(embed=embed)

            for target in targets:
                if utils.is_admin(target) is True or utils.is_owner(target) is True:
                    embed = discord.Embed(description="<a:no:849069815019995136> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
                    embed.color = discord.Color.red()
                    return await ctx.send(embed=embed)
                await target.kick(reason=reason)
                try:
                    embed = discord.Embed(description = f"You have been kicked from {ctx.guild} for {reason}.")
                    embed.timestamp = ctx.message.created_at
                    embed.footer = f"Kicked by: {ctx.author}"
                    embed.set_author(icon_url = target.avatar_url)
                    await target.send(embed=embed)
                except:
                    pass
            
        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            embed = discord.Embed(description = f"", title=f"__{len(targets)} Members Kicked for {reason}:__")
            for target in targets:
                embed.description += f"{target.mention}, "
            embed.timestamp = ctx.message.created_at
            embed.set_footer(text=f"Kicked by: {ctx.author}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            embed.color = 0x5865f2
            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: MemberConverter, *, reason=None):
        if reason == None:
            reason = f"{self.bot.user.name} | Kick"

        if utils.is_owner(member) is True or utils.is_admin(member) is True:
            embed = discord.Embed(description="<a:no:849069815019995136> *That user is an admin or owner. I can't do that.*", timestamp=ctx.message.created_at)
            embed.color = discord.Color.red()
            return await ctx.send(embed=embed)
        
        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully kicked {member.mention}.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Kicked by: {ctx.author}")
        await ctx.send(embed=embed)
        
        await member.kick(reason=reason)
        try:
            embed = discord.Embed(description = f"You have been kicked from {ctx.guild} for {reason}.")
            embed.timestamp = ctx.message.created_at
            embed.footer = f"Kicked by: {ctx.author}"
            embed.set_author(icon_url = member.avatar_url)
            embed.color = 0x5865f2
            await member.send(embed=embed)
            
        except:
            pass
        

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            embed = utils.format_modlogs(user=member, reason=reason, action="kicked")
            try:
                await modchannel.send(embed=embed)
            except:
                pass

    @commands.command(aliases=['slowmo', 'slowmode'], help="Sets the slow mode to (int) seconds.")
    @commands.has_permissions(manage_channels=True)
    async def setdelay(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully set slowmode to **{seconds}** seconds.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            try:
                await modchannel.send(embed=embed)
            except:
                pass


    @commands.command(aliases=['nick'])
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: commands.MemberConverter, *, nickname):
        beforename = member.display_name
        await member.edit(nick=nickname)
        embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully set {beforename}'s nickname to **{nickname}**.", timestamp=ctx.message.created_at)
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Nicknamed by: {ctx.author}")
        await ctx.send(embed=embed)
   
        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            try:
                await modchannel.send(embed=embed)
            except:
                pass


    @commands.command()
    @has_permissions(manage_roles=True)
    async def role(self, ctx, member: MemberConverter, role : RoleConverter):
        if role.position > ctx.author.top_role.position: 
            embed = discord.Embed(title=f"<a:no:849069815019995136> **{role} is above your top role.**", color=discord.Color.red())
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
            
        elif role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully unroled {member.mention} **{role}**.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Roled by: {ctx.author}")
            await ctx.send(embed=embed)
        
        else:
            await member.add_roles(role)
            embed = discord.Embed(description=f"<:yes:849069962014228490> Succesfully roled {member.mention} **{role}**.", timestamp=ctx.message.created_at)
            embed.color = discord.Color.green()
            embed.set_footer(text=f"Roled by: {ctx.author}")
            await ctx.send(embed=embed)

        modlogs = has_modlogs(ctx.guild)
        if modlogs is True:
            modchannel = self.bot.get_channel(id=utils.find_data(guild=ctx.guild, value="log-channel"))
            try:
                await modchannel.send(embed=embed)
            except:
                pass


def setup(bot):
    bot.add_cog(Moderation(bot))