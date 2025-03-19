from element import Element
import time
import threading
from queue import deque

class Matrix:
    def __init__(self, rows, columns):
        self.matrix = [[0] * columns for _ in range(rows)]
        self.rows = rows
        self.cols = columns
        self.elements_list = []
        self.elements_dict = {}
        self.mobile_elements = []
        self.target_set = set()
        self.target_dict = {}
        self.target_counters = {}
        self.fixed_elements = []
        self.fixed_elements_dict = {}
        for i in range(columns):
            e = Element(self, (rows-1,i))
            e2 = Element(self, (rows-2,i))
            self.elements_dict[(rows-2,i)] = e2
            self.elements_list.append(e)
            self.elements_list.append(e2)
        self.target_shape = None
        self.iteration = 1
    
    def bfs2(self, target):
        queue = deque([(target, [])])
        visited = set([target])  
        directions = {
            (-1, 0): "down",
            (0, -1): "right",
            (0, 1): "left",
            (1, 0): "up"
        }

        while queue:
            (r, c), path = queue.popleft()  
            if self.matrix[r][c] == 2:
                return (r, c), path  

            for (dr, dc), move in directions.items():
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < self.rows and 0 <= new_c < self.cols and (new_r, new_c) not in visited and self.matrix[new_r][new_c] != 4:
                        queue.append(((new_r, new_c), path + [move])) 
                        visited.add((new_r, new_c))

        return None  
        
    def find_width_and_origin(self):
        if not self.target_shape:
            return None 
        min_c = min(self.target_shape, key=lambda coordinate: coordinate[1])[1]
        max_c = max(self.target_shape, key=lambda coordinate: coordinate[1])[1]
        min_r = min(self.target_shape, key=lambda c: c[0])[0]  

        lowest_row = sorted([coordinate for coordinate in self.target_shape if coordinate[0] == min_r], key=lambda coordinate: coordinate[1]) 
        number_of_origins = int(len(self.target_shape)/10)
        origins = []
        for i in range(number_of_origins):
            origin = lowest_row[int((i+1)*len(lowest_row)/(number_of_origins+1))]
            if origin not in origins:
                origins.append(origin)
        print(origins)
        return max_c-min_c, origins

    def place_origin(self, target_width, target_origin):
        initial_column = int((len(self.matrix[0])-target_width)/2)
        return (len(self.matrix)-3,initial_column+target_origin[1])

    def run_matrix(self, target_shape):
        time.sleep(1)
        self.target_shape = target_shape
        width, origins = self.find_width_and_origin()
        print(origins)
        for origin in origins:
            origin_matrix_coordinates = self.place_origin(width, origin)
            e = self.elements_dict[(origin_matrix_coordinates[0]+1, origin_matrix_coordinates[1])]
            e.position = origin_matrix_coordinates
            e.status = "chief"
            e.relative_position = origin
            self.matrix[origin_matrix_coordinates[0]][origin_matrix_coordinates[1]] = 2
            self.matrix[origin_matrix_coordinates[0]+1][origin_matrix_coordinates[1]] = 0
            e.update_collections()
            self.fixed_elements.append(e)
            self.fixed_elements_dict[origin_matrix_coordinates] = e
            self.target_set.add(origin)
        self.mobile_elements = [e for e in self.elements_list if e not in self.fixed_elements]
        k = 0
        while len(self.target_dict) != len(target_shape) and k < 10:
            #k += 1
            threads = []
            for e in self.mobile_elements:
                thread = threading.Thread(target=e.run)
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()
            threads = []
            for value in self.target_counters.values():
                value += 1
            blocked_targets = [key for key, value in self.target_counters.items() if value > 5]
            for t in blocked_targets:
                src, path = self.bfs2(t)
                self.fixed_elements_dict[src].run_given_sequence(path, t)


            print(f"-------------ITERATION {self.iteration}-------------") #TO BE DELETED
            self.iteration += 1 #TO BE DELETED
            for row in self.matrix:
                    print(row)