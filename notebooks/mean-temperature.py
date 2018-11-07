import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('Qt4Agg')

import os
data_folder = "C:\\Users\\jeroe\\PycharmProjects\\PythonDataScienceWorkshops\\data"
os.chdir(data_folder)

temp = pd.read_csv("mean_temperature.csv", delimiter="\t", header=None)
print(temp.head())