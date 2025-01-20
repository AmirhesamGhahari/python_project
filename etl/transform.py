import pandas as pd

def transform_data(raw_data):
    # Convert to DataFrame for manipulation
    df = pd.DataFrame(raw_data)

    # Example transformations
    df['value'] = df['value'].astype(float)  # Ensure numeric data type
    df['timestamp'] = pd.Timestamp.now()    # Add a timestamp
    return df