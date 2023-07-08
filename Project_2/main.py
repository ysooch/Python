######################################################
# Project: <MarioGame Project>
# UIN: <673272656>
# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-2-ychan57#main.py>
# ######################################################

#########################################################

# Explanation of game to be graded :

# I have the total of 3 levels, and if the player gets 3pts, the level changed to level 2, and if the player gets 9pts, the level changed to level 3, and if the player gets 18pts, the game will be ended with end message screen.

# The player can get 1pt when collide with benefit object at the level 1, get 2pt at the level 2, get 3pt at the level 3.

#




import turtle
import random

# Show start screen
s = turtle.Screen()
s.setup(300,300)
s.screensize(300,300)
s.bgcolor("white")

# Display the game's name
text1 = turtle.Turtle()
text1.hideturtle()
text1.color("red")
text1.penup()
text1.goto(-65,30)
text1.pendown()
text1.write("MARIO GAME",
         move=False, align='left',
         font=('Arial', 15, 'normal'))

# Display how to start the game
text1.color("black")
text1.penup()
text1.goto(-105,0)
text1.pendown()
text1.write("Press 's' to start the game",
         move=False, align='left',
         font=('Arial', 12, 'normal'))

# Explanation for game's rule
text1.color("black")
text1.penup()
text1.goto(-70,-25)
text1.pendown()
text1.write("This game has 3 levels:",
         move=False, align='left',
         font=('Arial', 9, 'normal'))
text1.color("black")
text1.penup()
text1.goto(-115,-50)
text1.pendown()
text1.write("3pt - level1, 9pt - level2, 18pt - level3",
         move=False, align='left',
         font=('Arial', 9, 'normal'))



