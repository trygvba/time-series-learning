"""
To compare the earthquake and explosion signals, plot the data displayed in
figure 1.7 on the same graph using different colors or different line types and
comment on the results.
"""
import matplotlib.pyplot as plt
from src import utils
import os

data_dir = os.getenv("TIME_SERIES_DATA")
# Read data:
earthquake = utils.read_rdata(data_dir + "/EQ5.rda")
explosion = utils.read_rdata(data_dir + "/EXP6.rda")

# Plot the stuff:
plt.figure()
earthquake["EQ5"].plot(legend=True, color="k", linewidth=0.5,)
explosion["EXP6"].plot(legend=True, color="r", linewidth=0.5, style=["--"])
plt.show()
