import random
import discord
from discord.ext import commands

token = open("TestBotPython/token.txt").read()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("ready")


@client.event
async def on_member_join(member):
    print("here")
    channel = discord.utils.get(client.get_all_channels(), name="general")
    await channel.send(f"{member} joined")


@client.event
async def on_member_remove(member):
    print("gone")
    channel = discord.utils.get(client.get_all_channels(), name="general")
    await channel.send(f"{member} dipped")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong {round(client.latency * 1000)}ms")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question='none'):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes – definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return


client.run(token)
