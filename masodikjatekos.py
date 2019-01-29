#a második játékos kigyóját is elkészitem
import turtle
from tkinter import Tk,Button
import time
class Snake2(object):
    def __init__(self,x,y):
        #Létrehozom a kigyó tipus változoit
        self.test_darabok=[]
        self.hit_score=0
        self.fej=turtle.Turtle()
        self.fej.speed(0)
        self.fej.shape("triangle")
        self.fej.color("black")
        self.fej.penup()
        self.fej.goto(x,y)
        self.fej.direction="stop"
        self.nev=""
        # segéd változok a fej irányitásához
        self.fel=False
        self.balra=False
        self.jobbra=True
        self.le=False
    #A mozgás koordináció a fejnek
    def go_up():
        if valtozoletrehozas2.snake2.fej.direction!="down":
            valtozoletrehozas2.snake2.fej.direction="up"
            if valtozoletrehozas2.snake2.balra:
                valtozoletrehozas2.snake2.fej.right(90)
                valtozoletrehozas2.snake2.balra=False
            if valtozoletrehozas2.snake2.jobbra:
                valtozoletrehozas2.snake2.fej.left(90)
                valtozoletrehozas2.snake2.jobbra=False
            if valtozoletrehozas2.snake2.le:
                valtozoletrehozas2.snake2.fej.left(180)
                valtozoletrehozas2.snake2.le=False
            valtozoletrehozas2.snake2.fel=True
    def go_down():
        if valtozoletrehozas2.snake2.fej.direction !="up":
            valtozoletrehozas2.snake2.fej.direction="down"
            if valtozoletrehozas2.snake2.fel:
                valtozoletrehozas2.snake2.fej.right(180)
                valtozoletrehozas2.snake2.fel=False
            if valtozoletrehozas2.snake2.jobbra:
                valtozoletrehozas2.snake2.fej.right(90)
                valtozoletrehozas2.snake2.jobbra=False
            if valtozoletrehozas2.snake2.balra:
                valtozoletrehozas2.snake2.fej.left(90)
                valtozoletrehozas2.snake2.balra=False
            valtozoletrehozas2.snake2.le=True
    def go_right():
        if valtozoletrehozas2.snake2.fej.direction !="left":
            valtozoletrehozas2.snake2.fej.direction="right"
            if valtozoletrehozas2.snake2.fel:
                valtozoletrehozas2.snake2.fej.right(90)
                valtozoletrehozas2.snake2.fel=False
            if valtozoletrehozas2.snake2.balra:
                valtozoletrehozas2.snake2.fej.left(180)
                valtozoletrehozas2.snake2.balra=False
            if valtozoletrehozas2.snake2.le:
                valtozoletrehozas2.snake2.fej.left(90)
                valtozoletrehozas2.snake2.le=False
            valtozoletrehozas2.snake2.jobbra=True
        
    def go_left():
        if valtozoletrehozas2.snake2.fej.direction !="right":
            valtozoletrehozas2.snake2.fej.direction="left"
            if valtozoletrehozas2.snake2.fel:
                valtozoletrehozas2.snake2.fej.left(90)
                valtozoletrehozas2.snake2.fel=False
            if valtozoletrehozas2.snake2.jobbra:
                valtozoletrehozas2.snake2.fej.left(180)
                valtozoletrehozas2.snake2.jobbra=False
            if valtozoletrehozas2.snake2.le:
                valtozoletrehozas2.snake2.fej.right(90)
                valtozoletrehozas2.snake2.le=False
            valtozoletrehozas2.snake2.balra=True
    def mozgas(self):
        if valtozoletrehozas2.snake2.fej.direction=="up" :
            y=valtozoletrehozas2.snake2.fej.ycor()
            valtozoletrehozas2.snake2.fej.sety(y+20)
     
        if valtozoletrehozas2.snake2.fej.direction=="down":
            y=valtozoletrehozas2.snake2.fej.ycor()
            valtozoletrehozas2.snake2.fej.sety(y-20)

        if valtozoletrehozas2.snake2.fej.direction=="left":
            x=valtozoletrehozas2.snake2.fej.xcor()
            valtozoletrehozas2.snake2.fej.setx(x-20)

        if valtozoletrehozas2.snake2.fej.direction=="right":
            x=valtozoletrehozas2.snake2.fej.xcor()
            valtozoletrehozas2.snake2.fej.setx(x+20)

class Jatek2(object):
    def __init__(self):
        #felugró ablak elkészitése
        self.felugro=Tk()
        self.felugro.geometry("300x300")
        self.felugro.withdraw()
        #a játék gyorsasága
        self.delay=0.1
        #segéd változó ahhoz hogy játszott-e már hogy ne hozza folyton létre a buttonokat
        self.mar_jatszott=False
        #pontok ki írása és törlése az előző szöveg
        self.pont = turtle.Turtle()
        self.pont.speed(0)
        self.pont.shape("square")
        self.pont.color("Black")
        self.pont.penup()
        self.pont.hideturtle()
        self.pont.goto(0, 360)
        self.pont.clear()
        self.pont.write("pont: 0 Név:", align="center", font=("Courier", 24, "normal"))
        #elkészitem a pályát
        self.wn=turtle.Screen()
        self.wn.title("Snake játék")
        self.wn.bgcolor("yellow")
        self.wn.setup(width=800,height=800)
        self.wn.tracer(0)
        #A billentyű beolvasás
        self.wn.listen()
        self.wn.onkeypress(Snake2.go_up,"Up")
        self.wn.onkeypress(Snake2.go_down,"Down")
        self.wn.onkeypress(Snake2.go_left,"Left")
        self.wn.onkeypress(Snake2.go_right,"Right")
#azért hozom ezt létre hogy másik fájlban is elérjem és itt is tudjam használni
def valtozoletrehozas2():
    valtozoletrehozas2.snake2=Snake2(200,200)
    valtozoletrehozas2.game2=Jatek2()
valtozoletrehozas2()
