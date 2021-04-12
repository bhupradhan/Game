import pygame
import math
import random
from pygame import mixer

pygame.init()

#Screen Display
screen = pygame.display.set_mode((800,600))


#Icon and title bar
pygame.display.set_caption("Battle Space")
icon = pygame.image.load('icon.png')
#pygame.transform.scale(icon,(32,32))
pygame.display.set_icon(icon)

#Music
mixer.music.load('background2.wav')
mixer.music.play(-1)

p1Img = pygame.image.load('space-ship1.png')
p1Img=pygame.transform.scale(p1Img,(64,64))
p1X = 5
p1Y = 230
p1Y_change = 0
life1 = 5

p2Img = pygame.image.load('space-ship2.png')
p2Img=pygame.transform.scale(p2Img,(64,64))
p2X = 720
p2Y = 230
p2Y_change = 0
life2 = 5

#Background
background = pygame.image.load('background.png')
background=pygame.transform.scale(background,(800,600))

#bullet
bulletImg = pygame.image.load('fire.png')
bulletImg =pygame.transform.scale(bulletImg,(64,64))

bullet2Img = pygame.image.load('fire3.png')
bullet2Img =pygame.transform.scale(bullet2Img,(64,64))




# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(300)
    enemyY.append(230+(250*i))
    enemyX_change.append(4)
    enemyY_change.append(40)
'''
rock = pygame.image.load("asteroid.png")
rock = pygame.transform.scale(rock, (100, 100))
rockX = 340
rockY = 230
rockY_change = 5

rock2 = pygame.image.load("p3.png")
rock2 = pygame.transform.scale(rock2, (64, 64))
rock2X = 240
rock2Y = 230
rock2Y_change = 5

rock3 = pygame.image.load("p4.png")
rock3 = pygame.transform.scale(rock3, (64, 64))
rock3X = 440
rock3Y = 150
rock3Y_change = 5

rock4 = pygame.image.load("p5.png")
rock4 = pygame.transform.scale(rock4, (64, 64))
rock4X = 280
rock4Y = 400
rock4Y_change = 5

rock5 = pygame.image.load("p2.png")
rock5 = pygame.transform.scale(rock5, (64, 64))
rock5X = 440
rock5Y = 350
rock5Y_change = 5

'''


bulletX = 5
bulletY = 480
bulletX_change = 25
bulletY_change = 0
bullet_state = "ready"

#bullet2
bullet2X = 720
bullet2Y = 480
bullet2X_change = -25
bullet2Y_change = 10
bullet2_state = "ready2"

#score1
score1_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text1X=10
text1Y=10

#score2
score2_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text2X=600
text2Y=570

#game_over_text
over_font = pygame.font.Font('freesansbold.ttf',64)

font2 = pygame.font.Font('freesansbold.ttf',18)

def how_to_play():
    how_text = font2.render("HOW TO PLAY:", True, (255,255,255))
    screen.blit(how_text,(100,175))
    info = font2.render("1)IT IS A TWO PLAYER GAME",True, (255,255,255))
    screen.blit(info,(90,200))
    py1 = font2.render("PLAYER1: UP(to move upwards) DOWN(to move downwards) SPACE(to fire)",True, (255,255,255))
    screen.blit(py1,(100,225))
    py2 = font2.render("PLAYER2: W(to move upwards) S(to move downwards) E(to fire)",True, (255,255,255))
    screen.blit(py2,(100,250))
    hits = font2.render("2)EACH HIT GIVES ONE POINT",True, (255,255,255))
    screen.blit(hits,(90,275))
    diff = font2.render("3)IF THE SCORE DIFFRENCE IS 10 THE PLAY WITH HIGH SCORE WINS",True, (255,255,255))
    screen.blit(diff,(90,300))
    ast = font2.render("HITTING THE ASTEROIDS WONT FETCH ANY POINTS",True, (255,255,255))
    screen.blit(ast,(100,325))
    ent = font2.render("PREESS ENTER TO CONTINUE",True, (255,255,255))
    screen.blit(ent,(250,500))

def p1(x,y):
    screen.blit(p1Img,(x,y))

def p2(x,y):
    screen.blit(p2Img,(x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x,y))

def fire_bullet2(x,y):
    global bullet2_state
    bullet2_state = "fire2"
    screen.blit(bullet2Img,(x,y))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

def game_over_text(p):
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text,(200,250))
    if p==1:
        ply1 = over_font.render("PLAYER ONE WINS", True, (255,255,255))
        screen.blit(ply1,(120,350))
    elif p==2:
        ply2 = over_font.render("PLAYER TWO WINS", True, (255,255,255))
        screen.blit(ply2,(120,350))



