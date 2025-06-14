"""
Scene class for managing different game backgrounds based on score.
"""
import pygame

class Scene:
    def __init__(self):
        # Define scenes with their score thresholds and colors
        self.scenes = [
            {
                'name': 'Sky',
                'threshold': 0,
                'background': (135, 206, 235),  # Sky blue
                'description': 'Flying through the open sky'
            },
            {
                'name': 'Forest',
                'threshold': 50,
                'background': (34, 139, 34),  # Forest green
                'description': 'Soaring above the ancient forest'
            },
            {
                'name': 'Ice Kingdom',
                'threshold': 100,
                'background': (176, 224, 230),  # Powder blue
                'description': 'Braving the frozen ice kingdom'
            },
            {
                'name': 'Volcano',
                'threshold': 150,
                'background': (178, 34, 34),  # Firebrick red
                'description': 'Navigating the dangerous volcano'
            },
            {
                'name': 'Castle',
                'threshold': 200,
                'background': (72, 61, 139),  # Dark slate blue
                'description': 'Approaching the mystical castle'
            }
        ]
        
        # Current scene index
        self.current_scene = 0
        
        # Transition effect
        self.transition_active = False
        self.transition_progress = 0
        self.transition_speed = 5  # Higher is faster
        
    def get_current_scene(self):
        """Get the current scene data."""
        return self.scenes[self.current_scene]
    
    def update(self, score):
        """Update the scene based on player score."""
        # Check if we need to change scenes
        for i, scene in enumerate(self.scenes):
            if score >= scene['threshold'] and i > self.current_scene:
                self.transition_active = True
                self.transition_progress = 0
                self.current_scene = i
                break
    
    def get_background_color(self):
        """Get the current background color, considering transitions."""
        if not self.transition_active:
            return self.scenes[self.current_scene]['background']
        
        # During transition, blend colors
        current_color = self.scenes[self.current_scene]['background']
        
        # If transitioning from the first scene, just return current color
        if self.current_scene == 0:
            self.transition_active = False
            return current_color
        
        prev_color = self.scenes[self.current_scene - 1]['background']
        
        # Calculate blend based on transition progress (0-100)
        blend_ratio = self.transition_progress / 100
        
        # Blend the colors
        blended_color = [
            int(prev_color[i] * (1 - blend_ratio) + current_color[i] * blend_ratio)
            for i in range(3)
        ]
        
        return tuple(blended_color)
    
    def update_transition(self):
        """Update transition effect."""
        if self.transition_active:
            self.transition_progress += self.transition_speed
            if self.transition_progress >= 100:
                self.transition_active = False
                self.transition_progress = 100
    
    def draw_scene_info(self, screen, font):
        """Draw scene name when transitioning."""
        # This method is now empty as we've removed the scene announcements
        pass