#NOTE:   Rules:
""" 1. Any live cell with <2 neighbors dies (underpopulation)
    2. Any live cell with 2-3 neighbors lives
    3. Any live cell with >3 neighbors dies (overpopulation)
    4. Any dead cell with exactly 3 neighbors becomes alive (reproduction) """


import time 
import pygame 
import numpy as np 

color_bg = (10, 10, 10) 
color_grid = (40, 40, 40)
color_die_next = (170, 170, 170)        # Cell that will die
color_alive_next = (255, 255, 255)      # Living cell


def update(screen, cells, size, with_progress=False):
    #Updates the game based on conway's rules 
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

             # Loop through every cell in the grid
    for row, col in np.ndindex(cells.shape):
             # Count alive neighbors (3x3 area minus center cell)                             
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
             # Default color based on current state
        color = color_bg if cells[row, col] == 0 else color_alive_next

        #APPLY GAME RULES 
        if cells[row, col] == 1:              # Currently alive
            if alive < 2 or alive > 3:
                # Cell dies
                if with_progress:
                    color = color_die_next 

            elif 2 <= alive <= 3:
                # Cell survives
                updated_cells[row, col] = 1 
                if with_progress:
                    color = color_alive_next
        else:                                 # Currently dead
            if alive ==3:
                # Cell becomes alive (reproduction)
                updated_cells[row, col] = 1
                if with_progress:
                    color = color_alive_next
        #DRAW THE CELL 
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Create 60x80 grid (600x800 pixels, 10px per cell)
    cells = np.zeros((60,80))
    # Draw initial grid
    screen.fill(color_grid)
    update(screen, cells, 10)
    pygame.display.flip()

    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            # Handle quit
            if event.type == pygame.QUIT:
                return
            # Handle spacebar - toggle simulation
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running 
                    update(screen, cells, 10)
                    pygame.display.update()
            # Handle mouse click - add living cell    
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] =1
                update(screen,cells,10)
                pygame.display.update()
        # Draw grid
        screen.fill(color_grid)
        
        # Update simulation if running
        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        # Small delay to control speed
        time.sleep(0.001)
        
if __name__ == "__main__":
    main()
    
