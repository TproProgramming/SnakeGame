import pygame
import random
import sys


def run_game():
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

    # Set the initial score
    score = 0

    # Set the font for the score display
    font = pygame.font.Font(None, 36)

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

            # Increment the score
            score += 1

        # Check for collision with walls
        if (
            snake[0].x < 0
            or snake[0].x > 640 - 20
            or snake[0].y < 0
            or snake[0].y > 480 - 20
        ):
            # Game over
            return score

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, (0, 255, 0), segment)

        # Draw the food
        pygame.draw.rect(screen, (255, 0, 0), food)

        # Render the score text
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))

        # Draw the score text on the screen
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Wait for a frame
        clock.tick(60)


def show_high_scores(scores):
    # Sort scores in descending order
    scores.sort(reverse=True)

    # Display the top 10 scores
    print("----- Top 10 High Scores -----")
    for i, (name, score) in enumerate(scores[:10]):
        print(f"{i+1}. {name}: {score}")
    print("-----------------------------")


def update_high_scores(scores, new_score, name):
    scores.append((name, new_score))
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:10]  # Keep only the top 10 scores
    return scores


def save_high_scores(scores):
    with open("highscores.txt", "w") as file:
        for name, score in scores:
            file.write(f"{name}:{score}\n")


def load_high_scores():
    try:
        with open("highscores.txt", "r") as file:
            scores = [line.strip().split(":") for line in file]
            scores = [(name, int(score)) for name, score in scores]
    except FileNotFoundError:
        scores = []
    return scores


def play_game():
    high_scores = load_high_scores()

    while True:
        score = run_game()

        if score > 0 and score > min([s for _, s in high_scores] + [0]):
            # Player broke into the top 10 scores
            name = input("Congratulations! Enter your name: ")
            high_scores = update_high_scores(high_scores, score, name)
            save_high_scores(high_scores)
            show_high_scores(high_scores)
        else:
            # Player did not break into the top 10 scores
            show_high_scores(high_scores)

        play_again = input("Play again? (Y/N): ")
        if play_again.upper() != "Y":
            break


play_game()

