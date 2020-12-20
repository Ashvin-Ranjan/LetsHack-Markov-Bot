import discord
import discordhelp
import json
import emoji
import brain
import random
import asyncio

learnnew = True
client = discord.Client()

@client.event
async def on_ready():
	customActivity = discord.Game("hi")
	await client.change_presence(status=discord.Status.online, activity=customActivity)

	print("The bot is ready")
	

@client.event
async def on_message(message):

	#send message if @ ed
	if f'<@!{client.user.id}>' in message.content or f'<@{client.user.id}>' in message.content:
		try:
			async with message.channel.typing():
				await asyncio.sleep(random.random()/4)
				await message.channel.send(brain.createMessage())
		except:
			pass
		return

	if message.author == client.user:
		return


	prob = random.random()
	
	#send message or reaction
	if prob <= 0.01:
		try:
			async with message.channel.typing():
				await asyncio.sleep(random.random())
				await message.channel.send(brain.createMessage())
		except:
			pass

	#learning
	if learnnew and not message.author.bot:
		processed = message.content.replace("\n", u"\ufffc").replace(":", "").replace(",", "")

		
		
		end = ':%s,' % (processed.strip(u"\ufffc"))
		with open('messages.txt', 'a') as f:
			f.write(end + "\n")
		print(message.content)
		print(end)








client.run("")