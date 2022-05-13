import random 

def win():
    print("du har",usersumma,"poäng")
    print("datorn har ",dealersumma,"poäng")
    print("Du vann")
    print(kort1, kort2, dKort1, dKort2)
    play()
def loss(): 
    print("du har",usersumma,"poäng")
    print("datorn har ",dealersumma,"poäng")
    print("Du förlora")
    print(kort1, kort2, dKort1, dKort2)
    play()
def draw(): 
    print("du har",usersumma,"poäng")
    print("datorn har ",dealersumma,"poäng")
    print("Det blir lika")
    play()


def play():
    #bdKort2ter esset till en 1a istället för 11a om summan går över 21
    global kort1
    global kort2
    global dKort1
    global dKort2
    global usersumma
    global dealersumma
    kort1 = int(random.randint(1,14))
    if kort1 >= 11:
        kort1=10
    kort2 = int(random.randint(1,14))
    if kort2 > 11:
        kort2=10
    usersumma = int(kort2+kort1)
    #bestämmer dina 2 första kort
    dKort1 = int(random.randint(1,14))
    if dKort1 > 11:
        dKort1=10
    dKort2 = int(random.randint(1,14))
    if dKort2 > 11:
        dKort2=10
    #bestämmer datorns 2 första kort
    #om man drar ett klätt kort så blir det en 10a
    dealersumma = int(dKort1 + dKort2)

    if dealersumma < 17: 
            dKort3 = int(random.randint(1,14))
            if dKort3 > 11:
                dKort3=10
                dealersumma = int(dKort1 + dKort2 + dKort3)

    #dealercard()
    #drar ett till kort till datorn om summan är 16 eller lägre
    if dealersumma > 21:
        if dKort2 == 11:
            dealersumma = int(dKort1 + dKort2 + dKort3 - 10)
        elif dKort2 == 11:
            dealersumma = int(dKort1 + dKort2 + dKort3 - 10)
        else: 
            if dKort1 == 11:
                dealersumma = int(dKort1 + dKort2 + dKort3 - 10)
            else:
                win()
    print("du har",usersumma,"poäng")
    print("datorns första kort är", dKort1)
    userinput = int(input("hit(1) or stand(0)?"))
    #frågar om du vill ha ett till kort
    if userinput == 1: 
        kort3 = int(random.randint(1,14)) 
        if kort3 > 11:
            kort3=10
        usersumma = kort1 + kort2 + kort3 
    #om du vill ha ett till kort
        if usersumma > 21:
            if kort3 == 11:
                userrsumma = int(kort1 + kort2 + kort3 - 10)
            elif kort2 == 11:
                usersumma = int(kort1 + kort2 + kort3 - 10)
            else: 
                if kort1 == 11:
                    usersumma = int(kort1 + kort2 + kort3 - 10)
                else:
                    loss()
        elif 21 >= usersumma: 
            if usersumma<dealersumma: 
                loss()
            if usersumma>dealersumma: 
                win()
            if usersumma==dealersumma:
                draw()
    #gör omm ess till 1 om du har över 21 poäng.
    if userinput == 0: 
        if usersumma<dealersumma: 
            loss()
        if usersumma>dealersumma: 
            win()
        if usersumma==dealersumma:
            draw()
    #om du inte vill ha ett till kort

play()