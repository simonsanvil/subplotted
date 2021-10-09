import matplotlib.pyplot as plt
import numpy as np

from typing import List, Tuple, Iterable, Union

def subplotted(
    iterable:Union[int,Iterable],
    ncols:int=2,
    figsize=None,
    num_axes_second_dim:int=1,
    ncols_second_dim:int=2,
    zipped:bool=True,
    second_dim_wspace:float=0,
    second_dim_hspace:float=0,
    **kwargs
  ):
  '''
  Make matplotlib subplots from iterables. For each element of the iterable given a subplot will be made.

  Parameters
  ---------------
  iterable:Union[int,Iterable], required
    Iterable instance or integer (to make a range)
  ncols:int
    Number of columns for the subplots grid
  figsize:tuple, optional
    Tuple defining the (width,height) of the image of the matplotlib figure
  num_axes_second_dim:int=1
    Number of axes to return for each instance of the iterable, default is one ax. 
    If greater than one the resulting figure will look like a grid of len(iterable) where each cell has another of num_axes_second_dim subplots.
   ncols_second_dim:int=2
    Number of columns of the second dim (if num_axes_second_dim is greater than one)
  zipped:bool=True
    Whether to return the figure, axes, and iterable elements zipped or not. Set to True to use in for loops.
  second_dim_wspace:float=0
    Width space between each inner ax of the second dimension. Default is 0
  second_dim_hspace:float=0
    Height space between each inner ax of the second dimension. Default is 0
  '''
  if isinstance(iterable,int):
      iterable = range(iterable)
  nrows = get_nrows_from_iterable(iterable,ncols)
  figsize = figsize if figsize is not None else (ncols*8,nrows*5)
  fig = plt.figure(figsize=figsize, constrained_layout=False,**kwargs)
  outer_grid = fig.add_gridspec(nrows=nrows, ncols=ncols)
  if num_axes_second_dim>1:
    axlist = []
    for i in range(nrows):
      for j in range(ncols):
        if num_axes_second_dim:
          nrows_second_dim = np.ceil(num_axes_second_dim/ncols_second_dim).astype(int)
        elif isinstance(iterable[i+j],Iterable):
          nrows_second_dim = get_nrows_from_iterable(iterable[i+j],ncols_second_dim)
        else:
          raise ValueError(f"Cant subplot a second dimension if num_axes_second_dim is None and iterable position ({i},{j}) is not also an iterable")
        inner_grid = outer_grid[i, j].subgridspec(nrows_second_dim, ncols_second_dim, wspace=second_dim_wspace, hspace=second_dim_hspace)
        inner_axes =  [ax for subl in np.atleast_2d(inner_grid.subplots()) for ax in subl]
        axlist.append(inner_axes[:(num_axes_second_dim)])
  else:
    axes = np.atleast_2d(outer_grid.subplots())
    axlist = [ax for subl in axes for ax in subl]

  if zipped:
    return zip([fig for _ in axlist],axlist,iterable)
  else:
    return (fig,axlist,iterable)

def get_nrows_from_iterable(iterable,ncols):
  return np.ceil(len(iterable)/ncols).astype(int)
