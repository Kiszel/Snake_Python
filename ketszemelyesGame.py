from tkinter import Tk,Button
from Elsojatekos import Snake,Jatek,valtozoletrehozas
from masodikjatekos import Snake2,Jatek2,valtozoletrehozas2
from snake_object import Kaja,Body,MasodikjatekosBody
import random
import turtle
import time
import sys 
class KetszemelyesGame(object):
    def jatekinditas():
        #Ha nem elsőnek játszik akkor rejtse el a felúgro ablakot és törölje a szöveget amit belle lett írva
        if valtozoletrehozas.snake.nev!="":
            valtozoletrehozas2.game2.felugro.withdraw()
        else:
            #nevek bekerese
            valtozoletrehozas.snake.nev=input("Kérem adja meg a nevét")
            valtozoletrehozas2.snake2.nev=input("Kérem adja meg a nevét")
            #pontok ki írása és törlése az előző szöveg
            valtozoletrehozas.game.pont.clear()
        valtozoletrehozas2.game2.pont.clear()
        valtozoletrehozas2.game2.pont.write("Első játékos neve:{0} Első játékos pont: 0  Második játékos neve:{1} Második játékos pont: 0".format(valtozoletrehozas.snake.nev,valtozoletrehozas2.snake2.nev), align="center", font=("Courier",9, "normal"))
        #a fő játék ciklus
        while True:
            valtozoletrehozas2.game2.wn.update()
            #megnézni hozzá ér-e a a kajához
            if valtozoletrehozas.snake.fej.distance(valtozoletrehozas.food.kaja)<20:
                #random helyre elrakni a kaját
                x=random.randint(-390,390)
                y=random.randint(-390,390)
                valtozoletrehozas.food.kaja.goto(x,y)
                #a játékos pontot szerezz
                valtozoletrehozas.snake.hit_score+=1
                valtozoletrehozas2.game2.pont.clear()
                valtozoletrehozas2.game2.pont.write("Első játékos neve:{0} Első játékos pont: {1}  Második játékos neve:{2} Második játékos pont: {3}".format(valtozoletrehozas.snake.nev,valtozoletrehozas.snake.hit_score,valtozoletrehozas2.snake2.nev,valtozoletrehozas2.snake2.hit_score), align="center", font=("Courier",9, "normal"))
                #A kigyó teste
                test=Body()
                valtozoletrehozas.snake.test_darabok.append(test.test_darab)
            if valtozoletrehozas2.snake2.fej.distance(valtozoletrehozas.food.kaja)<20:
                #random helyre elrakni a kaját
                x=random.randint(-390,390)
                y=random.randint(-390,390)
                valtozoletrehozas.food.kaja.goto(x,y)
                #a játékos pontot szerezz
                valtozoletrehozas2.snake2.hit_score+=1
                valtozoletrehozas2.game2.pont.clear()
                valtozoletrehozas2.game2.pont.write("Első játékos neve:{0} Első játékos pont: {1}  Második játékos neve:{2} Második játékos pont:{3}".format(valtozoletrehozas.snake.nev,valtozoletrehozas.snake.hit_score,valtozoletrehozas2.snake2.nev,valtozoletrehozas2.snake2.hit_score), align="center", font=("Courier",9, "normal"))
                #A kigyó teste
                test2=MasodikjatekosBody()
                valtozoletrehozas2.snake2.test_darabok.append(test2.test_darab)

            
            # mozgatni az utolsó darabtól az elsőig forditva
            for i in range(len(valtozoletrehozas2.snake2.test_darabok)-1,0,-1):
                x=valtozoletrehozas2.snake2.test_darabok[i-1].xcor()
                y=valtozoletrehozas2.snake2.test_darabok[i-1].ycor()
                valtozoletrehozas2.snake2.test_darabok[i].goto(x,y)
                
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
            # az első test darabot oda rakni a fejhez
            if len(valtozoletrehozas2.snake2.test_darabok)>0:
                x=valtozoletrehozas2.snake2.fej.xcor()
                y=valtozoletrehozas2.snake2.fej.ycor()
                valtozoletrehozas2.snake2.test_darabok[0].goto(x,y)
             
            #megnézni hogy hozzá ér-e a falhoz
            if valtozoletrehozas.snake.fej.xcor()>390 or valtozoletrehozas.snake.fej.xcor()<-390 or valtozoletrehozas.snake.fej.ycor()>390 or valtozoletrehozas.snake.fej.ycor()<-390:
                KetszemelyesGame.jatekvege()
            #megnézni melyik irányba mozduljon el a kigyó
            valtozoletrehozas.snake.mozgas()

            #megnézni hogy hozzá ér-e a falhoz a masodik játékos
            if valtozoletrehozas2.snake2.fej.xcor()>390 or valtozoletrehozas2.snake2.fej.xcor()<-390 or valtozoletrehozas2.snake2.fej.ycor()>390 or valtozoletrehozas2.snake2.fej.ycor()<-390:
                KetszemelyesGame.jatekvege()
            #megnézni melyik irányba mozduljon el a kigyó
            valtozoletrehozas2.snake2.mozgas()
            #ütközik e a két fej
            if valtozoletrehozas.snake.fej.distance(valtozoletrehozas2.snake2.fej)<20:
                KetszemelyesGame.jatekvege()
            #ütközik-e a fej a testel
            try:
                for i in range(len(valtozoletrehozas.snake.test_darabok)):
                    #ütközik-e a első játékos saját magával
                    if valtozoletrehozas.snake.test_darabok[i].distance(valtozoletrehozas.snake.fej)<20:
                        KetszemelyesGame.jatekvege()
                    #ütközik-e a Második játékos a másik játékossal
                    if valtozoletrehozas.snake.test_darabok[i].distance(valtozoletrehozas2.snake2.fej)<20:
                        KetszemelyesGame.jatekvege()
                #ütközik-e a masodik játékos saját magával
                for i in range(len(valtozoletrehozas2.snake2.test_darabok)):
                    if valtozoletrehozas2.snake2.test_darabok[i].distance(valtozoletrehozas2.snake2.fej)<20:
                        KetszemelyesGame.jatekvege()
                #ütközik-e a Első játékos a másik játékossal
                    if valtozoletrehozas2.snake2.test_darabok[i].distance(valtozoletrehozas.snake.fej)<20:
                        KetszemelyesGame.jatekvege()
                time.sleep(valtozoletrehozas2.game2.delay)
            except:
                pass
        game2.wn.mainloop()
    def jatekvege():
        #a segéd változokat meghívni amit már a snake_object fájlban létrehoztam
        #ki írni az eredményt a fájlba
        with open("pontok.txt","at") as f:
            f.write("Két játékos mód:\n") 
            f.write("Első játékos név:{0} pont:{1} \t Második játékos név:{2} pont:{3}\n".format(valtozoletrehozas.snake.nev,valtozoletrehozas.snake.hit_score,valtozoletrehozas2.snake2.nev,valtozoletrehozas2.snake2.hit_score))
        time.sleep(1)
        #alap helyzetbe állitás a kigyókat
        valtozoletrehozas2.snake2.fej.goto(200,200)
        valtozoletrehozas2.snake2.fej.direction="stop"
        valtozoletrehozas.snake.fej.goto(0,0)
        valtozoletrehozas.snake.fej.direction="stop"
        #a test darabok törlése
        for i in range(len(valtozoletrehozas.snake.test_darabok)):
            valtozoletrehozas.snake.test_darabok[i].hideturtle()
        #a test darabok törlése
        for i in range(len(valtozoletrehozas2.snake2.test_darabok)):
            valtozoletrehozas2.snake2.test_darabok[i].hideturtle()  
        #kiüriteni a test_darabok listát
        valtozoletrehozas2.snake2.test_darabok.clear()
        valtozoletrehozas.snake.test_darabok.clear()
        #kiüriteni a test_darabok listát
        valtozoletrehozas.snake.test_darabok.clear()
        #felugró ablak elkészitése de csak egyszer hogy a buttonok ne szerepeljenek többször
        valtozoletrehozas2.game2.felugro.deiconify()
        if valtozoletrehozas2.game2.mar_jatszott==False:
            ujjatek_button=Button(valtozoletrehozas2.game2.felugro,text="Új játék",command=KetszemelyesGame.jatekinditas)
            ujjatek_button.pack()
            jatekvege_button=Button(valtozoletrehozas2.game2.felugro,text="Kilépés",command=exit)
            jatekvege_button.pack()
            valtozoletrehozas2.game2.mar_jatszott=True
        #a pontok kinullázása
        valtozoletrehozas.snake.hit_score=0
        valtozoletrehozas2.snake2.hit_score=0
        valtozoletrehozas2.game2.felugro.mainloop()
    

