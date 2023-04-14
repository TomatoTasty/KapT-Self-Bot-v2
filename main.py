import os
try:
    os.system('pip install -r requirements.txt')
except:
    print(colorama.Fore.RED + f'Нам не удалось установить библиотеки селфбота, убедитесь что файл requirements.txt имеется в папке селфбота!')
import discord
import colorama
import json
import datetime
import asyncio
import time
import random
import requests
import urllib
import requests as rq
from threading import Thread
from subprocess import Popen
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore
from gtts import gTTS
from asyncio import create_task
from click import clear
from asyncio import sleep
from datetime import datetime
from time import sleep
from os import error  
from prettytable import PrettyTable

class SELFBOT():
    __version__ = 1.1

# Config 

with open("cong.json", encoding = "utf8") as f:
	config = json.load(f)
token = config["main"]["token"]
prefix = config["main"]["prefix"]
application_id = config["status"]["application_id"]
large_image_id = config["status"]["large_image_id"]
large_text = config["status"]["small_text"]
big_text = config["status"]["large_text"]
image_text = config["status"]["image_text"]
stream_url = config["status"]["stream_url"]
restart_cmd = config["main"]["restart_command"]
pref=config["main"]["prefix"]
nukespam = config["main"]["nuke_spam"]

## Nuke cmds checking
async def check(ctx):
	if not config['main']['nuke_commands']:
		await ctx.message.edit(content='__**KapT-SelfBot Nuke**__\nКраш команды отключены! Для того чтобы включить краш команды измените файл cong.json')
		return False
	return True
##Status checking
def status_check():
    if config["main"]["status"]:
        return True
    return False

# Bot variable
client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command("help")

# Events         

@client.event
async def on_ready():
    if status_check():
	    await client.change_presence(
		    activity = discord.Activity(
			    type=discord.ActivityType.streaming,
			    application_id = application_id,
			    name = image_text,
                details = big_text,
			    assets = {
			        'large_image' : str(large_image_id),
			        'large_text' : str(large_text)
			    },
			    url = stream_url
			    )
        )
os.system('cls')
print(colorama.Fore.GREEN + f"""
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                           |
|  ██╗░░██╗░░░░░░██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  |
|  ██║░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  |
|  █████═╝░█████╗██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  |
|  ██╔═██╗░╚════╝██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  |
|  ██║░╚██╗░░░░░░██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  |
|  ╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  |
|                                                                           |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                       https://t.me/kapt_self_bot                          |
|                       Оригинал: Картавый чел#8630                         |
|                       Перевод: ! [xD] Pomidorka#1515                      |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                           {colorama.Fore.RED}PREFIX: {prefix}{colorama.Fore.GREEN}                                      |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|{colorama.Fore.RESET}""")
print(colorama.Fore.YELLOW + f'~~~~~~~~~~~~~~~~~~~~~~~~~~Список выполненных команд~~~~~~~~~~~~~~~~~~~~~~~~~~')
@client.event
async def on_command(ctx):
	#time=datetime.now().strftime('%H:%M:%S')
	arguments=ctx.message.content.replace(pref+ctx.invoked_with, '')
	print(f'{colorama.Fore.WHITE}[COMMAND] {colorama.Fore.LIGHTCYAN_EX}{pref}{ctx.invoked_with}{colorama.Fore.LIGHTGREEN_EX}{arguments}{colorama.Fore.RESET}')

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		error='Недостаточно аргументов!'
	elif isinstance(error, commands.CommandNotFound):
		return
	elif isinstance(error, commands.BadArgument):
		error='Указан не правильный аргумент!'
	elif isinstance(error, discord.errors.Forbidden):
		error='Не достаточно прав для выполнения данной команды!'
	error=str(error).replace('Command raised an exception: ', '')
	print(f"{colorama.Fore.RED}[ERROR] {error}")
	try: await ctx.send(f'Произошла ошибка!\n```{error}```')
	except: pass

# Other Shit

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'ua': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "ua", "th", "zh-CN", "ja", "zh-TW", "ko"
]

