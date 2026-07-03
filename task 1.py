import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")

plt.figure(figsize=(8,5))
plt.hist(df['Age'], bins=10)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")

gender_counts = df['Gender'].value_counts()

plt.figure(figsize=(6,4))
gender_counts.plot(kind='bar')

plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("world_population.csv")

top10 = df.sort_values('2022 Population', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top10['Country/Territory'], top10['2022 Population'])

plt.title('Top 10 Most Populated Countries (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")

plt.figure(figsize=(8,5))
plt.hist(df['Age'], bins=10)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)

plt.show()

