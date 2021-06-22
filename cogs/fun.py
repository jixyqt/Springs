import discord
from discord.ext import commands
import aiohttp
import random
import asyncio
import datetime
from discord.ext.commands.cooldowns import BucketType
import giphy_client
from giphy_client.rest import ApiException
import requests
import json
import re
import libneko 
from libneko import pag

invitere = r"(?:https?:\/\/)?discord(?:\.gg|app\.com\/invite)?\/(?:#\/)([a-zA-Z0-9-]*)"
# my own regex
invitere2 = r"(http[s]?:\/\/)*discord((app\.com\/invite)|(\.gg))\/(invite\/)?(#\/)?([A-Za-z0-9\-]+)(\/)?"


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.snipes = {}
        self.editsnipes = {}
        self.bulksnipes =  {}

        @bot.listen('on_bulk_message_delete')
        async def bulksnipecheck(messages):
            guild = random.choice(messages).guild
            self.bulksnipes[guild.id] = messages
            

        @bot.listen('on_message_delete')
        async def deletesnipecheck(msg):
            if msg.author.bot:
                return
            self.snipes[msg.channel.id] = msg

        @bot.listen('on_message_edit')
        async def editsnipecheck(before, after):
            if before.author.bot or after.author.bot:
                return 
            if (len(before.content) > len(after.content)):
                self.editsnipes[before.channel.id] = [before, after]

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def cuddle(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/cuddle').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} cuddled {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @cuddle.error
    async def cuddle_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to cuddle.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def hug(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/hug').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} hugged {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to hug.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def tickle(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/tickle').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} tickled {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @tickle.error
    async def tickle_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to tickle.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def kiss(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/kiss').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} kissed {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to kiss.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def pat(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/pat').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} patted {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @pat.error
    async def pet_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to pat.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def slap(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/slap').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} slapped {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to slap.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def fact(self, ctx):
        r = requests.get(f'https://nekos.life/api/v2/fact').json()
        fact = r["fact"]
        await ctx.send(fact + ".")

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def pin(self, ctx, message : commands.MessageConverter=None):
        message = ctx.message if not message else message
        await message.pin(reason=f"{self.bot.user.name} | Pin")
        await ctx.send(f"Pinned {message.content}.")

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def unpin(self, ctx, message : commands.MessageConverter=None):
        message = ctx.message if not message else message
        await message.unpin(reason=f"{self.bot.user.name} | Unpin")
        await ctx.send(f"Unpinned {message}.")

    @commands.command(aliases=["8ball"])
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def _8ball(self, ctx, *, question=None):
        if question is None:
            await ctx.send("You must provide a question for the 8ball to answer.")

        else:
            r = requests.get(f"https://nekos.life/api/v2/8ball").json()
            url = r["url"]
            desc = r["response"]
            embed = discord.Embed(title = "Answer:", timestamp=ctx.message.created_at, description = desc)
            embed.set_image(url=url)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_author(name=f"Question: {question}")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def feed(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/feed').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} fed {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @feed.error
    async def feed_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to feed.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(3, 5, commands.BucketType.user)
    async def spank(self, ctx, member: commands.MemberConverter):
        r = requests.get(f'https://nekos.life/api/v2/img/spank').json()
        url = r["url"]
        embed = discord.Embed(description=f"{ctx.author.mention} spanked {member.mention}", timestamp=ctx.message.created_at)
        embed.set_image(url=url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @spank.error
    async def spank_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument)):
            embed = discord.Embed(title="<:Error:852619009714683924> **You must select a user to spank.**", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            await ctx.send(embed=embed)

    def sanitise(self, string):
        if len(string) > 1024:
            string = string[0:1021] + "..."
        string = re.sub(invitere2, '[INVITE REDACTED]', string)
        return string


    @commands.command()
    @commands.cooldown(3, 14, BucketType.user)
    async def snipe(self, ctx):
        try:
            snipe = self.snipes[ctx.channel.id]
        except KeyError:
            return await ctx.send('No snipes in this channel!')
        if snipe is None:
            return await ctx.send('No snipes in this channel!')
        # there's gonna be a snipe after this point
        emb = discord.Embed()
    
        emb.set_author(
            name=str(snipe.author),
            icon_url=snipe.author.avatar_url)
        emb.description = self.sanitise(snipe.content)
        emb.colour = snipe.author.colour
        emb.timestamp = snipe.created_at
        emb.set_footer(
            text=f'Message sniped by {str(ctx.author)}',
            icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
        self.snipes[ctx.channel.id] = None

    @commands.command(aliases=['bulk-snipe'])
    @commands.cooldown(3, 14, BucketType.user)
    async def bulksnipe(self, ctx):
        try:
            snipe = self.editsnipes[ctx.channel.id]
        except KeyError:
            return await ctx.send('No snipes in this channel!')
        if snipe is None:
            return await ctx.send('No snipes in this channel!')
        
        
        
        @pag.embed_generator(max_chars=2048)
        def get_embed(paginator, page, page_index):
            em = discord.Embed(description=page, timestamp=datetime.datetime.utcnow())
            em.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
            emb = discord.Embed(title = f"{len(snipe)} Messages sniped in {ctx.channel}:")
            for message in snipe:
                emb.add_field(name="Content", value=f"`{message.content}`")
                emb.add_field(name="Author", value=f"{message.author.mention}")
                emb.add_field(name="Time", value=f"`{message.created_at}`")
            return em

        page = pag.EmbedNavigatorFactory(factory=get_embed)
        page.start(ctx)
        

    @commands.command(aliases=['edit-snipe'])
    @commands.cooldown(3, 14, BucketType.user)
    async def editsnipe(self, ctx):
        try:
            snipe = self.editsnipes[ctx.channel.id]
        except KeyError:
            return await ctx.send('No snipes in this channel!')
        if snipe is None:
            return await ctx.send('No snipes in this channel!')
        emb = discord.Embed(title=f"Message sniped in {ctx.channel}:")
        emb.set_author(
            name=str(snipe[0].author),
            icon_url=snipe[0].author.avatar_url)
        emb.colour = snipe[0].author.colour
        emb.add_field(
                name='Before',
                value=self.sanitise(snipe[0].content),
                inline=False)
        emb.add_field(
            name='After',
            value=self.sanitise(snipe[1].content),
            inline=False)
        
        emb.timestamp = snipe[0].created_at
        emb.set_footer("Sniped by {}".format(ctx.author))

    @commands.command(help="Sends random gif.")
    @commands.cooldown(3, 14, BucketType.user)
    async def gif(self, ctx,*,q="random"):

        api_key="kyFBqt0ZA68EMsAhO6XaNnYDBQdVuiBk"
        api_instance = giphy_client.DefaultApi()

        try: 
        
            
            api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title="Here's a gif!")
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
            emb.set_footer(
                text= f'Requested by {ctx.author}'
            )
            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)    

    @commands.command(help="Search a gif.", aliases=['search-gif'])
    @commands.cooldown(3, 14, BucketType.user)
    async def searchgif(self, ctx, *, q):

        api_key="kyFBqt0ZA68EMsAhO6XaNnYDBQdVuiBk"
        api_instance = giphy_client.DefaultApi()

        try: 
        
            
            api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title="Here's a gif!")
            emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
            emb.set_footer(
                text= f'Requested by {ctx.author}'
            )

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)      
 

    @commands.command(aliases=['fl','fli'], help="Flips a coin.")
    @commands.cooldown(3, 14, BucketType.user)
    async def flip(self, ctx):

        number = (random.randint(1, 2))

        
      
        if number == 1:

            embed = discord.Embed(

                title = "Tails",

                description = "Coin Flipped!",

                timestamp = datetime.datetime.utcnow()
            )

            embed.set_author(

                name = ctx.author.name,

                icon_url = ctx.author.avatar_url
            )

            embed.set_image(

                url = 'https://images-na.ssl-images-amazon.com/images/I/51NyMaKLydL._AC_.jpg'
            )

            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(

                title = "Heads",

                description = "Coin Flipped!",

                timestamp = datetime.datetime.utcnow()


            )

            embed.set_author(

                name = ctx.author.name,

                icon_url= ctx.author.avatar_url
            )

            embed.set_image(

                url= "https://i.ebayimg.com/images/g/xtcAAOSwLwBaZigS/s-l300.jpg"
            )

            await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(3, 14, BucketType.user)
    async def meme(self, ctx):
        await ctx.trigger_typing()
        r = requests.get("https://meme-api.herokuapp.com/gimme").json()
        postLink = str(r['postLink'])
        subreddit = str(r['subreddit'])
        caption = str(r['title'])
        image = str(r['url'])
        ups = str(r['ups'])

        embed = discord.Embed(title=f'{caption}', url=postLink, timestamp = ctx.message.created_at)
        embed.set_footer(text=f'👍 {ups} | {subreddit}')
        embed.set_image(url=image)
        await ctx.send(embed=embed)
        
    @commands.command(help="Rates how gay you are.", aliases=['gay-rate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def gayrate(self, ctx, member: commands.MemberConverter = None, *,q="gay"):

        if member is None:

            member = ctx.author
        
        
            gay = random.randint(1, 100)
            embed = discord.Embed(
                title = "Gayrate",
                description = f"{member.mention}, You are **{gay}%** gay.",
                timestamp = datetime.datetime.utcnow()
            )

            embed.set_author(
                name = ctx.author.name,
                icon_url = ctx.author.avatar_url
            )
            

            embed.set_footer(
                text = f"Requested by {ctx.author}"
            )

            if gay > 50:
                api_key="kyFBqt0ZA68EMsAhO6XaNnYDBQdVuiBk"
                api_instance = giphy_client.DefaultApi()
                api_response = api_instance.gifs_search_get(api_key, q, limit=12, rating='g')
                lst = list(api_response.data)
                giff = random.choice(lst)
                embed.set_image(
                    url = f"https://media.giphy.com/media/{giff.id}/giphy.gif"
                )
            else:
                embed.set_image(
                    url = ctx.author.avatar_url
                )

            


            await ctx.send(embed=embed)

        else:
            gay = random.randint(1, 100)
            embed = discord.Embed(
                title = "Gayrate",
                description = f"{member.mention}, You are **{gay}%** gay.",
                timestamp = datetime.datetime.utcnow()
            )

            embed.set_author(
                name = ctx.author.name,
                icon_url = ctx.author.avatar_url
            )

            embed.set_footer(
                text = f"Requested by {ctx.author}"
            )

            if gay > 50:
                api_key="kyFBqt0ZA68EMsAhO6XaNnYDBQdVuiBk"
                api_instance = giphy_client.DefaultApi()
                api_response = api_instance.gifs_search_get(api_key, q, limit=12, rating='g')
                lst = list(api_response.data)
                giff = random.choice(lst)
                embed.set_image(
                    url = f"https://media.giphy.com/media/{giff.id}/giphy.gif"
                )
            else:
                embed.set_image(
                    url = member.avatar_url
                )

            


            await ctx.send(embed=embed)



    @commands.command(help="Rates how much of a simp you are.", aliases=['simp-rate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def simprate(self, ctx, member: commands.MemberConverter = None, *,q="simp"):
        if member is None:
            member = ctx.author
        
            simp = random.randint(1, 100)
            embed = discord.Embed(
                title = "Simprate",
                description = f"{member.mention}, You are **{simp}%** simp.",
                timestamp = datetime.datetime.utcnow()
            )

            embed.set_author(
                name = ctx.author.name,
                icon_url = ctx.author.avatar_url
            )

            embed.set_footer(
                text = f"Requested by {ctx.author}"
            )

            if simp > 50:
                api_key="kyFBqt0ZA68EMsAhO6XaNnYDBQdVuiBk"
                api_instance = giphy_client.DefaultApi()
                api_response = api_instance.gifs_search_get(api_key, q, limit=12, rating='g')
                lst = list(api_response.data)
                giff = random.choice(lst)
                embed.set_image(
                    url = f"https://media.giphy.com/media/{giff.id}/giphy.gif"
                )
            else:
                embed.set_image(
                    url = ctx.author.avatar_url
                )


            await ctx.send(embed=embed)

        else:
            simp = random.randint(1, 100)
            embed = discord.Embed(
                title = "Simprate",
                description = f"{member.mention}, You are **{simp}%** simp.",
                timestamp = datetime.datetime.utcnow()
            )

            embed.set_author(
                name = ctx.author.name,
                icon_url = ctx.author.avatar_url
            )

            embed.set_footer(
                text= f'Requested by {ctx.author}'
            )

            if simp > 50:
                api_key="kyFBqt0ZA68EMsAhO6XaNnYDBQdVuiBk"
                api_instance = giphy_client.DefaultApi()
                api_response = api_instance.gifs_search_get(api_key, q, limit=12, rating='g')
                lst = list(api_response.data)
                giff = random.choice(lst)
                embed.set_image(
                    url = f"https://media.giphy.com/media/{giff.id}/giphy.gif"
                )
            else:
                embed.set_image(
                    url = member.avatar_url
                )

            


            await ctx.send(embed=embed)

    @commands.command(help="Shows mentioned user's pp size.", aliases=['pp'])
    @commands.cooldown(3, 14, BucketType.user)
    async def penis(self, ctx, member: commands.MemberConverter = None):
        if member is None:
            member = ctx.author
            pp = random.randint(1, 20)

            embed = discord.Embed(
                title = "peepee size machine",
                description = member.mention + "'s" + " peepee size:" + " 8" + ("=" * pp) + "D"
                
            )
            embed.set_footer(
                text= f'Requested by {ctx.author}'
            )
            await ctx.send(embed=embed)
        
        else:
            
            pp = random.randint(1, 20)

            embed = discord.Embed(
                title = "pee pee size machine",
                description = member.mention + "'s" + " peepee size:" + " 8" + ("=" * pp) + "D"
                
            )
            embed.set_footer(
                text= f'Requested by {ctx.author}'
            )
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Fun(bot))
