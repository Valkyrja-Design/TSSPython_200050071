import pygame
import sys
import time
import random
from settings import Settings
from snake_body import Snake
from food import Food
import game_functions as gf

def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.frame_size_x,settings.frame_size_y))
    fps_controller = pygame.time.Clock()
    food = Food(settings,screen)
    score = 0
    snake = Snake(settings,screen,score)
    
    while True:
        gf.check_events(screen,snake,food)
        snake.update_snake(settings,gf.game_over)
        snake.check_food(food)
        gf.update_screen(settings,screen,snake,food)
        fps_controller.tick(25)

run_game()
