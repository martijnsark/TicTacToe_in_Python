import sys  
import pygame  
import numpy as np  
import random  
import copy  
  
# Set up constants  
WIDTH = 700  
HEIGHT = 600  
BACKGROUND_COLOUR = (247, 243, 234)  
ROWS = 6  
COLUMNS = 7  
SQUARE_SIZE = WIDTH // COLUMNS  
LINE_COLOUR = (82, 82, 75)  
LINE_WIDTH = 2  
OFFSET = 20  
X_COLOUR = (0, 210, 210)  
X_WIDTH = 10  
O_COLOUR = (255, 32, 143)  
O_WIDTH = 10  
RADIUS = SQUARE_SIZE // 3  
WIN_COLOR = (248, 254, 18)  
  
pygame.init()  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("4-IN-A-ROW")  
  
class Board:  
    def __init__(self):  
        self.squares = np.zeros((ROWS, COLUMNS))  
        self.marked_slots = 0  
  
    def final_state(self, show=False):  
        # Check all possible lines for four in a row  
        for c in range(COLUMNS-3):  
            for r in range(ROWS):  
                if self.squares[r][c] == self.squares[r][c+1] == self.squares[r][c+2] == self.squares[r][c+3] != 0:  
                    if show:  
                        pygame.draw.line(screen, WIN_COLOR,  
                                         ((c+0.5)*SQUARE_SIZE, (r+0.5)*SQUARE_SIZE),  
                                         ((c+3.5)*SQUARE_SIZE, (r+0.5)*SQUARE_SIZE), LINE_WIDTH)  
                    return self.squares[r][c]  
        for c in range(COLUMNS):  
            for r in range(ROWS-3):  
                if self.squares[r][c] == self.squares[r+1][c] == self.squares[r+2][c] == self.squares[r+3][c] != 0:  
                    if show:  
                        pygame.draw.line(screen, WIN_COLOR,  
                                         ((c+0.5)*SQUARE_SIZE, (r+0.5)*SQUARE_SIZE),  
                                         ((c+0.5)*SQUARE_SIZE, (r+3.5)*SQUARE_SIZE), LINE_WIDTH)  
                    return self.squares[r][c]  
        for c in range(COLUMNS-3):  
            for r in range(ROWS-3):  
                if self.squares[r][c] == self.squares[r+1][c+1] == self.squares[r+2][c+2] == self.squares[r +3][c+3] != 0:  
                    if show:  
                        pygame.draw.line(screen, WIN_COLOR,  
                                         ((c+0.5)*SQUARE_SIZE, (r+0.5)*SQUARE_SIZE),  
                                         ((c+3.5)*SQUARE_SIZE, (r+3.5)*SQUARE_SIZE), LINE_WIDTH)  
                    return self.squares[r][c]  
        for c in range(3, COLUMNS):  
            for r in range(ROWS-3):  
                if self.squares[r][c] == self.squares[r+1][c-1] == self.squares[r+2][c-2] == self.squares[r+3][c-3] != 0:  
                    if show:  
                        pygame.draw.line(screen, WIN_COLOR,  
                                         ((c+0.5)*SQUARE_SIZE, (r+0.5)*SQUARE_SIZE),  
                                         ((c-2.5)*SQUARE_SIZE, (r+3.5)*SQUARE_SIZE), LINE_WIDTH)  
                    return self.squares[r][c]  
        return 0  # no winner yet  
  
    def marking_square(self, row, column, player):  
        if self.squares[row][column] == 0:  
            self.squares[row][column] = player  
            self.marked_slots += 1  
            return True  
        return False  
  
    def get_empty_squares(self):  
        empty_square_list = []  
        for c in range(COLUMNS):  
            for r in range(ROWS):  
                if self.squares[r][c] == 0:  
                    empty_square_list.append((r, c))  
        return empty_square_list  
  
    def is_full(self):  
        return self.marked_slots == ROWS * COLUMNS  
    
