import pygame
from sys import exit

def bye():
    pygame.quit()
    exit()

pygame.init()
pygame.display.init()
pygame.font.init()
l = [pygame.font.get_fonts()[20],32]
c = ["blue"]
s = [500,500,c[0]]
k = [pygame.K_ESCAPE]
m = ["W HAS BEEN PRESSED!",
     "A HAS BEEN PRESSED!",
     "S HAS BEEN PRESSED!",
     "D HAS BEEN PRESSED!",
     ]
screen = pygame.display.set_mode([500,500])

font1 = pygame.sysfont.SysFont(l[0], l[1], False, False)
clock = pygame.time.Clock()

def main(running):
    lastMessage = ""
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bye()
            if event.type == pygame.KEYUP and keys[pygame.K_w]:
                print(m[0])
                lastMessage += "w"
            if event.type == pygame.KEYUP and keys[pygame.K_a]:
                print(m[1])
                lastMessage += "a"
            if event.type == pygame.KEYUP and keys[pygame.K_s]:
                print(m[2])
                lastMessage += "s"
            if event.type == pygame.KEYUP and keys[pygame.K_d]:
                print(m[3])
                lastMessage += "d"
            if event.type == pygame.KEYUP and keys[pygame.K_RETURN]:
                print(lastMessage)
            
        screen.fill(s[2])
        pygame.display.update()
        clock.tick(60)

main(True)
