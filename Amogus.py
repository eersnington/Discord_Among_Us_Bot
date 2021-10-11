import discord
import random
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
from discord.ext import commands

client = commands.Bot(command_prefix='amb ')
client.remove_command('help')

guide_urls = {
    "crewmate": "https://www.reddit.com/r/AmongUs/comments/gg5oo1/among_usdetective_guide_101/?utm_source=share&utm_medium=web2x&context=3",
    "impostor": "https://www.reddit.com/r/AmongUs/comments/gfulqt/effort_post_complete_guide_to_playing_as_impostor/",
    "gameplay": "https://www.reddit.com/r/AmongUs/comments/iin01b/among_us_set_up_and_gameplay_guide_for_both/",
    "map1": "https://i.redd.it/tv8ef4iqszh41.png",
    "map2": "https://i.redd.it/8i1kd1mp9ij51.png",
    "map3": "https://i.imgur.com/YWH8hvg.jpg",
    "map4": "https://i.imgur.com/VBsnIVE.jpg"
}
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="Among Us"))

@client.command(pass_context=True)
async def test(ctx):
    await ctx.send(f'When the impostor is SUS... AMOGUS {ctx.author.mention}')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="List of Commands", description=f"More functionality than ",  color=discord.Color.gold())
    embed.add_field(name='📚 Guide', value='``amb guide help``', inline=True)
    embed.add_field(name='🤨 Sus', value='``amb sus {tag}``', inline=True)
    embed.add_field(name='🔍 Wiki', value='``amb wiki {search query}``', inline=True)
    embed.add_field(name='🎲 Game', value='``amb newgame {code} {server loc}``', inline=True)
    embed.add_field(name='🤫 Game', value='``amb mute (while in a voice channel)``', inline=True)
    embed.add_field(name='🎙️ Game', value='``amb unmute (while in a voice channel) ``', inline=True)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def guide(ctx, args):
    if args == "help":
        embed = discord.Embed(title="Command Usage",description="Brain size: Ooof", color=discord.Color.gold())
        embed.add_field(name='🕵️️ Crewmate Tips', value='``amb guide crewmate``', inline=True)
        embed.add_field(name='🗡️ Impostor Tips', value='``amb guide impostor``', inline=True)
        embed.add_field(name='🕹️ Complete Gameplay Guide', value='``amb guide gameplay``', inline=True)
        embed.add_field(name='🚀 The Skeld Map', value='``amb guide map1``', inline=True)
        embed.add_field(name='🏢 Mira HQ Map', value='``amb guide map2``', inline=True)
        embed.add_field(name='🏜️ Polus Map', value='``amb guide map3``', inline=True)
        embed.add_field(name='🏜️ Airship Map', value='``amb guide map4``', inline=True)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    if args == "crewmate":
        embed = discord.Embed(title= "Crewmate Guide",
                              description="Read through this reddit guide to become an epic gamer crewmate.",
                              color=discord.Color.blue(), url=guide_urls[args])
        embed.set_footer(icon_url=ctx.author.avatar_url, text= f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    if args == "impostor":
        embed = discord.Embed(title= "Impostor Guide",
                              description="Read through this reddit guide to become an epic gamer impostor.",
                              color=discord.Color.red(), url=guide_urls[args])
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    if args == "gameplay":
        embed = discord.Embed(title= "Complete Gameplay Guide",
                              description="Read through this reddit guide to set up epic games.",
                              color=discord.Color.green(), url=guide_urls[args])
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    if args == "map1":
        embed = discord.Embed(title= "The Skeld Guide", color=discord.Color.gold())
        embed.set_image(url=guide_urls[args])
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    if args == "map2":
        embed = discord.Embed(title= "Mira HQ Guide", color=discord.Color.gold())
        embed.set_image(url=guide_urls[args])
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    if args == "map3":
        embed = discord.Embed(title= "Polus Guide", color=discord.Color.gold())
        embed.set_image(url=guide_urls[args])
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    if args == "map4":
        embed = discord.Embed(title= "Airship Guide", color=discord.Color.gold())
        embed.set_image(url=guide_urls[args])
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def sus(ctx):
    msg_file = open('messages/sus.txt', 'r')
    embed = discord.Embed(title="",
                          description=f"{random.choice(msg_file.readlines())}",
                          color=discord.Color.gold())
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    msg_file.close()

@client.command(pass_context=True)
async def wiki(ctx, *, query):
    query = query.replace(' ', '+')
    res = requests.get("https://among-us.fandom.com/wiki/Special:Search?query=" + str(query))
    soup = bs(res.text, "html.parser")
    for link in soup.find_all():
        for i in range(1):
            url = link.get("href", "")
            if ("https://among-us.fandom.com/wiki/") in url and ("https://among-us.fandom.com/wiki/Special:Search?scope=") not in url:
                await ctx.send(url)
                return

@client.command(pass_context=True)
async def newgame(ctx, arg1, *, arg2):
    if len(arg1) != 6 or not arg1.isalpha():
        await ctx.send("Error, incorrect lobby code syntax")
        return
    now = datetime.now()
    now = now.strftime("%b-%d-%Y %H:%M")

    await ctx.send('@everyone')
    embed = discord.Embed(title="NEW AMONG US MATCH", description=f"{now}",  color=discord.Color.gold())
    embed.add_field(name='Code', value=f'``{arg1.upper()}``', inline=False)
    embed.add_field(name='Server', value=f'``{arg2}``', inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def mute(ctx):
    try:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    except:
        discord.Embed(title="Error", description=f"You did something wrong",
                      color=discord.Color.gold())
        return
    for member in channel.members:
        await member.edit(mute=True)
    embed = discord.Embed(title="MUTED", description="Everyone is now muted.", color=discord.Color.gold())
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def unmute(ctx):
    channel = ctx.message.author.voice.channel
    for member in channel.members:
        await member.edit(mute=False)
    embed = discord.Embed(title="UNMUTED", description="Everyone is now unmuted.", color=discord.Color.gold())
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="", description=f"Error. Try ``amb help``. ({error})",
                          color=discord.Color.gold())
    await ctx.send(embed=embed)

client.run("")

