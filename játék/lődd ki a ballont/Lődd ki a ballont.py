import pygame
import random

def pontok():
    score_surf = game_font.render('Pontszám: ' + str(score), True, FONT_COLOR)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)

def jatszottpontok():
    if score:
        final_score_surf = game_font.render("PONTSZÁM:" + str(score), True, FONT_COLOR)
        final_score_rect = final_score_surf.get_rect(center=(WIDTH / 2, HEIGHT - 220))
        screen.blit(final_score_surf, final_score_rect)

def hatralevoido():
    time_left_surf = game_font.render('A játék végéig:' + str(time_left), True, FONT_COLOR)
    time_left_rect = time_left_surf.get_rect(topleft=(10, 50))
    screen.blit(time_left_surf, time_left_rect)

WIDTH, HEIGHT = 1280, 620
BALLOON_SPEED = 4
FONT_COLOR = (27, 131, 142)
jatekido = 10000

pygame.init()

pygame.display.set_caption("Lődd ki a ballont")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg_surf = pygame.image.load('sky.png').convert_alpha()
bg_surf = pygame.transform.rotozoom(bg_surf, 0, 1.3)
bg_rect = bg_surf.get_rect(bottomleft=(0, HEIGHT))

balloon_surf = pygame.image.load('balloon.png').convert_alpha()
balloons_rect = []
balloons_timer = pygame.USEREVENT + 1
pygame.time.set_timer(balloons_timer, 400)

crosshair_surf = pygame.image.load('crosshair.png').convert_alpha()
crosshair_surf = pygame.transform.rotozoom(crosshair_surf, 0, 0.5)
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

game_font = pygame.font.SysFont('arial', 30, bold=True)
#nyitó és záró képernyő feliratai
title_surf = game_font.render("LŐDD KI A BALLONT", True, FONT_COLOR)
title_rect = title_surf.get_rect(center=(WIDTH / 2, 200))
run_surf = game_font.render("Nyomd meg a SPACE billentyűt", True, FONT_COLOR)
run_rect = run_surf.get_rect(center=(WIDTH / 2, HEIGHT - 150))

start_time = pygame.time.get_ticks()
score = 0
game_active = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        #lufik létrehozása megadott időközönként
        if event.type == balloons_timer:
            balloons_rect.append(balloon_surf.get_rect(center=(random.randint(50, WIDTH-50), HEIGHT-50)))

    screen.blit(bg_surf, bg_rect)

    if game_active:
        for index, balloon_rect in enumerate(balloons_rect):
            #lufik emelkedése
            balloons_rect[index].top -= BALLOON_SPEED
            #lufik oldalirányu mozgása
            mov_y = random.randint(0, 3)
            if mov_y == 0:
                balloons_rect[index].left -= 2
            else:
                balloons_rect[index].left += 2
            # lufik törlése a memóriábol (képernyő elhagyásakor)
            if balloons_rect[index].bottom <= -10:
                del balloons_rect[index]
            #találat vizsgálata
            if balloon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(num_buttons=3)[0]:
                del balloons_rect[index]
                score += 1

            screen.blit(balloon_surf, balloon_rect)
        screen.blit(crosshair_surf, crosshair_rect)

        #pontszám megjelenítése
        pontok()

        #a hátralévő játékidő számítása és megjelenítése
        time_left = int((start_time + jatekido - pygame.time.get_ticks()) / 1000)
        if time_left < 0:
            game_active = False
        hatralevoido()

    #nyitó és záró képernyő
    else:
        screen.blit(title_surf, title_rect)
        screen.blit(balloon_surf, balloon_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
        screen.blit(crosshair_surf, crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
        screen.blit(run_surf, run_rect)

        #pontszám, ha az értéke > mint 0
        jatszottpontok()


        #játék indítása

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            score = 0
            balloons_rect = []
            start_time = pygame.time.get_ticks()
            game_active = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
