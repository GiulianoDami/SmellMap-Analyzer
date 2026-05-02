import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_striped_map(array, title="Striped Receptor Map"):
    """
    Plot a striped map visualization of receptor arrangements.
    
    Parameters:
    array (np.ndarray): 2D array representing receptor types in striped arrangement
    title (str): Title for the plot
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(array, cmap='viridis', cbar=True, xticklabels=False, yticklabels=False)
    plt.title(title)
    plt.xlabel('Receptor Position')
    plt.ylabel('Receptor Type')
    plt.tight_layout()
    plt.show()

def plot_distribution_heatmap(distribution_dict, title="Receptor Distribution Heatmap"):
    """
    Plot a heatmap showing distribution of receptor types.
    
    Parameters:
    distribution_dict (dict): Dictionary with receptor types as keys and counts as values
    title (str): Title for the plot
    """
    # Convert dict to DataFrame for easier plotting
    df = pd.DataFrame(list(distribution_dict.items()), columns=['Receptor Type', 'Count'])
    
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Receptor Type', y='Count')
    plt.title(title)
    plt.xlabel('Receptor Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()