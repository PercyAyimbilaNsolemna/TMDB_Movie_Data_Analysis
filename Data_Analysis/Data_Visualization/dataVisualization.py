import pandas as pd
import matplotlib.pyplot as plt

def trendVisuals(data: pd.DataFrame, column1: str, column2: str, title:str):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[column1], data[column2])
    plt.xlabel(f"{column1.upper()}")
    plt.ylabel(f"{column2.upper()}")
    plt.title(f"{title}")
    plt.show()



def plot_yearly_box_office_trends(data: pd.DataFrame):
    data['release_year'] = pd.to_datetime(data['release_date']).dt.year
    yearly = data.groupby("release_year")["revenue_musd"].mean()

    plt.figure(figsize=(10, 5))
    plt.plot(yearly.index, yearly.values)
    plt.xlabel("Year")
    plt.ylabel("Average Revenue")
    plt.title("Yearly Box Office Performance")
    plt.grid(True)
    plt.show()


def plot_franchise_vs_standalone(data: pd.DataFrame):
    stats = data.agg(
        mean_revenue=("revenue_musd", "mean"),
        mean_budget=("budget_musd", "mean"),
        mean_rating=("vote_average", "mean"),
        mean_ROI=("ROI", "mean")
    )

    stats.plot(kind="bar", figsize=(10, 6))
    plt.title("Franchise vs Standalone Movie Success Metrics")
    plt.xlabel("Group")
    plt.ylabel("Value")
    plt.xticks(rotation=0)
    plt.grid(True)
    plt.tight_layout()
    plt.show()






def main():
    ...



if __name__ == "__main__":
    main()