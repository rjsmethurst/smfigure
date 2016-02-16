#github.com/rjsmethurst/prefig
"""
    An awesome plotting object to make any matplotlib plot look like it's been made with SuperMongo. 
    
    R. J. Smethurst 
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import colorConverter
import os

os.environ['PATH'] = os.environ['PATH'] + ':/usr/texbin'

class SMfigure(plt.Figure):
    """
        A class that can replace the 'plt.figure' python plotting command to create plots with defaults similar to SuperMongo plots.
        """

    params =   {'font.size' : 11,
                'text.usetex' : True,
                'xtick.major.size': 8,
                'ytick.major.size': 8,
                'xtick.minor.size': 3,
                'ytick.minor.size': 3,
                }
    plt.rcParams.update(params) 

    plt.rc('figure', figsize=(4,4), facecolor='none', edgecolor='none', autolayout=True)
    plt.rc('path', simplify=True)
    plt.rc('font', family='monospace', monospace=['Nimbus Mono L','Courier New', 'Andale Mono', 'Courier', 'Bitstream Vera Sans Mono',  'Fixed', 'Terminal', 'monospace'])
    plt.rc('axes', labelsize='large', facecolor='none', linewidth=0.7, color_cycle = ['k', 'r', 'g', 'b', 'c', 'm', 'y'])
    plt.rc('xtick', labelsize='medium')
    plt.rc('ytick', labelsize='medium')
    plt.rc('lines', markersize=4, linewidth=1, markeredgewidth=0.2)
    plt.rc('legend', numpoints=1, frameon=False, handletextpad=0.3, scatterpoints=1, handlelength=2, handleheight=0.1)
    plt.rc('savefig', dpi=300, facecolor='none', edgecolor='none', frameon='False')



        




