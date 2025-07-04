import pandas as pd
import numpy as np

file = "C:\\Users\\TEST\\Downloads\\business-operations-survey-2022-information-and-communications-technology.csv"
df = pd.read_csv(file,encoding ='ISO-8859-1')

df.to_csv("C:\\Users\\TEST\\Documents\\my_file.txt")

print(df)