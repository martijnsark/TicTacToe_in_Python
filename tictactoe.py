import pygame  # Importing pygame library for game development
import os  # Importing os module for interacting with the operating system

# Centers the window
os.environ['SDL_VIDEO_CENTERED'] = '1'  
pygame.init()  # Initializing pygame
pygame.font.init()  # Initializing font module

# Get the screen resolution
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Set the window size to match the screen resolution
window_size = (screen_width, screen_height)

screen = pygame.display.set_mode(window_size)  # Setting display window
pygame.display.set_caption("Tic Tac Toe")  # Setting the caption of the window


class StartScreen:
    def __init__(self):
        self.screens = [
            self.screen1,
            self.screen2,
            self.screen3,
            self.screen4
        ]
        self.current_screen_index = 0
        self.headline_font = pygame.font.SysFont("Courier New", 40)  # Setting headline font
        self.font = pygame.font.SysFont("Courier New", 25)  # Setting font
        self.button_img = pygame.image.load("images/exit.png")  # Loading button image
        self.button_rect = self.button_img.get_rect()
        self.button_rect.topright = (window_size[0] - 10, 10)
        self.depth = 4  # Depth for minimax algorithm

    # Method for displaying screen 1
    def screen1(self):
        screen.fill((192, 192, 192))  # Black background
        # Drawing headline (paragraph 1)
        headline_text = self.headline_font.render("Dit is een versie van Tic Tac Toe zonder machine learning.",
                                                  True, (0, 0, 0))
        headline_rect = headline_text.get_rect(center=(window_size[0] // 2, 50))  # Adjusted y-coordinate
        screen.blit(headline_text, headline_rect)

        # Adding empty space between paragraphs
        pygame.draw.rect(screen, (192, 192, 192), (0, 180, window_size[0], 20))

        # Drawing second extra text (paragraph 2)
        paragraph2_text = self.font.render("De regels van het spel.", True, (0, 0, 0))
        paragraph2_rect = paragraph2_text.get_rect(center=(window_size[0] // 2, 140))  # Adjusted y-coordinate
        paragraph2_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph2_text, paragraph2_rect)

        # Drawing second extra text (paragraph 2)
        paragraph2_text = self.font.render(
            "De winnaar is degene die als eerste vier op een rij heeft, horizontaal, verticaal en diagonaal.", True,
            (0, 0, 0))
        paragraph2_rect = paragraph2_text.get_rect(center=(window_size[0] // 2, 180))  # Adjusted y-coordinate
        paragraph2_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph2_text, paragraph2_rect)

        # Drawing third extra text (paragraph 3)
        paragraph3_text = self.font.render(
            "Je kunt alleen X'en en O's binnen het speelveld plaatsen van de 6 bij 6 rooster.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 210))  # Adjusted y-coordinate
        paragraph3_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph3_text, paragraph3_rect)

        # Drawing exit button
        screen.blit(self.button_img, self.button_rect)
        pygame.display.flip()

    # Method for displaying screen 2
    def screen2(self):
        screen.fill((192, 192, 192))  # Black background

        # Drawing headline (paragraph 1)
        headline_text = self.headline_font.render("Dit is een versie van Tic Tac Toe zonder machine learning.",
                                                  True, (0, 0, 0))
        headline_rect = headline_text.get_rect(center=(window_size[0] // 2, 50))  # Adjusted y-coordinate
        screen.blit(headline_text, headline_rect)

        # Drawing third extra text (paragraph 3)
        paragraph3_text = self.font.render("Hoe je speelt.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 140))  # Adjusted y-coordinate
        paragraph3_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph3_text, paragraph3_rect)

        # Drawing third extra text (paragraph 3)
        paragraph3_text = self.font.render("Normaal gesproken speel je tegen een AI.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 180))  # Adjusted y-coordinate
        paragraph3_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph3_text, paragraph3_rect)

        # Drawing third extra text (paragraph 3)
        paragraph3_text = self.font.render("Maar voor nu moet je met iemand anders samen spelen.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 210))  # Adjusted y-coordinate
        paragraph3_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph3_text, paragraph3_rect)

        # Drawing third extra text (paragraph 3)
        paragraph3_text = self.font.render("Het idee is dus dat je om de beurt speelt.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 240))  # Adjusted y-coordinate
        paragraph3_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph3_text, paragraph3_rect)

        # Drawing third extra text (paragraph 3)
        paragraph3_text = self.font.render(
            "Jullie spelen allebei op dezelfde computer, waarbij X altijd begint en O kies nu wie begint als welke.",
            True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 270))  # Adjusted y-coordinate
        paragraph3_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph3_text, paragraph3_rect)

        # Drawing exit button
        screen.blit(self.button_img, self.button_rect)
        pygame.display.flip()

    # Method for displaying screen 3
    def screen3(self):
        screen.fill((192, 192, 192))  # Black background

        # Drawing headline (paragraph 1)
        headline_text = self.headline_font.render("Dit is een versie van Tic Tac Toe zonder machine learning.",
                                                  True, (0, 0, 0))
        headline_rect = headline_text.get_rect(center=(window_size[0] // 2, 50))  # Adjusted y-coordinate
        screen.blit(headline_text, headline_rect)

        # Drawing third extra text (paragraph 4)
        paragraph4_text = self.font.render("De bediening.", True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 140))  # Adjusted y-coordinate
        paragraph4_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph4_text, paragraph4_rect)

        # Drawing third extra text (paragraph 4)
        paragraph4_text = self.font.render("Je kunt met linkermuisklik X'en en O's plaatsen.", True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 180))  # Adjusted y-coordinate
        paragraph4_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph4_text, paragraph4_rect)

        # Drawing third extra text (paragraph 4)
        paragraph4_text = self.font.render("Wanneer het spel voorbij is, kun je op ESC klikken om af te sluiten.",
                                            True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 210))
        # Adjusted y-coordinate
        paragraph4_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph4_text, paragraph4_rect)

        # Drawing third extra text (paragraph 4)
        paragraph4_text = self.font.render(
            "Je kunt ook linkermuisknop drukken op de swirl rechtsboven na een spel om opnieuw te beginnen.", True,
            (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 240))  # Adjusted y-coordinate
        paragraph4_rect.centerx = window_size[0] // 2  # Center horizontally
        screen.blit(paragraph4_text, paragraph4_rect)

        # Drawing exit button
        screen.blit(self.button_img, self.button_rect)
        pygame.display.flip()

    # Method for displaying screen 4
    def screen4(self):
        screen.fill((192, 192, 192))  # Black background
        paragraph4_text = self.font.render("Als je alles begrijpt, kun je rechtsboven op het kruisje klikken en beginnen.",
                                            True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 500))
        paragraph4_rect.centerx = window_size[0] // 2
        screen.blit(paragraph4_text, paragraph4_rect)

        # Drawing exit button
        screen.blit(self.button_img, self.button_rect)
        pygame.display.flip()

    # Method to show current screen
    def show_current_screen(self):
        self.screens[self.current_screen_index]()

    # Method to move to the next screen
    def next_screen(self):
        self.current_screen_index += 1
        if self.current_screen_index >= len(self.screens):
            return True  # Transition to the main game
        return False

    # Method to handle events
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    return self.next_screen()  # Transition to the next screen
        return False


