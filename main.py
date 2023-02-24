import pygame
import random

# Initialize Pygame
pygame.init()

# Set up game window
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up game variables
snake_size = 10
food_size = 10
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

# Define functions
def message(msg, color):
    """
    Displays message on the game screen
    """
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, [window_width/6, window_height/3])

def draw_snake(snake_list):
    """
    Draws the snake on the game screen
    """
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_size, snake_size])

def game_loop():
    """
    Main game loop
    """
    game_exit = False
    game_over = False

    # Set up initial snake position and velocity

    x = window_width/2
    y = window_height/2
    print("x: \n", x)
    print("y: \n", y)

    x_velocity = 0
    y_velocity = 0
    snake_list = []
    snake_length = 1

    # Set up initial food position
    food_x = round(random.randrange(0, window_width - food_size)/10.0)*10.0
    food_y = round(random.randrange(0, window_height - food_size)/10.0)*10.0

    while not game_exit:

        while game_over == True:
            window.fill(white)
            message("Game over! Press Q to quit or C to play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_velocity = -snake_size
                    y_velocity = 0
                elif event.key == pygame.K_RIGHT:
                    x_velocity = snake_size
                    y_velocity = 0
                elif event.key == pygame.K_UP:
                    y_velocity = -snake_size
                    x_velocity = 0
                elif event.key == pygame.K_DOWN:
                    y_velocity = snake_size
                    x_velocity = 0

        # Move the snake
        
        print("type before",type(x))
        x += x_velocity
        y += y_velocity
        window.fill(white)
        pygame.draw.rect(window, red, [food_x, food_y, food_size, food_size])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_over = True
        print("type after",type(x))
        draw_snake(snake_list)
        pygame.display.update()

        # Check for collision with food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, window_width - food_size)/10.0)*10.0
            food_y = round(random.randrange(0, window_height - food_size)/10.0)*10.0
            snake_length += 10

        # Check for collision with wall or self
        if x < 0 or x >= window_width or y < 0 or y >= window_height:
            game_over = True

        clock.tick(10)

    pygame.quit()
    quit()


game_loop()
