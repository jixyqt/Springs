import discord
from discord.audit_logs import AuditLogDiff
from discord.enums import AuditLogAction
from discord.ext import commands
from utils.utils import utils, bot_id
import datetime

class Antinuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_guild_role_update")
    async def permissions_given(self, before, after):
        toggle = utils.find_data(before.guild, "anti-nuke")
        if toggle is not True:
            return
        punishment = utils.find_data(before.guild, "anti-permissions-punishment")
        whitelisted = utils.find_data(before.guild, "whitelist-users")
        whitelist_roles = utils.find_data(before.guild, "whitelist-roles")
        limit = utils.find_data(before.guild, "anti-permissions-limit")
        logtoggle = utils.find_data(before.guild, "logging")
        if logtoggle is True:
            channel = utils.find_data(before.guild, "log-channel")
            if channel is not None:
                logchannel = self.bot.get_channel(id=channel)
            else:
                logtoggle = False
        else:
            pass

        async for i in after.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.role_update):
            if i.user.id in whitelisted:
                return  
            
            if i.user.id == bot_id:
                return

            if after.guild.owner == i.user:
                return

            if utils.is_owner(i.user) is True:
                return
            
            if i.user in after.guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return
            
            if limit == "kick_members" or "kickmembers" or "kick" or 1:
                if not before.permissions.kick_members and after.permissions.kick_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(kick_members=False)
                    await after.edit(permissions=permissions)


                if not before.permissions.ban_members and after.permissions.ban_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(ban_members=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.administrator and after.permissions.administrator:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(administrator=False)
                    await after.edit(permissions=permissions)
                    return

            elif limit == "ban_members" or "ban"or "banmembers" or 2:
                if not before.permissions.ban_members and after.permissions.ban_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(ban_members=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.administrator and after.permissions.administrator:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(administrator=False)
                    await after.edit(permissions=permissions)
                    return
                    

            elif limit == "manage_roles" or "roles" or "manageroles" or 3:
                if not before.permissions.manage_roles and after.permissions.manage_roles:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(manage_roles=False)
                    await after.edit(permissions=permissions)
            

                if not before.permissions.manage_guild and after.permissions.manage_guild:                                
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return
                    
                    permissions = after.permissions
                    permissions.update(manage_guild=False)
                    await after.edit(permissions=permissions)
                    
                
                if not before.permissions.kick_members and after.permissions.kick_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(kick_members=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.ban_members and after.permissions.ban_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(ban_members=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.manage_channels and after.permissions.manage_channels:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(manage_channels=False)
                    await after.edit(permissions=permissions)
                    
                
                if not before.permissions.manage_webhooks and after.permissions.manage_webhooks:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(manage_webhooks=False)
                    await after.edit(permissions=permissions)


                if not before.permissions.administrator and after.permissions.administrator:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(administrator=False)
                    await after.edit(permissions=permissions)
                    return

            elif limit == "manage_channels" or "managechannels" or "channels" or 4:
                if not before.permissions.manage_channels and after.permissions.manage_channels:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(manage_channels=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.administrator and after.permissions.administrator:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(administrator=False)
                    await after.edit(permissions=permissions)
                    
                if not before.permissions.manage_webhooks and after.permissions.manage_webhooks:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(manage_webhooks=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.kick_members and after.permissions.kick_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(kick_members=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.ban_members and after.permissions.ban_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(ban_members=False)
                    await after.edit(permissions=permissions)
                    return

            elif limit == "manage_webhooks" or "webhooks" or "managewebhooks" or 5:
                if not before.permissions.manage_webhooks and after.permissions.manage_webhooks:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(manage_webhooks=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.manage_guild and after.permissions.manage_guild:                                
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return
                    
                    permissions = after.permissions
                    permissions.update(manage_guild=False)
                    await after.edit(permissions=permissions)
                    
                
                if not before.permissions.kick_members and after.permissions.kick_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(kick_members=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.ban_members and after.permissions.ban_members:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(ban_members=False)
                    await after.edit(permissions=permissions)
                
                if not before.permissions.administrator and after.permissions.administrator:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(administrator=False)
                    await after.edit(permissions=permissions)
                    return

            elif limit == "administrator" or "admin" or 7:
                if not before.permissions.administrator and after.permissions.administrator:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(administrator=False)
                    await after.edit(permissions=permissions)
                    return

            elif limit == "manageservers" or "manage_server" or "guild" or "servers" or 6:
                if not before.permissions.manage_guild and after.permissions.manage_guild:                                
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return
                    
                    permissions = after.permissions
                    permissions.update(manage_guild=False)
                    await after.edit(permissions=permissions)

                if not before.permissions.administrator and after.permissions.administrator:
                    if punishment == 'kick':
                        await after.guild.kick(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="kicked")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'ban':
                        await after.guild.ban(i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="banned")
                            await logchannel.send(embed=embed)

                        return

                    if punishment == 'mute':
                        await utils.mute(guild=after.guild, member=i.user, reason='Springs Anti-Nuke | Dangerous Permissions Given')
                        if logtoggle is True:
                            embed = utils.format_logs(user=i.user, reason="Giving dangerous permissions", action="muted")
                            await logchannel.send(embed=embed)

                        return

                    permissions = after.permissions
                    permissions.update(administrator=False)
                    await after.edit(permissions=permissions)
                    return
            else:
                return

    @commands.Cog.listener("on_guild_role_create")
    async def anti_role_create(self, role: discord.Role):
        toggle = utils.find_data(role.guild, "anti-nuke")
        toggle2 = utils.find_data(role.guild, "anti-role-create")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(role.guild, "anti-role-create-punishment")
        whitelisted = utils.find_data(role.guild, "whitelist-users")
        whitelist_roles = utils.find_data(role.guild, "whitelist-roles")
        limit = utils.find_data(role.guild, "anti-role-create-limit")
        logtoggle = utils.find_data(role.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(role.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        roles_created = []

        async for i in role.guild.audit_logs(after= datetime.datetime.utcnow() - datetime.timedelta(minutes = 1), action=AuditLogAction.role_create):
            roles_created.append(i.target.id)

        async for i in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
            if i.user.id in whitelisted:
                return  
            
            if role.guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, role.guild) is True:
                return
            
            if i.user in role.guild.members:
                for rolee in i.user.roles:
                    if rolee.id in whitelist_roles:
                        return
            utils.upsert_data(role.guild, "role-create-audit", i.user.id)

            counter = 0
            data = utils.find_data(role.guild)
            for userID in data['role-create-audit']:
                if userID == i.user.id:
                    counter += 1
            

            if counter == limit:
                if punishment == 'kick':
                    await role.guild.kick(i.user, reason='Springs Anti-Nuke | Creating Roles')
                    for target in roles_created:
                        try:
                            target = role.guild.get_role(role_id=target)
                            await target.delete(reason="Springs Anti-Nuke | Deleting User-Created Roles")
                        except AttributeError:
                            pass
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Roles", action="kicked")
                        await logchannel.send(embed=embed)

                    return


                if punishment == 'ban':
                    await role.guild.ban(i.user, reason='Springs Anti-Nuke | Creating Roles')
                    for target in roles_created:
                        try:
                            target = role.guild.get_role(role_id=target)
                            await target.delete(reason="Springs Anti-Nuke | Deleting User-Created Roles")
                        except AttributeError:
                            pass
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Roles", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild=role.guild, member=i.user, reason='Springs Anti-Nuke | Creating Roles')
                    for target in roles_created:
                        try:
                            target = role.guild.get_role(role_id=target)
                            await target.delete(reason="Springs Anti-Nuke | Deleting User-Created Roles")
                        except AttributeError:
                            pass
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Roles", action="muted")
                        await logchannel.send(embed=embed)

                    return
            else:
                return

    @commands.Cog.listener("on_guild_role_delete")
    async def anti_role_delete(self, role: discord.Role):
        toggle = utils.find_data(role.guild, "anti-nuke")
        toggle2 = utils.find_data(role.guild, "anti-role-delete")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(role.guild, "anti-role-delete-punishment")
        whitelisted = utils.find_data(role.guild, "whitelist-users")
        whitelist_roles = utils.find_data(role.guild, "whitelist-roles")
        limit = utils.find_data(role.guild, "anti-role-delete-limit")
        logtoggle = utils.find_data(role.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(role.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass
        

        async for i in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete):
            if i.user.id in whitelisted:
                return  
            if i.user == self.bot.user:
                return

            if i.user.id == bot_id:
                return
            
            if role.guild.owner == i.user:
                return

            if utils.is_owner(i.user, role.guild) is True:
                return
            
            if i.user in role.guild.members:
                for rolee in i.user.roles:
                    if rolee.id in whitelist_roles:
                        return
            
            utils.upsert_data(role.guild, "role-delete-audit", i.user.id)

            counter = 0
            data = utils.find_data(role.guild)
            for userID in data['role-delete-audit']:
                if userID == i.user.id:
                    counter += 1

            if counter == limit: 
                if punishment == 'kick':
                    await role.guild.kick(i.user, reason='Springs Anti-Nuke | Deleting Roles')
                    await role.guild.create_role(name=role.name, permissions=role.permissions, hoist=role.hoist, color=role.color, mentionable=role.mentionable, reason="Springs Anti-Nuke | Recreating User-Deleted Roles")
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Roles", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await role.guild.ban(i.user, reason='Springs Anti-Nuke | Deleting Roles')
                    await role.guild.create_role(name=role.name, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable, color=role.color, reason="Springs Anti-Nuke | Recreating User-Deleted Roles")
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Roles", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild=role.guild, member=i.user, reason='Springs Anti-Nuke | Deleting Roles')
                    await role.guild.create_role(name=role.name, permissions=role.permissions, hoist=role.hoist, color=role.color, mentionable=role.mentionable, reason="Springs Anti-Nuke | Recreating User-Deleted Roles")
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Roles", action="muted")
                        await logchannel.send(embed=embed)

                    return
            else:
                return

    @commands.Cog.listener("on_guild_channel_create")
    async def anti_channel_create(self, channel):
        channels_created = []
        toggle = utils.find_data(channel.guild, "anti-nuke")
        toggle2 = utils.find_data(channel.guild, "anti-channel-create")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(channel.guild, "anti-channel-create-punishment")
        whitelisted = utils.find_data(channel.guild, "whitelist-users")
        whitelist_roles = utils.find_data(channel.guild, "whitelist-roles")
        limit = utils.find_data(channel.guild, "anti-channel-create-limit")
        logtoggle = utils.find_data(channel.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(channel.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass
        

        async for i in channel.guild.audit_logs(after= datetime.datetime.utcnow() - datetime.timedelta(minutes = 1), action=AuditLogAction.channel_create):
            channels_created.append(i.target.id)

        async for i in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
            if i.user.id in whitelisted:
                return  
            
            if channel.guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, channel.guild) is True:
                return
            
            if i.user in channel.guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(channel.guild, "channel-create-audit", i.user.id)

            counter = 0
            data = utils.find_data(channel.guild)
            for userID in data['channel-create-audit']:
                if userID == i.user.id:
                    counter += 1
            
            if counter == limit:
                if punishment == 'kick':
                    await channel.guild.kick(i.user, reason='Springs Anti-Nuke | Creating Channels')
                    for target in channels_created:
                        try:
                            target = channel.guild.get_channel(channel_id=target)
                            await target.delete(reason="Springs Anti-Nuke | Deleting User-Created Channels")
                        except AttributeError:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Channels", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await channel.guild.ban(i.user, reason='Springs Anti-Nuke | Creating Channels')
                    for target in channels_created:
                        try:
                            target = channel.guild.get_channel(channel_id=target)
                            await target.delete(reason="Springs Anti-Nuke | Deleting User-Created Channels")
                        except AttributeError:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Channels", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild=channel.guild, member=i.user, reason='Springs Anti-Nuke | Creating Channels')
                    for target in channels_created:
                        try:
                            target = channel.guild.get_channel(channel_id=target)
                            await target.delete(reason="Springs Anti-Nuke | Deleting User-Created Channels")
                        except AttributeError:
                            pass
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Channels", action="muted")
                        await logchannel.send(embed=embed)

                    return
            else:
                return

    @commands.Cog.listener("on_guild_channel_delete")
    async def anti_channel_delete(self, channel):
        toggle = utils.find_data(channel.guild, "anti-nuke")
        toggle2 = utils.find_data(channel.guild, "anti-channel-delete")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(channel.guild, "anti-channel-delete-punishment")
        whitelisted = utils.find_data(channel.guild, "whitelist-users")
        whitelist_roles = utils.find_data(channel.guild, "whitelist-roles")
        limit = utils.find_data(channel.guild, "anti-channel-delete-limit")
        logtoggle = utils.find_data(channel.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(channel.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass
        

        async for i in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
            if i.user.id in whitelisted:
                return  

            if i.user.id == bot_id:
                return
            
            if channel.guild.owner == i.user:
                return

            if utils.is_owner(i.user, channel.guild) is True:
                return
            
            if i.user in channel.guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return
            
            utils.upsert_data(channel.guild, "channel-delete-audit", i.user.id)

            counter = 0
            data = utils.find_data(channel.guild)
            for userID in data['channel-delete-audit']:
                if userID == i.user.id:
                    counter += 1
            

            if counter == limit:
                if punishment == 'kick':
                    await channel.guild.kick(i.user, reason='Springs Anti-Nuke | Deleting Channels')
                    new_channel = await channel.clone(reason="Springs Anti-Nuke | Recreating User-Deleted Channels")
                    await new_channel.edit(position=channel.position)
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Channels", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await channel.guild.ban(i.user, reason='Springs Anti-Nuke | Deleting Channels')
                    new_channel = await channel.clone(reason="Springs Anti-Nuke | Recreating User-Deleted Channels")
                    await new_channel.edit(position=channel.position)

                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Channels", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild=role.guild, member=i.user, reason='Springs Anti-Nuke | Deleting Channels')
                    new_channel = await channel.clone(reason="Springs Anti-Nuke | Recreating User-Deleted Channels")
                    await new_channel.edit(position=channel.position)
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Channels", action="muted")
                        await logchannel.send(embed=embed)

                    return
            else:
                return
                

    @commands.Cog.listener("on_member_ban")
    async def anti_ban(self, guild, user):
        toggle = utils.find_data(guild, "anti-nuke")
        toggle2 = utils.find_data(guild, "anti-ban")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(guild, "anti-ban-punishment")
        whitelisted = utils.find_data(guild, "whitelist-users")
        whitelist_roles = utils.find_data(guild, "whitelist-roles")
        limit = utils.find_data(guild, "anti-ban-limit")
        logtoggle = utils.find_data(guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass
        
        banned_users = []

        async for i in guild.audit_logs(after= datetime.datetime.utcnow() - datetime.timedelta(minutes= 1), action = AuditLogAction.ban):
            banned_users.append(i.target)
    

        async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            if i.user.id in whitelisted:
                return 
            
            if guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, guild) is True:
                return
            
            if i.user in guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(guild, "ban-audit", i.user.id)
            banned_users.append(i.target)
            
            counter = 0
            data = utils.find_data(guild)
            for userID in data['ban-audit']:
                if userID == i.user.id:
                    counter += 1


            if counter == limit:
                if punishment == 'kick':
                    await guild.kick(i.user, reason='Springs Anti-Nuke | Banning Members')
                    for target in banned_users:
                        try:
                            await guild.unban(target if target != i.user else target, reason='Springs Anti-Nuke | Unbanning User-Banned Members')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Banning Members", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await guild.ban(i.user, reason='Springs Anti-Nuke | Banning Members')
                    for target in banned_users:
                        try:
                            await guild.unban(target if target != i.user else target, reason='Springs Anti-Nuke | Unbanning User-Banned Members')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Banning Members", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild=guild, member=i.user, reason='Springs Anti-Nuke | Banning Members')
                    for target in banned_users:
                        try:
                            await guild.unban(target if target != i.user else target, reason='Springs Anti-Nuke | Unbanning User-Banned Members')
                        except:
                            pass

                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Banning Members", action="muted")
                        await logchannel.send(embed=embed)

                    return
            else:
                return

    @commands.Cog.listener("on_member_unban")
    async def anti_unban(self, guild, user):
        toggle = utils.find_data(guild, "anti-nuke")
        toggle2 = utils.find_data(guild, "anti-unban")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(guild, "anti-unban-punishment")
        whitelisted = utils.find_data(guild, "whitelist-users")
        whitelist_roles = utils.find_data(guild, "whitelist-roles")
        limit = utils.find_data(guild, "anti-unban-limit")
        logtoggle = utils.find_data(guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass
        
        unbanned_users = []

        async for i in guild.audit_logs(after= datetime.datetime.utcnow() - datetime.timedelta(minutes= 1), action = AuditLogAction.unban):
            unbanned_users.append(i.target)
    

        async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.unban):
            if i.user.id in whitelisted:
                return 
            
            if guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, guild) is True:
                return
            
            if i.user in guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(guild, "unban-audit", i.user.id)
            unbanned_users.append(i.target)
            
            counter = 0
            data = utils.find_data(guild)
            for userID in data['unban-audit']:
                if userID == i.user.id:
                    counter += 1

            if counter == limit:
                if punishment == 'kick':
                    await guild.kick(i.user, reason='Springs Anti-Nuke | Unbanning Members')
                    for target in unbanned_users:
                        try:
                            await guild.ban(target if target != i.user else target, reason='Springs Anti-Nuke | Banning User-Unbanned Members')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Unbanning Members", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await guild.ban(i.user, reason='Springs Anti-Nuke | Unbanning Members')
                    for target in unbanned_users:
                        try:
                            await guild.ban(target if target != i.user else target, reason='Springs Anti-Nuke | Banning User-Unbanned Members')
                        except:
                            pass

                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Unbanning Members", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild=guild, member=i.user, reason='Springs Anti-Nuke | Unbanning Members')
                    for target in unbanned_users:
                        try:
                            await guild.ban(target if target != i.user else target, reason='Springs Anti-Nuke | Banning User-Unbanned Members')
                        except:
                            pass

                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Unbanning Members", action="muted")
                        await logchannel.send(embed=embed)

                    return
            else:
                return
            
    @commands.Cog.listener("on_webhooks_update")
    async def anti_webhook_create(self, channel):
        toggle = utils.find_data(channel.guild, "anti-nuke")
        toggle2 = utils.find_data(channel.guild, "anti-webhook-create")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(channel.guild, "anti-webhook-create-punishment")
        whitelisted = utils.find_data(channel.guild, "whitelist-users")
        whitelist_roles = utils.find_data(channel.guild, "whitelist-roles")
        whitelist_webhooks = utils.find_data(channel.guild, "whitelist-webhook-channels")
        limit = utils.find_data(channel.guild, "anti-webhook-create-limit")
        logtoggle = utils.find_data(channel.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(channel.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        webhooks_created = []

        async for i in channel.guild.audit_logs(after= datetime.datetime.utcnow() - datetime.timedelta(minutes= 1), action = AuditLogAction.webhook_create):
            webhooks_created.append(i.target)

        async for i in channel.guild.audit_logs(limit=1, action=AuditLogAction.webhook_create):
            if i.user.id in whitelisted:
                return 
            
            if channel.guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, channel.guild) is True:
                return
            
            if i.user in channel.guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            if channel.id in whitelist_webhooks:
                return

            utils.upsert_data(channel.guild, "webhook-create-audit", i.user.id)
            webhooks_created.append(i.target)
            
            counter = 0
            data = utils.find_data(channel.guild)
            for userID in data['webhook-create-audit']:
                if userID == i.user.id:
                    counter += 1

            
            if counter == limit:
                if punishment == 'kick':
                    await channel.guild.kick(i.user, reason='Springs Anti-Nuke | Creating Webhooks')
                    for target in webhooks_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Webhooks')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Webhooks", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await channel.guild.ban(i.user, reason='Springs Anti-Nuke | Creating Webhooks')
                    for target in webhooks_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Webhooks')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Webhooks", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(channel.guild, i.user, reason='Springs Anti-Nuke | Creating Webhooks')
                    for target in webhooks_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Webhooks')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Webhooks", action="muted")
                        await logchannel.send(embed=embed)

                    return
            else:
                return  

    @commands.Cog.listener("on_webhooks_update")
    async def anti_webhook_delete(self, channel):
        toggle = utils.find_data(channel.guild, "anti-nuke")
        toggle2 = utils.find_data(channel.guild, "anti-webhook-delete")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(channel.guild, "anti-webhook-delete-punishment")
        whitelisted = utils.find_data(channel.guild, "whitelist-users")
        whitelist_roles = utils.find_data(channel.guild, "whitelist-roles")
        limit = utils.find_data(channel.guild, "anti-webhook-delete-limit")
        logtoggle = utils.find_data(channel.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(channel.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        async for i in channel.guild.audit_logs(limit=1, action=AuditLogAction.webhook_delete):
            if i.user.id in whitelisted:
                return 
            
            if channel.guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, channel.guild) is True:
                return
            
            if i.user in channel.guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(channel.guild, "webhook-delete-audit", i.user.id)
            
            counter = 0
            data = utils.find_data(channel.guild)
            for userID in data['webhook-delete-audit']:
                if userID == i.user.id:
                    counter += 1
            
            if counter == limit:
                if punishment == 'kick':
                    await channel.guild.kick(i.user, reason='Springs Anti-Nuke | Deleting Webhooks')
                    await channel.create_webhook(name="restored_webhook", reason="Springs Anti-Nuke | Restoring User-Deleted Webhooks")
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Webhooks", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await channel.guild.ban(i.user, reason='Springs Anti-Nuke | Deleting Webhooks')
                    await channel.create_webhook(name="restored_webhook", reason="Springs Anti-Nuke | Restoring User-Deleted Webhooks")
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Webhooks", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(channel.guild, i.user, reason='Springs Anti-Nuke | Deleting Webhooks')
                    await channel.create_webhook(name="restored_webhook", reason="Springs Anti-Nuke | Restoring User-Deleted Webhooks")
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Webhooks", action="kicked")
                        await logchannel.send(embed=embed)

                    return
            else:
                return 

    @commands.Cog.listener("on_guild_integrations_update")
    async def anti_integration_create(self, guild):
        toggle = utils.find_data(guild, "anti-nuke")
        toggle2 = utils.find_data(guild, "anti-integration-create")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(guild, "anti-integration-create-punishment")
        whitelisted = utils.find_data(guild, "whitelist-users")
        whitelist_roles = utils.find_data(guild, "whitelist-roles")
        limit = utils.find_data(guild, "anti-integration-create-limit")
        logtoggle = utils.find_data(guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        integrations_created = []

        async for i in guild.audit_logs(after= datetime.datetime.utcnow() - datetime.timedelta(minutes= 1), action = AuditLogAction.integration_create):
            integrations_created.append(i.target)

        async for i in guild.audit_logs(limit=1, action=AuditLogAction.integration_create):
            if i.user.id in whitelisted:
                return 
            
            if guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, guild) is True:
                return
            
            if i.user in guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(guild, "integration-create-audit", i.user.id)
            
            counter = 0
            data = utils.find_data(guild)
            for userID in data['integration-create-audit']:
                if userID == i.user.id:
                    counter += 1

            if counter == limit:
                if punishment == 'kick':
                    await guild.kick(i.user, reason='Springs Anti-Nuke | Creating Integrations')
                    for target in integrations_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Integrations')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Integration", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await guild.ban(i.user, reason='Springs Anti-Nuke | Creating Integrations')
                    for target in integrations_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Integrations')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Integrations", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild, i.user, reason='Springs Anti-Nuke | Creating Integrations')
                    for target in integrations_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Integrations')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Integrations", action="muted")
                        await logchannel.send(embed=embed)

            else:
                return

    
    @commands.Cog.listener("on_guild_integrations_update")
    async def anti_integration_delete(self, guild):
        toggle = utils.find_data(guild, "anti-nuke")
        toggle2 = utils.find_data(guild, "anti-integration-delete")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(guild, "anti-integration-delete-punishment")
        whitelisted = utils.find_data(guild, "whitelist-users")
        whitelist_roles = utils.find_data(guild, "whitelist-roles")
        limit = utils.find_data(guild, "anti-integration-delete-limit")
        logtoggle = utils.find_data(guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        async for i in guild.audit_logs(limit=1, action=AuditLogAction.integration_delete):
            if i.user.id in whitelisted:
                return 
            
            if guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, guild) is True:
                return
            
            if i.user in guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(guild, "integration-delete-audit", i.user.id)
            
            counter = 0
            data = utils.find_data(guild)
            for userID in data['integration-delete-audit']:
                if userID == i.user.id:
                    counter += 1

            
            if counter == limit:
                if punishment == 'kick':
                    await guild.kick(i.user, reason='Springs Anti-Nuke | Deleting Integrations')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Integrations", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await guild.ban(i.user, reason='Springs Anti-Nuke | Deleting Integrations')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Integrations", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild, i.user, reason='Springs Anti-Nuke | Deleting Integrations')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Integrations", action="kicked")
                        await logchannel.send(embed=embed)

                    return
            else:
                return 

    @commands.Cog.listener("on_guild_emojis_update")
    async def anti_emoji_create(self, guild, before, after):
        toggle = utils.find_data(guild, "anti-nuke")
        toggle2 = utils.find_data(guild, "anti-emoji-create")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(guild, "anti-emoji-create-punishment")
        whitelisted = utils.find_data(guild, "whitelist-users")
        whitelist_roles = utils.find_data(guild, "whitelist-roles")
        limit = utils.find_data(guild, "anti-emoji-create-limit")
        logtoggle = utils.find_data(guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        emojis_created = []
        async for i in guild.audit_logs(after= datetime.datetime.utcnow() - datetime.timedelta(minutes = 1), action=AuditLogAction.emoji_create):
            emojis_created.append(i.target)

        async for i in guild.audit_logs(limit=1, action=AuditLogAction.emoji_create):
            if i.user.id in whitelisted:
                return 
            
            if guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, guild) is True:
                return
            
            if i.user in guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(guild, "emoji-create-audit", i.user.id)
            
            counter = 0
            data = utils.find_data(guild)
            for userID in data['emoji-create-audit']:
                if userID == i.user.id:
                    counter += 1

            if counter == limit:
                if punishment == 'ban':
                    await guild.ban(i.user, reason='Springs Anti-Nuke | Creating Emojis')
                    for target in emojis_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Emojis')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Emojis", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'kick':
                    await guild.kick(i.user, reason='Springs Anti-Nuke | Creating Emojis')
                    for target in emojis_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Emojis')
                        except:
                            pass
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Emojis", action="kicked")
                        await logchannel.send(embed=embed)

                if punishment == 'mute':
                    await utils.mute(guild, i.user, reason='Springs Anti-Nuke | Creating Emojis')
                    for target in emojis_created:
                        try:
                            await target.delete(reason='Springs Anti-Nuke | Deleting User-Created Emojis')
                        except:
                            pass
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Creating Emojis", action="muted")
                        await logchannel.send(embed=embed)

            else:
                return


    @commands.Cog.listener("on_guild_emojis_update")
    async def anti_emoji_delete(self, guild, before, after):
        toggle = utils.find_data(guild, "anti-nuke")
        toggle2 = utils.find_data(guild, "anti-emoji-delete")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(guild, "anti-emoji-delete-punishment")
        whitelisted = utils.find_data(guild, "whitelist-users")
        whitelist_roles = utils.find_data(guild, "whitelist-roles")
        limit = utils.find_data(guild, "anti-emoji-delete-limit")
        logtoggle = utils.find_data(guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass



        async for i in guild.audit_logs(limit=1, action=AuditLogAction.emoji_delete):
            if i.user.id in whitelisted:
                return 
            
            if guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, guild) is True:
                return
            
            if i.user in guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(guild, "emoji-delete-audit", i.user.id)
            
            counter = 0
            data = utils.find_data(guild)
            for userID in data['emoji-delete-audit']:
                if userID == i.user.id:
                    counter += 1

            if counter == limit:
                if punishment == 'ban':
                    await guild.ban(i.user, reason='Springs Anti-Nuke | Deleting Emojis')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Emojis", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'kick':
                    await guild.kick(i.user, reason='Springs Anti-Nuke | Deleting Emojis')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Emojis", action="kicked")
                        await logchannel.send(embed=embed)

                if punishment == 'mute':
                    await utils.mute(guild, i.user, reason='Springs Anti-Nuke | Deleting Emojis')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Deleting Emojis", action="muted")
                        await logchannel.send(embed=embed)

            else:
                return

    @commands.Cog.listener("on_guild_update")
    async def anti_widget_edit(self, before, after):
        toggle = utils.find_data(before, "anti-nuke")
        toggle2 = utils.find_data(before, "anti-widget-create")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(before, "anti-widget-create-punishment")
        whitelisted = utils.find_data(before, "whitelist-users")
        whitelist_roles = utils.find_data(before, "whitelist-roles")
        logtoggle = utils.find_data(before, "logging")
        if logtoggle is True:
            channelID = utils.find_data(before, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        if before.widget != after.widget:
            async for i in after.audit_logs(limit=1, action=AuditLogAction.guild_update):
                if i.user.id in whitelisted:
                    return 
                
                if after.owner == i.user:
                    return

                if i.user.id == bot_id:
                    return

                if utils.is_owner(i.user, after) is True:
                    return
                
                if i.user in after.members:
                    for role in i.user.roles:
                        if role.id in whitelist_roles:
                            return
                
                if punishment == 'ban':
                    await after.ban(i.user, reason='Springs Anti-Nuke | Changing Widget')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Widget", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'kick':
                    await after.kick(i.user, reason='Springs Anti-Nuke | Changing Widget')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Widget", action="kicked")
                        await logchannel.send(embed=embed)

                if punishment == 'mute':
                    await utils.mute(after, i.user, reason='Springs Anti-Nuke | Changing Widget')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Widget", action="muted")
                        await logchannel.send(embed=embed)
        else:
            return

    @commands.Cog.listener("on_guild_update")
    async def anti_name_change(self, before, after):
        toggle = utils.find_data(before, "anti-nuke")
        toggle2 = utils.find_data(before, "anti-name-change")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(before, "anti-name-change-punishment")
        whitelisted = utils.find_data(before, "whitelist-users")
        whitelist_roles = utils.find_data(before, "whitelist-roles")
        logtoggle = utils.find_data(before, "logging")
        if logtoggle is True:
            channelID = utils.find_data(before, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        if before.name != after.name:
            async for i in after.audit_logs(limit=1, action=AuditLogAction.guild_update):
                if i.user.id in whitelisted:
                    return 
                
                if after.owner == i.user:
                    return

                if i.user.id == bot_id:
                    return

                if utils.is_owner(i.user, after) is True:
                    return
                
                if i.user in after.members:
                    for role in i.user.roles:
                        if role.id in whitelist_roles:
                            return
                
                if punishment == 'ban':
                    await after.ban(i.user, reason='Springs Anti-Nuke | Changing Guild Name')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Guild Name", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'kick':
                    await after.kick(i.user, reason='Springs Anti-Nuke | Changing Guild Name')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Guild Name", action="kicked")
                        await logchannel.send(embed=embed)

                if punishment == 'mute':
                    await utils.mute(after, i.user, reason='Springs Anti-Nuke | Changing Guild Name')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Guild Name", action="muted")
                        await logchannel.send(embed=embed)
        else:
            return


    @commands.Cog.listener("on_member_join")
    async def anti_bot(self, member):
        toggle = utils.find_data(member.guild, "anti-bot")
        if toggle is not True:
            return
        punishment = utils.find_data(member.guild, "anti-bot-punishment")
        whitelisted = utils.find_data(member.guild, "whitelist-users")
        whitelist_roles = utils.find_data(member.guild, "whitelist-roles")
        logtoggle = utils.find_data(member.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(member.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        if member.bot:
            async for i in member.guild.audit_logs(limit=1, action=AuditLogAction.bot_add):
                if i.user.id in whitelisted:
                    return 
                
                if member.guild.owner == i.user:
                    return

                if i.user.id == bot_id:
                    return

                if utils.is_owner(i.user, member.guild) is True:
                    return
                
                if i.user in member.guild.members:
                    for role in i.user.roles:
                        if role.id in whitelist_roles:
                            return

                if punishment == 'ban':
                    await member.guild.ban(i.user, reason='Springs Anti-Nuke | Added Unknown Bot')
                    await member.guild.ban(member, reason='Springs Anti-Nuke | Unknown Bot')
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Adding Unknown Bot", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'kick':
                    await member.guild.kick(i.user, reason='Springs Anti-Nuke | Added Unknown Bot')
                    await member.guild.ban(member, reason='Springs Anti-Nuke | Unknown Bot')
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Added Unknown Bot", action="kicked")
                        await logchannel.send(embed=embed)

                if punishment == 'mute':
                    await utils.mute(member.guild, i.user, reason='Springs Anti-Nuke | Added Unknown Bot')
                    await member.guild.ban(member, reason='Springs Anti-Nuke | Unknown Bot')
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Added Unknown Bot", action="muted")
                        await logchannel.send(embed=embed)

            else:
                return

    @commands.Cog.listener("on_member_remove")
    async def anti_kick(self, member):
        toggle = utils.find_data(member.guild, "anti-nuke")
        toggle2 = utils.find_data(member.guild, "anti-kick")
        if toggle is not True or toggle2 is not True:
            return
        limit = utils.find_data(member.guild, "anti-kick-limit")
        punishment = utils.find_data(member.guild, "anti-kick-punishment")
        whitelisted = utils.find_data(member.guild, "whitelist-users")
        whitelist_roles = utils.find_data(member.guild, "whitelist-roles")
        logtoggle = utils.find_data(member.guild, "logging")
        if logtoggle is True:
            channelID = utils.find_data(member.guild, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        async for i in member.guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
            if i.user.id in whitelisted:
                return 
            
            if member.guild.owner == i.user:
                return

            if i.user.id == bot_id:
                return

            if utils.is_owner(i.user, member.guild) is True:
                return
            
            if i.user in member.guild.members:
                for role in i.user.roles:
                    if role.id in whitelist_roles:
                        return

            utils.upsert_data(member.guild, "kick-audit", i.user.id)

            counter = 0
            data = utils.find_data(member.guild)
            for userID in data['kick-audit']:
                if userID == i.user.id:
                    counter += 1

            if counter == limit:
                if punishment == 'kick':
                    await member.guild.kick(i.user, reason='Springs Anti-Nuke | Kicking Members')
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Kicking Members", action="kicked")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'ban':
                    await member.guild.ban(i.user, reason='Springs Anti-Nuke | Kicking Members')
                    
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Kicking Members", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'mute':
                    await utils.mute(guild=member.guild, member=i.user, reason='Springs Anti-Nuke | Kicking Members')

                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Kicking Members", action="muted")
                        await logchannel.send(embed=embed)

                    return

    @commands.Cog.listener("on_guild_update")
    async def anti_vanity(self, before, after):
        toggle = utils.find_data(before, "anti-nuke")
        toggle2 = utils.find_data(before, "anti-vanity")
        if toggle is not True or toggle2 is not True:
            return
        punishment = utils.find_data(before, "anti-vanity-punishment")
        whitelisted = utils.find_data(before, "whitelist-users")
        whitelist_roles = utils.find_data(before, "whitelist-roles")
        logtoggle = utils.find_data(before, "logging")
        if logtoggle is True:
            channelID = utils.find_data(before, "log-channel")
            logchannel = self.bot.get_channel(id=channelID)
        else:
            pass

        if await before.vanity_invite() != await after.vanity_invite():
            async for i in after.audit_logs(limit=1, action=AuditLogDiff.vanity_url_code):
                if i.user.id in whitelisted:
                    return 
                
                if after.owner == i.user:
                    return

                if i.user.id == bot_id:
                    return

                if utils.is_owner(i.user, after) is True:
                    return
                
                if i.user in after.members:
                    for role in i.user.roles:
                        if role.id in whitelist_roles:
                            return
                
                if punishment == 'ban':
                    await after.ban(i.user, reason='Springs Anti-Nuke | Changing Vanity')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Vanity", action="banned")
                        await logchannel.send(embed=embed)

                    return

                if punishment == 'kick':
                    await after.kick(i.user, reason='Springs Anti-Nuke | Changing Vanity')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Vanity", action="kicked")
                        await logchannel.send(embed=embed)

                if punishment == 'mute':
                    await utils.mute(after, i.user, reason='Springs Anti-Nuke | Changing Vanity')
                    if logtoggle is True:
                        if logchannel is None:
                            return
                        embed = utils.format_logs(user=i.user, reason="Changing Vanity", action="muted")
                        await logchannel.send(embed=embed)
        else:
            return

    

def setup(bot):
    bot.add_cog(Antinuke(bot))