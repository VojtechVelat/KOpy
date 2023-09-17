
a = open("a.txt","r", encoding="utf-8")
b= open("b.txt","r", encoding="utf-8")
c= open("c.txt","r", encoding="utf-8")

def nacti(option):
    global a,b,c

    zavodnik = []
    
    if (option=="a"):
        zavodnik = a.readline()
    if (option=="b"):
        zavodnik = b.readline()
    if (option=="c"):
        zavodnik = c.readline()

    zavodnik = zavodnik.strip()

    mezery = 0
    i = 0

    while(mezery<5):
        if zavodnik[i].isspace():
            mezery = mezery + 1
        i = i + 1

    return zavodnik[0:i].strip()




for i in range (0,2):
    print('1'+nacti('a') + '  2' + nacti('b') + '    3'+ nacti('c'))
    print('1'+ nacti('b') + '  2' +nacti('c') + '    3'+ nacti('a'))
    print('1'+nacti('c') + '  2' + nacti('a') + '    3'+ nacti('b'))
   


a.close()
b.close()
c.close()
input()