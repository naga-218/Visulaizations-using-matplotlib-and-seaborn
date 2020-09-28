#!/usr/bin/env python
# coding: utf-8

# In[1]:


class plots():
    
    def __init__(self):
        self.df = None
    
    
    # Heatmap 
    def half_masked_corr_heatmap(self, df, title = None):
        plt.figure(figsize=(10,10))
        sns.set(font_scale=1)

        corr = df.corr()

        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True

        with sns.axes_style("white"):
            sns.heatmap(corr, mask = mask, annot= True, cmap='coolwarm')
    
        if title: plt.title(f'\n{title}\n', fontsize = 18) 
        plt.show();  
    
        return


    # Heatmap with target variable
    def corr_to_target(self, df, target, title = None):
        plt.figure(figsize=(4, 6))
        sns.set(font_scale=1)
    
        corr = df.corr()[[target]].sort_values(target, 
                                                 ascending = False)[1:]
    
        sns.heatmap(corr, annot= True, cmap = 'coolwarm')
    
        if title: plt.title(f'\n{title}\n', fontsize = 18)
        plt.show();
    
        return
    
    
    # Scatteplot
    def gen_scatterplots(self, df, target_column, list_of_columns, cols = 1):

        rows = math.ceil(len(list_of_columns)/cols)
        figwidth  = 5 * cols
        figheight = 4 * rows

        fig, ax = plt.subplots(nrows=rows,
                              ncols= cols,
                              figsize = (figwidth, figheight))

        color_choices = ['blue', 'grey', 'goldenrod','r', 'black', 'darkorange', 'g']

        plt.subplots_adjust(wspace=0.3, hspace=0.3)
        ax = ax.ravel()  # Ravel turns a matrix into a vector... easier to iterate

        for i, column in enumerate(list_of_columns):
            ax[i].scatter(df[column], 
                         df[target_column],
                         color = color_choices[i % len(color_choices)],
                         alpha = 0.1)


            ax[i].set_ylabel(f'{target_column}', fontsize = 14)
            ax[i].set_xlabel(f'{column}', fontsize = 14)

        plt.show();
        return
    
    
    # Histogram
    def gen_histograms(self, df, cols = 1):
        rows = math.ceil(len(df.columns)/cols)

        fig, ax = plt.subplots(nrows = rows, ncols = cols, figsize = (15, 12))
        ax = ax.ravel()

        for i, col in enumerate(df.columns): 
            ax[i].hist(df[col], alpha = 1)

            ax[i].set_title(f'{df[col].name}', fontsize = 18)
            ax[i].set_ylabel('Observations', fontsize = 14)
            ax[i].set_xlabel('', fontsize = 14)

        plt.show()

        return
    
    
    # Boxplot
    def gen_boxplots(self, df, cols = 1):
        rows = math.ceil(len(df.columns)/cols)

        fig, ax = plt.subplots(nrows= rows, ncols= cols, figsize = (15, 12))
        ax = ax.ravel()

        for i, col in enumerate(df.columns):
            ax[i].boxplot(x = df[col])

            ax[i].set_title(f'{df[col].name}', fontsize = 18)

        plt.show()

        return
    
    
    # Linecharts
    def gen_linecharts(self, df, cols = 1):
        rows = math.ceil(len(df.columns)/cols)

        fig, ax = plt.subplots(nrows= rows, ncols= cols, figsize = (15, 12))
        ax = ax.ravel()

        for i, col in enumerate(df.columns):
            ax[i].plot(df[col])

            ax[i].set_title(f'{df[col].name}', fontsize = 18)

        plt.show()

        return
    
    
    # Linecharts with rolling
    def gen_linecharts_rolling(self, df, roll_num, cols = 1):
        rows = math.ceil(len(df.columns)/cols)

        df = df.rolling(roll_num).mean()

        fig, ax = plt.subplots(nrows= rows, ncols= cols, figsize = (15, 12))
        ax = ax.ravel()

        for i, col in enumerate(df.columns):
            ax[i].plot(df[col])

            ax[i].set_title(f'{col}', fontsize = 18)

        plt.show()

        return


# In[ ]:





# In[ ]:




