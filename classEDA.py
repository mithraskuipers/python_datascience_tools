import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class EDA:
	def __init__(self, df):
		self.df = df

	def shape(self):
		return self.df.shape

	def head(self, n=5):
		return self.df.head(n)

	def tail(self, n=5):
		return self.df.tail(n)

	def info(self):
		return self.df.info()

	def describe(self):
		return self.df.describe()

	def missing_values(self):
		return self.df.isnull().sum()

	def plot_histograms(self, columns=None, bins=10, figsize=(12,6)):
		if not columns:
			columns = self.df.columns
		for col in columns:
			self.df[col].hist(bins=bins, figsize=figsize)
			plt.title(col)
			plt.show()

	def plot_density_plots(self, columns=None, figsize=(12,6)):
		if not columns:
			columns = self.df.columns
		for col in columns:
			self.df[col].plot.density(figsize=figsize)
			plt.title(col)
			plt.show()

	def plot_box_plots(self, columns=None, figsize=(12,6)):
		if not columns:
			columns = self.df.columns
		for col in columns:
			self.df[col].plot.box(figsize=figsize)
			plt.title(col)
			plt.show()

	def plot_scatter_matrix(self, columns=None, figsize=(12,12)):
		if not columns:
			columns = self.df.columns
		sns.pairplot(self.df[columns], diag_kind="hist", plot_kws={'alpha': 0.6, 's': 30, 'edgecolor': 'k'}, size=2, aspect=1)
		plt.show()

	def plot_correlation_matrix(self, figsize=(12,12)):
		corr = self.df.corr()
		sns.heatmap(corr, annot=True, cmap="YlGnBu", vmin=-1, vmax=1, fmt=".2f")
		plt.show()
		
	def unique_values(self, column):
		return self.df[column].nunique()

	def value_counts(self, column, normalize=False):
		return self.df[column].value_counts(normalize)

	def plot_value_counts(self, column, figsize=(12,6), title=None):
		value_counts = self.df[column].value_counts()
		value_counts.plot.bar(figsize=figsize)
		plt.title(title if title else "Value Counts for {}".format(column))

	def plot_bar_chart(self, x, y, figsize=(12,6), title=None):
		self.df.plot.bar(x=x, y=y, figsize=figsize)
		plt.title(title if title else "Bar Chart of {} vs {}".format(y, x))
		plt.show()

	def plot_line_chart(self, x, y, figsize=(12,6), title=None):
		self.df.plot.line(x=x, y=y, figsize=figsize)
		plt.title(title if title else "Line Chart of {} vs {}".format(y, x))
		plt.show()

	def plot_pie_chart(self, column, figsize=(12,6), title=None):
		self.df[column].value_counts().plot.pie(autopct='%1.1f%%', figsize=figsize)
		plt.title(title if title else "Pie Chart of {}".format(column))
		plt.show()

	def plot_hist_and_density(self, column, bins=10, figsize=(12,6), title=None):
		fig, ax = plt.subplots(nrows=1, ncols=2, figsize=figsize)
		self.df[column].plot.hist(bins=bins, ax=ax[0], edgecolor='black')
		self.df[column].plot.density(ax=ax[1], color='red')
		ax[0].set_title("Histogram of {}".format(column))
		ax[1].set_title("Density Plot of {}".format(column))
		plt.show()

	def plot_pairplot(self, columns=None, hue=None, diag_kind='hist', figsize=(12,12), title=None):
		sns.pairplot(self.df[columns], hue=hue, diag_kind=diag_kind, height=2, aspect=1)
		plt.title(title if title else "Pairplot of {}".format(columns))
		plt.show()

	def plot_scatter_plot(self, x, y, figsize=(12,6), title=None):
		self.df.plot.scatter(x=x, y=y, figsize=figsize)
		plt.title(title if title else "Scatter Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_box_plot(self, x, y, figsize=(12,6), title=None):
		self.df.plot.box(x=x, y=y, figsize=figsize)
		plt.title(title if title else "Box Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_violin_plot(self, x, y, figsize=(12,6), title=None):
		sns.violinplot(x=x, y=y, data=self.df)
		plt.title(title if title else "Violin Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_swarm_plot(self, x, y, figsize=(12,6), title=None):
		sns.swarmplot(x=x, y=y, data=self.df)
		plt.title(title if title else "Swarm Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_heatmap(self, figsize=(12,12), title=None):
		sns.heatmap(self.df.corr(), annot=True)
		plt.title(title if title else "Heatmap of Correlation Matrix")
		plt.show()

	def plot_count_plot(self, x, figsize=(12,6), title=None):
		sns.countplot(x=x, data=self.df)
		plt.title(title if title else "Count Plot of {}".format(x))
		plt.show()

	def plot_joint_plot(self, x, y, kind='scatter', figsize=(12,6), title=None):
		sns.jointplot(x=x, y=y, data=self.df, kind=kind)
		plt.title(title if title else "Joint Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_histogram(self, col, figsize=(12,6), title=None):
		plt.figure(figsize=figsize)
		self.df[col].plot.hist()
		plt.title(title if title else "Histogram of {}".format(col))
		plt.show()

	def plot_density_plot(self, col, figsize=(12,6), title=None):
		plt.figure(figsize=figsize)
		self.df[col].plot.density()
		plt.title(title if title else "Density Plot of {}".format(col))
		plt.show()

	def plot_bar_plot(self, x, y, figsize=(12,6), title=None):
		plt.figure(figsize=figsize)
		self.df.plot.bar(x=x, y=y)
		plt.title(title if title else "Bar Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_line_plot(self, x, y, figsize=(12,6), title=None):
		plt.figure(figsize=figsize)
		self.df.plot.line(x=x, y=y)
		plt.title(title if title else "Line Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_area_plot(self, x, y, figsize=(12,6), title=None):
		plt.figure(figsize=figsize)
		self.df.plot.area(x=x, y=y)
		plt.title(title if title else "Area Plot of {} vs {}".format(y, x))
		plt.show()

	def plot_scatter_plot(self, x, y, figsize=(12,6), title=None):
		plt.figure(figsize=figsize)
		self.df.plot.scatter(x=x, y=y)
		plt.title(title if title else "Scatter Plot of {} vs {}".format(y, x))
		plt.show()
