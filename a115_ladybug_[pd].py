#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5

  num_dots = num_dots + 1
#issues 1. xpos=ypos+25 instead of ypos=ypos+25 2. num_dot=num_dots 3. num_dots=1 instead of num_dots=0

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()