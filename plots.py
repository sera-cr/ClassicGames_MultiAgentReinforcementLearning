import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd


def q_learning_tictactoe_execution_time():
    # Q LEARNING TICTACTOE EXECUTION TIMES
    execution_times = [34.45, 31.89, 31.91, 34.43, 35.48, 34.90, 40.28, 69.70, 80.89, 114.93, 137.08, 178.13, 206.78,
                       231.38, 276.46]
    x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

    execution_times_series = pd.Series(execution_times)
    # Plot the figures
    # figure size
    plt.figure(figsize=(12, 8))
    # creating the plot
    ax = execution_times_series.plot(kind="bar", color="tab:blue")
    # plot title
    ax.set_title("Execution times Q-Learning in TicTacToe")
    ax.set_xlabel("Configurations")
    ax.set_ylabel("Execution time (s)")
    ax.set_xticklabels(x_labels)

    rects = ax.patches

    labels = [str(x) for x in execution_times]

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
        )

    # adding in red the elements with roulette wheel
    ax.get_children()[6].set_color('tab:red')
    ax.get_children()[8].set_color('tab:red')
    ax.get_children()[10].set_color('tab:red')
    ax.get_children()[12].set_color('tab:red')
    ax.get_children()[14].set_color('tab:red')

    red_patch = mpatches.Patch(color='tab:red', label='Using Roulette Wheel')
    blue_patch = mpatches.Patch(color='tab:blue', label='Not Using Roulette Wheel')
    ax.legend(handles=[blue_patch, red_patch])

    plt.show()


def sarsa_tictactoe_execution_time():
    # SARSA TICTACTOE EXECUTION TIMES
    execution_times = [34.25, 31.93, 32.07, 34.63, 34.26, 35.05, 40.93, 67.93, 79.84, 117.60, 131.78, 170.78, 205.05,
                       230.32, 272.81]
    x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

    execution_times_series = pd.Series(execution_times)
    # Plot the figures
    # figure size
    plt.figure(figsize=(12, 8))
    # creating the plot
    ax = execution_times_series.plot(kind="bar", color="tab:blue")
    # plot title
    ax.set_title("Execution times SARSA in TicTacToe")
    ax.set_xlabel("Configurations")
    ax.set_ylabel("Execution time (s)")
    ax.set_xticklabels(x_labels)

    rects = ax.patches

    labels = [str(x) for x in execution_times]

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
        )

    # adding in red the elements with roulette wheel
    ax.get_children()[6].set_color('tab:red')
    ax.get_children()[8].set_color('tab:red')
    ax.get_children()[10].set_color('tab:red')
    ax.get_children()[12].set_color('tab:red')
    ax.get_children()[14].set_color('tab:red')

    red_patch = mpatches.Patch(color='tab:red', label='Using Roulette Wheel')
    blue_patch = mpatches.Patch(color='tab:blue', label='Not Using Roulette Wheel')
    ax.legend(handles=[blue_patch, red_patch])

    plt.show()


def q_learning_connect4_execution_time():
    # Q LEARNING CONNECT4 EXECUTION TIMES
    execution_times = [105.77, 109.27, 109.88, 108.67, 109.34, 105.86, 111.09, 213.87, 213.03, 352.97, 364.44, 530.13,
                       540.70, 702.29, 711.59]
    x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

    execution_times_series = pd.Series(execution_times)
    # Plot the figures
    # figure size
    plt.figure(figsize=(12, 8))
    # creating the plot
    ax = execution_times_series.plot(kind="bar", color="tab:blue")
    # plot title
    ax.set_title("Execution times Q-Learning in Connect4")
    ax.set_xlabel("Configurations")
    ax.set_ylabel("Execution time (s)")
    ax.set_xticklabels(x_labels)

    rects = ax.patches

    labels = [str(x) for x in execution_times]

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
        )

    # adding in red the elements with roulette wheel
    ax.get_children()[6].set_color('tab:red')
    ax.get_children()[8].set_color('tab:red')
    ax.get_children()[10].set_color('tab:red')
    ax.get_children()[12].set_color('tab:red')
    ax.get_children()[14].set_color('tab:red')

    red_patch = mpatches.Patch(color='tab:red', label='Using Roulette Wheel')
    blue_patch = mpatches.Patch(color='tab:blue', label='Not Using Roulette Wheel')
    ax.legend(handles=[blue_patch, red_patch])

    plt.show()


def sarsa_connect4_execution_time():
    # SARSA CONNECT4 EXECUTION TIMES
    execution_times = [105.94, 104.93, 105.48, 103.23, 104.01, 104.79, 105.82, 211.64, 210.11, 349.57, 352.16, 523.70,
                       533.00, 705.31, 686.01]
    x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

    execution_times_series = pd.Series(execution_times)
    # Plot the figures
    # figure size
    plt.figure(figsize=(12, 8))
    # creating the plot
    ax = execution_times_series.plot(kind="bar", color="tab:blue")
    # plot title
    ax.set_title("Execution times SARSA in Connect4")
    ax.set_xlabel("Configurations")
    ax.set_ylabel("Execution time (s)")
    ax.set_xticklabels(x_labels)

    rects = ax.patches

    labels = [str(x) for x in execution_times]

    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
        )

    # adding in red the elements with roulette wheel
    ax.get_children()[6].set_color('tab:red')
    ax.get_children()[8].set_color('tab:red')
    ax.get_children()[10].set_color('tab:red')
    ax.get_children()[12].set_color('tab:red')
    ax.get_children()[14].set_color('tab:red')

    red_patch = mpatches.Patch(color='tab:red', label='Using Roulette Wheel')
    blue_patch = mpatches.Patch(color='tab:blue', label='Not Using Roulette Wheel')
    ax.legend(handles=[blue_patch, red_patch])

    plt.show()


if __name__ == '__main__':
    q_learning_connect4_execution_time()
