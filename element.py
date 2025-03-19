import time
from queue import deque
import copy

class Element:
    def __init__(self, Matrix, position):
        self.Matrix = Matrix
        self.position = position
        Matrix.matrix[position[0]][position[1]] = 1
        self.status = "member"
        self.relative_position = None
        self.rows = len(self.Matrix.matrix)
        self.cols = len(self.Matrix.matrix[0])
        self.path = ["center"]
    
    def sleep():
        time.sleep(0.2)

    def update_collections(self):
        r, c = self.relative_position
        directions = [
            ((r + 1, c), "up"), ((r - 1, c), "down"), 
            ((r, c - 1), "left"), ((r, c + 1), "right"),  
            ((r + 1, c - 1), "top-left"), ((r - 1, c - 1), "bottom-left"), 
            ((r + 1, c + 1), "top-right"), ((r - 1, c + 1), "bottom-right"),
            ((r + 2, c), "double-up"), ((r - 2, c), "double-down"), 
            ((r, c - 2), "double-left"), ((r, c + 2), "double-right"),  
            ((r + 2, c - 1), "double-top-left"), ((r - 2, c - 1), "double-bottom-left"), 
            ((r + 2, c + 1), "double-top-right"), ((r - 2, c + 1), "double-bottom-right"),
            ((r + 1, c - 2), "top-double-left"), ((r - 1, c - 2), "bottom-double-left"), 
            ((r + 1, c + 2), "top-double-right"), ((r - 1, c + 2), "bottom-double-right")    
        ]
        
        rm, cm = self.position
        for direction in directions:
            if direction[0] in self.Matrix.target_shape and direction[0] not in self.Matrix.target_set:
                self.Matrix.target_set.add(direction[0])
                match direction[1]:
                    case "up":                       
                        self.Matrix.target_dict[(rm-1,cm)] = direction[0]
                        self.Matrix.matrix[rm-1][cm] = 3
                        self.Matrix.target_counters[(rm-1,cm)] = 1
                    case "down":                       
                        self.Matrix.target_dict[(rm+1,cm)] = direction[0]
                        self.Matrix.matrix[rm+1][cm] = 3
                        self.Matrix.target_counters[(rm+1,cm)] = 1
                    case "left":                       
                        self.Matrix.target_dict[(rm,cm-1)] = direction[0]
                        self.Matrix.matrix[rm][cm-1] = 3
                        self.Matrix.target_counters[(rm,cm-1)] = 1
                    case "right":                       
                        self.Matrix.target_dict[(rm,cm+1)] = direction[0]
                        self.Matrix.matrix[rm][cm+1] = 3
                        self.Matrix.target_counters[(rm,cm+1)] = 1
                    case "top-left":
                        self.Matrix.target_dict[(rm-1,cm-1)] = direction[0]
                        self.Matrix.matrix[rm-1][cm-1] = 3
                        self.Matrix.target_counters[(rm-1,cm-1)] = 1
                    case "top-right":
                        self.Matrix.target_dict[(rm-1,cm+1)] = direction[0]
                        self.Matrix.matrix[rm-1][cm+1] = 3
                        self.Matrix.target_counters[(rm-1,cm+1)] = 1
                    case "bottom-left":
                        self.Matrix.target_dict[(rm+1,cm-1)] = direction[0]
                        self.Matrix.matrix[rm+1][cm-1] = 3
                        self.Matrix.target_counters[(rm+1,cm-1)] = 1
                    case "bottom-right":
                        self.Matrix.target_dict[(rm+1,cm+1)] = direction[0]
                        self.Matrix.matrix[rm+1][cm+1] = 3
                        self.Matrix.target_counters[(rm+1,cm+1)] = 1
                    case "double-up":                       
                        self.Matrix.target_dict[(rm-2,cm)] = direction[0]
                        self.Matrix.matrix[rm-2][cm] = 3
                        self.Matrix.target_counters[(rm-2,cm)] = 1
                    case "double-down":                       
                        self.Matrix.target_dict[(rm+2,cm)] = direction[0]
                        self.Matrix.matrix[rm+2][cm] = 3
                        self.Matrix.target_counters[(rm+2,cm)] = 1
                    case "double-left":                       
                        self.Matrix.target_dict[(rm,cm-2)] = direction[0]
                        self.Matrix.matrix[rm][cm-2] = 3
                        self.Matrix.target_counters[(rm,cm-2)] = 1
                    case "double-right":                       
                        self.Matrix.target_dict[(rm,cm+2)] = direction[0]
                        self.Matrix.matrix[rm][cm+2] = 3
                        self.Matrix.target_counters[(rm,cm+2)] = 1
                    case "double-top-left":
                        self.Matrix.target_dict[(rm-2,cm-1)] = direction[0]
                        self.Matrix.matrix[rm-2][cm-1] = 3
                        self.Matrix.target_counters[(rm-2,cm-1)] = 1
                    case "double-top-right":
                        self.Matrix.target_dict[(rm-2,cm+1)] = direction[0]
                        self.Matrix.matrix[rm-2][cm+1] = 3
                        self.Matrix.target_counters[(rm-2,cm+1)] = 1
                    case "double-bottom-left":
                        self.Matrix.target_dict[(rm+2,cm-1)] = direction[0]
                        self.Matrix.matrix[rm+2][cm-1] = 3
                        self.Matrix.target_counters[(rm+2,cm-1)] = 1
                    case "double-bottom-right":
                        self.Matrix.target_dict[(rm+2,cm+1)] = direction[0]
                        self.Matrix.matrix[rm+2][cm+1] = 3
                        self.Matrix.target_counters[(rm+2,cm+1)] = 1
                    case "top-double-left":
                        self.Matrix.target_dict[(rm-1,cm-2)] = direction[0]
                        self.Matrix.matrix[rm-1][cm-2] = 3
                        self.Matrix.target_counters[(rm-1,cm-2)] = 1
                    case "top-double-right":
                        self.Matrix.target_dict[(rm-1,cm+2)] = direction[0]
                        self.Matrix.matrix[rm-1][cm+2] = 3
                        self.Matrix.target_counters[(rm-1,cm+2)] = 1
                    case "bottom-double-left":
                        self.Matrix.target_dict[(rm+1,cm-2)] = direction[0]
                        self.Matrix.matrix[rm+1][cm-2] = 3
                        self.Matrix.target_counters[(rm+1,cm-2)] = 1
                    case "bottom-double-right":
                        self.Matrix.target_dict[(rm+1,cm+2)] = direction[0]
                        self.Matrix.matrix[rm+1][cm+2] = 3
                        self.Matrix.target_counters[(rm+1,cm+2)] = 1
    
    def bfs(self):
        queue = deque([(self.position, [])])
        visited = set([self.position])  

        directions = {
            (0, 1): "right",
            (0, -1): "left",
            (1, 0): "down",
            (-1, 0): "up"
        }

        while queue:
            (r, c), path = queue.popleft()  
            if self.Matrix.matrix[r][c] == 3:
                return (r, c), deque(path)  

            for (dr, dc), move in directions.items():
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < self.rows and 0 <= new_c < self.cols and (new_r, new_c) not in visited and self.Matrix.matrix[new_r][new_c] != 2 and self.Matrix.matrix[new_r][new_c] != 4:
                    queue.append(((new_r, new_c), path + [move])) 
                    visited.add((new_r, new_c))

        return None  
    
    def move_up(self):
        r,c = self.position
        if self.Matrix.matrix[r-1][c] != 1 and self.Matrix.matrix[r-1][c] != 2 and self.Matrix.matrix[r-1][c] != 4:
            self.Matrix.matrix[r][c] = 0
            self.Matrix.matrix[r-1][c] = 1
            self.position = (r-1,c)

    def move_down(self):
        r,c = self.position
        if self.Matrix.matrix[r+1][c] != 1 and self.Matrix.matrix[r+1][c] != 2 and self.Matrix.matrix[r+1][c] != 4:
            self.Matrix.matrix[r][c] = 0
            self.Matrix.matrix[r+1][c] = 1
            self.position = (r+1,c)

    def move_left(self):
        r,c = self.position
        if self.Matrix.matrix[r][c-1] != 1 and self.Matrix.matrix[r][c-1] != 2 and self.Matrix.matrix[r][c-1] != 4:
            self.Matrix.matrix[r][c] = 0
            self.Matrix.matrix[r][c-1] = 1
            self.position = (r,c-1)
    
    def move_right(self):
        r,c = self.position
        if self.Matrix.matrix[r][c+1] != 1 and self.Matrix.matrix[r][c+1] != 2 and self.Matrix.matrix[r+1][c+1] != 4:
            self.Matrix.matrix[r][c] = 0
            self.Matrix.matrix[r][c+1] = 1
            self.position = (r,c+1)

    def run(self):
        target, path = self.bfs()
        direction = path.popleft()
        match(direction):
            case "up":
                self.move_up()
            case "down":
                self.move_down()
            case "left":
                self.move_left()
            case "right":
                self.move_right()
        if self.position[0] == target[0] and self.position[1] == target[1]:
            self.relative_position = self.Matrix.target_dict[self.position]
            self.Matrix.matrix[self.position[0]][self.position[1]] = 2
            self.update_collections()
            self.Matrix.fixed_elements.append(self)
            self.Matrix.fixed_elements_dict[self.position] = self
            self.Matrix.mobile_elements.remove(self)
            self.Matrix.target_set.add(self.relative_position)
    
    def run_given_sequence(self, path, target):
        rr, cc = self.position()
        del self.Matrix.target_counetrs[target]
        direction = path.pop()
        match(direction):
            case "up":
                self.move_up()
            case "down":
                self.move_down()
            case "left":
                self.move_left()
            case "right":
                self.move_right()
        if self.position[0] == target[0] and self.position[1] == target[1]:
            self.relative_position = self.Matrix.target_dict[self.position]
            self.Matrix.matrix[self.position[0]][self.position[1]] = 2
            self.update_collections()
            self.Matrix.fixed_elements.append(self)
            self.Matrix.fixed_elements_dict[self.position] = self
            self.Matrix.mobile_elements.remove(self)
            self.Matrix.target_set.add(self.relative_position)
        self.Matrix.matrix[rr][cc] = 0
        
