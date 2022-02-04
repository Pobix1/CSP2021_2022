import pygame

class PLAYER:
    def __init__ (self, x, y, width, height, color=(255, 255, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color 

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 10
        if keys[pygame.K_RIGHT] and self.x < 1920 - self.width:
            self.x += 10
        if keys[pygame.K_DOWN] and self.y < 1080 - self.height:
            self.y += 10
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 10

    def draw(self, WIN):
        return pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))
   
class projectile():
    def __init__ (self, x, y, radius, color, facing):
        self.x = x
        self.y = y 
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing
    
    def draw(self, WIN):
        return pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)
        
    def reset(self):
        self.x = 100
        self.y = 100