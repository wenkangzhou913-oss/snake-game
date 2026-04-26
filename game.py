import pygame
import sys
import random
from snake import Snake
from food import Food

class Game:
    def __init__(self, width=800, height=600, grid_size=20):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.cols = width // grid_size
        self.rows = height // grid_size
        
        # Initialize Pygame
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.fps = 10
        
        # Game objects
        self.snake = Snake()
        self.food = Food(self.cols, self.rows)
        self.score = 0
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction((1, 0))
        return True

    def update(self):
        self.snake.move()
        
        # Check if snake eats food
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.refresh_food()
            self.score += 10
        
        # Check if snake collides with itself
        if self.snake.check_collision():
            self.game_over = True
        
        # Check if snake goes out of bounds
        head_x, head_y = self.snake.body[0]
        if head_x < 0 or head_x >= self.cols or head_y < 0 or head_y >= self.rows:
            self.game_over = True

    def render(self):
        self.screen.fill((0, 0, 0))  # Black background
        
        # Draw snake
        for segment in self.snake.body:
            x = segment[0] * self.grid_size
            y = segment[1] * self.grid_size
            pygame.draw.rect(self.screen, (0, 255, 0), (x, y, self.grid_size, self.grid_size))
        
        # Draw food
        food_x = self.food.position[0] * self.grid_size
        food_y = self.food.position[1] * self.grid_size
        pygame.draw.rect(self.screen, (255, 0, 0), (food_x, food_y, self.grid_size, self.grid_size))
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

    def run(self):
        running = True
        while running and not self.game_over:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        
        # Game over screen
        self.show_game_over()

    def show_game_over(self):
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        
        self.screen.fill((0, 0, 0))
        self.screen.blit(game_over_text, (self.width // 2 - 250, self.height // 2 - 100))
        self.screen.blit(score_text, (self.width // 2 - 150, self.height // 2))
        pygame.display.flip()
        
        # Wait for 3 seconds before closing
        pygame.time.wait(3000)
