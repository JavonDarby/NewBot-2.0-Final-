"""Visualization helpers for plotting trends and topic distributions."""

import matplotlib.pyplot as plt

def plot_topic_distribution(dist):
    plt.figure()
    plt.bar(range(len(dist)), dist)
    plt.show()
