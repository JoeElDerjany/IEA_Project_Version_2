from collections import deque

class Element:
    def __init__(self, matrix, initial_position):
        self.matrix = matrix
        self.initial_position = initial_position
        self.markers = []
    
    def bfs(matrix, start):
        rows, cols = len(matrix), len(matrix[0]) 
        queue = deque([(start, [])])
        visited = set([start])  

        directions = {
            (0, 1): "left",
            (0, -1): "right",
            (1, 0): "up",
            (-1, 0): "down"
        }

        while queue:
            (r, c), path = queue.popleft()  
            #print(r, c) # TO BE DELETED
            if matrix[r][c] == 1:
                return [start, (r, c), path, 0]  

            for (dr, dc), move in directions.items():
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and matrix[new_r][new_c] != 2 and matrix[new_r][new_c] != 4:
                    queue.append(((new_r, new_c), path + [move])) 
                    visited.add((new_r, new_c))

        return None  