class AI:  
    def __init__(self, level=1, player=2):  
        self.level = level  # 0 for random, 1 for minimax  
        self.player = player  # AI player number  
  
    def random_move(self, board):  
        empty_squares = board.get_empty_squares()  
        if empty_squares:  
            return random.choice(empty_squares)  
        return None  
  
    def minimax(self, board, depth, alpha, beta, maximizing_player):  
        if depth == 0 or board.final_state() or board.is_full():  
            if board.final_state() == self.player:  
                return (1000, None)  
            elif board.final_state() == 3 - self.player:  
                return (-1000, None)  
            else:  
                return (0, None)  
  
        if maximizing_player:  
            max_eval = float('-inf')  
            best_move = None  
            for row, col in board.get_empty_squares():  
                board.marking_square(row, col, self.player)  
                eval = self.minimax(board, depth - 1, alpha, beta, False)[0]  
                board.squares[row][col] = 0  # undo the move  
                if eval > max_eval:  
                    max_eval = eval  
                    best_move = (row, col)  
                alpha = max(alpha, eval)  
                if beta <= alpha:  
                    break  
            return max_eval, best_move  
        else:  
            min_eval = float('inf')  
            best_move = None  
            for row, col in board.get_empty_squares():  
                board.marking_square(row, col, 3 - self.player)  
                eval = self.minimax(board, depth - 1, alpha, beta, True)[0]  
                board.squares[row][col] = 0  # undo the move  
                if eval < min_eval:  
                    min_eval = eval  
                    best_move = (row, col)  
                beta = min(beta, eval)  
                if beta <= alpha:  
                    break  
            return min_eval, best_move  
  
    def choose_move(self, board):  
        if self.level == 0:  
            return self.random_move(board)  
        else:  
            _, move = self.minimax(board, 4, float('-inf'), float('inf'), True)  # depth set to 4 for performance  
            return move  
   
  
class Game:  
    def __init__(self):  
        self.board = Board()  
        self.player = 1  # 1 = X, 2 = O  
        self.running = True  
        self.draw_board()  
  
    def draw_board(self):  
        screen.fill(BACKGROUND_COLOUR)  
        for c in range(COLUMNS):  
            for r in range(ROWS):  
                pygame.draw.rect(screen, LINE_COLOUR,  
                                 (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)  
  
    def draw_figure(self, row, column):  
        center = (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)  
        if self.player == 1:  
            pygame.draw.line(screen, X_COLOUR,  
                             (center[0] - OFFSET, center[1] - OFFSET),  
                             (center[0] + OFFSET, center[1] + OFFSET), X_WIDTH)  
            pygame.draw.line(screen, X_COLOUR,  
                             (center[0] + OFFSET, center[1] - OFFSET),  
                             (center[0] - OFFSET, center[1] + OFFSET), X_WIDTH)  
        elif self.player == 2:  
            pygame.draw.circle(screen, O_COLOUR, center, RADIUS, O_WIDTH)  
  
    def switch_player(self):  
        self.player = 3 - self.player  
  
    def make_move(self, row, column):  
        if self.board.marking_square(row, column, self.player):  
            self.draw_figure(row, column)  
            if self.board.final_state(show=True) or self.board.is_full():  
                self.running = False  
            self.switch_player()  

def main():  
    pygame.init()  
    game = Game()  
    ai = AI(level=1, player=2)  # AI uses minimax and plays as O  
    clock = pygame.time.Clock()  
  
    while True:  
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                sys.exit()  
            elif event.type == pygame.MOUSEBUTTONDOWN and game.running and game.player == 1:  
                x, y = event.pos  
                column = x // SQUARE_SIZE  
                row = y // SQUARE_SIZE  
                if row < ROWS and column < COLUMNS:  
                    game.make_move(row, column)  
  
        if game.running and game.player == 2:  
            row, column = ai.choose_move(game.board)  
            if row is not None and column is not None:  
                game.make_move(row, column)  
  
        pygame.display.update()  
        clock.tick(20)  
  
main()  


