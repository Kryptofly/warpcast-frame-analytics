import pandas as pd
from collections import defaultdict

def analyze_engagement(frames):
    engagement_data = defaultdict(list)
    
    for frame in frames:
        frame_id = frame['id']
        frame_data = fetch_engagement(frame_id)
        engagement_data['frame_id'].append(frame_id)
        engagement_data['likes'].append(frame_data['likes'])
        engagement_data['comments'].append(frame_data['comments'])
        engagement_data['recasts'].append(frame_data['recasts'])
        engagement_data['timestamp'].append(frame['timestamp'])
    
    df = pd.DataFrame(engagement_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    return df
