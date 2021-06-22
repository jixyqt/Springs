import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from utils.utils import utils


class Punishments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['punishment-antibot', 'punish-bot', 'punish-antibot', 'antibot-punishment', 'antibotpunishment'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantibot(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-bot-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antibot punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-antilink', 'punish-link', 'punish-antilink', 'antilink-punishment', 'antilinkpunishment'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantilink(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-link-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antilink punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-antiinvite', 'punish-invite', 'punish-antiinvite', 'antiinvite-punishment', 'antiinvitepunishment'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiinvite(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-invite-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiinvite punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-ban', 'punish-ban', 'punish-antiban', 'antiban-punishment', 'punishment-antiban'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiban(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-ban-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiban punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-unban', 'punish-unban', 'punish-antiunban', 'antiunban-punishment', 'punishment-antiunban'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiunban(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-unban-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiunban punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-kick', 'punish-kick', 'punish-antikick', 'antikick-punishment', 'punishment-antikick'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantikick(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-kick-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antikick punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-integration-create', 'punish-integration-create', 'punish-antiintegrationcreate', 'antiintegrationcreate-punishment', 'antiintegrationcreate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiintegrationcreate(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-integration-create-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiintergration-create punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-integration-delete', 'punish-integration-delete', 'punish-antiintegrationdelete', 'antiintegrationdelete-punishment', 'antiintegrationdelete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiintegrationdelete(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-integration-delete-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiintergration-delete punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-webhook-create', 'punish-webhook-create', 'punish-antiwebhookcreate', 'antiwebhookcreate-punishment', 'antiwebhookcreate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiwebhookcreate(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-webhook-create-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiwebhook-create punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-webhook-delete', 'punish-webhook-delete', 'punish-antiwebhookdelete', 'antiwebhookdelete-punishment', 'antiwebhookdelete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiwebhookdelete(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-webhook-delete-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiwebhook-delete punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")



    @commands.command(aliases=['punishment-emoji-create', 'punish-emoji-create', 'punish-antiemojicreate', 'antiemojicreate-punishment', 'antiemojicreate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiemojicreate(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-emoji-create-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiemoji-create punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")
            
    @commands.command(aliases=['punishment-emoji-delete', 'punish-emoji-delete', 'punish-antiemojidelete', 'antiemojidelete-punishment', 'antiemojidelete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiemojidelete(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-emoji-delete-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiemoji-delete punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-widget-create', 'punish-widget-create', 'punish-antiwidgetcreate', 'antiwidgetcreate-punishment', 'antiwidgetcreate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiwidgetcreate(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-widget-create-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiwidget-create punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")
            
    @commands.command(aliases=['punishment-widget-delete', 'punish-widget-delete', 'punish-antiwidgetdelete', 'antiwidgetdelete-punishment', 'antiwidgetdelete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiwidgetdelete(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-widget-delete-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiwidget-delete punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-antivanity', 'punish-vanity', 'punish-antivanity', 'antivanity-punishment', 'antivanitypunishment'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantivanity(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-vanity-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antivanity punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-antinamechange', 'punish-namechange', 'punish-antinamechange', 'antinamechange-punishment', 'antinamechangepunishment'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantinamechange(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-name-change-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiname-change punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-antipermissions', 'punish-permissions', 'punish-antipermissions', 'antipermissions-punishment', 'antipermissionspunishment'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantipermissions(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-permissions-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antipermissions punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-antispam', 'punish-spam', 'punish-antispam', 'antispam-punishment', 'antispampunishment'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantispam(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-spam-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antispam punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")

    @commands.command(aliases=['punishment-role-create', 'punish-role-create', 'punish-antirolecreate', 'antirolecreate-punishment', 'antirolecreate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantirolecreate(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-role-create-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antirole-create punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")
            
    @commands.command(aliases=['punishment-role-delete', 'punish-role-delete', 'punish-antiroledelete', 'antiroledelete-punishment', 'antiroledelete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantiroledelete(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-role-delete-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antiwidget-delete punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")
    @commands.command(aliases=['punishment-channel-create', 'punish-channel-create', 'punish-antichannelcreate', 'antichannelcreate-punishment', 'antichannelcreate'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantichannelcreate(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-channel-create-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antichannel-create punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")
            
    @commands.command(aliases=['punishment-channel-delete', 'punish-channel-delete', 'punish-antichanneldelete', 'antichanneldelete-punishment', 'antichanneldelete'])
    @commands.cooldown(3, 14, BucketType.user)
    async def punishmentantichanneldelete(self, ctx, punishment):
        check = utils.is_guild_owner(ctx.guild, ctx.author)
        check2 = utils.is_owner(ctx.author)
        if check is not True and check2 is not True:
            embed = discord.Embed(title="<:Error:852619009714683924> | Error",description=f"Sorry only the server owners can use this command", color=0x5865f2)
            embed.timestamp = ctx.message.created_at
            return await ctx.send(embed=embed)

        if punishment == "kick" or punishment == "mute" or punishment == "ban": 
            utils.set_data("$set", ctx.guild, "anti-channel-delete-punishment", punishment)
            embed = discord.Embed(title=f"<:Check:855128805056184321> | Success", description=f"Successfully set {ctx.guild.name}'s antichannel-delete punishment to **{punishment}**.", timestamp=ctx.message.created_at)
            embed.color = 0x5865f2
            embed.set_footer(text=f"Action by: {ctx.author}")
            await ctx.send(embed=embed)
        else:
            return await ctx.send("Please select a valid punishment.")






def setup(bot):
    bot.add_cog(Punishments(bot))