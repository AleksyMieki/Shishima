import pygame
import constants


class Board:
    def __init__(self):
        self.board = [
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
            ['O', None, None]
        ]
        self.player_pieces = {
            'X': [(0, 0), (0, 1), (0, 2)],
            'O': [(2, 0), (1, 1),(1,2)]
        }
        self.board_image = pygame.image.load('board.png')
        self.square_positions = [
            [(236, 104), (374, 104), (470, 201)],
            [(470, 333), (374, 424), (236, 424)],
            [(143, 333), (143, 201), (307, 256)]
        ]

    def is_valid_move(self, old_i, old_j, new_i, new_j):
        if (new_i, new_j) in self.player_pieces['X'] or (new_i, new_j) in self.player_pieces['O']:
            return False

        allowed_moves = {
            (0, 0): [(0, 1), (2, 2), (2, 1)],
            (0, 1): [(0, 0), (2, 2), (0, 2)],
            (0, 2): [(0, 1), (2, 2), (1, 0)],
            (1, 0): [(0, 2), (2, 2), (1, 1)],
            (1, 1): [(1, 0), (2, 2), (1, 2)],
            (1, 2): [(1, 1), (2, 2), (2, 0)],
            (2, 0): [(1, 2), (2, 2), (2, 1)],
            (2, 1): [(2, 0), (2, 2), (0, 0)],
            (2, 2): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)]
        }

        return (new_i, new_j) in allowed_moves[(old_i, old_j)]

    def move_piece(self, old_i, old_j, new_i, new_j):
        # Move the piece on the board
        self.board[new_i][new_j] = self.board[old_i][old_j]
        self.board[old_i][old_j] = None

        # Update the player_pieces dictionary
        self.player_pieces[self.board[new_i][new_j]].remove((old_i, old_j))
        self.player_pieces[self.board[new_i][new_j]].append((new_i, new_j))

    def draw(self, screen, selected_piece=None, coords_font=None):
        # Draw the board image
        screen.blit(self.board_image, (0, -5))

        for player, color in [('X', constants.RED), ('O', constants.BLUE)]:
            for i, j in self.player_pieces[player]:
                x, y = self.square_positions[i][j]
                pygame.draw.circle(screen, color, (x, y), 30)

        # Draw the selected piece with a different color (e.g., yellow)
        if selected_piece is not None:
            i, j = selected_piece
            x, y = self.square_positions[i][j]
            pygame.draw.circle(screen, constants.YELLOW, (x, y), 30, 5)

    def get_square_index(self, x, y):
        for i, row in enumerate(self.square_positions):
            for j, (sx, sy) in enumerate(row):
                if abs(sx - x) < 30 and abs(sy - y) < 30:
                    return i, j
        return None, None

    def is_full(self):
        return len(self.player_pieces['X']) + len(self.player_pieces['O']) == 9

    def check_winner(self):
        if self.board[0][0] == self.board[2][2] == self.board[1][1] and self.board[2][2] != '':
            return self.board[2][2]
        if self.board[0][1] == self.board[2][2] == self.board[1][2] and self.board[2][2] != '':
            return self.board[2][2]
        if self.board[0][2] == self.board[2][2] == self.board[2][0] and self.board[2][2] != '':
            return self.board[2][2]
        if self.board[1][0] == self.board[2][2] == self.board[2][1] and self.board[2][2] != '':
            return self.board[2][2]
        return None