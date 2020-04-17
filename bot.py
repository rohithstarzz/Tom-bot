import discord
from discord.ext import commands, tasks
import random
from datetime import datetime
import pytz
import asyncio
from discord.utils import get
import youtube_dl
import os
from itertools import cycle


client = commands.Bot(command_prefix = '.')
status=cycle(['Apex Legends','The Witcher 3: Wild Hunt','Rocket League','Red Dead Redemption 2','Forza Horizon 4','FIFA 20',
        'Grand Theft Auto V','Minecraft','Fortnite Battle Royale','Call of Duty: Modern Warfare','Overwatch','CS:GO'])

@client.event
async def on_ready():
    print('Bot is ready')
    change_status.start()

@tasks.loop(minutes=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.send(
        f'Hi {member.mention}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.lower().count("hi")>0:
        await message.channel.send("Hello😀")

    elif message.content.lower().count("hello")>0:
         await message.channel.send("Hi😀")

    elif message.content.lower().count("vanakam")>0:
        await message.channel.send("vanakam🙏")

    elif message.content.lower().count("good morning")>0:
        await message.channel.send("Good Morning😀")

    elif message.content.lower().count("good afternoon") > 0:
        await message.channel.send("Good Afternoon😀")

    elif message.content.lower().count("good evening") > 0:
        await message.channel.send("Good evening😀")

    elif message.content.lower().count("good night") > 0:
        await message.channel.send("Good night😀")

    elif message.content.lower().count("created you")>0:
        await message.channel.send("I was created by rohith_starzz😎")

    elif message.content.lower().count("help")>0:
        embed = discord.Embed(title='About me',description="My name is TOM bot.\nI'am the manager of this server."
                            "\nI was created by Rohith starzz""\nBelow there are some useful commands")
        embed.add_field(name='.users',value='number of users online')
        embed.add_field(name='.ping', value='latency of my server')
        embed.add_field(name='.8ball', value='I will tell your future.\n'
                                             'To play Magic 8ball type : ".8ball your_question"')
        embed.add_field(name='.join', value='Joins in your voice channel\n'
                                            'Note : Before using join you should be in voice channel')
        embed.add_field(name='.leave', value='Leaves your voice channel')
        embed.add_field(name='.play', value='Plays song from youtube\n'
                                            'NOTE : To use play type ".play youtube_url\n'
                                            'Plays song only from youtube')
        embed.add_field(name='.pause', value='pauses the song')
        embed.add_field(name='.resume', value='resumes the song')
        embed.add_field(name='.stop', value='stops the song')
        await message.channel.send(content=None,embed=embed)

    elif message.content.lower().count("cool")>0:
        await message.channel.send("Cool cool😎")

    elif message.content.lower().count("thanks") > 0 or message.content.lower().count("thankyou") > 0 :
        await message.channel.send("Anytime😉")

    elif message.content.lower().count("awesome") > 0:
        await message.channel.send("You are awesome yourself😍")

    elif message.content.lower().count("your name")>0:
        await message.channel.send("My name is TOM bot😋")

    elif message.content.lower().count("hobby") > 0:
        await message.channel.send("My hobby is playing apex legends❤")

    elif message.content.lower().count("how are you") > 0:
        await message.channel.send("I'am great😋")

    elif message.content.lower().count("are you free") > 0:
        await message.channel.send("Yes,I'am free.\nWhat can i do for you?")
        await message.channel.send("Type help to know about me")

    elif message.content.lower().count("nice") > 0:
        await message.channel.send("✌")

    elif message.content.lower().count("my name") > 0:
        await message.channel.send(f"Your name is {message.author}")

    elif message.content.lower().count("what can you do")>0:
        em = discord.Embed(title='About me',description="My name is TOM bot.\nI'am the manager of this server."
                                      "\nI was created by Rohith starzz""\nBelow there are some useful commands")
        em.add_field(name='.users',value='number of users online')
        em.add_field(name='.ping', value='latency of my server')
        em.add_field(name='.8ball', value='I will tell your future.'
                                             '\nTo play Magic 8ball type : ".8ball your_question"')
        em.add_field(name='.join', value='Joins in your voice channel\n'
                                            'Note : Before using join you should be in voice channel')
        em.add_field(name='.leave', value='Leaves your voice channel')
        em.add_field(name='.play', value='Plays song from youtube\n'
                                            'NOTE : To use play type ".play youtube_url\n'
                                            'Plays song only from youtube')
        em.add_field(name='.pause', value='pauses the song')
        em.add_field(name='.resume', value='resumes the song')
        em.add_field(name='.stop', value='stops the song')
        await message.channel.send(content=None,embed=em)

    if message.content.lower().count("time") > 0:
        tz_delhi = pytz.timezone('Asia/Calcutta')
        datetime_delhi = datetime.now(tz_delhi)
        await message.channel.send(f"The time is {datetime_delhi.strftime('%I:%M %p')}")


    await client.process_commands(message)



@client.command(hidden=True)
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')


@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *,question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question : {question}\nAnswer : {random.choice(responses)}')

@client.command(pass_context=True, aliases=['j','joi'])
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            print(f"bot connected to {channel}\n")
        await ctx.send(f"Joined {channel}")
    else:
        await ctx.send(f"{ctx.message.author} You are not connected to a voice channel")


@client.command(pass_context=True, aliases=['l','lea'])
async def leave(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()
            print(f"The bot has left {channel}")
            await ctx.send(f"Left {channel}")
        else:
            print("Bot was told to leave voice channel,but was not in one")
            await ctx.send("Don't think I am in a voice channel")
    else:
        await ctx.send(f"{ctx.message.author} You are not connected to a voice channel.")


@client.command(pass_context=True, aliases=['p','pla'])
async def play(ctx,url: str):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected:
        song_there =os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            print("trying to delete song file, but its being played")
            await ctx.send("ERROR : Music playing")
            return

        await ctx.send("Getting everything ready now")

        voice = get(client.voice_clients,guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed file: {file}\n")
                os.rename(file, "song.mp3")


        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e:print(f"{name} has finished playing"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.40

        nname = name.rsplit("-", 2)
        await ctx.send(f"playing: {nname}")
        print("Playing\n")
    else:
        await ctx.send("I'am not connected in your voice channel")

@client.command(pass_context=True, aliases=['pa','pau'])
async def pause(ctx):

    voice = get(client.voice_clients,guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("Music paused")

    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing failed pause")

@client.command(pass_context=True, aliases=['r','res'])
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not paused")
        await ctx.send("Music is not paused")


@client.command(pass_context=True, aliases=['s','sto'])
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("Music stopped")

    else:
        print("No music is playing..Failed to stop")
        await ctx.send("No music is playing..Failed to stop")

@client.command(aliases=['ga'])
async def gas(ctx):
    await ctx.send(file=discord.File('gifs/gas.gif'))

@client.command(aliases=['sel'])
async def selfie(ctx):
    await ctx.send(file=discord.File('gifs/selfie.gif'))

@client.command(aliases=['sa'])
async def sad(ctx):
    await ctx.send(file=discord.File('gifs/sad.gif'))


discord_app_key = "" #get your discord app key from discord website
client.run(discord_app_key)
