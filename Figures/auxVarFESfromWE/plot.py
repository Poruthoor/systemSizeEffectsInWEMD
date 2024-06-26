import sys
import numpy as np
import argparse
import re
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from ast import literal_eval
from scipy import constants
from pathlib import Path

############################# Data Input ######################################

# Parse command-line
parser = argparse.ArgumentParser()
parser.add_argument('--suffix',
                    default="foo",
                    help='File name suffix')
parser.add_argument('--xRange',
                    default="(0, 1)",
                    help='xRange as a tuple')
parser.add_argument('--yRange',
                    default="(0, 4)",
                    help='yRange as a tuple')
parser.add_argument('--xLabel',
                    default="Fraction of Lipids in Clusters (FLC)",
                    help='X axis label')
parser.add_argument('--dat_files',
                    help='List of input files', nargs='+')
args = parser.parse_args()

###############################################################################
legend = list()

for m in range(len(args.dat_files)):

    basename = Path(args.dat_files[m]).stem
    legend.append(int(basename))

legend.sort()

print (" Analyzing system sizes :  ",legend)

if len(legend) == 1:
    legendRange = range(1)
else:
    legendRange = range(len(legend))

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

plotscale = 'energy'

SMALL_SIZE = 34
MEDIUM_SIZE = 34
BIGGER_SIZE = 34

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#  ################################ Ploting #######################################

fig, axs = plt.subplots(figsize=(14, 17))

colorDict = {"324":"blue", "648":"brown", "972":"green", "1944":"red",
             "3888":"purple", "7776":"olive", "10110":"black"}


for l in legendRange:

    FileName = str(legend[l]) + ".dat"

    for j in range(len(args.dat_files)):

        if FileName in args.dat_files[j]:

            print (args.dat_files[j])
            Data = np.loadtxt(args.dat_files[j],dtype=float, comments="#")
            x = Data[:,0]
            y = Data[:,1]
            niceYindex = np.isfinite(y)
            #  print (niceYindex)
            nice_x = x[niceYindex]
            nice_y = y[niceYindex]
            color = colorDict[str(legend[l])]

            #  axs.scatter(nice_x,nice_y, c=color)
            axs.plot(nice_x,nice_y,label=str(legend[l]) + " lipids", alpha=0.7,
                     linewidth=5, c=color)
            axs.set_xlim(tupX)
            axs.set_ylim(tupY)

ylabel = r'$\Delta G(x) (kcal/mol)$'
plt.xlabel(str(args.xLabel))
plt.ylabel(ylabel,labelpad=20)

box = axs.get_position()
axs.set_position([box.x0, box.y0 + box.height * 0.15,
                 box.width, box.height * 0.85])
axs.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3,
           frameon=False)
plt.savefig(args.suffix + ".pdf")
