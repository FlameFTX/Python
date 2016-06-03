import pygame, random

white =(255,255,255)

x_c=[]
y_c=[]
x_s=[]
y_s=[]
x_coord=250
y_coord=250
x_speed=0
y_speed=0
#even number(number of asteroids)
number=6

ufo=pygame.image.load('fruit2.png')
ufo=pygame.transform.scale(ufo,(82,82))
asteroid=pygame.image.load('fruit3.png')
asteroid=pygame.transform.scale(asteroid,(50,50))
angle=0
pygame.init()

size=[700,700]
screen=pygame.display.set_mode(size)

pygame.display.set_caption('My Game')

done=False

clock=pygame.time.Clock()

pygame.mouse.set_visible(1)

sp=5
ufosp=10
ufangle=0
ufanglechange=0

for x in range(number):
    x_c.append(random.choice(range(618)))
    y_c.append(random.choice(range(618)))
for x in range(number/2):
    x_s.append(sp)
    x_s.append(-1*sp)
    y_s.append(sp)
    y_s.append(-1*sp)
random.shuffle(x_s)
random.shuffle(y_s)

while done==False:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True

    #ufo processing
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				ufangle=ufangle+3
			if event.key==pygame.K_RIGHT:
				ufangle=ufangle-3
			if event.key==pygame.K_UP:
				y_speed=-1*ufosp
			if event.key==pygame.K_DOWN:
				y_speed=ufosp

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				x_speed=0
				ufangle=0
			if event.key==pygame.K_RIGHT:
				x_speed=0
				ufangle=0
			if event.key==pygame.K_UP:
				y_speed=0
			if event.key==pygame.K_DOWN:
				y_speed=0

	x_coord=x_coord+x_speed
	y_coord=y_coord+y_speed
	if x_coord<0:
		x_coord=0
	if x_coord>618:
		x_coord=618
	if y_coord<0:
		y_coord=0
	if y_coord>618:
		y_coord=618

    #asteroid processing
	asteroids=[]
	for ind in range(number):
		x_c[ind]=x_c[ind]+x_s[ind]
		y_c[ind]=y_c[ind]+y_s[ind]
		if x_c[ind]<0:
			x_c[ind]=0
			x_s[ind]=-1*x_s[ind]
		if x_c[ind]>618:
			x_c[ind]=618
			x_s[ind]=-1*x_s[ind]
		if y_c[ind]<0:
			y_c[ind]=0
			y_s[ind]=-1*y_s[ind]
		if y_c[ind]>618:
			y_c[ind]=618
			y_s[ind]=-1*y_s[ind]

	angle=angle+3.0
	ufanglechange=ufanglechange+ufangle

	ufrotufo=pygame.transform.rotate(ufo, ufanglechange)
	ufrotrec=ufrotufo.get_rect()
	ufrotrec.center = (x_coord,y_coord)

	rotasteroid=pygame.transform.rotate(asteroid,angle)
	rotrec=rotasteroid.get_rect()
	for ind in range(number):
		rotrec.center=(x_c[ind],y_c[ind])
		asteroids.append(rotrec.center)

	screen.fill(white)

	for ind in range(number):
		screen.blit(rotasteroid,asteroids[ind])
	screen.blit(ufrotufo,ufrotrec)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
