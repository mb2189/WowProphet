import discord
import os
from profile import Blizz


client = discord.Client()
blizz = Blizz()
print(discord.Client().user)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  await client.change_presence(activity=discord.Game(name="Try !prophet help"))



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == "!prophet help":
    await message.channel.send("This bot can return an image of a World of Warcraft character by typing '!prophet Character Realm'. If the realm is more than one word, use a dash inbetween like 'Burning-Legion'.")
    return 

  if message.content.startswith("!prophet"):
    msg = message.content
    msg_arr = msg.lower().split()

    try:
      img = blizz.get_character_image(characterName=msg_arr[1], realmSlug=msg_arr[2])
      await message.channel.send(img)

    except IndexError:
      await message.channel.send("Incorrect format. Queries should look like '!prophet Character Realm'.")


client.run(os.getenv('TOKEN'))
