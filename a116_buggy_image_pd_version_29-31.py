#   a116_buggy_image.py
import turtle as trtl
painter = trtl.Turtle()

#body
painter.hideturtle()
painter.pensize(40)
painter.circle(20)

#words with values/variables
legs = 8
leg_length = 70
leg_angle = 180 / legs
painter.pensize(5)
legs_drawn = 0

#legs drawing
while (legs_drawn < 4):
  painter.goto(0,20)
  painter.setheading(leg_angle*legs_drawn-45)
  painter.forward(leg_length)
  legs_drawn = legs_drawn + 1
while (legs_drawn < legs):
  painter.goto(0,20)
  painter.setheading(leg_angle*legs_drawn+45)
  painter.forward(leg_length)
  legs_drawn = legs_drawn + 1
painter.penup()
painter.pensize(10)
painter.goto(10,-10)
painter.color("red")
painter.pendown()
painter.circle(5)

painter.penup()
painter.goto(-25,-5)
painter.pendown()
painter.circle(5)
painter.hideturtle()
wn = trtl.Screen()



wn = trtl.Screen()
wn.mainloop()