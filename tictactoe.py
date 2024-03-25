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

class StartScreen:
    def __init__(self):
        self.headline_font = pygame.font.SysFont("Courier New", 40)  # Koplettergrootte ingesteld op 40 pixels
        self.font = pygame.font.SysFont("Courier New", 25)  # Tekstgrootte ingesteld op 25 pixels
        self.button_img = pygame.image.load("images/exit.png")
        self.button_rect = self.button_img.get_rect()
        self.button_rect.topright = (window_size[0] - 10, 10)

    def show(self):
        screen.fill((192, 192, 192))  # Zwarte achtergrond
        
        # Teken kopregel (alinea 1)
        headline_text = self.headline_font.render("Dit is een versie van Tic Tac Toe zonder machine learning.", True, (0, 0, 0))
        headline_rect = headline_text.get_rect(center=(window_size[0] // 2, 50))  # Aangepaste y-coördinaat
        screen.blit(headline_text, headline_rect)
        
        # Voeg lege ruimte toe tussen alinea's
        pygame.draw.rect(screen, (192, 192, 192), (0, 180, window_size[0], 20))
        
        # Teken tweede extra tekst (alinea 2)
        paragraph2_text = self.font.render("De regels van het spel.", True, (0, 0, 0))
        paragraph2_rect = paragraph2_text.get_rect(center=(window_size[0] // 2, 140))  # Aangepaste y-coördinaat
        paragraph2_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph2_text, paragraph2_rect)
        
        # Teken tweede extra tekst (alinea 2)
        paragraph2_text = self.font.render("De winnaar is degene die als eerste vier op een rij heeft, horizontaal, verticaal en diagonaal.", True, (0, 0, 0))
        paragraph2_rect = paragraph2_text.get_rect(center=(window_size[0] // 2, 180))  # Aangepaste y-coördinaat
        paragraph2_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph2_text, paragraph2_rect)
        
        # Teken derde extra tekst (alinea 3)
        paragraph3_text = self.font.render("Je kunt alleen X'en en O's binnen het speelveld plaatsen van de 6 bij 6 rooster.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 210))  # Aangepaste y-coördinaat
        paragraph3_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph3_text, paragraph3_rect)
        
        # Teken derde extra tekst (alinea 3)
        paragraph3_text = self.font.render("Hoe je speelt.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 290))  # Aangepaste y-coördinaat
        paragraph3_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph3_text, paragraph3_rect)
        
        # Teken derde extra tekst (alinea 3)
        paragraph3_text = self.font.render("Normaal gesproken speel je tegen een AI.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 330))  # Aangepaste y-coördinaat
        paragraph3_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph3_text, paragraph3_rect)
        
        # Teken derde extra tekst (alinea 3)
        paragraph3_text = self.font.render("Maar voor nu moet je met iemand anders samen spelen.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 360))  # Aangepaste y-coördinaat
        paragraph3_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph3_text, paragraph3_rect)
        
        # Teken derde extra tekst (alinea 3)
        paragraph3_text = self.font.render("Het idee is dus dat je om de beurt speelt.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 390))  # Aangepaste y-coördinaat
        paragraph3_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph3_text, paragraph3_rect)
        
        # Teken derde extra tekst (alinea 3)
        paragraph3_text = self.font.render("Jullie spelen allebei op dezelfde computer, waarbij X altijd begint en O kies nu wie begint als welke.", True, (0, 0, 0))
        paragraph3_rect = paragraph3_text.get_rect(center=(window_size[0] // 2, 420))  # Aangepaste y-coördinaat
        paragraph3_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph3_text, paragraph3_rect)
        
        # Teken derde extra tekst (alinea 4)
        paragraph4_text = self.font.render("De bediening.", True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 500))  # Aangepaste y-coördinaat
        paragraph4_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph4_text, paragraph4_rect)
        
         # Teken derde extra tekst (alinea 4)
        paragraph4_text = self.font.render("Je kunt met linkermuisklik X'en en O's plaatsen.", True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 540))  # Aangepaste y-coördinaat
        paragraph4_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph4_text, paragraph4_rect)
        
        # Teken derde extra tekst (alinea 4)
        paragraph4_text = self.font.render("Wanneer het spel voorbij is, kun je op ESC klikken om af te sluiten.", True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 570)) 
        # Aangepaste y-coördinaat
        paragraph4_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph4_text, paragraph4_rect) 
        
        # Teken derde extra tekst (alinea 4)
        paragraph4_text = self.font.render("Je kunt ook linkermuisknop drukken op de swirl rechtsboven na een spel om opnieuw te beginnen.", True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 600))  # Aangepaste y-coördinaat
        paragraph4_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph4_text, paragraph4_rect) 
        
        # Teken derde extra tekst (alinea 4)
        paragraph4_text = self.font.render("Als je alles begrijpt, kun je rechtsboven op het kruisje klikken en beginnen.", True, (0, 0, 0))
        paragraph4_rect = paragraph4_text.get_rect(center=(window_size[0] // 2, 730))  # Aangepaste y-coördinaat
        paragraph4_rect.centerx = window_size[0] // 2  # Horizontaal centreren
        screen.blit(paragraph4_text, paragraph4_rect) 
        
        # Teken afsluitknop
        screen.blit(self.button_img, self.button_rect)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    return True  # Transition to main game screen
        return False

class TicTacToe:
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
     for i in range(7):  # Changed range to 7 to include the last line
        pygame.draw.line(screen, self.table_color, (self.grid_offset_x + self.cell_size * i, self.grid_offset_y),
                         (self.grid_offset_x + self.cell_size * i, self.grid_offset_y + self.table_size), self.cell_size // 8)  # Vertical lines
        pygame.draw.line(screen, self.table_color, (self.grid_offset_x, self.grid_offset_y + self.cell_size * i),
                         (self.grid_offset_x + self.table_size, self.grid_offset_y + self.cell_size * i), self.cell_size // 8)  # Horizontal lines

    def _change_player(self):
        self.player = "O" if self.player == "X" else "X"

    def _move(self, pos):
        try:
            # Calculate the grid indices where the user clicked
            grid_x = (pos[0] - self.grid_offset_x) // self.cell_size
            grid_y = (pos[1] - self.grid_offset_y) // self.cell_size
            
            # Ensure the click is within the grid boundaries
            if 0 <= grid_x < 6 and 0 <= grid_y < 6:
                # Ensure the cell is empty before placing X or O
                if self.table[grid_x][grid_y] == "-":
                    self.table[grid_x][grid_y] = self.player
                    self._draw_char(grid_x, grid_y, self.player)
                    self._game_check()
                    self._change_player()
        except IndexError:
            print("Click inside the table only")

    def _draw_char(self, x, y, player):
        if player == "O":
            img = pygame.image.load("images/Tc-O.png")
        elif player == "X":
            img = pygame.image.load("images/Tc-X.png")
        img = pygame.transform.scale(img, (self.cell_size - self.table_space, self.cell_size - self.table_space))
        screen.blit(img, (self.grid_offset_x + x * self.cell_size + self.table_space // 2, 
                          self.grid_offset_y + y * self.cell_size + self.table_space // 2))

    def _message(self):
        message = ""
        if self.winner is not None:
            message = f'{self.winner} heeft gewonnen!!'
        elif not self.taking_move:
            message = 'GELIJKSPEL!!'
        else:
            message = f'{self.player} kan nu iets plaatsen in de grid.'

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
            for j in range(3):  # Adjusted to check for 4 in a row
                # Vertical check
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i][j + 1] == self.table[i][j + 2] == self.table[i][j + 3]:
                    self._pattern_strike((i, j), (i, j
                                                  + 3))
                    self.winner = self.player
                    self.taking_move = False
                    return
                # Horizontal check
                if self.table[j][i] != "-" and self.table[j][i] == self.table[j + 1][i] == self.table[j + 2][i] == self.table[j + 3][i]:
                    self._pattern_strike((j, i), (j + 3, i))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Left diagonal check
        for i in range(3):  # Adjusted to check for 4 in a row
            for j in range(3):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i + 1][j + 1] == self.table[i + 2][j + 2] == self.table[i + 3][j + 3]:
                    self._pattern_strike((i, j), (i + 3, j + 3))
                    self.winner = self.player
                    self.taking_move = False
                    return
        # Right diagonal check
        for i in range(3):  # Adjusted to check for 4 in a row
            for j in range(3, 6):
                if self.table[i][j] != "-" and self.table[i][j] == self.table[i + 1][j - 1] == self.table[i + 2][j - 2] == self.table[i + 3][j - 3]:
                    self._pattern_strike((i, j), (i + 3, j - 3))
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
    start_screen = StartScreen()
    while True:
        if start_screen.handle_events():
            break  # Exit the loop and start the game
        start_screen.show()

    g = TicTacToe(window_size[0])
    g.main()

