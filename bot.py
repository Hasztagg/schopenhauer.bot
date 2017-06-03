import discord
import random
from discord.ext.commands import Bot
import vars

schopenhauer = Bot(command_prefix="!")

@schopenhauer.event
async def on_ready():
	print("Zalogowano jako")
	print(schopenhauer.user.name)
	print(schopenhauer.user.id)
	print("---------")

@schopenhauer.command()
async def hello(*args):
	print (args)
	return await schopenhauer.say("Witam, i tak wszyscy umrzemy")

@schopenhauer.command()
async def magicznakula(*args):
  magiczne_powiedzenia = ["Tak", "Nie", "Nie wiem", "Hokus pokus, zapach lata, pora idejść z tego świata"]
  await self.schopenhauer.send_message(message.channel.format(random.choice(magiczne_powiedzenia)))

schopenhauer.run(vars.BOT_TOKEN)
