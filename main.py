import re, os, asyncio, random, string
from discord.ext import commands, tasks

token = os.environ['token']
spam_id = os.environ['spam_id']

pokename = 874910942490677270
client = commands.Bot(command_prefix= '.' )
intervals = [3.0, 2.2, 2.4, 2.6, 2.8]

@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = client.get_channel(int(spam_id))
    await channel.send(''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],7)*5))

@spam.before_loop
async def before_spam():
    await client.wait_until_ready()

spam.start()
@client.event
async def on_ready():
    print(f'Logged into account: {client.user.name}')

@client.event
async def on_message(message):
    if message.author.id == pokename:
      content = message.content
      
      if 'Rare Ping' in content:
        await message.channel.send(f'!lock')

      elif 'Regional Ping' in content:
        await message.channel.send(f'!lock')

      elif 'Collection Ping' in content and "@" in content:
        await message.channel.send(f'!lock')

      elif 'Shiny Hunt Pings' in content and "@" in content:
        await asyncio.sleep(12)
        await message.channel.send(f'!lock')


from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
  return "Your bot is alive!"
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
  server = Thread(target=run)
  server.start()

keep_alive()
client.run(f"{token}")