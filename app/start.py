import discord
from discord.ext import commands
from db import Database
from datetime import datetime
import datetime as dt
import asyncio
import os

bot = commands.Bot(command_prefix='&')


@bot.command()
async def roles(ctx):
    embed = discord.Embed()
    embed.title = "Roles"
    embed.description = "Get your roles"
    embed.add_field(name=":one:", value="Section 201", inline=False) 
    embed.add_field(name=":two:", value="Section 202", inline=False) 
    embed.add_field(name=":three:", value="Section 203", inline=False) 
    embed.add_field(name=":four:", value="Section 204", inline=False) 
    embed.add_field(name=":six:", value="Section 206", inline=False) 
    embed.add_field(name=":notebook:", value="Homework Reminder", inline=False)
    embed.add_field(name=":lab_coat:", value="Lab Report/ Prelab Reminder", inline=False)
    msg = await ctx.send(embed=embed)
async def add_role(user, role):
    await user.add_roles(discord.utils.get(user.guild.roles, name=role))

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "1️⃣":
        await add_role(user, "201")
    elif reaction.emoji == "2️⃣":
        await add_role(user, "202")
    elif reaction.emoji == "3️⃣":
        await add_role(user, "203")
    elif reaction.emoji == "4️⃣":
        await add_role(user, "204")
    elif reaction.emoji == "6️⃣":
        await add_role(user, "206")
    elif reaction.emoji == "🥼":
        await add_role(user, "Lab")
    elif reaction.emoji == "📓":
        await add_role(user, "Homework")
    
@bot.command()
async def add_homework(ctx, arg1, arg2):
    database = Database()
    embed = discord.Embed()
    homework = {"name" :arg1, "date" : arg2}
    database.add_homework(homework)
    embed.add_field(name="📓", value="Homework added due "+arg2)
    await ctx.send(embed=embed)

@bot.command()
async def get_homework(ctx):
    database = Database()
    embed = discord.Embed()
    homeworks = database.get_homeworks()
    embed.title = "Homeworks"
    embed.description = "Look at you! You really love homework don't you?"
    for homework in homeworks:
        embed.add_field(name=homework[0], value=homework[1], inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def remind_homework(ctx):
    while True:
        await asyncio.sleep(60*60)
        database = Database()
        for homework in database.get_homeworks():
            try:
                due = datetime.strptime(homework[1],  "%d/%m/%y %H:%M:%S")
                if (due - dt.timedelta(days=-1) > datetime.now() and homework[2] == 0):
                    await ctx.send("<@&937900368002678784>")
                    embed = discord.Embed(title="📓 Reminder")
                    embed.add_field(name=homework[0], value=homework[1])
                    database.update_notify(homework[0])
                    await ctx.send(embed=embed)
            except:
                print("error")


token = os.environ['DISCORD_TOKEN']
bot.run(token)
