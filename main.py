import discord
import music_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
file_path = 'APIKEY.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    args = message.content.split(" ")
    command = args.pop(0)
    
    if command == '.top10':
        artist = " ".join(args)
        try:
            await message.channel.send(music_commands.getTrack(artist))
        except Exception as e:
            await message.channel.send("That artist cannot be found.")

client.run(file_content)
