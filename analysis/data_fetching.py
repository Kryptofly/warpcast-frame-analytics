import requests
from config import WARPCAST_API_TOKEN, WARPCAST_API_ENDPOINT

def fetch_frames(username):
    url = f"{WARPCAST_API_ENDPOINT}/users/{username}/frames"
    headers = {
        'Authorization': f'Bearer {WARPCAST_API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    return response.json().get('data', [])

def fetch_engagement(frame_id):
    url = f"{WARPCAST_API_ENDPOINT}/frames/{frame_id}/engagement"
    headers = {
        'Authorization': f'Bearer {WARPCAST_API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    return response.json().get('data', [])
