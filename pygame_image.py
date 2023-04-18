import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs = [bg_img,pg.transform.flip(pg.image.load("ex01/fig/pg_bg.jpg"),True,False)]
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(pg.image.load("ex01/fig/3.png"),True,False)
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img,10, 1.0)]

    tmr = 0
    x = 0
    y = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1

        if x>= 3199:
            x=0
        x += 1
        screen.blit(bg_imgs[0], [-x, 0])
        screen.blit(bg_imgs[1], [1600-x, 0])
        screen.blit(bg_imgs[0],[3200-x,0])
        if y>=100:
            y=0
        y += 1
        if y>=50:
            screen.blit(kk_imgs[0],[300,200])
        if y<=51:
            screen.blit(kk_imgs[1],[300,200])

        
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()