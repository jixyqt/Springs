import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.ext.commands.core import has_permissions
from utils.utils import utils

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['join-role', 'auto-role', 'autorole'])
    @commands.has_permissions(manage_roles=True)
    async def joinrole(self, ctx, role: discord.Role):
        if role.id in utils.find_data(ctx.guild, "auto-roles"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {role.mention} is already on the join roles list", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.upsert_data(ctx.guild, "auto-roles", role.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully added {role.mention} to the join roles list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['remove-join-role', 'unjoinrole', 'unautorole', 'remove-auto-role'])
    @has_permissions(manage_roles=True)
    async def removeautorole(self, ctx, role: discord.Role):
        if role.id not in utils.find_data(ctx.guild, "auto-roles"):
            embed = discord.Embed(title=f"<:Error:852619009714683924> | Error",description=f"Sorry {role.mention} is not on the join roles list", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)
        
        utils.pull_data(ctx.guild, "auto-roles", role.id)
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully removed {role.mention} from the join roles list", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['clear-auto-roles', 'clear-join-roles', 'clearautoroles'])
    @commands.cooldown(3, 14, BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def clearjoinroles(self, ctx):
        utils.clear(ctx.guild, "auto-roles")
        embed = discord.Embed(title=f"<:Check:855128805056184321> | Success",description=f"Successfully cleared {ctx.guild.name}'s auto-roles", timestamp=ctx.message.created_at)
        embed.color = 0x5865f2
        embed.set_footer(text=f"Action by: {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=['autoroles', 'join-roles', 'auto-roles'])
    @commands.cooldown(3, 14, BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def joinroles(self, ctx):
        embed = discord.Embed(title=f"**__Auto Roles__**", color=0x5865f2, timestamp=ctx.message.created_at, description = '')
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)

        data = utils.find_data(ctx.guild)
        for roleID in data['auto-roles']:
            role = ctx.guild.get_role(roleID)
            embed.description += (f"🧾 | Role: {role.mention}\n")
        
        await ctx.send(embed=embed)


    @commands.Cog.listener("on_member_join")
    async def autorole_event(self, member):
        data = utils.find_data(member.guild, "auto-roles")
        for roleID in data:
            role = member.guild.get_role(roleID)
            await member.add_roles(role, reason="Springs Auto-Role")

def setup(bot):
    bot.add_cog(Utility(bot))