import turtle
import time
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple analog clock by NGB")
wn.tracer(0)

# create our drwing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(h,m,s,pen):
    
    #Draw the clock face
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)
    
    #Drwa the lines for the hour
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
    
        
    #draw hour hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)
    
    #draw minute hand
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (m / 60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)
    
     #draw second hand
    pen.penup()
    pen.goto(0,0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s / 60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(70)
while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    
    
    draw_clock(h,  m, s,pen)
    wn.update()
    
    time.sleep(1)
    
    pen.clear()
    

wn.mainloop()