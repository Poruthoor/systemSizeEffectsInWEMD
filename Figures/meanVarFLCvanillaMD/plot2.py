import sys
import numpy as np
import argparse
import re
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from ast import literal_eval
from scipy import constants

############################# Data Input ######################################

# Parse command-line
parser = argparse.ArgumentParser()
parser.add_argument('--suffix',
                    default="foo",
                    help='File name suffix')
parser.add_argument('--xRange',
                    default="(0, 10500)",
                    help='xRange as a tuple')
parser.add_argument('--yRange',
                    default="(0, 1)",
                    help='yRange as a tuple')
parser.add_argument('--xLabel',
                    default="System Size (# of lipids)",
                    help='X axis label')
parser.add_argument('--xlog',
                    default=False,
                    help='X axis to be in log scale')
parser.add_argument('--dat_file',
                    nargs='+',
                    help='Input file')
args = parser.parse_args()

###############################################################################
# Evaluating xRange
try:
    tupX = literal_eval(args.xRange)
except (SyntaxError, ValueError):
    print("%s -> Invalid tuple format given" % args.xRange)

# Evaluating yRange
try:
    tupY = literal_eval(args.yRange)
except (SyntaxError, ValueError):
    print("%s -> Invalid tuple format given" % args.yRange)

# #  ############################# Plot parameters #################################

#  plt.rcParams.update({'font.size': 14})
#  plt.style.use('dark_background')

SMALL_SIZE = 18
MEDIUM_SIZE = 18
BIGGER_SIZE = 18

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#  ################################ Ploting #######################################

temperatures = [323, 423]
lineStyle = ["-", "--"]

fig, axs = plt.subplots(figsize=(8, 6))

for file in args.dat_file:
        for tindex, tvalue in enumerate(temperatures):
            if (str(tvalue) in file):
                Data = np.loadtxt(file, dtype=float)
                x = Data[:,0]
                y = Data[:,1]
                yerr = Data[:,2]

                axs.errorbar(x, y, yerr, fmt=lineStyle[tindex], c="black",
                             label=str(tvalue)+"K",
                             capsize=5) #, 'o-', c="black", linewidth=5)

axs.set_ylim(tupY)

if args.xlog:
    axs.set_xscale("log")
else:
    axs.set_xlim(tupX)

ylabel = r'$<\text{FLC}>$'
plt.xlabel(str(args.xLabel))
plt.ylabel(ylabel)

fig.tight_layout()
box = axs.get_position()
axs.legend(loc='upper right', ncol=3,
              handlelength=1, frameon=False)

plt.savefig(str(args.suffix) + ".pdf")
