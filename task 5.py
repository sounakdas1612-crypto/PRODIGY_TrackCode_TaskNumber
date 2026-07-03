import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "US_Accidents_March23.csv",
    usecols=[
        "Severity",
        "Start_Time",
        "Weather_Condition",
        "State",
        "Start_Lat",
        "Start_Lng"
    ],
    low_memory=False
)

print(df.head())

df = df.dropna()

df["Start_Time"] = pd.to_datetime(df["Start_Time"])

df["Hour"] = df["Start_Time"].dt.hour

plt.figure(figsize=(6,4))

df["Severity"].value_counts().sort_index().plot.bar()

plt.title("Accident Severity")

plt.show()

plt.figure(figsize=(10,5))

df["Weather_Condition"].value_counts().head(10).plot.bar()

plt.title("Top Weather Conditions")

plt.xticks(rotation=45)

plt.show()

plt.figure(figsize=(10,5))

df.groupby("Hour").size().plot()

plt.title("Accidents by Hour")

plt.grid()

plt.show()

plt.figure(figsize=(10,5))

df["State"].value_counts().head(10).plot.bar()

plt.title("Top States")

plt.show()

sample = df.sample(5000, random_state=42)

plt.figure(figsize=(8,6))

plt.scatter(
    sample["Start_Lng"],
    sample["Start_Lat"],
    s=2
)

plt.title("Accident Hotspots")

plt.xlabel("Longitude")

plt.ylabel("Latitude")

plt.show()

print("Task Completed Successfully")
