import math,random, pygame, sys

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

    row_length = 9
    removed_cells = 30
    board = []
    box_length = math.sqrt(row_length)


    def __init__(self, removed_cells, row_length = 9):
        self.row_length = row_length
        self.removed_cells = removed_cells

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        pass

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        pass

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        pass

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        pass

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
        pass
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        pass

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        pass
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        pass

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
        pass

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

# def homeScreen():



if __name__ == "__main__":

    #Initialize pygame features
    pygame.init()
    pygame.font.init()

    #Screen dimensions
    screenWidth = 540
    screenHeight = screenWidth

    #Creates home screen
    homeScreen = pygame.display.set_mode((screenWidth, screenHeight))

    #Welcome message
    welcomeFont = pygame.font.SysFont("Arial", 70)
    welcomeSurface = welcomeFont.render("Welcome to Sudoku!", True, (0, 0, 0))
    welcomeRect = welcomeSurface.get_rect()
    welcomeRect.center = (screenWidth // 2, screenHeight // 8)

    #Select game mode message
    selectFont = pygame.font.SysFont("Arial", 40)
    selectSurface = selectFont.render("Select Game Mode:", True, (0, 0, 0))
    selectRect = selectSurface.get_rect()
    selectRect.center = (screenWidth // 2, screenHeight // 2)

    #Font , location, and dimensions for all the buttons on home screen
    buttonFont = selectFont = pygame.font.SysFont("Arial", 40)

    #Easy button
    easyButton = pygame.Rect(screenWidth//8, screenHeight// 1.5, 80, 60)
    easySurface = buttonFont.render("Easy", True, (0, 0, 0))
    easyRect = easySurface.get_rect()
    easyRect.center = (screenWidth//8, screenHeight// 1.5)

    #Medium button
    mediumButton = pygame.Rect(screenWidth//3, screenHeight// 1.5, 120, 60)
    mediumSurface = buttonFont.render("Medium", True, (0, 0, 0))
    mediumRect = mediumSurface.get_rect()
    mediumRect.center = (screenWidth // 3, screenHeight // 1.5)

    #Hard button
    hardButton = pygame.Rect(screenWidth // 1.6, screenHeight // 1.5, 80, 60)
    hardSurface = buttonFont.render("Hard", True, (0, 0, 0))
    hardRect = hardSurface.get_rect()
    hardRect.center = (screenWidth // 1.6, screenHeight // 1.5)




    clock = pygame.time.Clock()
    runningHome = True

    while runningHome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                clickLocation = event.pos

                if easyButton.collidepoint(clickLocation):
                    gameDifficulty = "Easy"
                    runningHome = False

                elif mediumButton.collidepoint(clickLocation):
                    gameDifficulty = "Medium"
                    runningHome = False

                elif hardButton.collidepoint(clickLocation):
                    gameDifficulty = "Hard"
                    runningHome = False

        #Makes all white home screen with 2 basic messages
        homeScreen.fill("white")
        homeScreen.blit(welcomeSurface, welcomeRect)
        homeScreen.blit(selectSurface, selectRect)

        #Display easy button
        pygame.draw.rect(homeScreen, "orange", easyButton)
        homeScreen.blit(easySurface, easyRect.center)

        #Display medium button
        pygame.draw.rect(homeScreen, "orange", mediumButton)
        homeScreen.blit(mediumSurface, mediumRect.center)

        #Display hard button
        pygame.draw.rect(homeScreen, "orange", hardButton)
        homeScreen.blit(hardSurface, hardRect.center)


        pygame.display.flip()
        clock.tick(60)

    gameScreen = pygame.display.set_mode((screenWidth, screenHeight))
    gameRunning = True

