import discord 
import weatherApi as api
import json_loader
# command 

#     $iniloc = setup location
#     $cuaca = get current weather with save location 
#     $5hari = get 5 day broadcast with save location
#     $di = take place name and country code and return current weather 


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    if msg.content.startswith('$di'):
        location_name = msg.content.replace('$di', '')
        bot_msg = api.get_location(location_name)
        await msg.channel.send(bot_msg)

    if(msg.content.startswith('$next5')):
        location_name = msg.content.replace('$next5', '')
        bot_msg = api.next_5_days(location_name)
        await msg.channel.send(bot_msg)
        

    if(msg.content).startswith('$hello'):
        await msg.channel.send('Hello')

data = json_loader.get_config()
client.run(data['BOT_TOKEN'])





