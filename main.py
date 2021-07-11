import pygame
import random as randomnumber

game = pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (251, 197, 49)

dis_width = 600
dis_height = 400

screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('PingPong by Vazzi')

pygame.joystick.init()

clock = pygame.time.Clock()

play_speed = 1
next_step = 9

ball_move = "right"
ball_pos = [300, 200]

firstpos = [160, 240]
secondpos = [160, 240]

first_points = 0
second_points = 0

score_font = pygame.font.SysFont("comicsansms", 35, True)

clock.tick(play_speed)

def playersmove():
    screen.fill(black)
    pygame.draw.line(screen, white, (20, firstpos[0]), (20, firstpos[1]), 10)
    pygame.draw.line(screen, white, (580, secondpos[0]), (580, secondpos[1]), 10)
    s = pygame.Surface((20, 20))
    x = ball_pos[0]
    y = ball_pos[1]
    s.fill(green)
    r, r.x, r.y = s.get_rect(), x, y
    screen.blit(s, r)

    value = score_font.render(str(first_points) + " - " + str(second_points), True, yellow)
    screen.blit(value, [250, 10])

    pygame.display.update()


def changeball():
    global ball_pos
    global ball_move
    global next_step
    global first_points
    global second_points
    if next_step == 0:
        next_step = 9
        if ball_move == "right":
            if 555 > ball_pos[0] > 20:
                ball_pos[0] += 1
                playersmove()
        elif ball_move == "left":
            if 555 > ball_pos[0] > 25:
                ball_pos[0] -= 1
                playersmove()
        if ball_pos[0] + 10 > 555:
            if secondpos[0] < ball_pos[1] < secondpos[1]:
                ball_move = "left"
                y = randomnumber.randint(50, 350)
                ball_pos[1] = y
            else:
                ball_move = "left"
                ball_pos = [300, 200]
                first_points += 1
        if ball_pos[0] - 10 < 25:
            if firstpos[0] < ball_pos[1] < firstpos[1]:
                ball_move = "right"
                y = randomnumber.randint(50, 350)
                ball_pos[1] = y
            else:
                ball_move = "right"
                ball_pos = [300, 200]
                second_points += 1

    else:
        next_step -= 1


def gameLoop():
    global ball_move
    started = False

    while True:

        playersmove()
        changeball()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord("w"):
                    if not started:
                        started = True
                    if firstpos[0] > 30:
                        firstpos[0] -= 30
                        firstpos[1] -= 30
                        playersmove()
                elif event.key == ord("s"):
                    if not started:
                        started = True
                    if firstpos[0] < (dis_height - 90):
                        firstpos[0] += 30
                        firstpos[1] += 30
                        playersmove()
                if event.key == pygame.K_UP:
                    if not started:
                        started = True
                    if secondpos[0] > 30:
                        secondpos[0] -= 30
                        secondpos[1] -= 30
                        playersmove()
                elif event.key == pygame.K_DOWN:
                    if not started:
                        started = True
                    if secondpos[0] < (dis_height - 90):
                        secondpos[0] += 30
                        secondpos[1] += 30
                        playersmove()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()


gameLoop()
