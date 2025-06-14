"""
Dragon class representing the player character.
"""
import pygame

class Dragon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 60
        self.speed = 5
        self.color = (128, 0, 128)  # Purple
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    
    def handle_events(self, event):
        """Handle keyboard input."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.moving_down = True
            elif event.key == pygame.K_LEFT:
                self.moving_left = True
            elif event.key == pygame.K_RIGHT:
                self.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.moving_down = False
            elif event.key == pygame.K_LEFT:
                self.moving_left = False
            elif event.key == pygame.K_RIGHT:
                self.moving_right = False
    
    def update(self):
        """Update dragon position."""
        if self.moving_up:
            self.y -= self.speed
        if self.moving_down:
            self.y += self.speed
        if self.moving_left:
            self.x -= self.speed
        if self.moving_right:
            self.x += self.speed
    
    def draw(self, screen):
        """Draw the dragon on the screen."""
        # Simple dragon shape (oval body with wings)
        pygame.draw.ellipse(screen, self.color, 
                           pygame.Rect(self.x, self.y, self.width, self.height))
        
        # Wings
        wing_left = [
            (self.x + 10, self.y + self.height // 2),
            (self.x - 15, self.y + 10),
            (self.x - 5, self.y + self.height - 10)
        ]
        wing_right = [
            (self.x + self.width - 10, self.y + self.height // 2),
            (self.x + self.width + 15, self.y + 10),
            (self.x + self.width + 5, self.y + self.height - 10)
        ]
        pygame.draw.polygon(screen, self.color, wing_left)
        pygame.draw.polygon(screen, self.color, wing_right)
        
        # Eyes
        pygame.draw.circle(screen, (255, 255, 255), 
                          (self.x + 20, self.y + 20), 5)
        pygame.draw.circle(screen, (255, 255, 255), 
                          (self.x + self.width - 20, self.y + 20), 5)