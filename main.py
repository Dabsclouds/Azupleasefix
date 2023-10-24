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
    channel = client.get_channel(message.channel.id)
    guild = message.guild
    category = channel.category
    if message.channel.category.name == 'catch':
    content = message.content
      
      if 'Ping' in content:
                await channel.clone()
                      category_name = 'Stock 1'
                      guild = message.guild
                      old_category = channel.category
                      new_category = [c for c in guild.categories if c.name == category_name][0]
                      num_channels = len(new_category.channels)
                      print(f"There are {num_channels} channels in the {category_name} category.")
                      if len(new_category.channels) <= 48:
                       await channel.edit(name=locked, category=new_category, sync_permissions=True)
                      if len(new_category.channels) >= 48:
                       category_name = 'Stock 2'
                       guild = message.guild
                       old_category = channel.category
                       new_category = [c for c in guild.categories if c.name == category_name][0]
                       num_channels = len(new_category.channels)
                       print(f"There are {num_channels} channels in the {category_name} category.")
                       if len(new_category.channels) <= 48:
                        await channel.edit(name=locked, category=new_category, sync_permissions=True)
                       if len(new_category.channels) >= 48:
                        category_name = 'Stock 3'
                        guild = message.guild
                        old_category = channel.category
                        new_category = [c for c in guild.categories if c.name == category_name][0]
                        num_channels = len(new_category.channels)
                        print(f"There are {num_channels} channels in the {category_name} category.")
                        if len(new_category.channels) <= 48:
                         await channel.edit(name=locked, category=new_category, sync_permissions=True)
                        if len(new_category.channels) >= 48:
                          category_name = 'Stock 4'
                          guild = message.guild
                          old_category = channel.category
                          new_category = [c for c in guild.categories if c.name == category_name][0]
                          num_channels = len(new_category.channels)
                          print(f"There are {num_channels} channels in the {category_name} category.")
                          if len(new_category.channels) <= 48:
                           await channel.edit(name=locked, category=new_category, sync_permissions=True)
                          if len(new_category.channels) >= 48:
                            category_name = 'Stock 5'
                            guild = message.guild
                            old_category = channel.category
                            new_category = [c for c in guild.categories if c.name == category_name][0]
                            num_channels = len(new_category.channels)
                            print(f"There are {num_channels} channels in the {category_name} category.")
                            if len(new_category.channels) <= 48:
                             await channel.edit(name=locked, category=new_category, sync_permissions=True)
                            if len(new_category.channels) >= 48:
                              category_name = 'Stock 6'
                              guild = message.guild
                              old_category = channel.category
                              new_category = [c for c in guild.categories if c.name == category_name][0]
                              num_channels = len(new_category.channels)
                              print(f"There are {num_channels} channels in the {category_name} category.")
                              if len(new_category.channels) <= 48:
                               await channel.edit(name=locked, category=new_category, sync_permissions=True)
                              if len(new_category.channels) >= 48:
                                category_name = 'Stock 7'
                                guild = message.guild
                                old_category = channel.category
                                new_category = [c for c in guild.categories if c.name == category_name][0]
                                num_channels = len(new_category.channels)
                                print(f"There are {num_channels} channels in the {category_name} category.")
                                if len(new_category.channels) <= 48:
                                 await channel.edit(name=locked, category=new_category, sync_permissions=True)
                                if len(new_category.channels) >= 48:
                                  category_name = 'Stock 8'
                                  guild = message.guild
                                  old_category = channel.category
                                  new_category = [c for c in guild.categories if c.name == category_name][0]
                                  num_channels = len(new_category.channels)
                                  print(f"There are {num_channels} channels in the {category_name} category.")
                                  if len(new_category.channels) <= 48: 
                                   await channel.edit(name=locked, category=new_category, sync_permissions=True)
                                  if len(new_category.channels) >= 48:
                                    category_name = 'Stock 9'
                                    guild = message.guild
                                    old_category = channel.category
                                    new_category = [c for c in guild.categories if c.name == category_name][0]
                                    num_channels = len(new_category.channels)
                                    print(f"There are {num_channels} channels in the {category_name} category.")
                                    if len(new_category.channels) <= 48: 
                                     await channel.edit(name=locked, category=new_category, sync_permissions=True)
                                    if len(new_category.channels) >= 48:
                                      category_name = 'Stock 10'
                                      guild = message.guild
                                      old_category = channel.category
                                      new_category = [c for c in guild.categories if c.name == category_name][0]
                                      num_channels = len(new_category.channels)
                                      print(f"There are {num_channels} channels in the {category_name} category.")
                                      if len(new_category.channels) <= 48: 
                                       await channel.edit(name=locked, category=new_category, sync_permissions=True)
                      await channel.send(f'<@716390085896962058> redirect 1 2 3 4 5 6 7 8 9 10')
          
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
