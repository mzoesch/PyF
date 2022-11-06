import pygame
import sys
import pygame.locals as pl


def main(*args, **kwargs) -> None:

    w, h = kwargs['width'], kwargs['height']

    pygame.init()
    pygame.display.set_caption('PyF')
    screen = pygame.display.set_mode(
        (w, h), 0, 32
    )
    screen.fill((0, 0, 0))  # Black

    fs: list[str] = pygame.font.get_fonts()
    mC = pygame.time.Clock()

    DELTAY, DELTAX = 30, 370
    x, y = 10, DELTAY

    i = 1
    for j in fs:

        if y > h - 50:  # New column
            y = DELTAY
            x += DELTAX

        f = pygame.font.SysFont(j, 20)

        try:
            l = f.render(f'{i}. Hello world!', True, (255, 255, 255))
            screen.blit(l, (x, y))
            y += DELTAY
            i += 1
            continue

        except Exception as e:
            print(f'{e} at {i=} => {j=}')

    while True:

        for event in pygame.event.get():
            if event.type == pl.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mC.tick(60)


if __name__ == '__main__':
    main(
        width=3600.,
        height=1000
    )
