import discord
from config import TOKEN, forbidden_words

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as {0}!".format(self.user))

    async def on_message(self, message):

        for i in forbidden_words:
            if i in message.content.lower():
                await message.reply("Achte auf deine Ausdrucksweise!")
                await message.delete()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)