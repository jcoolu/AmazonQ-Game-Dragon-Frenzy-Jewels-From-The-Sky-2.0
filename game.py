"""
Game class that manages the main game logic.
"""
import pygame
import random
from dragon import Dragon
from meteorite import Meteorite
from jewel import Jewel
from scene import Scene

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        
        # Create scene manager
        self.scene = Scene()
        self.background_color = self.scene.get_background_color()
        
        # Create game objects
        self.dragon = Dragon(self.width // 2, self.height - 100)  # Position dragon at bottom center
        self.meteorites = []
        self.jewels = []
        
        # Game state
        self.score = 0
        self.game_over = False
        self.spawn_timer = 0
        self.font = pygame.font.SysFont(None, 36)
        
        # Retry button
        self.retry_button = {
            'rect': pygame.Rect(self.width // 2 - 160, self.height // 2 + 50, 150, 50),
            'color': (50, 200, 50),
            'hover_color': (100, 250, 100),
            'text': 'Retry',
            'is_hovered': False
        }
        
        # Menu button
        self.menu_button = {
            'rect': pygame.Rect(self.width // 2 + 10, self.height // 2 + 50, 150, 50),
            'color': (50, 150, 200),
            'hover_color': (100, 200, 250),
            'text': 'Main Menu',
            'is_hovered': False
        }
    
    def handle_events(self, event):
        """Handle input events."""
        if not self.game_over:
            self.dragon.handle_events(event)
    
    def update(self):
        """Update game state."""
        if self.game_over:
            return
            
        # Update scene based on score
        self.scene.update(self.score)
        self.scene.update_transition()
        self.background_color = self.scene.get_background_color()
            
        # Update dragon
        self.dragon.update()
        
        # Keep dragon within screen bounds
        if self.dragon.x < 0:
            self.dragon.x = 0
        elif self.dragon.x > self.width - self.dragon.width:
            self.dragon.x = self.width - self.dragon.width
        if self.dragon.y < 0:
            self.dragon.y = 0
        elif self.dragon.y > self.height - self.dragon.height:
            self.dragon.y = self.height - self.dragon.height
            
        # Spawn new objects
        self.spawn_timer += 1
        if self.spawn_timer >= 60:  # Every second (assuming 60 FPS)
            self.spawn_timer = 0
            
            # Spawn meteorite
            if random.random() < 0.7:  # 70% chance
                x = random.randint(0, self.width - 50)
                speed = random.randint(3, 7)
                self.meteorites.append(Meteorite(x, -40, speed))
            
            # Spawn jewel
            if random.random() < 0.4:  # 40% chance
                x = random.randint(0, self.width - 30)
                speed = random.randint(2, 5)
                self.jewels.append(Jewel(x, -30, speed))
        
        # Update meteorites
        for meteorite in self.meteorites[:]:
            meteorite.update()
            # Remove if off-screen
            if meteorite.y > self.height:
                self.meteorites.remove(meteorite)
            # Check collision with dragon
            elif self.check_collision(self.dragon, meteorite):
                self.game_over = True
        
        # Update jewels
        for jewel in self.jewels[:]:
            jewel.update()
            # Remove if off-screen
            if jewel.y > self.height:
                self.jewels.remove(jewel)
            # Check collision with dragon
            elif self.check_collision(self.dragon, jewel):
                self.jewels.remove(jewel)
                self.score += 10
    
    def render(self):
        """Render the game."""
        # Clear screen
        self.screen.fill(self.background_color)
        
        # Draw game objects
        self.dragon.draw(self.screen)
        
        for meteorite in self.meteorites:
            meteorite.draw(self.screen)
            
        for jewel in self.jewels:
            jewel.draw(self.screen)
            
        # Draw scene transition information
        self.scene.draw_scene_info(self.screen, self.font)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over message and buttons
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
            self.screen.blit(game_over_text, text_rect)
            
            # Draw final score
            score_final_text = self.font.render(f"Final Score: {self.score}", True, (0, 0, 0))
            score_rect = score_final_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(score_final_text, score_rect)
            
            # Draw retry button
            button_color = self.retry_button['hover_color'] if self.retry_button['is_hovered'] else self.retry_button['color']
            pygame.draw.rect(self.screen, button_color, self.retry_button['rect'], border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), self.retry_button['rect'], 2, border_radius=10)  # Border
            
            # Retry button text
            button_text = self.font.render(self.retry_button['text'], True, (0, 0, 0))
            text_rect = button_text.get_rect(center=self.retry_button['rect'].center)
            self.screen.blit(button_text, text_rect)
            
            # Draw menu button
            button_color = self.menu_button['hover_color'] if self.menu_button['is_hovered'] else self.menu_button['color']
            pygame.draw.rect(self.screen, button_color, self.menu_button['rect'], border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), self.menu_button['rect'], 2, border_radius=10)  # Border
            
            # Menu button text
            button_text = self.font.render(self.menu_button['text'], True, (0, 0, 0))
            text_rect = button_text.get_rect(center=self.menu_button['rect'].center)
            self.screen.blit(button_text, text_rect)
    
    def check_collision(self, obj1, obj2):
        """Check if two objects are colliding."""
        return (obj1.x < obj2.x + obj2.width and
                obj1.x + obj1.width > obj2.x and
                obj1.y < obj2.y + obj2.height and
                obj1.y + obj1.height > obj2.y)
                
    def reset_game(self):
        """Reset the game state to start a new game."""
        self.dragon = Dragon(self.width // 2, self.height - 100)  # Position dragon at bottom center
        self.meteorites = []
        self.jewels = []
        self.score = 0
        self.game_over = False
        self.spawn_timer = 0
        
        # Reset scene
        self.scene = Scene()
        self.background_color = self.scene.get_background_color()