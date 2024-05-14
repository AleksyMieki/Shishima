import pygame
import board
import sys
import constants
import welcomeScreen
import game_engine as g


def main():

    pygame.init()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Shishima")
    clock = pygame.time.Clock()
    game_state = "welcome"
    welcome_screen = welcomeScreen.WelcomeScreen()
    game = g.Game()

    running = True
    while running:

        screen.fill(constants.WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == "welcome":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    button = welcome_screen.handle_click(x, y)
                    if button == "play":
                        game = g.Game()
                        game_state = "play"
                    elif button == "quit":
                        running = False

            elif game_state == "play":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    game.handle_click(x, y)

        if game_state == "welcome":
            welcome_screen.draw(screen)
        elif game_state == "play":
            game.draw(screen)
            if game.game_over:
                game.draw(screen)
                pygame.display.flip()
                pygame.time.delay(2000)
                game_state = "welcome"

        pygame.display.flip()
        clock.tick(constants.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
