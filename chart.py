import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def similarity_bar_graph(currency1, rating_df, root):
    try:
        plt.close(root.fig)
    except AttributeError:
        pass
    SMALL_SIZE = 2
    MEDIUM_SIZE = 3
    BIGGER_SIZE = 5

    plt.rc('font', size=BIGGER_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    fig, ax = plt.subplots(figsize=(3.1, 2.7))
    modes = (rating_df.loc[:, rating_df.columns != currency1]).mode().iloc[0]
    x = [i.split(' - ')[1] if ' - ' in i else i for i in modes.index]
    x = [i.replace(" ", "\n") if " " in i else i for i in x]
    y = modes.values
    ax.barh(x, y)

    plt.xticks(np.linspace(-2, 2, 5))

    ax.set_xlabel('Currency')
    ax.set_ylabel('Rating')
    ax.set_title(f'Currencies similarity ratings compared to {currency1}')

    # plt.xticks(rotation=90, ha='right')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas, fig


# exchange rate line graph
def exchange_rate_line_graph(df, currency1, currency2, root):
    try:
        plt.close(root.fig)
    except AttributeError:
        pass
    SMALL_SIZE = 3
    MEDIUM_SIZE = 5
    BIGGER_SIZE = 6

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    fig, ax = plt.subplots(figsize=(3.1, 2.7))
    ax.plot(df['Time Serie'], df[currency1], label=currency1)
    ax.plot(df['Time Serie'], df[currency2], label=currency2)

    plt.xlabel('Time Serie')
    plt.ylabel('Exchange Rate')
    plt.title(f'Trend of Currency of {currency1} and {currency2}')

    plt.legend(loc='upper right')
    # max in currency value
    if df[currency1].max() > df[currency2].max():
        y_lim = df[currency1].max()
    else:
        y_lim = df[currency2].max()
    plt.ylim(0, y_lim + 10)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas, fig


# rating of similarity corr heat map
def similarity_heatmap(rating_df, root):
    try:
        plt.close(root.fig)
    except AttributeError:
        pass
    SMALL_SIZE = 2
    MEDIUM_SIZE = 2
    BIGGER_SIZE = 3

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    plt.title(f'Correlation Heat map of ratings of similarity')
    plt.yticks(rotation=30, ha='right')
    plt.xticks(rotation=20, ha='right')

    fig, ax = plt.subplots(figsize=(3.2, 2.7))
    x = [i.split(' - ')[1] if ' - ' in i else i for i in rating_df.columns]
    x = [i.replace(" ", "\n") if " " in i else i for i in x]
    sns.heatmap(rating_df[rating_df.columns].corr(),
                square=True,
                linewidths=0.25,
                linecolor=(0, 0, 0),
                cmap=sns.color_palette("coolwarm"),
                annot=True,
                xticklabels=x,
                yticklabels=x)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas, fig


# comparison histogram
def compare_histogram(df, currency1, currency2, root):
    try:
        plt.close(root.fig)
    except AttributeError:
        pass
    SMALL_SIZE = 3
    MEDIUM_SIZE = 5
    BIGGER_SIZE = 6

    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    fig, ax = plt.subplots(figsize=(3.1, 2.7))
    plt.hist(df[currency1], label=currency1, alpha=0.5)
    plt.hist(df[currency2], label=currency2, alpha=0.5)

    plt.legend(loc='upper right')
    plt.title(f'Frequencyies of {currency1} and {currency2}')
    plt.xlabel('Exchange Rate')
    plt.ylabel('Frequency')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    return canvas, fig