h = f"""
**__KapT SelfBot Help__**\n
:shield: `{pref}help moderation`
:shield: **Показывает команды модерации**
:control_knobs: `{pref}help misc`
:control_knobs: **Показывает разные команды**
:tools: `{pref}help utility`
:tools: **Показывает служебные команды**
:globe_with_meridians: `{pref}status`
:globe_with_meridians: **Показывает команды статуса**
:exploding_head: `{pref}help nuke`
:exploding_head: **Показывает команды краша**
:mobile_phone: `{pref}help personal`
:mobile_phone: **Показывает персональные команды**
:heavy_plus_sign: `{pref}help math`
:heavy_plus_sign: **Показывает математические команды**
:information_source: `{pref}help server`
:information_source: **Показывает команды сервера**

`{pref}install`
**Ссылка на селфа**
`{pref}restart`
**Перезагрузка**
"""
h_moderation = f"""
**__KapT SelfBot Moderation__**\n
*[] обязателен, <> необязателен*
`{pref}Ban [участника]`
**Банит указанного участника**
`{pref}Kick [участника]`
**Удаляет указанного участника с сервера**
`{pref}AR [участник] [роль]`
**Добавляет указанную роль к указанному участнику**
`{pref}TR [участник] [роль]`
**Удаляет указанную роль от указанного участника**
`{pref}Mute [участника]`
**Отключает звук указанного участника**
`{pref}Purge <количество>`
**Очищает указанное количество сообщений**
"""
h_status = f"""
**__KapT SelfBot Status__**\n
[] Требуется, <> не обязателен*
`{pref}Game`
**Изменяет ваш статус на игру**
`{pref}Stream`
**Изменяет ваш статус на стрим**
`{pref}Listen`
**Изменяет ваш статус на слушает**
`{pref}Watch`
**Изменяет ваш статус на смотрит**
`{pref}Clear`
**Очищает ваш пользовательский статус**
"""
h_utility = f"""
**__KapT SelfBot Utility__**\n
*[] обязателен, <> необязателен*
`{pref}Avatar <участнк>`
**Показывает аватар упомянутых пользователей**
`{pref}Ping`
**Показывает задержку селфбота**
`{pref}Info`
**Показывает некоторую информацию о себе**
`{pref}Tts <язык> <сообщение>`
**Отправляет сообщение в виде текста в речь**
`{pref}Dumpemojis <serverid>`
**Дюпает эмодзи**
"""
h_misc = f"""
**__KapT SelfBot Miscellaneous__**\n
*[] обязателен, <> необязателен*
`{pref}Hug [участника] <участник>`
**Отправляет гифку с объятиями упомянутого участника/участника**
`{pref}Kiss [участник] <участник>`
**Отправляет гифку с поцелуями упомянутым участникам/участникам**
`{pref}Ascii [текст]`
**Отправляет указанный текст в ASCII**
`{pref}Wizz`
**Поддельные Wizzes на сервере, предназначенные только для того, чтобы напугать друзей**
`{pref}Dmlist [сообщение]`
**Все в ваших личных сообщениях перечисляют желаемое сообщение**
`{pref}DMFriends [сообщение]`
**Написать всем в вашем списке друзей нужное сообщение**
`{pref}DeleteDms`
**Удаляет все лс с людьми, у которых в нике есть слово "спам"**
"""
h_nuke = f"""
**__KapT SelfBot Nuke__**\n
*[] обязателен, <> необязателен*
`{pref}Banall`
**Банит всех участников сервера**
`{pref}Kickall`
**Кикает всех участников сервера**
`{pref}Schan [имя]`
**Спам каналы с желаемым именем**
`{pref}Dchan`
**Удаляет все каналы на сервере**
`{pref}DRole`
**Удаляет все роли на сервере**
`{pref}Dellall`
**Удалить все каналы и роли вместе с массбаном**
`{pref}Roles`
**Логирует все роли сервера**
`{pref}Spam [количество]`
**Начать рассылку спама выбранным количеством раз и вашим текстом**
`{pref}Anticrash`
**Начать краш сервера, обойдя некоторых антикраш-ботов**
`{pref}Auto`
**Начать автоматический краш**
`{pref}Hookall`
**Начать рассылку вебхуков по всем каналам**
`{pref}Bypass_spam [количество]`
**Запустить серверный рейд в обход некоторых антифлуд-ботов**
`{pref}Spamall [количество]`
**Запустить серверный рейд в обход некоторых антифлуд-ботов (во всех каналах)**
`{pref}Fastauto`
**Начать быстрый краш**
`{pref}Threadspam`
**Спам ветками в канале**
`{pref}Massreport [пользователь] [количество]`
**Массрепорт по пользователю и серверу**
"""
h_math = f"""
**__KapT SelfBot Math__**\n
*[] обязателен, <> необязателен*
`{pref}Add [число] [число]`
**Складывает два нужных числа**
`{pref}Subtract [число] [число]`
**Вычитает два желаемых числа**
`{pref}Multiply [число] [число]`
**Умножение двух желаемых чисел**
`{pref}Divite [число] [число]`
**Раздели два желаемых числа**
`{pref}Calculator [числа]`
**Вычисляет числа и операторы\nПример: 7*2/2**
"""
h_personal = f"""
**__KapT SelfBot Personal__**\n
*[] обязателен, <> необязателен*
`{pref}Guilds`
**Отображает все гильдии, в которых вы состоите**
`{pref}Prefix`
**Показывает префикс**
`{pref}Myroles`
**Показывает все роли, которые у вас есть**
`{pref}Nick [псевдоним]`
**Изменяет ваш псевдоним**
`{pref}Nickreset`
**Сбрасывает ваш псевдоним**
`{pref}Friendbackup`
**Создает резервную копию списка друзей в Friends.txt**
`{pref}Reactionall [количество]`
**Установите реакцию на столько сообщений, сколько вы указали**
`{pref}Create_guild`
**Создать сервер**
`{pref}Delguild`
**Удалить сервер (не работает если у вас 2fa!)**
"""
h_server = f"""
**__KapT SelfBot Server__**\n
*[] обязателен, <> необязателен*
`{pref}Servericon`
**Отправляет значок сервера**
`{pref}Serverbanner`
**Отправляет баннер сервера**
`{pref}Servername`
**Отправляет имя сервера**
`{pref}Serverinfo`
**Отправляет информацию о сервере**
`{pref}Serverroles`
**Отправляет список ролей сервера**
`{pref}Serverchannels`
**Отправляет список каналов серверов**
`{pref}Copy`
**Создает точную копию сервера**
`{pref}Leave`
**Команда для ухода с сервера**
`{pref}Invite [ссылка]`
**Команда для получения информации о приглашении**
`{pref}Clonechannel`
**Команда для клонирования канала**
"""

