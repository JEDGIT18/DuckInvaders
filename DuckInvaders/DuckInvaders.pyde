PX = 400
enemAlive = [[True,True,True,True,True,True], #checks if enemy on grid is alive 
          [True,True,True,True,True,True],
          [True,True,True,True,True,True],
          [True,True,True,True,True,True],
          [True,True,True,True,True,True],
          [True,True,True,True,True,True]
          ]
bulletShot = False
bulletSpd = 560;
bulletInGame = True
BX = 0 
def setup():
    global img
    size(900,700)
    img = loadImage("ship.png")
    strokeWeight(3)
    stroke(83, 249, 32)
   

def draw():
    global img, PX, bulletShot,bulletSpd,bulletInGame
    background(0)
    image(img,25,650,75,50)
    image(img,110,650,75,50)
    line(0,630,900,630)
    makeEnemies(50)
    image(img,PX,570,75,50)
    MovCheck() #calls movement check 
    bulletCheck() #checks if a player has shot a bullet 
    if bulletShot == True: #checks if a bullet is in play 
        playerBullet()
        bulletInGame = False
        if bulletSpd < 0: #checks if the bullet has to be put out of play 
            bulletShot = False
            bulletSpd = 560
            bulletInGame = True
        

def makeEnemies(size): #draws grid of enemies in center of screen 
    x = 250
    y = 50
    for i in range(0,3):
        for j in range(0,6):
            img=loadImage("Enemy2.png")
            image(img,x,y,size,size)
            x+= 75
        y += 75
        x = 250

def MovCheck(): # checks movement of player via key presses
    global PX
    if keyPressed == True:
        if key == 'd':
            if PX >= 800:
                PX += 0
            else:
                PX += 5
        elif key == 'a':
            if PX <= 0:
                PX += 0
            else: 
                PX -= 5

def bulletCheck(): # checks if the user will be allowed to shoot again based on if a bullet is already in play 
    global bulletShot
    if keyPressed == True:
        if key == 'w' and not bulletShot :
            bulletShot = True 

def getBullet(): #grabs the players coordinates for when the bullet is initially shot 
    global bulletInGame,PX,BX
    if bulletInGame:
        BX = PX
  

def playerBullet(): # draws player buller and makes it go up the screen 
    global PX, bulletSpd,BX, bulletInGame
    getBullet()
    rect(BX  + 35, bulletSpd,3,5)
    bulletSpd -= 10
