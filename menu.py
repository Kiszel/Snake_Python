def udvozlo_szoveg():
    print("Üdvözlöm! Ez egy egyszerű kigyós játék ahol van lehetőség 2 játékos modra")
def menukiir():
    print("KÍGYÓS JÁTÉK")
    print("Menü")
    print("1 - egyszemélyes játék")
    print("2 - kétszemélyes játék")
    print("3 - információ játék")
    print("4 - dicsöség lista")
    print("5 - kilépés játék")
    print("Kérem válasszon a fenti menüpontok közül")
    
def informacio():
    print("Az egyszemélyes játék szabályai:")
    print("\t ha bele ütközől a falba vagy saját magadba vesztesz")
    print("\t Az irányitás: WSAD")
    print(" A Kétszeméyles játék szabályai")
    print("\t Ugyan az mint az egyszemélyesnek csak ha az ellenfélbe ütközzöl akkor is vesztesz")
    print("\t Az irányitás: Nyilak") 
def dicsoseglista():
    try:
        with open("pontok.txt","rt") as f:
            while True:
                sor = f.readline()
                if sor == "":
                    break
                print(sor)
    except:
        print("nincs ilyen fájl még")
def menupontbekeres():
    while True:
        try:
            menuszam=int(input())
            if menuszam==1:
                from Game import Game
                Game.jatekinditas()
            elif menuszam==2:
                from ketszemelyesGame import KetszemelyesGame
                KetszemelyesGame.jatekinditas()
            elif menuszam==3:
                Menu.informacio()
                print("Válassz újra")
            elif menuszam==4:
                Menu.dicsoseglista()
                print("Válassz újra")
            elif menuszam==5:
                quit()
            else:
                print("Nem megfelelő szám")
                print("Válassz újra")
        except ValueError:
            print("ez nem szám")
            print("Válassz újra")

def ujjatek():
    udvozlo_szoveg()
    menukiir()
    menupontbekeres()   
    
                
            