class TicTacToe:
    def __init__(self, table_size, depth):
        self.table_size = min(window_size) - 100
        self.cell_size = self.table_size // 6
        self.table_space = self.cell_size // 3
        self.grid_offset_x = (window_size[0] - self.table_size) // 2
        self.grid_offset_y = (window_size[1] - self.table_size) // 4

        self.player = "X"
        self.ai_player = "O"
        self.winner = None
        self.taking_move = True
        self.running = True
        self.depth = depth  # Depth for minimax algorithm

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
        self.font = pygame.font.SysFont("Courier New", 50)
        self.FPS = pygame.time.Clock()

        self.restart_button_img = pygame.image.load("images/RestartGame.png")
        self.restart_button_rect = self.restart_button_img.get_rect()
        self.restart_button_rect.topright = (window_size[0] - 10, 10)


    # Method to draw the game grid
    def _draw_table(self):
        for i in range(7):
            pygame.draw.line(screen, self.table_color, (self.grid_offset_x + self.cell_size * i, self.grid_offset_y),
                             (self.grid_offset_x + self.cell_size * i, self.grid_offset_y + self.table_size),
                             self.cell_size // 8)
            pygame.draw.line(screen, self.table_color, (self.grid_offset_x, self.grid_offset_y + self.cell_size * i),
                             (self.grid_offset_x + self.table_size, self.grid_offset_y + self.cell_size * i),
                             self.cell_size // 8)

    # Method to switch players
    def _change_player(self):
        self.player = "O" if self.player == "X" else "X"

    # Method for player move
    def _move(self, pos):
        try:
            grid_x = (pos[0] - self.grid_offset_x) // self.cell_size
            grid_y = (pos[1] - self.grid_offset_y) // self.cell_size

            if 0 <= grid_x < 6 and 0 <= grid_y < 6:
                if self.table[grid_x][grid_y] == "-" and self.player == "X":
                    self.table[grid_x][grid_y] = self.player
                    self._draw_char(grid_x, grid_y, self.player)
                    self._game_check()
                    self._change_player()
                    if not self.taking_move:
                        return
                    self._ai_move()
        except IndexError:
            print("Click inside the table only")

   # Method to get empty cells on the board
    def _empty_cells(self):
        cells = []
        for i in range(6):
            for j in range(6):
                if self.table[i][j] == "-":
                    cells.append((i, j))
        return cells

    # Method to implement Minimax algorithm with alpha-beta pruning
    def _minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or not self.taking_move:
            if self.winner == self.ai_player:
                return 1
            elif self.winner == self.player:
                return -1
            else:
                return 0

        if maximizing_player:
            max_eval = float("-inf")
            for move in self._empty_cells():
                self.table[move[0]][move[1]] = self.ai_player
                eval = self._minimax(depth - 1, alpha, beta, False)
                self.table[move[0]][move[1]] = "-"
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            min_eval = float("inf")
            for move in self._empty_cells():
                self.table[move[0]][move[1]] = self.player
                eval = self._minimax(depth - 1, alpha, beta, True)
                self.table[move[0]][move[1]] = "-"
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval

    def _ai_move(self):
        best_move = None
        best_eval = float("-inf")
        alpha = float("-inf")  # Initial alpha value
        beta = float("inf")  # Initial beta value
        for move in self._empty_cells():
            self.table[move[0]][move[1]] = self.ai_player
            eval = self._minimax(self.depth, alpha, beta, False)  # Initial call with alpha and beta
            self.table[move[0]][move[1]] = "-"
            if eval > best_eval:
                best_eval = eval
                best_move = move
            alpha = max(alpha, eval)

        if best_move:
            self.table[best_move[0]][best_move[1]] = self.ai_player
            self._draw_char(best_move[0], best_move[1], self.ai_player)
            self._game_check()
            self._change_player()

    # Method to draw X or O on the grid
    def _draw_char(self, x, y, player):
        if player == "O":
            img = pygame.image.load("images/Tc-O.png")
        elif player == "X":
            img = pygame.image.load("images/Tc-X.png")
        img = pygame.transform.scale(img, (self.cell_size - self.table_space, self.cell_size - self.table_space))
        screen.blit(img, (self.grid_offset_x + x * self.cell_size + self.table_space // 2,
                          self.grid_offset_y + y * self.cell_size + self.table_space // 2))

    # Method to display game messages
    def _message(self):
        message = ""
        if self.winner is not None:
            message = f'{self.winner} heeft gewonnen!!'
        elif not self.taking_move:
            message = 'GELIJKSPEL!!'
        else:
            message = f'{self.player} kan nu iets plaatsen in de grid.'

        screen.fill(self.background_color, (0, window_size[1] - 50, window_size[0], 50))
        msg = self.font.render(message, True, self.instructions_color)
        screen.blit(msg, ((window_size[0] - msg.get_width()) // 2, window_size[1] - 50))

        screen.blit(self.restart_button_img, self.restart_button_rect)

    # Method to check game status
    def _game_check(self):
        # Check horizontal wins
        for i in range(6):
            for j in range(3):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i][j + 1] == self.table[i][j + 2] == \
                        self.table[i][j + 3]:
                    # If a win is detected, draw the winning pattern, set the winner, and stop the game
                    self._pattern_strike((i, j), (i, j + 3))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Check vertical wins
        for i in range(3):
            for j in range(6):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i + 1][j] == self.table[i + 2][j] == \
                        self.table[i + 3][j]:
                    # If a win is detected, draw the winning pattern, set the winner, and stop the game
                    self._pattern_strike((i, j), (i + 3, j))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Check diagonal (from top left to bottom right) wins
        for i in range(3):
            for j in range(3):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i + 1][j + 1] == self.table[i + 2][
                    j + 2] == self.table[i + 3][j + 3]:
                    # If a win is detected, draw the winning pattern, set the winner, and stop the game
                    self._pattern_strike((i, j), (i + 3, j + 3))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Check diagonal (from top right to bottom left) wins
        for i in range(3):
            for j in range(3, 6):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i + 1][j - 1] == self.table[i + 2][
                    j - 2] == self.table[i + 3][j - 3]:
                    # If a win is detected, draw the winning pattern, set the winner, and stop the game
                    self._pattern_strike((i, j), (i + 3, j - 3))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # If there are no wins and the grid is full, it's a draw
        if all(cell != "-" for row in self.table for cell in row):
            self.taking_move = False


    # Method to draw winning pattern
    def _pattern_strike(self, start_point, end_point):
        mid_val = self.cell_size // 2
        start_x, start_y = self.grid_offset_x + start_point[0] * self.cell_size + mid_val, self.grid_offset_y + \
                           start_point[1] * self.cell_size + mid_val
        end_x, end_y = self.grid_offset_x + end_point[0] * self.cell_size + mid_val, self.grid_offset_y + \
                       end_point[1] * self.cell_size + mid_val
        pygame.draw.line(screen, self.line_color, (start_x, start_y), (end_x, end_y), self.cell_size // 8)

    # Method to restart the game
    def restart_game(self):
        self.player = "X"
        self.winner = None
        self.taking_move = True
        self.table = [["-" for _ in range(6)] for _ in range(6)]
        screen.fill(self.background_color)
        self._draw_table()

    # Main method to run the game
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
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.VIDEORESIZE:
                    window_size = event.size
                    self.grid_offset_x = (window_size[0] - self.table_size) // 2
                    self.grid_offset_y = (window_size[1] - self.table_size) // 4
                    self.restart_button_rect.topright = (window_size[0] - 10, 10)
            pygame.display.flip()
            self.FPS.tick(60)


if __name__ == "__main__":
    start_screen = StartScreen()
    while True:
        if start_screen.handle_events():
            break
        start_screen.show_current_screen()

    depth = start_screen.depth  # Get depth from StartScreen
    g = TicTacToe(window_size[0], depth)  # Pass depth to TicTacToe
    g.main()