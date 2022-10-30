import pygame

walkRight = [pygame.image.load('sprite/R1.png'), pygame.image.load('sprite/R2.png'), pygame.image.load('sprite/R3.png'), pygame.image.load('sprite/R4.png'), pygame.image.load('sprite/R5.png'), pygame.image.load('sprite/R6.png'), pygame.image.load('sprite/R7.png'), pygame.image.load('sprite/R8.png'), pygame.image.load('sprite/R9.png')]
walkLeft = [pygame.image.load('sprite/L1.png'), pygame.image.load('sprite/L2.png'), pygame.image.load('sprite/L3.png'), pygame.image.load('sprite/L4.png'), pygame.image.load('sprite/L5.png'), pygame.image.load('sprite/L6.png'), pygame.image.load('sprite/L7.png'), pygame.image.load('sprite/L8.png'), pygame.image.load('sprite/L9.png')]
char = pygame.image.load('sprite/standing.png')

class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
