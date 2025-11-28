import math, random, pygame, sys

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length



	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    # row_length = 9
    # removed_cells = 30
    # board = []
    # box_length = math.sqrt(row_length)

    def __init__(self, removed_cells, row_length):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.box_length = int((row_length) ** (1 / 2))

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        for row in self.board:
            print(' '.join([str(cell) for cell in row]))

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        return not (num in self.board[row])

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        column = []
        for row in self.board:
            column.append(row[col])
        return not (num in column)

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        all_values = []
        for row_index in range(row_start, row_start + 3):
            for column_index in range(col_start, col_start + 3):
                all_values.append(self.board[row_index][column_index])
        return not (num in all_values)

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        box_row, box_col = int(3 * (row // 3)), int(3 * (col // 3))
        return self.valid_in_box(box_row, box_col, num) and self.valid_in_col(int(col), num) and self.valid_in_row(
            int(row), num)

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        random_values = random.sample(range(1, 10), 9)
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                self.board[row][col] = random_values[3 * (row - row_start) + (col - col_start)]

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        positions = [(t % 9, t // 9) for t in random.sample(range(0, 81), self.removed_cells)]
        for pos in positions:
            pos_x, pos_y = pos
            self.board[pos_x][pos_y] = 0


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):

        # Horiontal Lines
        for i in range(1, 10):

            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (self.width, i * 60), 5)
            else:

                pygame.draw.line(self.screen, (0, 0, 0), (0, i * 60), (self.width, i * 60))

        # Vertical lines
        for i in range(1, 9):

            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, self.height - 60), 5)

            else:
                pygame.draw.line(self.screen, (0, 0, 0), (i * 60, 0), (i * 60, self.height - 60))


if __name__ == "__main__":

    # Initialize pygame features
    pygame.init()
    pygame.font.init()

    # Screen dimensions
    screenWidth, screenHeight = 540, 600

    # Creates home screen
    homeScreen = pygame.display.set_mode((screenWidth, screenHeight))

    # Welcome message
    welcomeFont = pygame.font.SysFont("Arial", 70)
    welcomeSurface = welcomeFont.render("Welcome to Sudoku!", True, (0, 0, 0))
    welcomeRect = welcomeSurface.get_rect()
    welcomeRect.center = (screenWidth // 2, screenHeight // 8)

    # Select game mode message
    selectFont = pygame.font.SysFont("Arial", 40)
    selectSurface = selectFont.render("Select Game Mode:", True, (0, 0, 0))
    selectRect = selectSurface.get_rect()
    selectRect.center = (screenWidth // 2, screenHeight // 2)

    # Font , location, and dimensions for all the buttons on home screen
    buttonFont = selectFont = pygame.font.SysFont("Arial", 40)

    # Easy button
    easyButton = pygame.Rect(screenWidth // 8, screenHeight // 1.5, 80, 60)
    easySurface = buttonFont.render("Easy", True, (0, 0, 0))
    easyRect = easySurface.get_rect()
    easyRect.center = (screenWidth // 8, screenHeight // 1.5)

    # Medium button
    mediumButton = pygame.Rect(screenWidth // 3, screenHeight // 1.5, 120, 60)
    mediumSurface = buttonFont.render("Medium", True, (0, 0, 0))
    mediumRect = mediumSurface.get_rect()
    mediumRect.center = (screenWidth // 3, screenHeight // 1.5)

    # Hard button
    hardButton = pygame.Rect(screenWidth // 1.6, screenHeight // 1.5, 80, 60)
    hardSurface = buttonFont.render("Hard", True, (0, 0, 0))
    hardRect = hardSurface.get_rect()
    hardRect.center = (screenWidth // 1.6, screenHeight // 1.5)

    clock = pygame.time.Clock()
    runningHome = True
    condition = True

    while condition:

        while runningHome:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    clickLocation = event.pos

                    if easyButton.collidepoint(clickLocation):
                        gameDifficulty = "Easy"
                        removedCells = 30
                        runningHome = False

                    elif mediumButton.collidepoint(clickLocation):
                        gameDifficulty = "Medium"
                        removedCells = 40
                        runningHome = False

                    elif hardButton.collidepoint(clickLocation):
                        gameDifficulty = "Hard"
                        removedCells = 50
                        runningHome = False

            # Makes all white home screen with 2 basic messages
            homeScreen.fill("white")
            homeScreen.blit(welcomeSurface, welcomeRect)
            homeScreen.blit(selectSurface, selectRect)

            # Display easy button
            pygame.draw.rect(homeScreen, "orange", easyButton)
            homeScreen.blit(easySurface, easyRect.center)

            # Display medium button
            pygame.draw.rect(homeScreen, "orange", mediumButton)
            homeScreen.blit(mediumSurface, mediumRect.center)

            # Display hard button
            pygame.draw.rect(homeScreen, "orange", hardButton)
            homeScreen.blit(hardSurface, hardRect.center)

            pygame.display.flip()
            clock.tick(60)

        # Reset button
        resetButton = pygame.Rect(screenWidth // 8, screenHeight - 50, 90, 50)
        resetSurface = buttonFont.render("Reset", True, (0, 0, 0))
        resetRect = resetSurface.get_rect()
        resetRect.center = (screenWidth // 8, screenHeight - 50)

        # Restart button
        restartButton = pygame.Rect(screenWidth // 3, screenHeight - 50, 110, 50)
        restartSurface = buttonFont.render("Restart", True, (0, 0, 0))
        restartRect = restartSurface.get_rect()
        restartRect.center = (screenWidth // 3, screenHeight - 50)

        # Exit button
        exitButton = pygame.Rect(screenWidth // 1.6, screenHeight - 50, 60, 50)
        exitSurface = buttonFont.render("Exit", True, (0, 0, 0))
        exitRect = exitSurface.get_rect()
        exitRect.center = (screenWidth // 1.6, screenHeight - 50)

        gameScreen = pygame.display.set_mode((screenWidth, screenHeight))
        gameRunning = True

        while gameRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    clickLocation = event.pos

                    if exitButton.collidepoint(clickLocation):
                        sys.exit()

                    if restartButton.collidepoint(clickLocation):
                        runningHome = True
                        gameRunning = False

            # Draws the board
            homeScreen.fill("white")
            board = Board(screenWidth, screenHeight, gameScreen, gameDifficulty)
            board.draw()

            # Displays the reset button
            pygame.draw.rect(gameScreen, "orange", resetButton)
            gameScreen.blit(resetSurface, resetRect.center)

            # Displays the restart button
            pygame.draw.rect(gameScreen, "orange", restartButton)
            gameScreen.blit(restartSurface, restartRect.center)

            # Displays the exit button
            pygame.draw.rect(gameScreen, "orange", exitButton)
            gameScreen.blit(exitSurface, exitRect.center)

            pygame.display.flip()
            clock.tick(60)




