import pandas as pd
import numpy as np
def create_features(df:pd.DataFrame)->pd.DataFrame: #Convert processed data into model-ready numerical features.
    features = pd.DataFrame()
    for col in df.columns:
        features[f"{col}_mean"]=df[col].rolling(window=5).mean()
        features[f"{col}_std"]=df[col].rolling(window=5).std()
    features=features.dropna()
    return features