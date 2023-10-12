import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr, normaltest, pointbiserialr, shapiro
import os
from datetime import datetime

class DataScienceClass:
    def __init__(self, df):
        self.df = df

    def _calculate_correlation(self, var1, var2, method='pearson'):
        if method == 'pearson':
            corr, p_value = pearsonr(self.df[var1], self.df[var2])
        elif method == 'spearman':
            corr, p_value = spearmanr(self.df[var1], self.df[var2])
        else:
            raise ValueError("Invalid correlation method. Choose 'pearson' or 'spearman'.")
        return corr, p_value

    def _check_normality(self, df):
        flattened_data = df.values.flatten()
        _, p_value = shapiro(flattened_data)
        print(f"Normality check result: {'Normal' if p_value > 0.05 else 'Not Normal'} (p-value: {p_value:.3f})")
        return p_value > 0.05


    def _check_linearity(self, columns):
        for column1 in columns:
            for column2 in columns:
                if column1 != column2:
                    if np.issubdtype(self.df[column1].dtype, np.number) and np.issubdtype(self.df[column2].dtype, np.number):
                        correlation, _ = pearsonr(self.df[column1], self.df[column2])
                        if abs(correlation) < 0.3:
                            print(f"Linearity check result: Not Linear ({column1} - {column2} correlation: {correlation:.3f})")
                            return False
                    elif np.issubdtype(self.df[column1].dtype, np.number) and np.issubdtype(self.df[column2].dtype, np.object):
                        binary_column = self.df[column2].apply(lambda x: 1 if x == 'Yes' else 0)
                        correlation, _ = pointbiserialr(self.df[column1], binary_column)
                        if abs(correlation) < 0.3:
                            print(f"Linearity check result: Not Linear ({column1} - {column2} correlation: {correlation:.3f})")
                            return False
        print("Linearity check result: Linear")
        return True

    def select_best_correlation_method(self):
        is_normal = all(self._check_normality(self.df[column]) for column in self.df.columns)
        is_linear = self._check_linearity(self.df.columns)

        if is_normal and is_linear:
            best_method = 'pearson'
        else:
            best_method = 'spearman'

        print(f"Best correlation method for the dataset: {best_method.capitalize()}")
        return best_method

    def plot_annotated_heatmap(self, correlation_method='pearson', plot_title=None):
        corr_matrix = self.df.corr(method=correlation_method)

        plt.figure(figsize=(12, 10))  # Increase the figure size for clarity

        # Use seaborn to create a full square heatmap without a mask
        ax = sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt=".3f", annot_kws={"size": 10},
                         linewidths=0.5, square=True, cbar_kws={"shrink": 0.75}, vmin=-1, vmax=1)  # Set vmin and vmax

        # Add variable names at the center of the cells on the outside
        for i, var1 in enumerate(corr_matrix.columns):
            for j, var2 in enumerate(corr_matrix.columns):
                corr_value, p_value = self._calculate_correlation(var1, var2, method=correlation_method)

                if p_value < 0.001:
                    text = "{:.3f} ***".format(corr_value)
                elif p_value < 0.01:
                    text = "{:.3f} **".format(corr_value)
                elif p_value < 0.05:
                    text = "{:.3f} *".format(corr_value)
                else:
                    text = "{:.3f}".format(corr_value)

                plt.text(j + 0.5, i + 0.5, text, ha='center', va='center',
                         bbox=dict(facecolor='white', edgecolor='white', boxstyle='round,pad=0.3'))

        plt.xticks(np.arange(len(corr_matrix.columns)) + 0.5, corr_matrix.columns, rotation=45)
        plt.yticks(np.arange(len(corr_matrix.columns)) + 0.5, corr_matrix.columns, rotation=0)
        
        if plot_title:
            plt.title(plot_title, size=20)  # Set custom plot title if provided
            filename = f"{plot_title}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        else:
            plt.title(f"Annotated Heatmap of {correlation_method.capitalize()} Correlation")
            filename = f"heatmap_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

        # Save the plot as a high-resolution image in the script's directory
        plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename), dpi=300, bbox_inches='tight')
        plt.show()

# Example usage:

from sklearn.datasets import load_iris

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
ds_class = DataScienceClass(df)
#ds_class._check_linearity(df.columns)
#ds_class._check_normality(df)
best_correlation_method = ds_class.select_best_correlation_method()
ds_class.plot_annotated_heatmap(correlation_method=best_correlation_method, plot_title='Plotje')