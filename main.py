#!/usr/bin/env python3
"""
Dragon Frenzy: Jewels From The Sky
A side-scrolling game where you play as a purple dragon avoiding meteorites and collecting jewels.
"""
import pygame
import sys
from game import Game
from menu import Menu

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Dragon Frenzy: Jewels From The Sky"

def main():
    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    
    # Create game and menu instances
    game = Game(screen)
    menu = Menu(screen)
    
    # Game state
    game_state = "menu"  # "menu", "game", "game_over"
    
    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if game_state == "menu":
                action = menu.handle_events(event)
                if action == "start":
                    game_state = "game"
                    game.reset_game()  # Start a new game
                elif action == "howto":
                    menu.show_howto()
                elif action == "quit":
                    pygame.quit()
                    sys.exit()
            elif game_state == "game":
                game.handle_events(event)
                if game.game_over:
                    game_state = "game_over"
            elif game_state == "game_over":
                # Check for retry button click
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    game.retry_button['is_hovered'] = game.retry_button['rect'].collidepoint(mouse_pos)
                    
                    # Add menu button hover check
                    game.menu_button['is_hovered'] = game.menu_button['rect'].collidepoint(mouse_pos)
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if game.retry_button['rect'].collidepoint(mouse_pos):
                        game.reset_game()
                        game_state = "game"
                    elif game.menu_button['rect'].collidepoint(mouse_pos):
                        game_state = "menu"
        
        # Update and render based on game state
        if game_state == "menu":
            menu.render()
        elif game_state == "game":
            game.update()
            game.render()
        elif game_state == "game_over":
            game.render()  # This will show the game over screen with buttons
        
        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()