import pygame,sys
from classes import start_screen,screen_handler

pygame.init()

window_surface = pygame.display.set_mode((500,500))
pygame.display.set_caption("Sudoku")


screen_manager = screen_handler.ScreenHandler(window_surface)

screen_manager.set_screen(start_screen.StartScreen(screen_manager,window_surface))

while True:
    current_screen = screen_manager.get_current_screen()
    current_screen.tick()
    pygame.display.update()

    for event in pygame.event.get():
        current_screen.process_event(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

