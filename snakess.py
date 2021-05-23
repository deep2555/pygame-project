import pygame
from pygame.locals import * 
import random as r
pygame.init()
pygame.mixer.init()
 
pygame.mixer.music.load("spook.mp3")
pygame.mixer.music.play()


screen  = pygame.display.set_mode((720,320))
name= pygame.display.set_caption("snakess")
baground = pygame.image.load("snake2.jfif")
baground = pygame.transform.scale(baground, (720,320)).convert_alpha()
rect3 = baground.get_rect()



def plot_snake(screen, color, snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen,color,[x,y, snake_size,snake_size])

font = pygame.font.SysFont(None,30)
def text_screen(text , color, x,y):
        screen_text = font.render(text, True, color)
        screen.blit(screen_text, [x,y])


def welcome():
    exit_game= False
    while not exit_game:
        screen.fill((233,230,233))
        
        # font1 = pygame.font.SysFont(None, 30)
        # img1 = font1.render("welcome to the snakes game! ",True, (255,0,0))
        # rect1 = img1.get_rect()
        text_screen("welcome to the snakess game",(0,0,255), 720//3.5,320//3)
        text_screen("press space bar to play",(0,0,255) , 720//3, 320//2)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        game_loop()
        
        pygame.display.update()
        # clock.tick(40)
        

def game_loop():
    
   
    #define variables
    game_over = False
    grey = (127,127,127)
    blue = (0,0,255)
    green = (0,250,0)
    red = (255,0,0)
    white= (255,255,255)
    black = (0,0,0)
    snake_x= 50
    snake_y= 100
    food_x = r.randint(20, 720//2)
    food_y = r.randint(20, 320//2)
    velocity_x = 4
    velocity_y = 4
    score = 0
    fps= 40
    snake_list = []
    snake_lenght = 1
    snake_size= 25
    running = True
    with open("highscore.txt", "r")as f :
        highscore = f.read()


    clock = pygame.time.Clock()
    


    while running:
        if game_over ==True:
            with open("highscore.txt", "w")as f :
                f.write(str(highscore))

            screen.fill(white)
            text_screen("!!! GAME OVER !!!"
             "WANT TO PLAY AGAIN ? ", red,720//5,320//2.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False


                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        welcome()

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     running = False

                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        velocity_x= 10
                        velocity_y = 0

                    if event.key == K_LEFT:
                        velocity_x = -10
                        velocity_y = 0

                    if event.key == K_UP:
                        velocity_y = -10
                        velocity_x = 0

                    if event.key == K_DOWN:
                        velocity_y = 10
                        velocity_x = 0

            
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<18 and abs(snake_y - food_y)<18:
                score +=10
                print(score)

                if score > int(highscore):
                    highscore = score

                food_x = r.randint(20, 720//2) 
                food_y = r.randint(20, 320//2)
                snake_lenght +=5


            screen.fill(grey)
            screen.blit(baground, rect3)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)> snake_lenght:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > 720 or snake_y < 0 or snake_y > 320:
                game_over = True
                

            plot_snake(screen, black, snake_list, snake_size)
            # snake = pygame.draw.rect(screen ,blue, (snake_x, snake_y, 25,25))
            food = pygame.draw.circle(screen, red , (food_x,food_y),9,0)
            text_screen(f"score = {score}, highscore = {highscore}", black, 5,5)
            # font = pygame.font.SysFont(None, 30)
            # img = font.render(f'score = {score}', True,red)
            # rect =img.get_rect()
            # screen.blit(img, rect)
            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
welcome()