from dataclasses import dataclass, field
from typing import List, Tuple, Iterable, Union, Callable
import numpy as np

@dataclass
class SubplottedHelper:
  iterable:Iterable
  fig:object
  axlist:List
  outer_grid:object
  inner_grids:Tuple=field(default_factory=lambda : [])
  args:dict=field(default_factory=lambda : {})

  @property
  def figure(self):
    return self.fig
  
  @property
  def inner_grid_shape(self):
    if not self.inner_grids:
      return (1,1)
    grid0 = self.inner_grids[0]
    return (grid.nrows,grid.ncols)
  
  @property
  def subplots(self):
    return axlist

  def tight_layout(self):
    self.outer_grid.tight_layout(self.fig)

  def get_subplots(self,as_grid=True):
    if as_grid:
      axes = np.atleast_2d(self.axlist)
      axlist = [ax for subl in axes for ax in subl]
      nrows = np.ceil(len(self.iterable)/self.args.get('ncols')).astype(int)*self.inner_grid_shape[0]
      ncols = self.args.get('ncols')*self.inner_grid_shape[1]
      return np.array(axlist).reshape(nrows, ncols )

    return np.array(self.axlist)
  
  def set_all(self,indices:Union[List,Callable]=None,**kwargs):
    '''
    Batch setter for all ax subplots

    Parameters
    --------------
    indices : List, Callable or int
        Indices of the axes for which the function will be applied (starting with 0).
        If a callable it is expected to receive an index number of an ax and return a boolean value
        of whether or not the function should be applied to that index.
    **kwargs
        Arguments to pass to ax.set
    '''
    if isinstance(indices,dict):
      for inds,kwargs in indices.items():
        self.set_all_(inds,**kwargs)
      return
    return self.set_all_(indices,**kwargs)
  
  def set_all_(self,indices:Union[List,Callable]=None,val=None,**kwargs):
    '''
    Apply function to all axes

    Parameters:
    -----------
    func : Callable or str
        Callable or name of a matplotlib.axes function to apply to the ax.
        If a callable it must receive a matplotlib.axes ax as its first parameter.
    indices : List, Callable or int
        Indices of the axes for which the function will be applied (starting with 0).
        If a callable it is expected to receive an index number of an ax and return a boolean value
        of whether or not the function should be applied to that index.
    val : optional
        Single value to pass to func as second argument
    **kwargs
        Arguments to pass to func
    '''
    axes = np.atleast_2d(self.axlist)
    axlist = [ax for subl in axes for ax in subl]
    if isinstance(indices,int):
      indices = [indices]
    for i,ax in enumerate(axlist):
      if not indices:
        pass
      elif isinstance(indices,Callable):
        if not indices(i):
          continue
      elif i not in indices:
        # print(f"{i} not in indices")
        continue
      
      # if isinstance(func,str):
      #   func = getattr(ax,func)
      # if val is None:
      #   func(**kwargs)
      # else:
      #   func(val,**kwargs)
      kwargs_ = kwargs.copy()
      for arg in kwargs:
        if isinstance(kwargs[arg],Callable):
          kwargs_[arg] = kwargs[arg](i)
      
      # if isinstance(func,str):
      #   func = getattr(ax,func)
      # if val is None:
      #   func(**kwargs)
      # else:
      #   func(val,**kwargs)

      ax.set(**kwargs_)