# Main function
def main():

  # Show game screen
  s = turtle.Screen()
  s.setup(300,300)
  s.screensize(300,300)
  
  # Set background image
  turtle.bgpic("background.png")
  
  # Set the initial level, scores, lives for the game
  level = 1
  scores = 0
  lives = 3

  # Display the level, scores, lives on the screen
  text2 = turtle.Turtle()
  text2.hideturtle()
  text2.color("black")
  text2.penup()
  text2.goto(60, 105)
  text2.pendown()
  text2.write("Level: "+ str(level) ,
         move=False, align='left',
         font=('Arial', 10, 'normal'))
  text2.penup()
  text2.goto(60, 85)
  text2.pendown()
  text2.write("Scores : "+ str(scores) ,
         move=False, align='left',
         font=('Arial', 10, 'normal'))
  text2.penup()
  text2.goto(60, 65)
  text2.write("Lives : "+ str(lives) ,
         move=False, align='left',
         font=('Arial', 10, 'normal'))
  
  # Make a variable for turtle's position
  w, h = s.screensize()

  # Make a list for game objects
  game_objects = []

  # Set the game objects characteristics
  mario_dict = {"t": turtle.Turtle(), "x": 0, "y": -h/2+45, "radius": 20, "image":"mario.gif", "type":"mario"}
  bomb_dict = {"t": turtle.Turtle(), "x": 130, "y": h/2-76, "radius": 20, "image":"bomb.gif", "type":"bomb1"}
  bomb2_dict = {"t": turtle.Turtle(), "x": -25, "y": h/2-120, "radius": 20, "image":"bomb.gif", "type":"bomb2"}
  bomb3_dict = {"t": turtle.Turtle(), "x": 50, "y": -h/2+133, "radius": 20, "image":"bomb.gif", "type":"bomb3"}
  bomb4_dict = {"t": turtle.Turtle(), "x": -105, "y": -h/2+89, "radius": 20, "image":"bomb.gif", "type":"bomb4"}
  coin1_dict = {"t": turtle.Turtle(), "x": random.randint(-w/2,w/2), "y": h/2-30, "radius": 20, "image":"coin.gif", "type":"coin"}
 
  # Append dictionary to the list
  game_objects.append(mario_dict)
  game_objects.append(bomb_dict)
  game_objects.append(bomb2_dict)
  game_objects.append(bomb3_dict)
  game_objects.append(bomb4_dict)
  game_objects.append(coin1_dict)

  # Set the player to the initial position
  game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])


  # Display game objects on the screen
  for obj in game_objects:

    img = obj["image"] 
    t = obj["t"]
    s.addshape(img)
    t.shape(img)

  # Move players by using onkey events
  def up():
    game_objects[0]["t"].setheading(90)
    game_objects[0]["t"].forward(44)

  def down():
    game_objects[0]["t"].setheading(270)
    game_objects[0]["t"].forward(44)

  def left():
    game_objects[0]["t"].setheading(180)
    game_objects[0]["t"].forward(44)

  def right():
    game_objects[0]["t"].setheading(0)
    game_objects[0]["t"].forward(44)
  
  # Call the key events
  s.onkey(left, "Left")
  s.onkey(right, "Right")
  s.onkey(up, "Up")
  s.onkey(down, "Down")





  # Start game
  game_state = "play"


  # Make a condition function until the game ends
  while (game_state != "over"):

  
    for obj in game_objects:
      obj["t"].clear()




    # Set the condition for level 1
    if (level == 1):
      for obj in game_objects:
        s.tracer(0)
        if (obj["type"] != "mario"):
          obj["t"].goto(obj["x"], obj["y"])


      # Make a loop for position change of harm objects and benefit object
      for obj in game_objects:
        s.tracer(0)
        
        if (obj["type"] == "bomb1"):

          # The reason I set level*something is to change the speed when the level is changed
          obj["x"] -= level*0.1 

          if (obj["x"] < -w/2 - obj["radius"]):
            obj["y"] = h/2-76
            obj["x"] = w/2

        if (obj["type"] == "bomb3"):
          obj["x"] += level*0.05

          if (obj["x"] > w/2 - obj["radius"]):
            obj["y"] = h/2-120
            obj["x"] = -w/2
      
        if (obj["type"] == "bomb2"):
          obj["x"] -= level*0.1

          if (obj["x"] < -w/2 - obj["radius"]):
            obj["y"] = -h/2+133
            obj["x"] = w/2
        
        if (obj["type"] == "bomb4"):
          obj["x"] += level*0.05

          if (obj["x"] > w/2 - obj["radius"]):
            obj["y"] = -h/2+89
            obj["x"] = -w/2

    
      # Collision function when player touches other harm obejcts
      if (game_objects[0]["t"].distance(game_objects[1]["t"]) < 20):

        # When the collision happens, move player to its initial position
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1

        # Change the level, scores, lives to new one and display them on the screen
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))

      # Same code for collision with another objects  
      elif ((game_objects[0]["t"]).distance(game_objects[2]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
     
      # Same code for collision with another objects  
      elif ((game_objects[0]["t"]).distance(game_objects[3]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
      
      # Same code for collision with another objects  
      elif (game_objects[0]["t"].distance(game_objects[4]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
       
      # Collision function when player touches benefit obejcts
      elif (game_objects[0]["t"].distance(game_objects[5]["t"]) < 20):
        

        # When player collide with benefit obj, goto its original position
        game_objects[0]["x"] = 0
        game_objects[0]["y"] = -h/2+45
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        
        
        # When player collide with benefit obj, change the benefit object's x position randomly
        game_objects[5]["x"] = random.randint(-w/2+20, w/2-20)
        game_objects[5]["y"] = h/2-35
        game_objects[5]["t"].goto(game_objects[5]["x"], game_objects[5]["x"])
        

        # When player collide with benefit obj, get scores
        scores += 1

        # Renew the whole scores, level, lives displayment
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        




      # When player reaches the goal, change the level and renew displayment
      if scores == 3:
        level += 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))



    # Same code with level 1, but only the score points are changed (1pt to 2pt)
    if (level == 2):
      for obj in game_objects:
        if (obj["type"] != "mario"):
          obj["t"].goto(obj["x"], obj["y"])

      for obj in game_objects:
        s.tracer(0)

        if (obj["type"] == "bomb1"):
          obj["x"] -= level*0.1

          if (obj["x"] < -w/2 - obj["radius"]):
            obj["y"] = -h/2+75
            obj["x"] = w/2

        if (obj["type"] == "bomb3"):
          obj["x"] -= level*0.05

          if (obj["x"] < -w/2 - obj["radius"]):
            obj["y"] = -h/2+125
            obj["x"] = w/2
      
        if (obj["type"] == "bomb2"):
          obj["x"] += level*0.05

          if (obj["x"] > w/2 - obj["radius"]):
            obj["y"] = h/2-125
            obj["x"] = -w/2
        
        if (obj["type"] == "bomb4"):
          obj["x"] += level*0.1

          if (obj["x"] > w/2 - obj["radius"]):
            obj["y"] = h/2-75
            obj["x"] = -w/2
    
      if (game_objects[0]["t"].distance(game_objects[1]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))

      if ((game_objects[0]["t"]).distance(game_objects[2]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
     
      if ((game_objects[0]["t"]).distance(game_objects[3]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
      
      if (game_objects[0]["t"].distance(game_objects[4]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
       
      if (game_objects[0]["t"].distance(game_objects[5]["t"]) < 20):

        game_objects[0]["x"] = 0
        game_objects[0]["y"] = -h/2+45
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        
        
        
        game_objects[5]["x"] = random.randint(-w/2+20, w/2-20)
        game_objects[5]["y"] = h/2-35
        game_objects[5]["t"].goto(game_objects[5]["x"], game_objects[5]["x"])

        scores += 2
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))

      if scores == 9:
        level += 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))






    # Same code with level 2, but only the score points are changed (2pt to 3pt)
    if (level == 3):
      for obj in game_objects:
        if (obj["type"] != "mario"):
          obj["t"].goto(obj["x"], obj["y"])

      for obj in game_objects:
        s.tracer(0)

        if (obj["type"] == "bomb1"):
          obj["x"] -= level*0.1

          if (obj["x"] < -w/2 - obj["radius"]):
            obj["y"] = -h/2+75
            obj["x"] = w/2

        if (obj["type"] == "bomb3"):
          obj["x"] -= level*0.05

          if (obj["x"] < -w/2 - obj["radius"]):
            obj["y"] = -h/2+125
            obj["x"] = w/2
      
        if (obj["type"] == "bomb2"):
          obj["x"] += level*0.05

          if (obj["x"] > w/2 - obj["radius"]):
            obj["y"] = h/2-125
            obj["x"] = -w/2
        
        if (obj["type"] == "bomb4"):
          obj["x"] += level*0.1

          if (obj["x"] > w/2 - obj["radius"]):
            obj["y"] = h/2-75
            obj["x"] = -w/2
    
      if (game_objects[0]["t"].distance(game_objects[1]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))

      if ((game_objects[0]["t"]).distance(game_objects[2]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
     
      if ((game_objects[0]["t"]).distance(game_objects[3]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
      
      if (game_objects[0]["t"].distance(game_objects[4]["t"]) < 20):
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        lives -= 1
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
       
      if (game_objects[0]["t"].distance(game_objects[5]["t"]) < 20):
        
        game_objects[0]["x"] = 0
        game_objects[0]["y"] = -h/2+45
        game_objects[0]["t"].goto(game_objects[0]["x"], game_objects[0]["y"])
        
        game_objects[5]["x"] = random.randint(-w/2+20, w/2-20)
        game_objects[5]["y"] = h/2-35
        game_objects[5]["t"].goto(game_objects[5]["x"], game_objects[5]["x"])
        scores += 3
        text2.clear()
        text2.penup()
        text2.goto(60, 105)
        text2.pendown()
        text2.write("Level: "+ str(level) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 85)
        text2.pendown()
        text2.write("Scores : "+ str(scores) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
        text2.penup()
        text2.goto(60, 65)
        text2.write("Lives : "+ str(lives) ,
              move=False, align='left',
              font=('Arial', 10, 'normal'))
       

    s.update()


    # End game when scores == 18
    if (scores == 18):
        game_state = "over"
        
        # Change to end screen
        s.bgpic("blue.png")
        s.clear()

        # Show the "game ends", final level and scores
        text3 = turtle.Turtle()
        text3.hideturtle()
        text3.color("white")
        text3.penup()
        text3.goto(-105,0)
        text3.pendown()
        text3.write("Congratulations",
          move=False, align='left',
          font=('Arial', 20, 'normal'))
        text3.penup()
        text3.goto(-65,-20)
        text3.pendown()
        text3.write("Scores: "+ str(scores) + "   " + "Level: " + str(level), 
          move=False, align='left',
          font=('Arial', 10, 'normal'))
        s.bgpic("blue.png")
        
    # End game when lives == 0
    if (lives == 0):
        game_state = "over"
        
        # Change to end screen
        s.bgpic("green.png")
        s.clear()
       
        # Show the "game ends", final level and scores
        text3 = turtle.Turtle()
        text3.hideturtle()
        text3.color("red")
        text3.penup()
        text3.goto(-80,0)
        text3.pendown()
        text3.write("Game Over",
          move=False, align='left',
          font=('Arial', 20, 'normal'))
        text3.penup()
        text3.goto(-65,-20)
        text3.pendown()
        text3.write("Scores: "+ str(scores) + "   " + "Level: " + str(level), 
          move=False, align='left',
          font=('Arial', 10, 'normal'))
        s.bgpic("green.png")


# Run the main code for starting game
def start():
 s.clear()
 main()

# If pressing the button 's', game will be start
s.listen()
s.onkey(start, "s")




