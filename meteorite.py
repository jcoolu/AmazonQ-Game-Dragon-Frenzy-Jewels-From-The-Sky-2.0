"""
Meteorite class representing obstacles the player must avoid.
"""
import pygame

class Meteorite:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = speed
        self.color = (139, 69, 19)  # Brown
    
    def update(self):
        """Update meteorite position."""
        self.y += self.speed
    
    def draw(self, screen):
        """Draw the meteorite on the screen."""
        # Draw a simple meteorite (circle with some details)
        pygame.draw.circle(screen, self.color, 
                          (self.x + self.width // 2, self.y + self.height // 2), 
                          self.width // 2)
        
        # Add some crater details
        pygame.draw.circle(screen, (80, 40, 10), 
                          (self.x + self.width // 4, self.y + self.height // 4), 
                          self.width // 8)
        pygame.draw.circle(screen, (80, 40, 10), 
                          (self.x + 3 * self.width // 4, self.y + 3 * self.height // 4), 
                          self.width // 10)