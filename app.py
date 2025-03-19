from matrix import Matrix
import pygame
import threading

def display_matrix(matrix):
    pygame.init()

    ROWS, COLS = len(matrix), len(matrix[0])
    WIDTH, HEIGHT = 600, 400
    CELL_WIDTH = WIDTH // COLS
    CELL_HEIGHT = HEIGHT // ROWS

    COLORS = {
        0: (255, 255, 255),  # White
        1: (255, 165, 0),    # Orange
        2: (255, 165, 0),    # Orange
        3: (255, 255, 255),    # Yellow
        4: (139, 69, 19)     # Brown
    }

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Matrix Display")

    running = True
    while running:
        screen.fill((0, 0, 0)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(ROWS):
            for j in range(COLS):
                color = COLORS.get(matrix[i][j], (0, 0, 0)) 
                pygame.draw.rect(screen, color, (j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
                pygame.draw.rect(screen, (0, 0, 0), (j * CELL_WIDTH, i * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 1)  

        pygame.display.flip()
        pygame.time.delay(100)  

    pygame.quit()

inv_triangle = [(4,4), (4,5), (5,3), (5,4), (5,5), (5,6), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8)]
triangle = [(3,3), (3,4), (2,2), (2,3), (2,4), (2,5), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7)]
rectangle = [(3,0), (3,1), (3,2), (3,3), (3,4), (2,0), (2,1), (2,2), (2,3), (2,4), (1,0), (1,1), (1,2), (1,3), (1,4), (0,0), (0,1), (0,2), (0,3), (0,4)]
pillar = [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0), (3,1), (4,0), (4,1), (5,0), (5,1), (6,0), (6,1), (7,0), (7,1), (8,0), (8,1), (9,0), (9,1)]
cloud = [(4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8)]
square = [(0,0), (0,2), (0,3), (0,4), (0,7), (1,0), (1,2), (1,3), (1,4), (1,7), (2,0), (2,7), (3,0), (3,2), (3,3), (3,4), (3,5), (3,7), (3,1), (3,6)]

if __name__ == "__main__":
    rows = int(input("Number of rows: "))
    columns = int(input("Number of columns: "))
    mat = Matrix(rows, columns)
    display_matrix(mat.matrix)
    for row in mat.matrix:
        print(row)
    threading.Thread(target=mat.run_matrix, args=(triangle,)).start()
    display_matrix(mat.matrix)