# Self download & Restart

@client.command()
async def install(ctx):
    await ctx.message.delete()
    await ctx.send("""**__KapT SelfBot__**\n
Оригинал: https://github.com/KapTaBka/KapT-Self-Bot
Перевод: https://github.com/TomatoTasty/KapT-Self-Bot
""")

@client.command()
async def restart(ctx):
    await ctx.message.edit(content='Перезагрузка!')
    Popen(restart_cmd)
    await ctx.message.edit(content=f'Селфбот был успешно перезагружен!')
    await client.logout



# Help

@client.command()
async def help(ctx, cat=None):
    if cat==None:
        await ctx.message.edit(content=h)
        return
    cat=cat.lower()
    if cat=='moderation':
        await ctx.message.edit(content=h_moderation)
        return
    if cat=='status':
        await ctx.message.edit(content=h_status)
        return
    if cat=='utility':
        await ctx.message.edit(content=h_utility)
        return
    if cat=='misc':
        await ctx.message.edit(content=h_misc)
        return
    if cat=='nuke':
        if await check(ctx):
            await ctx.message.edit(content=h_nuke)
            return
    if cat=='math':
        await ctx.message.edit(content=h_math)
        return
    if cat=='server':
        await ctx.message.edit(content=h_server)
        return
    if cat=='personal':
        await ctx.message.edit(content=h_personal)
        return
    else:
        await ctx.message.edit(content=f'**__KapT Selfbot__**\n\nНеизвестная категория! Ввведите `{pref}help` для полученя помощи.')


# Mod


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason):
    await ctx.message.delete()
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason):
    await ctx.message.delete()
    await member.kick(reason=reason)


@client.command()
@commands.has_permissions(manage_roles=True)
async def ar(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await member.add_roles(role)


@client.command()
@commands.has_permissions(manage_roles=True)
async def tr(ctx, member: discord.Member, role: discord.Role):
    await ctx.message.delete()
    await member.remove_roles(role)


@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
    await ctx.message.delete()
    if isinstance(error, commands.RoleNotFound):
        await ctx.send("Роль мута не найдена!")
    else:
        role = client.get_role("Muted")
        await member.add_roles(role)


@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


# Misc


@client.command()
async def hug(ctx, member: discord.Member, user: discord.Member = None):
    await ctx.message.delete()
    user = ctx.author if not user else user
    hugg = requests.get("https://nekos.life/api/v2/img/hug")
    res = hugg.json()
    await ctx.send(f"""{user.mention} обнял {member.mention}\n\n""" +
                       res["url"])


@client.command()
async def kiss(ctx, member: discord.Member, user: discord.Member = None):
    await ctx.message.delete()
    user = ctx.author if not user else user
    kisss = requests.get("https://nekos.life/api/v2/img/kiss")
    res = kisss.json()
    await ctx.send(f"""{user.mention} поцеловал {member.mention}\n\n""" +
                       res["url"])

@client.command()
async def ascii(ctx, *, message):
    await ctx.message.delete()
    ascii = requests.get(
        f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}"
    ).text
    if len("```" + ascii + "```") > 2000:
        return
    await ctx.send(f"```{ascii}```")


