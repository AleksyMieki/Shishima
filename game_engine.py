import pygame
import board
import constants


class Game:
    def __init__(self):
        self.board = board.Board()
        self.player_turn = 'X'
        self.selected_piece = None
        self.game_over = False
        self.winner = None
        self.winner_font = pygame.font.Font(None, 40)
        self.coords_font = pygame.font.Font(None, 20)

    def draw(self, screen):
        # Draw the board and the pieces
        self.board.draw(screen, selected_piece=self.selected_piece)

        if self.game_over:
            winner_text = f"Player {self.winner} wins!"
            self.winner = self.player_turn
            winner_render = self.winner_font.render(winner_text, True, constants.BLACK)
            screen.blit(winner_render, (constants.WIDTH // 2 - 100, constants.HEIGHT // 2 - 40))
        # Display the game status

    def find_closest_square(self, x, y):
        min_distance = float('inf')
        closest_square = None
        click_threshold = 40

        for i in range(3):
            for j in range(3):
                square_x, square_y = self.board.square_positions[i][j]
                distance = (x - square_x) ** 2 + (y - square_y) ** 2

                if distance < min_distance:
                    min_distance = distance
                    closest_square = (i, j)

        if min_distance < click_threshold ** 2:
            return closest_square
        return None

    def handle_click(self, x, y):
        i, j = self.board.get_square_index(x, y)

        winner = self.board.check_winner()
        if winner or self.board.is_full():
            self.game_over = True
            self.winner = winner

        if (i, j) in self.board.player_pieces[self.player_turn]:
            self.selected_piece = (i, j)
            return

        if self.selected_piece is not None:
            old_i, old_j = self.selected_piece

            if self.board.is_valid_move(old_i, old_j, i, j):
                self.board.move_piece(old_i, old_j, i, j)
                self.selected_piece = None
                self.player_turn = 'O' if self.player_turn == 'X' else 'X'

        if self.board.check_winner() or self.board.is_full():
            self.game_over = True
