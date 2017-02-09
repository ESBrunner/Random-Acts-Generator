from random import shuffle
from random import randint

def randomacts(namesfile='names.txt'):
    '''This generates partners for an office Random Acts of Kindness exchange.
    Takes as an argument a textfile with a list of names. Randomly matches
    each participant with a partner. Makes a master list of partners, and
    then generates a text file to be emailed to each participant with their
    partner's name.'''
    nameslist=[]
    partnersdict={}
    fhand=open(namesfile)
    f=open('partners.txt','w')
    for line in fhand:
        nameslist.append(line.strip())
    shuffle(nameslist)
    for num in range(len(nameslist)):
        nfile=nameslist[num] +'.txt'
        partnersdict[nameslist[num]]=(nameslist[num-1], nfile)
    alphlist=sorted(list(partnersdict.keys()))
    for person in alphlist:
        f.write(person+ ": " +partnersdict[person][0]+'\n'+'\n')
        paper=open(partnersdict[person][1],'w')
        paper.write("Your partner is " + partnersdict[person][0] +'.')
    
