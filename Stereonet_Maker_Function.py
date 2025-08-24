import pandas as pd
import mplstereonet
import matplotlib.pyplot as plt

def plot_stereonet():

    '''
    Plots a Stereonet from an csv file with 'Azimuth' and 'Dip' columns.
    csv_path: path to csv
    title: figure title
    caption: figure bottom description

    The csv file should be formatted like this:
       Azimuth  Dip
    0        x   x
    1        x   x
    2        x   x
    3        x   x
    4        x   x
    '''

    csv_path = input("Please copy csv path here: ")
    df = pd.read_csv(csv_path)

    azimuth = df["Azimuth"]
    dip = df["Dip"]

    plt.close('all')
    fig = plt.figure(figsize=(6, 6))
    # This is the blank canvas of the stereonet itself, therefore we only need one.

    ax = fig.add_subplot(111, projection='stereonet')
    # Eventually, the option to generate numerous stereonets at once will be available.

    for _, row in df.iterrows():
        # index is used to call upon those numbers on the left of the df.
        # df.iterrows() is used to call each row one at a time.

        strike = (row["Azimuth"] - 90) % 360
        dip = (row["Dip"])

        ax.plane(strike, dip, color="black", linestyle="-")
        # I made the stereonet pink, of course.

    ax.grid(True, color="lightgray", linestyle="--", linewidth=0.7, alpha=0.7)

    # This shows the N, E, S, W values to orientate the viewer.
    ax.text(0, 1.08, "N", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(1.08, 0, "E", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(0, -1.08, "S", ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(-1.08, 0, "W", ha="center", va="center", fontsize=12, fontweight="bold")

    # This adds text such as a title and a description.
    title = input("Please input a title (optional): ")
    if title:
        ax.set_title(title, ha="center", va="center", fontsize=14, pad=30)

    caption = input("Please input a caption (optional): ")
    if caption:
        fig.text(0.5, 0.02, caption, ha="center", fontsize=10, style="italic")
        
    else:
        plt.show()

print(plot_stereonet())