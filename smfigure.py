#github.com/rjsmethurst/prefig
"""
    An awesome plotting object to make any plot poster or presentation ready in the colour of your choice!
    
    R. J. Smethurst 
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import colorConverter

class SMfigure(plt.Figure):
    """
        A class that can replace the 'plt.figure' python plotting command to create plots with defaults similar to SuperMongo plots.
        """
    def __init__(self):
        
        if edgecolor == 'w':
            col = colorConverter.to_rgba_array(plt.rcParams['axes.color_cycle'])[:,:-1]
            inv_col = (256-(256*col))/256.0
            plt.rc('axes', color_cycle = list(inv_col))
        
        plt.rc('figure', figsize=(4,4), facecolor='none', edgecolor='none')
        plt.rc('savefig', dpi=300, facecolor='none', edgecolor='none', frameon='False')
        f = {'family':serif, 'size':100%}
        plt.rc('font', **f)
        plt.rc('text', color=fontcol)
        plt.rc('axes', labelsize='x-large', edgecolor=edgecolor, labelcolor=labelcolor, facecolor='none', linewidth=3)
        plt.rc('xtick', labelsize='large', color=fontcol)
        plt.rc('ytick', labelsize='large', color=fontcol)
        plt.rc('lines', markersize=8, linewidth=2)


        




