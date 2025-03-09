import random
import turtle

screen = turtle.Screen()
speed = 1
screen.title("Recycling Game")
turtle.Screen().bgcolor("black")
border = turtle.Turtle()
border.speed(0)
border.pencolor("white")
border.pensize(10)
border.color("white","blue")
border.penup()
border.goto(-200,-200)
border.begin_fill()
border.pendown()
for _i in range(1,5):
  border.forward(425)
  border.left(90)
border.end_fill()
border.hideturtle()
# Player
player = turtle.Turtle()
player.penup()
player.shape("turtle")
player.color("green")
player.speed(0)
# Fish ( Points ) 
fish = turtle.Turtle()
fish.penup()
fish.speed(0)
fish.shape("classic")
fish.color("yellow")
fish.goto(100,100)
# Scoreboard
scoreb = turtle.Turtle()
scoreb.speed(0)
scoreb.color("white")
scoreb.penup()
scoreb.goto(0,-228)
scoreb.write("Score: 0", font=("Bold", 14, "bold italic underline"))
scoreb.hideturtle()
lives = 3
livesb = turtle.Turtle()
livesb.speed(0)
livesb.color("white")
livesb.penup()
livesb.goto(-120,-228)
livesb.write("Lives: " + str(lives),align="left",font=("Bold", 14, "bold italic underline"))

instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("white")
instructions.penup()
instructions.goto(0, -275)
instructions.write("Instructions: You are a Turtle. Your goal is to eat as many fish(yellow coloured triangles)as possible, without accidentally \n eating plastic bags(white coloured circles). Use 'E' to start the game,'A' to turn left, 'D' to turn right, 'W' to speed up and 'S' to slow down. ", 
                    align="center", font=("Arial", 12, "bold"))
instructions.hideturtle()
#plastic bag is enemy
plastic_bags = []

# Def Section
livesb.hideturtle()
def turnLeft():
  print("turn left")
  player.left(30)
def turnRight():
  player.right(30)
def increase():
  global speed
  if speed <= 3 and speed >= 0:
    speed = speed + 1
  elif speed > 3:
    speed = 3
  elif speed < 0:
    speed = 0

def decrease():
  global speed
  if speed > 0:
    speed = speed - 1
  else:
    speed = 0



  
  
# def isCollision(t1, t2):
#   if isinstance(t2, turtle.Turtle):
#     d = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
#     if d < 30:
#       return True    
#   else:
#     for t in t2:
#       d = ((t1.xcor() - t.xcor()) ** 2 + (t1.ycor() - t.ycor()) ** 2) ** 0.5
#       if d < 30:
#         return True
#   return False

def isCollision(t1,t2):
  d = ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5
  if d < 30:
    return True
  else:
    return False
      
activated = False
def activate():
  global activated
  activated = True

turtle.listen()
turtle.onkey(turnLeft,"a")
turtle.onkey(turnRight, "d")
turtle.onkey(increase,"w")
turtle.onkey(decrease,"s")
turtle.onkey(activate,"e")

score = 0

startGame = True  # Initialize the game state

while startGame:
  if not activated:
    player.forward(0)
    continue
  player.forward(speed)
  if (
      player.xcor() > 200
      or player.xcor() < -180
      or player.ycor() > 200
      or player.ycor() < -180
  ):
    player.left(180)

  if isCollision(player, fish):
    x = random.randint(-170, 190)
    y = random.randint(-170, 190)
    fish.goto(x, y)
    score += 1
    scoreb.clear()
    scoreb.write(
        "Score: " + str(score),
        font=("Bold", 14, "bold italic underline")
    )
    plastic_bags.append(turtle.Turtle())
    plastic_bags[len(plastic_bags) - 1].shape("circle")
    plastic_bags[len(plastic_bags) - 1].color("white")
    plastic_bags[len(plastic_bags) - 1].penup()
    plastic_bags[len(plastic_bags) - 1].speed(0)
    x = random.randint(-170, 190)
    y = random.randint(-170, 190)
    plastic_bags[len(plastic_bags) - 1].goto(x, y)
  for a in plastic_bags:
    if isCollision(player, a):
      lives -= 1
      a.hideturtle()  
      plastic_bags.remove(a)  
      livesb.clear()
      livesb.write(
        "Lives:  " + str(lives),
        align="left",
        font=("Bold", 14, "bold italic underline")
    )
      if lives == 0:
        startGame = False        
turtle.update()
turtle.done()





