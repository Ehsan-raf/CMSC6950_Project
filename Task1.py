from os.path import join
import datetime
import dateutil
from copy import deepcopy

import numpy as np
import pandas as pd

from pymagicc import MAGICC6, rcp26, zero_emissions
from pymagicc.io import MAGICCData

get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (12, 6)

with MAGICC6() as magicc:
    res = magicc.run(rcp26)

plt.figure()
res.filter(variable="Emis*CO2*", region="World").line_plot(hue="variable")
plt.figure()
res.filter(variable="Atmos*Conc*CO2", region="World").line_plot(hue="variable");
