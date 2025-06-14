"""
Menu class for the game.
"""
import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.background_color = (135, 206, 235)  # Sky blue
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 32)
        
        # Game title
        self.title = "Dragon Frenzy: Jewels From The Sky"
        
        # Menu buttons
        button_width = 250
        button_height = 60
        button_x = self.width // 2 - button_width // 2
        button_y_start = self.height // 2 - 50
        button_spacing = 80
        
        self.buttons = [
            {
                'rect': pygame.Rect(button_x, button_y_start, button_width, button_height),
                'color': (50, 200, 50),
                'hover_color': (100, 250, 100),
                'text': 'Start Game',
                'is_hovered': False,
                'action': 'start'
            },
            {
                'rect': pygame.Rect(button_x, button_y_start + button_spacing, button_width, button_height),
                'color': (50, 150, 200),
                'hover_color': (100, 200, 250),
                'text': 'How to Play',
                'is_hovered': False,
                'action': 'howto'
            },
            {
                'rect': pygame.Rect(button_x, button_y_start + button_spacing * 2, button_width, button_height),
                'color': (200, 50, 50),
                'hover_color': (250, 100, 100),
                'text': 'Quit Game',
                'is_hovered': False,
                'action': 'quit'
            }
        ]
        
        # Current view
        self.current_view = 'menu'  # 'menu', 'howto'
        
        # How to play text
        self.howto_text = [
            "How to Play",
            "",
            "- Use arrow keys to move the dragon in all directions",
            "- Collect falling jewels to earn points",
            "- Avoid meteorites falling from above",
            "- Try to get the highest score!"
        ]
        
        # Settings options
        self.settings = {
            'difficulty': 'Normal'  # Placeholder for settings
        }
        
        # Back button for sub-menus
        self.back_button = {
            'rect': pygame.Rect(50, self.height - 80, 120, 50),
            'color': (150, 150, 150),
            'hover_color': (200, 200, 200),
            'text': 'Back',
            'is_hovered': False
        }
    
    def handle_events(self, event):
        """Handle menu input events."""
        if event.type == pygame.MOUSEMOTION:
            # Check if mouse is over buttons
            mouse_pos = pygame.mouse.get_pos()
            
            # Main menu buttons
            if self.current_view == 'menu':
                for button in self.buttons:
                    button['is_hovered'] = button['rect'].collidepoint(mouse_pos)
            
            # Back button for sub-menus
            elif self.current_view == 'howto':
                self.back_button['is_hovered'] = self.back_button['rect'].collidepoint(mouse_pos)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # Main menu buttons
            if self.current_view == 'menu':
                for button in self.buttons:
                    if button['rect'].collidepoint(mouse_pos):
                        return button['action']
            
            # Back button for sub-menus
            elif self.current_view == 'howto':
                if self.back_button['rect'].collidepoint(mouse_pos):
                    self.current_view = 'menu'
        
        return None
    
    def render(self):
        """Render the menu."""
        # Clear screen
        self.screen.fill(self.background_color)
        
        # Draw title
        title_text = self.font.render(self.title, True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(self.width // 2, 100))
        self.screen.blit(title_text, title_rect)
        
        # Draw current view
        if self.current_view == 'menu':
            self._render_main_menu()
        elif self.current_view == 'howto':
            self._render_howto()
    
    def _render_main_menu(self):
        """Render the main menu buttons."""
        for button in self.buttons:
            # Draw button
            button_color = button['hover_color'] if button['is_hovered'] else button['color']
            pygame.draw.rect(self.screen, button_color, button['rect'], border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), button['rect'], 2, border_radius=10)  # Border
            
            # Button text
            button_text = self.small_font.render(button['text'], True, (0, 0, 0))
            text_rect = button_text.get_rect(center=button['rect'].center)
            self.screen.blit(button_text, text_rect)
    
    def _render_howto(self):
        """Render the how to play screen."""
        y_pos = 180
        line_spacing = 40
        
        for line in self.howto_text:
            if line == self.howto_text[0]:  # Title
                text = self.font.render(line, True, (0, 0, 0))
            else:
                text = self.small_font.render(line, True, (0, 0, 0))
            
            text_rect = text.get_rect(center=(self.width // 2, y_pos))
            self.screen.blit(text, text_rect)
            y_pos += line_spacing
        
        # Draw back button
        self._render_back_button()
    
    def _render_settings(self):
        """Render the settings screen."""
        # Title
        title_text = self.font.render("Settings", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(self.width // 2, 180))
        self.screen.blit(title_text, title_rect)
        
        # Difficulty setting
        diff_text = self.small_font.render(f"Difficulty: {self.settings['difficulty']}", True, (0, 0, 0))
        diff_rect = diff_text.get_rect(center=(self.width // 2, 250))
        self.screen.blit(diff_text, diff_rect)
        
        # Draw back button
        self._render_back_button()
    
    def _render_back_button(self):
        """Render the back button for sub-menus."""
        button_color = self.back_button['hover_color'] if self.back_button['is_hovered'] else self.back_button['color']
        pygame.draw.rect(self.screen, button_color, self.back_button['rect'], border_radius=10)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_button['rect'], 2, border_radius=10)  # Border
        
        # Button text
        button_text = self.small_font.render(self.back_button['text'], True, (0, 0, 0))
        text_rect = button_text.get_rect(center=self.back_button['rect'].center)
        self.screen.blit(button_text, text_rect)
    
    def show_howto(self):
        """Show the how to play screen."""
        self.current_view = 'howto'
    
    def show_settings(self):
        """Show the settings screen."""
        self.current_view = 'settings'