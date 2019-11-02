import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter, MultipleLocator
__all__ = ['plotPandas']

### this definition is just for the layout
def niceplot(ax):
    # the plot shows functions of a sinus
    # A shows a the sin(x), the others are changing in amplitude etc.
    # it makes sense to change the ticks of the x axis to pi
    # format the xaxis so that pi is shown
    # code from https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib
    ax.xaxis.set_major_formatter(FuncFormatter(
         lambda val,pos: '{:.1g}$\pi$'.format(val/np.pi) if val !=0 else '0'
    ))
    ax.xaxis.set_minor_formatter(FuncFormatter(
         lambda val,pos: '{:.2g}$\pi$'.format(val/np.pi) if val !=0 else '0'
    ))
    ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))
    ax.xaxis.set_minor_locator(MultipleLocator(base=np.pi/4))
    # set the legend to a nice spot (https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot)
    ax.legend(loc='upper right', bbox_to_anchor=(1, 1),
            ncol=2, fancybox=True, shadow=True)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.title('Mutations of Sin(x) ')
    plt.grid(True)
    plt.show()



### this opens the file, reads the data, assigns column headers and plots the data
## its also a lot faster! :-)
def plotPandas(filename):
    data = pd.read_csv(filename ,delimiter=' ', header=None)
    data.columns =[str(i) for i in range(len(data.columns))]

    myplot = data.plot(x='0')
    niceplot(myplot)



if __name__ == '__main__':

    plotPandas('plenty.data')