@client.command()
async def wizz(ctx):
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`")
    time.sleep(1)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Удаление {len(ctx.guild.text_channels)} текстовых каналов**")
    time.sleep(3)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Удаление {len(ctx.guild.voice_channels)} голосовых каналов**")
    time.sleep(2)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Удаление {len(ctx.guild.categories)} категорий**")
    time.sleep(2)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Удаление {len(ctx.guild.roles)} ролей**")
    time.sleep(5)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Спамминг текстовых каналов**")
    time.sleep(5)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Спамминг каналами**")
    time.sleep(2)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Спамминг ролей**")
    time.sleep(3)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Спаминг категориями**")
    time.sleep(2)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Отправление упоминаний**")
    time.sleep(10)
    await ctx.message.edit(content=f"`Crashing {ctx.guild}`\n**Бан {len(ctx.guild.members)}**")
    await ctx.message.edit(content=f"`Crashed {ctx.guild}`")


@client.command()
async def dmlist(ctx, *, x):
    await ctx.message.delete()
    for channel in client.private_channels:
        try:
            await channel.send(x)
            print(f"Отправил {channel}")
        except:
            print(f"Не могу отправить {channel}")
            continue


@client.command()
async def level(ctx):
    await ctx.message.delete()
    responses = [
        'Cry about it', 'We love you KapT', 'Shut the up'
    ]
    answer = random.choice(responses)
    await ctx.send(answer)
    await asyncio.sleep(5)


@client.command()
async def dmfriends(ctx, *, x):
    await ctx.message.delete()
    for friend in client.user.friends:
        try:
            await friend.send(x)
            print(f"Написал {friend.name}")
        except:
            print(f"Не могу написать {friend.name}")
            continue


@client.command()
async def deletedms(ctx, name='spam'):
	await ctx.message.delete()
	removed=0
	for dm in client.private_channels:
		if name.lower() in str(dm).lower():
			while True:
				response=requests.delete(f"https://discord.com/api/v9/channels/{dm.id}", headers={'authorization': token})
				if response!=401: break
				sleep(response.json()['retry_after'])
			removed+=1
	await ctx.send(f"**Удалил {removed}**")

# Utility


@client.command()
async def avatar(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    await ctx.message.edit(content=f'{member.avatar_url}')


@client.command()
async def banner(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    await ctx.message.edit(content=f'{client.user.banner_url}')

@client.command()
async def ping(ctx):
    await ctx.message.delete()
    msg = await ctx.send("Pinging...")
    await time.sleep(1)
    await msg.edit(content=f"🏓Pong! {round(client.latency * 1000)}ms")


@client.command()
async def info(ctx):
    await ctx.send(f"""**__{ctx.author}'s Info!__**

**Ник:**
`{client.user.name}`
**Айди:**
`{client.user.id}`
**Сервера:**
`{len(client.guilds)}`
**Аватарка:**
`{client.user.avatar_url}`""")
          
@client.command()
async def tts(ctx, lang, *, text: str):
    await ctx.message.delete()
    tts = gTTS(text, lang=lang)
    filename = f'KapT Self-Bot tts.mp3'
    tts.save(filename)
    await ctx.send(file=discord.File(fp=filename, filename=filename))
    if os.path.exists(filename):
        os.remove(filename)


@client.command()
async def dumpemojis(ctx, server_id: int = None):
    await ctx.message.delete()
    try:
        if server_id is None:
            server = ctx.guild
        else:
            server = discord.utils.get(ctx.bot.guilds, id=server_id)
        emojiNum = len(server.emojis)
        folderName = 'Emojis/' + server.name.translate(
            {ord(c): None
             for c in '/<>:"\\|?*'})
        if emojiNum > 0:
            if not os.path.exists(folderName):
                os.makedirs(folderName)
        for emoji in server.emojis:
            if emoji.animated:
                fileName = folderName + '/' + emoji.name + '.gif'
            else:
                fileName = folderName + '/' + emoji.name + '.png'
            if not os.path.exists(fileName):
                with open(fileName, 'wb') as outFile:
                    req = urllib.request.Request(
                        emoji.url, headers={'user-agent': 'Mozilla/5.0'})
                    data = urllib.request.urlopen(req).read()
                    outFile.write(data)
    except:
        pass


# Status


@client.command()
async def game(ctx, *, x):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, application_id = application_id, name='KapT Self-Bot', details=f"{x}", assets={'large_image': str(large_image_id), 'large_text': 'https://t.me/kapt_self_bot'}))

@client.command()
async def stream(ctx, *, x):
    await ctx.message.delete()
    await client.change_presence(
		activity = discord.Activity(
			type=discord.ActivityType.streaming,
			application_id = application_id,
			name = "KapT Self-Bot",
            details = f"{x}",
			assets = {
			  'large_image' : str(large_image_id),
			  'large_text':f'https://t.me/kapt_self_bot'
			},
			url = "https://twitch.tv/kapt"
			)
		)

@client.command()
async def listen(ctx):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listen, name='KapT SelfBot'))


@client.command()
async def watch(ctx):
    await ctx.message.delete()
    await client.change_presence(
       activity=discord.Activity(type=discord.ActivityType.watch, name='KapT SelfBot'))



@client.command()
async def clear(ctx):
    await ctx.message.delete()
    await client.change_presence(status=discord.Status.dnd)


# Nuke


@client.command()
async def banall(ctx):
    if await check(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try: 
                await member.ban()
            except: pass

@client.command()
async def kickall(ctx):
    if await check(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
            try:
                await member.kick()
                print(f"{colorama.Fore.GREEN} Кикнул {member}")
            except:
                print(f"{colorama.Fore.GREEN} Не могу кикнуть {member}")
            continue


@client.command()
async def schan(ctx, *, x):
    if await check(ctx):
        await ctx.message.delete()
        while True:
            await ctx.guild.create_text_channel(name=x)


@client.command()
async def srole(ctx, *, x):
    if await check(ctx):
        await ctx.message.delete()
        while True:
            await ctx.guild.create_role(name=x)


@client.command()
async def dchan(ctx):
    if await check(ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"Удалил {channel}")
            except:
                print(f"Не могу удалить {channel}")
                continue

@client.command()
async def massreport(ctx, count = 10, member: discord.Member = None):
    if member: pass
    elif ctx.message.reference:
        try: 
            async for message in ctx.history():
                if message.id == ctx.message.reference.message_id:
                    member = await ctx.guild.fetch_member(message.author)
                    break
        except: return await ctx.message.edit(content = "Не удалось получить целевого пользователя.")
    else: return await ctx.message.edit(content = "Целевой пользователь не указан! Ответьте на сообщение, отправленное целевым пользователем, или укажите его в качестве аргумента команды (использование: `.massreport [число] [@user]`).")
    await ctx.message.edit(content = f"Массовый отчет {member.mention} запущен. Пожалуйста, подождите...")
    start_time1 = round(time.time())
    start_time1_fmt = datetime.datetime.fromtimestamp(start_time1).strftime("%Y/%m/%d %H:%M:%S.%f")
    tokens_array = open("tokens.txt", "r").read().split("\n")
    log_table = PrettyTable(["№ report", "Report time", "Token number", "Reason", "Report status", "Channel ID", "Message ID"])
    log_table.sortby = "№ report"
    log_table.align = 'l'
    log_text = f'''**__Mass Reporter by KapT Self-Bot__
Время начала отчета: {start_time1_fmt} UTC
Целевой пользователь: {member.display_name}#{member.displayator} ({member.id})
Целевой сервер: {member.guild.name} ({member.guild.id})
Количество отчетов на пользователя: {count}
Количество токенов репортера: {len(tokens_array)}

Некоторые пояснения:
номер отчета - порядковый номер отчета
Report time - количество времени, прошедшее с момента запуска репортера (в этом разница)
номер токена - серийный номер токена репортера, который сделал отчет
Reason - случайная причина отчета о сообщении
Статус отчета - успешно или нет
Идентификатор канала — идентификатор канала, указанный в этом отчете.
Message ID - ID сообщения, которое было указано в этом отчете**'''
    collected_messages = []
    async for message in ctx.history(limit = 1000):
        if message.author == member:
            collected_messages.append(message.id)
    current_report = 1
    reason_dict = {
        "0": "Illegal content",
        "1": "Harrasment",
        "2": "Spam or phishing links",
        "3": "Self-harm",
        "4": "NSFW Content"
    }
    for _ in range(count):
        tkn = random.choice(tokens_array)
        msg = random.choice(collected_messages)
        rep = send_report(
            tkn,
            ctx.guild.id,
            ctx.channel.id,
            msg
        )
        if rep[0] == True:
            diff = round(time.time()) - start_time1
            if diff > 60: diffmins = diff / 60
            else: diffmins = 0
            diff = diff % 60
            if diff < 10: diff = f"0{diff}"
            log_table.add_row([
                    current_report,
                    f"+{diffmins}:{diff}",
                    tokens_array.index(tkn),
                    reason_dict[str(rep[1])],
                    "OK",
                    ctx.channel.id,
                    msg
            ])
        elif rep[0] == False:
            diff = round(time.time()) - start_time1
            if diff > 60: diffmins = diff / 60
            else: diffmins = 0
            diff = diff % 60
            if diff < 10: diff = f"0{diff}"
            log_table.add_row([
                    current_report,
                    f"+{diffmins}:{diff}",
                    tokens_array.index(tkn),
                    reason_dict[str(rep[1])],
                    "FAIL",
                    ctx.channel.id,
                    msg
            ])
        else:
            diff = round(time.time()) - start_time1
            if diff > 60: diffmins = diff / 60
            else: diffmins = 0
            diff = diff % 60
            if diff < 10: diff = f"0{diff}"
            log_table.add_row([
                    current_report,
                    f"+{diffmins}:{diff}",
                    tokens_array.index(tkn),
                    reason_dict[str(rep[1])],
                    rep[0],
                    ctx.channel.id,
                    msg
            ])
        current_report += 1
    log_filename = 'test'
    open(f"{log_filename}.txt", "w", encoding = 'utf-8').write(log_text + '\n\n' + log_table.get_string())
    await ctx.message.edit(content = f"Массовый репортер завершил свою работу. {len(tokens_array)} токенов отправили {current_report - 1} отчетов {member.mention}.")
    try: await ctx.send(file = discord.File(f"{log_filename}.txt"))
    except: await ctx.send("Не удается отправить файл журнала.")


@client.command()
async def drole(ctx):
    if await check(ctx):
        await ctx.message.delete()
        for role in ctx.guild.roles:
            try:
                await role.delete()
                print(f"Удалил {role}")
            except:
                print(f"Не могу удалить {role}")
            continue


@client.command()
async def roles(ctx):
    if await check(ctx):
        await ctx.message.delete()
        try:
            roles = [role for role in ctx.guild.roles[::-1]]
        except:
            await ctx.send("""**__Server Roles:__**\n""" +
                        "\n".join([role.name for role in roles]))

@client.command()
async def fastauto(ctx):
    if await check(ctx):
        for rolee in ctx.guild.roles:
            create_task(killrole(ctx, role=rolee))
        for channel in ctx.guild.channels:
            create_task(killchannel(ctx, ch=channel))
        for _ in range(50):
            create_task(createchannel(ctx))
            create_task(createrole(ctx))

@client.command()
async def auto(ctx):
    if await check(ctx):
        for a in ctx.guild.roles:
            try: await a.delete()
            except: pass
        for b in ctx.guild.channels:
            try: await b.delete()
            except: pass
        for c in ctx.guild.emojis:
            try: await c.delete()
            except: pass
        with open('crash.png', 'rb') as f:
            icon = f.read()
            try: await ctx.guild.edit(name="Crashed by KapT-SelfBot", icon=icon)
            except: pass
        for _ in range(50):
            try: await ctx.guild.create_text_channel(name="crash-by-KapT-SelfBot")
            except: pass
        for _ in range(50):
            try: await ctx.guild.create_role(name="Crashed by KapT-SelfBot")
            except: pass
        for member in ctx.guild.members:
            try: await member.ban()
            except: pass

@client.command()
async def hookall(ctx):
    if await check(ctx):
        member=ctx.author
        whlist=[]
        for channel in ctx.guild.text_channels:
            if member.permissions_in(channel).manage_webhooks:
                webhoks = await channel.webhooks()
                if len(webhoks) > 0:
                    for webhook in webhoks:
                        whlist.append(webhook)
                else:
                    webhook = await channel.create_webhook(name="Crashed by KapT-SelfBot")
                    whlist.append(webhook)
        while True:
            for webhook in whlist:
                try: await webhook.send(nukespam, username = "Crashed by SelfBot-Kapt")
                except: pass


@client.command()
async def spamall(ctx, kapt: int):
    if await check(ctx):
        for channel in ctx.guild.text_channels:
            create_task(sendch(ctx, ch=channel, text=f'{nukespam}\n||{random.randint(1000, 9999)}||', count=kapt))

@client.command(pass_contex=True)
async def bypass_spam(ctx, lol: int):
    if await check(ctx):
        await ctx.message.delete()
        for _i in range(lol):
            await ctx.send(f'{nukespam} ||{random.randint(1000, 9999)}||')

@client.command()
async def dellall(ctx):
    if await check(ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                pass
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                pass
        for members in ctx.guild.members:
            try:
                await members.ban()
            except:
                pass

@client.command()
async def anticrash(ctx):
    if await check(ctx):
        for role in ctx.guild.roles:
            try:
                await role.edit(name="Crashed by KapT-SelfBot", permissions=discord.Permissions(permissions=8))
            except:
                pass
            else:
                pass
        for channel in ctx.guild.channels:
            try:
                await channel.edit(name=f"Crashed by KapT-SelfBot-{random.randint(1, 1000)}", topic=nukespam)
            except:
                pass
            else:
                pass
        for chan in ctx.guild.text_channels:
            try:
                hell = await chan.create_webhook(name='Crashed by KapT-SelfBot')
            except:
                pass
        for i in range(30):
            for channels in ctx.guild.text_channels:
                hooks = await channels.webhooks()
                for hook in hooks:
                    await hook.send(nukespam)

async def sendhook(ctx, channelm):
		for i in range(100):
			hooks = await channelm.webhooks()
			for hook in hooks:
				await hook.send(nukespam)

@client.command(pass_contex=True)
async def spam(ctx, amount: int):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(nukespam)



@client.command()
async def threadspam(ctx, maxamount: int = 10):
    if await check(ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        threads = []
        for i in range(maxamount):
            thread = Thread(target=MassThread, args=(
                ctx,
                maxamount,
            )).start()
            threads.append(thread)

# Personal

@client.command()
async def invite(ctx, *, link):
    if "discord.gg/" in link:
        link2 = (link.split("https://discord.gg/")[1])[:10]
        response = requests.get(
            f'https://discord.com/api/v6/invite/{link2}').json()
        if 'Unknown Invite' in response:
            await ctx.message.edit(
                content="**Неверная ссылка для приглашения!**",
                delete_after=3)
        else:
            try:
                embed = f"**Имя: `{response['guild']['name']}`\nАйди: `{response['guild']['id']}`\nИмя приглашающего: `{response['inviter']['username']}`\nТег создателя приглашения: `{response['inviter']['discriminator']}`\nId создателя приглашения: `{response['inviter']['id']}`\nИмя канала: `{response['channel']['name']}`\nАйди канала: `{response['channel']['id']}`**"
            except:
                await ctx.message.edit(
                    content="**Неверная ссылка для приглашения!**",
                    delete_after=3)
                return

            await ctx.message.edit(content=embed)
    else:
        await ctx.message.edit(
            content=
            "**Пожалуйста, предоставьте ссылку-приглашение в формате\n```<https://discord.gg/link>```**",
            delete_after=5)

