import discord
from discord.ext import commands
from utils.utils import utils
from discord.ext.commands import BucketType

class Whitelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wl'])
    @commands.cooldown(3, 14, BucketType.user)
    async def whitelist(self, ctx, user: discord.User):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command.", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if user.id in utils.find_data(ctx.guild, "whitelist-users"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {user.mention} is already whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.upsert_data(ctx.guild, "whitelist-users", user.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully whitelisted {user.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)
    
    @commands.command(aliases=['wlr', 'whitelist-role'])
    @commands.cooldown(3, 14, BucketType.user)
    async def whitelistrole(self, ctx, role: discord.Role):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if role.id in utils.find_data(ctx.guild, "whitelist-roles"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {role.mention} is already whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "whitelist-roles", role.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully whitelisted {role.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['wli', 'whitelist-invite'])
    @commands.cooldown(3, 14, BucketType.user)
    async def whitelistinvite(self, ctx, channel: discord.TextChannel):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if channel.id in utils.find_data(ctx.guild, "whitelist-invite-channels"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {channel.mention} is already whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "whitelist-invite-channels", channel.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully whitelisted {channel.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['wlw', 'whitelist-webhook'])
    @commands.cooldown(3, 14, BucketType.user)
    async def whitelistwebhook(self, ctx, channel: discord.TextChannel):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if channel.id in utils.find_data(ctx.guild, "whitelist-webhook-channels"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {channel.mention} is already whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "whitelist-webhook-channels", channel.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully whitelisted {channel.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['wll', 'whitelist-link'])
    @commands.cooldown(3, 14, BucketType.user)
    async def whitelistlink(self, ctx, channel: discord.TextChannel):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if channel.id in utils.find_data(ctx.guild, "whitelist-link-channels"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {channel.mention} is already whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "whitelist-link-channels", channel.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully whitelisted {channel.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['uwl'])
    @commands.cooldown(3, 14, BucketType.user)
    async def unwhitelist(self, ctx, user: discord.User):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if user.id not in utils.find_data(ctx.guild, "whitelist-users"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {user.mention} is not whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.pull_data(ctx.guild, "whitelist-users", user.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully unwhitelisted {user.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['uwlr', 'unwhitelist-role'])
    @commands.cooldown(3, 14, BucketType.user)
    async def unwhitelistrole(self, ctx, role: discord.Role):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if role.id not in utils.find_data(ctx.guild, "whitelist-roles"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {role.mention} is not whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "whitelist-roles", role.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully unwhitelisted {role.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)
    

    @commands.command(aliases=['uwli', 'unwhitelist-invite'])
    @commands.cooldown(3, 14, BucketType.user)
    async def unwhitelistinvite(self, ctx, channel: discord.TextChannel):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if channel.id not in utils.find_data(ctx.guild, "whitelist-invite-channels"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {channel.mention} is not whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "whitelist-invite-channels", channel.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully unwhitelisted {channel.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['uwlw', 'unwhitelist-webhook'])
    @commands.cooldown(3, 14, BucketType.user)
    async def unwhitelistwebhook(self, ctx, channel: discord.TextChannel):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if channel.id not in utils.find_data(ctx.guild, "whitelist-webhook-channels"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {channel.mention} is not whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "whitelist-webhook-channels", channel.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully unwhitelisted {channel.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['uwll', 'unwhitelist-link'])
    @commands.cooldown(3, 14, BucketType.user)
    async def unwhitelistlink(self, ctx, channel: discord.TextChannel):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if channel.id not in utils.find_data(ctx.guild, "whitelist-link-channels"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {channel.mention} is not whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "whitelist-link-channels", channel.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully unwhitelisted {channel.mention}", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cwl', 'clear-whitelist'])
    async def clearwhitelist(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.clear(ctx.guild, "whitelist-users")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s whitelisted members", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cwlr', 'clear-whitelist-roles'])
    async def clearwhitelistroles(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
            
        utils.clear(ctx.guild, "whitelist-roles")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s whitelisted roles", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cwlw', 'clear-whitelist-webhooks'])
    async def clearwhitelistwebhooks(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
            
        utils.clear(ctx.guild, "whitelist-webhook-channels")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s whitelisted webhooks", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cwli', 'clear-whitelist-invites'])
    async def clearwhitelistinvites(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
            
        utils.clear(ctx.guild, "whitelist-invite-channels")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s whitelisted invites", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cwll', 'clear-whitelist-links'])
    async def clearwhitelistlinks(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
            
        utils.clear(ctx.guild, "whitelist-link-channels")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s whitelisted links", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['add-owner', 'owner'])
    @commands.cooldown(3, 14, BucketType.user)
    async def addowner(self, ctx, user: discord.User):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if user.id in utils.find_data(ctx.guild, "owners"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {user.mention} is already whitelisted", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "owners", user.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully added {user.mention} to the owner's list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['remove-owner', 'unowner'])
    @commands.cooldown(3, 14, BucketType.user)
    async def removeowner(self, ctx, user: discord.User):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if user.id not in utils.find_data(ctx.guild, "owners"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {user.mention} is not on the owner's list", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "owners", user.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully removed {user.mention} from the owner's list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['add-owner-role', 'owner-role', 'ownerrole'])
    @commands.cooldown(3, 14, BucketType.user)
    async def addownerrole(self, ctx, role: discord.Role):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if role.id in utils.find_data(ctx.guild, "owner-roles"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {role.mention} is already on the owner roles list", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "owner-roles", role.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully added {role.mention} to the owner roles list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['remove-owner-role', 'unowner-role', 'removeowner-role'])
    @commands.cooldown(3, 14, BucketType.user)
    async def removeownerrole(self, ctx, role: discord.Role):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        if role.id not in utils.find_data(ctx.guild, "owner-roles"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {role.mention} is not on the owner roles list", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "owner-roles", role.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully removed {role.mention} from the owner roles list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['clear-owners', 'col'])
    @commands.cooldown(3, 14, BucketType.user)
    async def clearowners(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owner can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.clear(ctx.guild, "owners")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s owner's", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)


    @commands.command(aliases=['clear-owner-roles', 'colr'])
    @commands.cooldown(3, 14, BucketType.user)
    async def clearownerroles(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        if check is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> **Sorry only the guild owner can use this command.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        utils.clear(ctx.guild, "owner-roles")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s owner roles list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)


    @commands.command(aliases=['wld', 'whitelisted-data', 'guild-whitelist'])
    @commands.cooldown(3, 14, BucketType.user)
    async def whitelisted(self, ctx):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        data = utils.find_data(ctx.guild)
        embed = discord.Embed(title=f"**__Whitelisted Data__**", color=0x5865f2, timestamp=ctx.message.created_at, description = '')
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.description += (f"👑 | {ctx.guild.owner.mention}\n")
        
        for userID in data['owners']:
            if userID != ctx.guild.owner_id:
                user = self.bot.get_user(userID)
                embed.description += (f"👑 | {user.mention}\n")
            else:
                pass

        for roleID in data['owner-roles']:
            role = ctx.guild.get_role(roleID)
            embed.description += (f"👑 | Role: {role.mention}\n")

        for userID in data['whitelist-users']:
            if userID != ctx.guild.owner_id and userID not in data['owners']:
                user1 = self.bot.get_user(userID) 
                embed.description += (f"📋 | {user1.mention}\n")
            else:
                pass
        
        for roleID in data['whitelist-roles']:
            if roleID not in data['owner-roles']:
                role = ctx.guild.get_role(roleID)
                embed.description += (f"📋 | Role: {role.mention}\n")
            else:
                pass

        for channelID in data['whitelist-invite-channels']:
            channel = self.bot.get_channel(channelID)
            embed.description += (f"📋 | Invite: {channel.mention}\n")

        for channelID in data['whitelist-link-channels']:
            channel = self.bot.get_channel(channelID)
            embed.description += (f"📋 | Link: {channel.mention}\n")
        
        for channelID in data['whitelist-webhook-channels']:
            channel = self.bot.get_channel(channelID)
            embed.description += (f"📋 | Webhook: {channel.mention}\n")

        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Whitelist(bot))