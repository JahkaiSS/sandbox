import pygame
from sys import exit

pygame.init()
pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode([500,500])

f = [pygame.font.get_fonts()[22],
     10]
font = pygame.sysfont.SysFont(f[0],f[1],False, False)

def bye():
    pygame.quit()
    exit()
def update(obj):
    pygame.display.update()
    obj.tick(60)

clock = pygame.time.Clock()

def main(go,color):
    key_list = []
    while go:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bye()
            if event.type == pygame.KEYUP:
                if keys:
                    for x, k in enumerate(range(len(keys))):
                        if keys[k] == True:
                            key_list.append([keys[k], x])
                        if keys[pygame.K_SPACE]:
                            key_list.clear()
            

        
        
        if keys[pygame.K_ESCAPE]:
            bye()
        
            
        

        
        font_surface = font.render(f"{key_list}",False,"white")

        screen.fill(color)
        screen.blit(font_surface,[0,0])
        
        update(clock)

main(True,"blue")

