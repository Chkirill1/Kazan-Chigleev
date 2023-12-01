import pygame

try:
    stroka = input().split()
    stroka = list(map(lambda x: int(x), stroka))
    a, n = stroka[0], stroka[1]
except:
    print("Неправильный формат!")


def draw(screen):
    screen.fill((255, 255, 255))
    storona = a // n
    x = 0
    yy = 0
    for i in range(n):
        if i % 2 == 0:
            x = 0
        else:
            x = storona
        for y in range(n):
            pygame.draw.rect(screen, pygame.Color("black"), (x, yy, a // n, a // n))
            x += storona * 2
        yy += storona


if __name__ == '__main__':
    pygame.init()
    size = width, height = a, a
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
