import discord
from discord.ext import commands
import os, math

from utils.utils import utils, blacklist

class Owners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.command(
        name='servers',
        description='List the servers that the bot is in',
        usage='servers',
        aliases=["serverlist"]
    )
    @commands.is_owner()
    async def servers(self, ctx, page: int = 1):
        output = ''
        guilds = self.bot.guilds
        pages = math.ceil(len(guilds)/15)
        if 1 <= page <= pages:
            counter = 1+(page-1)*15
            for guild in guilds[(page-1)*15:page*15]:
                gn = guild.name
                gi = str(guild.id)
                gm = str(len(guild.members))
                output += f'**{counter}.** `{gn}` **|** `{gi}` **|** `{gm}`\n'
                counter += 1
            embed = discord.Embed(
                colour=0x36393f,
                description=output,
                title='__**Server List**__',
                timestamp=ctx.message.created_at
            )
            embed.set_footer(
                text=f'Page {page} of {pages}'
            )
            msg = await ctx.send(
                embed=embed
            )
            await msg.add_reaction("<a:L_Arrow:767064087367647242>")
            await msg.add_reaction("<a:R_Arrow:767064076512919552")
            #while True:
            #  if msg.author.add_reaction("<a:lrArrow:767064087367647242>"):
            #    page.back()
            #  elif msg.author.add_reaction("<a:r_rightarrow:781535142698942515>"):
            #    page.next()
        else:
            await ctx.send(
                embed=utils.create_embed(
                    'Invalid Page Number.'
                ),
                delete_after=10
            )

    @commands.command(
        name='leaveserver',
        description='Leave the server of your choice',
        usage='leaveserver `[number on list]`'
    )
    @commands.is_owner()
    async def leaveserver(self, ctx, pos: int):
        guilds = self.bot.guilds
        guild = guilds[pos-1]
        await guild.leave()
        await ctx.send(
            embed=utils.create_embed(
                f'Left {guild.name}'
            )
        )

    @commands.command(
        name='userblacklist'
    )
    @commands.is_owner()
    async def userblacklist(self, ctx, id: int, reason=None):
        if blacklist.find_one({'user_id': id}):
            await ctx.send(
                embed=utils.create_embed(
                    'User ID already blacklisted.'
                )
            )
        else:
            if self.bot.get_user(id) != None:
                blacklist.insert_one({'user_id': id})
                await ctx.send(
                    embed=utils.create_embed(
                        f'User, <@{id}> is now blacklisted.'
                    )
                )
                user = self.bot.get_user(id)
                await user.send(embed=utils.create_embed(f'You have been blacklisted from Springs for {reason}'))
            else:
                await ctx.send(
                    embed=utils.create_embed(
                        'Unknown User ID. Please make sure that user is in a server that I am in!'
                    ),
                    delete_after=30
                )


    @commands.command(
        name='channelblacklist'
    )
    @commands.is_owner()
    async def channelblacklist(self, ctx, id: int, reason=None):
        if blacklist.find_one({'channel_id': id}):
            await ctx.send(
                embed=utils.create_embed(
                    'Channel ID already blacklisted.'
                )
            )
        else:
            if self.bot.get_channel(id) != None:
                blacklist.insert_one({'channel_id': id})
                await ctx.send(
                    embed=utils.create_embed(
                        f'Channel, <@{id}> is now blacklisted. Reason: {reason}'
                    )
                )
                await ctx.send(
                    embed=utils.create_embed(
                        'Unknown Channel ID. Make sure that channeld ID is correct'
                    ),
                    delete_after=30
                )


#        check = utils.is_guild_owner(ctx.guild, ctx.author)
#        check2 = utils.is_owner(ctx.author)
#        if check is not True and check2 is not True:
#            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
#            embed.timestamp = ctx.message.created_at
#            return await ctx.send(embed=embed)

    @commands.command(
        name='showblacklist',
        description='List of all blacklisted users.',
        usage='showblacklist `[page]`'
    )
    @commands.is_owner()
    async def showblacklist(self, ctx, page: int = 1):
        output = ''
        blacklisted = blacklist.find()
        pages = math.ceil(blacklisted.count()/10)
        if 1 <= page <= pages:
            counter = 1+(page-1)*10
            for user in blacklisted[(page-1)*10:page*10]:
                user = self.bot.get_user(user['user_id'])
                output += f'**{counter}.** `{user.name}` | `{user.id}`\n'
                #output += f'**{counter}.** `{user}` | `{user}`\n'
                counter += 1
            embed = discord.Embed(
                colour=0x36393f,
                title='**__Blacklisted Users__**',
                description=output,
                timestamp=ctx.message.created_at
            )
            embed.set_footer(
                text=f'Page {page} of {pages}'
            )
            await ctx.send(
                embed=embed
            )
        else:
            await ctx.send(
                embed=utils.create_embed(
                    'The specified page does not exist'
                ),
                delete_after=10
            )

    @commands.command(
        name='unblacklist',
        description='Remove\'s a user from the blacklist.',
        usage='unblacklist `[userid]`'
    )
    @commands.is_owner()
    async def unblacklist(self, ctx, userid: int):
        if blacklist.find_one({'user_id': userid}):
            blacklist.delete_one({'user_id': userid})
            await ctx.send(
                embed=utils.create_embed(
                    f'User, <@{userid}> has been unblacklisted.'
                ),
                delete_after=30
            )
        else:
            await ctx.send(
                embed=utils.create_embed(
                    f'User, <@{userid}> is not blacklisted.'
                ),
                delete_after=10
            )

def setup(bot):
    bot.add_cog(Owners(bot))