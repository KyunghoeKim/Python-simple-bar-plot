# This code draws beautiful bar graphs for you
# Specific format(.csv) required: ask KH for sample data
# Written by KH Kim, 04/16/18

import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



def read_all_csv_files(search_dir=None, ext='.csv'):
    work_dir = search_dir or os.getcwd()
    filenames = [f for f in os.listdir(work_dir) if f.endswith(ext)]
    for filename in filenames:
        df = pd.read_csv(os.path.join(work_dir, filename))
        for colname in df.columns:
            if df[colname].dtype == np.float64:
                ycol = colname
            elif df[colname].dtype == np.object:
                # convert string column into categorical type
                df[colname] = df[colname].astype('category')
                xcol = colname
        # return dataframe as well as filename (for saving figure), xcol and ycol
        yield (df, filename, xcol, ycol)

def barplot(df, filename, xcol, ycol, *, colors):
    fig, ax = plt.subplots(figsize=(3, 5))
    fig.dpi = 200
    
    x = df[xcol]
    y = df[ycol]
    data = []
    for i, category in enumerate(x.cat.categories):
        y_cat = y[x == category]
        estimated_mean = y_cat.mean()
        estimated_std = y_cat.std() / (len(y_cat) - 1)
        data.append([estimated_mean, 0., estimated_std])

    # Convert data to np array and transpose it (.T part) 
    data = np.array(data).T

    # Use category string value directily for x values (instead of np.arange)
    ax.bar(x.cat.categories, data[0],
           color=colors,
           yerr=data[1:],
           error_kw=dict(
               elinewidth=2,
               capsize=8,
               capthick=1.5))
    sns.swarmplot(x=xcol, y=ycol, data=df, color='black')

    # disable right and top axis spine (plot frame)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

# always wrap scripts within `if __name__ == '__main__':`
if __name__ == '__main__':
    for args in read_all_csv_files():
        barplot(*args, colors=[(0, 168/255, 1), '0.3'])
