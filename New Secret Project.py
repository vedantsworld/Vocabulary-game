from itertools import filterfalse

import random
import pygame


pygame.mixer.init()
pygame.mixer.music.load('FurElise.mp3')
musicAllowed = False

def newQuestion(rounds: int = 1, words: list = []):
    '''The function where you can generate a new question based off how many rounds you give and a list that is given '''
    answerResult = None
    
    def uniqueAnswer():
        'The function where you generate a unique answer'
        randAnsNum = random.randint(0,(len(words)-1)//2)*2+1
        randAns = words[randAnsNum]
        randAnsNum = random.randint(0,(len(words)-1)//2)*2+1
        randAns = words[randAnsNum]
            
        if randAns == rightAns:
                
            if randAnsNum > len(words)-3:
                randAns = words[wordNum-3]
            else:
                randAns = words[wordNum+3]
                    

        if randAns in randAnsLst:
            uniqueAnswer()
        else:
            
            randAnsLst.append(randAns)
        

                    
        
    for i in range(0,rounds):
        wordNum = random.randint(0,(len(words)-1)//2)*2
        word = words[wordNum]
        print('\t\t'+word)
        print('\n')
        rightAns = words[wordNum+1]
        rightAnsNum = random.randint(0,4)
        randAnsLst = []
        
        for i in range(0,5):
            
            if i == rightAnsNum:
                randAnsLst.append(words[wordNum+1])
                continue

            
            uniqueAnswer()

        for i in range(0,5):
            iNum = str(i+1)
            print(iNum+': '+randAnsLst[i])
                    
            
            
        print('\n')
        answer = input('What is the answer (number): ')
        answer = answer.strip()
        if 'a' in answer or 'b' in answer or 'c' in answer or 'd' in answer or 'e' in answer or 'f' in answer or 'g' in answer or 'h' in answer or 'i' in answer or 'j' in answer or 'k' in answer or 'l' in answer or 'm' in answer or 'n' in answer or 'o' in answer or 'p' in answer or 'q' in answer or 'r' in answer or 's' in answer or '-' in answer or '§' in answer or ' ' in answer or 't' in answer or 'u' in answer or 'v' in answer or 'w' in answer or 'x' in answer or 'y' in answer or 'z' in answer or ':' in answer or ']' in answer or '/' in answer:
            answer = 6
            
        answer = int(answer)
        
        if answer == rightAnsNum+1:
            print('That was the right answer :D')
            print('\n')
            return True
        else:
            print('Nope D:. It was {}'.format(words[wordNum+1]))
            print('\n')
            weakWords = open('weakWords.txt', 'a')
            weakWords.write('\n' + word)
            weakWords.close()
            return False



randWords = ['blurt', 'to cry out or say suddenly', 'teeming', 'full or crowded', 'reverberating',
             'echoing and vibrating', 'impenetrable', 'thick and inaccessible', 'palatial', 'vast and splendid',
             'precipitous', 'steep or dangerously high', 'quaint', 'charming or picturesque', 'snubbed',
             'ignored or rejected', 'infatuated', 'in love and obsessed', 'scorn', 'dislike and contempt', 'auspicious',
             'hopeful or promising', 'idealistic', 'very optimistic and unrealistic', 'intense', 'extreme or powerful',
             'flustered', 'nervous, muddled and unsettled', 'lashing', 'thrashing or beating', 'flurry',
             'short, swirling gust', 'searing', 'burning or scorching', 'windswept', 'windblown and untidy',
             'penetrating', 'piercing or sharp', 'electrifying', 'thrilling or stunning', 'wispy', 'thin or fine',
             'billowing', 'swelling or expanding', 'balmy', 'mild or warm', 'torrential',
             'falling heavily or forcefully', 'clammy', 'soggy or moist', 'nasal', 'whiny or from your nose', 'velvety',
             'smooth or silky', 'assertive', 'forceful or self-confident', 'scrawny', 'thin and bony', 'gruff',
             'rough or husky', 'conceited', 'vain or proud', 'bumbling', 'awkward, clumsy or useless', 'steely',
             'cold and determined', 'whiff', 'sniff or trace', 'tart', 'sharp or sour', 'tangy',
             'strong or sharp-tasting', 'unpalatable', 'unappealing or off-putting', 'siege', 'a blockade or assault',
             'drone', 'to hum or make a continuous dull sound', 'gawk', 'to gape or goggle', 'immerse',
             'to dunk or plunge', 'skulk', 'to creep or prowl', 'trudge', 'to plod or walk slowly', 'laborious',
             'difficult or exhausting', 'douse', 'to drench or put out with water', 'sneer',
             'to smirk or smile nastily', 'stagger', 'to stumble or walk unsteady', 'whimper', 'to whine or sniffle',
             'overwhelming', 'overpowering or immense', 'pampered', 'spoiled or coddled', 'scurry',
             'to scamper or scuttle', 'lax', 'lenient or not severe', 'isolated', 'remote or deserted', 'elusive',
             'slippery or evasive', 'slovenly', 'untidy or dishevelled', 'macabre', 'gruesome or bloody', 'discord',
             'conflict or war', 'disembark', 'to set off or leave', 'sultry', 'hot or humid', 'tactful',
             'polite or diplomatic', 'pliant', 'supple or flexible', 'discreet', 'unnoticeable, hidden', 'oblivious',
             'unaware about one\'s surroundings', 'irresolute', 'indecisive or not certain or unsure', 'assiduous',
             'showing care and perseverance', 'expedient', 'convenient, but may not be lawful', 'embellish',
             'exaggerate or to add untrue details', 'esoteric', 'very hard to understand', 'valorous',
             'brave or courageous', 'gibe', 'a cheeky or mischievous remark', 'jibe', 'to agree or concur', 'farcical',
             'ridiculous or nonsense', 'remonstrate', 'to make a forcefully remonstrative protest', 'ignominy',
             'shame or disgrace', 'puerile', 'childishly silly or immature', 'demure', 'shy or coy', 'squalor',
             'extremely dirty or unpleasant', 'inane', 'lacking sense or silly', 'reproach',
             'expressing disapproval of something', 'pillage', 'to rob or plunder something', 'blissful',
             'extremely happy or full of joy', 'usurp', 'to take a position of power forcefully', 'charismatic',
             'having a compelling charm', 'languish', 'lack vitality or grow weak', 'depraved',
             'morally corrupt, wicked', 'erratic', 'not regular in pattern, random', 'linger',
             'to stay somewhere longer than necessary', 'pedantic', 'excessively obsessed over small details',
             'euphoria', 'a feeling of intense excitement', 'glib', 'fluent but insincere', 'pitfall',
             'a hidden or unsuspected danger', 'discredit', 'to harm the reputation of', 'sanctimonious',
             'making a show of being morally superior', 'impromptu', 'done without being planned', 'sundry',
             'of various kinds', 'quiver', 'tremble or shake', 'furtive', 'attempting to avoid attention', 'culpable',
             'deserving blame', 'litigation', 'process of taking legal action', 'substantiate',
             'prove evidence in the support of', 'munificence', 'the quality of being generous', 'assent',
             'to grant approval of', 'antiquity', 'the ancient past', 'buttress',
             'a structure of stone bricks supporting a wall', 'erroneous', 'wrong or incorrect', 'effigy',
             'a sculpture or model of a person', 'vilify', 'to speak or write in a disparaging manner', 'reticent',
             'not revealing one\'s thoughts easily', 'vacillate', 'unsure, to waver between 2 options', 'punitive',
             'inflicted or intended to cause harm', 'whinge', 'complain persistently in a peevish manner', 'reverence',
             'deep respect for someone', 'imperious', 'arrogant of dominating', 'amorphous', 'without a shape or form',
             'aloof', 'not friendly, cool and distant', 'exuberance', 'the quality of being full of energy', 'ethereal',
             'very light or delicate that it seems out of this world', 'withhold', 'refuse to give something',
             'persona', 'the aspect of someone\'s character that\'s presented to others', 'emancipate',
             'to free or liberate', 'pseudonym', 'fake name, alias', 'anarchy', 'disorder, chaos', 'potent',
             'powerful or lethal', 'tentative', 'unsure, hesitant', 'uncharted',
             'unexplored, yet to be mapped or surveyed', 'jab', 'to stab or to hit quickly', 'flounder',
             'struggle or sink', 'homage', 'respect or reverence', 'tender', 'soft or young', 'congested',
             'crowded or packed', 'confidential', 'private, undisclosed', 'waver', 'hesitate, dither', 'snare',
             'to trap or catch someone', 'revenue', 'income or salary', 'disarray', 'chaos or confusion', 'haphazard',
             'random, disorderly', 'commerce', 'trade, can be services as well', 'antiquated',
             'old-fashioned or outdated', 'asset', 'artefact, can be gained from an inheritance', 'misdemeanour',
             'bad behaviour, ill-mannered', 'reprimand', 'to scold or to punish someone']

collectibles = ['Fire Shard', 'Ice Shard', 'Poison Shard', 'Stone Shard', 'Bonus Shard', 'Shadow Shard', 'Light Shard',
                'Blood Shard', 'Soul Shard', 'Metal Shard', 'Earth Shard', 'Space Shard', 'Lava Shard', 'Colour Shard',
                'Wind Shard', 'Electricity Shard', 'Air Shard', 'Water Shard', 'Sun Shard', 'Moon Shard']
collected = []

#Beginning sequence
continued = input()
if '§' in continued:
    pygame.mixer.music.play(100000)
    musicAllowed = True
print('A long time ago, the kingdom of Eschaton lived peacefully with its ruler, RobTop')
continued = input()
if continued == 's':
    ''''''
else:
    print(
        'RobTop held all of the 20 shards: Fire, Ice, Poison, Stone, Shadow, Light, Blood, Soul, Metal, Earth, Space, Lava, Colour, Wind, Electricity, Air, Water, Sun, Moon and Bonus Shards')
    continued = input()
    print('These shards were what kept the city safe')
    continued = input()
    print('Then one day, Anaban came...')
    continued = input()
    print('He wreaked havoc and seized the shards from RobTop.')
    continued = input()
    print('Before Anaban left, he left a message')
    continued = input()
    print('To get a shard, question you must answer')
    print('Words given and answers unknown')
    print('Questions 5 must be answered correctly')
    print('To gain a shard, not always unique')
    continued = input()
    print('You must help RobTop and get all of the shards, let\'s start!')
    continued = input()

print('If you are creating a new account, the session ID doesn\'t matter, just enter your new username and password.')
sessionNum = input('Session number: ')
name = input('What should be your username: ')
password = input('What should be your password: ')

save = open('savefile.txt', 'r')
Ssave = save.read()
saveLst = Ssave.split('|')
save.close()

saveIndex = -5
for i in range(0, len(saveLst)):
    if name in saveLst[i]:
        saveIndex = i

if saveIndex == -5:
    '''Trolololololololololo'''
    loggedIn = True
else:
    currentSave = saveLst[saveIndex].split(',')
    if sessionNum == currentSave[3]:
        '''Dunun click click click 
        HI'''
        if name == currentSave[0]:
            if password == currentSave[2]:
                print(f'Ok {name}, let\'s go!')
                loggedIn = True
                shardsRn = currentSave[1]
                shardsLst = shardsRn.split('/')
                for i in shardsLst:
                    if i != '':
                        collected.append(i)
            else:
                print('Nope, that\'s wrong, try again by rerunning the code')
                loggedIn = False
        else:
            print('Nope, that\'s wrong, try again by rerunning the code')
            loggedIn = False
    else:
        print('Nope, that\'s wrong, try again by rerunning the code')
        loggedIn = False


def playloop(name, music, musicState):
    #The loop to gain shards
    if musicState == 1:
        stateM = 2
    else:
        stateM = 3
    musicAllowed = music

    if musicAllowed == True and stateM == 2:
        randVar = random.randint(1,10)
        pygame.mixer.music.unload()
        if randVar == 1:
            pygame.mixer.music.load('IntoTheLight.mp3')
        elif randVar == 2:
            pygame.mixer.music.load('Sphere.mp3')
        elif randVar == 3:
            pygame.mixer.music.load('Dimension.mp3')
        elif randVar == 4:
            pygame.mixer.music.load('SonicBlaster.mp3')
        elif randVar == 5:
            pygame.mixer.music.load('NineCirclesXtrullor.mp3')
        elif randVar == 6:
            pygame.mixer.music.load('DanceOfTheViolins.mp3')
        elif randVar == 7:
            pygame.mixer.music.load('Thermodynamix.mp3')
        elif randVar == 8:
            pygame.mixer.music.load('BetrayalOfFearTeslaX.mp3')
        elif randVar == 9:
            pygame.mixer.music.load('Hydra.mp3')
        elif randVar == 10:
            pygame.mixer.music.load('DarkDragonFire.mp3')

        pygame.mixer.music.play(100000)
    q1 = False
    q2 = False
    q3 = False
    q4 = False
    q5 = False
    q1 = newQuestion(1, randWords)
    if q1 == True:
        q2 = vnewQuestion(1, randWords)
        if q2 == True:
            q3 = newQuestion(1, randWords)
            if q3 == True:
                q4 = newQuestion(1, randWords)
                if q4 == True:
                    q5 = newQuestion(1, randWords)

    if q1 == True and q2 == True and q3 == True and q4 == True and q5 == True:
        newShard = random.randint(0, len(collectibles) - 1)
        print(f'New shard unlocked: {collectibles[newShard]}')
        if collectibles[newShard] in collected:
            'WOLOLOLO'
        else:
            collected.append(collectibles[newShard])
    else:
        print('Bad luck :(')

    playAgain = input('Do you want to try again? (y/n): ')
    if playAgain == 'y':
        stateM += 1
        playloop(name, musicAllowed, stateM)
    else:
        gameloop(name, musicAllowed, 1)


def gameloop(name, music, musicState):
    #The loop to access everything
    state = musicState
    musicAllowed = music
    if musicAllowed == True and state == 1:
        pygame.mixer.music.unload()
        pygame.mixer.music.load('SpaceBattle.mp3')
        pygame.mixer.music.play(1000000)
    if musicAllowed == False:
        pygame.mixer.music.unload()
    accname = name
    command = input(f'Hello {accname}, what do you want to do: ')
    if command == 'enable':
        print('Music enabled')
        musicAllowed = True
    if command == 'disable':
        print('Music disabled')
        musicAllowed = False
    if command == 'help':
        print('These are your possible commands: ')
        print('')
        print('help: brings up the help menu')
        print('play: allows you to play the game and collect the shards')
        print('collection: allows you to view your collection')
        print('save: allows you to save your data')
        print('settings: brings up the settings menu')
        print('')
        state += 1
        gameloop(accname, musicAllowed, state)
    elif command == 'play':
        playloop(accname, musicAllowed, 1)
    elif command == 'collection':
        if len(collected) == 0:
            print('No shards yet, go collect some!')
        else:
            for i in enumerate(collected, 1):
                print(f'{i}')
        state += 1
        gameloop(accname, musicAllowed, state)
    elif command == 'save':
        'WOLOLO'
        save = open('savefile.txt', 'r')
        saveLst = save.read().split('|')
        save.close()
        sessionIDSoFar = open('sessions.txt', 'r')
        sessionId = sessionIDSoFar.read()
        sessionId = int(sessionId)
        sessionId += 1
        sessionId = str(sessionId)
        sessionIDSoFar.close()
        sessions = open('sessions.txt', 'w')
        sessions.write(sessionId)
        sessions.close()
        userIndex = -1
        collectedSave = ''
        for i in collected:
            collectedSave = collectedSave + '/' + i
        newSave = {'username': name, 'shards': collectedSave, 'password': password, 'sessionNum': sessionId}
        for i in range(0, len(saveLst)):
            updI = saveLst[i].split(',')
            if updI[0] == name:
                userIndex = int(i)
        if userIndex == -1:
            saveLst.append('')
            userIndex = len(saveLst) - 2
        ogSave = saveLst.copy()
        saveLst[userIndex] = newSave
        save = open('savefile.txt', 'w')
        save.write('')
        save.close()
        with open('savefile.txt', 'a') as save:
            saveValues = ogSave
            save.write('|')
            for i in range(0, len(saveValues)):
                save.write(saveValues[i])
                if i % 3 == 0:
                    save.write('|')
            newSaveValues = newSave.values()
            save.write('|')
            for i in newSaveValues:
                save.write(i + ',')
            save.write('|')

        save.close()
        print(
            f'Your new session ID is {sessionId}, remember it next time to log in to your save file as well as your username and password!')
        print('Rerun the code to read your new save file alongside your new session ID!')
        print('Until then, bye!')
    elif command == 'settings':
        print(f'Name: {accname}')
        changeQ = input('Do you wish to change anything (y/n): ')
        if changeQ == 'y':
            change = input('What would you like to change: ')
            if change == 'name':
                changeTo = input('What would you like to change it to: ')
                accname = changeTo
                state += 1
                gameloop(accname, musicAllowed, state)
            else:
                state += 1
                gameloop(accname, musicAllowed, state)
        else:
            state += 1
            gameloop(accname, musicAllowed, state)
    else:
        exitfs = input('Are you sure you want to exit: ')
        if exitfs == 'y':
            'Trololololololololo'
            if len(collected) == len(collectibles):
                print('You rescued the city of Eschaton, good job!')
                continued = input()
                print('RobTop thanks you profusely')
                continued = input()
                print('You can now leave knowing the city is safe')
                continued = input()
                print('Goodbye, return soon!')
            else:
                print('The city is in a state of panic')
                continued = input()
                if len(collected) == 1:
                    print(f'Only {len(collected)} shard has been found!')
                elif len(collected) == 0:
                    print('Not a single shard has been found!')
                else:
                    print(f'Only {len(collected)} shards have been found!')
                continued = input()
                print('We hope you\'ll come another day to find the remaining shards')
                continued = input()
                print('Until then, the city of Eschaton awaits you')
                continued = input()
                print('You walk away hearing the screams of people knowing they\'re not safe')
                continued = input()
                print('Goodbye')
        else:
            state += 1
            gameloop(accname, musicAllowed, state)


if loggedIn == True:
    print('These are your possible commands: ')
    print('')
    print('help: brings up the help menu')
    print('play: allows you to play the game and collect the shards')
    print('collection: allows you to view your collection')
    print('save: allows you to save your data')
    print('settings: brings up the settings menu')
    print('')
    pygame.mixer.music.unload()
    gameloop(name, musicAllowed, 1)
