import turtle as t

a = 0

def init():
    t.speed(0)
    t.colormode(255)
    t.pensize(0)

def spikeball1(size, sweep_ang, mult_ang, distance):
    t.pensize(size)
    t.pendown()
    for i in range(0,sweep_ang):
        t.pencolor(0,0,0)
        t.forward(distance)
        t.backward(distance)
        t.left(mult_ang)

def spikeball2(size, start_ang, sweep_ang, mult_ang, show_ang, distance):
    
    t.pensize(size)
    
    t.left(start_ang)
    a = start_ang
    print(a)    
    
    for i in range(0,sweep_ang):
        t.pencolor(255,255,0)
        t.pendown()
        t.forward(distance*0.03333333)
        t.pencolor(0,0,255)
        t.penup()
        t.forward(distance*0.3)
        t.pendown()
        t.forward(distance*(2/3))
        t.penup()
        t.backward(distance)
        t.left(mult_ang)
        if (show_ang == True):
            a = a + mult_ang
            print(a)
        
    #t.left(abs((start_ang + (sweep_ang*mult_ang)) - 360))
    t.setheading(0)

def spikeball3(size, start_ang, sweep_ang, mult_ang, show_ang, distance):
    
    t.pensize(size)
    
    t.left(start_ang)
    a = start_ang
    print(a)
    
    for i in range(0,sweep_ang):
        t.pencolor(255,0,0)
        t.penup()
        t.forward(distance*0.04375)
        t.pendown()
        t.forward(distance*0.01875)
        t.pencolor(255,0,255)
        t.penup()
        t.forward(distance*0.3125)
        t.pendown()
        t.forward(distance*0.625)
        t.penup()
        t.backward(distance)
        t.left(mult_ang)
        if (show_ang == True):
            a = a + mult_ang
            if (a == 360):
                a = 0
            print(a)
        
    #t.right(abs((start_ang + (sweep_ang*mult_ang)) - 360))
    t.setheading(0)

def boxprep(init_ang, distance, angle):
    t.left(init_ang)
    t.penup()
    t.forward(distance)
    t.left(angle)
    t.forward(distance)

def box(size, distance):
    t.pendown()
    t.pensize(size)
    for i in range(0,4):
        t.pencolor(0,0,0)
        t.left(90)
        t.forward(distance)
    t.penup()
    t.home()
    t.setheading(0)


init()
spikeball1(2, 180, 2, 100)
spikeball2(0, 46, 90, 2, False, 150)
spikeball3(0, 226, 90, 2, False, 160)
for i in [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]:
    boxprep(i, 170, 90)
    box(3, 340)
    
t.hideturtle()
t.exitonclick()
