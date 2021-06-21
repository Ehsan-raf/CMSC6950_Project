from pymagicc import MAGICC6
from pymagicc import rcp26

import matplotlib.pyplot as plt

plt.style.use("bmh")

with MAGICC6() as magicc:
    results = magicc.run(rcp26)
    
plt.figure(figsize=(16, 9))
results.filter(variable="*Temperature*").line_plot(x="time");