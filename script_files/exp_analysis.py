import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

print('testing a sample of the data')
df = pd.read_csv("data/amaretto_dataset_anon.csv", nrows=500000)

#Changing to datetime format
print(df.columns)
print(df.head())
