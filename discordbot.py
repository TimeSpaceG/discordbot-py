import discord
import openpyxl
from discord import Game

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

game = discord.Game("Your Game Name Here")

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    discord.Game("level봇 알리미")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    global sheet, file, author

    # 명령어에 따라 작업 수행
    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    elif message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    elif message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)

    elif message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)
        await message.guild.kick(author)

    elif message.content.startswith("/경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send("경고 2회 누적입니다. 서버에서 추방됩니다.")
                else:
                    await message.channel.send("경고를 1회 받았습니다.")
                    break
            if sheet["A" + str(i)].value is None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1회 받았습니다.")
                break
            i += 1

    # 정애니맨 명령어를 받았을 때
    if message.content.startswith("정애니맨"):
        await message.channel.send("반갑습니다. 저는 정애니맨봇입니다.")
access_token os.environ ["BOT_TOKEN"]
client.run("access_token")