@client.command()
async def delguild(ctx):
	try:
		await ctx.guild.delete()
	except Exception as e:
		await ctx.send(f'Произошла ошибка при удалении сервера | `{e}`')

@client.command()
async def create_guild(ctx, *, nameg='Guild by KapT-SelfBot'):
	new = await client.create_guild(name=nameg)
	listc = await new.fetch_channels()
	for c in listc:
		await c.delete()
	await new.create_text_channel('made-by-kapt-selfbot'),
	await ctx.send(f'Сервер создан {nameg}')

@client.command()
async def reactionall( ctx, amount: int):
	await ctx.message.delete()
	messages = await ctx.channel.history(limit=amount).flatten()
	reactioned=0
	for message in messages:
		await message.add_reaction("🐱")
		await message.add_reaction("✅")
		reactioned+=1
	await ctx.send(f"**:white_check_mark: Успешно настроены реакции на {reactioned} сообщения!**")

@client.command()
async def guilds(ctx):
    await ctx.message.delete()
    await ctx.send(f"""**Серверов:**
{len(client.guilds)}
**Названия:**\n""" + "\n".join([guild.name for guild in guilds]))


@client.command()
async def prefix(ctx):
    await ctx.message.delete()
    await ctx.send(f"""**__Префикс__**\n`""" + pref + "`")


