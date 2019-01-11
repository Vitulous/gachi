import discord
import random
import os
import re
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('--красиво'):
        s = ' '.join(message.content[10:])
        msg = s.format(message)
    if message.author == client.user:
        return
    message.content = message.content.lower()
    elif message.content.startswith('--помогачи'):
        msg = ('''Пока я раздеваюсь, ты можешь:
--брось x y
--ленни
--гачи
--красиво (текст)
лолировать не в себя и скобочки ставить''').format(message)
    elif message.content.startswith('--брось'):
        nums = re.findall('\d+', message.content)
        nums = list(map(int, nums))
        if 2 > len(nums) > 2 or nums[0] > 100 or nums[0] == 0 or nums[1] == 0 or nums[1] > 100:
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
