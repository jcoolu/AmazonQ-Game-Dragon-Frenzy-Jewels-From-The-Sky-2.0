"""
Jewel class representing collectible items that increase the player's score.
"""
import pygame
import random

class Jewel:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.speed = speed
        
        # Random jewel color
        self.colors = [
            (255, 0, 0),    # Ruby (red)
            (0, 0, 255),    # Sapphire (blue)
            (0, 255, 0),    # Emerald (green)
            (255, 255, 0),  # Topaz (yellow)
            (255, 0, 255)   # Amethyst (purple)
        ]
        self.color = random.choice(self.colors)
    
    def update(self):
        """Update jewel position."""
        self.y += self.speed * 0.7  # Jewels fall slower than meteorites
    
    def draw(self, screen):
        """Draw the jewel on the screen."""
        # Draw a diamond shape
        points = [
            (self.x + self.width // 2, self.y),
            (self.x + self.width, self.y + self.height // 2),
            (self.x + self.width // 2, self.y + self.height),
            (self.x, self.y + self.height // 2)
        ]
        pygame.draw.polygon(screen, self.color, points)
        
        # Add a shine effect
        shine_points = [
            (self.x + self.width // 2, self.y + 5),
            (self.x + self.width - 5, self.y + self.height // 2),
            (self.x + self.width // 2, self.y + self.height - 5),
            (self.x + 5, self.y + self.height // 2)
        ]
        pygame.draw.polygon(screen, (255, 255, 255), shine_points)