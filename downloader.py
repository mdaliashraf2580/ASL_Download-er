import yt_dlp
import os

DOWNLOAD_FOLDER = "downloads"


def download_media(url):
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    options = {
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "format": "best",
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        return True

    except Exception as e:
        print("Download Error:", e)
        return False
