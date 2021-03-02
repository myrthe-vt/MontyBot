#### Setting up the bot ####
# Importing both discord.py and the commands that belong to discord.py
import discord          #basic functions
import numpy            #calling the random inhabitants
import datetime         #changing seconds to hours and minutes
import os               #accessing operating system info
import random           #Generating random number
import sqlite3          #Local databaseS
import traceback        #Traceback for cogs
import sys              #For cogs
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

# Adding a client variable
client = commands.Bot(command_prefix = '!')

# Bot event: print when it goes live
# Additionally: connecting to the database
@client.event
async def on_ready():
    print("I am live!")

# ping pong to check the latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! The latency is {round(client.latency * 1000)} ms.')

# affirmations
@client.command()
async def affirmation(ctx):
    messages = ["You are precious, loved and worthy!", "You are beautiful, inside and out!", "You have a positive impact on this world!", 
    "Just keep moving forward, you got this!", "You are a wonderful person who deserves everything this world has to offer!",
    "You are honestly amazing!", "You are one of the nicest people I've ever seen!", "Your heart is so big and beautiful!", 
    "You mean a lot to me!", "You are strong and brave!", "You are so much stronger and braver than you think, lovely!",
    "You are spectacular!", "You are breathtaking!", "You are amazing!", "You are the bee's knees!", "You are legendary!",
    "You are sublime!", "I believe in you!", "I am so proud of you!", "You deserve love, compassion and empathy!", "You are enough!",
    "You matter!", "You are excellent!", "You are enough!", "You are worthy!", "You're doing your best!", "You deserve to be happy!",
    "You are astonishing!", "You are awesome!", "You are stellar!"]
    await ctx.send(random.choice(messages))

@client.command()
async def pet(ctx):
    message = "Thank you for the pets! Monty calms down with the attention."
    await ctx.send(message)

@client.command()
async def treat(ctx):
    message = "Monty loves the treat!! He gives you some licks of appreciation."
    await ctx.send(message)

@client.command()
async def scratch(ctx):
    message = "Thank you for the belly scratches! Monty feels so loved!"
    await ctx.send(message)

@client.command()
async def accountability(ctx):
    message = "Monty gently reminds you to Do The Thing, woof!"
    await ctx.send(message)

@client.command()
async def love(ctx):
    message = "Monty lets you know that he loves you very much!!"
    await ctx.send(message)

@client.command()
async def meds(ctx):
    message = "Monty gently reminds you that it's time to take your meds! Don't forget to stay hydrated too!"
    await ctx.send(message)


# Adding the token that belongs to the bot
client.run('ODE2MzQ3NTk5OTIwNjkzMzA4.YD5o8g.DpJa4vZZ_FiaJufxPaayzZImiBc') #Send me a request if you want the token