@client.command()
async def myroles(ctx):
    await ctx.message.delete()
    await ctx.send(f"""**Роли:**\n`{len(ctx.author.roles)}`
**Название:**\n""" + "\n".join([role.name for role in roles]))


@client.command()
async def nick(ctx, *, x):
    await ctx.message.delete()
    await ctx.author.edit(nick=x)

@client.command()
async def nickreset(ctx):
    await ctx.message.delete()
    await ctx.author.edit(nick=ctx.author.name)


@client.command(aliases=['friendexport'])
async def friendbackup(ctx):
    friends = requests.get(
        'https://discordapp.com/api/v8/users/@me/relationships',
        headers={
            'authorization': token,
            'user-agent': 'Mozilla/5.0'
        }).json()
    await ctx.message.delete()
    for friend in range(0, len(friends)):
        friend_id = friends[friend]['id']
        friend_name = friends[friend]['user']['username']
        friend_discriminator = friends[friend]['user']['discriminator']
        friendinfo = f'{friend_name}#{friend_discriminator} ({friend_id})'
        with open('Friends.txt', 'a+') as f:
            f.write(friendinfo + "\n")

# Math


@client.command()
async def add(ctx, number1, number2):
    x = f"{number1}+{number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(
            color=discord.Colour.from_rgb(255, 0, 0),
            description=f"Вопрос: {number1} + {number2}\nОтвет: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(
            f"""**Вопрос:** {number1} + {number2}\n**Ответ:** {eval(x)}""")


