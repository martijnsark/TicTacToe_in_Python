import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centers the window
pygame.init()
pygame.font.init()

# Get the screen resolution
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Set the window size to match the screen resolution
window_size = (screen_width, screen_height)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe")


class TicTacToe():
    def __init__(self, table_size):
        self.table_size = min(window_size) - 100  # Adjusted for screen size
        self.cell_size = self.table_size // 6
        self.table_space = self.cell_size // 3  # Adjusted for screen size
        self.grid_offset_x = (window_size[0] - self.table_size) // 2
        self.grid_offset_y = (window_size[1] - self.table_size) // 4  # Adjusted for positioning

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
        self.instructions_color = (0, 0, 255)
        self.game_over_bg_color = (47, 98, 162)
        self.game_over_color = (255, 179, 1)
        self.font = pygame.font.SysFont("Courier New", 50)  # Text height set to 50 pixels
        self.FPS = pygame.time.Clock()

        # Load restart button image
        self.restart_button_img = pygame.image.load("images/RestartGame.png")
        self.restart_button_rect = self.restart_button_img.get_rect()
        self.restart_button_rect.topright = (window_size[0] - 10, 10)

    def _draw_table(self):
        tb_space_point = (self.table_space, self.table_size - self.table_space)
        cell_space_point = (self.cell_size, self.cell_size * 2)
        for i in range(1, 6):
            pygame.draw.line(screen, self.table_color, (self.grid_offset_x + self.cell_size * i, self.grid_offset_y + self.table_space),
                             (self.grid_offset_x + self.cell_size * i, self.grid_offset_y + self.table_size - self.table_space), self.cell_size // 8)  # Adjusted for screen size
            pygame.draw.line(screen, self.table_color, (self.grid_offset_x + self.table_space, self.grid_offset_y + self.cell_size * i),
                             (self.grid_offset_x + self.table_size - self.table_space, self.grid_offset_y + self.cell_size * i), self.cell_size // 8)  # Adjusted for screen size

    def _change_player(self):
        self.player = "O" if self.player == "X" else "X"

    def _move(self, pos):
        try:
            x, y = (pos[0] - self.grid_offset_x) // self.cell_size, (pos[1] - self.grid_offset_y) // self.cell_size
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
        screen.blit(img, (self.grid_offset_x + x * self.cell_size, self.grid_offset_y + y * self.cell_size))

    def _message(self):
        message = ""
        if self.winner is not None:
            message = f'{self.winner} WINS!!'
        elif not self.taking_move:
            message = 'DRAW!!'
        else:
            message = f'{self.player} to move'

        # Clear previous message
        screen.fill(self.background_color, (0, window_size[1] - 50, window_size[0], 50))

        # Render and display the current message at the bottom of the screen
        msg = self.font.render(message, True, self.instructions_color)
        screen.blit(msg, ((window_size[0] - msg.get_width()) // 2, window_size[1] - 50))  # Adjusted y-coordinate

        # Draw restart button
        screen.blit(self.restart_button_img, self.restart_button_rect)

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
        start_x, start_y = self.grid_offset_x + start_point[0] * self.cell_size + mid_val, self.grid_offset_y + start_point[1] * self.cell_size + mid_val
        end_x, end_y = self.grid_offset_x + end_point[0] * self.cell_size + mid_val, self.grid_offset_y + end_point[1] * self.cell_size + mid_val
        pygame.draw.line(screen, self.line_color, (start_x, start_y), (end_x, end_y), self.cell_size // 8)

    def restart_game(self):
        self.player = "X"
        self.winner = None
        self.taking_move = True
        self.table = [["-" for _ in range(6)] for _ in range(6)]
        # Clear the screen
        screen.fill(self.background_color)
        # Redraw the table
        self._draw_table()

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
                    elif self.restart_button_rect.collidepoint(event.pos):
                        self.restart_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Exit on pressing Escape key
                        self.running = False
                if event.type == pygame.VIDEORESIZE:
                    window_size = event.size
                    self.grid_offset_x = (window_size[0] - self.table_size) // 2
                    self.grid_offset_y = (window_size[1] - self.table_size) // 4  # Adjusted for positioning
                    self.restart_button_rect.topright = (window_size[0] - 10, 10)
            pygame.display.flip()
            self.FPS.tick(60)


if __name__ == "__main__":
    g = TicTacToe(window_size[0])
    g.main()