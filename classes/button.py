import pygame
from typing import Callable

class Button:
    def __init__(self,position,text,click_function,
                 font=None,
                 text_color=(255,255,255),
                 background_color="orange",
                 background_size=None):
        self.position = position
        self.text = text
        self.click_function:Callable = click_function
        
        if font == None: font = pygame.font.SysFont("Arial", 40)
        self.font = font

        self.text_color = text_color
        self.background_color = background_color
        self.background_size = None
    def draw(self,main_surface:pygame.Surface):
        text_surface = self.font.render(self.text,True,self.text_color)
        if self.background_size == None:
            self.background_size = (text_surface.get_width(),text_surface.get_height())

        background_rect = pygame.Rect(0,0,self.background_size[0],self.background_size[1])
        background_rect.center = (self.position[0],self.position[1])
        self.background_rect = background_rect

        text_rect = text_surface.get_rect()
        text_rect.center = self.position

        pygame.draw.rect(main_surface,self.background_color,background_rect)
        main_surface.blit(text_surface,text_rect)
    
    def _process_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.background_rect.collidepoint(event.pos):
                self.click_function()