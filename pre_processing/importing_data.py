import pandas as pd

#Importing the data set
dataset = pd.read_csv('./data/pre_processing_data.csv');
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values
