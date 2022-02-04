import pygame
from Circle import CIRCLE
from Player import PLAYER
from Field import field

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#Colors
P = (255,255,255)
C = (153,50,204)
B = (216,191,216)
S = (0,255,0)

Start = 0
FPS = 60

pygame.mixer.init()
DS1 = pygame.mixer.music.load("Pac-Man Death - Sound Effect (HD).mp3")
DS2 = pygame.mixer.music.load("Metal Gear Solid - Snake death scream sound effect.mp3")
DS3 = pygame.mixer.music.load("Lego yoda death sound.mp3")
sound_list = [DS1, DS2, DS3]


player = PLAYER(100, 100, 50, 50, (P))
fieldStart = field(75,75,100,100)
fieldFinish = field(900,900,100,100)
circle = CIRCLE(960, 200, 12, 12, 25, (C))
circle2 = CIRCLE(1000, 250, 12, 12, 35, (C))
circle3 = CIRCLE(1040, 350, 12, 12, 45, (C))
circle4 = CIRCLE(1080, 450, 12, 12, 55, (C))

enemy = [circle.draw(WIN), circle2.draw(WIN), circle3.draw(WIN), circle4.draw(WIN)]

def draw_window():
    WIN.fill(B)
    fieldStart.draw(WIN)
    fieldFinish.draw(WIN)
    player.draw(WIN)
    circle.draw(WIN)
    circle2.draw(WIN)
    circle3.draw(WIN)
    circle4.draw(WIN)
    pygame.display.update()

def update():
    global sound_list
    keys = pygame.key.get_pressed()
    player.move(keys)
    circle.move(0,1920)
    circle2.move(0,1920)
    circle3.move(0,1920)
    circle4.move(0,1920)
    if player.draw(WIN).collidelist([fieldFinish.draw(WIN)]) != -1:
        print("Finished")
    if player.draw(WIN).collidelist(enemy) != -1:
        if sound_list > 0:
            current_sound = sound_list[0]
            current_sound.play()
            sound_list.pop(0)  

        else:
            sound_list = [DS1, DS2, DS3]
            current_sound = sound_list[0]
            current_sound.play()
            sound_list.pop(0)
            
        
        player.reset()
    draw_window()


#Game Loop
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.fill((202, 228, 241))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        
        if player.draw(WIN).collidelist([circle.draw(WIN)]) !=-1:
            print ("collision detected")

        update()

    pygame.quit()

if __name__ == "__main__":
    main()