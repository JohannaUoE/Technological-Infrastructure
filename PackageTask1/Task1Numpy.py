

#Import Packages that are needed
import numpy as np
from matplotlib import pyplot as plt
## allow functions to be used globally
__all__ = ['plotNumpy', 'plotIt', 'look_at_file']

'''Following are the Functions for Task 1. The first function (look_at_files) is only for testing purposes.
The second (plotIt) plots teh outputs of the third function (plotNumpy)'''


def look_at_file(infile):
    test_list = []
    with open(infile, 'r') as infile:
        line = infile.readline() #just read the first line to test the data is correct
        test_list.append(line.split()) #append the data to teh test list, which will be tested in Test_it
    return test_list


def plotIt(x,y):
    try:
        # .T transposes the array to 10 columns
        y2 = y.T
        # loop over every column in y2
        for i in range(len(y2)):
            #plot the x column against each y column
            plt.plot(x,y2[i])

        #label the plot
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.title('Mutations of Sin(x)')
        #display the plot
        plt.show()

    except SyntaxError:
        print('Look out for errors regarding the syntax')


def plotNumpy(infile):
    try:
        #open the file that has been prompted into the function as read
        with open(infile, 'r') as infile:
        #create an emtpty lists
            x = []
            y = []
        # loop over every line in the file
            for line in infile.readlines():
            #split the values after a space

                line = line.split()
                #append the first item to x
                x.append(line[0])
                # append all other items to y
                y.append(line[1:])
        # save x as numpy array (float)
        a = np.array(x, dtype=float)
        # save y as numpy array (float)
        b = np.array(y,dtype=float)
        #call plot it function with both arrays
        plotIt(a,b)

    except FileNotFoundError:
        print("Your File Path is wrong")





if __name__ == '__main__':
    x,y = plotNumpy()

    look_at_file()
