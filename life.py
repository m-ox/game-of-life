# There are four rules to the game of life
# Any live cell with fewer than two live neighbours dies, as if by underpopulation
# Any live cell with two or three live neighbours lives on to the next generation
# Any live cell with more than three live neighbours dies, as if by overpopulation
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa

class Life:
    def __init__(self, size):
        self.size = size

        # this randomly generates the 'live' cells on the grid
        rng = np.random.default_rng()
        self.grid = rng.integers(0, high=1, size=(self.size, self.size), dtype=np.int8, endpoint=True)


    def hello_neighbour(self, row, column):
        # print(f'{column},{row}')
        # check how many live neighbours

        neighbour_count = 0
        max = self.size-1
        
        if row > 0:
            top = self.grid[row-1,column]
        else:
            top = 0

        if column > 0:
            left = self.grid[row,column-1]
        else:
            left = 0

        if column < max:
            right = self.grid[row, column+1]
        else:
            right = 0

        if row < max:
            bottom = self.grid[row+1,column]
        else:
            bottom = 0

        neighbour_count += top + left + right + bottom

        return neighbour_count
        

    def step(self):
        # this shows the starting grid
        print(self.grid)
        neo_grid = np.zeros_like(self.grid) # epic

        # this performs a... chunky depth-first search into the grid
        i = -1
        for row in self.grid:
            i += 1
            j = -1
            
            for column in row:
                j += 1
                cell = self.grid[i,j]
                check = self.hello_neighbour(i,j)

                # cell alive condition
                if cell == 1:
                    # the following function checks for neighbours -- and returns how many neighbours there are
                    if check < 2 or check > 3:
                        neo_grid[i,j] = 0
                    else:
                        neo_grid[i,j] = 1
                # cell presumed dead condition
                else:
                    if check == 3:
                        neo_grid[i,j] = 1

        self.grid = neo_grid         


# below is the animate function that repeats the game step process
def animate(f):
    game.step()
    im.set_array(game.grid)

    return im,


def main():
    global im, game
    fig, ax = plt.subplots(1, 1)

    size = input("What size of game would you like? >> ")
    if size == '':
        game = Life(25) # default grid is 25 by 25
    elif int(size) > 100:
        print('I am not letting you blow up your computer today. Defaulted to 100.')
        game = Life(100)
    else:
        game = Life(int(size))
        
    im = ax.imshow(game.grid, animated=True)

    counter = input("How long do you want the game to last? (#iterations) >> ")
    if counter == '':
        counter = 5
    else:
        counter = int(counter)

    while np.sum(game.grid) > 0:
        anim = fa(fig, animate, frames=counter, interval=200, blit=True, repeat=False)
        counter -= 0
        plt.show()

        if np.sum(game.grid) == 0:
            print("The game of life ended in total annihilation!")
            break

        if counter == 0:
            print("The game of life has ended!")

    plt.show()


if __name__ == "__main__":main()