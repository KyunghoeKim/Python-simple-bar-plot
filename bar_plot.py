# This code draws beautiful bar graphs for you
# Specific format(.csv) required: ask KH for sample data
# Written by KH Kim, 04/16/18

#def bar_plot(filename = 'Datasheet2', xlabel = 'Group', ylabel = 'Stimulation time (s)'):

import os

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Handle variables
filename = 'Datasheet2'
xlabel = 'Group'
ylabel = 'Distance moved (cm)'
expGroupName = 'ChR2'
ctrlGroupName = 'eYFP'

xtickLabel = [expGroupName, ctrlGroupName]
pos = np.arange(len(xtickLabel))

# Initialize file information
dirname = "C:\\1\\"
ext = '.csv'
filename = os.path.join(dirname, filename + ext)

# Read csv file and classify
df = pd.read_csv(filename)
df_exp = df.loc[df[xlabel] == expGroupName]
df_ctrl = df.loc[df[xlabel] != expGroupName]

# Statistics
mean_exp = df_exp[ylabel].mean()
mean_ctrl = df_ctrl[ylabel].mean()

std_exp = df_exp[ylabel].std()
std_ctrl = df_ctrl[ylabel].std()

totalNumMouse = df.shape[0]
expNumMouse = df_exp.shape[0]
ctrlNumMouse = df_ctrl.shape[0]

ste_exp = std_exp / np.sqrt(expNumMouse)
ste_ctrl = std_ctrl / np.sqrt(ctrlNumMouse)

# For plot
means = [mean_exp, mean_ctrl]
stes = np.array([[0, 0], [ste_exp, ste_ctrl]])

# Plot
fig, ax = plt.subplots(figsize = (3, 5))
ax.bar(pos, means, color = [(0, 168/255, 1), '0.3'],
       yerr = stes,
       error_kw = dict(elinewidth = 2, capsize = 8, capthick = 1.5))
sns.swarmplot(x = xlabel, y = ylabel, data = df, color = 'black')

ax.set_xticks(pos)
ax.set_xticklabels(xtickLabel)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
fig.show()

