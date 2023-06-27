import os, discord
my_secret = os.environ['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!lyric'):
        await message.channel.send(message.content)
