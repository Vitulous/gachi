import discord
import random
import os
import re
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
