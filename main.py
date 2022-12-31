# The Logic Of Snake Game:
# 1- we are creating a grid on the screen (simulation)
# 2- some blocks of the grade are snake blocks
# we move objects not by pix but by cell size
# inorder to draw the snake we do the same thing we did for the fruit but we use multiple blocks not just one
# inorder to move the snake, the head is moved to a new block then the block before the head is moved to the old head position and so on
# create a direction where the head is going to be moved and then creating a new positions list
# 1) getting user inputs 2) creating a timer

import pygame, sys, random
from pygame.math import Vector2

pygame.init()

 
score_font = pygame.font.Font("Honey Silk.ttf", 15) # importing score font
class Score:
    def __init__(self):
        self.value = 0
    def increase_score(self):
        self.value += 10
    def display_score(self):
        score_text = "Your score is: " + str(self.value) + "pnts"
        score_surface = score_font.render(score_text, True, pygame.Color("yellow"))
        score_rect = score_surface.get_rect(center = (100, 20))
        screen.blit(score_surface, score_rect)
class Snake:
    def __init__(self):
        self.body = [Vector2(10, 20), Vector2(9, 20), Vector2(8, 20)]
        self.direction = Vector2(1, 0)
    def draw_snake(self):
        for part in self.body:
            rect = pygame.Rect(int(part.x)*square_size, int(part.y)*square_size, square_size, square_size)
            pygame.draw.rect(screen, pygame.Color("green"), rect)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy
    def increase_snake_siz(self):
        new_x = self.body[-1].x
        new_y = self.body[-1].y
        self.body.insert(-1, Vector2(new_x, new_y))

class Fruit:
    def __init__(self):
        self.x = random.randint(0, square_number - 1)
        self.y = random.randint(0, square_number - 1)
        self.pos = Vector2(self.x , self.y)
    
    def draw_fruit(self):
        rect = pygame.Rect(int(self.pos.x)*square_size, int(self.pos.y)*square_size, square_size, square_size)
        pygame.draw.rect(screen, pygame.Color("red"), rect)
    def change_fruit(self):
        self.x = random.randint(0, square_number - 1)
        self.y = random.randint(0, square_number - 1)
        self.pos = Vector2(self.x , self.y)


square_size = 15
square_number = 30
screen = pygame.display.set_mode((square_size*square_number, square_size*square_number))
pygame.display.set_caption("My Snake Game")
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()
score = Score()
SCREEN_UPDATE = pygame.USEREVENT # creating an event
pygame.time.set_timer(SCREEN_UPDATE, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.display_score()
            pygame.quit()
            sys.exit()
            
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
            if snake.body[0] == fruit.pos:
                score.increase_score()
                fruit.change_fruit()
                snake.increase_snake_siz()
            for i in snake.body[1:]:
                if i == snake.body[0]:
                    pygame.quit()
                    sys.exit()
            if snake.body[0].x >= square_number or snake.body[0].x < 0 or snake.body[0].y >= square_number or snake.body[0].y < 0:
                    pygame.quit()
                    sys.exit()
        if event.type == pygame.KEYDOWN: # a key pressed
            if event.key == pygame.K_UP:
                if snake.direction.y != 1:
                    snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if snake.direction.y != -1:
                    snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if snake.direction.x != -1:
                    snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if snake.direction.x != 1:
                    snake.direction = Vector2(-1, 0)
           

    screen.fill(pygame.Color("black"))
    score.display_score()
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)