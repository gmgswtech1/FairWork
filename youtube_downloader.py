#!/usr/bin/env python3
"""Download a YouTube video the user is authorized to save."""

import argparse
from pathlib import Path
from urllib.parse import urlparse

import yt_dlp

YOUTUBE_HOSTS = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "music.youtube.com",
    "youtu.be",
}


def is_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and (parsed.hostname or "").lower() in YOUTUBE_HOSTS


def main() -> int:
    parser = argparse.ArgumentParser(description="Download a YouTube video you are allowed to save.")
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument("-o", "--output", default="downloads", help="Folder to save the video in (default: downloads)")
    args = parser.parse_args()

    url = args.url or input("YouTube URL: ").strip()
    if not is_youtube_url(url):
        parser.error("enter a valid YouTube URL (youtube.com or youtu.be)")

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    options = {
        "format": "best[ext=mp4]/best",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            downloader.download([url])
    except yt_dlp.utils.DownloadError as error:
        print(f"Download failed: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
