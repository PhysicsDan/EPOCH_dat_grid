import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt

"""
It is best to create a new .dat file for every single array otherwise you are likely to make mistakes with calculating the byte offset from the start of a data file to find a given piece of data.

This code is very simple basically it will take an array and a specified set of dimensions (in 2D for now...) and will create the relavent .dat file which can be read by EPOCH. Note if you change the number of x and y points in EPOCH you will need to recreate the '.dat' file.

Note: it is worth checking the datafile using check_dat_file function. It rotates the image so it will be the same orientation as what EPOCH will see.

Also if you have a variation in number density then it is probably better to use npart rather than npart_per_cell in EPOCH so you don't have lots of low particle weights. Please correct me if I'm wrong!

- Daniel
"""
def main():
    # DEFINE YOUR GRID SHAPE HERE
    shape = (10,20) # ny and nx
    fname = 'particles'
    grid = np.logspace(22,25,200).reshape(shape)
    epoch_dat(grid, filename = fname, shape=shape)
    check_dat_file(fname, shape)

def epoch_dat(initial_grid, filename = 'particles',shape=None):

    if '.' in filename:
        filename = filename.split('.')[0]

    # just write out if file is ready
    if shape==None:
        with open(f"{filename}.dat", 'wb') as f:
            initial_grid.tofile(f)
        print(f"Saved data to {filename}.dat")
        return 'SUCCESS'
    else:
        # resize and output if necessary
        data = resize(initial_grid, shape)
        with open(f"{filename}.dat", 'wb') as f:
            data.tofile(f)
        print(f"Saved data to {filename}.dat")
        return 'SUCCESS'

def check_dat_file(filename, shape):
    d = np.fromfile(f'{filename}.dat', dtype='float64').reshape(shape)
    if d.size > 1000:
        d = d[::10,::10]
    plt.imshow(rotate90cw(d))
    plt.savefig(f'{filename}.png')
    plt.show()
    print("This is the orientation EPOCH will see")

def rotate90cw(grid):
    s = np.shape(grid)
    new_grid = np.zeros((s[1], s[0]))
    for i in range(s[0]):
        new_grid[:,i] = grid[i,:]
    return new_grid

if __name__ == '__main__':
    main()

