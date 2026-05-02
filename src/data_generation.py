import numpy as np
import pandas as pd
from typing import List

def generate_striped_map(num_receptors: int, num_stripes: int, stripe_widths: List[float]) -> pd.DataFrame:
    """
    Generate a synthetic striped receptor map.
    
    Parameters:
    - num_receptors (int): Total number of receptors to generate
    - num_stripes (int): Number of stripes in the map
    - stripe_widths (list): Width of each stripe as a fraction of total map width
    
    Returns:
    - pd.DataFrame: DataFrame containing receptor positions and types
    """
    # Normalize stripe widths
    stripe_widths = np.array(stripe_widths)
    stripe_widths = stripe_widths / np.sum(stripe_widths)
    
    # Generate receptor types based on stripe assignments
    receptor_types = []
    cumulative_width = 0
    
    for i in range(num_stripes):
        start_pos = cumulative_width
        end_pos = cumulative_width + stripe_widths[i]
        
        # Assign receptors to this stripe
        num_in_stripe = int(num_receptors * stripe_widths[i])
        receptor_types.extend([i] * num_in_stripe)
        cumulative_width = end_pos
    
    # Fill any remaining receptors
    while len(receptor_types) < num_receptors:
        receptor_types.append(np.random.randint(0, num_stripes))
    
    # Shuffle receptor types
    np.random.shuffle(receptor_types)
    
    # Generate positions along the map
    positions = np.random.uniform(0, 1, num_receptors)
    
    # Create DataFrame
    df = pd.DataFrame({
        'position': positions,
        'receptor_type': receptor_types
    })
    
    return df