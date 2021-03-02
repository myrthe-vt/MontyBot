#### Setting up the bot ####
# Importing both discord.py and the commands that belong to discord.py
import discord          #basic functions
import numpy            #calling the random inhabitants
import os               #accessing operating system info
import random           #Generating random number
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

# Adding a client variable
client = commands.Bot(command_prefix = '!')
TOKEN = os.getenv("CLIENT_TOKEN")

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
    "You mean a lot to me!", "You are strong and brave!", "You are so much stronger and braver than you think!",
    "You are spectacular!", "You are breathtaking!", "You are amazing!", "You are the bee's knees!", "You are legendary!",
    "You are sublime!", "I believe in you!", "I am so proud of you!", "You deserve love, compassion and empathy!", "You are enough!",
    "You matter!", "You are excellent!", "You are enough!", "You are worthy!", "You're doing your best!", "You deserve to be happy!",
    "You are astonishing!", "You are awesome!", "You are stellar!"]
    await ctx.send(random.choice(messages))

@client.command()
async def pet(ctx):
    message = "Monty loves to be pet. More pets please."
    await ctx.send(message)

@client.command()
async def treat(ctx):
    message = "Monty loves treats. It is Monty's favourite thing, apart from Mama and Papa."
    await ctx.send(message)

@client.command()
async def scratch(ctx):
    message = "oooh yeahh scratch ma belly"
    await ctx.send(message)

@client.command()
async def accountability(ctx):
    message = "Monty gently reminds you to Get It Done!"
    await ctx.send(message)

@client.command()
async def love(ctx):
    message = "Monty loves you...but only if you give him a kib"
    await ctx.send(message)

@client.command()
async def meds(ctx):
    message = "Monty hates taking meds. Mama and Papa cover mine in Peanut Butter and they think I don't notice. Take yours! "
    await ctx.send(message)


# Adding the token that belongs to the bot
client.run(TOKEN) #Send me a request if you want the token