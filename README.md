This simple python script will create a double precision binary file from a numpy 2D grid. This allows you to input interesting initial density 
distributions etc. into your EPOCH simulation. For more information on how to do this read the documents linked.

1) [Species Block](https://epochpic.github.io/documentation/input_deck/input_deck_species.html)
2) [Binary files](https://epochpic.github.io/documentation/input_deck/binary_files)

In this repo:
1) .py file: contains the relavent functions to create the .dat binary file
2) input.deck: An input for EPOCH which can read in the .dat file
3) particles.dat: The binary data file created using the python functions
4) particles.png: An image of the created grid (as seen by EPOCH)

Note: it is always worth creating a simple simulation to check that the input appears the way you want it to. This input.deck runs in a couple of seconds.

Also note that FORTRAN (and EPOCH) reads arrays as "column-major order" whereas numpy uses "row-major order" which is why the image is rotated when it is 
plotted.