@client.command()
async def subtract(ctx, number1, number2):
    x = f"{number1} - {number2}"
    await ctx.message.delete()
    try:
        embed = discord.Embed(
            color=discord.Colour.from_rgb(255, 0, 0),
            description=f"Вопрос: {number1} - {number2}\nОтвет: {eval(x)}")
        await ctx.send(embed=embed)
    except:
        await ctx.send(
            f"""**Вопрос:** {number1} - {number2}\n**Ответ:** {eval(x)}""")


@client.command()
async def multiply(ctx, number1, number2):
    x = f"{number1}*{number2}"
    await ctx.message.delete()
    await ctx.send(
            f"""**Вопрос:** {number1} * {number2}\n**Ответ:** {eval(x)}""")


@client.command()
async def divide(ctx, number1, number2):
    x = f"{number1} / {number2}"
    await ctx.message.delete()
    await ctx.send(
            f"""**Вопрос:** {number1} / {number2}\n**Ответ:** {eval(x)}""")


@client.command()
async def calculator(ctx, *, x):
    await ctx.message.delete()
    await ctx.send(f"""**Вопрос:** {x}\n**Ответ:** {eval(x)}""")


# Server


@client.command()
async def servericon(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.icon_url}")


@client.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.banner_url}")


@client.command()
async def servername(ctx):
    await ctx.message.delete()
    await ctx.send(ctx.guild.name)


