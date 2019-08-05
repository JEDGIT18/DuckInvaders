PX = 400
enemAlive = [[True,True,True,True,True,True], #checks if enemy on grid is alive 
          [True,True,True,True,True,True],
          [True,True,True,True,True,True],
          ]
bulletShot = False
bulletSpd = 560;
bulletInGame = True
BX = 0 
collision = False
lives = 3

def setup():
    global ship,enemy,Y,speedY,testL1,testL2,test
    size(900,700)
    speedY = 10 
    test = True
    testL1 = 0 
    testL2 = 0 
    ship  = loadImage("ship.png")
    enemy =loadImage("Enemy2.png")
    
   

def draw():
    global PX, bulletShot,bulletSpd,bulletInGame, collision,Y,speedY,testL1,testL2,test,lives
    background(0)
    ct = 1
    if lives >= 3:
        image(ship,25,650,75,50)
    if lives >=2:
        image(ship,110,650,75,50)
    strokeWeight(3)
    stroke(83, 249, 32)
    line(0,630,900,630)
    stroke(255)
    if lives >= 1:
        image(ship,PX,570,75,50)
        makeEnemies(50)
        MovCheck() #calls movement check 
        bulletCheck() #checks if a player has shot a bullet 
        if bulletShot == True: #checks if a bullet is in play 
            playerBullet()
            bulletInGame = False
            if bulletSpd < 0 or collision: #checks if the bullet has to be put out of play 
                bulletShot = False
                bulletSpd = 560
                bulletInGame = True
                collision = False
        enemyCollisionCheck()
        enemyBullet()
        playerCollsionCheck()
        if ct == 1:
            Y= speedY +testL2
            speedY+=20
            rect(testL1,Y,5,10)
            if Y>700:
                test=True
                testL1 = -100 
                testL2 = 0
                Y=1
            
                speedY=0
    else:
        textSize(50)
        text("Game Over",300,400)
        reRun = input("Continue: y/n")
        if reRun == "y".lower():
            lives = 3
        elif reRun == "n".lower():
            noLoop()

        
def enemyBullet():
    global testL1
    global testL2
    global x1
    global y1
    global test
    randX=int(random(0,6))
    randY=int(random(0,3))
    if test==True:
        if enemAlive[randY][randX] == True:
            x1 = 75*randX+250
            y1 = 75*randY+50
            noStroke()
            rect(x1+22.5,y1+25,5,10)
            testL1 = (x1+22.5)
            testL2 = (y1+25)
            test=False
        else:
            test = False
            
        
def makeEnemies(enemSize): #draws grid of enemies in center of screen 
    x = 250
    y = 50
    for r in range(len(enemAlive) ): #loops rows
        for c in range(len(enemAlive[r])):#rows collums 
            if enemAlive[r][c] == True:
                image(enemy,x,y,enemSize,enemSize)
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
    rect(BX  + 35, bulletSpd,5,10)
    bulletSpd -= 10
    
    
def enemyCollisionCheck(): #checks collision 
    global BX, bulletSpd,bulletInGame, collision
    x = 250 
    y = 50 
    delay(20)
    for r in range(len(enemAlive)): #loops through rows
        for c in range(len(enemAlive[r])):#loops collums
            if BX >= (x - 25)and BX <= (x +20) and bulletSpd > (y - 25) and bulletSpd < (y + 25):
                if enemAlive[r][c] == True:
                    print("collision")
                    background(0)
                    enemAlive[r][c] = False
                    bulletShot = False
                    bulletSpd = 560
                    bulletInGame = True
                    collision = True 
                    print("hit!")
                   
                    
           
            x+= 75
        
        y += 75
        x = 250

        
def playerCollsionCheck():
    global x1,y1,lives,testL1,Y,test,speedY,testL2
    print(testL1,Y,PX)
    print(lives)
    if testL1 > PX and testL1 < (PX +95) and Y > 570 and Y < (570 + 50):
        lives -= 1
        print("life lost")
        test=True
        testL1 = -100 
        testL2 = 0
        Y=1
        speedY=0
    
             
            
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
            
            
            
            
            
            
            
            
