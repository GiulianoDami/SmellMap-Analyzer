import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def analyze_receptor_distribution(array):
    """
    Analyze the distribution of receptor types in the given array.
    
    Parameters:
    array (numpy.ndarray): 2D array representing receptor distribution
    
    Returns:
    dict: Dictionary containing distribution statistics and visualization data
    """
    # Flatten the array to get all receptor values
    flattened = array.flatten()
    
    # Count occurrences of each receptor type
    unique, counts = np.unique(flattened, return_counts=True)
    
    # Calculate percentages
    total = len(flattened)
    percentages = (counts / total) * 100
    
    # Create summary statistics
    stats = {
        'total_receptors': total,
        'unique_types': len(unique),
        'distribution': dict(zip(unique, counts)),
        'percentages': dict(zip(unique, percentages))
    }
    
    return stats

def analyze_striped_organization(array):
    """
    Analyze the striped organization pattern in the receptor array.
    
    Parameters:
    array (numpy.ndarray): 2D array representing receptor distribution
    
    Returns:
    dict: Dictionary containing striped organization analysis results
    """
    if array.ndim != 2:
        raise ValueError("Array must be 2-dimensional")
    
    rows, cols = array.shape
    
    # Analyze horizontal stripes (row-wise patterns)
    row_patterns = []
    for i in range(rows):
        row = array[i, :]
        unique_elements, counts = np.unique(row, return_counts=True)
        row_patterns.append({
            'row_index': i,
            'pattern': dict(zip(unique_elements, counts))
        })
    
    # Analyze vertical stripes (column-wise patterns)
    col_patterns = []
    for j in range(cols):
        col = array[:, j]
        unique_elements, counts = np.unique(col, return_counts=True)
        col_patterns.append({
            'col_index': j,
            'pattern': dict(zip(unique_elements, counts))
        })
    
    # Calculate spatial correlation
    correlation_matrix = np.corrcoef(array.astype(float))
    
    # Identify dominant receptor types per row/column
    dominant_rows = [np.argmax(np.bincount(row)) for row in array]
    dominant_cols = [np.argmax(np.bincount(col)) for col in array.T]
    
    analysis_results = {
        'row_patterns': row_patterns,
        'col_patterns': col_patterns,
        'correlation_matrix': correlation_matrix,
        'dominant_row_types': dominant_rows,
        'dominant_col_types': dominant_cols
    }
    
    return analysis_results