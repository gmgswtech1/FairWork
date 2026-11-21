# Simple YouTube downloader

A small command-line Python program that downloads a single YouTube video to a local folder using `yt-dlp`.

Only download videos you own or are otherwise authorized to save, and follow YouTube's terms and applicable copyright law. This tool does not bypass DRM or access controls.

## Setup

Python 3.9 or newer is recommended.

```bash
python -m pip install -r requirements.txt
```

## Use

Pass the video URL as an argument:

```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Or run without an argument to be prompted for a URL:

```bash
python youtube_downloader.py
```

Files are saved in `downloads/` by default. Choose another folder with `-o`:

```bash
python youtube_downloader.py "https://youtu.be/VIDEO_ID" --output videos
```
