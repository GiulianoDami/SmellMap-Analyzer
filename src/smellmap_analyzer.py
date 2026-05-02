import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from typing import List, Dict, Tuple, Any
import warnings
warnings.filterwarnings('ignore')

def generate_striped_map(n_rows: int, n_cols: int, receptor_types: List[str]) -> np.ndarray:
    """
    Generate a striped olfactory receptor map with alternating patterns.
    
    Args:
        n_rows: Number of rows in the map
        n_cols: Number of columns in the map
        receptor_types: List of receptor type names
        
    Returns:
        2D numpy array representing the striped map
    """
    # Create base grid
    map_grid = np.zeros((n_rows, n_cols), dtype=int)
    
    # Assign receptor types in stripes
    for i in range(n_rows):
        stripe_start = (i // 2) * 2  # Every 2 rows form a stripe
        stripe_end = stripe_start + 2
        if stripe_end <= n_cols:
            map_grid[i, stripe_start:stripe_end] = np.random.choice(len(receptor_types))
        else:
            # Handle edge case where stripe extends beyond column limit
            remaining_cols = n_cols - stripe_start
            map_grid[i, stripe_start:] = np.random.choice(len(receptor_types), remaining_cols)
    
    return map_grid

def visualize_map(map_array: np.ndarray, title: str, xlabel: str, ylabel: str = "Rows") -> None:
    """
    Visualize the olfactory receptor map using matplotlib.
    
    Args:
        map_array: 2D numpy array representing the map
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(map_array, cmap="tab10", cbar=True, xticklabels=False, yticklabels=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

def simulate_odor_profile(receptor_types: List[str]) -> Dict[str, float]:
    """
    Simulate an odor profile with varying intensities for different receptor types.
    
    Args:
        receptor_types: List of receptor type names
        
    Returns:
        Dictionary mapping receptor types to their simulated intensities
    """
    # Generate random intensities for each receptor type
    intensities = {rt: np.random.uniform(0.1, 1.0) for rt in receptor_types}
    return intensities

def process_odor_through_stripes(odor_profile: Dict[str, float]) -> Dict[str, float]:
    """
    Process odor through the striped receptor organization.
    
    Args:
        odor_profile: Dictionary mapping receptor types to intensities
        
    Returns:
        Processed odor profile after striped processing
    """
    # Apply a simple transformation to simulate processing through stripes
    processed = {}
    for receptor_type, intensity in odor_profile.items():
        # Simulate some filtering effect
        processed[receptor_type] = intensity * np.random.uniform(0.8, 1.2)
    return processed

def analyze_receptor_distribution(map_array: np.ndarray) -> Dict[int, int]:
    """
    Analyze the distribution of receptor types in the map.
    
    Args:
        map_array: 2D numpy array representing the map
        
    Returns:
        Dictionary mapping receptor type indices to counts
    """
    unique, counts = np.unique(map_array, return_counts=True)
    return dict(zip(unique, counts))

def plot_receptor_distribution(distribution: Dict[int, int]) -> None:
    """
    Plot the receptor type distribution.
    
    Args:
        distribution: Dictionary mapping receptor type indices to counts
    """
    plt.figure(figsize=(8, 5))
    types = list(distribution.keys())
    counts = list(distribution.values())
    
    bars = plt.bar(range(len(types)), counts, color=plt.cm.tab10(np.linspace(0, 1, len(types))))
    plt.xlabel("Receptor Type Index")
    plt.ylabel("Count")
    plt.title("Distribution of Receptor Types in Map")
    plt.xticks(range(len(types)), [f"Type {t}" for t in types])
    plt.tight_layout()
    plt.show()

def analyze_striped_organization(map_array: np.ndarray) -> Dict[str, Any]:
    """
    Analyze the striped organization properties of the map.
    
    Args:
        map_array: 2D numpy array representing the map
        
    Returns:
        Dictionary containing analysis results
    """
    rows, cols = map_array.shape
    analysis = {
        "dimensions": (rows, cols),
        "total_cells": rows * cols,
        "unique_types": len(np.unique(map_array)),
        "striping_pattern": "alternating_rows"
    }
    
    # Check for stripe consistency
    stripe_consistency = []
    for i in range(0, rows, 2):
        if i + 1 < rows:
            stripe1 = set(map_array[i])
            stripe2 = set(map_array[i+1])
            stripe_consistency.append(len(stripe1.intersection(stripe2)) == 0)
    
    analysis["stripe_consistency"] = np.mean(stripe_consistency) if stripe_consistency else 0
    return analysis