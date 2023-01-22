import os
import asyncio
import pytube as pt
import discord
from discord import member,guild
from discord.ext import commands
import wikipedia
import random
import requests
import shutil

# BOT_KEY = os.environ['RSAKEY']


class AIBOT:
    aibot = False
    ch_id = 0
    yturl = ''
    def Bot(self, msg):
        url = f"https://v6.rsa-api.xyz/ai/response?user_id=420&message={msg}"
        headers = {
             'Authorization': 'Qgy5DMPfjnYX'
           }
        response = requests.request("GET", url, headers=headers)
        r = response.text
        r = r.split('"message":"')
        r = r[1]
        r = r.split('","warning')
        r = r[0]
        r = r.replace('"}', '')
        return r
    def Downloder(self):
        ytube = pt.YouTube(url=self.yturl) 
        # vid = ytube.streams.get_highest_resolution().download(output_path="./data", filename="video.mp4")
        aud = ytube.streams.get_audio_only().download(output_path="./data", filename="song.mp4")
    # def audDown(self):
    #     ytube = pt.YouTube(url=self.url)
    #     aud = ytube.streams.get_audio_only().download(output_path="./data", filename="song.mp4")
    def title(self):
        ytube = pt.YouTube(url=self.yturl) 
        return ytube.title
    def desc(self):
        ytube = pt.YouTube(url=self.yturl) 
        return ytube.description
    def thumnail(self):
        ytube = pt.YouTube(url=self.yturl)
        return ytube.thumbnail_url
    def fileh(self):
        if os.path.exists("data"):
            shutil.rmtree("data")
        else:    
            os.makedirs(name="data")


    # print(r)
B = AIBOT()

# configration
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="#",intents=intents)

id=  710871109947490369

f = open("rules.txt", "r")
rules = f.readlines()


banned_words=['fuck',"Fuck","FUCK",'dick',"SEX","Sex","se.x",'bitch',"mc","bc","lodu","madarchod","behanchod","sex"]

# On Ready

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=" #helps, #h"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="A song"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Over the mods"))
    print("Hi, I am DogeBot")
    bot = client.get_channel(id)
    await bot.send('DogeBot is Live :)') 

# async def ch_pr():
#     await client.wait_until_ready()
#     statuses = ["for #helps, #h","A song","Over the mods","Gaali Ban hai:)","Hi, I am DogeBot","#chatwithbot"]

#     while not client.is_closed():
#         status = random.choice(statuses)
#         await client.change_presence(activity=discord.Activity(name=status, type=discord.ActivityType.playing))
#         await asyncio.sleep(5)
# client.loop.create_task(ch_pr())
  

@client.event
async def on_message(msg):
    for word in banned_words:
            if word in msg.content:
                await msg.delete() 
    if client.user == msg.author:
        return 
    if B.aibot == True and msg.channel.id == B.ch_id:
        print(msg.content)
        response =  B.Bot(str(msg.content))
        await msg.reply(str(response))
    # elif str(msg.channel)  == "chat_with_bot":
    #     if "https" in str(msg.content):
    #         B.yturl = str(msg.content)
    #         B.Downloder()
    #         em = discord.Embed(title = B.title(), description = B.desc() , color = discord.Colour.dark_gold())
    #         em.set_thumbnail(url=B.thumnail())
    #         await msg.reply("Your file is now ready", embed=em)
    elif msg.channel.id == 847431857489575937 or str(msg.channel)=="search_with_bot":
        print(str(msg.content))
        response =  wikipedia.summary(str(msg.content), sentences = 3)
        print("yes its working",response)
        await msg.reply(response)    
    else:
        pass
    # print(msg.content)
    await client.process_commands(msg)
         


@client.command(name="version")
async def version(ctx):
    await ctx.message.channel.send("Version 1.0.1")

# rules

@client.command()
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1]) 

@client.command(name="ytsong")
async def videoD(ctx, url:str):
    B.fileh()
    B.yturl = url
    await ctx.message.channel.send("Loading....")
    B.Downloder()
    f = discord.File(r'E:\Development\Python\New folder\DogeBot\data\song.mp4')
    em = discord.Embed(title = B.title(), color = discord.Colour.blue())
    em.set_thumbnail(url=B.thumnail())
    em.set_image(url=B.thumnail())
    # await msg.reply("Your file is now ready", embed=em)
    await ctx.send("Your file is here ",file=f, embed=em)

@client.command(name="aichat")
async def AIchat(ctx):
    print(ctx.channel.id)
    if B.aibot == True:
        B.aibot=False
        await ctx.message.channel.send("Ai Bot is Now OFFLINE")
    else:
        B.aibot = True
        B.ch_id = ctx.channel.id
        await ctx.message.channel.send("Ai Bot start Now")
        


