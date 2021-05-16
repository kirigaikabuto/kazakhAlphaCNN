import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
print(df.head())
plt.figure(figsize = (10,10))
row, colums = 4, 4
for i in range(16):
    plt.subplot(colums, row, i + 1)
    plt.imshow(df.sample(50).iloc[i, 1:].values.reshape(28,28), cmap='Greys')
plt.show()