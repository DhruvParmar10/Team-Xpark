import discord
import datetime
from discord.ext import commands
import encodemsg
import decodemsg
intents = discord.Intents().all()

token = 'ODAxODIwOTI4MTkxMjM0MDU4.YAmP7g.0_5Rhc6kr8F470_yUvQlqbpe0-o'
client = commands.Bot(command_prefix='#', intents=intents)


def make_embed(author,text):
    embed = discord.Embed(color=discord.Colour.random(),title=f'',
                          description=f'```{text}```')
    embed.set_author(name=author.name, icon_url=author.avatar_url)
    return embed


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Depression'),status=discord.Status.idle)
    print('BOT IS READY!')

@client.command()
async def encode(ctx, person: discord.User, *, text):
    await ctx.message.delete()
    user = ctx.message.author.name
    await ctx.send(f'**{user}**: {encodemsg.encode(text)}')
    if person.dm_channel == None:
        await person.create_dm()
    # await person.dm_channel.send(f'**{user}**: {text}')
    embed = make_embed(ctx.message.author, text)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.message.guild.name}', icon_url="https://i.imgur.com/uZIlRnK.png")
    await person.dm_channel.send(embed=embed)

@client.command()
# @commands.has_role('OP')
async def decode(ctx,key ,* , text):
    if key.lower() == 'yellow':
        await ctx.message.delete()
        user = ctx.message.author.name
        await ctx.send(f'**{user}**: {decodemsg.decode(text)}')
    else:
        await ctx.message.delete()
        await ctx.send('Your key is invalid!')

@client.command()
async def encode2(ctx, *, text):
    await ctx.message.delete()
    user = ctx.message.author.name
    await ctx.send(f'**{user}**: {encodemsg.encode(text)}')


# @commands.command()
# async def decodelol(ctx, *, text,  person: discord.User):
#     if person.name == ctx.message.author.name:
#         await ctx.send('hi')


client.run(token)
