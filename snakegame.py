import pygame
import random

# Initialize Pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen Dimensions
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Game clock
clock = pygame.time.Clock()

# Font for score
font = pygame.font.SysFont("arial", 25)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.body = [(100, 100)]
        self.direction = 'RIGHT'

    def move(self):
        head = self.body[0]
        if self.direction == 'UP':
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == 'DOWN':
            new_head = (head[0], head[1] + BLOCK_SIZE)
        elif self.direction == 'LEFT':
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == 'RIGHT':
            new_head = (head[0] + BLOCK_SIZE, head[1])

        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                         random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
        self.is_food_on_screen = True

    def spawn(self):
        if not self.is_food_on_screen:
            self.position = (random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                             random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
            self.is_food_on_screen = True

    def draw(self):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))

# Display Score
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

# Main game function
def game_loop():
    game_over = False
    snake = Snake()
    food = Food()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                if event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                if event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'

        snake.move()
        
        # Check for collision with walls
        head_x, head_y = snake.body[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over = True

        # Check for collision with itself
        if len(snake.body) != len(set(snake.body)):
            game_over = True

        # Check if the snake eats food
        if snake.body[0] == food.position:
            snake.grow()
            food.is_food_on_screen = False

        # Spawn new food if needed
        food.spawn()

        # Fill the screen
        screen.fill(BLACK)

        # Draw snake and food
        snake.draw()
        food.draw()

        # Display score
        show_score(snake.length - 1)

        # Update the display
        pygame.display.update()

        # Set the game speed
        clock.tick(10)

    # Game over message
    game_over_text = font.render("Game Over! Press Q-Quit or C-Play Again", True, WHITE)
    screen.blit(game_over_text, [WIDTH // 6, HEIGHT // 3])
    pygame.display.update()

    # Wait for user input to restart or quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    game_loop()  # Restart the game

# Start the game
game_loop()
