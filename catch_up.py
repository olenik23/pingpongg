from pygame import *
x1 = 40 
y1 = 260

x2 =300
y2 =300

clock = time.Clock()

Fps = 60
events = event.get()

sprite1 = transform.scale(image.load('sprite1.png'),(100,100))
sprite2 = transform.scale(image.load('sprite2.png'),(100,100))

window = display.set_mode((700,500))
display.set_caption("Догонялки") 
background = transform.scale(image.load("background.png"),(700,500))

clock.tick(Fps)

keys_pressed = key.get_pressed()
game = True
while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
        if keys_pressed[K_UP]:
                y1 -= 10
    display.update()

