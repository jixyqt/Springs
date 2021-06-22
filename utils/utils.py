import datetime
from discord.ext.commands.errors import MissingRequiredArgument
import pymongo
import json
import os
import discord
from discord.ext import commands
import os
import logging

# Third party libraries
import textwrap
from traceback import format_exception
import discord
from discord.ext import commands
from asyncio.tasks import wait
from os import waitpid
from typing import Awaitable

import time
import discord, os, sys, json, random, string, requests, subprocess, ctypes
from pymongo.topology import _is_stale_server_description
from discord import colour
from discord import user
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
from discord import Permissions
from colorama import Fore, init
import datetime
import re
import time
import pymongo
from pymongo import MongoClient
import discord
import aiohttp
from discord.utils import get
import io

from discord.ext.commands import CommandNotFound

import discord
from pathlib import Path

from discord.ext import commands
import asyncio
import requests
import re

with open('./jsons/config.json', 'r') as f:
    config = json.load(f)


mongo_url = config["mongo"]
mongo = pymongo.MongoClient(mongo_url,tls=True, tlsAllowInvalidCertificates=True)
db = mongo.get_database("Springs").get_collection("GuildData")
blacklist = mongo.get_database("Springs").get_collection("blacklist")
bot_id = 842899285141225484

class utils:

    @classmethod
    async def create_guild(self, guild : discord.Guild):
        db.insert_one({
            #Whitelist
            "whitelist-users": [guild.owner_id, bot_id],
            "whitelist-roles": [],
            "whitelist-invite-channels": [],
            "whitelist-link-channels": [],
            "whitelist-webhook-channels": [],
            "owners": [guild.owner_id],
            "owner-roles": [],
            "admins": [member.id for member in guild.members if member.guild_permissions.administrator],
            "admin-roles": [role.id for role in guild.roles if role.permissions.administrator],
            "auto-roles": [],
            "blacklist-words": [],
            
            #Guild Data
            "prefix": ">",
            "guild_id": guild.id,
            "guild_name": guild.name,
            "vanity_url": None if guild.premium_tier == 3 else None,
            
            #Toggles
            "anti-ban": True,
            "anti-nuke": True,
            "anti-unban": True,
            "anti-kick": True,
            "anti-name-change": True,
            "anti-vanity": True,
            "anti-channel-create": True,
            "anti-channel-delete": True,
            "anti-role-create": True,
            "anti-role-delete": True,
            "anti-webhook-create": True,
            "anti-webhook-delete": True,
            "anti-permissions": True,
            "anti-emoji-create": True,
            "anti-emoji-delete": True,
            "anti-widget-create": True,
            "anti-widget-delete": True,
            "anti-integration-create": True,
            "anti-integration-delete": True,
            "anti-spam": True,
            "anti-link": True,
            "anti-invite": True,
            "anti-bot": True,
            "logging": True,
            "message-logging": True,
            "voice-logging": True,
            "server-logging": True,
            "mod-logging": True,
            "user-logging": False,
            "welcoming": False,
            "boosting": False,
            "leaving": False,

            #Limits
            "anti-ban-limit": 1,
            "anti-unban-limit": 1,
            "anti-kick-limit": 1, 
            "anti-channel-create-limit": 1,
            "anti-channel-delete-limit": 1,
            "anti-role-create-limit": 1,
            "anti-role-delete-limit": 1,
            "anti-webhook-create-limit": 1,
            "anti-webhook-delete-limit": 1,
            "anti-widget-create-limit": 1,
            "anti-widget-delete-limit": 1,
            "anti-integration-create-limit": 1,
            "anti-integration-delete-limit": 1,
            "anti-emoji-create-limit": 1,
            "anti-emoji-delete-limit": 1,
            "anti-permissions-limit" : "manage_roles",
            "anti-spam-limit": 10,
            
            #Logging
            "log-channel": None,
            "welcome-channel": None,
            "boost-channel": None,
            "leave-channel": None,
            "boost-message": None,
            "welcome-message": None,
            "leave-message": None,
            "boost-message": None,
            "welcome-embed": False,
            "boost-embed": False,
            "leave-embed": False,
            

            #Audits
            "ban-audit": [],
            "unban-audit": [],
            "kick-audit": [],
            "channel-create-audit": [],
            "channel-delete-audit": [],
            "role-create-audit": [],
            "role-delete-audit": [],
            "webhook-create-audit": [],
            "webhook-delete-audit": [],
            "emoji-create-audit": [],
            "emoji-delete-audit": [],
            "widget-create-audit": [],
            "widget-delete-audit": [],
            "integration-create-audit": [],
            "integration-delete-audit": [],
            "spam-audit": [],

            #Punishments
            "anti-ban-punishment": 'ban',
            "anti-unban-punishment": 'ban',
            "anti-kick-punishment": 'ban', 
            "anti-channel-create-punishment": 'ban',
            "anti-channel-delete-punishment": 'ban',
            "anti-role-create-punishment": 'ban',
            "anti-role-delete-punishment": 'ban',
            "anti-webhook-create-punishment": 'ban',
            "anti-webhook-delete-punishment": 'ban',
            "anti-widget-create-punishment": 'ban',
            "anti-widget-delete-punishment": 'ban',
            "anti-integration-create-punishment": 'ban',
            "anti-integration-delete-punishment": 'ban',
            "anti-emoji-create-punishment": 'ban',
            "anti-emoji-delete-punishment": 'ban',
            "anti-permissions-punishment" : "ban",
            "anti-spam-punishment": 'mute',
            "anti-name-change-punishment": 'ban',
            "anti-vanity-punishment": 'ban',
            "anti-bot-punishment": 'ban',
            "anti-invite-punishment": 'mute',
            "anti-link-punishment": 'mute'

        })

    """A simple utility class for all functions that will be used in the bot."""
    @classmethod
    def read_json(self, path, data):
        """A simple json reading function."""
        with open(f"{path}.json", 'r') as f:
            result =json.load(f)
            
        return result[f"{data}"]
    
    @classmethod
    def create_embed(self, text):
        embed = discord.Embed(
            description=text,
            colour=0x5865f2,
        )
        return embed

    @classmethod
    def msg_contains_word(self, msg, word):
        return re.search(fr'\b({word})\b', msg) is not None 

    @classmethod
    def clear(self, guild: discord.Guild, value: str):
        data = self.find_data(guild, value)
        try:
            for index in data:
                if index != guild.owner_id:
                    db.update_one({"guild_id": guild.id}, {"$pull": {value: index}})
                else:
                    pass
        except:
            raise KeyError
    

    @classmethod
    def is_whitelisted(self, member: discord.Member):
        """Checks to see if a user is whitelisted."""
        if member.id in db.find_one({"guild_id": member.guild.id})["whitelisted"]:
            return True
        else:
            return False
    
    @classmethod
    def format_logs(self, user, reason, action):
        embed = discord.Embed(title="<:Bell:852619072692551751> Anti-Nuke Triggered", color=0x5865f2, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="<:Cpu:854516106127605821> User:", value=user.mention, inline=False)
        embed.add_field(name="<:News:852619060427358218> Reason:", value=f"`{reason}`", inline=False)
        embed.add_field(name="<:Banned:851939261729079357> Action Taken:", value=f"`{action}`", inline=False)
        return embed

    @classmethod
    def format_modlogs(self, user, reason, action):
        embed = discord.Embed(title="<:Bell:852619072692551751> Moderation Triggered", color=0x5865f2, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="<:Cpu:854516106127605821> User:", value=user.mention, inline=False)
        embed.add_field(name="<:News:852619060427358218> Reason:", value=f"`{reason}`", inline=False)
        embed.add_field(name="<:Banned:851939261729079357> Action Taken:", value=f"`{action}`", inline=False)
        return embed

    @classmethod
    def is_admin(self, member: discord.Member or discord.User, guild: discord.Guild = None):
        """Checks to see if a user is an admin."""
        if member is discord.Member or guild is None:
            if member.id in db.find_one({"guild_id": member.guild.id})["admins"] or member.guild_permissions.administrator:
                return True
            else:
                return False
        if member is discord.User:
            if member.id in db.find_one({"guild_id": guild.id})["admins"]:
                return True
            else:
                return False 
        
    
    @classmethod
    def is_owner(self, member: discord.User or discord.Member, guild: discord.Guild=None):
        """Checks to see if a user is an owner."""
        if member is discord.Member or guild is None:
            if member.id in db.find_one({"guild_id": member.guild.id})["owners"]:
                return True
            else:
                return False

        if member is discord.User:
            if member.id in db.find_one({"guild_id": guild.id})["owners"]:
                return True
            else:
                return False
           

    @classmethod
    def is_guild_owner(self, guild: discord.Guild, user: discord.Member):
        """Checks to see if a user is the guild owner."""
        if user.id == guild.owner_id:
            return True
        else:
            return False

    @classmethod
    async def mute(self, guild: discord.Guild, member: discord.Member, reason=None):
        muted = discord.utils.get(guild.roles, name="Muted")
        if not muted:
            muted = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(muted, speak=False, send_messages=False, read_message_history=True, read_messages=True, connect=False)
        if reason == None:
            reason = f"{self.bot.user.name} | Mute"

        else:
            if muted in member.roles:
                return 
            else: 
                if len(member.roles) == 0:
                    pass
                else:
                    try:
                        for role in member.roles:
                            await member.remove_roles(role, reason=reason)
                    except:
                        pass
                
                await member.add_roles(muted, reason=reason)


    @classmethod
    def has_modlogs(self, guild: discord.Guild):
        if bool(db.find_one({"guild_id": guild.id})["logging"]) is True and db.find_one({"guild_id": guild.id})["log-channel"] is not None:
            return True
        else:
            return False

    @classmethod
    def set_data(self, typeKey: str, guild: discord.Guild, index: str, value):
        """Sets the data in a database."""
        db.update_one({"guild_id": guild.id}, {typeKey: {index: value}})

    @classmethod
    def find_data(self, guild: discord.Guild, value: str = None):
        """Finds specific data in a database."""
        if value is not None:
            return db.find_one({"guild_id": guild.id})[value]
        else:
            return db.find_one({"guild_id": guild.id})

    @classmethod
    def contains(self, object: discord.Role or discord.User or discord.TextChannel, guild: discord.Guild, value: str):
        if object.id in db.find_one({"guild_id": guild.id})[value]:
            return True
        else:
            return False
    
    @classmethod
    def set_toggle(self, typeKey: str, guild: discord.Guild, index: str, value: bool):
        """Sets the toggle in a database."""
        db.update_one({"guild_id": guild.id}, {typeKey: {index: value}})

    @classmethod
    def upsert_data(self, guild: discord.Guild, index: str, id):
        db.update_one({"guild_id": guild.id}, {"$push": {index: id }})
    
    @classmethod
    def pull_data(self, guild: discord.Guild, index: str, id):
        db.update_one({"guild_id": guild.id}, {"$pull": {index: id }})

    @classmethod
    def delete_guild(self, guild: discord.Guild):
        """Deletes the guild from selected database."""
        db.delete_one({"guild_id": guild.id})

    @classmethod
    def has_messagelogs(self, guild: discord.Guild):
        if utils.find_data(guild, "message-logging") is True and utils.find_data(guild, "logging") is True:
            return True
        elif utils.find_data(guild, "log-channel") is None:
            return False
        else:
            return False


    @classmethod
    def has_modlogs(self, guild: discord.Guild):
        if utils.find_data(guild, "mod-logging") is True and utils.find_data(guild, "logging") is True:
            return True
        elif utils.find_data(guild, "log-channel") is None:
            return False
        else:
            return False


    @classmethod
    def has_voicelogs(self, guild: discord.Guild):
        if utils.find_data(guild, "voice-logging") is True and utils.find_data(guild, "logging") is True:
            return True
        elif utils.find_data(guild, "log-channel") is None:
            return False
        else:
            return False


    @classmethod
    def has_serverlogs(self, guild: discord.Guild):
        if utils.find_data(guild, "server-logging") is True and utils.find_data(guild, "logging") is True:
            return True
        elif utils.find_data(guild, "log-channel") is None:
            return False
        else:
            return False


    @classmethod
    def has_userlogs(self, guild: discord.Guild):
        try:
            if utils.find_data(guild, "user-logging") is True and utils.find_data(guild, "logging") is True:
                return True
            if utils.find_data(guild, "log-channel") is None:
                return False
            else:
                return False
        except:
            return False

    @classmethod
    def make_request(self, type: str, url, headers=None, json=None):
        """Sends a get request."""
        if type == "GET" or "get":
            if headers is None or json is None:
                return requests.get(url)
            else:
                return requests.get(url, headers={'Authorization': f"Bot + {headers}"}, json=json)
        
        elif type == "POST" or "post":
            if headers is None or json is None:
                requests.post(url)
            else:
                requests.post(url, header={'Authorization': f"Bot + {headers}"}, json=json)

        elif type == "Put" or "put":
            if headers is None or json is None:
                requests.put(url)
            else:
                requests.put(url, header={'Authorization': f"Bot + {headers}"}, json=json)
        else:
            raise MissingRequiredArgument or AttributeError

    @classmethod
    def get_response(self, type: str, url, headers=None, json=None):
        """Sends a get request with the response."""
        if type == "GET" or "get":
            if headers is None or json is None:
                return requests.get(url).json()
            else:
                return requests.get(url, headers={'Authorization': f"Bot + {headers}"}, json=json).json()
        else:
            raise MissingRequiredArgument or AttributeError

    @classmethod
    def setup(self, bot: commands.AutoShardedBot):
        """Loads all bot cogs."""
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py') or '__pycache__' not in filename:
                bot.load_extension(f'cogs.{filename[:-3]}')
            else:
                print(f'Unable to load {filename[:-3]}')

    @classmethod
    async def get_prefix(self, bot, message):
        """Gets the bot prefix."""
        if message.guild:
            try:
                prefix = db.find_one({"guild_id": message.guild.id})["prefix"]
                return commands.when_mentioned_or(prefix, '>', '$')(bot, message)
            except(KeyError, AttributeError, TypeError):
                return commands.when_mentioned_or('>','$')(bot, message)
        else:
            return commands.when_mentioned_or('>', '$')(bot, message)

    @classmethod
    async def status_task(self, bot: commands.AutoShardedBot):
        """A simple status task loop."""
        while True:
            count = 0 
            for g in bot.guilds:
                count += len(g.members) 

            activity3 = discord.Game(name=">help")

            await bot.change_presence(status=discord.Status.online, activity=activity3)

            await asyncio.sleep(8)
            activity4 = discord.Game(name="discord.gg/springs")

            await bot.change_presence(status=discord.Status.online, activity=activity4)

            await asyncio.sleep(8)
            activity5 = discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} Guilds {count} Users | >info")
            await bot.change_presence(status=discord.Status.online, activity=activity5)

            await asyncio.sleep(8)
            activity6 = discord.Game(name=f">setup")
            await bot.change_presence(status=discord.Status.online, activity=activity6)

            await asyncio.sleep(8)

