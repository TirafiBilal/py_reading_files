import pandas as pd

data = []
with open ("C:\\Users\\TEST\\Documents\\file.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    parts = line.split(",")
    if len(parts) == 4:
        name = parts[0]
        status = parts[1]
        department = parts[2]
        age = parts[3]
        data.append([name, status, department, age])

df = pd.DataFrame(data)
print(df)
df.to_csv("C:\\Users\\TEST\\Documents\\file.csv")


