import discord
import random
import os
import re
import asyncio
import cv2
from google_trans_new import google_translator  
from google_images_download import google_images_download 
from moviepy.editor import *

translator = google_translator()
langs = ("af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-cn", "zh-tw", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "iw", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu", "fil", "he")

pi = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

response = google_images_download.googleimagesdownload()

client = discord.Client()

@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
    msg = None
    tmpsg = message.content
    message.content = message.content.lower()
    if message.content.startswith('--скажи'):
      if message.author.id == '314363965125820417':
        numb = re.search('\d+', message.content).group()
        numb = int(numb)
        if numb >= 49:
            await channel.send('иди нахуй')
            return
        elif numb > 9:
            s = tmpsg[9:]
        elif numb < 10:
            s = tmpsg[8:]
        for x in range(numb-1):
            await asyncio.sleep(1)
            msg = s.format(message)
            await channel.send(msg)
        return
      else: msg = 'иди нахуй'.format(message)
    if message.author.id == '626493193713877002':
      if message.content.startswith('--'):
        return
    
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
                if tim == 0: remsg = await channel.send(msg)
                else:
                    await asyncio.sleep(1)
                    await message.edit(remsg, msg)
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
                await channel.send(msgl)
        else: await channel.send('иди нахуй')
         
    elif message.content.startswith('--транс'):
        if tmpsg[7] == '(' and tmpsg[10] == ')':
            langcheck = tmpsg[8] + tmpsg[9]
            if langcheck in langs:
                ttext = translator.translate(tmpsg[12:], lang_tgt=langcheck)
            else: ttext = translator.translate(tmpsg[12:], lang_tgt='ru')
        else: ttext = translator.translate(tmpsg[8:], lang_tgt='ru')
        msg = ttext.format(message)
        
    elif message.content.startswith('--суп'):
        uwu = tmpsg[6:]
        for i in range (10):
            owo = random.choice(langs)
            ttext = translator.translate(uwu, lang_tgt=owo)
            uwu = ttext
        ttext = translator.translate(uwu, lang_tgt='ru')
        msg = ttext.format(message)
    
    elif message.content.startswith('--мошимоши'):
        ranstart = random.randint(1, 140)
        ranend = ranstart + 3
        clip = (VideoFileClip('ravu.mp4')
        .subclip(ranstart, ranend)
        .resize(0.5))
        clip.write_gif("sekkusu.gif")
        await channel.send(file=discord.File('sekkusu.gif'))
        return
    
    elif message.content.startswith('--отомсти'):
        cap = cv2.VideoCapture('whale.mp4')
        raframe = random.randint(11, 446)
        raframe = raframe * 1000
        cap.set(cv2.CAP_PROP_POS_MSEC, raframe)
        ret,frame = cap.read()            
        cv2.imwrite("revenge.png", frame)
        await channel.send(file=discord.File('revenge.png'))
        return

    elif message.content.startswith('--оцени'):
        s = len(tmpsg[8:])
        if s > 100:
            msg = 'иди нахуй'.format(message)
        else:
            rank = pi[s]
            if rank == '0': rank = '10'
            msg = (rank + '/10').format(message)
    
    elif message.content.startswith('--ищи'):
      if len(tmpsg) > 100:
        await channel.send('иди нахуй')
        return
      else:
        imkey = tmpsg[6:].replace(",", " ")
        arguments = {"keywords":imkey,"limit":1} 
        paths = response.download(arguments)
        print(paths)
        path = paths[0]
        print(path)
        path = path[imkey]
        print(path)
        path = ''.join(path)
        print(path)
        await channel.send(file=discord.File(path))
        return
            
    elif message.content.startswith('--помогачи'):
        msg = ('''Пока что не время умирать, ты все еще можешь:
--брось (число) (число)
--транс (текст)
--суп (текст)
--ленни
--джекпот
--эй
--гачи
--отомсти
--оцени (текст)
--ищи (текст)
--красиво (текст)
--гениально (текст)
--радужно (текст)
--рандом (список)
--? (вопрос)''').format(message)
        
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
            await channel.send(dice)
            
    elif message.content.startswith('--ленни'):
        msg = '( ͡° ͜ʖ ͡°)'.format(message)      
        
    elif message.content.startswith('--эй'):
        noodlen = random.randint(1, 20)
        for i in range(noodlen):
            eybo = random.randint(0, 1)
            if eybo == 0:
                msg = 'эй'.format(message)
            else: msg = 'братан'.format(message)
            await channel.send(msg)
            await asyncio.sleep(1)
        await channel.send('пошли лапшички навернем')
        return
        
    elif message.content.startswith('--гачи'):
        gachis = ('DO YOU LIKE WATCHING ME', 'ON THE HOUSE', 'PLAYING WITH FIRE', 'SHE GAVE ME QUITE A SHOW', 'THE SEMEN', 'WHY DON\'T YOU GET FUCKED', 'YOU GET MAD', 'AAAAAAAH', 'ANOTHER VICTIM', 'ASS WE CAN', 'AT LEAST IT SMELLS LIKE IT', 'ATTEEEN-TION', 'BET YOUR ASS', 'BIG SURPRISE', 'COME ON COLLEGE BOY', 'I\'M TAKING THAT ASS', 'LADIES FIRST', 'LASH OF THE SPANKING', 'LIKE EMBARRASSING ME', 'OH MY SHOULDER', 'ONE MORE ROUND', 'PULL UP OUR PANTS', 'SIX HOT LOADS', 'SPANK', 'THAT\'S POWER SON', 'THE OTHER NIGHT', 'THE POINT YOU WANNA BE', 'WHAT THE HELL ARE YOU TWO DOING', 'WORK THAT TOOL', 'YOU CAN GO NOW', 'YOU GOT ME MAD NOW', 'YOU LIKE CHALLENGES', 'YOU LIKE THAT', 'YOU RIPPED MY FUCKING PANTS', 'AN ASS I WOULDN\'T MIND FUCKING', 'I LOVE FIRE', 'IT TURNS ME ON', 'IT\'S A LOAN', 'OH HO HO GANGING UP', 'SO HOW YOU FEELING', 'TWO CAN PLAY IT', 'BOSS OF THIS GYM', 'COME ON', 'FUCK YOU LEATHER MAN', 'GO ANOTHER ROUND', 'JABRONI OUTFIT', 'KNOCKED OUT SOME JABRONI', 'LET\'S GIVE IT A GO', 'SETTLE IT', 'WRONG DOOR', 'IT GETS BIGGER WHEN I PULL', 'OUR DADDY TOLD US', 'RIP THE SKIN', 'SORRY FOR WHAT', 'OH OH AAAH AH', 'THANK YOU SIR', 'YES SIR', 'IT\'S MACABRE!', 'MMMMH', 'RIGHT HAPPY TO', 'SORRY', 'WITHOUT FURTHER INTERRUPTION', 'BOY NEXT DOOR', 'DEEP DARK FANTASIES', 'DO YOU LIKE WHAT YOU SEE', 'DUNGEON MASTER', 'FISTING IS 300', 'FUCK YOU', 'FUCKING CUMMING', 'FUCKYOU', 'FULL MASTER', 'I DON\'T DO ANAL', 'IT\'S BONDAGE, GAY WEBSITE', 'IT\'S SO FUCKING DEEP', 'LUBE IT UP', 'PERFORMANCE ARTIST', 'SHUT THE FUCK UP BOY', 'SLAVES', 'GET YOUR ASS BACK HERE', 'STICK YOUR FINGER', 'SUCTION', 'SWALLOW MY CUM', 'TAKE IT BOY', 'THAT TURNS ME ON', 'THAT\'S AMAZING')
        msg = ('♂' + random.choice(gachis) + '♂').format(message)
        
    elif message.content.startswith('--тесо'):
        charlist = ('Eldenheart', 'Likes-The-Pain', 'Atesmerius', 'Sekhautet', 'Ulenrel', 'Atete', 'Urjackar', 'Alaceth', 'Brontae', 'Minerva Mossmire', 'Helvenel', 'Tysdagr')
        msg = random.choice(charlist).format(message)
        
    elif message.content.startswith('--свитор'):
        charlist = ('Ta\'ar', 'Pep\'ar', 'Ract', 'Hot Character', 'Sarcastic Character', 'Song\'ar', 'Jen\'ar', 'Chirikyât\'ar', 'Secret Character', 'Ironic Character', 'Jøs Beroya', 'Eila\'ar', 'Edeeniz', 'Xii-ar', 'Slo\'ar', 'Ren\'ar', 'Pa\'rih\'ar', 'Desc\'ar', 'Lett\'ar', 'Aen\'ar', 'Nae Celos', 'Kûsk\'ar', 'Mort\'ar', 'Nevermo\'ar', 'Vhoer', 'Lora\'ar', 'Ad\'ar', 'Vit\'ar', 'Sit\'ar', 'Quen\'ar')
        msg = random.choice(charlist).format(message)
        
    elif message.content.startswith('--?'):
        ebanswer = ('Полюбому', 'Точно', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Есть все шансы', 'Да? Наверное?', 'Да', 'Хуй его знает', 'Иди нахуй с такими вопросами', 'Не скажу', 'Спроси у Вита', 'Собери чакру и спроси опять', 'И не надейся', 'Хуй там', 'Нет', 'Не лезь туда, дебил', 'Весьма сомнительно')
        msg = random.choice(ebanswer).format(message)
    
    elif message.content.startswith('--джекпот'):
        await channel.send(file=discord.File('./jackpot.jpg'))
        return
    
    elif message.author == client.user:
        return

    elif 'пасиб' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            msg = 'Пожалуйста.'.format(message)
        else: return
      
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
        
    elif ('heh' in message.content) or ('хех' in message.content):
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            await channel.send(file=discord.File('./ehe.jpg'))
            return
        else: return
        
    elif 'точно' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            msg = 'Точно'.format(message)
        else: return

    elif 'отчаян' in message.content:
        slowpoke = random.randint(1, 10)
        await asyncio.sleep(slowpoke)
        tryit = random.randint(0, 3)
        if tryit == 1:
            await channel.send(file=discord.File('./despair.gif'))
        return
        
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
               
    elif message.content.startswith('--'):
        msg = ('''Я в отчаянии!
Твоя неспособность правильно использовать команду, или даже написать "--помогачи" повергает меня в пучины отчаянья!
Пойду умру.''').format(message)
        
    if '--ответь' in message.content:
      if message.author.id == '314363965125820417':
        answer = 1
        numb = re.search('\d+', message.content).group()
        numb = int(numb)
        if numb >= 49:
            await channel.send('иди нахуй')
            return
        else:
          answer = numb
          for nigh in range(answer):
            asyncio.sleep(1)
            await channel.send(msg)
          return
    if msg == None: return
    else: await channel.send(msg)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')    
client.run(os.getenv('TOKEN'))  
