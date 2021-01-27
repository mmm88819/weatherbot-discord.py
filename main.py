import asyncio

import discord
from discord.ext import commands
import math

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Bot is ready. ")


@client.command()
async def weather(ctx, *args):
    author = ctx.message.author
    if len(args) == 0:
        await ctx.send("*NOTE: If you'd rather prefer to use a text version of this command, please use !weather text instead. (This might work better on lower-resolution screens.)*")
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
        wrld_map = await ctx.send('''
`For North America, react with 🐶.
For South America, react with 🥎.
For Europe, react with ⚽.
For Africa, react with 💎.
For Asia, react with 🏓.
For Australia and Oceania, react with 🎱.`''')
    emojis = ['🐶', '🥎', '⚽', '💎', '🏓', '🎱']
    for emoji in emojis:
        await wrld_map.add_reaction(emoji)
    try:
        reaction, user = await client.wait_for('reaction_add', check=lambda reaction, user: user == author, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send('`No reaction from user in 30 seconds. Please invoke the command again if you wish to proceed.`')
    else:
        if reaction=='🐶':
            na()
        if reaction=='🥎':
            na()
        if reaction=='⚽':
            na()
        if reaction=='💎':
            na()
        if reaction=='🏓':
            na()
        if reaction=='🎱':
            na()

token = 'NzkzNTU3NjAyMDQyNzczNTI0.X-uAGw.gpAcl5YC1Sdgr3cJ46PSWrSrLFg'
def na():
    pass
def sa():
    pass
def eu():
    pass
def afr():
    pass
def asia():
    pass
def oce():
    pass
client.run(token)
