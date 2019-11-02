try:
    import PackageTask1
except ImportError:
    print('The document you sppecified cannot be found')
    print('check for file direcrory and spellings')
import argparse
parser = argparse.ArgumentParser(description="Plotting Mutations of Sin(x)")
parser.add_argument('data',
                    help='File to be plotted')
args = parser.parse_args()

PackageTask1.plotNumpy(args.data)
PackageTask1.plotPandas(args.data)
