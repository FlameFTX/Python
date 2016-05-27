import pygame

#define some colors
black =(0,0,0)
white =(255,255,255)
green=(0,255,0)
red=(255,0,0)
angle=0
anglechange=0

ufo=pygame.image.load('1.png')
ufo=pygame.transform.scale(ufo,(82,82))
#setup
pygame.init()

#set the width and height of the screen[width,height]
size=[700,700]
screen=pygame.display.set_mode(size)

pygame.display.set_caption('My Game')

#loop until the user clicks the close button
done=False

#used to manage how fast the screen updates
clock=pygame.time.Clock()

#hide the mouse cursor
pygame.mouse.set_visible(0)

#speed in pixels per frame
x_speed=0
y_speed=0

#current position
x_coord=10
y_coord=10

sp=10

#main program loop
while done==False:
	#All event processing should go below this comment
	for event in pygame.event.get(): #user did something
		if event.type==pygame.QUIT: #if user clicked close
			done=True #flag that we are done so we exit this loop
            #user pressed down on a key

		if event.type==pygame.KEYDOWN:
            #figure out if it was an arrow key. If so
            #adjust speed
			if event.key==pygame.K_LEFT:
				angle=angle-3
			if event.key==pygame.K_RIGHT:
				angle=angle+3
			if event.key==pygame.K_UP:
				y_speed=-1*sp
			if event.key==pygame.K_DOWN:
				y_speed=sp

        #user let up on a key
		if event.type==pygame.KEYUP:
            	#if it is an arriw key, reset vector back to zero
			if event.key==pygame.K_LEFT:
				angle = 0
			if event.key==pygame.K_RIGHT:
				angle = 0
			if event.key==pygame.K_UP:
				y_speed=0
			if event.key==pygame.K_DOWN:
				y_speed=0

    #All event processing should go above this comment

    #all game logic should go below this comment

    #move the object according to the speed vector
	anglechange=anglechange+angle
	x_coord=x_coord+x_speed
	y_coord=y_coord+y_speed
	if x_coord<0:
		x_coord=screen.get_width()
	if x_coord>screen.get_width():
		x_coord=0
	if y_coord<0:
		y_coord=screen.get_height()
	if y_coord>screen.get_height():
		y_coord=0

	rotufo=pygame.transform.rotate(ufo, anglechange)

	rotrec=rotufo.get_rect()
	rotrec.center = (x_coord,y_coord)
    #all game logic should go above this comment

    #all code to draw should go below this comment

	screen.fill(white)

	screen.blit(rotufo,rotrec)

    #all code to draw should go above this comment

	pygame.display.flip()

    #limit to 20 frames per second
	clock.tick(60)

#close the window and quit
#on exit if running from IDLE
pygame.quit()
