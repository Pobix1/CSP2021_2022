# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import turtle 
import turtle as timer
import turtle as color
import leaderboard as lb
#-----game configuration----
score=0

#-----initialize turtle-----
font_setup=("Arial",20,"normal")
#score variables
score_writer=turtle
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0,375)
score_writer.pendown
#dot varibales
dot=trtl.Turtle()
dot.shape("circle")
dot.fillcolor("cyan")
dot.shapesize(2)
dot.speed(0)
dot.penup()
#counter varibales
counter=timer.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-700,375)
counter.pendown
timer = 30
counter_interval = 1000 
timer_up = False
#color varibales
color.penup()
color.hideturtle()
color.speed(0)
colors= ['red','blue','yellow']
stamps=0
color.shape
leaderboard_file_name="a122_leaderboard.txt"
leader_names_list=[]
leader_scores_list=[]
player_name=input("Enter Name: ")
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

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global dot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, dot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, dot, score)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        manage_leaderboard()
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

def start_game():
    stamps=0
    while (stamps<100):
        coloring()
        stamps+=1
    dot.onclick(dot_clicked)
    counter.getscreen().ontimer(countdown, counter_interval)
#-----events----------------
start_game()
wn=trtl.Screen()
wn.bgcolor()
wn.mainloop()
