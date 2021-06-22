import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h', 'cmds'])
    @commands.cooldown(3, 25, commands.BucketType.user)
    async def help(self, ctx):
        bot = self.bot
        embed1 = discord.Embed(title="__CATEGORIES__", description="*The default prefix for Springs is: `>`*\n *Example: `>help`*\n -**Info [`#1`]**\n -**Antinuke [`#2`]**\n -**Moderation [`#3`]**\n -**Music [`#4`]**\n -**Fun [`#5`]**\n -**Animals [`#6`]**\n -**Limits [`#7`]**\n -**Utility [`#8`]**\n -**Leveling [`#9`]**\n -**Voice [`#10`]**\n -**Welcome [`#11`]**\n -**Goodbye [`#12`]**\n -**Toggling [`#13`]**\n -**Logging [`#14`]**\n -**Management [`#15`]**\n -**Nsfw [`#16`]**", color=0x5865f2, timestamp=ctx.message.created_at)
        embed1.set_footer(text=f"1/17", icon_url=ctx.author.avatar_url)
        embed1.set_thumbnail(url=ctx.guild.icon_url)
        embed1.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed2 = discord.Embed(title="__Info__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed2.description = "\n **activity** - `Shows how many messages the user has sent.`\n **leaderboard-activity** - `Message count leaderboard`.\n **avatar** - `Shows the avatar of the user.`\n **credits** - `Shows Springs bot developers.`\n **boosts** - `Shows how many boosts the server has.`\n **bot-info** - `Shows the bot information.`\n **server-info** - `Shows the server information.`\n **server-icon** - `Shows the server icon/logo.`\n **server-banner** - `Shows the server banner.`\n **role-info** - `Shows the role information.`\n **channel-info** - `Shows the channel information.`\n **emoji-info** - `Shows emoji information.`\n **uptime** - `Shows the bot uptime.`\n **whois** - `Shows the information about a user.`\n **ping** - `Shows the bot ping`.\n **invite** - `Shows the bot invite link.`\n **bans** - `Shows the amount of bans the user has.`"
        embed2.set_footer(text="2/17", icon_url=ctx.author.avatar_url)
        embed2.set_thumbnail(url=ctx.guild.icon_url)
        embed2.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)
        
        embed3 = discord.Embed(title="__Antinuke__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed3.description = "\n **whitelist** - `Adds the user to the whitelist.`\n **whitelist/these** - `Adds multiple users to the whitelist.`\n **unwhitelist** - `Removes user from the whitelist.`\n **unwhitelist/these** - `Removes multiple users from the whitelist.`\n **whitelist/clear** - `Clears the whitelist.`\n **whitelisted** - `Shows users in the whitelist.`\n **admin** - `Adds or removes admin, enabling or disabling user to use antinuke settings.`\n **admin/these** - `Adds multiple users to the administrator list.`\n **admins/clear** - `CLears list of administrators.`\n **admins** - `Shows list of antinuke admins.`\n **settings** -`Shows antinuke settings.`"
        embed3.set_footer(text=f"3/17", icon_url=ctx.author.avatar_url)
        embed3.set_thumbnail(url=ctx.guild.icon_url)
        embed3.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed4 = discord.Embed(title="__Moderation__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed4.description = "\n **ban** - `Bans the user from the guild.`\n **ban/these** - `Bans multiple users from the guild.`\n **kick/these** - `Kicks multiple users from the guild.`\n **mute/these** - `Mutes multiple users from the guild. `\n **unmute** - `Unmutes the user.`\n **unmute/these** - `Unmutes multiple users.`\n **softban** - `Bans the user then unbans.`\n **softban/these** - `Bans then unbans multiple users from the guild.`\n **lock** - `Locks the channel.`\n **lock/these** - `Locks multiple channels of your choice.`\n **unlock** - `Unlocks the channel of your choice.`\n **unlock/these**- `Unlocks multiple channels of your choice.`\n **purge** - `Purges/bulk deletes messages from current channel.`\n **nuke** - `Deletes the channel then clones it.`\n **unban** - `Unbans the user.`\n **unban/these** - `Unbans multiple users.`\n **unban/all** - `Unbans all users in the server.`\n **role** - `Adds or removes role from a user.`\n **nickname** - `Sets the nickname of the user.`\n **slowmode** - `Sets the slowmode of a channel.`\n **mod** - `Adds or removes moderator, enabling or disabling user to use mod settings.`\n **mod/these** - `Adds multiple users to the moderation list.`\n **mods/clear** - `Clears the list of moderators.`\n **mods** - `Shows list of moderators.`"
        embed4.set_footer(text=f"4/17", icon_url=ctx.author.avatar_url)
        embed4.set_thumbnail(url=ctx.guild.icon_url)
        embed4.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)
        
        embed5 = discord.Embed(title="__Music__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed5.description = "\n **play and/or p** - `Plays the song of your choice in your vc.`\n **queue and/or q** - `Shows whats in queue to be played next. `\n **connect** - `Puts the bot in whatever vc your in.`\n **skip** - `Skips the song that is currently playing.`\n **pause** - `Pauses the song.`\n **resume** - `Resumes your music you left off at.`\n **stop** - `Stops the song until you resume.`\n **nowplaying** - `Shows the song that is currently playing.`\n **volume** - `Makes the bot louder or lower, by setting the volume.`\n **swap-dj** - `Sets the dj for the current music session.`"
        embed5.set_footer(text=f"5/17", icon_url=ctx.author.avatar_url)
        embed5.set_thumbnail(url=ctx.guild.icon_url)
        embed5.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed6 = discord.Embed(title="__Fun__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed6.description = "\n **cuddle ** - `Cuddle someone.`\n **dadjoke** - `The bot sends a dad joke.`\n **divorce** - `Divorce the user you are married to.`\n **feed** - `Feed someone.`\n **hug** - `Hug someone.`\n **kill** - `Kill someone.`\n **kiss** - `Kiss someone.`\n **lick** - `Lick someone.`\n **married** - `Shows the user you are married to.`\n **marry** - `Marry someone.`\n **pat** - `Pat someone.`\n **pet** - `Pet someone.`\n **rep** - `Give someone a reputation point.`\n **leaderboard-reputation** - `Shows the top 10 users with the most reputation points.`\n **ship** - `Ship someone.`\n **slap** - `Slap someone.`\n **spank** - `Spank someone.`\n **tickle** - `Tickle someone.`\n **gif** - `Sends a random gif.`\n **search-gif** - `Searches and sends gif of your choice.`\n **meme** - `Sends random meme.`\n **gay-rate** - `Shows how gay the user is.`\n **simp-rate** - `Shows how much of a simp the user is.`\n **penis** - `Shows the penis size of a user.`\n **8ball** - `Ask a question and get a random answer.`\n **fact** - `Sends random fact.`"
        embed6.set_footer(text=f"6/17", icon_url=ctx.author.avatar_url)
        embed6.set_thumbnail(url=ctx.guild.icon_url)
        embed6.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed7 = discord.Embed(title="__Animals __", color=0x5865f2, timestamp=ctx.message.created_at)
        embed7.description = "\n **dog** - `Shows a picture of a dog.`\n **cat** - `Shows a picture of a cat.`\n **fox** - `Shows a picture of a fox.`\n **panda** - `Shows a picture of a panda.`\n **racoon** - `Shows a picture of a racoon.`\n **koala** - `Shows a picture of a koala.`\n **whale** - `Shows a picture of a whale.`\n **goat** - `Shows a picture of a goat.`\n **bunny** - `Shows a picture of a bunny.`\n **shiba** - `Shows a picture of a shiba.`\n **koala** - `Shows a picture of a koala.`\n **duck** - `Shows a picture of a duck.`\n **lizard** - `Shows a picture of a lizard.`"
        embed7.set_footer(text=f"7/17", icon_url=ctx.author.avatar_url)
        embed7.set_thumbnail(url=ctx.guild.icon_url)
        embed7.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed8 = discord.Embed(title="__Limits__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed8.description = "\n **unban-limit** - `Sets antinuke ban limit.`\n **unban-limit** - `Sets antinuke ban limit.`\n **kick-limit** - `Sets the antinuke kick limit.`\n **channel/create-limit** - `Sets antinuke channel create limit.`\n **channel/delete-limit** - `Sets antinuke channel delete limit.`\n **role/create-limit** - `Sets antinuke role create limit.`\n **role/delete-limit** - `Sets antinuke role delete limit.`\n **webhook/create-limit** - `Sets the antinuke webhook create limit.`\n **webhook/delete-limit** - `Sets the antinuke webhook delete limit.`\n **emoji/create-limit** - `Sets the antinuke emoji create limit.`\n **emoji/delete-limit** - `Sets the antinuke emoji delete limit.`\n **spam-limit** - `Sets the server spam limit.`\n **permissons-limit** - `Sets antinuke permissions limit.`"
        embed8.set_footer(text="8/17", icon_url=ctx.author.avatar_url)
        embed8.set_thumbnail(url = ctx.guild.icon_url)
        embed8.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed9 = discord.Embed(title="__Utility__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed9.description = "\n **pin** - `Pins the message of choice.`\n **unpin** - `Unpins the message of choice.`\n **create-emoji** - `Creates emoji in server.`\n **add-emoji** - `Add one emoji to the server.`\n **add/emojis-these** - `Add multiple emojis to your server.`\n **invite-tracker** - `Sets the invite tracker channel.`\n **word-blacklist** - `Add/Remove a word from the blacklisted words.`\n **blacklisted-words** - `Shows the server blacklisted words.`\n **word/blacklist-clear** - `Clears list of blacklisted words.`\n **join-age** - `Sets the required age to join the server.`\n **color-roles** - `Sets up the color roles for the server.`\n **react-roles** - `Sets up the role reactions for the server.`\n **booster-message** - `Set the message that should be sent when a user boosts the server.`\n **create-embed** - `Sends a custom embed message.`\n **top-invites** - `Top 10 users with the most invites.`\n **afk** - `Sets that the user is afk.`\n **snipe ** - `Shows the last deleted message.`\n **editsnipe** - `Shows the last edited message.`\n **bulksnipe** - `Shows that last bulk deleted message.`\n **set-banner** - `Sets server banner.`\n **set-icon** - `Sets server icon.`"
        embed9.set_footer(text="9/17", icon_url=ctx.author.avatar_url)
        embed9.set_thumbnail(url = ctx.guild.icon_url)
        embed9.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed10 = discord.Embed(title="__Leveling__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed10.description = "\n **level-addrole** - `Set the role that the users get when they reach a specified level.`\n **doublexp-role** - `Set the roles that recieve double xp.`\n **leaderboard** - `Shows the top 10 users with the highest rank.`\n **level-channel** - `Set the channel where the level up message should be sent.`\n **level-message** - `Set the message that should be sent when a user levels up.`\n **level-roles** - `Shows the list of the roles that are given when a user reaches a specific level.`\n **noxp-channel** - `Set the channels where the users dont recieve xp`\n **noxp-role** - `Set the roles that dont earn xp.`\n **noxp-roles** - `Shows the list of the roles that dont earn xp.`\n **rank** - `Shows the rank of a user.`\n **remove-levelrole** - `Removes the role that the users get when they reach a specified level.`\n **reset** - `Resets a user rank.`\n **server-cardcolor** - `Set the server rank card color.`\n **user-cardcolor** - `Set your custom rank card color.`\n **server-rankcard** - `Set the server rank card image.`\n **user-rankcard** - `Set your custom rank card image.`\n **xp-gain** - `Sets the minimun and the maximum xp that the users earn.`"
        embed10.set_footer(text="10/17", icon_url=ctx.author.avatar_url)
        embed10.set_thumbnail(url = ctx.guild.icon_url)
        embed10.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed11 = discord.Embed(title="__Voice__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed11.description = "\n **voice-limit** - `Sets the maximum users that can join your voice channel.`\n **voice-reject** - `Doesn't allow a user to join your voice channel.`\n **voice-name** - `Changes the name of your voice channel.`\n **voice-setup** - `Sets up the custom voice channel for your server.`\n **voice-lock** - `Locks your voice channel.`\n **voice-permit** - `Allows other users to join your voice channel.`\n **voice-unlock** - `Unlocks the voice channel.`"
        embed11.set_footer(text="11/17", icon_url=ctx.author.avatar_url)
        embed11.set_thumbnail(url = ctx.guild.icon_url)
        embed11.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)
        
        embed12 = discord.Embed(title="__Welcome__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed12.description = "\n **join-role** - `Adds or removes the role that the users get when they join the server.`\n **join-roles** - `Shows list of join roles.`\n **welcome-message** - `Sets the welcome message that is sent when a user joins the server.`\n **welcome-channel** - `Sets the channel where the welcome message should be sent.`\n **welcome-embed** - `Enables or disables the embed welcome message.`\n **welcome-tester** - `Preview of the welcome message.`"
        embed12.set_footer(text="12/17", icon_url=ctx.author.avatar_url)
        embed12.set_thumbnail(url = ctx.guild.icon_url)
        embed12.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed13 = discord.Embed(title="__Goodbye__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed13.description = "\n **goodbye-message** - `Sets the goodbye message that is sent when a user leaves the server.`\n **goodbye-channel** - `Sets the channel where the goodbye message should be sent.`\n **goodbye-embed** - `Enables or disables the embed goodbye message.`\n **goodbye-tester** - `Preview of the goodbye message.`"
        embed13.set_footer(text="13/17", icon_url=ctx.author.avatar_url)
        embed13.set_thumbnail(url = ctx.guild.icon_url)
        embed13.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed14 = discord.Embed(title="__Toggling__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed14.description = "\n **toggle-vanity** - `Enables or disables antivanity.`\n **toggle-namechange** - `Enables or disables antinamechange.`\n **toggle-unban** - `Enables or diables antinuke unban.`\n **toggle-antinuke** - `Enables or disables antinuke.`\n **toggle-bot** - `Enables or disables antibot.`\n **toggle-link** - `Enables or disables antilink.`\n **anti/channel-create** - `Enables or disables antinuke channel create setting.`\n **toggle/channel-delete** - `Enables or disables antinuke channel delete setting.`\n **toggle/role-create** - `Enables or disables antinuke role create setting.`\n **toggle/role-delete** - `Enables or disables antinuke role delete setting.`\n **toggle/webhook-create** - `Enables or disables antinuke webhook create setting.`\n **toggle/webhook-delete** - `Enables or disables antinuke webhook delete setting.`\n **toggle-levels** - `Enables or disables levelling system.`\n **toggle-invites** - `Enables or disables invite tracker system.`\n **toggle-welcome** - `Enables or disables welcome message.`\n **toggle-leave** - `Enables or disables welcome message.`\n **toggle/join-roles** - `Enables or disables join roles.`\n **toggle/spam-detect** - `Enables or disables spam detection system.`\n **anti/emoji-create** - `Enables or disables antinuke emoji create setting.`\n **anti/emoji-delete** - `Enables or disables antinuke emoji delete setting.`"
        embed14.set_footer(text="14/17", icon_url=ctx.author.avatar_url)
        embed14.set_thumbnail(url = ctx.guild.icon_url)
        embed14.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed15 = discord.Embed(title="__Logging__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed15.description = "\n **set-messagelogs** - `Set the channel where the message logs should be sent.`\n **set-modlogs** - `Set the channel where the bot logs should be sent.`\n **set-userlogs** - `Set the channel where the user logs should be sent.`\n **set-voicelogs** - `Set the channel where the voice logs should be sent.`\n \n **toggle-logging** - `Enables or disables logs settings.`\n **set-auditlogs** - `Sets the channel where audit logs should be sent.`"
        embed15.set_footer(text="15/17", icon_url=ctx.author.avatar_url)
        embed15.set_thumbnail(url = ctx.guild.icon_url)
        embed15.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)

        embed16 = discord.Embed(title="__Management__", color=0x5865f2, timestamp=ctx.message.created_at)
        embed16.description = "\n **role-all** - `Adds selected role to everyone in server.`\n **create-channel** - `Creates a text channel.`\n **create/voice-channel** - `Creates a voice channel.`\n **create/channel-category** - `Creates a category.` **create-role** - `Creates a role.`\n **create-webhook** - `Creates a webhook.`\n **vanity** - `Set guild's vanity url.`\n **set-voicelogs** - `Set the channel where the voice logs should be sent.`"
        embed16.set_footer(text="16/17", icon_url=ctx.author.avatar_url)
        embed16.set_thumbnail(url = ctx.guild.icon_url)
        embed16.set_author(name="Springs Help Menu", icon_url=bot.user.avatar_url)
        
        embed17 = discord.Embed(title="__Nsfw__",color=0x5865f2, timestamp=ctx.message.created_at)
        embed17.description = "\n **hentai** - `Shows random hentai gif.`\n **blowjob** - `Gives blowjob to user of your choice.`\n **anal** - `Shows random anal sex.`\n **boobs** - `Shows random boob nsfw.`\n **tits** - `Shows random tit nsfw.`\n **pussy** - `Shows random picture of a pussy.`\n **lesbian** - `Shows lesbian nsfw.`\n **cum** - `Cum on user of your choice.`\n **spank** - `Spank user of your choice.`\n **orgasm** - `Shows orgasm nsfw.`"
        embed17.set_footer(text="17/17", icon_url=ctx.author.avatar_url)
        embed17.set_thumbnail(url = ctx.guild.icon_url)
        embed17.set_author(name="Thanks for using Springs!", icon_url=bot.user.avatar_url)

        pages = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17]

        message = await ctx.send(embed=embed1)
        await message.add_reaction('◀')
        await message.add_reaction('▶')
        await message.add_reaction('🔐')



        def check(reaction, user):
            return user == ctx.author


        async def helpmenu():
            i = 0
            reaction = None
            
            while True:

                if str(reaction) == '◀':
                    if i > 0:
                        i -= 1
                        await message.edit(embed=pages[i])

                elif str(reaction) == '▶':
                    if i < 17:
                        i += 1
                        await message.edit(embed=pages[i])

                if str(reaction) == '🔐':
                    await message.clear_reactions()
                    break

                try:
                    reaction, user = await bot.wait_for('reaction_add', check=check)
                    await message.remove_reaction(reaction, user)
                
                except:
                    break
        
        await helpmenu()

def setup(bot):
    bot.add_cog(Help(bot))