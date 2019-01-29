from tkinter import Tk,Button
from Elsojatekos import Snake,Jatek,valtozoletrehozas
from snake_object import Kaja,Body
import random
import turtle
import time
class Game(object):
    def jatekinditas():
        #Ha nem elsőnek játszik akkor rejtse el a felúgro ablakot és törölje a szöveget amit belle lett írva
        if valtozoletrehozas.snake.nev!="":
            valtozoletrehozas.game.felugro.withdraw()
        else:
            #név bekerese
            valtozoletrehozas.snake.nev=input("Kérem adja meg a nevét")
        # eredmény kiírása
        valtozoletrehozas.game.pont.clear()
        valtozoletrehozas.game.pont.write("Pont: {0}  Név: {1}".format(valtozoletrehozas.snake.hit_score,valtozoletrehozas.snake.nev), align="center", font=("Courier", 24, "normal"))

        #a fő játék ciklus
        while True:
            valtozoletrehozas.game.wn.update()
            #megnézni hozzá ér-e a a kajához
            if valtozoletrehozas.snake.fej.distance(valtozoletrehozas.food.kaja)<20:
                #random helyre elrakni a kaját
                x=random.randint(-390,390)
                y=random.randint(-390,390)
                valtozoletrehozas.food.kaja.goto(x,y)
                #a játékos pontot szerezz
                valtozoletrehozas.snake.hit_score+=1
                #A kigyó teste
                test=Body()
                valtozoletrehozas.snake.test_darabok.append(test.test_darab)
                # eredmény kiírása
                valtozoletrehozas.game.pont.clear()
                valtozoletrehozas.game.pont.write("Pont: {0}  Név: {1}".format(valtozoletrehozas.snake.hit_score,valtozoletrehozas.snake.nev), align="center", font=("Courier", 24, "normal"))
            # mozgatni az utolsó darabtól az elsőig forditva
            for i in range(len(valtozoletrehozas.snake.test_darabok)-1,0,-1):
                x=valtozoletrehozas.snake.test_darabok[i-1].xcor()
                y=valtozoletrehozas.snake.test_darabok[i-1].ycor()
                valtozoletrehozas.snake.test_darabok[i].goto(x,y)
                
            # az első test darabot oda rakni a fejhez
            if len(valtozoletrehozas.snake.test_darabok)>0:
                x=valtozoletrehozas.snake.fej.xcor()
                y=valtozoletrehozas.snake.fej.ycor()
                valtozoletrehozas.snake.test_darabok[0].goto(x,y)    


            #megnézni hogy hozzá ér-e a falhoz
            if valtozoletrehozas.snake.fej.xcor()>390 or valtozoletrehozas.snake.fej.xcor()<-390 or valtozoletrehozas.snake.fej.ycor()>390 or valtozoletrehozas.snake.fej.ycor()<-390:
                Game.jatekvege()
            #megnézni milyek irányba mozduljon el a kigyó
            valtozoletrehozas.snake.mozgas()
            
            #ütközik-e a fej a testel
            try:
                #ha ütközik vége a meghivóm a jatekveg függvényt
                for i in range(len(valtozoletrehozas.snake.test_darabok)):
                    if valtozoletrehozas.snake.test_darabok[i].distance(valtozoletrehozas.snake.fej)<20:
                        Game.jatekvege()
                time.sleep(valtozoletrehozas.game.delay)
            except:
                pass
        valtozoletrehozas.game.wn.mainloop()
    def jatekvege():
        #ki írni az eredményt a fájlba
        with open("pontok.txt","at") as f:
            f.write("Egy játékos mód:\n")
            f.write("Pont: {0}  Név: {1}\n".format(valtozoletrehozas.snake.hit_score,valtozoletrehozas.snake.nev))
        time.sleep(1)
        #alap helyzetbe állitás a kigyót
        valtozoletrehozas.snake.fej.goto(0,0)
        valtozoletrehozas.snake.fej.direction="stop"
        #a test darabok törlése
        for i in range(len(valtozoletrehozas.snake.test_darabok)):
            valtozoletrehozas.snake.test_darabok[i].hideturtle()               
        #kiüriteni a test_darabok listát
        valtozoletrehozas.snake.test_darabok.clear()
        #felugró ablak elkészitése de csak egyszer készitem el hogy buttonok ne többször szerepljenek
        valtozoletrehozas.game.felugro.deiconify()
        if valtozoletrehozas.game.mar_jatszott==False:
            ujjatek_button=Button(valtozoletrehozas.game.felugro,text="Uj játék",command=Game.jatekinditas)
            ujjatek_button.pack()
            jatekvege_button=Button(valtozoletrehozas.game.felugro,text="Kilépés",command=exit)
            jatekvege_button.pack()
            valtozoletrehozas.game.mar_jatszott=True
        #a pont kinullázása
        valtozoletrehozas.snake.hit_score=0
        valtozoletrehozas.game.felugro.mainloop()
        
                  
