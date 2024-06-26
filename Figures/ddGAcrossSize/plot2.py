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
                    default="(-1.5, 1.5)",
                    help='yRange as a tuple')
parser.add_argument('--xLabel',
                    default="System Size (# of lipids)",
                    help='X axis label')
parser.add_argument('--xlog',
                    default=False,
                    help='X axis to be in log scale')
parser.add_argument('--dat_file',
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

fig, axs = plt.subplots(figsize=(8, 6))

Data = np.loadtxt(args.dat_file,dtype=float)
x = Data[:,0]
y = Data[:,1]

axs.plot(x, y, 'o-', c="black", linewidth=3)
axs.scatter(x, y, s=100, c="black")
axs.set_ylim(tupY)

if args.xlog:
    axs.set_xscale("log")
else:
    axs.set_xlim(tupX)

#  box = axs.get_position()
#  axs.set_position([box.x0, box.y0 + box.height * 0.10,
                 #  box.width, box.height * 0.90])
#  axs.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=1)

ylabel = r'$\Delta\Delta G\ (kcal/mol)$'
plt.xlabel(str(args.xLabel))
plt.ylabel(ylabel)
plt.axhline(0, color='grey',linewidth=2)
plt.savefig(str(args.suffix) + ".pdf")
