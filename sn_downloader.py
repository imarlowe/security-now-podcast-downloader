import os
import requests

# Base URL for Security Now episodes
BASE_URL = "https://media.grc.com/sn/SN-{0:03d}.mp3"

# Directory inside Pythonista (this will show up in the Files app under "On My iPhone > Pythonista3")
SAVE_DIR = os.path.expanduser("~/Documents/SecurityNow")

# Ensure the directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

def download_episode(episode_number):
    url = BASE_URL.format(episode_number)
    file_path = os.path.join(SAVE_DIR, f"SN-{episode_number:03d}.mp3")

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"✅ Downloaded SN-{episode_number:03d}")
        else:
            print(f"❌ Episode {episode_number} not found (HTTP {response.status_code})")
    except Exception as e:
        print(f"❌ Error downloading episode {episode_number}: {e}")

def download_episodes(start_episode, count=10):
    for i in range(start_episode, start_episode + count):
        download_episode(i)

# Set starting episode number here
download_episodes(start_episode=257, count=10)  # Change episode # and count # as needed
