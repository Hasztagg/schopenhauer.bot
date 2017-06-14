import discord
import random
import time
from discord.ext.commands import Bot
import vars

schopenhauer = Bot(command_prefix="!")

@schopenhauer.event
async def on_ready():
	print("Zalogowano jako")
	print(schopenhauer.user.name)
	print(schopenhauer.user.id)
	print("---------")

@schopenhauer.command
async def hello(*args):
	print (args)
	return await schopenhauer.say("Witam, i tak wszyscy umrzemy")

"""@schopenhauer.command()
"""

@schopenhauer.event
async def on_message(message):
	if message.content.startswith('!rzut'):
		wynik = random.randrange(0,3)
		if wynik == 0:
			wynik = "Orzeł. Nie żyje."
		if wynik == 1:
			wynik = "Reszka. I po co to komu."
		if wynik == 2:
			wynik = "Nie wiem skończyły mi się monety. Znowu."
		await schopenhauer.send_message(message.channel, "Czekaj no, szukam monety...")
		time.sleep(1)
		await schopenhauer.send_message(message.channel, "%s" % wynik)
	if message.content.startswith('!kula'):
		magiczne_powiedzenia = ["Tak", "Nie", "Nie wiem", "Hokus pokus, zapach lata, pora idejść z tego świata."]
		await schopenhauer.send_message(message.channel, (random.choice(magiczne_powiedzenia)))


schopenhauer.run(vars.BOT_TOKEN)
