import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load sample dataset
df = sns.load_dataset("penguins")

print(df.head(10))

# Drop missing values
df = df.dropna()

print(df.head(10))
print(df.info())

# ---------------------------------------------------------
# STEP 1: CREATE A SCATTER PLOT
# ---------------------------------------------------------

plt.figure(figsize=(7, 5))

sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species"
)

plt.title("Scatter Plot: Bill Length vs. Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.show()

# ---------------------------------------------------------
# STEP 2: CREATE A CORRELATION HEATMAP
# ---------------------------------------------------------

plt.figure(figsize=(6, 5))

# Select only numerical columns
numeric_data = df.select_dtypes(include="number")

# Calculate correlation
correlation_matrix = numeric_data.corr()

# Draw heatmap
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="RdYlGn",       # RED = Negative, GREEN = Positive
    fmt=".2f",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Heatmap")
plt.show()
