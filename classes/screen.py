import pygame
from typing import Callable

class Screen:
    def __init__(self,screen_manager,main_surface):
        self.screen_manager = screen_manager
        self.main_surface:pygame.Surface = main_surface
        self.event_listeners:list[Callable[[pygame.event.Event]]] = []
    #Screen manager ensures that the main surface is cleared before invoking the start method
    def start(self,*args,**kwargs):
        pass
    def process_event(self,event:pygame.event.Event):
        for event_listener in self.event_listeners:
            event_listener(event)
    def tick(self):
        pass
    def add_event_listener(self,callable:Callable[[pygame.event.Event],None]):
        self.event_listeners.append(callable)
