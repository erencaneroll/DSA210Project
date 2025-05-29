import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
import os


df = pd.read_csv("historical_player_data.csv")

# data cleaning
df = df.dropna(subset=["Position", "Fantasy_Points"])

# average points
avg_points_by_position = df.groupby("Position")["Fantasy_Points"].mean().sort_values(ascending=False)

os.makedirs("figure", exist_ok=True)

# create and save the graph
plt.figure(figsize=(10, 6))
avg_points_by_position.plot(kind='bar', color='skyblue')
plt.title("Average Fantasy Points by Position")
plt.xlabel("Position")
plt.ylabel("Average Fantasy Points")
plt.xticks(rotation=0)
plt.tight_layout()

# show and save the graph
plt.savefig("figure/position_avg_points.png")
plt.show()

#preparing the groups for anova test
groups = [group["Fantasy_Points"].values for _, group in df.groupby("Position") if len(group) > 1]


anova_result = f_oneway(*groups)


print(f"\nANOVA p-değeri: {anova_result.pvalue:.5e}")


if anova_result.pvalue < 0.05:
    print("\nConclusion:")
    print("- There is a statistically significant difference in fantasy point contributions between positions.")
    print("- Null hypothesis (H0) is rejected.")
    print("- Player position significantly affects weekly fantasy performance.\n")
else:
    print("\nConclusion:")
    print("- No statistically significant difference was found between positions.")
    print("- Cannot reject the null hypothesis (H0).\n")