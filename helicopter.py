import pygame as pg

pg.init()
screen = pg.display.set_mode((640,480))
pg.display.set_caption("Heli")
done = False
clock = pg.time.Clock()

#Load images here
heli_left = pg.image.load("copter_left.png")
heli_left = pg.transform.scale(heli_left, (64,64))
heli_right = pg.image.load("copter_right.png")
heli_right = pg.transform.scale(heli_right, (64,64))

#Initialize some variables
x = 25
y = 25
dx = 0
dy = 0
up_key = False
looking = "right"

while not done:
    # Game Update
    if up_key:
        dy = dy - 1
    else:
        dy = dy + 1
    dy = dy+1
    if dy > 7:
        dy = 7
    if dy < -7:
        dy = -7
    last_x = x
    last_y = y
    
    x = x + dx
    heli_rect = pg.Rect(x,y,64,64)
    platform_rect = pg.Rect((100,300,200,30))
    if heli_rect.colliderect(platform_rect):
        x = last_x
        dx = 0

    y = y + dy
    heli_rect = pg.Rect(x,y,64,64)
    platform_rect = pg.Rect((100,300,200,30))
    if heli_rect.colliderect(platform_rect):
        y = last_y
        dy = 0

    if y > 480-64:
        y = 480-64
        dy = 0
    if x > 640:
        x = -64
    
    #Keyboard and Mouse Controls
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                dx = 5
                looking = "right"
            if event.key == pg.K_LEFT:
                dx = -5
                looking = "left"
            if event.key == pg.K_UP:
                up_key = True
            if event.key == pg.K_DOWN:
                dy = 2
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                dx = 0
            if event.key == pg.K_RIGHT:
                dx = 0
            if event.key == pg.K_UP:
                up_key = False
            if event.key == pg.K_DOWN:
                dy = 0

    screen.fill((255,255,255))
    #Drawing Here
    pg.draw.rect(screen,(0,0,0),[0,0,639,479],2)
    pg.draw.rect(screen,(0,150,0),(100,300,200,30))
    if looking == "right":
        screen.blit(heli_right, (x,y))
    else:
        screen.blit(heli_left, (x,y))
    #Display what was drawn before
    pg.display.flip()
    clock.tick(30)

pg.quit()

        

    