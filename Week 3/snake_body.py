import pygame
class Snake:

    def __init__(self,settings,screen,score):
        self.screen = screen
        self.settings = settings
        self.score = score
        self.color = settings.snake_color
        self.direction = settings.init_direction
        self.snake_body=[]
        for i in settings.snake_body:
            self.snake_body.append(pygame.Rect(i[0],i[1],settings.snake_size,settings.snake_size))
                              
    def update_snake(self,settings,game_over):
        self.recent_tail_position_top = self.snake_body[len(self.snake_body)-1].top
        self.recent_tail_position_left = self.snake_body[len(self.snake_body)-1].left
        
        if (self.direction=='RIGHT'):
            head = self.snake_body[0]
            for i in self.snake_body:
                if (i == head):
                    continue
                elif (i.top == head.top and i.left == head.left+10):
                    game_over(self.settings,self.screen,self.score)
            if (self.snake_body[0].x+10>=settings.frame_size_x):
                game_over(self.settings,self.screen,self.score)
            else:
                for i in range(len(self.snake_body)-1,0,-1):
                    self.snake_body[i].x = self.snake_body[i-1].x
                    self.snake_body[i].y = self.snake_body[i-1].y
                self.snake_body[0].x+=10
                
        elif (self.direction=='LEFT'):
            head = self.snake_body[0]
            for i in self.snake_body:
                if (i == head):
                    continue
                elif (i.top == head.top and i.left == head.left-10):
                    game_over(self.settings,self.screen,self.score)
            if (self.snake_body[0].x<=0):
                game_over(self.settings,self.screen,self.score)
            else:
                for i in range(len(self.snake_body)-1,0,-1):
                    self.snake_body[i].x = self.snake_body[i-1].x
                    self.snake_body[i].y = self.snake_body[i-1].y
                self.snake_body[0].x-=10
                
        elif (self.direction=='UP'):
            head = self.snake_body[0]
            for i in self.snake_body:
                if (i == head):
                    continue
                elif (i.top == head.top-10 and i.left == head.left):
                    game_over(self.settings,self.screen,self.score)
            if (self.snake_body[0].y<=0):
                game_over(self.settings,self.screen,self.score)
            else:
                for i in range(len(self.snake_body)-1,0,-1):
                    self.snake_body[i].x = self.snake_body[i-1].x
                    self.snake_body[i].y = self.snake_body[i-1].y
                self.snake_body[0].y-=10
                
        elif (self.direction=='DOWN'):
            head = self.snake_body[0]
            for i in self.snake_body:
                if (i == head):
                    continue
                elif (i.top == head.top+10 and i.left == head.left):
                    game_over(self.settings,self.screen,self.score)
            if (self.snake_body[0].y+10>=settings.frame_size_y):
                game_over(self.settings,self.screen,self.score)
            else:
                for i in range(len(self.snake_body)-1,0,-1):
                    self.snake_body[i].x = self.snake_body[i-1].x
                    self.snake_body[i].y = self.snake_body[i-1].y
                self.snake_body[0].y+=10
        
    def draw_snake(self):
        
        for i in self.snake_body:
            pygame.draw.rect(self.screen,self.color,i)

    def change_direction(self,direction):
        if (direction == 'RIGHT' and self.direction != 'LEFT'):
            self.direction = direction
        elif (direction == 'LEFT' and self.direction != 'RIGHT'):
            self.direction = direction
        elif (direction == 'UP' and self.direction != 'DOWN'):
            self.direction = direction
        elif (direction == 'DOWN' and self.direction != 'UP'):
            self.direction = direction
            
    def grow_body(self):
        curr_body = self.snake_body
        length = len(curr_body)
        self.snake_body.append(pygame.Rect(self.recent_tail_position_left,self.recent_tail_position_top,self.settings.snake_size,self.settings.snake_size))
        
    def check_food(self,food):
        
        if (self.direction == 'RIGHT' and self.snake_body[0].right>=food.get_left() and self.snake_body[0].right<=food.get_right() and self.snake_body[0].top==food.get_top()):
            food.create_food(self.settings,self)
            self.score+=1
            self.grow_body()
            
        elif (self.direction == 'LEFT' and self.snake_body[0].left<=food.get_right() and self.snake_body[0].left>=food.get_left() and self.snake_body[0].top==food.get_top()):
            food.create_food(self.settings,self)
            self.score+=1
            self.grow_body()
        
        elif (self.direction == 'UP' and self.snake_body[0].top<=food.get_bottom() and self.snake_body[0].top>=food.get_top() and self.snake_body[0].left==food.get_left()):
            food.create_food(self.settings,self)
            self.score+=1
            self.grow_body()
        elif (self.direction == 'DOWN' and self.snake_body[0].bottom>=food.get_top() and self.snake_body[0].bottom<=food.get_bottom() and self.snake_body[0].left==food.get_left()):
            food.create_food(self.settings,self)
            self.score+=1
            self.grow_body()

    def get_snake_body(self):

        return self.snake_body
