import pygame
import random

class Food:

    def __init__(self,settings,screen):
        
        self.screen = screen
        self.food = pygame.Rect(200,300,10,10)
        self.color = (255,0,0)
        
    def create_food(self,settings,snake):

        while(True):
            self.food.left = random.randrange(0,settings.frame_size_x-5,10)
            self.food.top = random.randrange(0,settings.frame_size_y-5,10)
            flag = False
            for i in snake.get_snake_body():
                if (self.food.left == i.left and self.food.top == i.top):
                   flag = True 
            if not (flag):
                break
        
    def draw_food(self):

        pygame.draw.rect(self.screen,self.color,self.food)

    def get_top(self):

        return self.food.top

    def get_left(self):

        return self.food.left

    def get_right(self):

        return self.food.right

    def get_bottom(self):

        return self.food.bottom
