# import the packages that will be used
import numpy as np

from matplotlib import pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter, MultipleLocator
import cartopy.crs as ccrs
import cartopy
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.feature as cfeature


__all__ = ['read_nat_neigh','readNeigh']





def readNeigh(infile):
    #this function is just for testing reasons
    key = [] #create empty list
    with open(infile, 'r') as infile: #open file

        for line in infile.readlines(): #iterate over all lines

            if line[0].isalpha(): #if a file starts with a letter, the line shall
            #be appended to the list
                    key.append(str(line.strip()))
                    continue
            else:
                continue # everything else shall be ignored
    return key



def read_nat_neigh(infile):
    x = [] #create empty list
    y = [] #create empty list
    dict = {} #create empty dictionary
    with open(infile, 'r') as infile: # open file
        for line in infile.readlines(): #read all lines


            if line[0] == "#": #if the line start with a # then it shall be
            #ignored
                continue

            if line[0].isalpha(): #if a file starts with a letter, the line shall
            #be appended to the list
                key = str(line.strip())
                continue #then continue

            if line[0] == "[": #if the line starts with a [

                linelist = np.array(eval(line)).T #create an array from the line
                #eval if list looks like a list, make it to list and T. = transpose
                #https://stackoverflow.com/questions/20543573/how-to-convert-list-lookalike-into-a-list
                #https://docs.scipy.org/doc/numpy-1.5.x/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T

                x, y = linelist[0], linelist[1] # stire first item as x and second as y
                continue #then continue

            if line != "\n": # if a line is not starting with linebreack
            # it must start with ()
            # after stripping and splitting the strings, store them in columns as a and b
                a, b = line[1:-2].strip().split(', ')
                #append a and b as float to x and y respectively
                x.append(float(a))
                y.append(float(b))
                continue

            if line == "\n": #if the line is empty (linebreack) the neighboorhood must be over
                dict.update({key:[x,y]}) #append all stored item to the dictionary
                #clear the lists for the next neighboorhood
                x = []
                y = []
                key = []


    plotmap(dict) #call the function and parse the dictionary into it




def plotmap(my_dict):


    for key in my_dict.keys(): #iterate through the dictionary calling every key
        # plot the coodrinates of each Neighbourhood
        fig = plt.plot(my_dict[key][0], my_dict[key][1])
        ax = plt.axes(projection=ccrs.OSGB()) #specify coordinate system
    plt.title('Neighbourhoods of Edinburgh')
    #insert a point like the Castle to orientate better within the map
    ax.plot(325149, 673492, 'bo', transform = ccrs.OSGB())
    ax.text(325148, 673492, 'Castle', transform = ccrs.OSGB())
    ax.gridlines() # add gridlines
    ax.set_xticks([305000, 310000, 315000, 320000, 325000, 330000, 335000],crs=ccrs.OSGB())


    plt.show()


if __name__ == '__main__':

    readNeigh('natural_neighbourhoods.dat')
    secondfile('natural_neighbourhoods.dat')
