import os
from dotenv import load_dotenv

load_dotenv()

WARPCAST_API_TOKEN = os.getenv('WARPCAST_API_TOKEN')
WARPCAST_API_ENDPOINT = "https://api.warpcast.com"  # Replace with the actual endpoint
