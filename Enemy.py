import pygame

class Enemy(object):
    walkRight = [pygame.image.load('sprite/R1E.png'), pygame.image.load('sprite/R2E.png'), pygame.image.load('sprite/R3E.png'), pygame.image.load('sprite/R4E.png'), pygame.image.load('sprite/R5E.png'), pygame.image.load('sprite/R6E.png'), pygame.image.load('sprite/R7E.png'), pygame.image.load('sprite/R8E.png'), pygame.image.load('sprite/R9E.png'), pygame.image.load('sprite/R10E.png'), pygame.image.load('sprite/R11E.png')]
    walkLeft = [pygame.image.load('sprite/L1E.png'), pygame.image.load('sprite/L2E.png'), pygame.image.load('sprite/L3E.png'), pygame.image.load('sprite/L4E.png'), pygame.image.load('sprite/L5E.png'), pygame.image.load('sprite/L6E.png'), pygame.image.load('sprite/L7E.png'), pygame.image.load('sprite/L8E.png'), pygame.image.load('sprite/L9E.png'), pygame.image.load('sprite/L10E.png'), pygame.image.load('sprite/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0