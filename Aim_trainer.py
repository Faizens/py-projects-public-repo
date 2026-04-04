import pygame
import random 
import time
import math

pygame.init()

width, height = 800, 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aim Trainer")

target_increment = 400
target_event = pygame.USEREVENT

target_padding = 30

bg_color = (0, 25, 40)

lives = 3

top_bar_height = 50

label_font = pygame.font.SysFont("comicsans", 24)

class Target():
    max_size = 30 
    growth_rate = 0.2 
    color = "red"
    sec_color = "white"
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True 
    def update(self):
        if self.size + self.growth_rate >= self.max_size:
            self.grow = False

        if self.grow:
            self.size += self.growth_rate
        
        else:
            self.size -= self.growth_rate

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.sec_color, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.sec_color, (self.x, self.y), self.size * 0.4)
    
    def collide(self, x, y):
       dis = math.sqrt((x - self.x)**2 + (y - self.y)**2)
       return dis <= self.size

def draw(win, targets):
    win.fill(bg_color)

    for target in targets:
        target.draw(win)


def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}{seconds:02d}.{milli}"

def draw_top_bar(win, elapsed_time, target_pressed, misses):
    pygame.draw.rect(win, "grey", (0, 0, width, top_bar_height))
    time_label = label_font.render(
        f"Time: {format_time(elapsed_time)}", 1, 'black')

    win.blit(time_label, (5, 5))

def main():
    run = True 

    targets = []

    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    pygame.time.set_timer(target_event, target_increment)

    while run:
        clock.tick(60)

        click = False 

        mouse_pos = pygame.mouse.get_pos()

        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == target_event:
                x = random.randint(target_padding, width - target_padding)
                y = random.randint(target_padding, height - target_padding)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_pos):
                targets.remove(target)
                target_pressed += 1

        if misses >= lives:
            pass # end the game
            
        draw(win, targets)
        draw_top_bar(win, elapsed_time, target_pressed, misses)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()