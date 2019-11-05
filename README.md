# Technological-Infrastructure
Exam No.: B154523
These files are for the assignment of Technological Infrastructures at the University of Edinburgh (Msc Earth Observation and Geoinformation Management).

This Code is also uploaded on GitHub "JohannaUoE" Repository: "Technological-Infrastructure"

## Tests
Before running any tasks, the test (Tests folder) suite should be used by prompting "nosetests-3.6" into the shell. The test file performes 3 tests. The script tests, if the files are including correct data in order to perform the plottings. If the tests are failing, make sure the files are correct and in the right file directory. 

### Test 'test_numpy'
The first function "test_numpy" tests the first line of the 'plenty.data' file. It should include a list of 10 times '0.0'. If it does not include this line, this test fails.

### Test 'test_numpy2'
The second function of the test suite is called 'test_numpy2'. This test checks the file for the number of columns. If the file is not erroneus, the file contains 11 columns.

### Test 'test_neigh'

This function 'test_neigh' reads all the names of the neighbourhoods within the file and stores them as a list. It then compares this list against the list that was specified.


## Task 1

Run Task1.py in the shell, specifying the "plenty.data" file.
The file uses argparse to allow a user-friendly command-line interfaces.

Two plots are plotted. One is done with numpy arrays. The other is performed with the use of the package Pandas.
The plots are displaying mutations of sin(x), where x = pi

### PackageTask1
This Package includes two files with multiple functions. 

The file 'Task1Numpy' contains three functions:
  - 'look_at_file(infile)': This function is only for testing
  - 'plotIt(x,y)': Plots the x and y coordinates which will be parsed into the function
  - 'plotNumpy(infile)': Reads the file that is parsed into it and returns numpy arrays

The file 'Task1Pandas' contains two functions:

  - 'plotPandas(filename)': This function reads the data of the file using the Package Pandas, which is helpful reading data as DataFrames
  - 'niceplot(ax)': Plots the data frame that is parsed into the function. Since these datas are a mutation of the sin(x), the ticks of the x axis are converted to pi.

The '_ _init_ _.py' file reads allows the Package to be read



## Task 2

Run Task2.py in the shell, specifying the "natural_neighbourhoods.dat" file
If cartopy is not installed yet, install cartopy by using eg. pip install cartopy
The plot displays the neighboorhoods of Edinburgh. To orientate within the map, the castles is plotted as a point, labelled "Castle"

### PackageTask2

This Package includes two files with multiple functions. 

The file 'N_Neigh_Read' contains three functions:
  - 'readNeigh(infile)': This function is only for testing and reads all the names of the neighboorhoods
  - 'read_nat_neigh(infile)': Reads the data of the file. Iterates with a for loop over the lines and decides how the lines shall be handled. Stores a dictionary with entries of each neighboorhood with all coordinates of the vertices
  - 'plotmap(my_dict)': The dictionary is parsed into the function and plotted with cartopy and an additional shapefile 
  

The '_ _init_ _.py' file reads allows the Package to be read

Notes: 
in order to plot the grindlines with corresponding ticks in OSGB, I tried the following:

    gl = ax.gridlines(crs=ccrs.OSGB(), draw_labels=True,
                  linewidth=1, color='black', alpha=1, linestyle='-')
    gl.xlabels_top = True
    gl.ylabels_left = True
    gl.xlines = True
    gl.ylines = True

This error was produced:
TypeError: Cannot label OSGB gridlines. Only PlateCarree gridlines are currently supported.

Therefore, only gridlines in OSGB are displayed.
I did not use matplotlib gridlines, because they are orthogonal to the x and y axis, which is wrong
within OSGB and do not correspond with the displayed data

--> More details can be read within the codes

## References

Spatial Data Gov Scot (2019), ‘Data Zone Boundaries 2011’.
URL: https: // www. spatialdata. gov. scot/ geonetwork/ srv/ ger/ catalog.
search; jsessionid= D7F77645605E75A5049CE35CFB59347F# /metadata/7d3e8709-98fa-4d71-867c-d5c8293823f2
[last access 05.11.2019]

Lee, K. D. (2011). Python programming fundamentals. Springer.

Scitools.org.uk (2019) 'Cartopy Docs'
URL: https://scitools.org.uk/cartopy/docs/v0.13/index.html [last access 05.11.2019]


Docs Python Org (2019) 'argparse — Parser for command-line options, arguments and sub-commands'
URL: https://docs.python.org/3/library/argparse.html [last access 05.11.2019]

Note: References of Stackoverflow are given within in the code
