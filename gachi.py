import discord
import random
import os
import re
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    '''if message.author.id == '533708296956280832':
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 1)
        if len(message.attachments) > 0 or 'http' in message.content:
            msg = '<@!224599912061468672>, угомони свою хуйню'.format(message)
            await client.send_message(message.channel, msg)
        elif '314363965125820417' in message.content:
            if tryit == 1:
                msg = 'И Д И  Н А Х У Й'.format(message)
                await client.send_message(message.channel, msg)
            else:
                msg = 'сходи нахуй, пожалуйста'.format(message)
                knt = await client.get_user_info(224599912061468672)
                await client.send_message(knt, msg)
        else:
            if tryit == 1:
                msg = '<@!533708296956280832>, иди нахуй'.format(message)
                await client.send_message(message.channel, msg)
            else:
                await client.send_file(message.channel, './ucku.png')
        return'''
    tmpsg = message.content
    message.content = message.content.lower()
    if message.content.startswith('--красиво'):
        s = ' '.join(tmpsg[10:])
        msg = s.format(message)
    elif message.content.startswith('--гениально'):
        womsg = tmpsg[12:]
        listmsg = re.sub("[^\w]", " ",  womsg).split()
        endl = len(listmsg)
        endl = endl - 1
        rnx = random.sample(range(0, endl), endl)
        arbit = endl/2
        if rnx[0] > arbit:
            firs = list(listmsg[0])
            firs[0] = ('**' + firs[0] + '**')
            listmsg[0] = ''.join(firs)
        listmsg[rnx[0]] = ('[' + listmsg[rnx[0]] + ']')
        listmsg[rnx[1]] = (listmsg[rnx[1]] + '_' + listmsg[rnx[1] + 1])
        listmsg[rnx[1] + 1] = ''
        if endl > 2 and rnx[2] is not rnx[1] + 1: listmsg[rnx[2]] = ('*' + listmsg[rnx[2]] + '*')
        if endl > 3: listmsg[rnx[3]] = listmsg[rnx[3]].upper()
        if endl > 4: listmsg[rnx[4]] = ' '.join(listmsg[rnx[4]])
        msg = ' '.join(listmsg).format(message)
    elif message.content.startswith('--рандом'):
        listmsg = re.sub("[^\w]", " ",  tmpsg[9:]).split()
        random.shuffle(listmsg)
        endl = len(listmsg)
        nl = 0
        if 0 < endl < 100: 
            for il in range(endl):
                nl += 1
                msgl = (str(nl) + '. ' + listmsg[il]).format(message)
                await client.send_message(message.channel, msgl)
        else: await client.send_message(message.channel, 'иди нахуй')
    elif message.content.startswith('--скажи'):
        numb = re.search('\d+', message.content).group()
        numb = int(numb)
        if numb >= 100:
            await client.send_message(message.channel, 'иди нахуй')
            return
        elif numb > 9:
            s = tmpsg[9:]
        elif numb < 10:
            s = tmpsg[8:]
        for x in range(numb-1):
            msg = s.format(message)
            await client.send_message(message.channel, msg)
    elif message.content.startswith('--помогачи'):
        msg = ('''Пока я раздеваюсь, ты можешь:
--брось (число) (число)
--ленни
--гачи
--красиво (текст)
--гениально (текст)
--скажи(число) (текст)
--рандом (список)
--? (вопрос)
лолировать не в себя и скобочки ставить''').format(message)
    elif message.content.startswith('--брось'):
        nums = re.findall('\d+', message.content)
        nums = list(map(int, nums))
        if len(nums) > 2 or nums[0] > 100 or nums[0] == 0 or nums[1] == 0 or nums[1] > 100:
            msg = 'иди нахуй'
        else:
            res = 0
            dice = []
            for x in range(nums[0]):
                die = random.randint(1, nums[1])
                dice.append(die)
                res += die
                msg = 'Итого: ' + str(res).format(message)
            await client.send_message(message.channel, dice)
    elif message.content.startswith('--ленни'):
        msg = '( ͡° ͜ʖ ͡°)'.format(message)
    elif message.content.startswith('--гачи'):
        gachis = ('DO YOU LIKE WATCHING ME', 'ON THE HOUSE', 'PLAYING WITH FIRE', 'SHE GAVE ME QUITE A SHOW', 'THE SEMEN', 'WHY DON\'T YOU GET FUCKED', 'YOU GET MAD', 'AAAAAAAH', 'ANOTHER VICTIM', 'ASS WE CAN', 'AT LEAST IT SMELLS LIKE IT', 'ATTEEEN-TION', 'BET YOUR ASS', 'BIG SURPRISE', 'COME ON COLLEGE BOY', 'I\'M TAKING THAT ASS', 'LADIES FIRST', 'LASH OF THE SPANKING', 'LIKE EMBARRASSING ME', 'OH MY SHOULDER', 'ONE MORE ROUND', 'PULL UP OUR PANTS', 'SIX HOT LOADS', 'SPANK', 'THAT\'S POWER SON', 'THE OTHER NIGHT', 'THE POINT YOU WANNA BE', 'WHAT THE HELL ARE YOU TWO DOING', 'WORK THAT TOOL', 'YOU CAN GO NOW', 'YOU GOT ME MAD NOW', 'YOU LIKE CHALLENGES', 'YOU LIKE THAT', 'YOU RIPPED MY FUCKING PANTS', 'AN ASS I WOULDN\'T MIND FUCKING', 'I LOVE FIRE', 'IT TURNS ME ON', 'IT\'S A LOAN', 'OH HO HO GANGING UP', 'SO HOW YOU FEELING', 'TWO CAN PLAY IT', 'BOSS OF THIS GYM', 'COME ON', 'FUCK YOU LEATHER MAN', 'GO ANOTHER ROUND', 'JABRONI OUTFIT', 'KNOCKED OUT SOME JABRONI', 'LET\'S GIVE IT A GO', 'SETTLE IT', 'WRONG DOOR', 'IT GETS BIGGER WHEN I PULL', 'OUR DADDY TOLD US', 'RIP THE SKIN', 'SORRY FOR WHAT', 'OH OH AAAH AH', 'THANK YOU SIR', 'YES SIR', 'IT\'S MACABRE!', 'MMMMH', 'RIGHT HAPPY TO', 'SORRY', 'WITHOUT FURTHER INTERRUPTION', 'BOY NEXT DOOR', 'DEEP DARK FANTASIES', 'DO YOU LIKE WHAT YOU SEE', 'DUNGEON MASTER', 'FISTING IS 300', 'FUCK YOU', 'FUCKING CUMMING', 'FUCKYOU', 'FULL MASTER', 'I DON\'T DO ANAL', 'IT\'S BONDAGE, GAY WEBSITE', 'IT\'S SO FUCKING DEEP', 'LUBE IT UP', 'PERFORMANCE ARTIST', 'SHUT THE FUCK UP BOY', 'SLAVES', 'GET YOUR ASS BACK HERE', 'STICK YOUR FINGER', 'SUCTION', 'SWALLOW MY CUM', 'TAKE IT BOY', 'THAT TURNS ME ON', 'THAT\'S AMAZING')
        msg = ('♂' + random.choice(gachis) + '♂').format(message)
    elif 'лол' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 1)
        if tryit == 1:
            msg = 'лол'.format(message)
        else: return
    elif ':_1:' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 1)
        if tryit == 1:
            msg = '<:_1:526447595157979136>'.format(message)
        else: return
    elif ')))' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        smiltot = ''
        tryit = random.randint(0, 1)
        if tryit == 1:
            snum = random.randint(5, 20)
            for x in range(snum):
                lel = random.randint(0, 1)
                if lel == 1: smil = ')'
                else: smil = '0'
                smiltot += smil
                msg = smiltot.format(message)   
    elif message.content.startswith('--тесо'):
        charlist = ('Eldenheart', 'Likes-The-Pain', 'Atesmerius', 'Sekhautet', 'Ulenrel', 'Atete', 'Urjackar', 'Alaceth')
        msg = random.choice(charlist).format(message)
    elif message.content.startswith('--свитор'):
        charlist = ('Ta\'ar', 'Pep\'ar', 'Ract', 'Hot Character', 'Sarcastic Character', 'Song\'ar', 'Jen\'ar', 'Chirikyât\'ar', 'Secret Character', 'Ironic Character', 'Jøs Beroya', 'Eila\'ar', 'Edeeniz', 'Xii-ar', 'Slo\'ar', 'Ren\'ar', 'Pa\'rih\'ar', 'Desc\'ar', 'Lett\'ar', 'Aen\'ar', 'Nae Celos', 'Kûsk\'ar', 'Mort\'ar', 'Nevermo\'ar', 'Vhoer', 'Lora\'ar', 'Ad\'ar', 'Vit\'ar', 'Sit\'ar', 'Quen\'ar')
        msg = random.choice(charlist).format(message)
    elif message.content.startswith('--?'):
        ebanswer = ('Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется — «да»', 'Вероятнее всего', 'Есть все шансы', 'Знаки говорят — «да»', 'Да', 'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'И не надейся', 'Мой ответ — «нет»', 'По моим данным — «нет»', 'Перспективы не очень хорошие', 'Весьма сомнительно')
        msg = random.choice(ebanswer).format(message)
    elif message.content.startswith('--'):
        msg = 'пиши --помогачи, или сосни петуха'.format(message)
    await client.send_message(message.channel, msg)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')    
client.run(os.getenv('TOKEN'))  
