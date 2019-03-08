import discord
import random
import os
import re
import asyncio
import cv2
from googletrans import Translator
from moviepy.editor import *
import youtube_dl

translator = Translator()
langs = ("af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "iw", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu", "fil", "he")

ydl = youtube_dl.YoutubeDL({'outtmpl': 'ytvid.mp4',
                            'format': '135',
                            'continuedl': 'True'})

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
        if endl > 1:
            tryit = random.randint(0, 1)
            rnx = random.sample(range(0, endl), endl)
            if rnx[0] < endl - 1: 
                listmsg[rnx[0]] = (listmsg[rnx[0]] + '_' + listmsg[rnx[0] + 1])
                listmsg[rnx[0] + 1] = ''
            if endl > 1 and rnx[1] is not rnx[0] + 1:
                if tryit == 0: listmsg[rnx[1]] = ('[' + listmsg[rnx[1]] + ']')
                elif rnx[1] is not 0: listmsg[rnx[1]] = ('[' + listmsg[rnx[1]] + ']')
            if endl > 2 and rnx[2] is not rnx[0] + 1 and rnx[2] is not 0: listmsg[rnx[2]] = ('*' + listmsg[rnx[2]] + '*')
            if endl > 3 and rnx[3] is not rnx[0] + 1: listmsg[rnx[3]] = listmsg[rnx[3]].upper()
            if endl > 4 and rnx[4] is not rnx[0] + 1: listmsg[rnx[4]] = ' '.join(listmsg[rnx[4]])
            if endl > 5 and rnx[5] is not rnx[0] + 1 and rnx[5] is not 0: listmsg[rnx[5]] = ('__' + listmsg[rnx[5]] + '__')    
            if tryit == 1:
                firs = list(listmsg[0])
                firs[0] = ('**' + firs[0] + '**')
                listmsg[0] = ''.join(firs)
            msg = ' '.join(listmsg).replace('  ', ' ').format(message)
        else: msg = 'иди нахуй'.format(message)
            
    elif message.content.startswith('--радужно'):
        womsg = tmpsg[10:]
        listmsg = re.sub("[^\w]", " ",  womsg).split()
        endl = len(listmsg)
        if endl > 1:
            for tim in range(10):
                listmsg = re.sub("[^\w]", " ",  womsg).split()
                msg = ''
                rnx = random.sample(range(0, endl), endl)
                lang = ('diff', 'CSS', 'yaml', 'fix', 'brainfuck', '')
                for i in range(endl):                
                    colr = random.choice(lang)
                    if colr == 'diff': mns = '-'
                    else: mns = ''
                    listmsg[rnx[i]] = ('''```''' + colr + '''
''' + mns + listmsg[rnx[i]] + '''
```''')           
                msg = ' '.join(listmsg).format(message)
                if tim == 0: remsg = await client.send_message(message.channel, msg)
                else:
                    await asyncio.sleep(1)
                    await client.edit_message(remsg, msg)
            return
        else: msg = 'иди нахуй'.format(message)
            
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
         
    elif message.content.startswith('--транс'):
        if tmpsg[7] == '(' and tmpsg[10] == ')':
            langcheck = tmpsg[8] + tmpsg[9]
            if langcheck in langs:
                ttext = translator.translate(tmpsg[12:], dest=langcheck).text
            else: ttext = translator.translate(tmpsg[12:], dest='ru').text
        else: ttext = translator.translate(tmpsg[8:], dest='ru').text
        msg = ttext.format(message)
        
    elif message.content.startswith('--суп'):
        uwu = tmpsg[6:]
        for i in range (10):
            owo = random.choice(langs)
            ttext = translator.translate(uwu, dest=owo).text
            uwu = ttext
        ttext = translator.translate(uwu, dest='ru').text
        msg = ttext.format(message)
        
    elif message.content.startswith('--сексплз'):
        cap = cv2.VideoCapture('ravu.mp4')
        raframe = random.randint(1, 144)
        raframe = raframe * 1000
        cap.set(cv2.CAP_PROP_POS_MSEC, raframe)
        ret,frame = cap.read()            
        cv2.imwrite("sekkusu.png", frame)
        await client.send_file(message.channel, 'sekkusu.png')
        return
    
    elif message.content.startswith('--мошимоши'):
        ranstart = random.randint(1, 140)
        ranend = ranstart + 3
        clip = (VideoFileClip('ravu.mp4')
        .subclip(ranstart, ranend)
        .resize(0.5))
        clip.write_gif("sekkusu.gif")
        await client.send_file(message.channel, 'sekkusu.gif')
        return
    
    elif message.content.startswith('--отомсти'):
        cap = cv2.VideoCapture('whale.mp4')
        raframe = random.randint(11, 446)
        raframe = raframe * 1000
        cap.set(cv2.CAP_PROP_POS_MSEC, raframe)
        ret,frame = cap.read()            
        cv2.imwrite("revenge.png", frame)
        await client.send_file(message.channel, 'revenge.png')
        return
        
    elif message.content.startswith('--гиф'):
        yturl = 'https://www.youtube.com/watch?v=' + tmpsg[6:]
        givid = ydl.download([yturl])
        clip = VideoFileClip('ytvid.mp4', target_resolution=(none, 480))
        t_end = int(clip.duration)
        ranend = random.randint(1, t_end)
        ranstart = ranend - 3
        clip = (clip
        .subclip(ranstart, ranend))
        clip.write_gif("yt.gif")
        await client.send_file(message.channel, 'yt.gif')
        os.remove('ytvid.mp4')
        return
        
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
--транс (текст)
--суп (текст)
--ленни
--гачи
--сексплз
--отомсти
--сыграем
--какигратьто?
--красиво (текст)
--гениально (текст)
--радужно (текст)
--скажи(число) (текст)
--рандом (список)
--? (вопрос)
лолировать не в себя, кекать, гг и скобочки ставить''').format(message)
        
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
            
    elif message.content.startswith('--какигратьто?'):
        msg = ('''Солнце бьет Луну, как Хаширама пиздил Мадару;
