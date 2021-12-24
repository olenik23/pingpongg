from pygame import *

fon = (200,255,255)
ww = 600
wh = 500
win = display.set_mode((ww,wh))
win.fill(fon)

clock = time.Clock()
fps = 60 
game = True 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(fps)