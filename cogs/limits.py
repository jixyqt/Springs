import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from utils.utils import utils, db


class Limits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ban-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def banlimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-ban-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiban limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['spam-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def spamlimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-spam-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antispam limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['kick-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def kicklimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-kick-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antikick limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['unban-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def unbanlimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-unban-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiunban limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['channel-create-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def channelcreatelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-channel-create-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antichannel-create limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['channel-delete-limit'])
    async def channeldeletelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "anti-channel-delete-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antichannel-delete limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['webhook-create-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def webhookcreatelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-webhook-create-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiwebhook-create limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['webhook-delete-limit'])
    async def webhookdeletelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")

        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "anti-webhook-delete-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiwebhook-delete limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['widget-create-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def widgetcreatelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")

        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-widget-create-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiwidget-create limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['widget-delete-limit'])
    async def widgetdeletelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "anti-widget-delete-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiwidget-delete limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['integration-create-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def integrationcreatelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-integration-create-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiintergration-create limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['integration-delete-limit'])
    async def integrationdeletelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "anti-integration-delete-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiintergration-delete limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['role-create-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def rolecreatelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-role-create-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antirole-create limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['role-delete-limit'])
    async def roledeletelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "anti-role-delete-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antirole-delete limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['emoji-create-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def emojicreatelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.set_data("$set", ctx.guild, "anti-emoji-create-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiemoji-create limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['emoji-delete-limit'])
    async def emojideletelimit(self, ctx, limit: int):
        if limit > 10:
            return await ctx.send("Please select a valid integer between 1 and 10.")
        
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "anti-emoji-delete-limit", limit)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antiemoji-delete limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['permissions-limit', 'perms-limit', 'permlimit', 'perm-limit'])
    @commands.cooldown(3, 14, BucketType.user)
    async def permissionslimit(self, ctx, limit):

        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        if limit == "ban_members" or limit == "banmembers" or limit == "ban" or limit == "1":
            utils.set_data("$set", ctx.guild, "anti-permissions-limit", limit)

        elif limit == "manage_channels" or limit == "managechannels" or limit == "channels" or limit == "4":
            utils.set_data("$set", ctx.guild, "anti-permissions-limit", limit)

        elif limit == "administrator" or limit == "admin" or limit == "7":
            utils.set_data("$set", ctx.guild, "anti-permissions-limit", limit)

        elif limit == "kick_members" or limit == "kick"or limit == "kickmembers" or limit == "2":
            utils.set_data("$set", ctx.guild, "anti-permissions-limit", limit)
        
        elif limit == "manageservers" or limit == "manage_server" or limit == "guild" or limit == "servers" or limit == "6":
            utils.set_data("$set", ctx.guild, "anti-permissions-limit", limit)

        elif limit == "manage_webhooks" or limit == "webhooks" or limit == "managewebhooks" or limit == "5":
            utils.set_data("$set", ctx.guild, "anti-permissions-limit", limit)
        
        elif limit == "manage_roles" or limit == "roles" or limit == "manageroles" or limit == "3":
            utils.set_data("$set", ctx.guild, "anti-permissions-limit", limit)

        else:
            return await ctx.send("Please enter a valid permission limit.")
            
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully set {ctx.guild.name}'s antipermissions limit to **{limit}**.", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Limits(bot))