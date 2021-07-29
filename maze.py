import random


def init_maze(size):
    cells = size * 2 + 1
    explored = []

    for i in range(cells):
        row = []
        for j in range(cells):
            if i % 2 == 1 and j % 2 == 1:
                row.append(False)
            else:
                row.append(True)
        explored.append(row)

    return explored


def get_neighbors(pos, size):
    cells = size * 2 + 1
    neighbors = []
    x = pos[0]
    y = pos[1]

    if x != 1:
        path = []
        path.append((x - 1, y))  # neighbor - up
        path.append((x - 2, y))  # neighbor - up
        neighbors.append(path)

    if x != cells - 2:
        path = []
        path.append((x + 1, y))  # neighbor - down
        path.append((x + 2, y))  # neighbor - down
        neighbors.append(path)
    if y != 1:
        path = []
        path.append((x, y - 1))  # neighbor - left
        path.append((x, y - 2))  # neighbor - left
        neighbors.append(path)
    if y != cells - 2:
        path = []
        path.append((x, y + 1))  # neighbor - right
        path.append((x, y + 2))  # neighbor - right
        neighbors.append(path)

    return neighbors


def draw_maze(maze):

    for row in maze:
        r = ""
        for cell in row:
            if cell == 'm':
                r += '   '
            elif cell:
                r += ' X '
            else:
                r += '   '
        print(r)


def create_maze(start, size):
    # start (1,1)
    frontier_stack = [[start, start]]
    maze = init_maze(size)
    explored = []

    while frontier_stack:
        # current_cell position tuple (x, y)
        current_cell = frontier_stack.pop()
        temp_stack = [item[1] for item in frontier_stack]
        explored.append(current_cell[1])

        # clear path
        # cell to remove
        pos = current_cell[0]
        maze[pos[0]][pos[1]] = 'm'

        pos = current_cell[1]
        maze[pos[0]][pos[1]] = 'm'

        all_neighbors = get_neighbors(current_cell[1], size)
        neighbors = [neighbor for neighbor in all_neighbors
                     if neighbor[1] not in explored and neighbor[1] not in temp_stack]

        if neighbors:
            random.shuffle(neighbors)
            frontier_stack.extend(neighbors)

    return maze


# m = create_maze((1, 1), 20)
# draw_maze(m)

