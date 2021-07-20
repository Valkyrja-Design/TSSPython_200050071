import sys
import pygame
import time

def check_events(screen,snake,food):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                snake.change_direction('RIGHT')
            elif (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                snake.change_direction('LEFT')
            elif (event.key == pygame.K_w or event.key == pygame.K_UP):
                snake.change_direction('UP')
            elif (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                snake.change_direction('DOWN')
                
def update_screen(settings,screen,snake,food):
    screen.fill(settings.bg_color)
    display_score(screen,snake.score)
    snake.draw_snake()
    food.draw_food()
    pygame.display.flip()

def game_over(settings,screen,score):
    #gameover 
    gameover_img = pygame.font.SysFont('timesnewroman', 60).render("YOU DIED", True, (166,16,30))
    gameover_rect = gameover_img.get_rect()
    gameover_rect.centerx = settings.frame_size_x/2
    gameover_rect.centery = settings.frame_size_y/2-50

    #score
    score_img = pygame.font.SysFont('timesnewroman', 30).render("Score : "+str(score),True, (166,16,30))
    score_rect = score_img.get_rect()
    score_rect.centerx = settings.frame_size_x/2
    score_rect.centery = settings.frame_size_y/2+10
    #draw the text on the screen
    screen.fill(settings.bg_color)
    screen.blit(score_img,score_rect)
    screen.blit(gameover_img, gameover_rect)
    #display the last drawn screen
    pygame.display.flip()
    #wait for 3 seconds and then exit the game
    time.sleep(3)
    pygame.display.quit()
    sys.exit()

def display_score(screen,score):
    score_img = pygame.font.SysFont('timesnewroman', 20).render("Score : "+str(score),True, (240,240,240))
    score_rect = score_img.get_rect()
    score_rect.top = 20
    score_rect.left = 40
    screen.blit(score_img,score_rect)
    
            