@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    await ctx.send(f"""**__SERVERINFO__**
        
**Имя:**
`{ctx.guild.name}`
**Айди:**
`{ctx.guild.id}`
**Владелец:**
`{ctx.guild.owner}`
**Роли::**
`{len(ctx.guild.roles)}`
**Текстовых каналов:**
`{len(ctx.guild.text_channels)}`
**Голосовых каналов:**
`{len(ctx.guild.voice_channels)}`
**Категории:**
`{len(ctx.guild.categories)}`
**Бусты:**
`{ctx.guild.premium_subscription_count}`
**Участники:**
`{ctx.guild.member_count}`""")


@client.command()
async def serverroles(ctx):
    await ctx.message.delete()
    await ctx.send("""**__Роли:__**\n""" +
                       "\n".join([role.name for role in roles]))


@client.command()
async def serverchannels(ctx):
    await ctx.message.delete()
    await ctx.send("""**__Каналы:__**\n""" +
                       "\n".join([channel.name for channel in channels]))


@client.command()
async def copy(ctx):
    await ctx.message.delete()
    await client.create_guild(f'{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for role in ctx.guild.roles:
                name = role.name
                color = role.colour
                perms = role.permissions
                await g.create_role(name=name, permissions=perms, colour=color)

@client.command()
async def clonechannel(ctx):
    await ctx.message.delete()
    new = await ctx.channel.clone()
    await new.edit(position=ctx.channel.position)
    await ctx.channel.delete()

@client.command()
async def leave(ctx):
    await ctx.send('GG')
    await ctx.guild.leave()


@client.command()
async def leaveallservers(ctx):
    await ctx.message.delete()
    try:
        guilds = requests.get(
            'https://canary.discordapp.com/api/v8/users/@me/guilds',
            headers={
                'authorization': token,
                'user-agent': 'Mozilla/5.0'
            }).json()
        for guild in range(0, len(guilds)):
            guild_id = guilds[guild]['id']
            requests.delete(
                f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}',
                headers={
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0'
                })
    except Exception:
        pass


@client.command()
async def deleteallfriends(ctx):
    try:
        friends = requests.get(
            'https://canary.discordapp.com/api/v8/users/@me/relationships',
            headers={
                'authorization': token,
                'user-agent': 'Mozilla/5.0'
            }).json()
        for friend in range(0, len(friends)):
            friend_id = friends[friend]['id']
            requests.put(
                f'https://canary.discordapp.com/api/v8/users/@me/relationships/{friend_id}',
                json={'type': 2},
                headers={
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0'
                })
            requests.delete(
                f'https://canary.discordapp.com/api/v8/channels/{friend_id}',
                headers={
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0'
                })
    except Exception:
        pass

# SHIIIIIIIIIIIIIT

def MassThread(ctx, maxamount):
    while maxamount >= 0:
        r = requests.post(
            f"https://canary.discord.com/api/v9/channels/{ctx.channel.id}/threads",
            json={
                "name": f"Raid by KapT Self-Bot",
                "type": 11,
                "auto_archive_duration": 60,
                "location": "Slash Command"
            },
            headers={"Authorization": f"{token}"})
        if r.status_code != int(201):
            print(f"{r.json()}")
            if r.json()['retry_after'] >= 200:
                print(f"more 200s.")
                break
        elif r.status_code == int(404):
            print(f"Channel deleted")
            break
        elif r.status_code == int(429):
            print(f"API BAN :(")
            break
        else:
            print(f"Done")
            maxamount - 1
        continue

#start_time = datetime(2021,12,26,18,35,00)
#start_unix_time = datetime(1970,1,1,0,0,0)

async def killchannel(ctx, ch):
    try:
        await ch.delete()
    except:
        pass


async def killrole(ctx, role):
    try:
        await role.delete()
    except:
        pass


async def createchannel(ctx):
    try:
        c = await ctx.guild.create_text_channel(
            f'crash-by-KapT Self-Bot-{random.randint(1, 1000)}')
    except:
        pass
    else:
        pass


async def createrole(ctx):
    try:
        await ctx.guild.create_role(
            name=f'Crash by KapT Self-Bot {random.randint(1, 1000)}', color=0xff0000)
    except:
        pass

def send_report(token: str, guild_id: int, channel_id: int, message_id: int):
    reason = random.choice([0, 1, 2, 3, 4])
    Responses = {
        '401: Unauthorized': f'Недействительный токен Discord.',
        'Missing Access': f'Отсутствует доступ к каналу или серверу.',
        'You need to verify your account in order to perform this action.': f'Не верефицирован.'
    }

    json={
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason,
    }
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'sv-SE',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }

    report = rq.post('https://discordapp.com/api/v9/report', json=json, headers=headers)
    
    if (status := report.status_code) == 201:
        return (True, reason)
    elif status in (401, 403):
        return (False, reason)
    else:
        return (report.status_code, reason)

async def sendch(ctx, ch, text, count):
    for _ in range(count):
        try:
            await ch.send(text)
        except:
            pass

try: client.run(token, bot=False)
except:
    clear()
    print(colorama.Fore.CYAN + f'Неверный токен!')
