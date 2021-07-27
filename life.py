# There are four rules to the game of life
# Any live cell with fewer than two live neighbours dies, as if by underpopulation
# Any live cell with two or three live neighbours lives on to the next generation
# Any live cell with more than three live neighbours dies, as if by overpopulation
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

import numpy as np

class Life:
    
    def __init__(self, size):
        self.size = size

        # this randomly generates the 'live' cells on the grid
        rng = np.random.default_rng()
        self.grid = rng.integers(0, high=1, size=(self.size, self.size), dtype=np.int8, endpoint=True)

    def hello_neighbour(self, column, row):
        # print(f'{column},{row}')

        # this confirms the cell is alive
        if self.grid[column,row] == 1:
            print(column, row, 'cell')

    def play(self):
        # this shows the starting grid
        print(self.grid)

        # this performs a... chunky depth-first search into the grid
        i = -1
        for row in self.grid:
            i += 1
            j = -1
            for column in row:
                j += 1
                # the following function checks for neighbours
                self.hello_neighbour(i, j)

def main():
    size = input("What size of game would you like? >> ")
    if size == '':
        game = Life(25) # default grid is 25 by 25
    else:
        game = Life(int(size))
    game.play()

if __name__ == "__main__":main()