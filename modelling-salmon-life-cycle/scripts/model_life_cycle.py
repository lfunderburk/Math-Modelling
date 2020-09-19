# Authors: Courtney V, Laura GF, Pierayeh Vahdani
# Date created: Sept 12 2020
# Date modified: 

# Import libraries 
import numpy as np
from scipy.integrate import odeint
from ipywidgets import interact, interact_manual, widgets, Layout, VBox, HBox, Button
from IPython.display import display, Javascript, Markdown, HTML, clear_output
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import requests as r

def functions(par1):
    return par1


if __name__ == "__main__":
    
    print("This is the main program")
    print("This program models the life cycle of chinook salmon")