# Help

@client.command(aliases=['h'])
async def helps(ctx):
    em = discord.Embed(title = "DogeBot Command List", description = "We have some really kick-ass " , color = discord.Colour.dark_gold())
    em.set_author(name=ctx.author.name)

    em.add_field(name="#version",value="DogeBot Version", inline=True)
    em.add_field(name="#server",value="Know your Server Information", inline=True)
    em.add_field(name="Admin ",value="#Kick, #Ban, #unban", inline=True)
    em.add_field(name="Clean ",value=" #clean 5 0r #c 5 or use  cleanx,cx also", inline=False)
    em.add_field(name="Whois ",value="Know your server member (#whois @member)", inline=True)
    em.add_field(name="Mute UnMute ",value=" #Mute @member 0r #m And  #unmute @member ", inline=True)
    em.add_field(name="Aichat",value="want to chat with Bot type #aichat for start and Stop AI chat (Or ha gaali or PornStar search ka Naam  bhi mat lena :)", inline=False)
    em.add_field(name="No abusing Word ",value="no one use Abusing word in this server because (Jab saala ham nhi dete toh tum kese de sakte ho :)", inline=False)

    await ctx.send(embed=em) 

# Server Information

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    desc = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    members = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    em = discord.Embed(
        title=name + " Server Information",
        description= desc,
        color= discord.Colour.blue()
        )
    em.set_thumbnail(url=icon)
    em.add_field(name="Owner", value=owner, inline=True)
    em.add_field(name="Server ID", value=id, inline=True)
    em.add_field(name="Region", value=region, inline=False)
    em.add_field(name="Member Count", value=members, inline=True)
    
    await ctx.send(embed=em)
    

#Search Member 

@client.command()
# @commands.has_permissions(administrator=True)
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name, description = member.mention, color = discord.Colour.green())
    embed.add_field(name = "ID", value=member.id, inline= True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    
       
    
# Clean Message 

        
@client.command(aliases = ['c'])
@commands.has_permissions(manage_messages=True)
async def clean(ctx,amount:int):
    await ctx.channel.purge(limit = amount+1)
    await ctx.send('Cleared by {}'.format(ctx.author.mention))
    # await ctx.message.delete()

@client.command(aliases = ['cx'])
@commands.has_permissions(manage_messages=True)
async def cleanx(ctx,amount:int):
    await ctx.channel.purge(limit = amount+1)
    
    # await ctx.send('Cleared by {}'.format(ctx.author.mention))
    
# Mute Member
@client.command(aliases=['m'])
@commands.has_permissions(administrator=True)
async def mute(ctx, member : discord.Member):
    mute = ctx.guild.get_role(847496652176097290)
    await member.add_roles(mute)
    await ctx.send(member.name+" has been Muted by {}".format(ctx.author.mention))

# UnMute Member
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)    

# Kick  Member 

@client.command(aliases = ['k'])
@commands.has_permissions(administrator = True)
async def kick(ctx, member : discord.Member,*,reason="You Dont Follow Server Rules"):
    embed = discord.Embed(title = member.name, description = member.mention, color = discord.Colour.dark_red())
    embed.add_field(name = "ID", value=member.id, inline= True)
    embed.add_field(name = "Reason", value="You have been kicked from Our server By {} , Because:".format(ctx.author.mention)+reason, inline= True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await member.send(embed=embed)
    await member.kick(reason=reason)

# Ban Member     

@client.command(aliases = ['b'])
@commands.has_permissions(administrator = True)
async def ban(ctx, member : discord.Member,*,reason="You Dont Follow Server Rules"):
    embed = discord.Embed(title = member.name, description = member.mention, color = discord.Colour.orange())
    embed.add_field(name = "ID", value=member.id, inline= True)
    embed.add_field(name = "Reason", value=member.name+" has been Banned from Our server By{} , Because:".format(ctx.author.mention)+reason, inline= True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    await  member.send(embed=embed)
    await member.ban(reason=reason)

    

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
            
 			await ctx.guild.unban(user) 
    # await ctx.channel.send(f"Unbanned: {user.mention}") 
    # await member.send("You are Unbanned you can join") 


# @client.event
# async def on_disconnect():
#     bot = client.get_channel(id)
#     await bot.send('Goodbye :(') 

bot = "ODQ3MTQyMjE5MTMwNjAxNTYz.GDJ9Qz.rgg-8LukPepMHmhpm5wwwiOmLbsz09XtvNwBaU"
DISCORD_TOKEN="ODQ3MTQyMjE5MTMwNjAxNTYz.GVO63h.kR3lEsGfcChUB-okaqqqgNkvi0bSSdIVucgJ44"
client.run(DISCORD_TOKEN)    
# client.run(os.environ['TOKEN'])  
