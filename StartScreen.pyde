ball_y = 100
y_speed = 4
ball_x = 100
x_speed = 4

def setup():
    global start
    global gamend
    global gamewin
    size(900,800)
    start = True
    gamend = False
    gamewin = False
    
def gameScreen():
    global ball_y
    global ball_x
    global y_speed
    global x_speed
    
    background(255, 227, 254)
    
    fill(227, 242, 255)
    ellipse(ball_x, ball_y, 25, 25)
    
    rect(5, mouseY, 20, 70)
    
    # if ball_x < mouseX + 10 and ball_x > mouseX - 10  and ball_y < 800 and ball_y > 0:
    #     print("bounce")
    #     x_speed = -x_speed
    
    if ball_x == 20 and ball_y > mouseY and ball_y < mouseY + 125:
        print("You win")
        x_speed = -x_speed
    
    # if ball_x < 25:
    #     print("bounceback")
    #     x_speed = 4
    
    if ball_x > 900:
        x_speed = -x_speed
        
    if ball_y < 25:
        y_speed = -y_speed
    
    if ball_y > 775:
        y_speed = -y_speed
    
    if ball_x < 10:
        y_speed = 0
        x_speed = 0
        print("You lose")
        
    
    ball_x = ball_x + x_speed
    ball_y = ball_y + y_speed
    
def startScreen():
        background(255, 255, 176)
        img = loadImage("bathtime.png")
        img2 = loadImage("betterpart.png")
        image(img2, 35, 400, 800, 750)
        image(img, 35, 0, 800, 750)
def gameLose():
    background(255, 255, 176)
    img3 = loadImage("youlose.png")
    image(img3, 40, 100, 800, 750)

def gameWon():
    background(255, 255, 176)
    img4 = loadImage("youwin.png")
    image(img4, 40, 100, 800, 750)
        
def draw():
    global start
    global x_speed
    global gamend
    global gamewin
    if start == False:
        gameScreen()
    else:
        startScreen()
    if gamend == True:
        gameLose()
    if x_speed == 0:
        gamend = True
    if ball_x == 20 and ball_y > mouseY and ball_y < mouseY + 125:
        gamewin = True
    if gamewin == True:
        gameWon()
    if keyPressed and key == ' ':
        start = False
        print("done")
    # draw start screen
        
        
        
        
        
    
