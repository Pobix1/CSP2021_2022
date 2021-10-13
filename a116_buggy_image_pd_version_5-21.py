#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
legs = 6
leg_length = 70
leg_angle = 380 / legs
painter.pensize(5)
legs_drawn = 0
while (legs_drawn < legs):
  painter.goto(0,0)
  painter.setheading(leg_angle*legs_drawn)
  painter.forward(leg_length)
  legs_drawn = legs_drawn + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()