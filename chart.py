import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# making charts part

# all functions to draw graphs

# rating of similarity bar graph
def similarity_bar_graph(rating_df, root):
    fig, ax = plt.subplots(figsize=(4,3))
    modes = rating_df.mode().iloc[0]
    ax.bar(modes.index, modes.values)

    ax.set_xlabel('Currency')
    ax.set_ylabel('Rating')
    ax.set_title('Currencies similarity ratings')

    plt.xticks(rotation=45, ha='right')

    SMALL_SIZE = 5
    MEDIUM_SIZE = 7
    BIGGER_SIZE = 8

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
    fig, ax = plt.subplots(figsize=(4,3))
    ax.plot(df['Time Serie'], df[currency1], label=currency1)
    ax.plot(df['Time Serie'], df[currency2], label=currency2)

    plt.legend(loc='upper right')
    #max in currency value
    if df[currency1].max() > df[currency2].max():
        y_lim = df[currency1].max()
    else:
        y_lim = df[currency2].max()
    plt.ylim(0, y_lim + 10)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas


# rating of similarity corr heat map
def similarity_heatmap(rating_df, root):
    fig, ax = plt.subplots(figsize=(4,3))

    SMALL_SIZE = 5
    MEDIUM_SIZE = 7
    BIGGER_SIZE = 8

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
    fig, ax = plt.subplots(figsize=(4,3))
    plt.hist(df[currency1], label=currency1, alpha=0.5)
    plt.hist(df[currency2], label=currency2, alpha=0.5)

    plt.legend(loc='upper right')
    plt.title(f'Frequencyies of {currency1} and {currency2}')
    plt.ylabel('Frequency')

    SMALL_SIZE = 5
    MEDIUM_SIZE = 7
    BIGGER_SIZE = 8

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
