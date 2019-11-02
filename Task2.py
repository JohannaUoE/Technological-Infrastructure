try:
    import PackageTask2
except ImportError:
    print('The document you sppecified cannot be found')
    print('check for file direcrory and spellings')


import argparse
parser = argparse.ArgumentParser(description="Plotting Neighbourhoods")
parser.add_argument('dat',
                    help='File to be plotted')
args = parser.parse_args()

PackageTask2.read_nat_neigh(args.dat)
