class Settings:
    """Game Settings"""
    def __init__(self):
        #window parameters
        self.frame_size_x = 720
        self.frame_size_y = 480
        self.bg_color = (0,0,0)
        
        #parameters for snake
        self.snake_size = 10
        self.snake_pos = [100,50]
        self.snake_body = [[100,50],[90,50],[80,50]]
        self.init_direction = 'RIGHT'
        self.snake_color = (0, 255, 0)
    
        #parameters for food
        self.food_pos = [0,0]
        self.food_spawn = False
        
