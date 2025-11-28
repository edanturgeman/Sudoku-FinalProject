from .lose_screen import LoseScreen
from .win_screen import WinScreen
from .start_screen import StartScreen
from .sudoku_screen import SudokuScreen

class ScreenHandler:
    def __init__(self,window_surface):
        self.window_surface = window_surface
    def make_screen(self,screen_name):
        mapping = {
            "Lose" : LoseScreen(self,self.window_surface),
            "Win" : WinScreen(self,self.window_surface),
            "Start" : StartScreen(self,self.window_surface),
            "Sudoku" : SudokuScreen(self,self.window_surface),
            
        }
        return mapping[screen_name]
    def set_screen(self,screen,*args,**kwargs):
        self.current = screen
        self.window_surface.fill((0,0,0))
        screen.start(*args,**kwargs)
    def get_current_screen(self):
        return self.current
    