def show_score(x,y,score_value):
    score = font.render("SCORE :" + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

howto = True
running = True
while howto:

    #Bkg image
    screen.blit(background,(0,0))
    how_to_play()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            howto = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                howto = False

        pygame.display.update()




while running:

    #rockY += rockY_change


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #KEYPRESSP1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1Y_change = -5
            if event.key == pygame.K_s:
                p1Y_change = +5
            if event.key == pygame.K_e:
                if bullet_state == "ready":
                    bulletY=p1Y
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                p1Y_change = 0

        #KEYPRESSP2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p2Y_change = -5
            if event.key == pygame.K_DOWN:
                p2Y_change = +5
            if event.key == pygame.K_SPACE:
                if bullet2_state == "ready2":
                    bullet2Y=p2Y
                    bullet2_sound = mixer.Sound('laser2.wav')
                    bullet2_sound.play()
                    fire_bullet2(bullet2X,bullet2Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p2Y_change = 0
    '''
    if rockY<0 :
        rockY_change = random.randint(0,5)
        rockY_change = rockY_change * 1


    if rockY>=536 :
        rockY_change = random.randint(0,10)
        rockY_change = rockY_change * -1
    '''


    #P1bound
    if p1Y<0:
        p1Y=0
    if p1Y>536:
        p1Y=536

    #P2bound
    if p2Y<0:
        p2Y=0
    if p2Y>536:
        p2Y=536

    #set bg
    screen.fill((0,0,255))

    #Bkg image
    screen.blit(background,(0,0))

    # Enemy Movement
    for i in range(num_of_enemies):
        enemyY[i] += enemyY_change[i]
        if enemyY[i] <= 0:
            enemyY_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyY[i] >= 536:
            enemyY_change[i] = -4
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)

    #Bullet1Movement
    if bulletX >= 760:
        bullet_state="ready"
        bulletX = 5
    if bullet_state == "fire":
        bulletX += bulletX_change
        fire_bullet(bulletX,bulletY)

    #Bullet2Movement
    if bullet2X <= 10:
        bullet2_state="ready2"
        bullet2X = 720
    if bullet2_state == "fire2":
        bullet2X += bullet2X_change
        fire_bullet2(bullet2X,bullet2Y)

    #collision of bullet1 and player 2
    collision = isCollision(p2X,p2Y,bulletX,bulletY)
    if collision:
        #p2X=900
        #p2Y=900
        score1_value += 1
        bulletX=5
        bullet_state="ready"


    collision2 = isCollision(p1X,p1Y,bullet2X,bullet2Y)
    if collision2:
        #p1X=900
        #p1Y=900
        score2_value += 1
        bullet2X=720
        bullet2_state="ready2"
    '''
    collision3 = isCollision(rockX,rockY,bulletX,bulletY)
    if collision3:

        bulletX = 5
        bullet_state = "ready"



    collision5 = isCollision(rock2X, rock2Y, bulletX, bulletY)
    if collision5:
        bulletX = 5
        bullet_state = "ready"
    collision6 = isCollision(rock2X, rock2Y, bullet2X, bullet2Y)
    if collision6:
        bullet2X = 5
        bullet2_state = "ready"

    collision7 = isCollision(rock3X, rock3Y, bulletX, bulletY)
    if collision7:
        bulletX = 5
        bullet_state = "ready"
    collision8 = isCollision(rock3X, rock3Y, bullet2X, bullet2Y)
    if collision8:
        bullet2X = 5
        bullet2_state = "ready"

    collision9 = isCollision(rock4X, rock4Y, bulletX, bulletY)
    if collision9:
        bulletX = 5
        bullet_state = "ready"
    collision10 = isCollision(rock4X, rock4Y, bullet2X, bullet2Y)
    if collision10:
        bullet2X = 5
        bullet2_state = "ready"

    collision11 = isCollision(rock5X, rock5Y, bulletX, bulletY)
    if collision11:
        bulletX = 5
        bullet_state = "ready"
    collision12 = isCollision(rock5X, rock5Y, bullet2X, bullet2Y)
    if collision12:
        bullet2X = 5
        bullet2_state = "ready"
    '''

    if (score1_value - score2_value) >= 10:
        game_over_text(1)
        '''
        rock2X=1000
        rock2Y=1000
        rock3X=1000
        rock3Y=1000
        rock4X=1000
        rock4Y=1000
        rock5X=1000
        rock5Y=1000
        '''
        p1X=10000
        p1Y=10000
        p2X=10000
        p2Y=10000
    elif(score2_value - score1_value) >= 10:
        game_over_text(2)
        '''
        rock2X=1000
        rock2Y=1000
        rock3X=1000
        rock3Y=1000
        rock4X=1000
        rock4Y=1000
        rock5X=1000
        rock5Y=1000
        '''
        p1X=10000
        p1Y=10000
        p2X=10000
        p2Y=10000


    p1Y += p1Y_change
    p2Y += p2Y_change
    p1(p1X,p1Y)
    p2(p2X,p2Y)
    '''
    screen.blit(rock,(rockX,rockY))
    screen.blit(rock2, (rock2X, rock2Y))
    screen.blit(rock3, (rock3X, rock3Y))
    screen.blit(rock4, (rock4X, rock4Y))
    screen.blit(rock5, (rock5X, rock5Y))
    '''
    show_score(text1X,text1Y,score1_value)
    show_score(text2X,text2Y,score2_value)

    pygame.display.update()
