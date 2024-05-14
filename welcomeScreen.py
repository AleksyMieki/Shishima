import pygame
import constants


class WelcomeScreen:
    def __init__(self):
        self.title_font = pygame.font.Font("Sigmar-Regular.ttf", 80)
        self.title_text = self.title_font.render("SHISHIMA", True, constants.BLUE)

        self.play_button = pygame.Rect(100, 200, 220, 60)
        self.quit_button = pygame.Rect(100, 300, 220, 60)
        self.button_font = pygame.font.Font("Sigmar-Regular.ttf", 40)
        self.play_text = self.button_font.render("Play Game", True, constants.BLUE)
        self.quit_text = self.button_font.render("Quit", True, constants.BLUE)

    def draw_button(self, screen, button_rect, text_surface):
        pygame.draw.rect(screen, constants.BLACK, button_rect, border_radius=10)
        screen.blit(text_surface, (button_rect.x + 20, button_rect.y + 10))

    def draw(self, screen):
        screen.fill(constants.BLACK)

        screen.blit(self.title_text, (constants.WIDTH // 2 - self.title_text.get_width() // 2, 50))

        self.draw_button(screen, self.play_button, self.play_text)
        self.draw_button(screen, self.quit_button, self.quit_text)

    def handle_click(self, x, y):
        if self.play_button.collidepoint(x, y):
            return "play"
        elif self.quit_button.collidepoint(x, y):
            return "quit"

