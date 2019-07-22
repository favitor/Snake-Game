import pygame
from random import randrange

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (46,139, 87)
blue = (0, 0, 255)

try:
    pygame.init()
except:
    print("Não foi possivel inicar com sucesso")
#variables
width = 320
height = 280
size = 10
score = 40

hour = pygame.time.Clock()
background = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')


def text(msg, color, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    text_1 = font.render(msg, True, color)
    background.blit(text_1, [x, y])
def snake(SnakeXY):
    for XY in SnakeXY:
        pygame.draw.rect(background, green, [XY[0], XY[1], size, size])

def food(pos_x, pos_y):
    pygame.draw.rect(background, red, [pos_x, pos_y, size, size])

def game():
    exit = True
    gameover = False
    pos_x = randrange(0, width-size, 10)
    pos_y = randrange(0, height-size-score, 10)
    food_x = randrange(0, width-size, 10)
    food_y = randrange(0, height-size-score, 10)
    velocity_x = 0
    velocity_y = 0
    SnakeXY = []
    SnakeLen = 1
    points = 0
    while exit:
        while gameover:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        exit = True
                        gameover = False
                        pos_x = randrange(0, width-size, 10)
                        pos_y = randrange(0, height-size-score, 10)
                        food_x = randrange(0, width-size, 10)
                        food_y = randrange(0, height-size-score, 10)
                        velocity_x = 0
                        velocity_y = 0
                        SnakeXY = []
                        SnakeLen = 1
                        points = 0
                        gameover = False
                    if event.key == pygame.K_e:
                        exit = False
                        gameover = False
                if event.type == pygame.MOUSEBUTTOMDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    print(pygame.mouse.get_pos())
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        exit = True
                        gameover = False
                        pos_x = randrange(0, width-size, 10)
                        pos_y = randrange(0, height-size-score, 10)
                        food_x = randrange(0, width-size, 10)
                        food_y = randrange(0, height-size-score, 10)
                        velocity_x = 0
                        velocity_y = 0
                        SnakeXY = []
                        SnakeLen = 1
                        points = 0
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        exit = False
                        gameover = False
            background.fill(white)
            text("Game Over", red, 50, 65, 30)
            text("Final Score: "+str(points), black, 30, 70, 80)
            pygame.draw.rect(background, black, [45, 120, 135, 27])
            text("Continue(C)", white, 30, 50, 125)
            pygame.draw.rect(background, black, [190, 120, 75, 27])
            text("Exit(E)", white, 30, 195, 125)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocity_x != size:
                    velocity_y = 0
                    velocity_x =- size
                if event.key == pygame.K_RIGHT and velocity_x != -size:
                    velocity_y = 0
                    velocity_x = size
                if event.key == pygame.K_UP and velocity_y != size:
                    velocity_x = 0
                    velocity_y =- size
                if event.key == pygame.K_DOWN and velocity_y != -size:
                    velocity_x = 0
                    velocity_y = size

        if exit:                    
            background.fill(black)        
            pos_x += velocity_x
            pos_y += velocity_y

            if pos_x == food_x and pos_y == food_y:
                food_x = randrange(0, width-size, 10)
                food_y = randrange(0, height-size-score, 10)
                SnakeLen += 1
                points += 1

            if pos_x + size > width - score:
                gameover = True
            if pos_x < 0:
                gameover = True
            if pos_y + size > height - score:
                gameover = True
            if pos_y < 0:
                gameover = True

            
            SnakeHead = []
            SnakeHead.append(pos_x)
            SnakeHead.append(pos_y)
            SnakeXY.append(SnakeHead)
            if len(SnakeXY) > SnakeLen:
                del SnakeXY[0]
            if any(Block == SnakeHead for Block in SnakeXY[:-1]):
                gameover = True

            pygame.draw.rect(background, blue, [0, height-score, width, score])
            text("Score: "+str(points), white, 20, 10, height-30)
            snake(SnakeXY)
            food(food_x, food_y)
            pygame.display.update()
            hour.tick(15)
    
game()

pygame.quit()