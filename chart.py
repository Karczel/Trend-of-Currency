import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# making charts part

# all functions to draw graphs

# rating of similarity bar graph
def similarity_bar_graph(rating_df, root):
    fig, ax = plt.subplots(figsize=(2,2))
    modes = rating_df.mode().iloc[0]
    ax.bar(modes.index, modes.values)

    ax.set_xlabel('Currency')
    ax.set_ylabel('Rating')
    ax.set_title('Currencies similarity ratings')

    plt.xticks(rotation=45, ha='right')

    SMALL_SIZE = 1
    MEDIUM_SIZE = 2
    BIGGER_SIZE = 3

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas


# exchange rate line graph
def exchange_rate_line_graph(df, currency1, currency2, root):
    fig, ax = plt.subplots(figsize=(2, 2))
    for i in df.columns[1:]:
        if i in [currency1, currency2]:
            ax.plot(df['Time Serie'], df[i], label=i)

    plt.legend(loc='upper right')
    plt.ylim(0, 2000)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas


# rating of similarity corr heat map
def similarity_heatmap(rating_df, root):
    fig, ax = plt.subplots(figsize=(2, 2))

    SMALL_SIZE = 1
    MEDIUM_SIZE = 2
    BIGGER_SIZE = 3

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    sns.heatmap(rating_df[rating_df.columns[1:]].corr(),
                square=True,
                linewidths=0.25,
                linecolor=(0, 0, 0),
                cmap=sns.color_palette("coolwarm"),
                annot=True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas


# comparison histogram
def compare_histogram(df, currency1, currency2, root):
    fig, ax = plt.subplots(figsize=(2, 2))
    for i in range(1, len(df.columns)):
        if df.columns[i] in [currency1, currency2]:
            plt.hist(df[df.columns[i]], label=df.columns[i], alpha=0.5)

    plt.legend(loc='upper right')
    plt.title(f'Frequencyies of {currency1} and {currency2}')
    plt.ylabel('Frequency')

    SMALL_SIZE = 1
    MEDIUM_SIZE = 2
    BIGGER_SIZE = 3

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas
