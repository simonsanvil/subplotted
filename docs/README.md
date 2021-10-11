Module subplotted.subplotted
============================

Functions
---------

    
`get_nrows_from_iterable(iterable, ncols)`
:   

    
`subplotted(iterable: Union[int, Iterable[+T_co]], ncols: int = 2, figsize=None, axes_per_iter: int = 1, ncols_second_dim: int = 2, zipped: bool = True, second_dim_wspace: float = 0, second_dim_hspace: float = 0, **kwargs)`
:   Make matplotlib subplots from iterables. For each element of the iterable given a subplot will be made.
    
    Parameters
    ---------------
    iterable : Union[int,Iterable], required
        Iterable instance or integer (to make a range)    
    ncols : int
        Number of columns for the subplots grid
    figsize : tuple, optional
        Tuple defining the (width,height) of the image of the matplotlib figure
    axes_per_iter : int=1
        Number of axes to return for each instance of the iterable, default is one ax. 
        If greater than one the resulting figure will look like a grid of len(iterable) cells where each cell has another of axes_per_iter subplot.
    ncols_second_dim : int=2
        Number of columns of the second dim (if axes_per_iter is greater than one)
    zipped : bool=True
        Whether to return the figure, axes, and iterable elements zipped or not. Set to True to use in for loops.
    second_dim_wspace : float=0
        Width space between each inner ax of the second dimension. Default is 0
    second_dim_hspace : float=0
        Height space between each inner ax of the second dimension. Default is 0