import pygame
from Player import Player
from Projectile import Projectile
from Enemy import Enemy


pygame.init()

bg = pygame.image.load('sprite/bg.jpg')

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("jeudeouf")

clock = pygame.time.Clock()


def redrawgamewindow():
    win.blit(bg, (0, 0))
    player.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


player = Player(200, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 300)
bullets = []
running = True
while running:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if player.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.vel - player.width:
        player.x += player.vel
        player.left = False
        player.right = True
        player.standing = False
    else:
        player.standing = True
        player.walkcount = 0

    if not (player.isJump):
        if keys[pygame.K_UP]:
            player.isJump = True
            player.right = False
            player.left = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.jumpCount = 10
            player.isJump = False

    redrawgamewindow()

pygame.quit()
