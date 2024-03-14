import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

window_size = (600, 650)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe")


class TicTacToe():
    def __init__(self, table_size):
        self.table_size = table_size
        self.cell_size = table_size // 6
        self.table_space = 20

        self.player = "X"
        self.winner = None
        self.taking_move = True
        self.running = True
        self.table = []
        for col in range(6):
            self.table.append([])
            for row in range(6):
                self.table[col].append("-")

        self.background_color = (25, 174, 66)
        self.table_color = (50, 50, 50)
        self.line_color = (190, 0, 10)
        self.instructions_color = (17, 53, 165)
        self.game_over_bg_color = (47, 98, 162)
        self.game_over_color = (255, 179, 1)
        self.font = pygame.font.SysFont("Courier New", 30)
        self.FPS = pygame.time.Clock()

    def _draw_table(self):
        tb_space_point = (self.table_space, self.table_size - self.table_space)
        cell_space_point = (self.cell_size, self.cell_size * 2)
        for i in range(1, 6):
            pygame.draw.line(screen, self.table_color, (self.cell_size * i, self.table_space),
                             (self.cell_size * i, self.table_size - self.table_space), 8)
            pygame.draw.line(screen, self.table_color, (self.table_space, self.cell_size * i),
                             (self.table_size - self.table_space, self.cell_size * i), 8)

    def _change_player(self):
        self.player = "O" if self.player == "X" else "X"

    def _move(self, pos):
        try:
            x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
            if self.table[x][y] == "-":
                self.table[x][y] = self.player
                self._draw_char(x, y, self.player)
                self._game_check()
                self._change_player()
        except IndexError:
            print("Click inside the table only")

    def _draw_char(self, x, y, player):
        if self.player == "O":
            img = pygame.image.load("images/Tc-O.png")
        elif self.player == "X":
            img = pygame.image.load("images/Tc-X.png")
        img = pygame.transform.scale(img, (self.cell_size, self.cell_size))
        screen.blit(img, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def _message(self):
        if self.winner is not None:
            screen.fill(self.game_over_bg_color, (220, 605, 160, 30))
            msg = self.font.render(f'{self.winner} WINS!!', True, self.game_over_color)
            screen.blit(msg, (230, 605))
        elif not self.taking_move:
            screen.fill(self.game_over_bg_color, (220, 605, 160, 30))
            instructions = self.font.render('DRAW!!', True, self.game_over_color)
            screen.blit(instructions, (270, 605))
        else:
            screen.fill(self.background_color, (220, 605, 160, 30))
            instructions = self.font.render(f'{self.player} to move', True, self.instructions_color)
            screen.blit(instructions, (220, 605))

    def _game_check(self):
        # Vertical, Horizontal, and Diagonal checks
        for i in range(6):
            for j in range(4):
                # Vertical check
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i][j + 1] == self.table[i][j + 2]:
                    self._pattern_strike((i, j), (i, j + 2))
                    self.winner = self.player
                    self.taking_move = False
                    return
                # Horizontal check
                if self.table[j][i] != "-" and self.table[j][i] == self.table[j + 1][i] == self.table[j + 2][i]:
                    self._pattern_strike((j, i), (j + 2, i))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Left diagonal check
        for i in range(4):
            for j in range(4):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i + 1][j + 1] == self.table[i + 2][j + 2]:
                    self._pattern_strike((i, j), (i + 2, j + 2))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Right diagonal check
        for i in range(4):
            for j in range(2, 6):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i + 1][j - 1] == self.table[i + 2][j - 2]:
                    self._pattern_strike((i, j), (i + 2, j - 2))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Check for draw
        if all(cell != "-" for row in self.table for cell in row):
            self.taking_move = False

    def _pattern_strike(self, start_point, end_point):
        mid_val = self.cell_size // 2
        start_x, start_y = start_point[0] * self.cell_size + mid_val, start_point[1] * self.cell_size + mid_val
        end_x, end_y = end_point[0] * self.cell_size + mid_val, end_point[1] * self.cell_size + mid_val
        pygame.draw.line(screen, self.line_color, (start_x, start_y), (end_x, end_y), 8)

    def main(self):
        screen.fill(self.background_color)
        self._draw_table()
        while self.running:
            self._message()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.taking_move:
                        self._move(event.pos)
            pygame.display.flip()
            self.FPS.tick(60)


if __name__ == "__main__":
    g = TicTacToe(window_size[0])
    g.main()


    