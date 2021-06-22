import discord
from discord.ext import commands
import aiohttp
import random
import asyncio
import datetime
import giphy_client
from giphy_client.rest import ApiException
import requests



class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['tits', 'melons'])
    @commands.is_nsfw()
    
    async def boobs(self, ctx):
        msgs =  ["Look at these fat melons!", "Here are some tits!", "Look at these twins!", "Here are some cowgirls!", "Here are some boobs!"]
        r = requests.get(f'https://nekos.life/api/v2/img/tits').json()
        url = r["url"]
        embed = discord.Embed(title="__Boobs__", description=random.choice(msgs), timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['ass'])
    @commands.is_nsfw()
    async def anal(self, ctx):
        msgs = ["Here is some backbreaking anal!", "Look at this legshaking anal!"]
        r = requests.get(f'https://nekos.life/api/v2/img/anal').json()
        url = r["url"]
        embed = discord.Embed(title="__Anal__", description=random.choice(msgs), timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['coochie', 'vagina'])
    @commands.is_nsfw()
    async def pussy(self, ctx):
        msgs = ["Here is some fat cat!", "Look at this wap!"]
        r = requests.get(f'https://nekos.life/api/v2/img/pussy').json()
        url = r["url"]
        embed = discord.Embed(title="__Pussy__", description=random.choice(msgs), timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['les'])
    @commands.is_nsfw()
    async def lesbian(self, ctx):
        msgs = ["Here is some lesbian"]
        r = requests.get(f'https://nekos.life/api/v2/img/les').json()
        url = r["url"]
        embed = discord.Embed(title="__Lesbian__", description=random.choice(msgs), timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['ass'])
    @commands.is_nsfw()
    async def anal(self, ctx):
        msgs = ["Here is some backbreaking anal!", "Look at this legshaking anal!"]
        r = requests.get(f'https://nekos.life/api/v2/img/anal').json()
        url = r["url"]
        embed = discord.Embed(title="__Anal__", description=random.choice(msgs), timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['nut', 'jizz'])
    @commands.is_nsfw()
    async def cum(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/cum').json()
        url = r["url"]
        embed = discord.Embed(title="__Cum__", description=f"{ctx.author.mention} cummed on {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        msgs = ["Here is some hentai!"]
        r = requests.get(f'https://nekos.life/api/v2/img/Random_hentai_gif').json()
        url = r["url"]
        embed = discord.Embed(title="__Hentai__", description=random.choice(msgs), timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['bj'])
    @commands.is_nsfw()
    async def blowjob(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/blowjob').json()
        url = r["url"]
        embed = discord.Embed(title="__Blowjob__", description=f"{ctx.author.mention} topped off {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Nsfw(bot))