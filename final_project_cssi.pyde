import testinggg 
feed = 5
startHungerX= 600
fun = 5
startFunX= 50
freshness = 5
startFreshnessX= 600
fatigue = 5
startFatigueX= 600

def setup():
    global startHungerX
    global startFunX
    size(900,800)
    background(250, 240, 247)
    fill(56, 30, 30)
    rect(0,400, 1000, 600 )
    fill(255,255,255)
    rect(0,650, 1000, 600 )
    pet = loadImage("redpanda.png")
    fridge = loadImage("refridgerator.png")
    tub = loadImage("bath tub.png")
    window = loadImage("window2.png")
    ball = loadImage("ball.png")
    bed = loadImage("bed.png")
    image(window, 550,50, 350, 350)
    image(pet, 250,350, 350, 350)
    image(fridge, -30, 150, 350, 300)
    image(tub, 500, 170, 400, 370)
    image(ball, 90, 450, 180, 180)
    image(bed, 500, 370, 350, 370)
    fill(0,0,0)
    textSize(20)
    text("Hunger", 600, 680)
    rect(600,690,200,30)
    textSize(20)
    text("Fun", 50, 680)
    rect(50,690,200,30)
    i = 0
    while i < 5: 
        fill(255,0,0)
        rect(startHungerX, 690,20,30)
        startHungerX += 20
        i += 1
    i = 0
    while i < 5: 
        fill(255,0,0)
        rect(startFunX, 690,20,30)
        startFunX += 20
        i += 1
    
def draw():
    global feed
    global startHungerX
    global fun
    global startFunX
    if feed < 10 and mousePressed: 
        if mouseX > 45 and mouseX < 180 and mouseY > 150 and mouseY < 400:
            print(mouseX)
            frameRate(1)
            fill(255,0,0)
            rect(startHungerX, 690,20,30)
            startHungerX += 20
            feed += 1
            #print(feed)
    if feed >= 0: 
        if frameCount % 10 == 0: 
            fill(0,0,0)
            rect(startHungerX, 690,20,30)
            startHungerX -= 20
            feed -= 1
            #print(feed)
    if fun < 10 and mousePressed: 
        if mouseX > 150 and mouseX < 280 and mouseY > 480 and mouseY < 580:
            print(mouseY)
            frameRate(1)
            fill(255,0,0)
            rect(startFunX, 690,20,30)
            startFunX += 20
            fun += 1
            #print(fun)
    if fun >= 0: 
        if frameCount % 10 == 0: 
            fill(0,0,0)
            rect(startFunX, 690,20,30)
            startFunX -= 20
            fun -= 1
            #print(fun)
