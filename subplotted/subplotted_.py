import matplotlib.pyplot as plt
import numpy as np

def subplotted(iterable,ncols=2,figsize=None,zipped=True ,**kwargs):
    if isinstance(iterable,int):
        iterable = range(iterable)
    total_rows = np.ceil(len(iterable)/ncols).astype(int)
    figsize = figsize if figsize is not None else (ncols*10,total_rows*6)
    fig, axes = plt.subplots(total_rows,ncols,figsize=figsize,**kwargs)
    axes = np.atleast_2d(axes)
    axlist = [ax for subl in axes for ax in subl]#[0:len(iterable)]
    if len(axlist) > len(iterable):
        for ax in axlist[len(iterable):]:
            ax.axis('off')
    if zipped:
        return zip([fig for _ in axlist],axlist,iterable)
    else:
        return (fig,axlist,iterable)