Луна бьет Небо, как Мадара ебет Мито;
Небо бьет Солнце, как Мито изменяет Хашираме до слез.''').format(message)
        
    elif message.content.startswith('--сыграем'):
        await client.send_message(message.channel, 'Солнце, Небо, Луна')
        await client.send_message(message.channel, 'Раз..')
        await client.send_message(message.channel, 'Два..')
        await client.send_message(message.channel, 'Три!')
        chmsg = await client.wait_for_message(author=message.author)
        rantypes = ('Солнце', 'Небо', 'Луна')
        boch = random.choice(rantypes)
        eny = 0
        if boch == 'Солнце': eny = 1
        elif boch == 'Небо': eny = 2
        elif boch == 'Луна': eny = 3
        ply = 0
        chmsg.content = chmsg.content.lower()
        if 'солнце' in chmsg.content: ply = 1
        elif 'небо' in chmsg.content: ply = 2
        elif 'луна' in chmsg.content: ply = 3
        msg = (boch + '!').format(message)
        await client.send_message(message.channel, msg)
        await client.send_message(message.channel, '...')
        if eny == 0 or ply == 0: msg = 'иди нахуй'.format(message)
        elif eny == ply: msg = 'Ничья!'.format(message)
        elif eny - ply == 1 or ply - eny == 2: msg = 'Я победил!'.format(message)
        elif ply - eny == 1 or eny - ply == 2: msg = 'Я проиграл.. В этот раз.'.format(message)
            
    elif message.content.startswith('--ленни'):
        msg = '( ͡° ͜ʖ ͡°)'.format(message)
        
    elif message.content.startswith('--гачи'):
        gachis = ('DO YOU LIKE WATCHING ME', 'ON THE HOUSE', 'PLAYING WITH FIRE', 'SHE GAVE ME QUITE A SHOW', 'THE SEMEN', 'WHY DON\'T YOU GET FUCKED', 'YOU GET MAD', 'AAAAAAAH', 'ANOTHER VICTIM', 'ASS WE CAN', 'AT LEAST IT SMELLS LIKE IT', 'ATTEEEN-TION', 'BET YOUR ASS', 'BIG SURPRISE', 'COME ON COLLEGE BOY', 'I\'M TAKING THAT ASS', 'LADIES FIRST', 'LASH OF THE SPANKING', 'LIKE EMBARRASSING ME', 'OH MY SHOULDER', 'ONE MORE ROUND', 'PULL UP OUR PANTS', 'SIX HOT LOADS', 'SPANK', 'THAT\'S POWER SON', 'THE OTHER NIGHT', 'THE POINT YOU WANNA BE', 'WHAT THE HELL ARE YOU TWO DOING', 'WORK THAT TOOL', 'YOU CAN GO NOW', 'YOU GOT ME MAD NOW', 'YOU LIKE CHALLENGES', 'YOU LIKE THAT', 'YOU RIPPED MY FUCKING PANTS', 'AN ASS I WOULDN\'T MIND FUCKING', 'I LOVE FIRE', 'IT TURNS ME ON', 'IT\'S A LOAN', 'OH HO HO GANGING UP', 'SO HOW YOU FEELING', 'TWO CAN PLAY IT', 'BOSS OF THIS GYM', 'COME ON', 'FUCK YOU LEATHER MAN', 'GO ANOTHER ROUND', 'JABRONI OUTFIT', 'KNOCKED OUT SOME JABRONI', 'LET\'S GIVE IT A GO', 'SETTLE IT', 'WRONG DOOR', 'IT GETS BIGGER WHEN I PULL', 'OUR DADDY TOLD US', 'RIP THE SKIN', 'SORRY FOR WHAT', 'OH OH AAAH AH', 'THANK YOU SIR', 'YES SIR', 'IT\'S MACABRE!', 'MMMMH', 'RIGHT HAPPY TO', 'SORRY', 'WITHOUT FURTHER INTERRUPTION', 'BOY NEXT DOOR', 'DEEP DARK FANTASIES', 'DO YOU LIKE WHAT YOU SEE', 'DUNGEON MASTER', 'FISTING IS 300', 'FUCK YOU', 'FUCKING CUMMING', 'FUCKYOU', 'FULL MASTER', 'I DON\'T DO ANAL', 'IT\'S BONDAGE, GAY WEBSITE', 'IT\'S SO FUCKING DEEP', 'LUBE IT UP', 'PERFORMANCE ARTIST', 'SHUT THE FUCK UP BOY', 'SLAVES', 'GET YOUR ASS BACK HERE', 'STICK YOUR FINGER', 'SUCTION', 'SWALLOW MY CUM', 'TAKE IT BOY', 'THAT TURNS ME ON', 'THAT\'S AMAZING')
        msg = ('♂' + random.choice(gachis) + '♂').format(message)
        
    elif 'лол' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            msg = 'лол'.format(message)
        else: return
        
    elif 'кек' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            msg = 'кек'.format(message)
        else: return
        
    elif 'гг' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            msg = 'гг'.format(message)
        else: return
        
    elif ':_1:' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            msg = '<:_1:526447595157979136>'.format(message)
        else: return
        
    elif '))' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        smiltot = ''
        tryit = random.randint(0, 3)
        if tryit == 1:
            snum = random.randint(5, 50)
            for x in range(snum):
                lel = random.randint(0, 1)
                if lel == 1: smil = ')'
                else: smil = '0'
                smiltot += smil
                msg = smiltot.format(message)  
                
    elif message.content.startswith('--тесо'):
        charlist = ('Eldenheart', 'Likes-The-Pain', 'Atesmerius', 'Sekhautet', 'Ulenrel', 'Atete', 'Urjackar', 'Alaceth', 'Brontae')
        msg = random.choice(charlist).format(message)
        
    elif message.content.startswith('--свитор'):
        charlist = ('Ta\'ar', 'Pep\'ar', 'Ract', 'Hot Character', 'Sarcastic Character', 'Song\'ar', 'Jen\'ar', 'Chirikyât\'ar', 'Secret Character', 'Ironic Character', 'Jøs Beroya', 'Eila\'ar', 'Edeeniz', 'Xii-ar', 'Slo\'ar', 'Ren\'ar', 'Pa\'rih\'ar', 'Desc\'ar', 'Lett\'ar', 'Aen\'ar', 'Nae Celos', 'Kûsk\'ar', 'Mort\'ar', 'Nevermo\'ar', 'Vhoer', 'Lora\'ar', 'Ad\'ar', 'Vit\'ar', 'Sit\'ar', 'Quen\'ar')
        msg = random.choice(charlist).format(message)
        
    elif message.content.startswith('--?'):
        ebanswer = ('Полюбому', 'Точно', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Есть все шансы', 'Да? Наверное?', 'Да', 'Хуй его знает', 'Иди нахуй с такими вопросами', 'Не скажу', 'Спроси у Вита', 'Собери чакру и спроси опять', 'И не надейся', 'Хуй там', 'Нет', 'Не лезь туда, дибил', 'Весьма сомнительно')
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
