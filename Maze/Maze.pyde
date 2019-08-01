x = 100
y = 700
speed_x = 10
speed_y = 10


def setup():
    global maze
    global win
    global didit
    global x
    global y
    size(900, 800)
    background(245, 255, 210)
    didit = False

    def maze():
        global speed_x
        global speed_y
        global x
        global y
        global maze
        background(245, 255, 210)
        noStroke()
        rect(0, 0, 100, 799)
        rect(100, 400, 700, 100)
        rect(200, 590, 700, 300)
        rect(200, 310, 700, -100)
        rect(100, 0, 700, 100)
        imgr = loadImage("redpanda.png")
        image(imgr, x, y, 200, 200)
        if keyPressed and key == 'a' or key == 'A':
            if x < 30: 
                x = x + 20
            x = x - speed_x
        if keyPressed and key == 'd' or key == 'D':
            if y > 475 and x > 100 and x < 150:
                x = x - 20
            if y > 460 and y < 360 and x > 700:
                x = x - 20
            if x > 750:
                x = x - 20
            x = x + speed_x 
        if keyPressed and key == 's' or key == 'S':
            if y > 660:
                y = y - 20
            if y > 300 and y < 440 and x < 740:
                y = y - 20
            if x > 100 and y > 460:
                y = y - 20
            y = y + speed_y 
        if keyPressed and key == 'w' or key == 'W':
            if y < 440  and y > 360 and x < 740:
                y = y + 20
            if y < 100 and y > 0 and x < 700:
                y = y + 20
            y = y - speed_y 
        if y < 100:
            print("done")
            
def gameWin():
    background(0,0,0)
    textSize(56)
    text("You Win!", 300, 400)
    text ("Press t to go back!", 300, 500)
def draw():
    global maze
    global didit
    global win
    global x
    global y
    if y < 10:
        didit = True 
    if didit == True:
        gameWin()
    if didit == False:
        maze()
    # if keyPressed and key == 't':
    
