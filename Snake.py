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


def show_high_scores(high_scores, screen, font):
    screen.fill((0, 0, 0))

    # Sort scores in descending order
    high_scores.sort(key=lambda x: x[1], reverse=True)

    # Display the top 10 scores
    title_text = font.render("Top 10 High Scores", True, (255, 255, 255))
    screen.blit(title_text, (250, 50))

    for i, (name, score) in enumerate(high_scores[:10]):
        score_text = font.render(f"{i + 1}. {name}: {score}", True, (255, 255, 255))
        screen.blit(score_text, (250, 100 + i * 30))

    pygame.display.update()


def get_player_name(screen, font):
    input_box = pygame.Rect(250, 250, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    player_name = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, input_box, 2)
        
        # Add text above the input box
        text_prompt = font.render("Enter Your Name:", True, (255, 255, 255))
        screen.blit(text_prompt, (250, 220))
        
        text_surface = font.render(player_name, True, (255, 255, 255))
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

    return player_name

 
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
    # Initialize pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((640, 480))

    # Set the font for the score display
    font = pygame.font.Font(None, 36)

    high_scores = load_high_scores()

    while True:
        score = run_game()

        if score > 0 and score > min([s for _, s in high_scores] + [0]):
            # Player broke into the top 10 scores
            player_name = get_player_name(screen, font)
            high_scores = update_high_scores(high_scores, score, player_name)
            save_high_scores(high_scores)
            show_high_scores(high_scores, screen, font)
        else:
            # Player did not break into the top 10 scores
            show_high_scores(high_scores, screen, font)

        play_again = ''
        while play_again.upper() != "Y" and play_again.upper() != "N":
            play_again_text = font.render("Play again? (Y/N): ", True, (255, 255, 255))
            screen.blit(play_again_text, (250, 400))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        play_again = "Y"
                    elif event.key == pygame.K_n:
                        play_again = "N"

        if play_again.upper() == "N":
            break


def main():
    # Initialize pygame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((640, 480))

    # Set the font for the score display
    font = pygame.font.Font(None, 36)

    play_game()

    # Display high scores before quitting
    show_high_scores(load_high_scores(), screen, font)

    while True:
        play_again_text = font.render("Play again? (Y/N): ", True, (255, 255, 255))
        screen.blit(play_again_text, (250, 400))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    play_game()
                    show_high_scores(load_high_scores(), screen, font)
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()

