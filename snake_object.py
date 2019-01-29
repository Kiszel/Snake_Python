import random
import turtle
class Body(object):
    def __init__(self):
        self.test_darab=turtle.Turtle()
        self.test_darab.speed(0)
        self.test_darab.shape("square")
        self.test_darab.color("gray")
        self.test_darab.penup()
class MasodikjatekosBody(object):
    def __init__(self):
        self.test_darab=turtle.Turtle()
        self.test_darab.speed(0)
        self.test_darab.shape("square")
        self.test_darab.color("gray")
        self.test_darab.penup()

class Kaja(object):
    def __init__(self,x,y):
        self.kaja=turtle.Turtle()
        self.kaja.speed(0)
        self.kaja.shape("square")
        self.kaja.color("blue")
        self.kaja.penup()
        self.kaja.goto(x,y)

