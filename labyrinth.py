import random
import matplotlib.pyplot as plt

class Labyrinth:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.used = [[False] * w for _ in range(h)]
        self.neighbors = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        self.walls = set()

        for i in range(h + 1):
            for j in range(w):
                self.walls.add((i, j, i, j + 1))
        for i in range(w + 1):
            for j in range(h):
                self.walls.add((j, i, j + 1, i))
        
        self.generate([random.randint(0, h - 1), random.randint(0, w - 1)])

        self.walls = list(self.walls)
        border = []
        for wall in self.walls:
            if wall[0] == wall[2] == 0 or wall[1] == wall[3] == 0\
                    or wall[0] == wall[2] == h or wall[1] == wall[3] == w:
                        border.append(wall)
        
        for i in range(2):
            enter = random.choice(border)
            border.remove(enter)
            self.walls.remove(enter)
        

        
        for wall in self.walls:
            plt.plot([wall[0], wall[2]], [wall[1], wall[3]])
        plt.show()


    def on_board(self, pos):
        return pos[1] >= 0 and pos[1] < w and pos[0] >= 0 and pos[0] < h


    def get_wall(self, before, after):
        if before > after:
            before, after = after, before
        if before[0] == after[0]:
            return (before[0], after[1], before[0] + 1, after[1])
        else:
            return (after[0], before[1], after[0], before[1] + 1)
    

    def generate(self, pos):
        self.used[pos[0]][pos[1]] = True
        moves = [[pos[0] + neighbor[0], pos[1] + neighbor[1]] for neighbor in self.neighbors]

        while True:
            possible_moves = []
            for move in moves:
                if self.on_board(move) and not self.used[move[0]][move[1]]:
                    possible_moves.append(move)
            
            if not possible_moves:
                break

            move = random.choice(possible_moves)
            self.walls.remove(self.get_wall(pos, move))
            
            self.generate(move)


w, h = map(int, input().split())
L = Labyrinth(w, h)
