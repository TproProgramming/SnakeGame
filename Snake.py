import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((640, 480))

# Create the snake
snake = [pygame.Rect(200, 200, 20, 20)]

# Create the food
food = pygame.Rect(400, 400, 20, 20)

# Create the clock
clock = pygame.time.Clock()

# Set the initial movement direction
direction = "RIGHT"

# Set the game timer
movement_timer = pygame.time.get_ticks()

# Set the movement speed (lower value = faster speed)
movement_speed = 150

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Update the snake's movement based on the timer
    if pygame.time.get_ticks() - movement_timer >= movement_speed:
        if direction == "UP":
            snake[0].y -= 20
        elif direction == "DOWN":
            snake[0].y += 20
        elif direction == "LEFT":
            snake[0].x -= 20
        elif direction == "RIGHT":
            snake[0].x += 20

        # Move the snake body
        for i in range(len(snake) - 1, 0, -1):
            snake[i].x = snake[i - 1].x
            snake[i].y = snake[i - 1].y

        # Reset the movement timer
        movement_timer = pygame.time.get_ticks()

    # Check for collision with food
    if snake[0].colliderect(food):
        # Grow the snake
        segment = pygame.Rect(snake[-1].x, snake[-1].y, 20, 20)
        snake.append(segment)

        # Create new food
        food.x = random.randint(0, 640 - 20)
        food.y = random.randint(0, 480 - 20)

    # Check for collision with walls
    if snake[0].x < 0 or snake[0].x > 640 - 20 or snake[0].y < 0 or snake[0].y > 480 - 20:
        # Game over
        pygame.quit()
        sys.exit()
    
    """
    # Check for collision with itself
    for segment in snake[1:]:
        if snake[0].colliderect(segment):
            # Game over
            pygame.quit()
            sys.exit()
    """
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), segment)

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), food)

    # Update the display
    pygame.display.update()

    # Wait for a frame
    clock.tick(60)
