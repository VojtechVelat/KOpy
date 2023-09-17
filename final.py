
a = open("a.txt","r", encoding="utf-8")
b= open("b.txt","r", encoding="utf-8")
c= open("c.txt","r", encoding="utf-8")

cas = 0

def nacti(option):
    global a,b,c,cas

    zavodnik = []
    
    if (option=="a"):
        zavodnik = a.readline()
    if (option=="b"):
        zavodnik = b.readline()
    if (option=="c"):
        zavodnik = c.readline()

    zavodnik = zavodnik

    

    i = 0

    while(zavodnik[i]!=':'):
        i=i+1
    
    j = i

    while(zavodnik[j].isspace()==False):
        j = j - 1

    while(zavodnik[i].isspace()==False):
        i = i + 1
    
    cas = zavodnik[j:i].strip()
    



    mezery = 0
    i = 0

    while(mezery<5):
        if zavodnik[i].isspace():
            mezery = mezery + 1
        i = i + 1

    return zavodnik[0:i].strip()

for k in range(0,2):
    zavodnice = [0,0,0]
    casy = [0,0,0]
    zavodnice[0] = nacti('a')
    casy[0] = cas
    zavodnice[1] = nacti('b')
    casy[1] = cas
    zavodnice[2] = nacti('c')
    casy[2] = cas


    for i in range (0,3):
        minutes, seconds = map(int, casy[i].split(":"))
        casy[i] = minutes*60 + seconds

    for i in range(0,3):
        z = casy.index(min(casy)) 
        print(zavodnice[z] + ' ' + str(3*k + i + 1))
        casy[z] = 100000000000000000

a.close()
b.close()
c.close()
input()