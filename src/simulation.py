import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def simulate_odor_profile(receptor_types):
    """
    Simulate an odor profile based on receptor types.
    
    Args:
        receptor_types (list): List of receptor type identifiers
        
    Returns:
        dict: Dictionary with receptor types as keys and activation levels as values
    """
    # Generate random activation levels for each receptor type
    activation_levels = {}
    for receptor_type in receptor_types:
        # Activation level between 0.1 and 1.0
        activation_levels[receptor_type] = np.random.uniform(0.1, 1.0)
    
    return activation_levels

def process_odor_through_stripes(odor_profile):
    """
    Process odor profile through striped receptor pathways.
    
    Args:
        odor_profile (dict): Dictionary with receptor types as keys and activation levels as values
        
    Returns:
        dict: Processed odor information with stripe-based organization
    """
    # Define stripe patterns (simplified representation)
    stripes = {
        'stripe_1': ['OR1', 'OR2', 'OR3'],
        'stripe_2': ['OR4', 'OR5', 'OR6'],
        'stripe_3': ['OR7', 'OR8', 'OR9'],
        'stripe_4': ['OR10', 'OR11', 'OR12']
    }
    
    # Initialize processed data
    processed_data = {
        'receptor_activations': odor_profile,
        'stripe_activations': {},
        'total_activation': sum(odor_profile.values())
    }
    
    # Calculate stripe activations based on receptor activations
    for stripe_name, receptor_list in stripes.items():
        stripe_activation = 0
        for receptor in receptor_list:
            if receptor in odor_profile:
                stripe_activation += odor_profile[receptor]
        processed_data['stripe_activations'][stripe_name] = stripe_activation
    
    return processed_data