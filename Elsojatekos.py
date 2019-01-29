# a Snake objektum elkészitése
import turtle
from tkinter import Tk,Button
import time
import random
from snake_object import Kaja

class Snake(object):
    def __init__(self,x,y):
        #létrehozom a kigyó tipus változoit
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
        if valtozoletrehozas.snake.fej.direction!="down":
            valtozoletrehozas.snake.fej.direction="up"
            if valtozoletrehozas.snake.balra:
                valtozoletrehozas.snake.fej.right(90)
                valtozoletrehozas.snake.balra=False
            if valtozoletrehozas.snake.jobbra:
                valtozoletrehozas.snake.fej.left(90)
                valtozoletrehozas.snake.jobbra=False
            if valtozoletrehozas.snake.le:
                valtozoletrehozas.snake.fej.left(180)
                valtozoletrehozas.snake.le=False
            valtozoletrehozas.snake.fel=True
    def go_down():
        if valtozoletrehozas.snake.fej.direction !="up":
            valtozoletrehozas.snake.fej.direction="down"
            if valtozoletrehozas.snake.fel:
                valtozoletrehozas.snake.fej.right(180)
                valtozoletrehozas.snake.fel=False
            if valtozoletrehozas.snake.jobbra:
                valtozoletrehozas.snake.fej.right(90)
                valtozoletrehozas.snake.jobbra=False
            if valtozoletrehozas.snake.balra:
                valtozoletrehozas.snake.fej.left(90)
                valtozoletrehozas.snake.balra=False
            valtozoletrehozas.snake.le=True
    def go_right():
        if valtozoletrehozas.snake.fej.direction !="left":
            valtozoletrehozas.snake.fej.direction="right"
            if valtozoletrehozas.snake.fel:
                valtozoletrehozas.snake.fej.right(90)
                valtozoletrehozas.snake.fel=False
            if valtozoletrehozas.snake.balra:
                valtozoletrehozas.snake.fej.left(180)
                valtozoletrehozas.snake.balra=False
            if valtozoletrehozas.snake.le:
                valtozoletrehozas.snake.fej.left(90)
                valtozoletrehozas.snake.le=False
            valtozoletrehozas.snake.jobbra=True
        
    def go_left():
        if valtozoletrehozas.snake.fej.direction !="right":
            valtozoletrehozas.snake.fej.direction="left"
            if valtozoletrehozas.snake.fel:
                valtozoletrehozas.snake.fej.left(90)
                valtozoletrehozas.snake.fel=False
            if valtozoletrehozas.snake.jobbra:
                valtozoletrehozas.snake.fej.left(180)
                valtozoletrehozas.snake.jobbra=False
            if valtozoletrehozas.snake.le:
                valtozoletrehozas.snake.fej.right(90)
                valtozoletrehozas.snake.le=False
            valtozoletrehozas.snake.balra=True
   
    #a koordináta rendszerben való irányitás
    def mozgas(self):
        if valtozoletrehozas.snake.fej.direction=="up" :
            y=valtozoletrehozas.snake.fej.ycor()
            valtozoletrehozas.snake.fej.sety(y+20)
     
        if valtozoletrehozas.snake.fej.direction=="down":
            y=valtozoletrehozas.snake.fej.ycor()
            valtozoletrehozas.snake.fej.sety(y-20)

        if valtozoletrehozas.snake.fej.direction=="left":
            x=valtozoletrehozas.snake.fej.xcor()
            valtozoletrehozas.snake.fej.setx(x-20)

        if valtozoletrehozas.snake.fej.direction=="right":
            x=valtozoletrehozas.snake.fej.xcor()
            valtozoletrehozas.snake.fej.setx(x+20)

        

# a pálya létre hozása
class Jatek(object):
    def __init__(self):
        #felugró ablak hogy játszott-e már
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
        #a pálya létrehozása
        self.wn=turtle.Screen()
        self.wn.title("Snake játék")
        self.wn.bgcolor("yellow")
        self.wn.setup(width=800,height=800)
        self.wn.tracer(0)
        #A billentyű beolvasás
        self.wn.listen()
        self.wn.onkeypress(Snake.go_up,"w")
        self.wn.onkeypress(Snake.go_down,"s")
        self.wn.onkeypress(Snake.go_left,"a")
        self.wn.onkeypress(Snake.go_right,"d")
#létre hozom ebben a függvényben a változókat hogy másikfájlban is elérjem őket mert itt is szeretném használni
def valtozoletrehozas():
    valtozoletrehozas.snake=Snake(0,0)
    valtozoletrehozas.game=Jatek()
    valtozoletrehozas.food=Kaja(random.randint(-390,390),random.randint(-390,390))
valtozoletrehozas()
