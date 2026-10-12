import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Netflix_Final_Cleaned.csv")
# countplot()
sns.countplot(data=df,x="type")

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.show()

sns.countplot(data=df,x="rating",hue="type")

plt.xticks(rotation=45)

plt.title("Ratings by Content Type")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")

plt.show()
# barplot()
avg_duration = df.groupby("content_type")["duration_value"].mean().reset_index()

sns.barplot(data=avg_duration,x="content_type",y="duration_value")

plt.title("Average Duration by Content Type")
plt.xlabel("Content Type")
plt.ylabel("Average Duration")

plt.show()

# histplot()
sns.histplot(data=df,x="release_year",bins=20)

plt.title("Netflix Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()

# boxplot()
sns.boxplot(data=df,x="duration_value")

plt.title("Netflix Duration Distribution")
plt.xlabel("Duration")

plt.show()

# violinplot()
sns.violinplot(data=df,x="content_type",y="duration_value")

plt.title("Duration Distribution by Content Type")
plt.show()

# scatterplot()
sns.scatterplot(data=df,x="release_year",y="duration_value")

plt.title("Release Year vs Duration")
plt.xlabel("Release Year")
plt.ylabel("Duration")

plt.show()

# lineplot()
yearly_content = (df.groupby("release_year").size().reset_index(name="title_count"))

sns.lineplot(data=yearly_content,x="release_year",y="title_count",marker="o")

plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()

# hue
sns.countplot(data=df,x="rating",hue="type")

plt.xticks(rotation=45)
plt.title("Rating Distribution by Content Type")
plt.show()

# palette
sns.countplot(
    data=df,
    x="type",
    palette="Set2"
)


# order
rating_order = df["rating"].value_counts().head(10).index

sns.countplot(
    data=df,
    y="rating",
    order=rating_order
)

plt.title("Top 10 Netflix Ratings")
plt.show()

# heatmap()

numeric_df = df[["release_year", "added_year", "added_month", "duration_value"]]

correlation = numeric_df.corr()

sns.heatmap(correlation,annot=True,cmap="coolwarm")

plt.title("Netflix Numeric Feature Correlation")
plt.show()


# pairplot()

sns.pairplot(df[["release_year", "added_year", "added_month", "duration_value"]].dropna())

plt.show()

# jointplot()
sns.jointplot(
    data=df,
    x="release_year",
    y="duration_value",
    kind="scatter"
)

plt.show()

# catplot()
sns.catplot(
    data=df,
    x="type",
    hue="rating",
    kind="count"
)

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

movies = df[df["type"] == "Movie"]

sns.boxplot(
    data=movies,
    x="rating",
    y="duration_value"
)

plt.xticks(rotation=45)
plt.title("Movie Duration by Rating")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

movies = df[df["type"] == "Movie"]
sns.violinplot(data=movies,x="rating",y="duration_value")

plt.xticks(rotation=45)
plt.title("Movie Duration Distribution by Rating")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

yearly_content = df["release_year"].value_counts().sort_index()
sns.lineplot(x=yearly_content.index,y=yearly_content.values,marker="o")

plt.title("Netflix Titles Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()


year_type = pd.crosstab(df["release_year"],df["type"])
print(year_type)
sns.heatmap(year_type,annot=True,fmt="d")

plt.title("Movies vs TV Shows by Release Year")
plt.xlabel("Content Type")
plt.ylabel("Release Year")
plt.show()

sns.jointplot(
    data=movies,
    x="release_year",
    y="duration_value",
    kind="scatter"
)

plt.show()


top_ratings = df["rating"].value_counts().head(10).index

sns.countplot(data=df,x="rating",hue="type",order=top_ratings,palette="Set2")

plt.xticks(rotation=45)
plt.title("Top 10 Netflix Ratings: Movies vs TV Shows")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()


movies = df[df["type"] == "Movie"]
top_ratings = movies["rating"].value_counts().head(10).index

sns.barplot(data=movies,x="rating",y="duration_value",order=top_ratings,errorbar=None)

plt.xticks(rotation=45)
plt.title("Average Movie Duration by Top 10 Ratings")
plt.xlabel("Rating")
plt.ylabel("Average Duration (Minutes)")
plt.tight_layout()
plt.show()


rating_type = (df[df["rating"].isin(top_ratings)].groupby(["rating", "type"]).size().reset_index(name="count"))

sns.barplot(data=rating_type,x="rating",y="count",hue="type",order=top_ratings,errorbar=None)

plt.xticks(rotation=45)
plt.title("Netflix Titles by Rating and Type")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

g = sns.FacetGrid(df,col="type")
g.map(sns.histplot,"release_year")
plt.show()

g = sns.FacetGrid(df,col="type",hue="rating")
g.map(sns.scatterplot,"release_year","duration_value")

g.add_legend()

plt.show()

def custom_plot(data, **kwargs):

    # 1. Histogram banao
    sns.histplot(
        data=data,
        x="release_year",
        bins=15,
        **kwargs
    )

    # 2. Average release year nikalo
    avg_year = data["release_year"].mean()

    # 3. Average par vertical line
    plt.axvline(avg_year, linestyle="--")

    # 4. Average ko text ke form me show karo
    plt.text(
        avg_year,
        100,
        f"Average: {avg_year:.0f}"
    )


g = sns.FacetGrid(df,col="type")

g.map_dataframe(custom_plot)

plt.show()

year_type = (df.groupby(["release_year", "type"]).size().reset_index(name="count"))
year_type = year_type[year_type["release_year"] >= 2000]
plt.figure(figsize=(12, 6))
sns.lineplot(data=year_type,x="release_year",y="count",hue="type",marker="o",palette="Set2")
plt.title("Netflix Movies vs TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.show()

rating_type = (df.groupby(["rating", "type"]).size().reset_index(name="count"))
print(rating_type)

plt.figure(figsize=(12,7))
sns.barplot(data=rating_type,x="rating",y="count",hue="type",palette="Set2")

plt.title("Movies and TV Shows by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Movies and TV Shows")
plt.grid(True)
plt.tight_layout()
plt.show()

rating_order = (df["rating"]).value_counts().index

plt.figure(figsize=(12,7))

sns.barplot(data=rating_type,x="rating",y="count",hue="type",order=rating_order,hue_order=["Movie","TV Show"],palette="Set2",errorbar=None)

plt.title("Movies and TV shows by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Titles (counts)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 7))

sns.barplot(
    data=rating_type,
    x="rating",
    y="count",
    hue="type",
    order=rating_order,
    hue_order=["Movie", "TV Show"],
    palette="Set2",
    errorbar=None,
    dodge=True,
    width=0.8,
    fill=True,
    edgecolor="black",
    linewidth=1,
    alpha=0.8
)

plt.title("Movies and TV Shows by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 7))

sns.stripplot(data=df,x="type",y="release_year",hue="type",palette="Set2",jitter=True,size=4,alpha=0.6)

plt.title("Release Year Distribution by Type")
plt.xlabel("Type")
plt.ylabel("Release Year")
plt.grid(True)
plt.tight_layout()
plt.show()


sns.catplot(
    data=df,
    x="type",
    y="release_year",
    hue="type",
    kind="box",
    height=6,
    aspect=1.5
)

import seaborn as sns
import matplotlib.pyplot as plt

# Netflix data me sirf useful numerical columns
sample_df = df[["release_year", "duration_value", "type"]].dropna()

# Data ko chhota kar rahe hain taaki plots fast chale
sample_df = sample_df.sample(500, random_state=42)


# ==========================================================
# 1. PAIRGRID
# ==========================================================

g1 = sns.PairGrid(
    sample_df,
    vars=["release_year", "duration_value"],
    hue="type"
)

g1.map(sns.scatterplot)

g1.add_legend()

plt.show()


# ==========================================================
# 2. JOINTGRID
# ==========================================================

g2 = sns.JointGrid(
    data=sample_df,
    x="release_year",
    y="duration_value"
)

g2.plot(
    sns.scatterplot,
    sns.histplot
)

plt.show()


# ==========================================================
# 3. FACETGRID
# ==========================================================

g3 = sns.FacetGrid(
    sample_df,
    col="type",
    height=5,
    aspect=1.2
)

g3.map_dataframe(
    sns.scatterplot,
    x="release_year",
    y="duration_value"
)

g3.set_axis_labels(
    "Release Year",
    "Duration"
)

g3.set_titles("{col_name}")

plt.show()

rating_count = df["rating"].value_counts().reset_index()
rating_count.columns = ["rating", "count"]

print(rating_count)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=rating_count,
    x="rating",
    y="count",
    hue="rating",
    palette="Set2",
    legend=False
)

plt.title("Netflix Titles by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show()

year_count = (
    df["added_year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_count.columns = ["year", "count"]

print(year_count)

plt.figure(figsize=(12, 7))

sns.lineplot(
    data=year_count,
    x="year",
    y="count",
    marker="o"
)

plt.title("Netflix Titles Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.grid(True)
plt.tight_layout()
plt.show()