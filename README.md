# Security Now Podcast Downloader

This Python script automates the process of downloading archived episodes of the GRC *Security Now* podcast. The script was created with the help of ChatGPT, which generated the code based on my input and feedback. I guided the process by refining the prompts to ensure the script met my specific needs. The project demonstrates practical problem-solving using automation tools and publicly available archives.

## Problem

Manually downloading each archive podcast episode individually was time-consuming and inefficient—especially when listening to multiple episodes per day.

## Solution

This script automates the process by fetching episodes directly from the GRC *Security Now* podcast archive. To avoid putting unnecessary load on the server, it downloads up to 10 episodes per run. The episodes are saved locally and can be played using any compatible media player.

## Features

- Automatically downloads episodes of the *Security Now* podcast using a predictable URL structure.
- Limits downloads to 10 episodes at a time to reduce server impact.
- Designed and tested for use with Pythonista on iOS.

## How to Use

This script was developed and tested using [Pythonista *not a sponsor*], Python IDE for iOS. The following steps describe how to run the script in that environment:

1. **Install Pythonista** from the App Store on your iPhone or iPad.
2. **Download this script** (e.g., `download_podcasts.py`) from this GitHub repository. [code can also be simply copy and pasted into a new Pythonista file and empty script
3. **Open the script in Pythonista.**
4. **Edit the episode number range** in the script (if needed) to specify which episodes you'd like to download.
5. **Run the script.** Episodes will be saved in Pythonista's local file storage.
6. **Move the files manually** (if desired) into the Files app or another folder for playback.

> **Note:** Although this script was created for Pythonista, it uses only standard Python libraries and may also work in other environments (such as desktop Python installations) with minor adjustments—particularly to file paths and download directories.

## Recommended Playback

While the downloaded `.mp3` files can be played using any audio app, I recommend **VLC Media Player** for its features:

- Remembers where playback left off
- Allows skip-forward and rewind gestures via tapping the screen
- Plays audio files consecutively without manual input
- Has a folder in 'Files' App which allows moving audio files from Python program.

These features improve the experience, especially when listening to older episodes that contain unskippable ads.

## Requirements

- Python 3.x
- Internet connection
- Optional: Pythonista ($9.99 iOS app) or another Python environment
- Optional: VLC Media Player (for playback)

## Acknowledgments

The script was fully generated using ChatGPT. I contributed by crafting and refining the prompts, testing the code, and guiding the functionality based on my specific use case. This project showcases my ability to identify inefficiencies, leverage automation tools, and communicate clearly with AI to create effective solutions.

## Future Improvements

- Create a version for desktop use with enhanced file management.
- Add support for automated metadata tagging for skipping by 10, 15, 30 second increments.
- Explore creating a GUI or user interface for non-technical users.
