from operator import add
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import has_permissions
import pymongo
import discord
from discord.ext import commands
from utils.utils import utils, db
import datetime


class Args:
	InvalidArgs = [
		"users",
		"owners",
		"_id",
		"guild_id",
		"guild-name",
		"vanity-url",
		"whitelisted-roles",
		"whitelisted-invite-channels",
		"whitelisted-webhook-channels",
    ]

	ValidArgs = [
        "anti-nuke",
        "anti-permissions",
        "anti-unban",
		"anti-ban",
		"anti-bot",
		"anti-kick",
		"anti-link",
		"anti-spam",
		"anti-name-change",
		"anti-widget-create",
		"anti-widget-delete",
		"anti-role-create",
		"anti-role-delete",
		"anti-vanity",
		"anti-channel-create",
		"anti-channel-delete",
		"anti-webhook-create",
        "anti-webhook-delete",
        "anti-emoji-create",
        "anti-emoji-delete",
        "anti-integration-create",
        "anti-integration-delete",
        "anti-invite",
        "logging"
    ]


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['set-prefix', 'pre', 'setprefix'])
    @commands.cooldown(3, 14, commands.BucketType.user)
    async def prefix(self, ctx, prefix):
        check = utils.is_admin(ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server admins can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.set_data("$set", ctx.guild, "prefix", prefix)

        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Succesfully set prefix to: **{prefix}**", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Set by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['antinuke', 'toggle-antinuke'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantinuke(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-nuke", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antinuke to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-nuke", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antinuke to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-nuke")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-nuke", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antinuke to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-nuke", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antinuke to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antinuke toggle.")

    @commands.command(aliases=['antibot', 'toggle-antibot', 'toggle-bot'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantibot(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-bot", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antibot to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-bot", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antibot to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-bot")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-bot", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antibot to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-bot", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antibot to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antibot toggle.")

    @commands.command(aliases=['antilink', 'toggle-antilink', 'toggle-link'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantilink(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-link", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antilink to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-link", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antilink to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-link")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-link", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antilink to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-link", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antilink to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antilink toggle.")

    @commands.command(aliases=['antiinvite', 'toggle-antiinvite', 'toggle-invite'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiinvite(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-invite", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiinvite to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-invite", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiinvite to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-invite")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-invite", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiinvite to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-invite", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiinvite to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiinvite toggle.")


    @commands.command(aliases=['antiban', 'toggle-antiban', 'toggle-ban'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiban(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-ban", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiiban to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-ban", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiban to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-ban")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-ban", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiban to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-ban", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiban to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiban toggle.")

    @commands.command(aliases=['antiunban', 'toggle-antiunban', 'toggle-unban'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiunban(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-unban", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiunban to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-unban", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiunban to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-unban")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-unban", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiunban to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-unban", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiunban to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiunban toggle.")

    @commands.command(aliases=['antikick', 'toggle-antikick', 'toggle-kick'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantikick(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-kick", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antikick to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-kick", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antikick to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-kick")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-kick", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antikick to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-kick", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antikick to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antikick toggle.")

    @commands.command(aliases=['antivanity', 'toggle-antivanity', 'toggle-vanity'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantivanity(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-vanity", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antivanity to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-vanity", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antivanity to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-vanity")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-vanity", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antivanity to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-vanity", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antivanity to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antivanity toggle.")

    @commands.command(aliases=['antichannel-create', 'toggle-channel-create'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantichannelcreate(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-channel-create", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-channel-create", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-channel-create")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-channel-create", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-channel-create", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antichannel-create toggle.")

    @commands.command(aliases=['antichannel-delete', 'toggle-channel-delete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantichanneldelete(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-channel-delete", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-channel-delete", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-channel-delete")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-channel-delete", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-channel-delete", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antichannel-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antichannel-delete toggle.")

    @commands.command(aliases=['antirole-create', 'toggle-role-create'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantirolecreate(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-role-create", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-role-create", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-role-create")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-role-create", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-role-create", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antirole-create toggle.")

    @commands.command(aliases=['antirole-delete', 'toggle-role-delete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiroledelete(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-role-delete", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-role-delete", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-role-delete")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-role-delete", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-role-delete", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antirole-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antirole-delete toggle.")                    

    @commands.command(aliases=['antiwebhook-create', 'toggle-webhook-create'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiwebhookcreate(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-webhook-create", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-webhook-create", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-webhook-create")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-webhook-create", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-webhook-create", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiwebhook-create toggle.")

    @commands.command(aliases=['antiwebhook-delete', 'toggle-webhook-delete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiwebhookdelete(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-webhook-delete", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-webhook-delete", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-webhook-delete")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-webhook-delete", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-webhook-delete", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwebhook-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiwebhook-delete toggle.")

    @commands.command(aliases=['antiemoji-create', 'toggle-emoji-create'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiemojicreate(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-emoji-create", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-emoji-create", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-emoji-create")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-emoji-create", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-emoji-create", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiemoji-create toggle.")

    @commands.command(aliases=['antiemoji-delete', 'toggle-emoji-delete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiemojidelete(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-emoji-delete", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-emoji-delete", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-emoji-delete")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-emoji-delete", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-emoji-delete", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiemoji-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiemoji-delete toggle.")

    @commands.command(aliases=['antiwidget-create', 'toggle-widget-create'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiwidgetcreate(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-widget-create", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-widget-create", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-widget-create")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-widget-create", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-widget-create", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiwidget-create toggle.")

    @commands.command(aliases=['antiwidget-delete', 'toggle-widget-delete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiwidgetdelete(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-widget-delete", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-widget-delete", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-widget-delete")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-widget-delete", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-widget-delete", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiwidget-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiwidget-delete toggle.")

    @commands.command(aliases=['integration-create', 'toggle-integration-create'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiintegrationcreate(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-integration-create", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-integration-create", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-integration-create")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-integration-create", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-create to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-integration-create", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-create to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiintegration-create toggle.")

    @commands.command(aliases=['integration-delete', 'toggle-integration-delete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def toggleantiintegrationdelete(self, ctx, toggle=None):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if toggle == "off":
            utils.set_toggle("$set", ctx.guild, "anti-integration-delete", False)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        elif toggle == "on":
            utils.set_toggle("$set", ctx.guild, "anti-integration-delete", True)
            tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
            tog.set_thumbnail(url = ctx.guild.icon_url)
            await ctx.send(embed=tog)
        else:
            if toggle is None:
                result = utils.find_data(ctx.guild, "anti-integration-delete")
                if result is False:
                    utils.set_toggle("$set", ctx.guild, "anti-integration-delete", True)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-delete to on", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                elif result is True:
                    utils.set_toggle("$set", ctx.guild, "anti-integration-delete", False)
                    tog = discord.Embed(title = f"<:Check:855128805056184321> | Success", description=f"**{ctx.author}** toggled antiintergration-delete to off", timestamp=datetime.datetime.utcnow(), color=0x5865f2)
                    tog.set_thumbnail(url = ctx.guild.icon_url)
                    await ctx.send(embed=tog)
                else:
                    return await ctx.send("Couldn't change the antiintegration-delete toggle.")


    @commands.command(aliases=['set'])
    @commands.cooldown(3, 14, BucketType.user)
    async def settings(self, ctx):       
        embed = discord.Embed(title=f"__Settings__", timestamp=datetime.datetime.utcnow())
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        data = utils.find_data(ctx.guild)
        
        for valid in Args.ValidArgs:
            if data[valid] is True:
                try:
                    limit = utils.find_data(ctx.guild, f"{valid}-limit")
                    punishment = utils.find_data(ctx.guild, f"{valid}-punishment")
                    embed.add_field(name=f"**{valid}**", value=f"Enabled: <:yes:849069962014228490>\n Limit: `{limit}`\n Punishment: `{punishment}`")
                except KeyError:
                    try:
                        limit = utils.find_data(ctx.guild, f"{valid}-limit")
                        embed.add_field(name=f"**{valid}**", value=f"Enabled: <:yes:849069962014228490>\n Limit: `{limit}`")
                    except KeyError:
                        try:
                            punishment = utils.find_data(ctx.guild, f"{valid}-punishment")
                            embed.add_field(name=f"**{valid}**", value=f"Enabled: <:yes:849069962014228490>\n Punishment: `{punishment}`")
                        except KeyError:
                            embed.add_field(name=f"**{valid}**", value=f"Enabled: <:yes:849069962014228490>\n")

                
            elif data[valid] is False:
                embed.add_field(name=f"**{valid}**", value=f"Disabled: <a:no:849069815019995136>\n")
            else:
                pass

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Settings(bot))