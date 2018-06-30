import pygame
from methLab import MethLab

methLab = MethLab(0., 1)

pygame.init()

SCREENSIZE = (640, 480)
BGCOLOR = (255, 255, 255)
BLUE = (0, 102, 153)
ORANGE = (234, 167, 65)
BLACK = (0, 0, 0)

FPS = 60

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Meth Game")

font = pygame.font.Font("freesansbold.ttf", 50)
textSurf = font.render("Meth Labs", True, ORANGE, BLUE)
textRect = textSurf.get_rect()
textRect.centerx = screen.get_rect().centerx
textRect.centery = 50

font2 = pygame.font.Font("freesansbold.ttf", 40)
methTextSurf = font2.render("Meth: %5d" % (int(methLab.meth),),
        True, BLACK, BGCOLOR)
methTextRect = methTextSurf.get_rect()
methTextRect.x = 50
methTextRect.y = 200

clock = pygame.time.Clock()

done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    methLab.makeMeth(FPS)
    methTextSurf = font2.render("Meth: %5d" % (int(methLab.meth),),
            True, BLACK, BGCOLOR)

    screen.fill(BGCOLOR)

    screen.blit(textSurf, textRect)
    screen.blit(methTextSurf, methTextRect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
