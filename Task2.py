import matplotlib.pyplot as plt
import pymagicc
from pymagicc import scenarios
from pymagicc import rcps
import scmdata

results = []
for scen in rcps.groupby("scenario"):
    results_scen = pymagicc.run(scen)
    results.append(results_scen)

results = scmdata.run_append(results)

temperature_rel_to_1850_1900 = (
    results
    .filter(variable="Surface Temperature", region="World")
    .relative_to_ref_period_mean(year=range(1850, 1900 + 1))
)

temperature_rel_to_1850_1900.lineplot()
plt.title("Global Mean Temperature Projection")
plt.ylabel("°C over pre-industrial (1850-1900 mean)");

