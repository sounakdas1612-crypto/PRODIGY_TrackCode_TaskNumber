
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Tweets.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

df = df.dropna(subset=["text","airline_sentiment"])

# Graph 1 - Sentiment Distribution

plt.figure(figsize=(6,4))

df["airline_sentiment"].value_counts().plot(kind="bar")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()

# Graph 2 - Pie Chart

plt.figure(figsize=(6,6))

df["airline_sentiment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Sentiment Percentage")

plt.show()

# Graph 3 - Airlines Count

plt.figure(figsize=(8,5))

df["airline"].value_counts().plot(kind="bar")

plt.title("Tweets by Airline")

plt.xlabel("Airline")

plt.ylabel("Count")

plt.xticks(rotation=30)

plt.show()

# Graph 4 - Sentiment by Airline

pd.crosstab(df["airline"],df["airline_sentiment"]).plot(
    kind="bar",
    figsize=(9,5)
)

plt.title("Sentiment by Airline")

plt.xlabel("Airline")

plt.ylabel("Count")

plt.xticks(rotation=30)

plt.show()

# Graph 5 - Tweet Length

df["Tweet_Length"]=df["text"].astype(str).apply(len)

plt.figure(figsize=(8,4))

plt.hist(df["Tweet_Length"],bins=30)

plt.title("Tweet Length Distribution")

plt.xlabel("Tweet Length")

plt.ylabel("Frequency")

plt.show()

# Graph 6 - Average Tweet Length

df.groupby("airline_sentiment")["Tweet_Length"].mean().plot(kind="bar")

plt.title("Average Tweet Length by Sentiment")

plt.xlabel("Sentiment")

plt.ylabel("Average Length")

plt.show()

print("\n========== KEY FINDINGS ==========")
print("1. Dataset cleaned successfully.")
print("2. Sentiment distribution analyzed.")
print("3. Airline-wise sentiment visualized.")
print("4. Tweet length analyzed.")
print("5. Public opinion compared across airlines.")
