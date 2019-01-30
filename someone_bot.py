import discord
import random

TOKEN = "[Redacted for security]"

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if "@someone" in message.content:
		members = message.server.members
		online = list()
		for m in members:
			if m.status == discord.Status.online:
				online.append(m)
		msg = ""
		if len(online) > 0:
			index = random.randint(0, len(online) - 1)
			chosen = online[index]
			chosen = "<@" + chosen.id + ">"
			msg = message.content.replace("@someone", chosen)
			if message.mention_everyone:
				msg = msg.replace("@everyone", "everyone")
		else:
			msg = "Nobody online"
		await client.send_message(message.channel, msg)


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print("on following servers:")
	for s in client.servers:
		print(s.name)
	print('------')

client.run(TOKEN)