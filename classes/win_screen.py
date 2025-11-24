import pygame
from pygame.event import Event
from .screen import Screen
from .button import Button
import sys

class WinScreen(Screen):
    def __init__(self, screen_manager, surface):
        super().__init__(screen_manager,surface)
    def start(self):
        surface = self.main_surface

        title_font = pygame.font.SysFont("Arial",30)
        title_surface = title_font.render("You win!",True,(255,255,255))

        title_rect = title_surface.get_rect()
        title_rect.center = (250,100)

        def stop():
            sys.exit()

        buttons:list[Button] = [
            Button((250,250),"Exit",lambda: stop()),
        ]

        for button in buttons:
            button.draw(surface)
            self.add_event_listener(button._process_event)

        surface.blit(title_surface,title_rect)

    def process_event(self, event: Event):
        return super().process_event(event)
    def tick(self):
        pass