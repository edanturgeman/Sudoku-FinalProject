import pygame
from pygame.event import Event
from .screen import Screen
from .button import Button

class StartScreen(Screen):
    def __init__(self, screen_manager, surface):
        super().__init__(screen_manager,surface)
    def start(self):
        surface = self.main_surface

        title_font = pygame.font.SysFont("Arial",30)
        title_surface = title_font.render("Welcome to Sudoku!",True,(255,255,255))

        header_font = pygame.font.SysFont("Arial",20)
        header_surface = header_font.render("Select Game Mode:",True,(255,255,255))

        title_rect = title_surface.get_rect()
        header_rect = header_surface.get_rect()
        title_rect.center = (250,100)
        header_rect.center = (250,200)

        def go_to_sudoku_screen(difficulty):
            sudoku_screen = self.screen_manager.make_screen("Sudoku")
            self.screen_manager.set_screen(sudoku_screen,difficulty)

        buttons:list[Button] = [
            Button((250,250),"Easy",lambda: go_to_sudoku_screen("Easy")),
            Button((250,300),"Normal",lambda: go_to_sudoku_screen("Normal")),
            Button((250,350),"Hard",lambda: go_to_sudoku_screen("Hard"))
        ]

        for button in buttons:
            button.draw(surface)
            self.add_event_listener(button._process_event)

        surface.blit(title_surface,title_rect)
        surface.blit(header_surface,header_rect)

    def process_event(self, event: Event):
        return super().process_event(event)
    def tick(self):
        pass