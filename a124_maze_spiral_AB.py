import turtle as trtl
import random


M = trtl.Turtle()
M.color("red")
L = trtl.Turtle()
L.pu()
L.goto(-200, 200)
L.pd()
L.pensize(4)
L.ht()
L.speed(10)
count = 500
wall_width =18
door_width =18


def M_up():
    M.setheading(90)
    M.forward(10)
def M_down():
    M.setheading(270)
    M.forward(10)
def M_left():
    M.setheading(180)
    M.forward(10)
def M_right():
    M.setheading(0)
    M.forward(10)

for i in range(25):

    if i < 21:
        door = random.randint  (door_width, count-2*door_width)
        barrier = random.randint(2*wall_width, count - 2*door_width)
        if door < barrier:

            L. forward(door)
            L.penup()
            L.forward(door_width)
            L.pendown()
            L.forward(barrier - door - door_width)


            L.right(90)
            L.forward(wall_width*2)
            L.backward(wall_width*2)
            L.left(90)

            L.forward(count-barrier)


        else:
            L.forward(barrier)


            L.right(90)
            L.forward(wall_width*2)
            L.backward(wall_width*2)
            L.left(90)

            L.forward(door - barrier)
            L.penup()
            L.forward(door_width)
            L.pendown()

            L.forward(count - door - door_width)


        L.right(90)
    count = count - wall_width
    
  


wn = trtl.Screen()
wn.onkeypress(M_up,"Up")
wn.onkeypress(M_down,"Down")
wn.onkeypress(M_left,"Left")
wn.onkeypress(M_right,"Right")
wn.listen()
wn.mainloop()
