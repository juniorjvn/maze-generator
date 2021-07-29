from tkinter import *
import time
import random
from maze import init_maze, get_neighbors

BLOCKS = 25
BLOCK_SIZE = 10
TOTAL_BLOCKS = BLOCKS * 2 + 1
SPEED = 0.0005

WIDTH = BLOCK_SIZE * TOTAL_BLOCKS
HEIGHT = WIDTH


def draw_maze(canvas, maze):

    for i in range(TOTAL_BLOCKS):
        for j in range(TOTAL_BLOCKS):
            x = j * BLOCK_SIZE
            y = i * BLOCK_SIZE
            color = ""
            if maze[i][j]:
                color = 'black'
            else:
                color = 'white'
            canvas.create_rectangle(x, y, x+BLOCK_SIZE, y+BLOCK_SIZE, fill=color, outline=color)


start = time.perf_counter()
WIN = Tk()
canvas = Canvas(WIN, width=WIDTH, height=HEIGHT)
canvas.pack()

maze = init_maze(BLOCKS)
draw_maze(canvas, maze)
WIN.update()
time.sleep(SPEED)

start_point = (1, 1)
frontier_stack = [[start_point, start_point]]
explored = []

while frontier_stack:
    # current_cell position tuple (x, y)
    current_cell = frontier_stack.pop()
    temp_stack = [item[1] for item in frontier_stack]
    explored.append(current_cell[1])

    # clear path
    # cell to remove
    pos = current_cell[0]
    x = pos[1] * BLOCK_SIZE
    y = pos[0] * BLOCK_SIZE
    maze[pos[0]][pos[1]] = False
    canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill='#00AD40', outline='#00AD40')

    pos = current_cell[1]
    x = pos[1] * BLOCK_SIZE
    y = pos[0] * BLOCK_SIZE
    maze[pos[0]][pos[1]] = False
    canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill='#00AD40', outline='#00AD40')

    WIN.update()
    time.sleep(SPEED)

    all_neighbors = get_neighbors(current_cell[1], BLOCKS)
    neighbors = [neighbor for neighbor in all_neighbors
                 if neighbor[1] not in explored and neighbor[1] not in temp_stack]

    if neighbors:
        random.shuffle(neighbors)
        frontier_stack.extend(neighbors)
end = time.perf_counter()
print('finish in', round(end - start, 2), 'second')

WIN.mainloop()

