def solution(rectangle, characterX, characterY, itemX, itemY):
    scaled_grid_2x = [[0 for _ in range(100)] for _ in range(100)]
    scaled_rectangle_2x = [(point * 2 - 1 for point in points) for points in rectangle]

    for (x1, y1, x2, y2) in scaled_rectangle_2x:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (i == x1 or i == x2 or j == y1 or j == y2) and scaled_grid_2x[i][j] != -1:
                    scaled_grid_2x[i][j] = 1
                else:
                    scaled_grid_2x[i][j] = -1

    queue = [(characterX * 2 - 1, characterY * 2 - 1, 0)]
    scaled_grid_2x[characterX * 2 - 1][characterY * 2 - 1] = 2
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    target = (itemX * 2 - 1, itemY * 2 - 1)
    while queue:
        x, y, movement = queue.pop(0)
        if (x, y) == target:
            return movement // 2

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 100 and 0 <= ny < 100 and scaled_grid_2x[nx][ny] == 1:
                scaled_grid_2x[nx][ny] = 2
                queue.append((nx, ny, movement + 1))
    return 0
