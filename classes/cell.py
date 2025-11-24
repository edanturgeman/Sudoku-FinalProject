import pygame


class Cell:
    def __init__(self,position,size,txt,fixed=False):
        self.position = position
        self.size = size

        self.selected = False
        
        self.sketched_text = ""
        self.central_text = str(txt)
        self.fixed = fixed

    def draw(self,surface):
        self.surface = surface
        color = "white"
        width = 1
        if self.selected:
            color = "red"
            width = 3
        self.cell_rect = pygame.draw.rect(surface, color, (self.position[0],self.position[1],self.size[0],self.size[1]),width)
        
        font = pygame.font.SysFont("Arial", 20)
        text_surface = font.render(self.central_text,True,"white")
        text_rect = text_surface.get_rect()
        text_rect.center = (self.position[0]+self.size[0]/2,self.position[1]+self.size[1]/2)

        sketched_font = pygame.font.SysFont("Arial", 15)
        sketched_text_surface = sketched_font.render(self.sketched_text,True,"grey")
        sketched_text_rect = text_surface.get_rect()
        sketched_text_rect.center = (self.position[0]+self.size[0]/4,self.position[1]+self.size[1]/4)

        surface.blit(text_surface,text_rect)
        surface.blit(sketched_text_surface,sketched_text_rect)

    def set_sketched_text(self,new_text):
        self.sketched_text = new_text

    def get_rect(self):
        return self.cell_rect
