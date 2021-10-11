subplotted
==============================

Easily generate matplotlib.pyplot subplot axes directly from iterables

Installation
-------------

```
pip install git+git://github.com/simonsanvil/subplotted.git
```

Usage
----------------

```python
from subplotted import subplotted
from skimage import io
img_paths = [f for f in os.listdir('images') if f.endswith('.jpg')]

#Make two columns of subplots of these images
for S, ax, img_path in subplotted(img_paths,ncols=2,figsize=(6,10)):
    img = io.imread(img_path)
    ax.imshow(img)
```
![example img 1](https://www.dropbox.com/s/ee4w6uqb7c011oj/subplotted_ex_1.png?raw=1)

Use the subplot helper "S" to help you customize the aspect of your figure.


```python
#Make it 5 columns instead of 2 and customize the figure
for S,ax,(i,img_path) in subplotted(enumerate(img_paths),ncols=5,figsize=(22,6)):
  img = io.imread(img_path)
  ax.imshow(img)
  #Customize each individual ax
  ax.set_title(f"Image {i}")
else:
  #Customize all axes at the same time using the subplot helper "S"
  S.set_all(ylabel='Height',xlabel='Width') #Set ylabel of all subplots
  #Or set them by their index (starting from 0 from left to right top to bottom)
  S.set_all(yticks=[],indices=[1,2,3,4,6,7,8,9]) #Remove the yticks of all subplots that are not in the leftmost
  #You can also use a lambda filter instead
  S.set_all(xticks=[],indices=lambda i: i<5) #Remove the xticks of the first row
  #S contains an instance of the entire figure that can be obtained with "fig"
  S.fig.tight_layout()
```

![example img 1](https://www.dropbox.com/s/b6q4quqnwmcxtwq/subplotted_ex_2.png?raw=1)


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │    
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── subplotted                <- Source code for this project.
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

