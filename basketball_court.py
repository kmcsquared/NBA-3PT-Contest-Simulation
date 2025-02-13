"""
This module provides functionality to draw a basketball court using Matplotlib.

Functions:
    draw_court(ax, color):
        Parameters:
            ax (matplotlib.axes.Axes): The axes on which to draw the court.
            color (str): The color of the court lines.
            show_ticks (bool): Show axes ticks if True, hide ticks if False
        Returns:
            None
"""

# The following code is taken from an article by Naveen Venkatesan
# Article: https://towardsdatascience.com/make-a-simple-nba-shot-chart-with-python-e5d70db45d0d
# Code: https://github.com/naveenv92/medium-articles/blob/master/articles/nba-shotchart/nba_shotchart.ipynb

from matplotlib.patches import Arc, Circle
from matplotlib import rcParams

# Function to draw basketball court
def draw_court(ax, color, show_ticks=False):
    """
    Draws the basketball court lines on the given axes.

    :param ax: The axes on which to draw the court.
    :type ax: matplotlib.axes.Axes
    :param color: The color of the court lines.
    :type color: str
    :return: None
    """

    # Draw short-corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # Draw 3PT arc
    ax.add_artist(
        Arc(
            xy=(0, 140),
            width=440,
            height=315,
            theta1=0,
            theta2=180,
            facecolor='none',
            edgecolor=color,
            lw=2
        )
    )

    # Draw lane and key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(Circle(xy=(0, 190), radius=60, facecolor='none', edgecolor=color, lw=2))

    # Draw rim
    ax.add_artist(Circle(xy=(0, 60), radius=15, facecolor='none', edgecolor=color, lw=2))
    # Draw backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    # Remove ticks if necessary
    if not show_ticks:
        ax.set_xticks([])
        ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(left=-250, right=250)
    ax.set_ylim(bottom=0, top=470)
    ax.invert_yaxis()

    # Define general plot parameters
    rcParams['font.family'] = 'Arial'
    rcParams['font.size'] = 18
    rcParams['axes.linewidth'] = 2
