# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import turtle 
import turtle as timer
import turtle as color
#-----game configuration----
score=0

#-----initialize turtle-----
font_setup=("Arial",20,"normal")
score_writer=turtle
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0,375)
dot=trtl.Turtle()
dot.shape("circle")
dot.fillcolor("cyan")
dot.shapesize(2)
dot.speed(0)
dot.penup()
counter=timer.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-700,375)
timer = 30
counter_interval = 1000 
timer_up = False
color.penup()
color.hideturtle()
color.speed(0)
colors= ['red','blue','yellow']
stamps=0
color.shape
#-----game functions--------
def dot_clicked(x,y):
    change_position()
    update_score()

def change_position():
    new_xpos=rand.randint(-650,650)
    new_ypos=rand.randint(-400,400)
    dot.goto(new_xpos,new_ypos)

def update_score():
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def coloring():
    new_xpos=rand.randint(-650,650)
    new_ypos=rand.randint(-400,400)
    color.goto(new_xpos,new_ypos)
    color.fillcolor(rand.choice(colors))
    color.stamp()


#-----events----------------
while (stamps<100):
    coloring()
    stamps+=1
dot.onclick(dot_clicked)
wn=trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.bgcolor()
wn.mainloop()
