from dataclasses import dataclass, field
from typing import List, Tuple, Iterable, Union, Callable

@dataclass
class SubplottedHelper:
  iterable:Iterable
  fig:object
  axlist:List
  outer_grid:object
  inner_grid_shape:Tuple=field(default_factory=lambda : (1,1))
  args:dict=field(default_factory=lambda : {})

  @property
  def figure(self):
    return self.fig
  
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
    '''
    return self.apply_func_all('set',indices,**kwargs)
  
  def apply_func_all(self,func_name:str,indices:Union[List,Callable]=None,val=None,**kwargs):
    axes = np.atleast_2d(self.axlist)
    axlist = [ax for subl in axes for ax in subl]
    if not indices:
      indices = []
    for i,ax in enumerate(axlist):
      if isinstance(indices,Callable):
        if not indices(i):
          continue
      elif i not in indices:
        continue

      func = getattr(ax,func_name)
      if val is None:
        func(**kwargs)
      else:
        func(val,**kwargs)