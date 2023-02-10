import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

class VarAnalyzer:
	def __init__(self, data, column_name):
		self.data = data
		self.column_name = column_name

	def missing_values(self):
		return self.data[self.column_name].isnull().sum()

	def outliers(self):
		data = self.data[self.column_name].dropna()
		q1, q3 = data.quantile(0.25), data.quantile(0.75)
		iqr = q3 - q1
		lower_bound = q1 - (1.5 * iqr)
		upper_bound = q3 + (1.5 * iqr)
		return len(data[(data < lower_bound) | (data > upper_bound)])

	def summary_statistics(self):
		return self.data[self.column_name].describe()

	def distribution_plot(self):
		sns.distplot(self.data[self.column_name].dropna(), kde=True, norm_hist=True)
		plt.show()

	def skewness(self):
		return stats.skew(self.data[self.column_name].dropna())

	def kurtosis(self):
		return stats.kurtosis(self.data[self.column_name].dropna())

	def normality_test(self):
		return stats.normaltest(self.data[self.column_name].dropna())

	def generate_report(self):
		report = 'Data Report for Column: {}\n'.format(self.column_name)
		report += 'Number of missing values: {}\n'.format(self.missing_values())
		report += 'Number of outliers: {}\n'.format(self.outliers())
		report += 'Summary Statistics:\n{}\n'.format(self.summary_statistics())
		report += 'Skewness: {}\n'.format(self.skewness())
		report += 'Kurtosis: {}\n'.format(self.kurtosis())
		normality_test_result = self.normality_test()
		report += 'Normality Test Statistic: {}\n'.format(normality_test_result[0])
		report += 'Normality Test p-value: {}\n'.format(normality_test_result[1])
		if self.skewness() > 0.5 or self.kurtosis() > 3:
			report += 'The data is not normally distributed.\n'
			report += 'Advice: Consider transforming the data using log or square root transformation to reduce skewness and kurtosis.\n'
		else:
			report += 'The data is normally distributed.\n'
		return report