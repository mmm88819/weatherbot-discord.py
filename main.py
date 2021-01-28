import asyncio

import discord
from discord.ext import commands
import math

client = commands.Bot(command_prefix='!')

with open('discord-token.txt', 'r') as f:
    discordtoken = f.read()
with open('weatherapi-token.txt', 'r') as f:
    weathertoken = f.read()


@client.event
async def on_ready():
    print("Bot is ready. ")


@client.command()
async def weather(ctx, *args):
    author = ctx.message.author
    picksglobal = {
        'North America': '🐶',
        'South America': '🥎',
        'Europe': '⚽',
        'Africa': '💎',
        'Asia': '🏓',
        'Australia & Oceania': '🎱'
    }

    if len(args) == 0:
        await ctx.send(
            "*NOTE: If you'd rather prefer to use a text version of this command, please use !weather text instead. (This might work better on lower-resolution screens.)*")
        wiad = '`Pick the continent you want to check the weather in with an emote: `'
        await ctx.send(wiad)
        wrld_map = await ctx.send('''.                                                               ▄                 ████▀                                             ▄▄▄▄▄▄▄▄
                          ▄▄██████████▀▀    █      ▄█▀▀    ▄           ▄█▀█▄▄▄███████████████████▄
                         ▀▀   ▀███████▄    ▄█▄                            ▄▄  ▀▀  ████████████████████▀▀
                                      ███🐶██████▀▀                          ▀██⚽█▀▀█▀▀███████████████   ▄
                                   █████████▀                                    ██ ▄▄▀  ▀  ▀▀██   ████████🏓██▀▀█   █
                                   █ ███▀▀█                                          ▄█████▄███████████████████▄     ▀
                                        ▀█▄▄    ▄▄                                   ██████████▄ ▀██▀     ▀███▀▀██▀▀
                                                ▀█                                         ▀███████████▄ ▀               █▀         █▀        ▀
                                                      ▀████▄                           ▀▀▀▀███💎███▀                  ▀          █      ▄    ▀
                                                       ███████▄▄                              ▀█████▀                                      █   ▀           ▀█▄
                                                        ▀███████▀                                █████     ▄                                                ▄▄    ▄
                                                            ▀██🥎█▀                                 ▀████    █                                        ▄▄█████▄
                                                               ████                                           ██▀                                                   ████🎱█▀
                                                               ██▀                                                                                                                        ▀█
                                                                 █▄''')
    elif args[0] == 'text':
        wrld_map = ''
        for continent in list(picksglobal.keys()):
            wrld_map += '`For ' + continent + ', react with ' + picksglobal[continent] + '.` \n'
        wrld_map = await ctx.send(wrld_map)
    else:
        await ctx.send('Wrong argument specified. Please invoke command again')

    for continent in picksglobal:
        await wrld_map.add_reaction(picksglobal[continent])
    try:
        reaction, user = await client.wait_for('reaction_add', check=lambda reaction, user: user == author, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send('`No reaction from user in 30 seconds. Please invoke the command again if you wish to proceed.`')
    else:
        pass


client.run(discordtoken)
