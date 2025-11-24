import pygame
from pygame.event import Event
from .screen import Screen
from .button import Button
from .cell import Cell

import sudoku_generator
import copy
import sys


class SudokuScreen(Screen):
    def __init__(self, screen_manager, surface):
        super().__init__(screen_manager,surface)
    def start(self,difficulty):
        surface = self.main_surface

        to_remove = 0
        if difficulty == "Easy":
            to_remove = 30
        if difficulty == "Normal":
            to_remove = 40
        if difficulty == "Hard":
            to_remove = 50
        generated_board = sudoku_generator.generate_sudoku(9,to_remove)
        self.board = copy.deepcopy(generated_board)

        def reset_board():
            for cell in self.cells.values():
                if cell.fixed == False:
                    cell.central_text = ""
                    cell.sketched_text = ""
            self.board = copy.deepcopy(generated_board)
        def restart_game():
            sudoku_screen = self.screen_manager.make_screen("Start")
            self.screen_manager.set_screen(sudoku_screen)
        def exit():
            sys.exit()

        button_font = pygame.font.SysFont("Arial", 20)
        self.buttons:list[Button] = [
            Button((83,475),"Reset",reset_board,button_font ),
            Button((250,475),"Restart",restart_game,button_font ),
            Button((416,475),"Exit",exit,button_font )
        ]

        for button in self.buttons:
            button.draw(surface)
            self.event_listeners.append(button._process_event)
        self.cells = {}
        for x in range(0,9):
            for y in range(0,9):
                fixed = False
                txt = str(self.board[y][x])
                if txt == "0":
                    txt = ""
                else:
                    fixed = True
                cell = Cell((75+40*x,50+40*y),(40,40),txt,fixed)
                self.cells.update({(x,y):cell})
                cell.draw(surface)
        self.current_cell = None
        self.current_cell_pos = None

    def check_for_end_game(self):
        exists_empty_cell = False
        for row in self.board:
            for x in row:
                if x == 0:
                    exists_empty_cell = True
        if exists_empty_cell == False:
            def is_list_valid(lis):
                for i in range(1,10):
                    if i not in lis:
                        return False
                return True
            is_board_valid = True
            for row in self.board:
                if not is_list_valid(row):
                    is_board_valid = False
            for col in range(0,9):
                column = []
                for row in self.board:
                    column.append(row[col])
                if not is_list_valid(column):
                    is_board_valid = False
            for top_left_x in range(0,3):
                for top_left_y in range(0,3):
                    lis = []
                    for x in range(3*top_left_x,3*top_left_x+3):
                        for y in range(3*top_left_y,3*top_left_y+3):
                            lis.append(self.board[x][y])
                    if not is_list_valid(lis):
                        is_board_valid = False
            if is_board_valid == True:
                self.screen_manager.set_screen(self.screen_manager.make_screen("Win"))
            else:
                self.screen_manager.set_screen(self.screen_manager.make_screen("Lose"))
    def process_event(self, event: Event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN and self.current_cell_pos != None:
            if pygame.K_0 < event.key <= pygame.K_9:
                key_value = event.key - pygame.K_0
                if self.current_cell != None and not self.current_cell.fixed and self.current_cell.central_text == "":
                    self.current_cell.sketched_text = str(key_value)
            if event.key == pygame.K_RETURN:
                if self.current_cell != None and not self.current_cell.fixed and self.current_cell.sketched_text != "":
                    self.current_cell.central_text = self.current_cell.sketched_text
                    self.current_cell.sketched_text = ""
                    pos = self.current_cell_pos
                    assert self.board[pos[1]][pos[0]] == 0
                    self.board[pos[1]][pos[0]] = int(self.current_cell.central_text)
                    
                    self.check_for_end_game()


            new_pos = None
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                new_pos = (self.current_cell_pos[0],self.current_cell_pos[1]-1)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                new_pos = (self.current_cell_pos[0]+1,self.current_cell_pos[1])
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                new_pos = (self.current_cell_pos[0],self.current_cell_pos[1]+1)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                new_pos = (self.current_cell_pos[0]-1,self.current_cell_pos[1])
            if new_pos != None and (new_pos[0] >= 0 and new_pos[0] < 9) and (new_pos[1] >= 0 and new_pos[1] < 9):
                self.current_cell_pos = new_pos
                if self.current_cell != None:
                    self.current_cell.selected = False
                self.current_cell = self.cells.get(new_pos)
                
                assert self.current_cell != None

                self.current_cell.selected = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            for pos,cell in self.cells.items():
                if cell.cell_rect.collidepoint(event.pos):
                    if self.current_cell:
                        self.current_cell.selected = False
                    if self.current_cell != cell:
                        self.current_cell = cell
                        self.current_cell_pos = pos
                        self.current_cell.selected = True

                    
    def tick(self):
        self.main_surface.fill((0,0,0))
        for cell in self.cells.values():
            cell.draw(self.main_surface)
        for button in self.buttons:
            button.draw(self.main_surface)
