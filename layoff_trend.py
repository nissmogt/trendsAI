import pandas as pd
import matplotlib.pyplot as plt


def load_data(data_path, col_label):
    df = pd.read_csv(data_path, header=0)
    if col_label:
        return df.drop(col_label, axis=1)
    else:
        return df


# define function to process layoff data
def process_layoff_data(df):
    df.Reported_date = pd.to_datetime(df.Reported_date)
    # removes unclear elements from layoff data
    df_filter = df[df["Num_layoffs"] != "Unclear"]
    df_filter = df_filter.dropna()
    df_filter.reset_index(drop=True, inplace=True)

    for i, elem in df_filter["Num_layoffs"].iteritems():
        if "," in elem:
            df_filter["Num_layoffs"][i] = int(elem.replace(",", ""))
        else:
            df_filter["Num_layoffs"][i] = int(elem)

    return df_filter


def plot_layoffs_by_date(df):
    # calculate rolling average of layoffs with a window of 4 months
    w = 4
    df["Rolling_Avg"] = df["Num_layoffs"].rolling(window=w).mean()

    # display publication-quality font formatting
    plt.rcParams["font.family"] = "Helvetica"
    # define function to plot number of layoffs by date
    plt.figure(0, figsize=(10, 5), dpi=100, facecolor="w", edgecolor="k")
    # plot rolling average
    plt.plot(df["Reported_date"], df["Rolling_Avg"], color="black", linestyle="-", linewidth=2,
             label="Rolling Avg (every {} months)".format(w), alpha=0.5)
    plt.scatter(df["Reported_date"], df["Num_layoffs"], label="company layoffs", color="xkcd:blue")
    # show where Meta data point is
    plt.scatter(df[df["Company"] == "Meta"]["Reported_date"],
                df[df["Company"] == "Meta"].Num_layoffs, label="Meta", color="xkcd:orangered", marker="*", s=100)
    plt.title("Layoffs in Tech - 2022")
    plt.xlabel("Date")
    plt.ylabel("Number of Layoffs")
    plt.legend(loc="best")
    plt.semilogy()
    plt.grid(which="both", axis="both", alpha=0.2)
    # save figure as png image with dpi of 200 to plots folder
    plt.savefig("plots/layoffs_by_date.png", dpi=200)
    plt.show()


raw_data = 'crunchbase_notable_layoffs.csv'
df_layoffs = load_data(raw_data, "Notes")
df_processed = process_layoff_data(df_layoffs)
# print df_processed Num_layoffs statistics
x = [df_processed["Num_layoffs"].max(), df_processed["Num_layoffs"].min(), df_processed["Num_layoffs"].mean(),
     df_processed["Num_layoffs"].median(), df_processed["Num_layoffs"].std()]
# print argmax and argmin of Num_layoffs
print("Max layoffs: {}, Min layoffs: {}".format(df_processed["Num_layoffs"].argmax(),df_processed["Num_layoffs"].argmin()))

print("Max: {}\n Min: {}\n Mean: {}\n Median: {}\n Std: {}".format(*x))
plot_layoffs_by_date(df_processed)