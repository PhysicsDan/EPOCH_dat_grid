import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt

"""
It is best to create a new .dat file for every single array otherwise you are likely to make mistakes with calculating the byte offset from the start of a data file to find a given piece of data.

This code is very simple basically it will take an array and a specified set of dimensions (in 2D for now...) and will create the relavent .dat file which can be read by EPOCH. Note if you change the number of x and y points in EPOCH you will need to recreate the '.dat' file.

Note: it is worth checking the datafile using check_dat_file function.

Also if you have a variation in number density then it is probably better to use npart rather than npart_per_cell in EPOCH so you don't have lots of low particle weights. Please correct me if I'm wrong!

- Daniel
"""
def __main__():
    # DEFINE YOUR GRID SHAPE HERE
    shape = (10,20) # ny and nx
    fname = 'particles'
    grid = np.logspace(22,25,200).reshape(shape)
    create_epoch_dat(grid, filename = fname, shape=shape)
    check_dat_file(fname, shape)

def create_epoch_dat(initial_grid, filename = 'particles',shape=None):
    '''
    Outputs a numpy array in the correct format for EPOCH (test)

            Parameters:
                    initial_grid (np.array): 2d parameter grid
                    filename (str): Name of output file
                    shape (tuple): Shape of desired array (optional)
            Returns:
                    (str): 'SUCCESS'
    '''

    if filename.split('.')[-1]!='dat':
        if len(filename.split('.'))>2:
            filename = filename[0]
        filename += '.dat'

    # just write out if file is ready
    if shape!=None:
        # resize and output if necessary
        initial_grid = resize(initial_grid, shape)
    
    with open(filename, 'wb') as f:
        initial_grid.tofile(f)
    print(f"Saved data to {filename}")
    return 'SUCCESS'

def check_dat_file(filename, shape):
    if filename.split('.')[-1]!='dat':
        filename+='.dat'
    d = np.fromfile(filename, dtype='float64').reshape(shape)
    # note for imshow (0,0) is bottom left
    # in epoch (0,0) is top right
    # therefore we use [::-1,:] when plotting with plt.imshow
    if d.size > 1000:
        plt.imshow(d[::-10,::10])
    else:
        plt.imshow(d[::-1,:])
    plt.savefig(f"{filename.split('.')[0]}.png")
    plt.show()
    print("This is the orientation EPOCH will see\n")
    return d

def rotate90cw(grid):
    s = np.shape(grid)
    new_grid = np.zeros((s[1], s[0]))
    for i in range(s[0]):
        new_grid[:,i] = grid[i,:]
    return new_grid

if __name__ == '__main__':
    __main__()

